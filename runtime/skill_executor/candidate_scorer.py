from __future__ import annotations

import re
from typing import Any

from skill_registry.load_skills import load_skills


SCORE_KEYS = [
    "clarity",
    "hook_strength",
    "next_page_pull",
    "emotional_pull",
    "skill_alignment",
    "safety",
    "originality",
    "platform_readability",
]

AUTHOR_STYLE_PATTERNS = [
    "style of",
    "in the style",
    "as written by",
    "copy the style",
    "by artist",
    "模仿",
    "仿照",
    "作者风格",
    "某作者",
    "像某人",
]

EMPTY_SCARE_TERMS = [
    "scary",
    "creepy",
    "terrifying",
    "horrifying",
    "spooky",
    "可怕",
    "恐怖",
    "吓人",
    "诡异",
    "惊悚",
]

CONCRETE_TERMS = [
    "concrete",
    "specific",
    "fact",
    "rule",
    "object",
    "choice",
    "question",
    "detail",
    "evidence",
    "cause",
    "具体",
    "事实",
    "规则",
    "物件",
    "选择",
    "问题",
    "线索",
    "细节",
    "证据",
    "因果",
    "下一页",
]

RISKY_CONTENT_PATTERNS = [
    "gore",
    "dismember",
    "mutilat",
    "graphic blood",
    "sexual",
    "adult content",
    "self-harm",
    "suicide",
    "血腥",
    "肢解",
    "虐杀",
    "性描写",
    "成人内容",
    "自残",
    "自杀",
    "儿童受害细节",
]

HOOK_FIELDS = {"typed_hook", "next_page_question", "final_hook_sentence"}
EMOTIONAL_FIELDS = {"typed_narration", "reader_retention_goal", "emotional_anchor", "emotional_delta"}


def _normalize_skills(skills: list[dict[str, Any]] | dict[str, Any] | None) -> list[dict[str, Any]]:
    if skills is None:
        return load_skills()
    if isinstance(skills, dict):
        loaded = skills.get("skills", [])
        return loaded if isinstance(loaded, list) else []
    return skills


def _skill_lookup(skills: list[dict[str, Any]] | dict[str, Any] | None) -> dict[str, dict[str, Any]]:
    return {str(skill.get("skill_id")): skill for skill in _normalize_skills(skills) if skill.get("skill_id")}


def _text(candidate: dict[str, Any]) -> str:
    parts = [
        str(candidate.get("proposed_text") or ""),
        str(candidate.get("rationale") or ""),
        str(candidate.get("repair_action") or ""),
    ]
    return " ".join(parts).strip()


def _contains_any(text: str, patterns: list[str]) -> bool:
    lowered = text.lower()
    return any(pattern.lower() in lowered for pattern in patterns)


def _long_sentence(text: str) -> bool:
    sentences = [part.strip() for part in re.split(r"[。！？!?；;.\n]", text) if part.strip()]
    return any(len(sentence) > 140 for sentence in sentences)


def _skill_supports_candidate(skill: dict[str, Any], field: str, action: str) -> bool:
    if action and action in skill.get("repair_actions", []):
        return True
    supported_fields = {
        *[str(item) for item in skill.get("output_fields", [])],
        *[str(item) for item in skill.get("graph_fields_affected", [])],
    }
    return field in supported_fields


def _hard_failures(candidate: dict[str, Any], skills: dict[str, dict[str, Any]]) -> list[str]:
    text = _text(candidate)
    field = str(candidate.get("target_field") or "")
    action = str(candidate.get("repair_action") or "")
    skill_id = str(candidate.get("skill_id") or "")
    failures: list[str] = []

    if _contains_any(text, AUTHOR_STYLE_PATTERNS):
        failures.append("author_style_instruction")
    if _contains_any(text, EMPTY_SCARE_TERMS) and not _contains_any(text, CONCRETE_TERMS):
        failures.append("empty_scare")
    if _contains_any(text, RISKY_CONTENT_PATTERNS):
        failures.append("unsafe_adult_or_gory_detail")
    if _long_sentence(text):
        failures.append("long_sentence_overload")
    if not field or not action:
        failures.append("no_corresponding_repair_target")

    skill = skills.get(skill_id)
    if not skill or not _skill_supports_candidate(skill, field, action):
        failures.append("skill_id_mismatch")

    return list(dict.fromkeys(failures))


