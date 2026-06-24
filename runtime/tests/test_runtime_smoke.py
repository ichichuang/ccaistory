from __future__ import annotations

from pathlib import Path
from typing import Any
import json
import subprocess
import sys
import tempfile

from artifact_registry.hash_utils import json_sha256
from artifact_registry.lineage import trace_lineage
from artifact_registry.registry import check_registry, register_artifact
from core.io import RUNTIME_ROOT, result
from contracts.contract_loader import load_contract, r00_required_questions
from contracts.validate_contracts import validate_contracts
from lint_engine.semantic_lint import lint_asset
from multimodal_qa.artifact_bridge import create_image_qa_artifact_payload, register_image_qa_artifact
from multimodal_qa.manual_review import validate_image_review_form
from multimodal_qa.qa_merge import merge_image_review_to_asset_qa
from multimodal_qa.review_form_generator import generate_image_review_form
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
from skill_executor.candidate_scorer import score_candidate
from skill_executor.conflict_resolver import resolve_conflicts
from skill_executor.executor import execute_skill_graph, execute_skill_node
from story_analyzer.analyzer import analyze_story_core, analyze_story_graph
from story_analyzer.character_stakes import analyze_character_stakes
from story_analyzer.clue_ledger import analyze_clue_ledger
from story_analyzer.tension_curve import analyze_tension_curve
from telemetry.telemetry import validate_telemetry


FIXTURE_DIR = RUNTIME_ROOT / "tests" / "fixtures"


