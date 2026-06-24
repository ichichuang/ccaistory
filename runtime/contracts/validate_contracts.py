from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


RUNTIME_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = RUNTIME_ROOT.parent
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.insert(0, str(RUNTIME_ROOT))

from contracts.contract_loader import CONTRACTS_DIR, REQUIRED_CONTRACT_FILES, ContractError, load_contract
from core.io import result


EXPECTED_ASSET_TYPES = [
    "R00_PAPER_MARK_ANCHOR",
    "R01_CHARACTER_ANCHOR",
    "R02_SCENE_PROP_ANCHOR",
    "P01_PLATFORM_LAYOUT_SAMPLE",
    "S_SOURCE_ILLUSTRATION",
]

EXPECTED_GATES = [
    "story_core_gate",
    "page_count_gate",
    "skill_selection_gate",
    "skill_runtime_gate",
    "story_analyzer_gate",
    "skill_executor_gate",
    "graph_integrity_gate",
    "visual_asset_ontology_gate",
    "prompt_compile_gate",
    "semantic_lint_gate",
    "telemetry_gate",
    "asset_qa_gate",
    "human_acceptance_gate",
]

EXPECTED_ACTIONS = [
    "create_story_core",
    "assess_page_count",
    "select_skills",
    "apply_skill_runtime",
    "analyze_story_graph",
    "repair_story_graph_before_skill_executor",
    "execute_skill_node",
    "execute_skill_graph",
    "review_skill_executor_proposed_changes",
    "apply_approved_skill_changes",
    "check_story_graph",
    "build_visual_asset_specs",
    "compile_prompts",
    "run_semantic_lint",
    "generate_source_pilot_task_list",
    "record_execution_telemetry",
    "generate_image_review_form",
    "validate_image_review",
    "merge_image_qa",
    "register_image_qa_artifact",
    "review_asset_for_acceptance",
    "run_asset_qa",
    "accept_asset",
    "reject_asset",
    "build_platform_page_layout",
    "run_human_complete_reading",
]

EXPECTED_STATES = [
    "empty",
    "story_core_created",
    "minimum_viable_story",
    "page_count_assessed",
    "skill_selected",
    "skill_runtime_checked",
    "story_analyzed",
    "story_analysis_blocked",
    "skill_executor_checked",
    "skill_executor_reviewed",
    "skill_executor_applied",
    "skill_executor_passed",
    "story_graph_ready",
    "platform_story_reading_test",
    "visual_asset_specs_ready",
    "prompts_compiled",
    "semantic_lint_passed",
    "source_pilot_ready",
    "source_pilot_generation",
    "asset_qa_pending",
    "image_review_form_pending",
    "image_review_validated",
    "image_qa_merged",
    "image_qa_registered",
    "asset_acceptance_reviewed",
    "asset_accepted",
    "asset_rejected",
    "platform_layout_ready",
    "human_complete_reading_passed",
    "publish_ready",
]

ASSET_KEYS = [
    "asset_type",
    "purpose",
    "required_fields",
    "allowed_content",
    "forbidden_content",
    "required_canvas",
    "required_text_policy",
    "required_reference_policy",
    "hard_failures",
    "qa_questions",
    "unlocks_after_acceptance",
]

VISUAL_ASSET_SPEC_REQUIRED_FIELDS = [
    "asset_id",
    "asset_type",
    "asset_scope",
    "allowed_content",
    "forbidden_content",
    "visual_center",
    "density_range",
    "composition_mode",
    "text_policy",
    "paper_policy",
    "style_policy",
    "reference_dependencies",
    "acceptance_questions",
    "repair_policy",
]

GATE_KEYS = [
    "gate_id",
    "required_inputs",
    "pass_conditions",
    "fail_conditions",
    "next_allowed_action_on_pass",
    "next_allowed_action_on_fail",
    "blocked_actions",
]

