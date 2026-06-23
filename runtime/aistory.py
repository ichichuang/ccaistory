#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

RUNTIME_ROOT = Path(__file__).resolve().parent
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.insert(0, str(RUNTIME_ROOT))

from artifact_registry.lineage import trace_lineage
from artifact_registry.registry import (
    check_registry,
    get_artifact,
    list_artifacts,
    query_artifacts,
    register_artifact,
    update_artifact_status,
    validate_artifact_by_id,
)
from core.io import PROJECT_ROOT, print_json, read_json, result
from contracts.sync_docs_check import check_contract_drift
from contracts.validate_contracts import validate_contracts
from graph_engine.graph_checks import check_graph
from lint_engine.semantic_lint import lint_asset_file, lint_compiled_file
from pipeline_runner.checkpoint import read_checkpoint_status
from pipeline_runner.executor import execute_pipeline
from pipeline_runner.planner import plan_pipeline
from pipeline_runner.recovery import resume_run
from pipeline_runner.run_manifest import list_runs, load_manifest
from prompt_compiler.compiler import compile_asset_file
from qa_engine.asset_qa import qa_asset_file
from skill_orchestrator.orchestrator import plan_node_skills, select_story_skills
from skill_registry.load_skills import load_skills, validate_skills
from skill_runtime.evaluator import evaluate_node
from skill_runtime.patch_generator import generate_skill_patch
from skill_runtime.repair_loop import repair_skill_graph
from skill_executor.candidate_scorer import score_candidate
from skill_executor.conflict_resolver import resolve_conflicts
from skill_executor.executor import execute_skill_graph, execute_skill_node
from state_machine.state_machine import ACTIONS, can_run, get_status
from story_analyzer.analyzer import analyze_story_core, analyze_story_graph
from story_analyzer.character_stakes import analyze_character_stakes
from story_analyzer.clue_ledger import analyze_clue_ledger
from story_analyzer.page_count_estimator import estimate_pages_for_story_core
from story_analyzer.story_type_classifier import classify_story_core
from story_analyzer.tension_curve import analyze_tension_curve
from telemetry.telemetry import validate_telemetry_file


