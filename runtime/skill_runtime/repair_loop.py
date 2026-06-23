from __future__ import annotations

from typing import Any

from core.io import result
from skill_runtime.evaluator import evaluate_node
from skill_runtime.patch_applier import apply_skill_patch
from skill_runtime.patch_generator import generate_skill_patch


def _nodes_from_graph(story_graph: dict[str, Any]) -> list[dict[str, Any]]:
    if isinstance(story_graph.get("nodes"), list):
        return [node for node in story_graph["nodes"] if isinstance(node, dict)]
    nested = story_graph.get("story_graph")
    if isinstance(nested, dict) and isinstance(nested.get("nodes"), list):
        return [node for node in nested["nodes"] if isinstance(node, dict)]
    return []


def repair_skill_graph(story_graph: dict[str, Any], dry_run: bool = True) -> dict[str, Any]:
    nodes = _nodes_from_graph(story_graph)
    failed_nodes: list[str] = []
    repair_nodes: list[dict[str, Any]] = []
    evaluations: list[dict[str, Any]] = []

    for node in nodes:
        evaluation = evaluate_node(node, total_nodes=len(nodes))
        evaluations.append(evaluation)
        if evaluation["passed"]:
            continue

        patch = generate_skill_patch(
            node,
            skill_failures=evaluation["skill_failures"],
            repair_targets=evaluation["repair_targets"],
        )
        applied = apply_skill_patch(node, patch, dry_run=dry_run)
        failed_nodes.append(evaluation["node_id"])
        repair_nodes.append(
            {
                "node_id": evaluation["node_id"],
                "evaluation": evaluation,
                "patch": patch,
                "dry_run": dry_run,
                "required_rewrite_fields": applied["required_rewrite_fields"],
            }
        )

    if not nodes:
        return result(
            False,
            failed_nodes=[],
            repair_plan=[],
            graph_repair_plan={"failed_count": 0, "nodes": [], "graph_failure": "nodes_missing"},
            next_action="repair_story_graph_with_skill_patches",
            evaluations=[],
        )

    passed = not failed_nodes
    graph_repair_plan = {
        "failed_count": len(failed_nodes),
        "nodes": repair_nodes,
    }
    return result(
        passed,
        failed_nodes=failed_nodes,
        repair_plan=repair_nodes,
        graph_repair_plan=graph_repair_plan,
        next_action="proceed_to_visual_manifest_or_next_gate" if passed else "repair_story_graph_with_skill_patches",
        evaluations=evaluations,
    )
