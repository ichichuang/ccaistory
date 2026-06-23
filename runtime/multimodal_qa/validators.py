from __future__ import annotations

from typing import Any

from core.io import result
from multimodal_qa.image_review_schema import REVIEW_DECISIONS


YES_VALUES = {"yes", "true", "1", "y", "pass", "passed", "是", "有", "通过"}
NO_VALUES = {"no", "false", "0", "n", "fail", "failed", "否", "无", "不通过"}


def normalize_answer(value: Any) -> str:
    if isinstance(value, bool):
        return "yes" if value else "no"
    if value is None:
        return ""
    text = str(value).strip()
    if not text:
        return ""
    lowered = text.lower()
    if lowered in YES_VALUES:
        return "yes"
    if lowered in NO_VALUES:
        return "no"
    return text


def normalize_ratio(value: Any) -> str:
    return str(value or "").strip().replace(" ", "")


def answer_matches(expected: Any, actual: Any) -> bool:
    expected_normalized = normalize_answer(expected)
    if expected_normalized not in {"yes", "no"}:
        return normalize_answer(actual) != ""
    return normalize_answer(actual) == expected_normalized


def _questions(form: dict[str, Any]) -> list[dict[str, Any]]:
    questions = form.get("questions")
    if not isinstance(questions, list):
        return []
    return [item for item in questions if isinstance(item, dict)]


def validate_canvas_ratio(form: dict[str, Any]) -> dict[str, Any]:
    expected = normalize_ratio(form.get("expected_canvas_ratio"))
    actual = normalize_ratio(form.get("actual_canvas_ratio"))
    failures: list[str] = []
    if expected and not actual:
        failures.append("actual_canvas_ratio_missing")
    elif expected and actual and expected != actual:
        failures.append("canvas_ratio_mismatch")
    return result(not failures, expected_canvas_ratio=expected, actual_canvas_ratio=actual, failures=failures)


def validate_reference_dependencies(form: dict[str, Any]) -> dict[str, Any]:
    expected = form.get("expected_reference_dependencies", [])
    available = form.get("available_reference_dependencies", [])
    if not isinstance(expected, list):
        return result(False, failures=["expected_reference_dependencies_not_list"], missing_reference_dependencies=[])
    if not isinstance(available, list):
        return result(False, failures=["available_reference_dependencies_not_list"], missing_reference_dependencies=[])
    expected_ids = [item for item in expected if isinstance(item, str) and item]
    available_ids = {item for item in available if isinstance(item, str) and item}
    missing = [item for item in expected_ids if item not in available_ids]
    failures = ["reference_dependencies_missing"] if missing else []
    return result(not failures, missing_reference_dependencies=missing, failures=failures)


def validate_required_answers(form: dict[str, Any]) -> dict[str, Any]:
    missing: list[str] = []
    for question in _questions(form):
        if question.get("required") is True and normalize_answer(question.get("actual_answer")) == "":
            question_id = question.get("question_id")
            missing.append(question_id if isinstance(question_id, str) else "")
    missing = [item for item in missing if item]
    failures = ["required_answers_missing"] if missing else []
    return result(not failures, missing_required_answers=missing, failures=failures)


def validate_hard_fail_mismatch(form: dict[str, Any]) -> dict[str, Any]:
    mismatches: list[dict[str, Any]] = []
    for question in _questions(form):
        if question.get("hard_fail_if_mismatch") is not True:
            continue
        actual = question.get("actual_answer")
        if normalize_answer(actual) == "":
            continue
        expected = question.get("expected_answer")
        if not answer_matches(expected, actual):
            mismatches.append(
                {
                    "question_id": question.get("question_id", ""),
                    "expected_answer": expected,
                    "actual_answer": actual,
                    "question": question.get("question", ""),
                }
            )
    failures = ["hard_fail_mismatch"] if mismatches else []
    return result(not failures, hard_fail_mismatches=mismatches, failures=failures)


def validate_decision_consistency(form: dict[str, Any]) -> dict[str, Any]:
    failures: list[str] = []
    decision = form.get("decision")
    if decision not in REVIEW_DECISIONS:
        failures.append(f"unknown_review_decision:{decision}")

    required_result = validate_required_answers(form)
    hard_result = validate_hard_fail_mismatch(form)
    canvas_result = validate_canvas_ratio(form)
    reference_result = validate_reference_dependencies(form)

    has_missing_required = not required_result["passed"]
    has_hard_failure = not hard_result["passed"] or not canvas_result["passed"] or not reference_result["passed"]

    if has_missing_required and decision != "pending":
        failures.append("missing_required_answers_require_pending_decision")
    if has_hard_failure and decision != "fail":
        failures.append("hard_failure_requires_fail_decision")
    if decision == "pass" and has_missing_required:
        failures.append("pass_decision_with_missing_required_answers")
    if decision == "pass" and has_hard_failure:
        failures.append("pass_decision_with_hard_failure")

    return result(
        not failures,
        decision=decision,
        has_missing_required=has_missing_required,
        has_hard_failure=has_hard_failure,
        failures=list(dict.fromkeys(failures)),
    )
