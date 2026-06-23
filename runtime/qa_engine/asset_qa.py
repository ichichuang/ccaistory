from __future__ import annotations

from typing import Any

from core.io import read_json, result


R00_REQUIRED_QUESTIONS = [
    ("has_person", False, "是否有人物？必须否。"),
    ("has_stick_figure", False, "是否有火柴人？必须否。"),
    ("has_complete_scene", False, "是否有完整场景？必须否。"),
    ("has_prop_collection", False, "是否有道具集合？必须否。"),
    ("is_symbol_sheet", False, "是否是符号散点表？必须否。"),
    ("looks_like_ui_or_flowchart", False, "是否像 UI/流程图？必须否。"),
    ("looks_like_dirty_scrap", False, "是否像乱涂垃圾纸？必须否。"),
    ("clean_white_paper", True, "是否纸张清洁白色？必须是。"),
    ("no_yellowed_old_paper", True, "是否没有泛黄旧纸？必须是。"),
    ("controlled_child_handwriting_sample", True, "是否有可控儿童笔迹样本？必须是。"),
    ("reasonable_short_clue_count", True, "是否短线索数量合理？必须是。"),
    ("no_long_body_text", True, "是否没有长正文？必须是。"),
    ("has_visual_center_or_order", True, "是否有视觉中心或秩序？必须是。"),
    ("usable_as_reference_asset", True, "是否可作为后续 reference asset？必须是。"),
]


def _answers(qa: dict[str, Any]) -> dict[str, Any]:
    answers = qa.get("answers")
    if isinstance(answers, dict):
        return answers
    result_block = qa.get("asset_qa_result", {})
    if isinstance(result_block, dict) and isinstance(result_block.get("answers"), dict):
        return result_block["answers"]
    return {}


def qa_asset(qa: dict[str, Any]) -> dict[str, Any]:
    block = qa.get("asset_qa_result", qa)
    asset_type = block.get("asset_type")
    answers = _answers(qa)
    failed: list[str] = []
    details: list[dict[str, Any]] = []

    if asset_type == "R00_PAPER_MARK_ANCHOR":
        for question_id, expected, text in R00_REQUIRED_QUESTIONS:
            actual = answers.get(question_id)
            if actual is None:
                failed.append("missing_r00_required_question")
                details.append({"question_id": question_id, "question": text, "expected": expected, "actual": actual})
            elif bool(actual) is not expected:
                failed.append("r00_hard_failure")
                details.append({"question_id": question_id, "question": text, "expected": expected, "actual": actual})
    else:
        if not answers:
            failed.append("missing_answers")

    failed_unique = list(dict.fromkeys(failed))
    decision = "accepted" if not failed_unique else "rejected"
    return result(
        not failed_unique,
        asset_qa_result={
            "asset_type": asset_type,
            "decision": decision,
            "failed_rules": failed_unique,
            "details": details,
            "allow_accepted": decision == "accepted",
        },
    )


def qa_asset_file(path: str) -> dict[str, Any]:
    return qa_asset(read_json(path))