def _score_clarity(text: str, hard_failures: list[str]) -> int:
    if not text or "long_sentence_overload" in hard_failures:
        return 1
    score = 3
    if _contains_any(text, CONCRETE_TERMS):
        score += 2
    if _contains_any(text, ["vague", "泛泛", "空泛"]):
        score -= 1
    return max(0, min(5, score))


def _score_hook(candidate: dict[str, Any], text: str) -> int:
    field = str(candidate.get("target_field") or "")
    skill_id = str(candidate.get("skill_id") or "")
    score = 2
    if field in HOOK_FIELDS:
        score += 2
    if skill_id in {"page_turn_hook", "horror_escalation", "platform_completion_rate"}:
        score += 1
    if _contains_any(text, ["悬念", "question", "问题", "下一页", "unresolved"]):
        score += 1
    return max(0, min(5, score))


def _score_next_page_pull(candidate: dict[str, Any], text: str) -> int:
    field = str(candidate.get("target_field") or "")
    score = 2
    if field in {"next_page_question", "final_hook_sentence", "typed_hook"}:
        score += 2
    if _contains_any(text, ["下一页", "next page", "继续", "question", "问题"]):
        score += 1
    return max(0, min(5, score))


def _score_emotional(candidate: dict[str, Any], text: str) -> int:
    field = str(candidate.get("target_field") or "")
    skill_id = str(candidate.get("skill_id") or "")
    score = 2
    if field in EMOTIONAL_FIELDS or skill_id == "emotional_pull":
        score += 2
    if _contains_any(text, ["情绪", "选择", "关系", "care", "choice", "emotion"]):
        score += 1
    return max(0, min(5, score))


def _score_alignment(candidate: dict[str, Any], skills: dict[str, dict[str, Any]]) -> int:
    skill = skills.get(str(candidate.get("skill_id") or ""))
    if not skill:
        return 0
    field = str(candidate.get("target_field") or "")
    action = str(candidate.get("repair_action") or "")
    if action in skill.get("repair_actions", []):
        return 5
    if _skill_supports_candidate(skill, field, action):
        return 4
    return 1


def _score_safety(candidate: dict[str, Any], hard_failures: list[str]) -> int:
    if "unsafe_adult_or_gory_detail" in hard_failures or "author_style_instruction" in hard_failures:
        return 0
    risk_flags = candidate.get("risk_flags", [])
    if isinstance(risk_flags, list) and "child_safety_boundary" in risk_flags:
        return 4
    return 5


def _score_originality(text: str, hard_failures: list[str]) -> int:
    if "author_style_instruction" in hard_failures:
        return 0
    if _contains_any(text, ["template copy", "照搬"]):
        return 2
    return 4


def _score_readability(text: str, hard_failures: list[str]) -> int:
    if "long_sentence_overload" in hard_failures:
        return 1
    if len(text) <= 240:
        return 5
    if len(text) <= 420:
        return 4
    return 2


def score_candidate(
    candidate: dict[str, Any],
    skills: list[dict[str, Any]] | dict[str, Any] | None = None,
) -> dict[str, Any]:
    skill_lookup = _skill_lookup(skills)
    text = _text(candidate)
    hard_failures = _hard_failures(candidate, skill_lookup)
    scores = {
        "clarity": _score_clarity(text, hard_failures),
        "hook_strength": _score_hook(candidate, text),
        "next_page_pull": _score_next_page_pull(candidate, text),
        "emotional_pull": _score_emotional(candidate, text),
        "skill_alignment": _score_alignment(candidate, skill_lookup),
        "safety": _score_safety(candidate, hard_failures),
        "originality": _score_originality(text, hard_failures),
        "platform_readability": _score_readability(text, hard_failures),
    }
    total_score = sum(scores[key] for key in SCORE_KEYS)
    passed = not hard_failures
    if hard_failures:
        recommendation = "reject_candidate"
    elif total_score >= 30:
        recommendation = "accept_candidate"
    elif total_score >= 24:
        recommendation = "needs_manual_rewrite"
    else:
        recommendation = "reject_candidate"

    return {
        "candidate_id": str(candidate.get("candidate_id") or ""),
        "passed": passed,
        "scores": scores,
        "total_score": total_score,
        "hard_failures": hard_failures,
        "recommendation": recommendation,
    }
