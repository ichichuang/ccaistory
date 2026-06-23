from __future__ import annotations

from typing import Any

from artifact_registry.registry import load_registry
from core.io import result


def _artifacts_by_id(registry: dict[str, Any]) -> dict[str, dict[str, Any]]:
    artifacts = registry.get("artifacts", {})
    if not isinstance(artifacts, dict):
        return {}
    return {key: value for key, value in artifacts.items() if isinstance(value, dict)}


def _actual_prompt_present(artifact: dict[str, Any], lineage_items: list[dict[str, Any]]) -> bool:
    candidates = [artifact, *(item.get("artifact", {}) for item in lineage_items)]
    for item in candidates:
        metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
        if isinstance(metadata, dict) and metadata.get("actual_prompt_sent_to_external_tool"):
            return True
    return False


def trace_lineage(artifact_id: str, *, registry_path: str | None = None) -> dict[str, Any]:
    registry = load_registry(registry_path)
    artifacts = _artifacts_by_id(registry)
    root = artifacts.get(artifact_id)
    if root is None:
        return result(
            False,
            artifact_id=artifact_id,
            lineage=[],
            missing_dependencies=[],
            missing_required_ancestors=["artifact_not_found"],
        )

    lineage: list[dict[str, Any]] = []
    missing_dependencies: list[str] = []
    seen: set[str] = set()

    def visit(current_id: str, depth: int, relation: str) -> None:
        current = artifacts.get(current_id)
        if current is None:
            missing_dependencies.append(current_id)
            return
        if current_id in seen:
            return
        seen.add(current_id)
        lineage.append(
            {
                "artifact_id": current_id,
                "artifact_type": current.get("artifact_type", ""),
                "status": current.get("status", ""),
                "depth": depth,
                "relation": relation,
                "artifact": current,
            }
        )
        for parent_id in current.get("parent_artifact_ids", []):
            visit(parent_id, depth + 1, "parent")
        for dependency_id in current.get("dependency_artifact_ids", []):
            visit(dependency_id, depth + 1, "dependency")

    visit(artifact_id, 0, "self")
    ancestor_types = {item["artifact_type"] for item in lineage if item["artifact_id"] != artifact_id}
    missing_required: list[str] = []

    if root.get("artifact_type") == "accepted_reference_asset" and root.get("status") == "accepted":
        required = {
            "compiled_prompt",
            "external_generation_candidate",
            "execution_telemetry",
            "asset_qa_result",
        }
        missing_required.extend(sorted(required - ancestor_types))
    if root.get("artifact_type") == "external_generation_candidate" and not _actual_prompt_present(root, lineage):
        missing_required.append("actual_prompt_sent_to_external_tool")

    public_lineage = [
        {key: value for key, value in item.items() if key != "artifact"}
        for item in lineage
    ]
    return result(
        not missing_dependencies and not missing_required,
        artifact_id=artifact_id,
        lineage=public_lineage,
        missing_dependencies=sorted(set(missing_dependencies)),
        missing_required_ancestors=list(dict.fromkeys(missing_required)),
    )
