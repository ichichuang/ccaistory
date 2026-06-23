from __future__ import annotations

from collections import defaultdict
from typing import Any


def _node_id(node: dict[str, Any]) -> str:
    return str(node.get("node_id") or node.get("id") or node.get("page_id") or node.get("page_index") or "")


def _score_lookup(scored_candidates: list[dict[str, Any]] | dict[str, Any]) -> dict[str, dict[str, Any]]:
    if isinstance(scored_candidates, dict):
        scored = scored_candidates.get("scored_candidates", scored_candidates.get("scores", []))
    else:
        scored = scored_candidates
    if not isinstance(scored, list):
        return {}
    return {str(item.get("candidate_id")): item for item in scored if isinstance(item, dict)}


def _candidate_list(candidates: dict[str, Any] | list[Any]) -> list[dict[str, Any]]:
    if isinstance(candidates, list):
        return [item for item in candidates if isinstance(item, dict)]
    if isinstance(candidates, dict):
        items = candidates.get("candidates")
        if isinstance(items, list):
            return [item for item in items if isinstance(item, dict)]
    return []


def _current_value(node: dict[str, Any], field: str) -> Any:
    value = node.get(field, "")
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value if value is not None else ""
    return value


def build_proposed_changes(
    node: dict[str, Any],
    candidates: dict[str, Any] | list[Any],
    scored_candidates: list[dict[str, Any]] | dict[str, Any],
) -> dict[str, Any]:
    score_by_id = _score_lookup(scored_candidates)
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for candidate in _candidate_list(candidates):
        field = str(candidate.get("target_field") or "")
        if field:
            grouped[field].append(candidate)

    proposed_changes: list[dict[str, Any]] = []
    for field, field_candidates in sorted(grouped.items()):
        ranked = sorted(
            field_candidates,
            key=lambda item: (
                bool(score_by_id.get(str(item.get("candidate_id") or ""), {}).get("passed")),
                int(score_by_id.get(str(item.get("candidate_id") or ""), {}).get("total_score") or 0),
                str(item.get("candidate_id") or ""),
            ),
            reverse=True,
        )
        if not ranked:
            continue
        selected = ranked[0]
        score = score_by_id.get(str(selected.get("candidate_id") or ""), {})
        if not score.get("passed"):
            continue
        proposed_changes.append(
            {
                "field": field,
                "current_value": _current_value(node, field),
                "recommended_candidate_id": str(selected.get("candidate_id") or ""),
                "recommended_text": str(selected.get("proposed_text") or ""),
                "scores": score.get("scores", {}),
                "reason": str(selected.get("rationale") or ""),
                "human_approval_required": True,
            }
        )

    return {"node_id": _node_id(node), "proposed_changes": proposed_changes}
