from __future__ import annotations

from typing import Any


CHECKED_FIELDS = [
    "typed_hook",
    "typed_narration",
    "final_hook_sentence",
    "next_page_question",
    "reader_retention_goal",
    "visual_memory_point",
    "applied_skills",
    "emotional_turn",
    "suspense_type",
    "payoff_target",
]

WEAKNESS_SKILLS = {
    "weak_opening_hook": ["page_turn_hook"],
    "missing_next_question": ["page_turn_hook"],
    "missing_emotional_pull": ["emotional_pull"],
    "no_information_gain": ["platform_completion_rate", "misdirection_disproof"],
    "weak_visual_memory": ["platform_completion_rate"],
    "unclear_suspense_type": ["horror_escalation"],
    "missing_payoff_target": ["fate_loop", "strange_tale_twist"],
    "overloaded_page": ["world_compression", "platform_completion_rate"],
    "unsafe_child_adaptation": ["child_safe_adaptation"],
    "ending_without_callback": ["fate_loop", "strange_tale_twist"],
}

WEAKNESS_FIELDS = {
    "weak_opening_hook": "typed_hook",
    "missing_next_question": "next_page_question",
    "missing_emotional_pull": "emotional_turn",
    "no_information_gain": "information_gain",
    "weak_visual_memory": "visual_memory_point",
    "unclear_suspense_type": "suspense_type",
    "missing_payoff_target": "payoff_target",
    "overloaded_page": "typed_narration",
    "unsafe_child_adaptation": "typed_narration",
    "ending_without_callback": "opening_callback",
}


def _blank(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return not value.strip()
    if isinstance(value, (list, tuple, set, dict)):
        return len(value) == 0
    return False


def _as_int(value: Any) -> int | None:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _node_id(node: dict[str, Any]) -> str:
    return str(node.get("node_id") or node.get("id") or node.get("page_id") or node.get("page_index") or "")


def _role(node: dict[str, Any]) -> str:
    return str(node.get("page_role") or node.get("role") or node.get("node_role") or "").strip().lower()


def _is_opening(node: dict[str, Any]) -> bool:
    page_index = _as_int(node.get("page_index") or node.get("index"))
    return _role(node) in {"opening", "开头", "first"} or page_index == 1


def _is_ending(node: dict[str, Any], total_nodes: int | None = None) -> bool:
    role = _role(node)
    if role in {"ending", "final", "conclusion", "closing", "end", "结尾", "终页"}:
        return True
    if node.get("is_final") is True or node.get("final_page") is True:
        return True
    page_index = _as_int(node.get("page_index") or node.get("index"))
    total_pages = _as_int(node.get("total_pages") or node.get("page_count")) or total_nodes
    return bool(page_index and total_pages and page_index >= total_pages)


def _text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return " ".join(_text(item) for item in value)
    if isinstance(value, dict):
        return " ".join(_text(item) for item in value.values())
    return str(value)


def _has_unsafe_child_content(node: dict[str, Any]) -> bool:
    text = _text(node).lower()
    unsafe_terms = ("blood", "gore", "corpse", "murder", "kill", "血腥", "尸体", "杀死", "肢解")
    return any(term in text for term in unsafe_terms)


def _information_gain_missing(node: dict[str, Any]) -> bool:
    value = node.get("information_gain")
    if isinstance(value, (int, float)):
        return value <= 0
    if not _blank(value):
        return False
    narration = _text(node.get("typed_narration"))
    return len(narration.strip()) < 30 and _blank(node.get("threat_delta")) and _blank(node.get("disproof_signal"))


def _overloaded(node: dict[str, Any]) -> bool:
    event_count = _as_int(node.get("page_event_count") or node.get("event_count"))
    if event_count is not None and event_count > 3:
        return True
    narration = _text(node.get("typed_narration"))
    return len(narration) > 700 or len(narration.split()) > 120


def _repair_target(node_id: str, weakness: str) -> dict[str, Any]:
    field = WEAKNESS_FIELDS[weakness]
    skill = WEAKNESS_SKILLS[weakness][0]
    return {
        "node_id": node_id,
        "field": field,
        "weakness": weakness,
        "skill_id": skill,
        "repair_action": f"repair_{weakness}",
    }


def analyze_node(
    node: dict[str, Any],
    *,
    story_type: str = "unknown",
    total_nodes: int | None = None,
) -> dict[str, Any]:
    node_id = _node_id(node)
    weaknesses: list[str] = []
    ending = _is_ending(node, total_nodes=total_nodes)

    if _is_opening(node) and (_blank(node.get("typed_hook")) or _blank(node.get("final_hook_sentence")) or len(_text(node.get("typed_hook")).strip()) < 10):
        weaknesses.append("weak_opening_hook")
    if not ending and _blank(node.get("next_page_question")):
        weaknesses.append("missing_next_question")
    if _blank(node.get("emotional_turn")) and _blank(node.get("reader_care_reason")):
        weaknesses.append("missing_emotional_pull")
    if _information_gain_missing(node):
        weaknesses.append("no_information_gain")
    if _blank(node.get("visual_memory_point")):
        weaknesses.append("weak_visual_memory")
    if _blank(node.get("suspense_type")):
        weaknesses.append("unclear_suspense_type")
    if (ending or not _blank(node.get("twist_reveal")) or "payoff" in _role(node)) and _blank(node.get("payoff_target")):
        weaknesses.append("missing_payoff_target")
    if _overloaded(node):
        weaknesses.append("overloaded_page")
    if "child" in (story_type or "").lower() and _has_unsafe_child_content(node):
        weaknesses.append("unsafe_child_adaptation")
    if ending and _blank(node.get("opening_callback")) and _blank(node.get("callback_target")):
        weaknesses.append("ending_without_callback")

    high = {"unsafe_child_adaptation", "ending_without_callback", "missing_payoff_target"}
    if "weak_opening_hook" in weaknesses and _blank(node.get("typed_hook")):
        high.add("weak_opening_hook")
    risk_level = "low"
    if any(item in high for item in weaknesses) or len(weaknesses) >= 4:
        risk_level = "high"
    elif weaknesses:
        risk_level = "medium"

    recommended_skills = list(dict.fromkeys(skill for weakness in weaknesses for skill in WEAKNESS_SKILLS[weakness]))
    return {
        "node_id": node_id,
        "weaknesses": weaknesses,
        "recommended_skills": recommended_skills,
        "risk_level": risk_level,
        "repair_targets": [_repair_target(node_id, weakness) for weakness in weaknesses],
    }