def _load(name: str) -> dict[str, Any]:
    with (FIXTURE_DIR / name).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def run_smoke_tests() -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    story_project_root = RUNTIME_ROOT.parent / "故事项目"
    existing_story_projects = {
        path.resolve()
        for path in story_project_root.iterdir()
        if path.is_dir()
    } if story_project_root.exists() else set()

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

    generated_review = generate_image_review_form(
        asset_type="R00_PAPER_MARK_ANCHOR",
        asset_id="fixture_asset_r00",
        candidate_id="fixture_candidate_alpha",
        artifact_id="fixture_generation_candidate",
    )
    checks.append(
        {
            "name": "R00 image review form has 14 contract QA plus common questions",
            "passed": generated_review["passed"]
            and generated_review["contract_question_count"] == 14
            and generated_review["common_question_count"] == 4
            and generated_review["question_count"] == 18,
        }
    )

    passed_review = _load("image_review_r00_passed.json")
    passed_merge = merge_image_review_to_asset_qa(passed_review)
    passed_asset_qa = qa_asset({"asset_qa_result": passed_merge["asset_qa_result"]})
    checks.append(
        {
            "name": "passed image review can merge to asset_qa_result",
            "passed": passed_merge["passed"] and passed_asset_qa["passed"],
        }
    )

    missing_review = validate_image_review_form(_load("image_review_r00_missing_required.json"))
    checks.append(
        {
            "name": "missing required image review stays pending and blocked",
            "passed": not missing_review["passed"]
            and missing_review["review_validation_result"]["decision"] == "pending"
            and missing_review["review_validation_result"]["allow_accepted"] is False,
        }
    )

    stick_review = validate_image_review_form(_load("image_review_r00_failed_stick_figure.json"))
    stick_merge = merge_image_review_to_asset_qa(_load("image_review_r00_failed_stick_figure.json"))
    stick_asset_qa = qa_asset({"asset_qa_result": stick_merge["asset_qa_result"]})
    checks.append(
        {
            "name": "stick figure image review fail is blocked",
            "passed": stick_review["passed"]
            and stick_review["review_validation_result"]["allow_accepted"] is False
            and "has_stick_figure" in stick_review["review_validation_result"]["hard_failures"]
            and not stick_asset_qa["passed"],
        }
    )

    symbol_review = validate_image_review_form(_load("image_review_r00_failed_symbol_sheet.json"))
    symbol_merge = merge_image_review_to_asset_qa(_load("image_review_r00_failed_symbol_sheet.json"))
    symbol_asset_qa = qa_asset({"asset_qa_result": symbol_merge["asset_qa_result"]})
    checks.append(
        {
            "name": "symbol sheet image review fail is blocked",
            "passed": symbol_review["passed"]
            and symbol_review["review_validation_result"]["allow_accepted"] is False
            and "is_symbol_sheet" in symbol_review["review_validation_result"]["hard_failures"]
            and not symbol_asset_qa["passed"],
        }
    )

    wrong_ratio_review = validate_image_review_form(_load("image_review_r00_wrong_ratio.json"))
    wrong_ratio_merge = merge_image_review_to_asset_qa(_load("image_review_r00_wrong_ratio.json"))
    wrong_ratio_asset_qa = qa_asset({"asset_qa_result": wrong_ratio_merge["asset_qa_result"]})
    checks.append(
        {
            "name": "wrong ratio image review fail is blocked",
            "passed": wrong_ratio_review["passed"]
            and wrong_ratio_review["review_validation_result"]["allow_accepted"] is False
            and "canvas_ratio_mismatch" in wrong_ratio_review["review_validation_result"]["hard_failures"]
            and not wrong_ratio_asset_qa["passed"],
        }
    )

    pending_review = validate_image_review_form(_load("image_review_r00_pending.json"))
    pending_merge = merge_image_review_to_asset_qa(_load("image_review_r00_pending.json"))
    pending_asset_qa = qa_asset({"asset_qa_result": pending_merge["asset_qa_result"]})
    checks.append(
        {
            "name": "pending image review cannot be accepted",
            "passed": pending_review["passed"]
            and pending_review["review_validation_result"]["allow_accepted"] is False
            and not pending_asset_qa["passed"],
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

    micro_analysis = analyze_story_core(_load("story_core_analyzer_micro_horror.json"))
    checks.append(
        {
            "name": "micro horror recommends 6-8 pages",
            "passed": 6 <= micro_analysis["page_count"]["recommended_pages"] <= 8,
        }
    )

    classic_analysis = analyze_story_core(_load("story_core_analyzer_classic_adaptation.json"))
    checks.append(
        {
            "name": "classic adaptation recommends at least 12 pages",
            "passed": classic_analysis["page_count"]["minimum_pages"] >= 12
            and classic_analysis["page_count"]["recommended_pages"] >= 12,
        }
    )

    weak_opening_analysis = analyze_story_graph(_load("story_graph_analyzer_weak_opening.json"))
    checks.append(
        {
            "name": "weak opening is diagnosed",
            "passed": any(
                "weak_opening_hook" in node["weaknesses"]
                for node in weak_opening_analysis["node_diagnostics"]
            ),
        }
    )

    missing_payoff_ledger = analyze_clue_ledger(_load("story_graph_analyzer_missing_payoff.json"))
    checks.append(
        {
            "name": "missing payoff is blocked by clue ledger",
            "passed": any(failure.startswith("unpaid_clue:") for failure in missing_payoff_ledger["failures"]),
        }
    )

    flat_middle_tension = analyze_tension_curve(_load("story_graph_analyzer_flat_middle.json"))
    checks.append(
        {
            "name": "flat middle is blocked by tension curve",
            "passed": "middle_without_escalation" in flat_middle_tension["failures"],
        }
    )

    weak_stakes = analyze_character_stakes(_load("story_graph_analyzer_weak_stakes.json"))
    checks.append(
        {
            "name": "weak stakes are blocked by character stakes",
            "passed": not weak_stakes["passed"] and bool(weak_stakes["missing_stakes"]),
        }
    )

    valid_analyzer_result = analyze_story_graph(_load("story_graph_analyzer_valid.json"))
    checks.append(
        {
            "name": "analyzer pass outputs recommended_skill_plan",
            "passed": valid_analyzer_result["passed"]
            and bool(valid_analyzer_result["recommended_skill_plan"]["selected_skill_set"]),
        }
    )

    cli_result = subprocess.run(
        [
            sys.executable,
            str(RUNTIME_ROOT / "aistory.py"),
            "analyze-graph",
            "--graph",
            str(FIXTURE_DIR / "story_graph_analyzer_valid.json"),
        ],
        cwd=RUNTIME_ROOT.parent,
        capture_output=True,
        text=True,
        check=False,
    )
    try:
        cli_payload = json.loads(cli_result.stdout)
    except json.JSONDecodeError:
        cli_payload = {}
    checks.append(
        {
            "name": "CLI analyze-graph is available",
            "passed": cli_result.returncode == 0 and cli_payload.get("passed") is True,
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

    executor_invalid_node = execute_skill_node(_load("node_executor_needs_hook.json"), dry_run=True)
    checks.append(
        {
            "name": "invalid node generates proposed_changes",
            "passed": not executor_invalid_node["passed"] and bool(executor_invalid_node["proposed_changes"]),
        }
    )
    checks.append(
        {
            "name": "proposed_changes require human approval",
            "passed": executor_invalid_node["manual_approval_required"]
            and all(change.get("human_approval_required") is True for change in executor_invalid_node["proposed_changes"]),
        }
    )

    executor_valid_node = execute_skill_node(_load("node_executor_valid.json"), dry_run=True)
    checks.append(
        {
            "name": "valid node does not generate meaningless proposed_changes",
            "passed": executor_valid_node["passed"] and not executor_valid_node["proposed_changes"],
        }
    )

    executor_invalid_graph = execute_skill_graph(_load("story_graph_executor_invalid.json"), dry_run=True)
    checks.append(
        {
            "name": "invalid graph generates executor proposed_changes",
            "passed": not executor_invalid_graph["passed"] and bool(executor_invalid_graph["proposed_changes"]),
        }
    )

    executor_valid_graph = execute_skill_graph(_load("story_graph_executor_valid.json"), dry_run=True)
    checks.append(
        {
            "name": "valid graph passes skill executor",
            "passed": executor_valid_graph["passed"] and not executor_valid_graph["proposed_changes"],
        }
    )

    author_style_score = score_candidate(_load("skill_candidate_invalid_author_style.json"))
    checks.append(
        {
            "name": "author style candidate is blocked",
            "passed": not author_style_score["passed"]
            and "author_style_instruction" in author_style_score["hard_failures"],
        }
    )

    empty_scare_score = score_candidate(_load("skill_candidate_invalid_empty_scare.json"))
    checks.append(
        {
            "name": "empty scare candidate is blocked",
            "passed": not empty_scare_score["passed"] and "empty_scare" in empty_scare_score["hard_failures"],
        }
    )

    valid_candidate_score = score_candidate(_load("skill_candidate_valid.json"))
    checks.append(
        {
            "name": "valid candidate receives accept recommendation",
            "passed": valid_candidate_score["passed"]
            and valid_candidate_score["recommendation"] == "accept_candidate",
        }
    )

    conflict_result = resolve_conflicts(_load("skill_candidates_conflict.json"))
    checks.append(
        {
            "name": "conflict resolver emits resolution_plan",
            "passed": bool(conflict_result["resolution_plan"]["conflicts"])
            and conflict_result["resolution_plan"]["manual_review_required"],
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
    checks.append(
        {
            "name": "pipeline plan includes story analyzer gate",
            "passed": valid_pipeline_plan["passed"]
            and any(
                step["action_id"] == "analyze_story_graph" and step["gate"] == "story_analyzer_gate"
                for step in valid_pipeline_plan["plan"]
            ),
        }
    )
    checks.append(
        {
            "name": "pipeline plan includes skill executor manual stage",
            "passed": valid_pipeline_plan["passed"]
            and any(step["action_id"] == "execute_skill_graph" for step in valid_pipeline_plan["plan"])
            and any(
                step["action_id"] == "review_skill_executor_proposed_changes"
                and step["manual_approval_required"]
                for step in valid_pipeline_plan["plan"]
            ),
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

    high_risk_plan = {
        "passed": True,
        "next_allowed_action": "analyze_story_graph",
        "blocked_reason": [],
        "plan": [
            {
                "step_id": "step_01_analyze_story_graph",
                "action_id": "analyze_story_graph",
                "required_inputs": ["story_graph", "skill_runtime_result"],
                "expected_outputs": ["story_analysis_result", "recommended_skill_plan", "repair_priority"],
                "gate": "story_analyzer_gate",
                "manual_approval_required": False,
            },
            {
                "step_id": "step_02_execute_skill_graph",
                "action_id": "execute_skill_graph",
                "required_inputs": ["story_graph", "skill_runtime_result", "story_analysis_result"],
                "expected_outputs": ["skill_executor_result", "proposed_changes"],
                "gate": "skill_executor_gate",
                "manual_approval_required": False,
            },
        ],
        "story_core_path": str(FIXTURE_DIR / "story_graph_analyzer_missing_payoff.json"),
    }
    blocked_by_analyzer = execute_pipeline(
        high_risk_plan,
        project_path=str(FIXTURE_DIR / "story_graph_analyzer_missing_payoff.json"),
        requested_until="execute_skill_graph",
        dry_run=True,
        command="smoke-test analyzer gate",
    )
    checks.append(
        {
            "name": "analyzer high risk does not enter skill executor",
            "passed": not blocked_by_analyzer["passed"]
            and blocked_by_analyzer["run_result"]["stopped_at"] == "step_01_analyze_story_graph"
            and not blocked_by_analyzer["run_result"]["executed_steps"],
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

    artifact_hash = json_sha256({"artifact": "fixture"})
    checks.append(
        {
            "name": "artifact hash can be generated",
            "passed": bool(artifact_hash.get("hash")) and artifact_hash.get("algorithm") == "sha256",
        }
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        registry_path = Path(temp_dir) / "registry.json"
        artifact_fixture_names = [
            "artifact_visual_asset_spec.json",
            "artifact_compiled_prompt.json",
            "artifact_semantic_lint_result.json",
            "artifact_generation_candidate.json",
            "artifact_execution_telemetry.json",
            "artifact_asset_qa_passed.json",
            "artifact_accepted_reference_asset_valid.json",
        ]
        artifact_registrations = [
            register_artifact(_load(name), registry_path=registry_path)
            for name in artifact_fixture_names
        ]
        checks.append(
            {
                "name": "registry can register artifact chain",
                "passed": all(item["passed"] for item in artifact_registrations),
            }
        )

        image_qa_payload = create_image_qa_artifact_payload(
            _load("image_review_r00_passed.json"),
            registry_path=str(registry_path),
            source_path="runtime/tests/fixtures/image_review_r00_passed.json",
        )
        image_qa_registration = register_image_qa_artifact(
            _load("image_review_r00_passed.json"),
            registry_path=str(registry_path),
            source_path="runtime/tests/fixtures/image_review_r00_passed.json",
        )
        checks.append(
            {
                "name": "register-image-qa-artifact can generate artifact payload",
                "passed": image_qa_payload["passed"]
                and image_qa_payload["artifact"]["artifact_type"] == "asset_qa_result"
                and image_qa_registration["passed"],
            }
        )

        duplicate_artifact = register_artifact(_load("artifact_visual_asset_spec.json"), registry_path=registry_path)
        checks.append(
            {
                "name": "duplicate artifact_id is blocked",
                "passed": not duplicate_artifact["passed"] and "duplicate_artifact_id" in duplicate_artifact["failures"],
            }
        )

        valid_lineage = trace_lineage("fixture_accepted_reference_asset_valid", registry_path=str(registry_path))
        checks.append(
            {
                "name": "accepted reference asset passes telemetry and QA",
                "passed": valid_lineage["passed"] and not valid_lineage["missing_required_ancestors"],
            }
        )
        checks.append(
            {
                "name": "lineage traces accepted asset to compiled_prompt",
                "passed": any(
                    item["artifact_type"] == "compiled_prompt"
                    for item in valid_lineage["lineage"]
                ),
            }
        )

        missing_qa = register_artifact(
            _load("artifact_accepted_reference_asset_missing_qa.json"),
            registry_path=registry_path,
        )
        checks.append(
            {
                "name": "accepted reference asset missing image QA is blocked",
                "passed": not missing_qa["passed"]
                and any("accepted_reference_asset" in failure for failure in missing_qa["failures"]),
            }
        )

        rejected_registration = register_artifact(_load("artifact_rejected_asset.json"), registry_path=registry_path)
        rejected_reference_layout = {
            "artifact_id": "fixture_platform_layout_rejected_reference",
            "artifact_type": "platform_page_layout",
            "project_id": "fixture_project",
            "story_id": "fixture_story",
            "asset_id": "fixture_asset_r00",
            "run_id": "fixture_run",
            "candidate_id": "",
            "source_path": "",
            "content_hash": {
                "hash": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "algorithm": "sha256",
            },
            "source_hash": {
                "hash": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "algorithm": "sha256",
            },
            "parent_artifact_ids": [],
            "dependency_artifact_ids": ["fixture_rejected_asset"],
            "created_at": "2026-06-23T00:00:00Z",
            "status": "draft",
            "metadata": {"reference_dependency_ids": ["fixture_rejected_asset"]},
        }
        rejected_reference = register_artifact(rejected_reference_layout, registry_path=registry_path)
        checks.append(
            {
                "name": "rejected asset cannot be used as reference",
                "passed": rejected_registration["passed"] and not rejected_reference["passed"],
            }
        )

        registry_check = check_registry(registry_path=registry_path)
        checks.append(
            {
                "name": "artifact registry has zero broken lineage links",
                "passed": registry_check["passed"] and registry_check["broken_link_count"] == 0,
            }
        )

    generated_forbidden_artifacts = []
    if story_project_root.exists():
        for path in story_project_root.iterdir():
            if path.is_dir() and path.resolve() not in existing_story_projects:
                generated_forbidden_artifacts.append(str(path))
    checks.append({"name": "pipeline does not create story project", "passed": not generated_forbidden_artifacts})
    image_artifacts = list(RUNTIME_ROOT.rglob("*.png")) + list((RUNTIME_ROOT.parent / "资产库").rglob("*.png"))
    checks.append({"name": "pipeline does not generate images", "passed": not image_artifacts})
    checks.append({"name": "pipeline does not generate execution package", "passed": not list(RUNTIME_ROOT.rglob("*执行包*"))})
    checks.append({"name": "pipeline does not generate publish package", "passed": not list(RUNTIME_ROOT.rglob("*发布包*"))})
    checks.append({"name": "skill executor does not create story project", "passed": not generated_forbidden_artifacts})
    checks.append({"name": "skill executor does not generate images", "passed": not image_artifacts})
    checks.append({"name": "skill executor does not generate execution package", "passed": not list(RUNTIME_ROOT.rglob("*执行包*"))})
    checks.append({"name": "registry does not create story project", "passed": not generated_forbidden_artifacts})
    checks.append({"name": "registry does not generate images", "passed": not image_artifacts})
    checks.append({"name": "registry does not generate execution package", "passed": not list(RUNTIME_ROOT.rglob("*执行包*"))})
    checks.append({"name": "registry does not generate publish package", "passed": not list(RUNTIME_ROOT.rglob("*发布包*"))})

    failed = [check for check in checks if not check["passed"]]
    return result(not failed, smoke_checks=checks, failed_checks=failed)
