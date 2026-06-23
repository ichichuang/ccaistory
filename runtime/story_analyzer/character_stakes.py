from __future__ import annotations

from typing import Any


STAKE_FIELDS = [
    "protagonist_want",
    "protagonist_fear",
    "reader_care_reason",
    "relationship_signal",
    "emotional_turn",
]


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


def _has_choice(node: dict[str, Any]) -> bool:
    return any(not _blank(node.get(field)) for field in ("character_choice", "protagonist_choice", "decision", "choice", "action_choice"))


def _observer_only(node: dict[str, Any]) -> bool:
    text = _text(node.get("typed_narration")).lower()
    observer_terms = ("observes", "watches", "sees", "notices", "looks", "看见", "看到", "观察", "发现")
    return any(term in text for term in observer_terms) and not _has_choice(node)


def _abstract_emotion_only(node: dict[str, Any]) -> bool:
    emotional_turn = _text(node.get("emotional_turn")).lower()
    abstract_terms = ("fear", "afraid", "sad", "lonely", "scared", "worried", "害怕", "恐惧", "难过", "孤独", "担心")
    if not emotional_turn or not any(term in emotional_turn for term in abstract_terms):
        return False
    return all(_blank(node.get(field)) for field in ("concrete_behavior", "character_action", "body_signal", "relationship_signal", "character_choice"))


def _graph_value(story_graph: dict[str, Any], field: str) -> Any:
    if field in story_graph:
        return story_graph[field]
    nested = story_graph.get("story_graph")
    if isinstance(nested, dict) and field in nested:
        return nested[field]
    return None


def analyze_character_stakes(story_graph: dict[str, Any]) -> dict[str, Any]:
    nodes = _nodes_from_graph(story_graph)
    missing_stakes: list[str] = []
    for field in STAKE_FIELDS:
        if _blank(_graph_value(story_graph, field)) and all(_blank(node.get(field)) for node in nodes):
            missing_stakes.append(field)

    weak_nodes: list[dict[str, Any]] = []
    for node in nodes:
        failures: list[str] = []
        if _blank(_graph_value(story_graph, "reader_care_reason")) and _blank(node.get("reader_care_reason")):
            failures.append("reader_care_reason_missing")
        if _observer_only(node):
            failures.append("observer_without_choice")
        if _abstract_emotion_only(node):
            failures.append("abstract_emotion_without_behavior")
        if failures:
            weak_nodes.append({"node_id": _node_id(node), "failures": failures})

    if nodes and not any(_has_choice(node) for node in nodes):
        if "protagonist_choice" not in missing_stakes:
            missing_stakes.append("protagonist_choice")

    recommended_skills = ["emotional_pull"]
    if any("child" in _text(node).lower() or "孩子" in _text(node) for node in nodes):
        recommended_skills.append("child_perspective_wonder")

    return {
        "passed": not missing_stakes and not weak_nodes,
        "missing_stakes": list(dict.fromkeys(missing_stakes)),
        "weak_nodes": weak_nodes,
        "recommended_skills": list(dict.fromkeys(recommended_skills if (missing_stakes or weak_nodes) else [])),
    }
