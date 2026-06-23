from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from artifact_registry.hash_utils import json_sha256
from core.io import read_json, result


def _now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def create_telemetry_record(**payload: Any) -> dict[str, Any]:
    return {
        "execution_telemetry": {
            "asset_id": payload.get("asset_id"),
            "asset_type": payload.get("asset_type"),
            "actual_prompt_sent_to_external_tool": payload.get("actual_prompt_sent_to_external_tool"),
            "reference_assets_required": payload.get("reference_assets_required", []),
            "reference_assets_uploaded_or_available": payload.get("reference_assets_uploaded_or_available", []),
            "canvas_ratio_requested": payload.get("canvas_ratio_requested"),
            "canvas_ratio_actual": payload.get("canvas_ratio_actual"),
            "tool_name": payload.get("tool_name"),
            "output_path": payload.get("output_path"),
        }
    }


def validate_telemetry(record: dict[str, Any]) -> dict[str, Any]:
    telemetry = record.get("execution_telemetry", record)
    failed: list[str] = []
    if not telemetry.get("actual_prompt_sent_to_external_tool"):
        failed.append("missing_actual_prompt_sent_to_external_tool")

    required = set(telemetry.get("reference_assets_required", []) or [])
    available = set(telemetry.get("reference_assets_uploaded_or_available", []) or [])
    missing_refs = sorted(required - available)
    if missing_refs:
        failed.append("reference_assets_missing")

    requested = telemetry.get("canvas_ratio_requested")
    actual = telemetry.get("canvas_ratio_actual")
    if requested and actual and requested != actual:
        failed.append("canvas_ratio_mismatch")
    elif requested and not actual:
        failed.append("missing_canvas_ratio_actual")

    passed = not failed
    return result(
        passed,
        execution_telemetry={
            "failed_rules": failed,
            "missing_reference_assets": missing_refs,
            "allow_accepted_review": passed,
        },
    )


def validate_telemetry_file(path: str) -> dict[str, Any]:
    return validate_telemetry(read_json(path))


def create_telemetry_artifact_payload(
    record: dict[str, Any],
    *,
    artifact_id: str,
    project_id: str = "",
    story_id: str = "",
    run_id: str = "",
    candidate_id: str = "",
    parent_artifact_ids: list[str] | None = None,
    dependency_artifact_ids: list[str] | None = None,
) -> dict[str, Any]:
    validation = validate_telemetry(record)
    if not validation["passed"]:
        return result(False, failures=["telemetry_validation_failed"], telemetry_validation=validation)

    telemetry = record.get("execution_telemetry", record)
    content_hash = json_sha256(record)
    if not content_hash.get("hash"):
        return result(False, failures=content_hash.get("failures", ["telemetry_hash_failed"]))

    artifact = {
        "artifact_id": artifact_id,
        "artifact_type": "execution_telemetry",
        "project_id": project_id,
        "story_id": story_id,
        "asset_id": telemetry.get("asset_id") or "",
        "run_id": run_id,
        "candidate_id": candidate_id,
        "source_path": "",
        "content_hash": content_hash,
        "source_hash": content_hash,
        "parent_artifact_ids": parent_artifact_ids or [],
        "dependency_artifact_ids": dependency_artifact_ids or [],
        "created_at": _now(),
        "status": "telemetry_recorded",
        "metadata": {
            "actual_prompt_sent_to_external_tool": telemetry.get("actual_prompt_sent_to_external_tool", ""),
            "tool_name": telemetry.get("tool_name", ""),
            "output_path": telemetry.get("output_path", ""),
            "canvas_ratio_requested": telemetry.get("canvas_ratio_requested", ""),
            "canvas_ratio_actual": telemetry.get("canvas_ratio_actual", ""),
        },
    }
    return result(True, artifact=artifact, telemetry_validation=validation)
