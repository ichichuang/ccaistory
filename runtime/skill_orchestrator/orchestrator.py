from __future__ import annotations

from typing import Any

from skill_registry.load_skills import skill_map


ROLE_RULES: dict[str, list[str]] = {
    "opening": ["page_turn_hook", "emotional_pull"],
    "first_anomaly": ["everyday_anomaly", "misdirection_disproof"],
    "middle_escalation": ["horror_escalation", "platform_completion_rate"],
    "rule_reveal": ["rule_horror", "horror_escalation"],
    "ending": ["fate_loop", "strange_tale_twist"],
}


def infer_page_role(page_index: int, total_pages: int, story_type: str = "horror") -> str:
    if page_index <= 1:
        return "opening"
    if page_index == 2:
        return "first_anomaly"
    if page_index >= total_pages:
        return "ending"
    if story_type == "horror" and page_index >= max(3, int(total_pages * 0.65)):
        return "rule_reveal"
    return "middle_escalation"


def global_skills(story_type: str, total_pages: int) -> list[str]:
    normalized = story_type.lower()
    selected: list[str] = []
    if any(token in normalized for token in ("child", "children", "kid", "儿童", "child_safe")):
        selected.append("child_safe_adaptation")
    if total_pages >= 16 or any(token in normalized for token in ("long", "classic", "complex", "长篇", "复杂")):
        selected.append("world_compression")
    return selected


def plan_node_skills(
    story_type: str = "horror",
    page_role: str | None = None,
    page_index: int = 1,
    total_pages: int = 12,
    suspense_type: str | None = None,
) -> dict[str, Any]:
    skills = skill_map()
    role = page_role or infer_page_role(page_index, total_pages, story_type)
    selected = [*global_skills(story_type, total_pages), *ROLE_RULES.get(role, ["page_turn_hook"])]
    if suspense_type == "rule" and "rule_horror" not in selected:
        selected.append("rule_horror")
    selected = list(dict.fromkeys(selected))
    known = [skill_id for skill_id in selected if skill_id in skills]
    required_graph_fields = sorted(
        {
            field
            for skill_id in known
            for field in skills[skill_id].get("graph_fields_affected", [])
        }
    )
    validation_questions = [
        question
        for skill_id in known
        for question in skills[skill_id].get("validation_questions", [])
    ]
    return {
        "selected_skill_set": known,
        "node_skill_plan": {
            "story_type": story_type,
            "page_role": role,
            "page_index": page_index,
            "total_pages": total_pages,
            "suspense_type": suspense_type,
            "skills": known,
        },
        "required_graph_fields": required_graph_fields,
        "validation_questions": validation_questions,
    }


def select_story_skills(story_type: str = "horror", total_pages: int = 12) -> dict[str, Any]:
    node_plans = [
        plan_node_skills(
            story_type=story_type,
            page_index=page_index,
            total_pages=total_pages,
        )["node_skill_plan"]
        for page_index in range(1, total_pages + 1)
    ]
    selected = sorted({skill_id for plan in node_plans for skill_id in plan["skills"]})
    required_graph_fields = sorted(
        {
            field
            for page_index in range(1, total_pages + 1)
            for field in plan_node_skills(story_type=story_type, page_index=page_index, total_pages=total_pages)[
                "required_graph_fields"
            ]
        }
    )
    validation_questions = []
    for page_index in range(1, total_pages + 1):
        validation_questions.extend(
            plan_node_skills(story_type=story_type, page_index=page_index, total_pages=total_pages)[
                "validation_questions"
            ]
        )
    return {
        "selected_skill_set": selected,
        "node_skill_plan": node_plans,
        "required_graph_fields": required_graph_fields,
        "validation_questions": list(dict.fromkeys(validation_questions)),
    }
