from __future__ import annotations

from typing import Any

from skill_registry.load_skills import load_skills
from story_analyzer.character_stakes import analyze_character_stakes
from story_analyzer.clue_ledger import analyze_clue_ledger
from story_analyzer.node_diagnostics import analyze_node
from story_analyzer.page_count_estimator import estimate_page_count, estimate_pages_for_story_core
from story_analyzer.story_type_classifier import classify_story_core
from story_analyzer.tension_curve import analyze_tension_curve


def _nodes_from_graph(story_graph: dict[str, Any]) -> list[dict[str, Any]]:
    if isinstance(story_graph.get("nodes"), list):
        return [node for node in story_graph["nodes"] if isinstance(node, dict)]
    nested = story_graph.get("story_graph")
    if isinstance(nested, dict) and isinstance(nested.get("nodes"), list):
        return [node for node in nested["nodes"] if isinstance(node, dict)]
    return []


def _story_graph(payload: dict[str, Any]) -> dict[str, Any]:
    graph = payload.get("story_graph")
    if isinstance(graph, dict):
        return graph
    if isinstance(payload.get("nodes"), list):
        return payload
    return {}


def _count_twists(nodes: list[dict[str, Any]]) -> int:
    return sum(1 for node in nodes if node.get("twist_reveal") or "twist" in str(node.get("page_role", "")).lower())


def _payoff_targets(nodes: list[dict[str, Any]]) -> list[Any]:
    return [node["payoff_target"] for node in nodes if node.get("payoff_target")]


def _skill_lookup() -> dict[str, dict[str, Any]]:
    return {str(skill["skill_id"]): skill for skill in load_skills() if skill.get("skill_id")}


def _known_skills(skills: list[str]) -> list[str]:
    known = _skill_lookup()
    return [skill_id for skill_id in list(dict.fromkeys(skills)) if skill_id in known]


def _required_fields_and_questions(skill_ids: list[str]) -> tuple[list[str], list[str]]:
    known = _skill_lookup()
    required_fields = sorted(
        {
            field
            for skill_id in skill_ids
            for field in known.get(skill_id, {}).get("graph_fields_affected", [])
        }
    )
    questions = [
        question
        for skill_id in skill_ids
        for question in known.get(skill_id, {}).get("validation_questions", [])
    ]
    return required_fields, list(dict.fromkeys(questions))


def _recommended_skill_plan(
    *,
    nodes: list[dict[str, Any]],
    story_type: dict[str, Any],
    node_diagnostics: list[dict[str, Any]],
    clue_ledger: dict[str, Any],
    tension_curve: dict[str, Any],
    character_stakes: dict[str, Any],
) -> dict[str, Any]:
    selected: list[str] = list(story_type.get("recommended_global_skills", []))
    selected.extend(skill for item in node_diagnostics for skill in item.get("recommended_skills", []))
    if clue_ledger.get("failures"):
        selected.extend(["misdirection_disproof", "strange_tale_twist", "fate_loop"])
    if tension_curve.get("failures"):
        selected.extend(["horror_escalation", "platform_completion_rate", "page_turn_hook"])
    selected.extend(character_stakes.get("recommended_skills", []))
    if not selected:
        selected.append("page_turn_hook")
    selected = _known_skills(selected)
    required_fields, questions = _required_fields_and_questions(selected)

    by_node = {item["node_id"]: item for item in node_diagnostics}
    node_plan = []
    for index, node in enumerate(nodes):
        node_id = str(node.get("node_id") or node.get("id") or node.get("page_index") or index + 1)
        applied = node.get("applied_skills") if isinstance(node.get("applied_skills"), list) else []
        node_skills = _known_skills([*applied, *by_node.get(node_id, {}).get("recommended_skills", [])])
        if not node_skills:
            node_skills = selected[:2]
        node_plan.append(
            {
                "node_id": node_id,
                "page_index": node.get("page_index") or index + 1,
                "skills": node_skills,
                "source": "story_analyzer",
            }
        )

    return {
        "source": "story_analyzer",
        "selected_skill_set": selected,
        "node_skill_plan": node_plan,
        "required_graph_fields": required_fields,
        "validation_questions": questions,
    }


