from __future__ import annotations

from typing import Any

from core.io import find_story_core, load_json_file, result


REQUIRED_NODE_FIELDS = ["typed_hook", "typed_narration", "final_hook_sentence", "applied_skills"]


def _node_id(node: dict[str, Any]) -> str:
    return str(node.get("node_id") or node.get("id") or node.get("page_id") or node.get("page_index"))


def _has_new_problem(node: dict[str, Any]) -> bool:
    for field in ("next_page_question", "new_question", "new_problem"):
        value = node.get(field)
        if isinstance(value, str) and value.strip():
            return True
    return False


def check_graph(project_path: str) -> dict[str, Any]:
    story_core_path = find_story_core(project_path)
    if story_core_path is None:
        return result(False, graph_check_result={"failed_rules": ["story_core_missing"]})

    story_core = load_json_file(story_core_path)
    story_graph = story_core.get("story_graph", {})
    nodes = story_graph.get("nodes", [])
    edges = story_graph.get("edges", [])
    failed: list[str] = []
    details: list[dict[str, Any]] = []

    if not isinstance(nodes, list) or not nodes:
        failed.append("nodes_missing")
    if not isinstance(edges, list):
        failed.append("edges_not_list")
        edges = []

    if isinstance(nodes, list):
        for index, node in enumerate(nodes):
            if not isinstance(node, dict):
                failed.append("node_not_object")
                continue
            for field in REQUIRED_NODE_FIELDS:
                value = node.get(field)
                if value in (None, "", []):
                    failed.append(f"missing_{field}")
                    details.append({"node": _node_id(node), "field": field})

        node_ids = [_node_id(node) for node in nodes if isinstance(node, dict)]
        edge_pairs = {
            (
                str(edge.get("from") or edge.get("source")),
                str(edge.get("to") or edge.get("target")),
            )
            for edge in edges
            if isinstance(edge, dict)
        }
        for left, right in zip(node_ids, node_ids[1:]):
            if (left, right) not in edge_pairs:
                failed.append("edge_continuity_broken")
                details.append({"from": left, "to": right})

        for left, right in zip(nodes, nodes[1:]):
            if isinstance(left, dict) and isinstance(right, dict):
                if not _has_new_problem(left) and not _has_new_problem(right):
                    failed.append("two_consecutive_pages_without_new_problem")
                    details.append({"nodes": [_node_id(left), _node_id(right)]})

        if len(nodes) >= 2 and isinstance(nodes[-1], dict):
            ending = nodes[-1]
            if not (
                ending.get("opening_callback")
                or ending.get("callbacks_opening")
                or ending.get("ending_echoes_opening")
            ):
                failed.append("ending_does_not_callback_opening")

    failed_unique = list(dict.fromkeys(failed))
    return result(
        not failed_unique,
        graph_check_result={
            "node_count": len(nodes) if isinstance(nodes, list) else 0,
            "edge_count": len(edges),
            "failed_rules": failed_unique,
            "details": details,
        },
    )
