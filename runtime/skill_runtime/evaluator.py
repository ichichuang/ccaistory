from __future__ import annotations

from typing import Any

from skill_registry.load_skills import load_skills


KEY_FIELDS = [
    "typed_hook",
    "typed_narration",
    "next_page_question",
    "final_hook_sentence",
    "reader_retention_goal",
    "visual_memory_point",
    "technique_notes",
]

OPTIONAL_WEAK_FIELDS = ["typed_narration", "visual_memory_point", "technique_notes"]

FIELD_REPAIR_ACTIONS = {
    "applied_skills": "select_applicable_skill",
    "typed_hook": "rewrite_typed_hook",
    "next_page_question": "add_next_page_question",
    "final_hook_sentence": "rewrite_final_hook_sentence",
    "reader_retention_goal": "add_reader_retention_goal",
    "opening_callback": "add_opening_callback",
    "threat_delta": "add_threat_delta",
}

FIELD_HARD_FAILURES = {
    "typed_hook": "missing_typed_hook",
    "next_page_question": "no_page_turn_question",
    "final_hook_sentence": "flat_final_sentence",
    "reader_retention_goal": "no_retention_goal",
    "opening_callback": "ending_not_callback_opening",
    "threat_delta": "threat_not_escalated",
    "applied_skills": "no_applied_skills",
}