ACTION_KEYS = [
    "action_id",
    "required_state",
    "required_gate_result",
    "required_inputs",
    "outputs",
    "blocked_if",
    "next_action_on_pass",
    "next_action_on_fail",
]

STATE_KEYS = [
    "state_id",
    "allowed_actions",
    "blocked_actions",
    "required_artifacts",
    "next_states",
]

SKILL_CONSISTENCY_FIELDS = ["skill_id", "input_fields", "output_fields", "hard_failures", "repair_actions"]
AUTHOR_STYLE_PATTERNS = ["style of", "by artist", "模仿某作者", "仿照某作者", "以某作者"]
HISTORICAL_STORY_PATTERNS = ["KHN2_", "故事000", "story_project_"]


def _relative(path: Path) -> str:
    return str(path.relative_to(PROJECT_ROOT))


def _append_missing_keys(failures: list[str], namespace: str, data: dict[str, Any], required: list[str]) -> None:
    missing = [key for key in required if key not in data]
    if missing:
        failures.append(f"{namespace}:missing_keys:{','.join(missing)}")


def _load_json_contracts(failures: list[str]) -> list[str]:
    parsed: list[str] = []
    for name in REQUIRED_CONTRACT_FILES:
        path = CONTRACTS_DIR / name
        if not path.exists():
            failures.append(f"missing_contract:{_relative(path)}")
            continue
        try:
            with path.open("r", encoding="utf-8") as handle:
                data = json.load(handle)
            if not isinstance(data, dict):
                failures.append(f"contract_root_not_object:{_relative(path)}")
            parsed.append(_relative(path))
        except json.JSONDecodeError as exc:
            failures.append(f"invalid_json:{_relative(path)}:{exc}")
    return parsed


def validate_visual_assets(failures: list[str]) -> dict[str, Any]:
    try:
        contract = load_contract("visual_assets")
    except ContractError as exc:
        failures.append(str(exc))
        return {}
    asset_types = contract.get("asset_types")
    if not isinstance(asset_types, dict):
        failures.append("visual_assets:asset_types_not_object")
        return contract
    for asset_type in EXPECTED_ASSET_TYPES:
        asset = asset_types.get(asset_type)
        if not isinstance(asset, dict):
            failures.append(f"visual_assets:missing_asset_type:{asset_type}")
            continue
        _append_missing_keys(failures, f"visual_assets:{asset_type}", asset, ASSET_KEYS)
        if asset.get("asset_type") != asset_type:
            failures.append(f"visual_assets:{asset_type}:asset_type_mismatch")
        required_fields = asset.get("required_fields")
        if not isinstance(required_fields, list):
            failures.append(f"visual_assets:{asset_type}:required_fields_not_list")
        else:
            missing_required_fields = [
                field for field in VISUAL_ASSET_SPEC_REQUIRED_FIELDS if field not in required_fields
            ]
            if missing_required_fields:
                failures.append(
                    f"visual_assets:{asset_type}:required_fields_missing:{','.join(missing_required_fields)}"
                )
    r00 = asset_types.get("R00_PAPER_MARK_ANCHOR", {})
    qa_questions = r00.get("qa_questions")
    if not isinstance(qa_questions, list) or len(qa_questions) != 14:
        failures.append("visual_assets:R00_PAPER_MARK_ANCHOR:qa_question_count_not_14")
    return contract


def validate_quality_gates(failures: list[str]) -> dict[str, Any]:
    try:
        contract = load_contract("quality_gates")
    except ContractError as exc:
        failures.append(str(exc))
        return {}
    gates = contract.get("gates")
    if not isinstance(gates, dict):
        failures.append("quality_gates:gates_not_object")
        return contract
    for gate_id in EXPECTED_GATES:
        gate = gates.get(gate_id)
        if not isinstance(gate, dict):
            failures.append(f"quality_gates:missing_gate:{gate_id}")
            continue
        _append_missing_keys(failures, f"quality_gates:{gate_id}", gate, GATE_KEYS)
        if gate.get("gate_id") != gate_id:
            failures.append(f"quality_gates:{gate_id}:gate_id_mismatch")
    return contract


