from __future__ import annotations

from pathlib import Path
from typing import Any

from core.io import find_story_core, load_json_file, result


ACTIONS = [
    "create_story_core",
    "run_long_story_page_count_audit",
    "select_technique_combination",
    "strengthen_story_graph_hooks",
    "generate_platform_story_layout",
    "run_image_reading_test",
    "create_visual_manifest",
    "compile_source_illustration_prompt",
    "run_source_prompt_semantic_lint",
    "generate_source_illustration_pilot_task_list",
    "external_single_image_generation",
    "record_image_execution_telemetry",
    "run_asset_level_acceptance",
    "route_accepted_or_rejected",
    "synthesize_platform_publish_page",
    "manual_full_reading",
    "prepublish_check",
    "publish_ready",
]


def _state_block(story_core: dict[str, Any]) -> dict[str, Any]:
    machine_state = story_core.get("machine_state")
    if isinstance(machine_state, dict):
        return machine_state
    return story_core


def get_status(project_path: str | Path | None = None) -> dict[str, Any]:
    if project_path is None:
        return {
            "status": "empty",
            "story_core": None,
            "machine_state": None,
            "current_state": None,
            "gate_result": None,
            "next_allowed_action": None,
            "blocked_actions": [],
        }

    story_core_path = find_story_core(project_path)
    if story_core_path is None:
        return {
            "status": "empty",
            "story_core": None,
            "machine_state": None,
            "current_state": None,
            "gate_result": None,
            "next_allowed_action": None,
            "blocked_actions": [],
        }

    story_core = load_json_file(story_core_path)
    state = _state_block(story_core)
    return {
        "status": "loaded",
        "story_core": str(story_core_path),
        "machine_state": state,
        "current_state": state.get("current_state"),
        "gate_result": state.get("gate_result"),
        "next_allowed_action": state.get("next_allowed_action"),
        "blocked_actions": state.get("blocked_actions", []),
    }


def validate_story_core(story_core: dict[str, Any]) -> dict[str, Any]:
    state = _state_block(story_core)
    missing = [
        field
        for field in ("current_state", "gate_result", "next_allowed_action", "blocked_actions")
        if field not in state
    ]
    blocked_actions = state.get("blocked_actions")
    if blocked_actions is not None and not isinstance(blocked_actions, list):
        missing.append("blocked_actions:list")
    return result(not missing, missing_fields=missing)


def can_run(project_path: str | Path, action: str) -> dict[str, Any]:
    story_core_path = find_story_core(project_path)
    if story_core_path is None:
        return result(False, action=action, reason="story_core.json not found")

    story_core = load_json_file(story_core_path)
    validation = validate_story_core(story_core)
    if not validation["passed"]:
        return result(False, action=action, reason="machine_state incomplete", details=validation)

    state = _state_block(story_core)
    blocked_actions = state.get("blocked_actions", [])
    if action in blocked_actions:
        return result(False, action=action, reason="action is blocked", blocked_actions=blocked_actions)

    gate_result = state.get("gate_result")
    if gate_result != "passed":
        return result(False, action=action, reason="gate_result is not passed", gate_result=gate_result)

    next_allowed_action = state.get("next_allowed_action")
    allowed = next_allowed_action
    if isinstance(allowed, str):
        allowed_actions = [allowed]
    elif isinstance(allowed, list):
        allowed_actions = allowed
    else:
        allowed_actions = []

    if action not in allowed_actions:
        return result(
            False,
            action=action,
            reason="action does not match next_allowed_action",
            next_allowed_action=next_allowed_action,
        )

    return result(
        True,
        action=action,
        reason="action allowed",
        current_state=state.get("current_state"),
        gate_result=gate_result,
        next_allowed_action=next_allowed_action,
    )
