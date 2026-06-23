from __future__ import annotations

from copy import deepcopy
from typing import Any

from artifact_registry.hash_utils import json_sha256
from artifact_registry.registry import load_registry, register_artifact
from core.io import read_json, result
from multimodal_qa.image_review_schema import utc_now
from multimodal_qa.qa_merge import merge_image_review_to_asset_qa


def _artifact_items(registry: dict[str, Any]) -> dict[str, dict[str, Any]]:
    artifacts = registry.get("artifacts", {})
    if not isinstance(artifacts, dict):
        return {}
    return {key: value for key, value in artifacts.items() if isinstance(value, dict)}


def _find_telemetry_artifact(
    artifacts: dict[str, dict[str, Any]],
    *,
    candidate_artifact_id: str,
    candidate_id: str,
    asset_id: str,
) -> dict[str, Any] | None:
    for artifact in artifacts.values():
        if artifact.get("artifact_type") != "execution_telemetry":
            continue
        linked_ids = [*artifact.get("parent_artifact_ids", []), *artifact.get("dependency_artifact_ids", [])]
        if candidate_artifact_id in linked_ids:
            return artifact
        if candidate_id and artifact.get("candidate_id") == candidate_id and artifact.get("asset_id") == asset_id:
            return artifact
    return None


def _qa_status(asset_qa_result: dict[str, Any]) -> str:
    if asset_qa_result.get("allow_accepted") is True and asset_qa_result.get("decision") == "accepted":
        return "qa_passed"
    if asset_qa_result.get("manual_decision") == "fail":
        return "qa_failed"
    return "qa_pending"


def create_image_qa_artifact_payload(
    review_form: dict[str, Any],
    *,
    registry_path: str | None = None,
    source_path: str = "",
) -> dict[str, Any]:
    registry = load_registry(registry_path)
    artifacts = _artifact_items(registry)
    candidate_artifact_id = str(review_form.get("artifact_id", ""))
    candidate_artifact = artifacts.get(candidate_artifact_id)
    if not candidate_artifact or candidate_artifact.get("artifact_type") != "external_generation_candidate":
        return result(False, failures=["candidate_artifact_not_found"], artifact_id=candidate_artifact_id)

    telemetry_artifact = _find_telemetry_artifact(
        artifacts,
        candidate_artifact_id=candidate_artifact_id,
        candidate_id=str(review_form.get("candidate_id", "")),
        asset_id=str(review_form.get("asset_id", "")),
    )
    if telemetry_artifact is None:
        return result(False, failures=["telemetry_artifact_not_found"], artifact_id=candidate_artifact_id)

    merge_result = merge_image_review_to_asset_qa(review_form)
    asset_qa_result = merge_result["asset_qa_result"]
    payload_hash = json_sha256({"image_review_form": review_form, "asset_qa_result": asset_qa_result})
    if not payload_hash.get("hash"):
        return result(False, failures=payload_hash.get("failures", ["image_qa_payload_hash_failed"]))

    review_id = str(review_form.get("review_id", "")) or "image_review"
    artifact_id = f"{review_id}_asset_qa_result"
    dependency_ids = list(
        dict.fromkeys(
            [
                candidate_artifact_id,
                str(telemetry_artifact.get("artifact_id", "")),
            ]
        )
    )
    artifact = {
        "artifact_id": artifact_id,
        "artifact_type": "asset_qa_result",
        "project_id": candidate_artifact.get("project_id", ""),
        "story_id": candidate_artifact.get("story_id", ""),
        "asset_id": review_form.get("asset_id", ""),
        "run_id": candidate_artifact.get("run_id", ""),
        "candidate_id": review_form.get("candidate_id", ""),
        "source_path": source_path,
        "content_hash": payload_hash,
        "source_hash": deepcopy(payload_hash),
        "parent_artifact_ids": [candidate_artifact_id],
        "dependency_artifact_ids": dependency_ids,
        "created_at": utc_now(),
        "status": _qa_status(asset_qa_result),
        "metadata": {
            "source_payload_type": "image_review_form",
            "review_id": review_id,
            "image_review_decision": review_form.get("decision", ""),
            "asset_qa_decision": asset_qa_result.get("decision", ""),
            "allow_accepted": asset_qa_result.get("allow_accepted", False),
            "manual_evidence": review_form.get("manual_evidence", {}),
            "machine_assist": review_form.get("machine_assist", {}),
            "failure_reasons": review_form.get("failure_reasons", []),
            "repair_suggestions": review_form.get("repair_suggestions", []),
        },
    }
    return result(
        True,
        artifact=artifact,
        asset_qa_result=asset_qa_result,
        review_validation_result=merge_result.get("review_validation_result", {}),
        failures=[],
    )


def register_image_qa_artifact(
    review_form: dict[str, Any],
    *,
    registry_path: str | None = None,
    source_path: str = "",
    dry_run: bool = False,
) -> dict[str, Any]:
    payload = create_image_qa_artifact_payload(review_form, registry_path=registry_path, source_path=source_path)
    if not payload["passed"]:
        return payload
    registration = register_artifact(payload["artifact"], registry_path=registry_path, dry_run=dry_run)
    return result(
        registration["passed"],
        artifact=payload["artifact"],
        asset_qa_result=payload["asset_qa_result"],
        review_validation_result=payload["review_validation_result"],
        artifact_registration=registration,
        failures=registration.get("failures", []),
    )


def register_image_qa_artifact_file(path: str, *, registry_path: str | None = None, dry_run: bool = False) -> dict[str, Any]:
    return register_image_qa_artifact(read_json(path), registry_path=registry_path, source_path=path, dry_run=dry_run)
