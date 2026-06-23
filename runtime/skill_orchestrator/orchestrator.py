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


def _analysis_selected_skills(story_analysis_result: dict[str, Any] | None) -> list[str]:
    if not isinstance(story_analysis_result, dict):
        return []
    plan = story_analysis_result.get("recommended_skill_plan")
    if not isinstance(plan, dict):
        return []
    selected = plan.get("selected_skill_set")
    if not isinstance(selected, list):
        return []
    skills = skill_map()
    return [skill_id for skill_id in selected if isinstance(skill_id, str) and skill_id in skills]


def _analysis_node_plan(
    story_analysis_result: dict[str, Any] | None,
    page_index: int,
) -> dict[str, Any] | None:
    if not isinstance(story_analysis_result, dict):
        return None
    plan = story_analysis_result.get("recommended_skill_plan")
    if not isinstance(plan, dict):
        return None
    node_plans = plan.get("node_skill_plan")
    if not isinstance(node_plans, list):
        return None
    for node_plan in node_plans:
        if not isinstance(node_plan, dict):
            continue
        try:
            node_page = int(node_plan.get("page_index"))
        except (TypeError, ValueError):
            continue
        if node_page == page_index:
            return node_plan
    return None


def _fields_and_questions(selected: list[str]) -> tuple[list[str], list[str]]:
    skills = skill_map()
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
    return required_graph_fields, list(dict.fromkeys(validation_questions))


def plan_node_skills(
    story_type: str = "horror",
    page_role: str | None = None,
    page_index: int = 1,
    total_pages: int = 12,
    suspense_type: str | None = None,
    story_analysis_result: dict[str, Any] | None = None,
) -> dict[str, Any]:
    analysis_node_plan = _analysis_node_plan(story_analysis_result, page_index)
    if analysis_node_plan is not None:
        selected = _analysis_selected_skills(story_analysis_result)
        node_selected = [
            skill_id
            for skill_id in analysis_node_plan.get("skills", [])
            if isinstance(skill_id, str) and skill_id in skill_map()
        ]
        if node_selected:
            selected = node_selected
        required_graph_fields, validation_questions = _fields_and_questions(selected)
        return {
            "selected_skill_set": selected,
            "node_skill_plan": {
                "story_type": story_type,
                "page_role": page_role or analysis_node_plan.get("page_role") or "",
                "page_index": page_index,
                "total_pages": total_pages,
                "suspense_type": suspense_type,
                "skills": selected,
                "source": "story_analyzer",
            },
            "required_graph_fields": required_graph_fields,
            "validation_questions": validation_questions,
        }

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


def select_story_skills(
    story_type: str = "horror",
    total_pages: int = 12,
    story_analysis_result: dict[str, Any] | None = None,
) -> dict[str, Any]:
    analysis_selected = _analysis_selected_skills(story_analysis_result)
    if analysis_selected:
        plan = story_analysis_result.get("recommended_skill_plan", {}) if isinstance(story_analysis_result, dict) else {}
        node_plan = plan.get("node_skill_plan", [])
        required_graph_fields, validation_questions = _fields_and_questions(analysis_selected)
        return {
            "selected_skill_set": analysis_selected,
            "node_skill_plan": node_plan,
            "required_graph_fields": required_graph_fields,
            "validation_questions": validation_questions,
            "source": "story_analyzer",
        }

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