def _is_blank(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return not value.strip()
    if isinstance(value, (list, tuple, set, dict)):
        return len(value) == 0
    return False


def _node_id(node: dict[str, Any]) -> str:
    return str(node.get("node_id") or node.get("id") or node.get("page_id") or node.get("page_index") or "")


def _as_int(value: Any) -> int | None:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _normalize_applied_skills(value: Any) -> list[str]:
    if isinstance(value, str):
        return [part.strip() for part in value.split(",") if part.strip()]
    if not isinstance(value, list):
        return []

    skill_ids: list[str] = []
    for item in value:
        if isinstance(item, str) and item.strip():
            skill_ids.append(item.strip())
        elif isinstance(item, dict):
            skill_id = item.get("skill_id") or item.get("id")
            if isinstance(skill_id, str) and skill_id.strip():
                skill_ids.append(skill_id.strip())
    return list(dict.fromkeys(skill_ids))


def _role(node: dict[str, Any]) -> str:
    return str(node.get("page_role") or node.get("role") or node.get("node_role") or "").strip().lower()


def _is_ending_node(node: dict[str, Any], total_nodes: int | None = None) -> bool:
    role = _role(node)
    if role in {"ending", "final", "conclusion", "closing", "end", "结尾", "终页"}:
        return True
    if node.get("is_final") is True or node.get("final_page") is True:
        return True

    page_index = _as_int(node.get("page_index") or node.get("index"))
    total_pages = _as_int(node.get("total_pages") or node.get("page_count")) or total_nodes
    return bool(page_index and total_pages and page_index >= total_pages)


def _is_middle_escalation_node(node: dict[str, Any], applied_skills: list[str]) -> bool:
    role = _role(node)
    return role in {"middle_escalation", "escalation", "middle"} or "horror_escalation" in applied_skills


def _has_escalation_explanation(node: dict[str, Any]) -> bool:
    for field in ("threat_delta", "escalation_delta", "escalation_note", "escalation_explanation", "threat_escalation"):
        if not _is_blank(node.get(field)):
            return True

    notes = node.get("technique_notes")
    text = ""
    if isinstance(notes, str):
        text = notes
    elif isinstance(notes, list):
        text = " ".join(str(item) for item in notes)
    elif isinstance(notes, dict):
        text = " ".join(str(value) for value in notes.values())
    lowered = text.lower()
    return any(token in lowered for token in ("escalat", "threat", "升级", "递进", "威胁"))


def _skill_map(skills: list[dict[str, Any]] | None = None) -> dict[str, dict[str, Any]]:
    loaded = skills if skills is not None else load_skills()
    return {str(skill.get("skill_id")): skill for skill in loaded if skill.get("skill_id")}


def _repair_action(skill: dict[str, Any] | None, field: str) -> str:
    preferred = FIELD_REPAIR_ACTIONS.get(field, f"repair_{field}")
    actions = skill.get("repair_actions", []) if skill else []
    if preferred in actions:
        return preferred

    field_token = field.replace("_", "")
    for action in actions:
        if field_token in str(action).replace("_", ""):
            return str(action)
    if field == "final_hook_sentence":
        for action in actions:
            if "hook" in str(action):
                return str(action)
    if field == "opening_callback":
        for action in actions:
            if "callback" in str(action) or "opening" in str(action):
                return str(action)
    if field == "threat_delta":
        for action in actions:
            if "threat" in str(action) or "escalation" in str(action):
                return str(action)
    return preferred


def _target(
    node_id: str,
    field: str,
    reason: str,
    skill_id: str = "",
    skill: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "node_id": node_id,
        "field": field,
        "reason": reason,
        "skill_id": skill_id,
        "hard_failure": FIELD_HARD_FAILURES.get(field, reason),
        "repair_action": _repair_action(skill, field),
    }


def _failure(target: dict[str, Any], skill: dict[str, Any] | None = None) -> dict[str, Any]:
    return {
        "node_id": target["node_id"],
        "skill_id": target.get("skill_id", ""),
        "field": target["field"],
        "failure": target["reason"],
        "hard_failure": target.get("hard_failure", target["reason"]),
        "validation_questions": skill.get("validation_questions", []) if skill else [],
        "repair_action": target.get("repair_action", ""),
    }


def evaluate_node(
    node: dict[str, Any],
    skills: list[dict[str, Any]] | None = None,
    total_nodes: int | None = None,
) -> dict[str, Any]:
    skill_lookup = _skill_map(skills)
    node_id = _node_id(node)
    applied_skills = _normalize_applied_skills(node.get("applied_skills"))
    ending = _is_ending_node(node, total_nodes=total_nodes)

    missing_fields: list[str] = []
    weak_fields: list[str] = []
    repair_targets: list[dict[str, Any]] = []
    skill_failures: list[dict[str, Any]] = []

    def add_blocking(field: str, reason: str, skill_id: str = "") -> None:
        skill = skill_lookup.get(skill_id) if skill_id else None
        target = _target(node_id=node_id, field=field, reason=reason, skill_id=skill_id, skill=skill)
        if field not in missing_fields:
            missing_fields.append(field)
        repair_targets.append(target)
        skill_failures.append(_failure(target, skill=skill))

    if not applied_skills:
        add_blocking("applied_skills", "applied_skills_empty")

    for skill_id in applied_skills:
        if skill_id not in skill_lookup:
            target = _target(
                node_id=node_id,
                field="applied_skills",
                reason="unknown_skill",
                skill_id=skill_id,
                skill=None,
            )
            repair_targets.append(target)
            skill_failures.append(_failure(target))

    hook_skill = "page_turn_hook" if "page_turn_hook" in applied_skills else (applied_skills[0] if applied_skills else "")
    retention_skill = (
        "platform_completion_rate"
        if "platform_completion_rate" in applied_skills
        else ("emotional_pull" if "emotional_pull" in applied_skills else hook_skill)
    )

    if _is_blank(node.get("typed_hook")):
        add_blocking("typed_hook", "typed_hook_empty", hook_skill)
    if _is_blank(node.get("final_hook_sentence")):
        add_blocking("final_hook_sentence", "final_hook_sentence_empty", hook_skill)
    if not ending and _is_blank(node.get("next_page_question")):
        add_blocking("next_page_question", "next_page_question_empty", hook_skill)
    if _is_blank(node.get("reader_retention_goal")):
        add_blocking("reader_retention_goal", "reader_retention_goal_empty", retention_skill)
    if ending and _is_blank(node.get("opening_callback")):
        ending_skill = "fate_loop" if "fate_loop" in applied_skills else ("strange_tale_twist" if "strange_tale_twist" in applied_skills else hook_skill)
        add_blocking("opening_callback", "ending_opening_callback_empty", ending_skill)
    if _is_middle_escalation_node(node, applied_skills) and not _has_escalation_explanation(node):
        add_blocking("threat_delta", "middle_escalation_without_threat_delta", "horror_escalation" if "horror_escalation" in applied_skills else hook_skill)

    for field in OPTIONAL_WEAK_FIELDS:
        if _is_blank(node.get(field)) and field not in weak_fields:
            weak_fields.append(field)

    return {
        "passed": not skill_failures,
        "node_id": node_id,
        "skill_failures": skill_failures,
        "missing_fields": missing_fields,
        "weak_fields": weak_fields,
        "repair_targets": repair_targets,
        "checked_fields": KEY_FIELDS,
        "applied_skills": applied_skills,
    }
