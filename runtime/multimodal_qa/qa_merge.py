from __future__ import annotations

from typing import Any

from core.io import read_json, result
from multimodal_qa.manual_review import validate_image_review_form
from multimodal_qa.validators import normalize_answer


def _answer_value(question: dict[str, Any]) -> Any:
    expected = normalize_answer(question.get("expected_answer"))
    actual = normalize_answer(question.get("actual_answer"))
    if expected in {"yes", "no"}:
        return actual == "yes"
    return question.get("actual_answer", "")


def _asset_decision(manual_decision: str, allow_accepted: bool) -> str:
    if allow_accepted and manual_decision == "pass":
        return "accepted"
    if manual_decision == "fail":
        return "rejected"
    if manual_decision == "conditional_pass":
        return "conditional_pass"
    return "pending"


def merge_image_review_to_asset_qa(form: dict[str, Any]) -> dict[str, Any]:
    validation = validate_image_review_form(form)
    review_validation = validation.get("review_validation_result", {})
    questions = form.get("questions", [])
    answers = {
        item.get("question_id"): _answer_value(item)
        for item in questions
        if isinstance(item, dict) and isinstance(item.get("question_id"), str)
    }
    manual_decision = str(form.get("decision", "pending"))
    allow_accepted = bool(review_validation.get("allow_accepted"))
    asset_decision = _asset_decision(manual_decision, allow_accepted)
    failed_rules: list[str] = []
    if not review_validation.get("required_answers_complete", False):
        failed_rules.append("image_review_missing_required_answers")
    if review_validation.get("hard_failures"):
        failed_rules.append("image_review_hard_failure")
    if manual_decision != "pass":
        failed_rules.append(f"image_review_decision:{manual_decision}")

    asset_qa_result = {
        "asset_id": form.get("asset_id", ""),
        "asset_type": form.get("asset_type", ""),
        "candidate_id": form.get("candidate_id", ""),
        "source_artifact_id": form.get("artifact_id", ""),
        "source_review_id": form.get("review_id", ""),
        "source_payload_type": "image_review_form",
        "manual_decision": manual_decision,
        "decision": asset_decision,
        "allow_accepted": allow_accepted,
        "answers": answers,
        "manual_evidence": form.get("manual_evidence", {}),
        "machine_assist": form.get("machine_assist", {}),
        "failure_reasons": form.get("failure_reasons", []),
        "repair_suggestions": form.get("repair_suggestions", []),
        "failed_rules": list(dict.fromkeys(failed_rules)),
        "image_review_validation": review_validation,
        "expected_canvas_ratio": form.get("expected_canvas_ratio", ""),
        "actual_canvas_ratio": form.get("actual_canvas_ratio", ""),
        "expected_reference_dependencies": form.get("expected_reference_dependencies", []),
        "available_reference_dependencies": form.get("available_reference_dependencies", []),
    }
    return result(
        validation["passed"],
        asset_qa_result=asset_qa_result,
        review_validation_result=review_validation,
        failures=validation.get("failures", []),
    )


def merge_image_review_file(path: str) -> dict[str, Any]:
    return merge_image_review_to_asset_qa(read_json(path))
