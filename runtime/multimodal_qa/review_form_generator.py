from __future__ import annotations

from typing import Any

from contracts.contract_loader import visual_asset_contract
from core.io import result
from multimodal_qa.image_review_schema import empty_image_review_form, make_question


COMMON_IMAGE_REVIEW_QUESTIONS = [
    {
        "question_id": "common_canvas_ratio_correct",
        "question": "实际比例是否正确？",
        "expected_answer": "yes",
    },
    {
        "question_id": "common_reference_dependencies_satisfied",
        "question": "reference_dependencies 是否满足？",
        "expected_answer": "yes",
    },
    {
        "question_id": "common_has_long_body_text",
        "question": "是否有长正文？",
        "expected_answer": "no",
    },
    {
        "question_id": "common_accepted_reference_ready",
        "question": "是否可作为 accepted reference？",
        "expected_answer": "yes",
    },
]


def _contract_questions(asset_contract: dict[str, Any]) -> list[dict[str, Any]]:
    questions = asset_contract.get("qa_questions", [])
    if not isinstance(questions, list):
        return []
    generated: list[dict[str, Any]] = []
    for item in questions:
        if not isinstance(item, dict):
            continue
        question_id = item.get("question_id")
        question = item.get("question")
        if not isinstance(question_id, str) or not isinstance(question, str):
            continue
        generated.append(
            make_question(
                question_id=question_id,
                question=question,
                expected_answer=item.get("expected"),
                required=True,
                hard_fail_if_mismatch=True,
            )
        )
    return generated


def _common_questions() -> list[dict[str, Any]]:
    return [
        make_question(
            question_id=item["question_id"],
            question=item["question"],
            expected_answer=item["expected_answer"],
            required=True,
            hard_fail_if_mismatch=True,
        )
        for item in COMMON_IMAGE_REVIEW_QUESTIONS
    ]


def _expected_reference_dependencies(asset_contract: dict[str, Any]) -> list[str]:
    reference_policy = asset_contract.get("required_reference_policy", {})
    if not isinstance(reference_policy, dict):
        return []
    refs = reference_policy.get("required_references", [])
    if not isinstance(refs, list):
        return []
    return [item for item in refs if isinstance(item, str) and item]


def generate_image_review_form(
    *,
    asset_type: str,
    asset_id: str,
    candidate_id: str,
    artifact_id: str,
) -> dict[str, Any]:
    asset_contract = visual_asset_contract(asset_type)
    canvas = asset_contract.get("required_canvas", {})
    expected_canvas_ratio = canvas.get("ratio", "") if isinstance(canvas, dict) else ""
    questions = [*_contract_questions(asset_contract), *_common_questions()]
    form = empty_image_review_form(
        asset_type=asset_type,
        asset_id=asset_id,
        candidate_id=candidate_id,
        artifact_id=artifact_id,
        expected_canvas_ratio=expected_canvas_ratio,
        expected_reference_dependencies=_expected_reference_dependencies(asset_contract),
        questions=questions,
    )
    return result(
        True,
        image_review_form=form,
        contract_question_count=len(questions) - len(COMMON_IMAGE_REVIEW_QUESTIONS),
        common_question_count=len(COMMON_IMAGE_REVIEW_QUESTIONS),
        question_count=len(questions),
    )
