from __future__ import annotations

import hashlib
from typing import Any

from skill_registry.load_skills import load_skills


FIELD_GUIDANCE = {
    "applied_skills": "根据 page_role、page_index 和已选技法计划补齐 applied_skills；先记录应使用的 skill，再重新评估节点。",
    "typed_hook": "为 typed_hook 添加具体悬念：指出本页出现的新异常、物件、规则或选择，并把问题指向后续页面。",
    "typed_narration": "重写 typed_narration 的结构目标：保留具体行动、感知和因果线索，删除空泛形容。",
    "next_page_question": "补充可复述的翻页问题，聚焦下一页要验证的事实，不提前解释真相。",
    "final_hook_sentence": "强化 final_hook_sentence：用一个清楚的新事实或未解问题收束本页，并推动下一页阅读。",
    "reader_retention_goal": "补充 reader_retention_goal：说明读者应带着哪个具体疑问、情绪或选择继续阅读。",
    "opening_callback": "补充 opening_callback：让结尾回扣开头的具体图像、规则或选择，而不是口号式闭环。",
    "threat_delta": "记录 threat_delta：说明威胁相对上一页的具体差量，必须来自事实、规则或选择推进。",
    "normal_baseline": "补充 normal_baseline：先说明日常基线，再让异常从一个小而具体的细节偏离。",
    "anomaly_delta": "收窄 anomaly_delta：把异常限定为可观察的小变化，避免开局直接解释真相。",
    "rule_visibility": "补强 rule_visibility：让规则可被读者复述，并说明违反规则会触发什么后果。",
    "consequence_question": "补充 consequence_question：把规则后果转为下一步需要验证的问题。",
    "twist_reveal": "重整 twist_reveal：只保留前文证据能支撑的转折，删除无证据反转。",
    "misdirection_target": "补充 misdirection_target：给出公平误导的旧解释，并保留反证空间。",
    "disproof_signal": "补充 disproof_signal：加入能推翻旧解释但不泄底的具体证据。",
    "compressed_world_facts": "压缩 compressed_world_facts：只保留本页行动必须理解的设定，把次要信息后移。",
    "safe_substitutions": "补充 safe_substitutions：用象征、环境或规则信号替代危险细节，保留核心悬念。",
    "visual_safety_notes": "补充 visual_safety_notes：约束画面威胁强度，避免儿童危险或成人化细节。",
}

ACTION_TYPE_HINTS = {
    "add_": "add_missing_field",
    "state_": "add_missing_field",
    "make_": "strengthen_field",
    "rewrite_": "rewrite_instruction",
    "replace_": "rewrite_instruction",
    "remove_": "rewrite_instruction",
    "soften_": "rewrite_instruction",
    "preserve_": "rewrite_instruction",
    "split_": "split_overloaded_field",
    "move_": "split_overloaded_field",
    "merge_": "strengthen_field",
    "tie_": "strengthen_field",
    "connect_": "strengthen_field",
    "link_": "strengthen_field",
    "anchor_": "strengthen_field",
    "plant_": "add_missing_field",
    "delay_": "rewrite_instruction",
    "keep_": "strengthen_field",
    "reduce_": "rewrite_instruction",
}

OPERATION_TYPES = {
    "add_missing": "add_missing_field",
    "strengthen": "strengthen_field",
    "split": "split_overloaded_field",
    "remove": "rewrite_instruction",
    "suggest_rewrite": "rewrite_instruction",
}

HOOK_FIELDS = {"typed_hook", "next_page_question", "final_hook_sentence"}
RETENTION_FIELDS = {"reader_retention_goal", "typed_narration"}


def _node_id(node: dict[str, Any]) -> str:
    return str(node.get("node_id") or node.get("id") or node.get("page_id") or node.get("page_index") or "")


def _normalize_skills(skills: list[dict[str, Any]] | dict[str, Any] | None) -> list[dict[str, Any]]:
    if skills is None:
        return load_skills()
    if isinstance(skills, dict):
        loaded = skills.get("skills", [])
        return loaded if isinstance(loaded, list) else []
    return skills


def _skill_lookup(skills: list[dict[str, Any]] | dict[str, Any] | None) -> dict[str, dict[str, Any]]:
    return {str(skill.get("skill_id")): skill for skill in _normalize_skills(skills) if skill.get("skill_id")}


def _as_skill_ids(value: Any) -> list[str]:
    if isinstance(value, str):
        return [item.strip() for item in value.split(",") if item.strip()]
    if isinstance(value, list):
        ids: list[str] = []
        for item in value:
            if isinstance(item, str) and item.strip():
                ids.append(item.strip())
            elif isinstance(item, dict):
                skill_id = item.get("skill_id") or item.get("id")
                if isinstance(skill_id, str) and skill_id.strip():
                    ids.append(skill_id.strip())
        return list(dict.fromkeys(ids))
    return []


