from __future__ import annotations

from typing import Any

from core.io import read_json, result
from multimodal_qa.image_review_schema import IMAGE_REVIEW_FORM_FIELDS, QUESTION_FIELDS
from multimodal_qa.validators import (
    validate_canvas_ratio,
    validate_decision_consistency,
    validate_hard_fail_mismatch,
    validate_reference_dependencies,
    validate_required_answers,
)


def _schema_failures(form: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    missing = [field for field in IMAGE_REVIEW_FORM_FIELDS if field not in form]
    if missing:
        failures.append(f"image_review_form_missing_fields:{','.join(missing)}")
    questions = form.get("questions")
    if not isinstance(questions, list):
        failures.append("questions_not_list")
        return failures
    for index, question in enumerate(questions):
        if not isinstance(question, dict):
            failures.append(f"question_not_object:{index}")
            continue
        missing_question_fields = [field for field in QUESTION_FIELDS if field not in question]
        if missing_question_fields:
            failures.append(f"question_missing_fields:{index}:{','.join(missing_question_fields)}")
    return failures


def validate_image_review_form(form: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(form, dict):
        return result(False, failures=["image_review_form_root_not_object"])

    schema_failures = _schema_failures(form)
    required_result = validate_required_answers(form)
    hard_result = validate_hard_fail_mismatch(form)
    canvas_result = validate_canvas_ratio(form)
    reference_result = validate_reference_dependencies(form)
    decision_result = validate_decision_consistency(form)

    validation_failures = [
        *schema_failures,
        *([] if required_result["passed"] else required_result["failures"]),
        *decision_result["failures"],
    ]
    hard_failures = [
        item["question_id"]
        for item in hard_result["hard_fail_mismatches"]
        if isinstance(item.get("question_id"), str) and item.get("question_id")
    ]
    if not canvas_result["passed"]:
        hard_failures.extend(canvas_result["failures"])
    if not reference_result["passed"]:
        hard_failures.extend(reference_result["failures"])

    required_complete = required_result["passed"]
    allow_accepted = (
        not schema_failures
        and required_complete
        and not hard_failures
        and form.get("decision") == "pass"
    )
    form_valid = not validation_failures

    return result(
        form_valid,
        review_validation_result={
            "review_id": form.get("review_id", ""),
            "asset_id": form.get("asset_id", ""),
            "asset_type": form.get("asset_type", ""),
            "candidate_id": form.get("candidate_id", ""),
            "artifact_id": form.get("artifact_id", ""),
            "decision": form.get("decision", ""),
            "required_answers_complete": required_complete,
            "missing_required_answers": required_result["missing_required_answers"],
            "hard_failures": list(dict.fromkeys(hard_failures)),
            "hard_fail_mismatches": hard_result["hard_fail_mismatches"],
            "canvas_ratio": canvas_result,
            "reference_dependencies": reference_result,
            "decision_consistency": decision_result,
            "allow_accepted": allow_accepted,
            "form_valid": form_valid,
            "validation_failures": list(dict.fromkeys(validation_failures)),
        },
        failures=list(dict.fromkeys(validation_failures)),
    )


def validate_image_review_file(path: str) -> dict[str, Any]:
    return validate_image_review_form(read_json(path))