def validate_pipeline_actions(failures: list[str]) -> dict[str, Any]:
    try:
        contract = load_contract("pipeline_actions")
    except ContractError as exc:
        failures.append(str(exc))
        return {}
    actions = contract.get("actions")
    if not isinstance(actions, dict):
        failures.append("pipeline_actions:actions_not_object")
        return contract
    for action_id in EXPECTED_ACTIONS:
        action = actions.get(action_id)
        if not isinstance(action, dict):
            failures.append(f"pipeline_actions:missing_action:{action_id}")
            continue
        _append_missing_keys(failures, f"pipeline_actions:{action_id}", action, ACTION_KEYS)
        if action.get("action_id") != action_id:
            failures.append(f"pipeline_actions:{action_id}:action_id_mismatch")
    return contract


def validate_state_machine(failures: list[str]) -> dict[str, Any]:
    try:
        contract = load_contract("state_machine")
    except ContractError as exc:
        failures.append(str(exc))
        return {}
    states = contract.get("states")
    if not isinstance(states, dict):
        failures.append("state_machine:states_not_object")
        return contract
    for state_id in EXPECTED_STATES:
        state = states.get(state_id)
        if not isinstance(state, dict):
            failures.append(f"state_machine:missing_state:{state_id}")
            continue
        _append_missing_keys(failures, f"state_machine:{state_id}", state, STATE_KEYS)
        if state.get("state_id") != state_id:
            failures.append(f"state_machine:{state_id}:state_id_mismatch")
    return contract


def validate_pipeline_contract_links(
    failures: list[str],
    actions_contract: dict[str, Any],
    state_contract: dict[str, Any],
    gate_contract: dict[str, Any],
) -> None:
    actions = actions_contract.get("actions", {})
    states = state_contract.get("states", {})
    gates = gate_contract.get("gates", {})
    if not isinstance(actions, dict) or not isinstance(states, dict) or not isinstance(gates, dict):
        return

    terminal_markers = {
        state_id
        for state_id, state in states.items()
        if isinstance(state, dict) and not state.get("next_states")
    }
    allowed_targets = set(actions) | terminal_markers
    allowed_gate_results = {"pending", "passed", "rework_required", "blocked"}

    for action_id, action in actions.items():
        if not isinstance(action, dict):
            continue
        required_state = action.get("required_state")
        state = states.get(required_state)
        if not isinstance(state, dict):
            failures.append(f"pipeline_links:{action_id}:required_state_missing:{required_state}")
            continue
        if action_id not in state.get("allowed_actions", []):
            failures.append(f"pipeline_links:{action_id}:not_allowed_by_state:{required_state}")
        if action.get("required_gate_result") not in allowed_gate_results:
            failures.append(f"pipeline_links:{action_id}:unknown_required_gate_result:{action.get('required_gate_result')}")
        for transition_key in ("next_action_on_pass", "next_action_on_fail"):
            target = action.get(transition_key)
            if target not in allowed_targets:
                failures.append(f"pipeline_links:{action_id}:{transition_key}_unknown:{target}")

    for state_id, state in states.items():
        if not isinstance(state, dict):
            continue
        for action_id in state.get("allowed_actions", []):
            if action_id not in allowed_targets:
                failures.append(f"pipeline_links:{state_id}:allowed_action_unknown:{action_id}")

    for gate_id, gate in gates.items():
        if not isinstance(gate, dict):
            continue
        for field in ("next_allowed_action_on_pass", "next_allowed_action_on_fail"):
            target = gate.get(field)
            if target not in allowed_targets:
                failures.append(f"pipeline_links:{gate_id}:{field}_unknown:{target}")

    try:
        from pipeline_runner.planner import ACTION_GATE_MAP
    except Exception as exc:  # pragma: no cover - surfaced via CLI
        failures.append(f"pipeline_links:runner_gate_map_unavailable:{exc}")
        return
    for action_id, gate_id in ACTION_GATE_MAP.items():
        if action_id not in actions:
            failures.append(f"pipeline_links:runner_action_missing:{action_id}")
        if gate_id not in gates:
            failures.append(f"pipeline_links:runner_gate_missing:{gate_id}")