def _patches_from_plan(repair_plan: dict[str, Any] | list[Any]) -> list[dict[str, Any]]:
    if isinstance(repair_plan, list):
        return [item for item in repair_plan if isinstance(item, dict)]
    if not isinstance(repair_plan, dict):
        return []
    if isinstance(repair_plan.get("patches"), list):
        return [item for item in repair_plan["patches"] if isinstance(item, dict)]

    patches: list[dict[str, Any]] = []
    for key in ("repair_plan", "nodes"):
        items = repair_plan.get(key)
        if not isinstance(items, list):
            continue
        for item in items:
            if not isinstance(item, dict):
                continue
            nested_patch = item.get("patch")
            if isinstance(nested_patch, dict) and isinstance(nested_patch.get("patches"), list):
                patches.extend(patch for patch in nested_patch["patches"] if isinstance(patch, dict))
            elif isinstance(item.get("patches"), list):
                patches.extend(patch for patch in item["patches"] if isinstance(patch, dict))
    return patches


def _candidate_type(patch: dict[str, Any]) -> str:
    operation = str(patch.get("operation") or "")
    if operation in OPERATION_TYPES:
        return OPERATION_TYPES[operation]
    action = str(patch.get("repair_action") or "")
    for prefix, candidate_type in ACTION_TYPE_HINTS.items():
        if action.startswith(prefix):
            return candidate_type
    return "rewrite_instruction"


def _field_supported_by_skill(field: str, skill: dict[str, Any]) -> bool:
    supported = {
        *[str(item) for item in skill.get("output_fields", [])],
        *[str(item) for item in skill.get("graph_fields_affected", [])],
    }
    return field in supported


def _infer_skill_id(
    *,
    field: str,
    patch: dict[str, Any],
    node: dict[str, Any],
    skills: dict[str, dict[str, Any]],
) -> str:
    explicit = str(patch.get("skill_id") or "")
    if explicit in skills:
        return explicit

    for skill_id in _as_skill_ids(node.get("applied_skills")):
        skill = skills.get(skill_id)
        if skill and _field_supported_by_skill(field, skill):
            return skill_id

    if field in HOOK_FIELDS and "page_turn_hook" in skills:
        return "page_turn_hook"
    if field in RETENTION_FIELDS:
        if "platform_completion_rate" in skills:
            return "platform_completion_rate"
        if "emotional_pull" in skills:
            return "emotional_pull"
    if field in {"threat_delta", "safe_substitutions", "visual_safety_notes"}:
        if "child_safe_adaptation" in skills and field != "threat_delta":
            return "child_safe_adaptation"
        if "horror_escalation" in skills:
            return "horror_escalation"

    applied = _as_skill_ids(node.get("applied_skills"))
    return applied[0] if applied else ("page_turn_hook" if "page_turn_hook" in skills else "")


def _proposed_text(field: str, action: str, reason: str, candidate_type: str) -> str:
    guidance = FIELD_GUIDANCE.get(
        field,
        f"为 {field} 生成结构化修复指令：补齐缺失目标，保持清晰、儿童安全和故事因果一致。",
    )
    return (
        f"{guidance} repair_action={action or 'repair_field'}；failure_reason={reason or 'skill_runtime_failure'}；"
        f"candidate_type={candidate_type}。"
    )


def _risk_flags(field: str, skill_id: str, action: str) -> list[str]:
    flags: list[str] = []
    if skill_id == "horror_escalation" or "threat" in action:
        flags.append("avoid_empty_scare")
    if skill_id == "child_safe_adaptation" or field in {"safe_substitutions", "visual_safety_notes"}:
        flags.append("child_safety_boundary")
    if field in {"typed_hook", "final_hook_sentence", "next_page_question"}:
        flags.append("clarity_before_hook")
    return flags


def _candidate_id(node_id: str, field: str, skill_id: str, action: str, index: int) -> str:
    digest = hashlib.sha1(f"{node_id}:{field}:{skill_id}:{action}:{index}".encode("utf-8")).hexdigest()[:12]
    return f"cand_{digest}"


def generate_candidates(
    node: dict[str, Any],
    repair_plan: dict[str, Any] | list[Any],
    skills: list[dict[str, Any]] | dict[str, Any] | None = None,
    contracts: dict[str, Any] | None = None,
) -> dict[str, Any]:
    del contracts
    skill_lookup = _skill_lookup(skills)
    node_id = _node_id(node)
    patches = _patches_from_plan(repair_plan)
    candidates: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str]] = set()

    for index, patch in enumerate(patches, start=1):
        field = str(patch.get("field") or "")
        action = str(patch.get("repair_action") or "")
        if not field:
            continue
        skill_id = _infer_skill_id(field=field, patch=patch, node=node, skills=skill_lookup)
        reason = str(patch.get("reason") or "skill_runtime_failure")
        candidate_type = _candidate_type(patch)
        key = (field, skill_id, action)
        if key in seen:
            continue
        seen.add(key)
        candidates.append(
            {
                "candidate_id": _candidate_id(node_id, field, skill_id, action, index),
                "node_id": node_id,
                "target_field": field,
                "skill_id": skill_id,
                "repair_action": action,
                "candidate_type": candidate_type,
                "proposed_text": _proposed_text(field, action, reason, candidate_type),
                "rationale": str(patch.get("instruction") or reason),
                "risk_flags": _risk_flags(field, skill_id, action),
            }
        )

    return {"node_id": node_id, "candidates": candidates}
