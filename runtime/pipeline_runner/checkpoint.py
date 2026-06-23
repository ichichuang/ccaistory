from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from core.io import RUNTIME_ROOT, result
from pipeline_runner.pipeline_errors import PipelineCheckpointError


RUNS_ROOT = RUNTIME_ROOT / ".runs"

STEP_STATUSES = {
    "pending",
    "running",
    "passed",
    "failed",
    "blocked",
    "waiting_for_manual_approval",
    "waiting_for_external_generation",
}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _run_dir(run_id: str) -> Path:
    return RUNS_ROOT / run_id


def checkpoint_path(run_id: str) -> Path:
    return _run_dir(run_id) / "checkpoint.json"


def create_checkpoint(
    run_id: str,
    project_path: str,
    steps: list[dict[str, Any]],
    next_action: str = "",
) -> dict[str, Any]:
    now = _now()
    return {
        "run_id": run_id,
        "project_path": project_path,
        "started_at": now,
        "updated_at": now,
        "current_step": steps[0]["step_id"] if steps else None,
        "steps": [
            {
                "step_id": step["step_id"],
                "action_id": step["action_id"],
                "gate": step.get("gate", ""),
                "status": "pending",
                "manual_approval_required": bool(step.get("manual_approval_required")),
            }
            for step in steps
        ],
        "last_error": None,
        "next_action": next_action,
    }


def save_checkpoint(checkpoint: dict[str, Any]) -> Path:
    run_id = checkpoint.get("run_id")
    if not isinstance(run_id, str) or not run_id:
        raise PipelineCheckpointError("checkpoint.run_id is required")
    checkpoint["updated_at"] = _now()
    path = checkpoint_path(run_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(checkpoint, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    return path


def load_checkpoint(run_id: str) -> dict[str, Any]:
    path = checkpoint_path(run_id)
    if not path.exists():
        raise PipelineCheckpointError(f"checkpoint not found: runtime/.runs/{run_id}/checkpoint.json")
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise PipelineCheckpointError(f"checkpoint root must be object: runtime/.runs/{run_id}/checkpoint.json")
    return data


def mark_step_status(
    checkpoint: dict[str, Any],
    step_id: str,
    status: str,
    last_error: str | None = None,
) -> dict[str, Any]:
    if status not in STEP_STATUSES:
        raise PipelineCheckpointError(f"unknown checkpoint step status: {status}")
    found = False
    for step in checkpoint.get("steps", []):
        if step.get("step_id") == step_id:
            step["status"] = status
            checkpoint["current_step"] = step_id
            found = True
            break
    if not found:
        raise PipelineCheckpointError(f"checkpoint step not found: {step_id}")
    checkpoint["last_error"] = last_error
    checkpoint["updated_at"] = _now()
    return checkpoint


def read_checkpoint_status(run_id: str) -> dict[str, Any]:
    try:
        checkpoint = load_checkpoint(run_id)
    except PipelineCheckpointError as exc:
        return result(False, run_id=run_id, blocked_reason=[str(exc)])
    return result(True, run_id=run_id, checkpoint=checkpoint)
