from __future__ import annotations

from typing import Any

from core.io import result


ARTIFACT_TYPES = {
    "story_core",
    "story_graph",
    "story_analysis_result",
    "skill_executor_result",
    "visual_asset_spec",
    "compiled_prompt",
    "semantic_lint_result",
    "source_pilot_task_list",
    "external_generation_candidate",
    "execution_telemetry",
    "image_review_form",
    "asset_qa_result",
    "accepted_reference_asset",
    "platform_page_layout",
    "publish_package",
}

ARTIFACT_STATUSES = {
    "draft",
    "compiled",
    "lint_passed",
    "lint_failed",
    "generated",
    "telemetry_recorded",
    "qa_pending",
    "qa_passed",
    "qa_failed",
    "accepted",
    "rejected",
    "deprecated",
}

REQUIRED_ARTIFACT_FIELDS = [
    "artifact_id",
    "artifact_type",
    "project_id",
    "story_id",
    "asset_id",
    "run_id",
    "candidate_id",
    "source_path",
    "content_hash",
    "source_hash",
    "parent_artifact_ids",
    "dependency_artifact_ids",
    "created_at",
    "status",
    "metadata",
]

STRING_FIELDS = {
    "artifact_id",
    "artifact_type",
    "project_id",
    "story_id",
    "asset_id",
    "run_id",
    "candidate_id",
    "source_path",
    "created_at",
    "status",
}

LIST_FIELDS = {"parent_artifact_ids", "dependency_artifact_ids"}


def _validate_hash_block(name: str, block: Any, failures: list[str]) -> None:
    if not isinstance(block, dict):
        failures.append(f"{name}_not_object")
        return
    digest = block.get("hash")
    algorithm = block.get("algorithm")
    if not isinstance(digest, str) or not digest:
        failures.append(f"{name}_hash_missing")
    if algorithm != "sha256":
        failures.append(f"{name}_algorithm_not_sha256")


def validate_artifact_schema(artifact: dict[str, Any]) -> dict[str, Any]:
    failures: list[str] = []
    if not isinstance(artifact, dict):
        return result(False, failures=["artifact_root_not_object"])

    missing = [field for field in REQUIRED_ARTIFACT_FIELDS if field not in artifact]
    if missing:
        failures.append(f"missing_fields:{','.join(missing)}")

    for field in STRING_FIELDS:
        if field in artifact and not isinstance(artifact.get(field), str):
            failures.append(f"{field}_not_string")

    artifact_id = artifact.get("artifact_id")
    artifact_type = artifact.get("artifact_type")
    status = artifact.get("status")
    if not artifact_id:
        failures.append("artifact_id_missing")
    if artifact_type not in ARTIFACT_TYPES:
        failures.append(f"unknown_artifact_type:{artifact_type}")
    if status not in ARTIFACT_STATUSES:
        failures.append(f"unknown_status:{status}")

    for field in LIST_FIELDS:
        value = artifact.get(field)
        if not isinstance(value, list) or not all(isinstance(item, str) and item for item in value):
            failures.append(f"{field}_not_string_list")
        elif artifact_id and artifact_id in value:
            failures.append(f"{field}_contains_self")

    _validate_hash_block("content_hash", artifact.get("content_hash"), failures)
    _validate_hash_block("source_hash", artifact.get("source_hash"), failures)

    if not isinstance(artifact.get("metadata"), dict):
        failures.append("metadata_not_object")

    return result(not failures, artifact_id=artifact.get("artifact_id", ""), failures=failures)
