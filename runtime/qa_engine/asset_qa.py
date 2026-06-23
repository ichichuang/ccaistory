from __future__ import annotations

from typing import Any

from contracts.contract_loader import ContractError, r00_required_questions
from core.io import read_json, result


def get_r00_required_questions() -> list[tuple[str, bool, str]]:
    return r00_required_questions()


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
        try:
            required_questions = get_r00_required_questions()
        except ContractError as exc:
            failed.append("contract_missing")
            details.append({"error": str(exc)})
        else:
            for question_id, expected, text in required_questions:
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
