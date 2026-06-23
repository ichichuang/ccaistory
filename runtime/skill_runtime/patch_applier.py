from __future__ import annotations

from copy import deepcopy
from typing import Any

from core.io import result


def _node_id(node: dict[str, Any]) -> str:
    return str(node.get("node_id") or node.get("id") or node.get("page_id") or node.get("page_index") or "")


def _as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return list(value)
    return [value]


def apply_skill_patch(
    node: dict[str, Any],
    patch: dict[str, Any],
    dry_run: bool = True,
) -> dict[str, Any]:
    target = deepcopy(node)
    patches = patch.get("patches", [])
    if not isinstance(patches, list):
        patches = []

    required_fields = sorted(
        {
            str(item.get("field"))
            for item in patches
            if isinstance(item, dict) and item.get("field") and item.get("field") != "typed_narration"
        }
    )
    if any(isinstance(item, dict) and item.get("field") == "typed_narration" for item in patches):
        required_fields.append("typed_narration")
        required_fields = sorted(set(required_fields))

    target["repair_suggestions"] = [*_as_list(target.get("repair_suggestions")), *patches]
    target["required_rewrite_fields"] = sorted(
        set(str(item) for item in _as_list(target.get("required_rewrite_fields")) if item) | set(required_fields)
    )

    runtime_note = {
        "source": "skill_runtime.patch_applier",
        "node_id": patch.get("node_id") or _node_id(node),
        "patch_count": len(patches),
        "required_rewrite_fields": target["required_rewrite_fields"],
    }
    target["technique_notes"] = [*_as_list(target.get("technique_notes")), runtime_note]

    if not dry_run:
        node.clear()
        node.update(target)

    return result(
        True,
        dry_run=dry_run,
        node_id=_node_id(target),
        applied_patch_count=len(patches),
        required_rewrite_fields=target["required_rewrite_fields"],
        node=target,
    )
