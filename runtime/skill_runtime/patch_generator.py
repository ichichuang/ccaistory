from __future__ import annotations

from typing import Any

from skill_registry.load_skills import load_skills
from skill_runtime.evaluator import evaluate_node


ACTION_FIELDS = {
    "add_next_page_question": "next_page_question",
    "rewrite_final_hook_sentence": "final_hook_sentence",
    "replace_author_style_with_abstract_hook": "typed_hook",
    "add_threat_delta": "threat_delta",
    "tie_escalation_to_prior_fact": "threat_delta",
    "remove_empty_scare": "typed_narration",
    "state_normal_baseline": "normal_baseline",
    "reduce_initial_anomaly": "anomaly_delta",
    "connect_anomaly_to_page_question": "next_page_question",
    "make_rule_explicit": "rule_visibility",
    "add_rule_consequence": "consequence_question",
    "link_rule_to_previous_anomaly": "rule_visibility",
    "rewrite_from_child_perception": "typed_narration",
    "soften_unsafe_content": "typed_narration",
    "anchor_wonder_in_concrete_detail": "visual_memory_point",
    "plant_prior_evidence": "opening_callback",
    "remove_unearned_reversal": "twist_reveal",
    "connect_twist_to_opening": "opening_callback",
    "add_opening_callback": "opening_callback",
    "state_loop_mechanism": "loop_confirmation",
    "align_ending_with_first_page": "opening_callback",
    "add_fair_false_explanation": "misdirection_target",
    "add_disproof_evidence": "disproof_signal",
    "delay_full_explanation": "next_page_question",
    "add_concrete_emotional_anchor": "typed_narration",
    "tie_emotion_to_choice": "reader_retention_goal",
    "remove_empty_sentiment": "typed_narration",
    "move_world_detail_to_later_page": "compressed_world_facts",
    "keep_only_actionable_fact": "compressed_world_facts",
    "merge_repeated_context": "compressed_world_facts",
    "add_reader_retention_goal": "reader_retention_goal",
    "split_overloaded_page": "typed_narration",
    "move_secondary_fact_downstream": "typed_narration",
    "replace_explicit_harm_with_symbolic_signal": "safe_substitutions",
    "soften_visual_threat": "visual_safety_notes",
    "preserve_question_not_harm": "next_page_question",
}


def _node_id(node: dict[str, Any]) -> str:
    return str(node.get("node_id") or node.get("id") or node.get("page_id") or node.get("page_index") or "")


def _skill_map(skills: list[dict[str, Any]] | None = None) -> dict[str, dict[str, Any]]:
    loaded = skills if skills is not None else load_skills()
    return {str(skill.get("skill_id")): skill for skill in loaded if skill.get("skill_id")}


def _operation(action: str, field: str, reason: str) -> str:
    if action.startswith("add_") or reason.endswith("_empty"):
        return "add_missing"
    if action.startswith("split_"):
        return "split"
    if action.startswith("remove_") or action.startswith("replace_"):
        return "remove"
    if action.startswith("rewrite_"):
        return "suggest_rewrite"
    return "strengthen" if field else "suggest_rewrite"


def _instruction(field: str, action: str, reason: str) -> str:
    return (
        f"Apply `{action}` to `{field}` as a structural repair for `{reason}`. "
        "Record the needed rewrite target and guidance only; do not generate final prose."
    )


def _fallback_action(skill: dict[str, Any] | None, field: str) -> str:
    if not skill:
        return f"repair_{field}"
    for action in skill.get("repair_actions", []):
        if ACTION_FIELDS.get(str(action)) == field:
            return str(action)
    actions = skill.get("repair_actions", [])
    return str(actions[0]) if actions else f"repair_{field}"


def generate_skill_patch(
    node: dict[str, Any],
    skill_failures: list[dict[str, Any]] | None = None,
    repair_targets: list[dict[str, Any]] | None = None,
    skills: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    skill_lookup = _skill_map(skills)
    if skill_failures is None or repair_targets is None:
        evaluation = evaluate_node(node, skills=skills)
        skill_failures = evaluation["skill_failures"]
        repair_targets = evaluation["repair_targets"]

    patches: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str]] = set()
    for target in repair_targets:
        field = str(target.get("field") or "")
        skill_id = str(target.get("skill_id") or "")
        skill = skill_lookup.get(skill_id)
        action = str(target.get("repair_action") or _fallback_action(skill, field))
        field = field or ACTION_FIELDS.get(action, "")
        reason = str(target.get("reason") or target.get("hard_failure") or "skill_runtime_repair")
        key = (field, skill_id, action)
        if key in seen:
            continue
        seen.add(key)
        patches.append(
            {
                "field": field,
                "operation": _operation(action, field, reason),
                "reason": reason,
                "skill_id": skill_id,
                "repair_action": action,
                "instruction": _instruction(field, action, reason),
            }
        )

    return {
        "node_id": _node_id(node),
        "patches": patches,
        "source_failures": skill_failures,
    }