def _priority(
    *,
    node_diagnostics: list[dict[str, Any]],
    clue_ledger: dict[str, Any],
    tension_curve: dict[str, Any],
    character_stakes: dict[str, Any],
) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for diagnostic in node_diagnostics:
        for weakness in diagnostic.get("weaknesses", []):
            items.append(
                {
                    "source": "node_diagnostics",
                    "risk_level": diagnostic["risk_level"],
                    "node_id": diagnostic["node_id"],
                    "issue": weakness,
                    "repair_targets": diagnostic.get("repair_targets", []),
                }
            )
    for failure in clue_ledger.get("failures", []):
        items.append({"source": "clue_ledger", "risk_level": "high", "issue": failure})
    for failure in tension_curve.get("failures", []):
        items.append({"source": "tension_curve", "risk_level": "high", "issue": failure})
    if not character_stakes.get("passed", True):
        for issue in character_stakes.get("missing_stakes", []):
            items.append({"source": "character_stakes", "risk_level": "high", "issue": issue})
        for weak_node in character_stakes.get("weak_nodes", []):
            items.append(
                {
                    "source": "character_stakes",
                    "risk_level": "high",
                    "node_id": weak_node.get("node_id", ""),
                    "issue": ",".join(weak_node.get("failures", [])),
                }
            )
    order = {"high": 0, "medium": 1, "low": 2}
    return sorted(items, key=lambda item: order.get(str(item.get("risk_level")), 9))


def analyze_story_core(story_core: dict[str, Any]) -> dict[str, Any]:
    graph = _story_graph(story_core)
    story_type = classify_story_core(story_core)
    page_count = estimate_pages_for_story_core(story_core)
    return _analyze(graph, story_type=story_type, page_count=page_count)


def analyze_story_graph(story_graph: dict[str, Any]) -> dict[str, Any]:
    graph = _story_graph(story_graph) or story_graph
    nodes = _nodes_from_graph(graph)
    story_type = {"story_type": "unknown", "confidence": 0.2, "reason_codes": ["graph_only_input"], "recommended_global_skills": []}
    page_count = estimate_page_count(
        story_type="unknown",
        event_count=len(nodes),
        twist_count=_count_twists(nodes),
        required_payoffs=_payoff_targets(nodes),
    )
    return _analyze(graph, story_type=story_type, page_count=page_count)


def _analyze(story_graph: dict[str, Any], *, story_type: dict[str, Any], page_count: dict[str, Any]) -> dict[str, Any]:
    nodes = _nodes_from_graph(story_graph)
    node_diagnostics = [
        analyze_node(node, story_type=story_type["story_type"], total_nodes=len(nodes)) for node in nodes
    ]
    clue_ledger = analyze_clue_ledger(story_graph)
    tension_curve = analyze_tension_curve(story_graph)
    character_stakes = analyze_character_stakes(story_graph)
    recommended_skill_plan = _recommended_skill_plan(
        nodes=nodes,
        story_type=story_type,
        node_diagnostics=node_diagnostics,
        clue_ledger=clue_ledger,
        tension_curve=tension_curve,
        character_stakes=character_stakes,
    )
    repair_priority = _priority(
        node_diagnostics=node_diagnostics,
        clue_ledger=clue_ledger,
        tension_curve=tension_curve,
        character_stakes=character_stakes,
    )
    high_risk = (
        not nodes
        or any(item.get("risk_level") == "high" for item in node_diagnostics)
        or bool(clue_ledger.get("failures"))
        or bool(tension_curve.get("failures"))
        or not character_stakes.get("passed", True)
    )
    return {
        "passed": not high_risk,
        "story_type": story_type,
        "page_count": page_count,
        "node_diagnostics": node_diagnostics,
        "clue_ledger": clue_ledger,
        "tension_curve": tension_curve,
        "character_stakes": character_stakes,
        "recommended_skill_plan": recommended_skill_plan,
        "repair_priority": repair_priority,
        "next_action": "repair_story_graph_before_skill_executor" if high_risk else "proceed_to_skill_executor_or_next_gate",
    }
