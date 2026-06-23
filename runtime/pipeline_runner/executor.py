from __future__ import annotations

from typing import Any

from artifact_registry.registry import register_artifact, validate_artifact_by_id
from contracts.validate_contracts import validate_contracts
from core.io import find_story_core, load_json_file, result
from pipeline_runner.checkpoint import create_checkpoint, mark_step_status, save_checkpoint
from pipeline_runner.pipeline_errors import PipelineCheckpointError
from pipeline_runner.run_manifest import append_created_artifact_ids, create_run_manifest
from story_analyzer.analyzer import analyze_story_core, analyze_story_graph


EXTERNAL_GENERATION_ACTIONS = {"generate_source_pilot_task_list"}
EXTERNAL_REQUIRED_ARTIFACTS = [
    "external_generation_candidate",
    "execution_telemetry",
    "image_review_form",
    "image_review_validation_result",
    "asset_qa_result",
]
ACCEPTANCE_ACTIONS = {"accept_asset", "reject_asset"}
SKILL_EXECUTOR_DRY_RUN_ACTIONS = {"execute_skill_node", "execute_skill_graph"}
SKILL_EXECUTOR_APPROVAL_ACTIONS = {"review_skill_executor_proposed_changes", "apply_approved_skill_changes"}
ANALYZER_ACTIONS = {"analyze_story_graph"}


def _acceptance_inputs_present(step: dict[str, Any]) -> bool:
    required = set(step.get("required_inputs", []))
    return {"execution_telemetry", "image_review_validation_result", "asset_qa_result"}.issubset(required)


def _register_step_artifacts(step: dict[str, Any], *, dry_run: bool) -> dict[str, Any]:
    payloads = step.get("artifact_payloads", [])
    if payloads in (None, []):
        return result(True, artifact_ids=[])
    if not isinstance(payloads, list) or not all(isinstance(item, dict) for item in payloads):
        return result(False, failures=["artifact_payloads_not_list"])

    artifact_ids: list[str] = []
    for artifact in payloads:
        registration = register_artifact(artifact, dry_run=dry_run)
        if not registration["passed"]:
            return result(False, failures=registration.get("failures", []), artifact_registration=registration)
        artifact_ids.append(registration["artifact_id"])
    return result(True, artifact_ids=artifact_ids)


def _validate_acceptance_artifact(step: dict[str, Any]) -> dict[str, Any]:
    artifact_id = step.get("artifact_id") or step.get("accepted_artifact_id")
    if not artifact_id:
        return result(True, artifact_id="")
    if not isinstance(artifact_id, str):
        return result(False, failures=["acceptance_artifact_id_not_string"])
    validation = validate_artifact_by_id(artifact_id)
    if not validation["passed"]:
        return validation
    return result(True, artifact_id=artifact_id)