def _parse_json_file(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_runtime() -> dict[str, Any]:
    schema_dir = RUNTIME_ROOT / "schemas"
    fixture_dir = RUNTIME_ROOT / "tests" / "fixtures"
    parsed: list[str] = []
    failures: list[str] = []
    for directory in (schema_dir, fixture_dir):
        if not directory.exists():
            failures.append(f"missing_directory:{directory.relative_to(PROJECT_ROOT)}")
            continue
        for path in sorted(directory.glob("*.json")):
            try:
                _parse_json_file(path)
                parsed.append(str(path.relative_to(PROJECT_ROOT)))
            except Exception as exc:  # pragma: no cover - reported via CLI
                failures.append(f"{path.relative_to(PROJECT_ROOT)}:{exc}")
    skill_validation = validate_skills()
    if not skill_validation["passed"]:
        failures.append("skill_registry_invalid")
    return result(not failures, parsed_json=parsed, skill_validation=skill_validation, failures=failures)


def smoke_test() -> dict[str, Any]:
    from tests.test_runtime_smoke import run_smoke_tests

    return run_smoke_tests()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="AI Story Compiler v0.1")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("status")
    sub.add_parser("validate")
    sub.add_parser("list-actions")
    sub.add_parser("list-contracts")
    sub.add_parser("validate-contracts")
    sub.add_parser("check-contract-drift")
    sub.add_parser("smoke-test")
    sub.add_parser("list-runs")

    artifact_register = sub.add_parser("artifact-register")
    artifact_register.add_argument("--artifact", required=True)
    artifact_register.add_argument("--registry")
    artifact_register.add_argument("--dry-run", action="store_true")

    artifact_list = sub.add_parser("artifact-list")
    artifact_list.add_argument("--project-id", default="")
    artifact_list.add_argument("--asset-id", default="")
    artifact_list.add_argument("--status", default="")
    artifact_list.add_argument("--registry")

    artifact_get = sub.add_parser("artifact-get")
    artifact_get.add_argument("--artifact-id", required=True)
    artifact_get.add_argument("--registry")

    artifact_update = sub.add_parser("artifact-update-status")
    artifact_update.add_argument("--artifact-id", required=True)
    artifact_update.add_argument("--status", required=True)
    artifact_update.add_argument("--registry")
    artifact_update.add_argument("--dry-run", action="store_true")

    artifact_lineage = sub.add_parser("artifact-lineage")
    artifact_lineage.add_argument("--artifact-id", required=True)
    artifact_lineage.add_argument("--registry")

    artifact_validate = sub.add_parser("artifact-validate")
    artifact_validate.add_argument("--artifact-id", required=True)
    artifact_validate.add_argument("--registry")

    artifact_check = sub.add_parser("artifact-check-registry")
    artifact_check.add_argument("--registry")

    analyze_story = sub.add_parser("analyze-story")
    analyze_story.add_argument("--story-core", required=True)

    analyze_graph = sub.add_parser("analyze-graph")
    analyze_graph.add_argument("--graph", required=True)

    classify_story = sub.add_parser("classify-story")
    classify_story.add_argument("--story-core", required=True)

    estimate_pages = sub.add_parser("estimate-pages")
    estimate_pages.add_argument("--story-core", required=True)

    analyze_clues = sub.add_parser("analyze-clues")
    analyze_clues.add_argument("--graph", required=True)

    analyze_tension = sub.add_parser("analyze-tension")
    analyze_tension.add_argument("--graph", required=True)

    analyze_stakes = sub.add_parser("analyze-stakes")
    analyze_stakes.add_argument("--graph", required=True)

    can = sub.add_parser("can-run")
    can.add_argument("--project", required=True)
    can.add_argument("--action", required=True)

    select = sub.add_parser("select-skills")
    select.add_argument("--story-type", default="horror")
    select.add_argument("--pages", type=int, required=True)

    plan = sub.add_parser("plan-node-skills")
    plan.add_argument("--story-type", default="horror")
    plan.add_argument("--page-role")
    plan.add_argument("--page-index", type=int, required=True)
    plan.add_argument("--pages", type=int, required=True)
    plan.add_argument("--suspense-type")

    evaluate = sub.add_parser("evaluate-node")
    evaluate.add_argument("--node", required=True)

    patch = sub.add_parser("generate-skill-patch")
    patch.add_argument("--node", required=True)

    skill_graph = sub.add_parser("check-skill-graph")
    skill_graph.add_argument("--graph", required=True)

    repair_graph = sub.add_parser("repair-skill-graph")
    repair_graph.add_argument("--graph", required=True)
    repair_graph.add_argument("--dry-run", action="store_true", default=True)

    execute_node = sub.add_parser("execute-skill-node")
    execute_node.add_argument("--node", required=True)

    execute_graph = sub.add_parser("execute-skill-graph")
    execute_graph.add_argument("--graph", required=True)

    score_skill_candidate = sub.add_parser("score-skill-candidate")
    score_skill_candidate.add_argument("--candidate", required=True)

    resolve_skill_conflicts = sub.add_parser("resolve-skill-conflicts")
    resolve_skill_conflicts.add_argument("--candidates", required=True)

    graph = sub.add_parser("check-graph")
    graph.add_argument("--project", required=True)

    compile_asset = sub.add_parser("compile-asset")
    compile_asset.add_argument("--spec", required=True)

    lint_asset = sub.add_parser("lint-asset")
    lint_asset.add_argument("--spec", required=True)

    lint_prompt = sub.add_parser("lint-prompt")
    lint_prompt.add_argument("--compiled", required=True)

    telemetry = sub.add_parser("validate-telemetry")
    telemetry.add_argument("--telemetry", required=True)

    qa = sub.add_parser("qa-asset")
    qa.add_argument("--qa", required=True)

    pipeline_plan = sub.add_parser("pipeline-plan")
    pipeline_plan.add_argument("--project")
    pipeline_plan.add_argument("--until", dest="requested_until", default="")

    pipeline_run = sub.add_parser("pipeline-run")
    pipeline_run.add_argument("--project")
    pipeline_run.add_argument("--until", dest="requested_until", default="")
    pipeline_run.add_argument("--dry-run", action="store_true", default=True)

    pipeline_status = sub.add_parser("pipeline-status")
    pipeline_status.add_argument("--run-id", required=True)

    pipeline_resume = sub.add_parser("pipeline-resume")
    pipeline_resume.add_argument("--run-id", required=True)
    pipeline_resume.add_argument("--dry-run", action="store_true", default=True)

    args = parser.parse_args(argv)

    if args.command == "status":
        payload = get_status()
    elif args.command == "validate":
        payload = validate_runtime()
    elif args.command == "list-actions":
        payload = {"actions": ACTIONS}
    elif args.command == "list-contracts":
        payload = {
            "contracts": [
                "runtime/contracts/state_machine.json",
                "runtime/contracts/visual_assets.json",
                "runtime/contracts/skill_definitions.json",
                "runtime/contracts/quality_gates.json",
                "runtime/contracts/pipeline_actions.json",
            ]
        }
    elif args.command == "validate-contracts":
        payload = validate_contracts()
    elif args.command == "check-contract-drift":
        payload = check_contract_drift()
    elif args.command == "list-runs":
        payload = list_runs()
    elif args.command == "artifact-register":
        payload = register_artifact(read_json(args.artifact), registry_path=args.registry, dry_run=args.dry_run)
    elif args.command == "artifact-list":
        if args.project_id or args.asset_id or args.status:
            payload = query_artifacts(
                project_id=args.project_id,
                asset_id=args.asset_id,
                status=args.status,
                registry_path=args.registry,
            )
        else:
            payload = list_artifacts(registry_path=args.registry)
    elif args.command == "artifact-get":
        payload = get_artifact(args.artifact_id, registry_path=args.registry)
    elif args.command == "artifact-update-status":
        payload = update_artifact_status(
            args.artifact_id,
            args.status,
            registry_path=args.registry,
            dry_run=args.dry_run,
        )
    elif args.command == "artifact-lineage":
        payload = trace_lineage(args.artifact_id, registry_path=args.registry)
    elif args.command == "artifact-validate":
        payload = validate_artifact_by_id(args.artifact_id, registry_path=args.registry)
    elif args.command == "artifact-check-registry":
        payload = check_registry(registry_path=args.registry)
    elif args.command == "analyze-story":
        payload = analyze_story_core(read_json(args.story_core))
    elif args.command == "analyze-graph":
        payload = analyze_story_graph(read_json(args.graph))
    elif args.command == "classify-story":
        payload = classify_story_core(read_json(args.story_core))
    elif args.command == "estimate-pages":
        payload = estimate_pages_for_story_core(read_json(args.story_core))
    elif args.command == "analyze-clues":
        payload = analyze_clue_ledger(read_json(args.graph))
    elif args.command == "analyze-tension":
        payload = analyze_tension_curve(read_json(args.graph))
    elif args.command == "analyze-stakes":
        payload = analyze_character_stakes(read_json(args.graph))
    elif args.command == "can-run":
        payload = can_run(args.project, args.action)
    elif args.command == "select-skills":
        payload = select_story_skills(args.story_type, args.pages)
    elif args.command == "plan-node-skills":
        payload = plan_node_skills(
            story_type=args.story_type,
            page_role=args.page_role,
            page_index=args.page_index,
            total_pages=args.pages,
            suspense_type=args.suspense_type,
        )
    elif args.command == "evaluate-node":
        payload = evaluate_node(read_json(args.node))
    elif args.command == "generate-skill-patch":
        node = read_json(args.node)
        evaluation = evaluate_node(node)
        payload = generate_skill_patch(
            node,
            skill_failures=evaluation["skill_failures"],
            repair_targets=evaluation["repair_targets"],
        )
    elif args.command == "check-skill-graph":
        payload = repair_skill_graph(read_json(args.graph), dry_run=True)
    elif args.command == "repair-skill-graph":
        payload = repair_skill_graph(read_json(args.graph), dry_run=True)
    elif args.command == "execute-skill-node":
        payload = execute_skill_node(read_json(args.node), dry_run=True)
    elif args.command == "execute-skill-graph":
        payload = execute_skill_graph(read_json(args.graph), dry_run=True)
    elif args.command == "score-skill-candidate":
        payload = score_candidate(read_json(args.candidate))
    elif args.command == "resolve-skill-conflicts":
        payload = resolve_conflicts(read_json(args.candidates))
    elif args.command == "check-graph":
        payload = check_graph(args.project)
    elif args.command == "compile-asset":
        payload = compile_asset_file(args.spec)
    elif args.command == "lint-asset":
        payload = lint_asset_file(args.spec)
    elif args.command == "lint-prompt":
        payload = lint_compiled_file(args.compiled)
    elif args.command == "validate-telemetry":
        payload = validate_telemetry_file(args.telemetry)
    elif args.command == "qa-asset":
        payload = qa_asset_file(args.qa)
    elif args.command == "pipeline-plan":
        payload = plan_pipeline(project_path=args.project, requested_until=args.requested_until)
    elif args.command == "pipeline-run":
        plan_result = plan_pipeline(project_path=args.project, requested_until=args.requested_until)
        payload = execute_pipeline(
            plan_result,
            project_path=args.project or "",
            requested_until=args.requested_until,
            dry_run=args.dry_run,
            command=f"pipeline-run --until {args.requested_until} --dry-run",
        )
    elif args.command == "pipeline-status":
        payload = read_checkpoint_status(args.run_id)
        if payload.get("passed"):
            try:
                payload["run_manifest"] = load_manifest(args.run_id)
            except Exception as exc:  # pragma: no cover - surfaced via CLI JSON
                payload["run_manifest_error"] = str(exc)
    elif args.command == "pipeline-resume":
        payload = resume_run(args.run_id, dry_run=args.dry_run)
    elif args.command == "smoke-test":
        payload = smoke_test()
    else:
        parser.error(f"Unknown command: {args.command}")

    print_json(payload)
    return 0 if payload.get("passed", True) else 1


if __name__ == "__main__":
    raise SystemExit(main())
