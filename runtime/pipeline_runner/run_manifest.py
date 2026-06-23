from __future__ import annotations

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from contracts.contract_loader import ContractError, load_contract
from core.io import RUNTIME_ROOT, result
from pipeline_runner.checkpoint import RUNS_ROOT


CONTRACT_NAMES = ["pipeline_actions", "state_machine", "quality_gates"]


def _now_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")


def create_run_id() -> str:
    return f"run_{_now_compact()}_{uuid.uuid4().hex[:8]}"


def _run_dir(run_id: str) -> Path:
    return RUNS_ROOT / run_id


def manifest_path(run_id: str) -> Path:
    return _run_dir(run_id) / "run_manifest.json"


def _contract_versions() -> dict[str, Any]:
    versions: dict[str, Any] = {}
    for name in CONTRACT_NAMES:
        contract = load_contract(name)
        versions[name] = contract.get("version")
    return versions


def create_run_manifest(
    *,
    project_path: str,
    requested_until: str,
    command: str,
    dry_run: bool,
    plan_result: dict[str, Any],
) -> dict[str, Any]:
    run_id = create_run_id()
    run_dir = _run_dir(run_id)
    run_dir.mkdir(parents=True, exist_ok=True)

    try:
        contract_versions = _contract_versions()
    except ContractError as exc:
        contract_versions = {"error": str(exc)}

    plan = plan_result.get("plan", [])
    manual_points = [
        step["step_id"]
        for step in plan
        if isinstance(step, dict) and step.get("manual_approval_required")
    ]
    blocked_actions_seen = [
        reason
        for reason in plan_result.get("blocked_reason", [])
        if isinstance(reason, str) and reason
    ]
    manifest = {
        "run_id": run_id,
        "project_path": project_path,
        "requested_until": requested_until,
        "contract_versions": contract_versions,
        "command": command,
        "dry_run": dry_run,
        "created_artifacts": [
            f"runtime/.runs/{run_id}/run_manifest.json",
            f"runtime/.runs/{run_id}/checkpoint.json",
        ],
        "manual_approval_points": manual_points,
        "blocked_actions_seen": blocked_actions_seen,
    }
    manifest_path(run_id).write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    return manifest


def load_manifest(run_id: str) -> dict[str, Any]:
    path = manifest_path(run_id)
    if not path.exists():
        raise FileNotFoundError(f"run manifest not found: runtime/.runs/{run_id}/run_manifest.json")
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"run manifest root must be object: runtime/.runs/{run_id}/run_manifest.json")
    return data


def list_runs() -> dict[str, Any]:
    runs: list[dict[str, Any]] = []
    if RUNS_ROOT.exists():
        for path in sorted(RUNS_ROOT.iterdir()):
            if not path.is_dir():
                continue
            manifest_file = path / "run_manifest.json"
            checkpoint_file = path / "checkpoint.json"
            if not manifest_file.exists():
                continue
            with manifest_file.open("r", encoding="utf-8") as handle:
                manifest = json.load(handle)
            if not isinstance(manifest, dict):
                continue
            runs.append(
                {
                    "run_id": manifest.get("run_id", path.name),
                    "project_path": manifest.get("project_path", ""),
                    "requested_until": manifest.get("requested_until", ""),
                    "dry_run": manifest.get("dry_run", True),
                    "has_checkpoint": checkpoint_file.exists(),
                }
            )
    return result(True, run_count=len(runs), runs=runs)
