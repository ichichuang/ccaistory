from __future__ import annotations

from collections import defaultdict
from typing import Any


DEFAULT_RESOLUTION_ORDER = [
    "safety",
    "clarity",
    "story_coherence",
    "hook_strength",
    "platform_retention",
    "style",
]

HOOK_SKILLS = {"page_turn_hook", "horror_escalation"}
CLARITY_SKILLS = {"world_compression", "rule_horror", "misdirection_disproof"}
COHERENCE_SKILLS = {"strange_tale_twist", "fate_loop", "misdirection_disproof", "rule_horror"}
RETENTION_SKILLS = {"platform_completion_rate"}


def _candidate_list(value: dict[str, Any] | list[Any]) -> list[dict[str, Any]]:
    if isinstance(value, list):
        return [item for item in value if isinstance(item, dict)]
    if isinstance(value, dict):
        candidates = value.get("candidates")
        if isinstance(candidates, list):
            return [item for item in candidates if isinstance(item, dict)]
    return []


def _score_lookup(scored_candidates: list[dict[str, Any]] | dict[str, Any] | None) -> dict[str, dict[str, Any]]:
    if isinstance(scored_candidates, dict):
        scored = scored_candidates.get("scored_candidates", scored_candidates.get("scores", []))
    else:
        scored = scored_candidates
    if not isinstance(scored, list):
        return {}
    return {str(item.get("candidate_id")): item for item in scored if isinstance(item, dict)}


def _node_id(candidates: list[dict[str, Any]]) -> str:
    node_ids = sorted({str(candidate.get("node_id") or "") for candidate in candidates if candidate.get("node_id")})
    if not node_ids:
        return ""
    return node_ids[0] if len(node_ids) == 1 else "multiple"


def _candidate_ids(candidates: list[dict[str, Any]], skill_ids: set[str]) -> list[str]:
    return [
        str(candidate.get("candidate_id"))
        for candidate in candidates
        if candidate.get("candidate_id") and str(candidate.get("skill_id") or "") in skill_ids
    ]


def _add_pair_conflict(
    conflicts: list[dict[str, Any]],
    *,
    conflict_type: str,
    field: str,
    candidates: list[dict[str, Any]],
    left: set[str],
    right: set[str],
    reason: str,
    preferred_priority: str,
) -> None:
    skill_ids = {str(candidate.get("skill_id") or "") for candidate in candidates}
    if not (skill_ids & left and skill_ids & right):
        return
    involved = (skill_ids & left) | (skill_ids & right)
    conflicts.append(
        {
            "conflict_type": conflict_type,
            "field": field,
            "skill_ids": sorted(involved),
            "candidate_ids": _candidate_ids(candidates, involved),
            "reason": reason,
            "preferred_priority": preferred_priority,
        }
    )


def _score_conflicts(
    conflicts: list[dict[str, Any]],
    *,
    field: str,
    candidates: list[dict[str, Any]],
    scores: dict[str, dict[str, Any]],
) -> None:
    for candidate in candidates:
        score = scores.get(str(candidate.get("candidate_id") or ""))
        if not score:
            continue
        dimensions = score.get("scores", {})
        if not isinstance(dimensions, dict):
            continue
        hook = int(dimensions.get("hook_strength") or 0)
        clarity = int(dimensions.get("clarity") or 0)
        if hook >= clarity + 2:
            conflicts.append(
                {
                    "conflict_type": "hook_strength_vs_clarity",
                    "field": field,
                    "skill_ids": [str(candidate.get("skill_id") or "")],
                    "candidate_ids": [str(candidate.get("candidate_id") or "")],
                    "reason": "hook_strength_score_exceeds_clarity_score",
                    "preferred_priority": "clarity",
                }
            )


def resolve_conflicts(
    candidates: dict[str, Any] | list[Any],
    scored_candidates: list[dict[str, Any]] | dict[str, Any] | None = None,
) -> dict[str, Any]:
    candidate_items = _candidate_list(candidates)
    scores = _score_lookup(scored_candidates)
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for candidate in candidate_items:
        grouped[(str(candidate.get("node_id") or ""), str(candidate.get("target_field") or ""))].append(candidate)

    conflicts: list[dict[str, Any]] = []
    for (_node, field), items in grouped.items():
        if len(items) < 2:
            _score_conflicts(conflicts, field=field, candidates=items, scores=scores)
            continue
        _add_pair_conflict(
            conflicts,
            conflict_type="hook_strength_vs_clarity",
            field=field,
            candidates=items,
            left=HOOK_SKILLS,
            right=CLARITY_SKILLS,
            reason="hook pressure and clarity compression both target the same field",
            preferred_priority="clarity",
        )
        _add_pair_conflict(
            conflicts,
            conflict_type="horror_escalation_vs_child_safe_adaptation",
            field=field,
            candidates=items,
            left={"horror_escalation"},
            right={"child_safe_adaptation"},
            reason="threat escalation and child safety both target the same field",
            preferred_priority="safety",
        )
        _add_pair_conflict(
            conflicts,
            conflict_type="world_compression_vs_emotional_pull",
            field=field,
            candidates=items,
            left={"world_compression"},
            right={"emotional_pull"},
            reason="compression may remove emotional context from the same field",
            preferred_priority="story_coherence",
        )
        _add_pair_conflict(
            conflicts,
            conflict_type="platform_completion_rate_vs_story_coherence",
            field=field,
            candidates=items,
            left=RETENTION_SKILLS,
            right=COHERENCE_SKILLS,
            reason="retention pacing may compete with coherence repair on the same field",
            preferred_priority="story_coherence",
        )
        _score_conflicts(conflicts, field=field, candidates=items, scores=scores)

    conflicts = [dict(item) for item in {repr(conflict): conflict for conflict in conflicts}.values()]
    resolution_plan = {
        "node_id": _node_id(candidate_items),
        "conflicts": conflicts,
        "resolution_order": DEFAULT_RESOLUTION_ORDER,
        "manual_review_required": bool(conflicts),
    }
    return {**resolution_plan, "resolution_plan": resolution_plan}
