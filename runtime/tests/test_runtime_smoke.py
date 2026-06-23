from __future__ import annotations

from pathlib import Path
from typing import Any

from core.io import RUNTIME_ROOT, result
from contracts.contract_loader import load_contract, r00_required_questions
from contracts.validate_contracts import validate_contracts
from lint_engine.semantic_lint import lint_asset
from pipeline_runner.checkpoint import read_checkpoint_status, save_checkpoint
from pipeline_runner.executor import execute_pipeline
from pipeline_runner.planner import plan_pipeline
from pipeline_runner.recovery import resume_run
from pipeline_runner.run_manifest import list_runs
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

    contract_validation = validate_contracts()
    checks.append({"name": "validate-contracts passes", "passed": contract_validation["passed"]})

    visual_assets = load_contract("visual_assets")
    checks.append({"name": "visual_assets.json can load", "passed": bool(visual_assets.get("asset_types"))})

    checks.append({"name": "R00 QA comes from contract", "passed": len(r00_required_questions()) == 14})

    valid_compile = compile_asset(_load("r00_valid_spec.json"))
    checks.append({"name": "valid R00 spec can compile", "passed": valid_compile["passed"]})

    invalid_stick = lint_asset(_load("r00_invalid_stick_figure_spec.json"))
    checks.append({"name": "R00 stick figure is blocked", "passed": not invalid_stick["passed"]})
    checks.append(
        {
            "name": "semantic_lint reads R00 contract",
            "passed": "stick figure" in invalid_stick["semantic_lint_result"]["asset_scope_conflicts"],
        }
    )

    invalid_symbol = lint_asset(_load("r00_invalid_symbol_sheet_spec.json"))
    checks.append({"name": "R00 symbol sheet is blocked", "passed": not invalid_symbol["passed"]})

    telemetry = validate_telemetry(_load("telemetry_valid.json"))
    checks.append({"name": "valid telemetry passes", "passed": telemetry["passed"]})

    invalid_qa = qa_asset(_load("qa_r00_invalid.json"))
    checks.append({"name": "invalid QA blocks accepted", "passed": not invalid_qa["passed"]})
    checks.append(
        {
            "name": "asset_qa reads R00 contract",
            "passed": invalid_qa["asset_qa_result"]["details"][0]["question_id"] == "has_stick_figure",
        }
    )

    skill_contract = load_contract("skill_definitions")
    skills_json = _load("../../skill_registry/skills.json")
    checks.append(
        {
            "name": "skill_definitions matches skills.json count",
            "passed": len(skill_contract["skills"]) == len(skills_json["skills"]) == 12,
        }
    )

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

    empty_plan = plan_pipeline(requested_until="semantic_lint")
    expected_empty_plan = _load("pipeline_empty_plan_expected.json")
    checks.append(
        {
            "name": "pipeline-plan empty repository returns empty_state_plan",
            "passed": empty_plan == expected_empty_plan,
        }
    )

    valid_pipeline_plan = plan_pipeline(FIXTURE_DIR / "story_core_pipeline_valid.json", requested_until="semantic_lint")
    checks.append(
        {
            "name": "valid story_core generates pipeline plan",
            "passed": valid_pipeline_plan["passed"]
            and any(step["action_id"] == "run_semantic_lint" for step in valid_pipeline_plan["plan"]),
        }
    )

    blocked_pipeline_plan = plan_pipeline(
        FIXTURE_DIR / "story_core_pipeline_blocked.json",
        requested_until="semantic_lint",
    )
    checks.append(
        {
            "name": "blocked story_core blocks disallowed action",
            "passed": not blocked_pipeline_plan["passed"]
            and "action_blocked:run_semantic_lint" in blocked_pipeline_plan["blocked_reason"],
        }
    )

    pipeline_run = execute_pipeline(
        empty_plan,
        requested_until="semantic_lint",
        dry_run=True,
        command="smoke-test pipeline-run --until semantic_lint --dry-run",
    )
    run_result = pipeline_run.get("run_result", {})
    manifest_path = RUNTIME_ROOT.parent / run_result.get("run_manifest", "")
    checkpoint_path = RUNTIME_ROOT.parent / run_result.get("checkpoint", "")
    checks.append(
        {
            "name": "pipeline-run dry-run creates run manifest and checkpoint",
            "passed": pipeline_run["passed"] and manifest_path.exists() and checkpoint_path.exists(),
        }
    )

    pipeline_status = read_checkpoint_status(run_result.get("run_id", ""))
    checks.append(
        {
            "name": "pipeline-status can read run",
            "passed": pipeline_status["passed"] and pipeline_status["checkpoint"]["run_id"] == run_result.get("run_id"),
        }
    )

    manual_checkpoint = _load("pipeline_checkpoint_valid.json")
    save_checkpoint(manual_checkpoint)
    resume_result = resume_run("fixture_manual_approval", dry_run=True)
    checks.append(
        {
            "name": "pipeline-resume does not pass manual approval",
            "passed": resume_result["passed"] and resume_result["resume_status"] == "approval_required",
        }
    )

    runs = list_runs()
    checks.append(
        {
            "name": "list-runs is available",
            "passed": runs["passed"] and any(item["run_id"] == run_result.get("run_id") for item in runs["runs"]),
        }
    )

    generated_forbidden_artifacts = []
    for path in (RUNTIME_ROOT.parent / "故事项目").iterdir():
        if path.is_dir():
            generated_forbidden_artifacts.append(str(path))
    checks.append({"name": "pipeline does not create story project", "passed": not generated_forbidden_artifacts})
    image_artifacts = list(RUNTIME_ROOT.rglob("*.png")) + list((RUNTIME_ROOT.parent / "资产库").rglob("*.png"))
    checks.append({"name": "pipeline does not generate images", "passed": not image_artifacts})
    checks.append({"name": "pipeline does not generate execution package", "passed": not list(RUNTIME_ROOT.rglob("*执行包*"))})
    checks.append({"name": "pipeline does not generate publish package", "passed": not list(RUNTIME_ROOT.rglob("*发布包*"))})

    failed = [check for check in checks if not check["passed"]]
    return result(not failed, smoke_checks=checks, failed_checks=failed)
