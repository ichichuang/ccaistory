from __future__ import annotations

from copy import deepcopy
from typing import Any

from contracts.contract_loader import load_all_contracts
from core.io import result
from skill_registry.load_skills import load_skills
from skill_runtime.evaluator import evaluate_node
from skill_runtime.patch_generator import generate_skill_patch
from skill_executor.candidate_generator import generate_candidates
from skill_executor.candidate_scorer import score_candidate
from skill_executor.conflict_resolver import resolve_conflicts
from skill_executor.proposed_changes import build_proposed_changes


def _node_id(node: dict[str, Any]) -> str:
    return str(node.get("node_id") or node.get("id") or node.get("page_id") or node.get("page_index") or "")


def _nodes_from_graph(story_graph: dict[str, Any]) -> list[dict[str, Any]]:
    if isinstance(story_graph.get("nodes"), list):
        return [node for node in story_graph["nodes"] if isinstance(node, dict)]
    nested = story_graph.get("story_graph")
    if isinstance(nested, dict) and isinstance(nested.get("nodes"), list):
        return [node for node in nested["nodes"] if isinstance(node, dict)]
    return []


def _execute_single(
    node: dict[str, Any],
    *,
    skills: list[dict[str, Any]],
    contracts: dict[str, Any],
    total_nodes: int | None = None,
) -> dict[str, Any]:
    evaluation = evaluate_node(node, skills=skills, total_nodes=total_nodes)
    if evaluation["passed"]:
        return {
            "node_id": evaluation["node_id"],
            "evaluation": evaluation,
            "patch": {"node_id": evaluation["node_id"], "patches": [], "source_failures": []},
            "candidates": [],
            "scored_candidates": [],
            "conflict_resolution": resolve_conflicts([]),
            "proposed_changes": {"node_id": evaluation["node_id"], "proposed_changes": []},
        }

    patch = generate_skill_patch(
        node,
        skill_failures=evaluation["skill_failures"],
        repair_targets=evaluation["repair_targets"],
        skills=skills,
    )
    candidate_result = generate_candidates(node, patch, skills=skills, contracts=contracts)
    candidates = candidate_result["candidates"]
    scored = [score_candidate(candidate, skills=skills) for candidate in candidates]
    conflict_resolution = resolve_conflicts(candidates, scored)
    proposed = build_proposed_changes(node, candidates, scored)

    return {
        "node_id": evaluation["node_id"],
        "evaluation": evaluation,
        "patch": patch,
        "candidates": candidates,
        "scored_candidates": scored,
        "conflict_resolution": conflict_resolution,
        "proposed_changes": proposed,
    }


def execute_skill_node(
    node: dict[str, Any],
    *,
    dry_run: bool = True,
    skills: list[dict[str, Any]] | None = None,
    contracts: dict[str, Any] | None = None,
) -> dict[str, Any]:
    target = deepcopy(node)
    loaded_skills = skills if skills is not None else load_skills()
    loaded_contracts = contracts if contracts is not None else load_all_contracts()
    node_result = _execute_single(target, skills=loaded_skills, contracts=loaded_contracts)
    proposed_changes = node_result["proposed_changes"]["proposed_changes"]
    failed_nodes = [] if node_result["evaluation"]["passed"] else [node_result["node_id"]]
    return result(
        not failed_nodes,
        mode="node",
        dry_run=dry_run,
        failed_nodes=failed_nodes,
        node_results=[node_result],
        proposed_changes=proposed_changes,
        manual_approval_required=bool(proposed_changes),
        next_action="review_skill_executor_proposed_changes" if proposed_changes else "proceed_to_next_gate",
    )


def execute_skill_graph(
    story_graph: dict[str, Any],
    *,
    dry_run: bool = True,
    skills: list[dict[str, Any]] | None = None,
    contracts: dict[str, Any] | None = None,
) -> dict[str, Any]:
    graph_copy = deepcopy(story_graph)
    loaded_skills = skills if skills is not None else load_skills()
    loaded_contracts = contracts if contracts is not None else load_all_contracts()
    nodes = _nodes_from_graph(graph_copy)
    if not nodes:
        return result(
            False,
            mode="graph",
            dry_run=dry_run,
            failed_nodes=[],
            node_results=[],
            proposed_changes=[],
            manual_approval_required=False,
            next_action="repair_story_graph_with_skill_patches",
            graph_failure="nodes_missing",
        )

    node_results = [
        _execute_single(node, skills=loaded_skills, contracts=loaded_contracts, total_nodes=len(nodes)) for node in nodes
    ]
    failed_nodes = [item["node_id"] for item in node_results if not item["evaluation"]["passed"]]
    proposed_changes = [
        {"node_id": item["node_id"], **change}
        for item in node_results
        for change in item["proposed_changes"]["proposed_changes"]
    ]

    return result(
        not failed_nodes,
        mode="graph",
        dry_run=dry_run,
        failed_nodes=failed_nodes,
        node_results=node_results,
        proposed_changes=proposed_changes,
        manual_approval_required=bool(proposed_changes),
        next_action="review_skill_executor_proposed_changes" if proposed_changes else "proceed_to_next_gate",
    )
