from __future__ import annotations

from pathlib import Path
from typing import Any

from contracts.contract_loader import ContractError, load_contract
from core.io import find_story_core, load_json_file, result
from pipeline_runner.pipeline_errors import PipelineContractError


ACTION_GATE_MAP = {
    "create_story_core": "story_core_gate",
    "assess_page_count": "page_count_gate",
    "select_skills": "skill_selection_gate",
    "apply_skill_runtime": "skill_runtime_gate",
    "analyze_story_graph": "story_analyzer_gate",
    "execute_skill_node": "skill_executor_gate",
    "execute_skill_graph": "skill_executor_gate",
    "review_skill_executor_proposed_changes": "skill_executor_gate",
    "apply_approved_skill_changes": "skill_executor_gate",
    "check_story_graph": "graph_integrity_gate",
    "build_visual_manifest": "visual_asset_ontology_gate",
    "build_visual_asset_specs": "visual_asset_ontology_gate",
    "compile_prompts": "prompt_compile_gate",
    "run_semantic_lint": "semantic_lint_gate",
    "generate_source_pilot_task_list": "telemetry_gate",
    "record_execution_telemetry": "telemetry_gate",
    "run_asset_qa": "asset_qa_gate",
    "accept_asset": "asset_qa_gate",
    "reject_asset": "asset_qa_gate",
    "build_platform_page_layout": "human_acceptance_gate",
    "run_human_complete_reading": "human_acceptance_gate",
}

MANUAL_APPROVAL_ACTIONS = {
    "generate_source_pilot_task_list",
    "review_skill_executor_proposed_changes",
    "apply_approved_skill_changes",
    "accept_asset",
    "reject_asset",
    "run_human_complete_reading",
}

VIRTUAL_INPUTS = {
    "story_core",
    "skill_definitions",
    "visual_assets_contract",
}

ACCEPTANCE_REQUIRED_INPUTS = {
    "accept_asset": ["execution_telemetry", "asset_qa_result"],
    "reject_asset": ["execution_telemetry", "asset_qa_result"],
}


def _load_contract_blocks() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    try:
        actions_contract = load_contract("pipeline_actions")
        state_contract = load_contract("state_machine")
        gate_contract = load_contract("quality_gates")
    except ContractError as exc:
        raise PipelineContractError(str(exc)) from exc

    actions = actions_contract.get("actions")
    states = state_contract.get("states")
    gates = gate_contract.get("gates")
    if not isinstance(actions, dict):
        raise PipelineContractError("pipeline_actions.json must contain object key: actions")
    if not isinstance(states, dict):
        raise PipelineContractError("state_machine.json must contain object key: states")
    if not isinstance(gates, dict):
        raise PipelineContractError("quality_gates.json must contain object key: gates")
    return actions, states, gates


def _state_block(story_core: dict[str, Any]) -> dict[str, Any]:
    machine_state = story_core.get("machine_state")
    if isinstance(machine_state, dict):
        return machine_state
    return story_core