def _load_skills_file(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if isinstance(data, dict):
        skills = data.get("skills")
    else:
        skills = data
    if not isinstance(skills, list) or not all(isinstance(skill, dict) for skill in skills):
        raise ValueError(f"skills root must be a list or object with skills list: {_relative(path)}")
    return skills


def validate_skill_definitions(failures: list[str]) -> dict[str, Any]:
    try:
        contract = load_contract("skill_definitions")
    except ContractError as exc:
        failures.append(str(exc))
        return {}
    contract_skills = contract.get("skills")
    if not isinstance(contract_skills, list) or not all(isinstance(skill, dict) for skill in contract_skills):
        failures.append("skill_definitions:skills_not_list")
        return contract
    registry_skills = _load_skills_file(RUNTIME_ROOT / "skill_registry" / "skills.json")
    if len(contract_skills) != 12:
        failures.append(f"skill_definitions:skill_count_not_12:{len(contract_skills)}")
    if len(contract_skills) != len(registry_skills):
        failures.append(f"skill_definitions:registry_count_mismatch:{len(contract_skills)}:{len(registry_skills)}")
    registry_by_id = {skill.get("skill_id"): skill for skill in registry_skills}
    contract_ids = [skill.get("skill_id") for skill in contract_skills]
    if len(contract_ids) != len(set(contract_ids)):
        failures.append("skill_definitions:duplicate_skill_id")
    for skill in contract_skills:
        skill_id = skill.get("skill_id")
        if not isinstance(skill_id, str):
            failures.append("skill_definitions:missing_skill_id")
            continue
        registry_skill = registry_by_id.get(skill_id)
        if registry_skill is None:
            failures.append(f"skill_definitions:skill_id_not_in_registry:{skill_id}")
            continue
        for field in SKILL_CONSISTENCY_FIELDS:
            if skill.get(field) != registry_skill.get(field):
                failures.append(f"skill_definitions:{skill_id}:field_mismatch:{field}")
        serialized = json.dumps(skill, ensure_ascii=False).lower()
        for pattern in AUTHOR_STYLE_PATTERNS:
            if pattern.lower() in serialized:
                failures.append(f"skill_definitions:{skill_id}:author_style_instruction:{pattern}")
        for pattern in HISTORICAL_STORY_PATTERNS:
            if pattern.lower() in serialized:
                failures.append(f"skill_definitions:{skill_id}:historical_story_reference:{pattern}")
    return contract


def validate_contracts() -> dict[str, Any]:
    failures: list[str] = []
    parsed_json = _load_json_contracts(failures)
    visual_contract = validate_visual_assets(failures)
    gate_contract = validate_quality_gates(failures)
    actions_contract = validate_pipeline_actions(failures)
    state_contract = validate_state_machine(failures)
    validate_pipeline_contract_links(failures, actions_contract, state_contract, gate_contract)
    skill_contract = validate_skill_definitions(failures)
    r00_qa_count = len(
        visual_contract.get("asset_types", {}).get("R00_PAPER_MARK_ANCHOR", {}).get("qa_questions", [])
    )
    skill_count = len(skill_contract.get("skills", []))
    return result(
        not failures,
        parsed_json=parsed_json,
        r00_qa_count=r00_qa_count,
        skill_count=skill_count,
        failures=list(dict.fromkeys(failures)),
    )


def main() -> int:
    from core.io import print_json

    payload = validate_contracts()
    print_json(payload)
    return 0 if payload["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