def _analyze_project_story(plan_result: dict[str, Any], project_path: str) -> dict[str, Any]:
    story_path = plan_result.get("story_core_path")
    if not story_path:
        resolved = find_story_core(project_path)
        story_path = str(resolved) if resolved is not None else ""
    if not story_path:
        return {
            "passed": False,
            "next_action": "repair_story_graph_before_skill_executor",
            "repair_priority": [{"source": "pipeline_runner", "risk_level": "high", "issue": "story_core_missing"}],
        }
    resolved_path = find_story_core(story_path)
    if resolved_path is None:
        return {
            "passed": False,
            "next_action": "repair_story_graph_before_skill_executor",
            "repair_priority": [{"source": "pipeline_runner", "risk_level": "high", "issue": "story_payload_missing"}],
        }
    payload = load_json_file(resolved_path)
    if not isinstance(payload, dict):
        return {
            "passed": False,
            "next_action": "repair_story_graph_before_skill_executor",
            "repair_priority": [{"source": "pipeline_runner", "risk_level": "high", "issue": "story_payload_not_object"}],
        }
    if isinstance(payload.get("story_graph"), dict):
        return analyze_story_core(payload)
    return analyze_story_graph(payload)


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

            if action_id in ACCEPTANCE_ACTIONS:
                artifact_validation = _validate_acceptance_artifact(step)
                if not artifact_validation["passed"]:
                    mark_step_status(checkpoint, step_id, "failed", "acceptance_artifact_registry_validation_failed")
                    save_checkpoint(checkpoint)
                    return result(
                        False,
                        run_result={
                            "run_id": manifest["run_id"],
                            "run_status": "failed",
                            "dry_run": dry_run,
                            "stopped_at": step_id,
                            "last_error": "acceptance_artifact_registry_validation_failed",
                            "executed_steps": executed_steps,
                            "artifact_validation": artifact_validation,
                            "run_manifest": f"runtime/.runs/{manifest['run_id']}/run_manifest.json",
                            "checkpoint": f"runtime/.runs/{manifest['run_id']}/checkpoint.json",
                        },
                    )

            if action_id in SKILL_EXECUTOR_DRY_RUN_ACTIONS and not dry_run:
                mark_step_status(checkpoint, step_id, "failed", "skill_executor_requires_dry_run")
                save_checkpoint(checkpoint)
                return result(
                    False,
                    run_result={
                        "run_id": manifest["run_id"],
                        "run_status": "failed",
                        "dry_run": dry_run,
                        "stopped_at": step_id,
                        "last_error": "skill_executor_requires_dry_run",
                        "executed_steps": executed_steps,
                        "run_manifest": f"runtime/.runs/{manifest['run_id']}/run_manifest.json",
                        "checkpoint": f"runtime/.runs/{manifest['run_id']}/checkpoint.json",
                    },
                )

            if action_id in ANALYZER_ACTIONS:
                analysis_result = _analyze_project_story(plan_result, project_path)
                if not analysis_result.get("passed"):
                    mark_step_status(checkpoint, step_id, "failed", "story_analyzer_high_risk")
                    checkpoint["next_action"] = analysis_result.get(
                        "next_action",
                        "repair_story_graph_before_skill_executor",
                    )
                    save_checkpoint(checkpoint)
                    return result(
                        False,
                        run_result={
                            "run_id": manifest["run_id"],
                            "run_status": "blocked",
                            "dry_run": dry_run,
                            "stopped_at": step_id,
                            "last_error": "story_analyzer_high_risk",
                            "next_action": checkpoint["next_action"],
                            "executed_steps": executed_steps,
                            "story_analysis_result": analysis_result,
                            "run_manifest": f"runtime/.runs/{manifest['run_id']}/run_manifest.json",
                            "checkpoint": f"runtime/.runs/{manifest['run_id']}/checkpoint.json",
                        },
                    )

            if action_id in SKILL_EXECUTOR_APPROVAL_ACTIONS and not step.get("manual_approval_required"):
                mark_step_status(checkpoint, step_id, "failed", "skill_executor_approval_action_not_manual")
                save_checkpoint(checkpoint)
                return result(
                    False,
                    run_result={
                        "run_id": manifest["run_id"],
                        "run_status": "failed",
                        "dry_run": dry_run,
                        "stopped_at": step_id,
                        "last_error": "skill_executor_approval_action_not_manual",
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
                        "required_artifacts_after_external_generation": EXTERNAL_REQUIRED_ARTIFACTS,
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

            artifact_registration = _register_step_artifacts(step, dry_run=dry_run)
            if not artifact_registration["passed"]:
                mark_step_status(checkpoint, step_id, "failed", "artifact_registration_failed")
                save_checkpoint(checkpoint)
                return result(
                    False,
                    run_result={
                        "run_id": manifest["run_id"],
                        "run_status": "failed",
                        "dry_run": dry_run,
                        "stopped_at": step_id,
                        "last_error": "artifact_registration_failed",
                        "artifact_registration": artifact_registration,
                        "executed_steps": executed_steps,
                        "run_manifest": f"runtime/.runs/{manifest['run_id']}/run_manifest.json",
                        "checkpoint": f"runtime/.runs/{manifest['run_id']}/checkpoint.json",
                    },
                )
            if artifact_registration["artifact_ids"]:
                append_created_artifact_ids(manifest["run_id"], artifact_registration["artifact_ids"])

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