def _collect_keys(value: Any, keys: set[str]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            keys.add(key)
            _collect_keys(child, keys)
    elif isinstance(value, list):
        for item in value:
            _collect_keys(item, keys)


def _available_inputs(story_core: dict[str, Any]) -> set[str]:
    available = set(VIRTUAL_INPUTS)
    _collect_keys(story_core, available)
    return available


def _unique(items: list[str]) -> list[str]:
    return list(dict.fromkeys(items))


def _first_allowed(next_allowed_action: Any) -> str:
    if isinstance(next_allowed_action, str):
        return next_allowed_action
    if isinstance(next_allowed_action, list):
        return next((item for item in next_allowed_action if isinstance(item, str) and item), "")
    return ""


def _normalize_gate(requested_until: str | None, gates: dict[str, Any], actions: dict[str, Any]) -> str:
    if not requested_until:
        return ""
    if requested_until in gates:
        return requested_until
    with_suffix = f"{requested_until}_gate"
    if with_suffix in gates:
        return with_suffix
    action_gate = ACTION_GATE_MAP.get(requested_until)
    if action_gate in gates:
        return action_gate
    if requested_until in actions:
        return requested_until
    return requested_until


def _gate_for_action(action_id: str, gates: dict[str, Any]) -> str:
    gate = ACTION_GATE_MAP.get(action_id, "")
    if gate and gate in gates:
        return gate
    return ""


def _next_state_for_action(
    current_state: str,
    next_action: str,
    states: dict[str, Any],
) -> str:
    current = states.get(current_state, {})
    next_states = current.get("next_states", [])
    if not isinstance(next_states, list):
        return ""
    for state_id in next_states:
        state = states.get(state_id)
        if isinstance(state, dict) and next_action in state.get("allowed_actions", []):
            return state_id
    if next_action in states:
        return next_action
    for state_id in next_states:
        if state_id in states:
            return state_id
    return ""


def _plan_failure(
    *,
    project_path: str,
    current_state: str,
    next_allowed_action: str,
    requested_until: str,
    plan: list[dict[str, Any]],
    blocked_reason: list[str] | None = None,
    missing_inputs: list[str] | None = None,
) -> dict[str, Any]:
    return result(
        False,
        project_path=project_path,
        current_state=current_state,
        next_allowed_action=next_allowed_action,
        requested_until=requested_until,
        plan=plan,
        blocked_reason=blocked_reason or [],
        missing_inputs=missing_inputs or [],
    )


def plan_pipeline(project_path: str | Path | None = None, requested_until: str | None = None) -> dict[str, Any]:
    try:
        actions, states, gates = _load_contract_blocks()
    except PipelineContractError as exc:
        return _plan_failure(
            project_path=str(project_path or ""),
            current_state="",
            next_allowed_action="",
            requested_until=requested_until or "",
            plan=[],
            blocked_reason=[f"contract_error:{exc}"],
        )

    normalized_until = _normalize_gate(requested_until, gates, actions)
    if normalized_until and normalized_until not in gates and normalized_until not in actions:
        return _plan_failure(
            project_path=str(project_path or ""),
            current_state="",
            next_allowed_action="",
            requested_until=requested_until or "",
            plan=[],
            blocked_reason=[f"unknown_requested_until:{requested_until}"],
        )

    if project_path is None:
        return result(
            True,
            project_path="",
            current_state="empty",
            next_allowed_action="create_story_core",
            requested_until=requested_until or "",
            requested_until_gate=normalized_until,
            plan=[],
            plan_type="empty_state_plan",
            blocked_reason=["empty_state_plan"],
            missing_inputs=[],
        )

    story_core_path = find_story_core(project_path)
    if story_core_path is None:
        return _plan_failure(
            project_path=str(project_path),
            current_state="empty",
            next_allowed_action="create_story_core",
            requested_until=requested_until or "",
            plan=[],
            blocked_reason=["story_core_missing"],
        )

    story_core = load_json_file(story_core_path)
    if not isinstance(story_core, dict):
        return _plan_failure(
            project_path=str(project_path),
            current_state="",
            next_allowed_action="",
            requested_until=requested_until or "",
            plan=[],
            blocked_reason=["story_core_root_not_object"],
        )

    state = _state_block(story_core)
    current_state = state.get("current_state")
    gate_result = state.get("gate_result")
    next_action = _first_allowed(state.get("next_allowed_action"))
    story_blocked_actions = state.get("blocked_actions", [])
    if not isinstance(current_state, str) or not isinstance(gate_result, str) or not next_action:
        return _plan_failure(
            project_path=str(project_path),
            current_state=current_state if isinstance(current_state, str) else "",
            next_allowed_action=next_action,
            requested_until=requested_until or "",
            plan=[],
            blocked_reason=["machine_state_incomplete"],
            missing_inputs=["current_state", "gate_result", "next_allowed_action"],
        )
    if not isinstance(story_blocked_actions, list):
        return _plan_failure(
            project_path=str(project_path),
            current_state=current_state,
            next_allowed_action=next_action,
            requested_until=requested_until or "",
            plan=[],
            blocked_reason=["blocked_actions_not_list"],
            missing_inputs=["blocked_actions:list"],
        )

    available = _available_inputs(story_core)
    plan: list[dict[str, Any]] = []
    seen_actions: set[str] = set()
    first_step = True
    state_id = current_state
    action_id = next_action
    active_gate_result = gate_result

    for index in range(len(actions) + 1):
        if not action_id:
            break
        if action_id == "publish_ready":
            break
        if action_id in seen_actions:
            return _plan_failure(
                project_path=str(project_path),
                current_state=state_id,
                next_allowed_action=action_id,
                requested_until=requested_until or "",
                plan=plan,
                blocked_reason=[f"pipeline_loop_detected:{action_id}"],
            )
        seen_actions.add(action_id)

        action = actions.get(action_id)
        state_contract = states.get(state_id)
        if not isinstance(action, dict):
            return _plan_failure(
                project_path=str(project_path),
                current_state=state_id,
                next_allowed_action=action_id,
                requested_until=requested_until or "",
                plan=plan,
                blocked_reason=[f"action_not_in_pipeline_contract:{action_id}"],
            )
        if not isinstance(state_contract, dict):
            return _plan_failure(
                project_path=str(project_path),
                current_state=state_id,
                next_allowed_action=action_id,
                requested_until=requested_until or "",
                plan=plan,
                blocked_reason=[f"state_not_in_contract:{state_id}"],
            )

        blocked_actions = _unique(
            [
                *(story_blocked_actions if first_step else []),
                *state_contract.get("blocked_actions", []),
            ]
        )
        if action_id in blocked_actions:
            return _plan_failure(
                project_path=str(project_path),
                current_state=state_id,
                next_allowed_action=action_id,
                requested_until=requested_until or "",
                plan=plan,
                blocked_reason=[f"action_blocked:{action_id}"],
            )

        allowed_actions = state_contract.get("allowed_actions", [])
        if action_id not in allowed_actions:
            return _plan_failure(
                project_path=str(project_path),
                current_state=state_id,
                next_allowed_action=action_id,
                requested_until=requested_until or "",
                plan=plan,
                blocked_reason=[f"action_not_allowed_by_state:{state_id}:{action_id}"],
            )

        if action.get("required_state") != state_id:
            return _plan_failure(
                project_path=str(project_path),
                current_state=state_id,
                next_allowed_action=action_id,
                requested_until=requested_until or "",
                plan=plan,
                blocked_reason=[f"action_required_state_mismatch:{action_id}:{action.get('required_state')}"],
            )

        required_gate_result = action.get("required_gate_result")
        if first_step and required_gate_result != active_gate_result:
            return _plan_failure(
                project_path=str(project_path),
                current_state=state_id,
                next_allowed_action=action_id,
                requested_until=requested_until or "",
                plan=plan,
                blocked_reason=[f"gate_result_mismatch:{active_gate_result}:{required_gate_result}"],
            )

        required_inputs = _unique(
            [
                *state_contract.get("required_artifacts", []),
                *action.get("required_inputs", []),
                *ACCEPTANCE_REQUIRED_INPUTS.get(action_id, []),
            ]
        )
        missing_inputs = [name for name in required_inputs if name not in available]
        if missing_inputs:
            return _plan_failure(
                project_path=str(project_path),
                current_state=state_id,
                next_allowed_action=action_id,
                requested_until=requested_until or "",
                plan=plan,
                blocked_reason=["missing_inputs"],
                missing_inputs=missing_inputs,
            )

        gate_id = _gate_for_action(action_id, gates)
        step = {
            "step_id": f"step_{index + 1:02d}_{action_id}",
            "action_id": action_id,
            "required_inputs": required_inputs,
            "expected_outputs": list(action.get("outputs", [])),
            "gate": gate_id,
            "manual_approval_required": action_id in MANUAL_APPROVAL_ACTIONS,
        }
        plan.append(step)
        available.update(step["expected_outputs"])

        if normalized_until and (normalized_until == gate_id or normalized_until == action_id):
            return result(
                True,
                project_path=str(project_path),
                story_core_path=str(story_core_path),
                current_state=current_state,
                next_allowed_action=next_action,
                requested_until=requested_until or "",
                requested_until_gate=normalized_until,
                plan=plan,
                plan_type="ordered_steps",
                blocked_reason=[],
                missing_inputs=[],
            )

        action_id = action.get("next_action_on_pass", "")
        state_id = _next_state_for_action(state_id, action_id, states)
        active_gate_result = "passed"
        first_step = False
        if not state_id:
            break

    if normalized_until and plan:
        return _plan_failure(
            project_path=str(project_path),
            current_state=current_state,
            next_allowed_action=next_action,
            requested_until=requested_until or "",
            plan=plan,
            blocked_reason=[f"requested_until_not_reached:{requested_until}"],
        )

    return result(
        True,
        project_path=str(project_path),
        story_core_path=str(story_core_path),
        current_state=current_state,
        next_allowed_action=next_action,
        requested_until=requested_until or "",
        requested_until_gate=normalized_until,
        plan=plan,
        plan_type="ordered_steps",
        blocked_reason=[],
        missing_inputs=[],
    )
