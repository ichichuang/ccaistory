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

from core.io import PROJECT_ROOT, print_json, read_json, result
from contracts.sync_docs_check import check_contract_drift
from contracts.validate_contracts import validate_contracts
from graph_engine.graph_checks import check_graph
from lint_engine.semantic_lint import lint_asset_file, lint_compiled_file
from prompt_compiler.compiler import compile_asset_file
from qa_engine.asset_qa import qa_asset_file
from skill_orchestrator.orchestrator import plan_node_skills, select_story_skills
from skill_registry.load_skills import load_skills, validate_skills
from skill_runtime.evaluator import evaluate_node
from skill_runtime.patch_generator import generate_skill_patch
from skill_runtime.repair_loop import repair_skill_graph
from state_machine.state_machine import ACTIONS, can_run, get_status
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
    elif args.command == "smoke-test":
        payload = smoke_test()
    else:
        parser.error(f"Unknown command: {args.command}")

    print_json(payload)
    return 0 if payload.get("passed", True) else 1


if __name__ == "__main__":
    raise SystemExit(main())
