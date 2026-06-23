from __future__ import annotations

from pathlib import Path
from typing import Any

from core.io import RUNTIME_ROOT, result
from lint_engine.semantic_lint import lint_asset
from prompt_compiler.compiler import compile_asset
from qa_engine.asset_qa import qa_asset
from skill_orchestrator.orchestrator import select_story_skills
from skill_runtime.evaluator import evaluate_node
from skill_runtime.patch_applier import apply_skill_patch
from skill_runtime.patch_generator import generate_skill_patch
from skill_runtime.repair_loop import repair_skill_graph
from telemetry.telemetry import validate_telemetry

import json


FIXTURE_DIR = RUNTIME_ROOT / "tests" / "fixtures"


def _load(name: str) -> dict[str, Any]:
    with (FIXTURE_DIR / name).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def run_smoke_tests() -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    valid_compile = compile_asset(_load("r00_valid_spec.json"))
    checks.append({"name": "valid R00 spec can compile", "passed": valid_compile["passed"]})

    invalid_stick = lint_asset(_load("r00_invalid_stick_figure_spec.json"))
    checks.append({"name": "R00 stick figure is blocked", "passed": not invalid_stick["passed"]})

    invalid_symbol = lint_asset(_load("r00_invalid_symbol_sheet_spec.json"))
    checks.append({"name": "R00 symbol sheet is blocked", "passed": not invalid_symbol["passed"]})

    telemetry = validate_telemetry(_load("telemetry_valid.json"))
    checks.append({"name": "valid telemetry passes", "passed": telemetry["passed"]})

    invalid_qa = qa_asset(_load("qa_r00_invalid.json"))
    checks.append({"name": "invalid QA blocks accepted", "passed": not invalid_qa["passed"]})

    plan = select_story_skills("horror", 12)
    checks.append(
        {
            "name": "12-page horror skill plan generated",
            "passed": bool(plan["selected_skill_set"]) and len(plan["node_skill_plan"]) == 12,
        }
    )

    valid_opening = evaluate_node(_load("node_valid_opening.json"))
    checks.append({"name": "valid opening node passes skill evaluator", "passed": valid_opening["passed"]})

    invalid_no_hook = evaluate_node(_load("node_invalid_no_hook.json"))
    checks.append({"name": "no_hook node is blocked", "passed": not invalid_no_hook["passed"]})

    invalid_no_next = evaluate_node(_load("node_invalid_no_next_question.json"))
    checks.append({"name": "no_next_question node is blocked", "passed": not invalid_no_next["passed"]})

    invalid_ending = evaluate_node(_load("node_invalid_ending_no_callback.json"))
    checks.append({"name": "ending_no_callback node is blocked", "passed": not invalid_ending["passed"]})

    invalid_graph = repair_skill_graph(_load("story_graph_invalid_skill_runtime.json"), dry_run=True)
    checks.append(
        {
            "name": "invalid graph generates repair_plan",
            "passed": not invalid_graph["passed"] and bool(invalid_graph["repair_plan"]),
        }
    )

    valid_graph = repair_skill_graph(_load("story_graph_valid_skill_runtime.json"), dry_run=True)
    checks.append({"name": "valid graph passes repair_loop", "passed": valid_graph["passed"]})

    patch = generate_skill_patch(
        _load("node_invalid_no_hook.json"),
        skill_failures=invalid_no_hook["skill_failures"],
        repair_targets=invalid_no_hook["repair_targets"],
    )
    checks.append({"name": "patch generator emits structured patch", "passed": bool(patch["patches"])})

    dry_run_node = _load("node_invalid_no_hook.json")
    before_dry_run = json.dumps(dry_run_node, sort_keys=True, ensure_ascii=False)
    dry_run_result = apply_skill_patch(dry_run_node, patch, dry_run=True)
    after_dry_run = json.dumps(dry_run_node, sort_keys=True, ensure_ascii=False)
    checks.append(
        {
            "name": "patch applier dry-run does not mutate input",
            "passed": dry_run_result["passed"] and before_dry_run == after_dry_run,
        }
    )

    generated_forbidden_artifacts = []
    for path in (RUNTIME_ROOT.parent / "故事项目").iterdir():
        if path.is_dir():
            generated_forbidden_artifacts.append(str(path))
    checks.append({"name": "no story project created", "passed": not generated_forbidden_artifacts})
    checks.append({"name": "no images generated", "passed": not list(RUNTIME_ROOT.rglob("*.png"))})
    checks.append({"name": "no execution package generated", "passed": not list(RUNTIME_ROOT.rglob("*执行包*"))})

    failed = [check for check in checks if not check["passed"]]
    return result(not failed, smoke_checks=checks, failed_checks=failed)
