from __future__ import annotations

from typing import Any


STORY_TYPE_SKILLS = {
    "micro_horror": ["page_turn_hook", "everyday_anomaly", "fate_loop"],
    "platform_horror": ["page_turn_hook", "platform_completion_rate", "horror_escalation"],
    "classic_adaptation": ["world_compression", "misdirection_disproof", "strange_tale_twist"],
    "rule_horror": ["rule_horror", "horror_escalation", "page_turn_hook"],
    "folk_strange_tale": ["strange_tale_twist", "fate_loop", "misdirection_disproof"],
    "child_safe_mystery": ["child_safe_adaptation", "child_perspective_wonder", "emotional_pull", "page_turn_hook"],
    "emotional_suspense": ["emotional_pull", "misdirection_disproof", "page_turn_hook"],
    "unknown": [],
}


def _text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        return " ".join(f"{key} {_text(child)}" for key, child in value.items())
    if isinstance(value, list):
        return " ".join(_text(item) for item in value)
    return str(value)


def _contains(text: str, keywords: tuple[str, ...]) -> bool:
    return any(keyword in text for keyword in keywords)


def _unique(items: list[str]) -> list[str]:
    return list(dict.fromkeys(items))


def _result(story_type: str, confidence: float, reason_codes: list[str]) -> dict[str, Any]:
    return {
        "story_type": story_type,
        "confidence": round(max(0.0, min(confidence, 1.0)), 2),
        "reason_codes": _unique(reason_codes),
        "recommended_global_skills": STORY_TYPE_SKILLS[story_type],
    }


def classify_story(
    story_premise: Any = "",
    source_type: Any = "",
    target_mode: Any = "",
    constraints: Any = None,
    tags: Any = None,
) -> dict[str, Any]:
    combined = " ".join(
        part.strip()
        for part in (
            _text(story_premise),
            _text(source_type),
            _text(target_mode),
            _text(constraints),
            _text(tags),
        )
        if part and part.strip()
    )
    text = combined.lower()
    if len(text) < 8:
        return _result("unknown", 0.2, ["insufficient_story_signal", "manual_confirmation_required"])

    reasons: list[str] = []
    if _contains(text, ("经典改编", "原作", "版权审查", "adaptation", "classic", "copyright", "source text")):
        reasons.append("classic_or_copyright_signal")
        return _result("classic_adaptation", 0.9, reasons)

    if _contains(text, ("规则", "禁止", "不能做", "不可", "rule", "forbidden", "must not", "cannot")):
        reasons.append("rule_or_forbidden_signal")
        return _result("rule_horror", 0.88, reasons)

    child_signal = _contains(text, ("儿童安全", "无血腥", "儿童", "孩子", "校园", "家", "楼道", "school", "home", "corridor", "child safe", "no gore"))
    horror_signal = _contains(text, ("恐怖", "怪谈", "异常", "悬疑", "horror", "anomaly", "mystery", "suspense"))
    if child_signal and _contains(text, ("儿童安全", "无血腥", "child safe", "no gore", "校园", "school")):
        reasons.append("child_safe_mystery_signal")
        return _result("child_safe_mystery", 0.84, reasons)
    if child_signal and horror_signal:
        reasons.append("platform_child_horror_signal")
        return _result("platform_horror", 0.72, reasons)

    if _contains(text, ("志怪", "民间", "民俗", "传说", "folk", "strange tale", "folklore")):
        reasons.append("folk_strange_tale_signal")
        return _result("folk_strange_tale", 0.82, reasons)

    if _contains(text, ("微型", "短篇", "一页", "micro", "very short", "short-short")):
        reasons.append("micro_story_signal")
        return _result("micro_horror", 0.78, reasons)

    if _contains(text, ("情绪", "关系", "失去", "愧疚", "牵挂", "emotional", "relationship", "grief", "care")):
        reasons.append("emotional_suspense_signal")
        return _result("emotional_suspense", 0.74, reasons)

    if _contains(text, ("平台", "图文", "完读", "page turn", "platform", "completion")) or horror_signal:
        reasons.append("platform_horror_signal")
        return _result("platform_horror", 0.66, reasons)

    return _result("unknown", 0.28, ["insufficient_story_signal", "manual_confirmation_required"])


def classify_story_core(story_core: dict[str, Any]) -> dict[str, Any]:
    return classify_story(
        story_premise=story_core.get("story_premise")
        or story_core.get("premise")
        or story_core.get("summary")
        or story_core.get("story_title")
        or story_core.get("title")
        or "",
        source_type=story_core.get("source_type") or story_core.get("adaptation_source_type") or "",
        target_mode=story_core.get("target_mode") or story_core.get("platform_mode") or story_core.get("story_type") or "",
        constraints=story_core.get("constraints") or story_core.get("safety_constraints") or {},
        tags=story_core.get("tags") or story_core.get("story_tags") or [],
    )
