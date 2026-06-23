from __future__ import annotations

from typing import Any

from contracts.validate_contracts import validate_contracts
from core.io import result
from pipeline_runner.checkpoint import create_checkpoint, mark_step_status, save_checkpoint
from pipeline_runner.pipeline_errors import PipelineCheckpointError
from pipeline_runner.run_manifest import create_run_manifest


EXTERNAL_GENERATION_ACTIONS = {"generate_source_pilot_task_list"}
ACCEPTANCE_ACTIONS = {"accept_asset", "reject_asset"}


def _acceptance_inputs_present(step: dict[str, Any]) -> bool:
    required = set(step.get("required_inputs", []))
    return {"execution_telemetry", "asset_qa_result"}.issubset(required)


def execute_pipeline(
    plan_result: dict[str, Any],
    *,
    project_path: str = "",
    requested_until: str = "",
    dry_run: bool = True,
    command: str = "",
) -> dict[str, Any]:
    plan = plan_result.get("plan", [])
    if not isinstance(plan, list):
        return result(False, run_result={"run_status": "failed", "last_error": "plan_not_list"})

    manifest = create_run_manifest(
        project_path=project_path,
        requested_until=requested_until,
        command=command,
        dry_run=dry_run,
        plan_result=plan_result,
    )
    checkpoint = create_checkpoint(
        manifest["run_id"],
        project_path,
        plan,
        next_action=plan_result.get("next_allowed_action", ""),
    )

    contract_validation = validate_contracts()
    if not contract_validation["passed"]:
        checkpoint["last_error"] = "contracts_invalid"
        save_checkpoint(checkpoint)
        return result(
            False,
            run_result={
                "run_id": manifest["run_id"],
                "run_status": "failed",
                "dry_run": dry_run,
                "run_manifest": f"runtime/.runs/{manifest['run_id']}/run_manifest.json",
                "checkpoint": f"runtime/.runs/{manifest['run_id']}/checkpoint.json",
                "last_error": "contracts_invalid",
                "dry_run_checks": {"validate_contracts": contract_validation},
            },
        )

    if not plan_result.get("passed", False):
        checkpoint["last_error"] = ";".join(plan_result.get("blocked_reason", [])) or "plan_failed"
        checkpoint["next_action"] = plan_result.get("next_allowed_action", "")
        save_checkpoint(checkpoint)
        return result(
            False,
            run_result={
                "run_id": manifest["run_id"],
                "run_status": "blocked",
                "dry_run": dry_run,
                "run_manifest": f"runtime/.runs/{manifest['run_id']}/run_manifest.json",
                "checkpoint": f"runtime/.runs/{manifest['run_id']}/checkpoint.json",
                "last_error": checkpoint["last_error"],
                "dry_run_checks": {"validate_contracts": contract_validation},
            },
        )

    if not plan:
        save_checkpoint(checkpoint)
        return result(
            True,
            run_result={
                "run_id": manifest["run_id"],
                "run_status": "empty_state_plan",
                "dry_run": dry_run,
                "executed_steps": [],
                "run_manifest": f"runtime/.runs/{manifest['run_id']}/run_manifest.json",
                "checkpoint": f"runtime/.runs/{manifest['run_id']}/checkpoint.json",
                "dry_run_checks": {"validate_contracts": contract_validation},
            },
        )

    executed_steps: list[str] = []
    try:
        for step in plan:
            step_id = step["step_id"]
            action_id = step["action_id"]
            mark_step_status(checkpoint, step_id, "running")
            save_checkpoint(checkpoint)

            if action_id in ACCEPTANCE_ACTIONS and not _acceptance_inputs_present(step):
                mark_step_status(checkpoint, step_id, "failed", "acceptance_requires_telemetry_and_qa")
                save_checkpoint(checkpoint)
                return result(
                    False,
                    run_result={
                        "run_id": manifest["run_id"],
                        "run_status": "failed",
                        "dry_run": dry_run,
                        "stopped_at": step_id,
                        "last_error": "acceptance_requires_telemetry_and_qa",
                        "executed_steps": executed_steps,
                        "run_manifest": f"runtime/.runs/{manifest['run_id']}/run_manifest.json",
                        "checkpoint": f"runtime/.runs/{manifest['run_id']}/checkpoint.json",
                    },
                )

            if action_id in EXTERNAL_GENERATION_ACTIONS:
                mark_step_status(checkpoint, step_id, "waiting_for_external_generation")
                save_checkpoint(checkpoint)
                return result(
                    True,
                    run_result={
                        "run_id": manifest["run_id"],
                        "run_status": "waiting_for_external_generation",
                        "dry_run": dry_run,
                        "stopped_at": step_id,
                        "executed_steps": executed_steps,
                        "run_manifest": f"runtime/.runs/{manifest['run_id']}/run_manifest.json",
                        "checkpoint": f"runtime/.runs/{manifest['run_id']}/checkpoint.json",
                    },
                )

            if step.get("manual_approval_required"):
                mark_step_status(checkpoint, step_id, "waiting_for_manual_approval")
                save_checkpoint(checkpoint)
                return result(
                    True,
                    run_result={
                        "run_id": manifest["run_id"],
                        "run_status": "waiting_for_manual_approval",
                        "dry_run": dry_run,
                        "stopped_at": step_id,
                        "executed_steps": executed_steps,
                        "run_manifest": f"runtime/.runs/{manifest['run_id']}/run_manifest.json",
                        "checkpoint": f"runtime/.runs/{manifest['run_id']}/checkpoint.json",
                    },
                )

            mark_step_status(checkpoint, step_id, "passed")
            save_checkpoint(checkpoint)
            executed_steps.append(step_id)
    except (KeyError, PipelineCheckpointError) as exc:
        checkpoint["last_error"] = str(exc)
        save_checkpoint(checkpoint)
        return result(
            False,
            run_result={
                "run_id": manifest["run_id"],
                "run_status": "failed",
                "dry_run": dry_run,
                "last_error": str(exc),
                "executed_steps": executed_steps,
                "run_manifest": f"runtime/.runs/{manifest['run_id']}/run_manifest.json",
                "checkpoint": f"runtime/.runs/{manifest['run_id']}/checkpoint.json",
            },
        )

    return result(
        True,
        run_result={
            "run_id": manifest["run_id"],
            "run_status": "completed",
            "dry_run": dry_run,
            "executed_steps": executed_steps,
            "run_manifest": f"runtime/.runs/{manifest['run_id']}/run_manifest.json",
            "checkpoint": f"runtime/.runs/{manifest['run_id']}/checkpoint.json",
            "dry_run_checks": {"validate_contracts": contract_validation},
        },
    )
