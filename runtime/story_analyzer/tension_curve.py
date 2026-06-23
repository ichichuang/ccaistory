from __future__ import annotations

from typing import Any


DIMENSIONS = ["threat_level", "uncertainty", "emotional_pressure", "information_gain", "next_page_pull"]


def _nodes_from_graph(story_graph: dict[str, Any]) -> list[dict[str, Any]]:
    if isinstance(story_graph.get("nodes"), list):
        return [node for node in story_graph["nodes"] if isinstance(node, dict)]
    nested = story_graph.get("story_graph")
    if isinstance(nested, dict) and isinstance(nested.get("nodes"), list):
        return [node for node in nested["nodes"] if isinstance(node, dict)]
    return []


def _node_id(node: dict[str, Any]) -> str:
    return str(node.get("node_id") or node.get("id") or node.get("page_id") or node.get("page_index") or "")


def _blank(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return not value.strip()
    if isinstance(value, (list, tuple, set, dict)):
        return len(value) == 0
    return False


def _score_value(value: Any) -> float:
    if isinstance(value, bool):
        return 0.7 if value else 0.0
    if isinstance(value, (int, float)):
        number = float(value)
        return max(0.0, min(number / 10 if number > 1 else number, 1.0))
    if isinstance(value, str):
        lowered = value.strip().lower()
        if not lowered:
            return 0.0
        named = {
            "none": 0.0,
            "low": 0.25,
            "medium": 0.55,
            "high": 0.8,
            "very_high": 0.95,
            "无": 0.0,
            "低": 0.25,
            "中": 0.55,
            "高": 0.8,
        }
        if lowered in named:
            return named[lowered]
        return 0.6
    if isinstance(value, (list, tuple, set, dict)):
        return 0.6 if value else 0.0
    return 0.0


def _dimension_score(node: dict[str, Any], dimension: str, ending: bool) -> float:
    if dimension in node:
        return _score_value(node.get(dimension))
    if dimension == "threat_level":
        return 0.65 if not _blank(node.get("threat_delta")) else 0.25
    if dimension == "uncertainty":
        return 0.7 if not _blank(node.get("next_page_question")) else 0.25
    if dimension == "emotional_pressure":
        return 0.6 if not _blank(node.get("emotional_turn")) else 0.25
    if dimension == "information_gain":
        return 0.55 if not _blank(node.get("information_gain")) or not _blank(node.get("threat_delta")) else 0.2
    if dimension == "next_page_pull":
        if ending:
            return 0.55 if not _blank(node.get("opening_callback")) or not _blank(node.get("payoff_target")) else 0.2
        return 0.7 if not _blank(node.get("next_page_question")) or not _blank(node.get("final_hook_sentence")) else 0.15
    return 0.0


def _page_index(node: dict[str, Any], fallback: int) -> int:
    try:
        return int(node.get("page_index") or node.get("index") or fallback)
    except (TypeError, ValueError):
        node_id = _node_id(node)
        if len(node_id) >= 3 and node_id[0].lower() == "s" and node_id[1:].isdigit():
            return int(node_id[1:])
    return fallback


def _middle_indices(nodes: list[dict[str, Any]]) -> list[int]:
    s06_s09 = [index for index, node in enumerate(nodes) if 6 <= _page_index(node, index + 1) <= 9]
    if s06_s09:
        return s06_s09
    total = len(nodes)
    if total < 4:
        return []
    return [index for index in range(total) if 0.35 <= index / max(total - 1, 1) <= 0.75]


def analyze_tension_curve(story_graph: dict[str, Any]) -> dict[str, Any]:
    nodes = _nodes_from_graph(story_graph)
    if not nodes:
        return {
            "curve": [],
            "midpoint_status": "missing",
            "failures": ["nodes_missing"],
            "recommended_repairs": [{"repair_action": "add_story_graph_nodes"}],
        }

    curve: list[dict[str, Any]] = []
    for index, node in enumerate(nodes):
        ending = index == len(nodes) - 1
        dimensions = {dimension: round(_dimension_score(node, dimension, ending), 2) for dimension in DIMENSIONS}
        overall = round(sum(dimensions.values()) / len(DIMENSIONS), 2)
        curve.append({"node_id": _node_id(node), "page_index": _page_index(node, index + 1), **dimensions, "overall": overall})

    failures: list[str] = []
    repairs: list[dict[str, Any]] = []
    if curve[0]["overall"] < 0.35:
        failures.append("weak_opening")
        repairs.append({"node_id": curve[0]["node_id"], "repair_action": "strengthen_opening_hook"})

    last = nodes[-1]
    if _blank(last.get("opening_callback")) and _blank(last.get("payoff_target")):
        failures.append("weak_ending_callback")
        repairs.append({"node_id": curve[-1]["node_id"], "repair_action": "add_ending_callback"})

    middle = _middle_indices(nodes)
    midpoint_status = "not_applicable"
    if len(middle) >= 2:
        scores = [curve[index]["overall"] for index in middle]
        increases = [later - earlier for earlier, later in zip(scores, scores[1:])]
        if len(scores) >= 3 and all(delta < -0.02 for delta in increases):
            midpoint_status = "declining"
            failures.append("middle_continuous_decline")
            repairs.append({"repair_action": "add_midpoint_escalation"})
        elif max(scores) - min(scores) < 0.08 or not any(delta > 0.04 for delta in increases):
            midpoint_status = "flat"
            failures.append("middle_without_escalation")
            repairs.append({"repair_action": "add_midpoint_information_gain"})
        else:
            midpoint_status = "upgrading"

    return {
        "curve": curve,
        "midpoint_status": midpoint_status,
        "failures": list(dict.fromkeys(failures)),
        "recommended_repairs": repairs,
    }
