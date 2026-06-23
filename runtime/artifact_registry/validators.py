from __future__ import annotations

from typing import Any

from artifact_registry.artifact_schema import validate_artifact_schema
from core.io import result


def _artifacts_by_id(registry: dict[str, Any]) -> dict[str, dict[str, Any]]:
    artifacts = registry.get("artifacts", {})
    if isinstance(artifacts, dict):
        return {key: value for key, value in artifacts.items() if isinstance(value, dict)}
    if isinstance(artifacts, list):
        return {
            item["artifact_id"]: item
            for item in artifacts
            if isinstance(item, dict) and isinstance(item.get("artifact_id"), str)
        }
    return {}


def _linked_artifacts(artifact: dict[str, Any], registry: dict[str, Any], *, parents_only: bool = False) -> list[dict[str, Any]]:
    by_id = _artifacts_by_id(registry)
    link_ids = list(artifact.get("parent_artifact_ids", []))
    if not parents_only:
        link_ids.extend(artifact.get("dependency_artifact_ids", []))
    return [by_id[item] for item in link_ids if item in by_id]


def _linked_types(artifact: dict[str, Any], registry: dict[str, Any], *, parents_only: bool = False) -> set[str]:
    return {
        item.get("artifact_type", "")
        for item in _linked_artifacts(artifact, registry, parents_only=parents_only)
    }


def _reference_dependency_ids(artifact: dict[str, Any]) -> list[str]:
    metadata = artifact.get("metadata", {})
    refs = metadata.get("reference_dependency_ids") if isinstance(metadata, dict) else None
    if isinstance(refs, list):
        return [item for item in refs if isinstance(item, str) and item]
    if artifact.get("artifact_type") == "platform_page_layout":
        return list(artifact.get("dependency_artifact_ids", []))
    return []


def validate_artifact(artifact: dict[str, Any], registry: dict[str, Any]) -> dict[str, Any]:
    schema_result = validate_artifact_schema(artifact)
    failures = list(schema_result.get("failures", []))
    by_id = _artifacts_by_id(registry)

    parent_ids = artifact.get("parent_artifact_ids", [])
    dependency_ids = artifact.get("dependency_artifact_ids", [])
    linked_ids = [*parent_ids, *dependency_ids]
    missing = [artifact_id for artifact_id in linked_ids if artifact_id not in by_id]
    if missing:
        failures.append(f"missing_dependencies:{','.join(sorted(set(missing)))}")

    artifact_type = artifact.get("artifact_type")
    status = artifact.get("status")
    parent_types = _linked_types(artifact, registry, parents_only=True)
    associated_types = _linked_types(artifact, registry)

    if artifact_type == "compiled_prompt" and "visual_asset_spec" not in parent_types:
        failures.append("compiled_prompt_requires_visual_asset_spec_parent")
    if artifact_type == "semantic_lint_result" and "compiled_prompt" not in parent_types:
        failures.append("semantic_lint_result_requires_compiled_prompt_parent")
    if artifact_type == "external_generation_candidate":
        required = {"compiled_prompt", "semantic_lint_result"}
        missing_types = sorted(required - associated_types)
        if missing_types:
            failures.append(f"external_generation_candidate_missing_dependencies:{','.join(missing_types)}")
    if artifact_type == "execution_telemetry" and not (
        {"external_generation_candidate", "compiled_prompt"} & associated_types
    ):
        failures.append("execution_telemetry_requires_candidate_or_compiled_prompt")
    if artifact_type == "asset_qa_result" and "external_generation_candidate" not in associated_types:
        failures.append("asset_qa_result_requires_external_generation_candidate")

    if artifact_type == "accepted_reference_asset" and status == "accepted":
        required = {"external_generation_candidate", "execution_telemetry", "asset_qa_result"}
        missing_types = sorted(required - associated_types)
        if missing_types:
            failures.append(f"accepted_reference_asset_missing_dependencies:{','.join(missing_types)}")
        qa_artifacts = [
            item
            for item in _linked_artifacts(artifact, registry)
            if item.get("artifact_type") == "asset_qa_result"
        ]
        if not any(item.get("status") == "qa_passed" for item in qa_artifacts):
            failures.append("accepted_reference_asset_requires_qa_passed")

    for reference_id in _reference_dependency_ids(artifact):
        reference = by_id.get(reference_id)
        if reference is None:
            failures.append(f"reference_dependency_missing:{reference_id}")
            continue
        reference_status = reference.get("status")
        if reference_status in {"rejected", "deprecated"}:
            failures.append(f"reference_dependency_not_allowed:{reference_id}:{reference_status}")
        if reference.get("artifact_type") == "accepted_reference_asset" and reference_status != "accepted":
            failures.append(f"reference_dependency_not_accepted:{reference_id}:{reference_status}")

    return result(not failures, artifact_id=artifact.get("artifact_id", ""), failures=list(dict.fromkeys(failures)))
