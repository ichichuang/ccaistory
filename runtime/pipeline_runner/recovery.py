from __future__ import annotations

from typing import Any

from core.io import result
from pipeline_runner.checkpoint import load_checkpoint
from pipeline_runner.pipeline_errors import PipelineCheckpointError


def _current_step(checkpoint: dict[str, Any]) -> dict[str, Any] | None:
    current_step = checkpoint.get("current_step")
    for step in checkpoint.get("steps", []):
        if isinstance(step, dict) and step.get("step_id") == current_step:
            return step
    return None


def resume_run(run_id: str, dry_run: bool = True) -> dict[str, Any]:
    try:
        checkpoint = load_checkpoint(run_id)
    except PipelineCheckpointError as exc:
        return result(False, run_id=run_id, resume_status="missing_checkpoint", blocked_reason=[str(exc)])

    failed_steps = [
        step for step in checkpoint.get("steps", []) if isinstance(step, dict) and step.get("status") == "failed"
    ]
    if failed_steps:
        return result(
            True,
            run_id=run_id,
            dry_run=dry_run,
            resume_status="repair_required",
            current_step=failed_steps[-1].get("step_id"),
            checkpoint=checkpoint,
        )

    current = _current_step(checkpoint)
    if current and current.get("status") == "waiting_for_manual_approval":
        return result(
            True,
            run_id=run_id,
            dry_run=dry_run,
            resume_status="approval_required",
            current_step=current.get("step_id"),
            checkpoint=checkpoint,
        )
    if current and current.get("status") == "waiting_for_external_generation":
        return result(
            True,
            run_id=run_id,
            dry_run=dry_run,
            resume_status="external_generation_required",
            current_step=current.get("step_id"),
            checkpoint=checkpoint,
        )

    if checkpoint.get("last_error"):
        return result(
            True,
            run_id=run_id,
            dry_run=dry_run,
            resume_status="repair_required",
            current_step=checkpoint.get("current_step"),
            checkpoint=checkpoint,
        )

    pending_steps = [
        step
        for step in checkpoint.get("steps", [])
        if isinstance(step, dict) and step.get("status") in {"pending", "running", "blocked"}
    ]
    if pending_steps:
        return result(
            True,
            run_id=run_id,
            dry_run=dry_run,
            resume_status="resume_available",
            current_step=pending_steps[0].get("step_id"),
            checkpoint=checkpoint,
        )

    return result(
        True,
        run_id=run_id,
        dry_run=dry_run,
        resume_status="complete",
        current_step=checkpoint.get("current_step"),
        checkpoint=checkpoint,
    )
