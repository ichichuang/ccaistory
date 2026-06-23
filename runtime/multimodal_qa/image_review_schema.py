from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


REVIEW_DECISIONS = {"pending", "pass", "fail", "conditional_pass"}
EXPECTED_ANSWERS = {"yes", "no", "value"}

IMAGE_REVIEW_FORM_FIELDS = [
    "review_id",
    "artifact_id",
    "asset_id",
    "asset_type",
    "candidate_id",
    "image_path",
    "expected_canvas_ratio",
    "actual_canvas_ratio",
    "expected_reference_dependencies",
    "available_reference_dependencies",
    "questions",
    "manual_evidence",
    "machine_assist",
    "reviewer",
    "reviewed_at",
    "decision",
    "failure_reasons",
    "repair_suggestions",
]

QUESTION_FIELDS = [
    "question_id",
    "question",
    "expected_answer",
    "actual_answer",
    "required",
    "hard_fail_if_mismatch",
    "evidence",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def review_id_for(asset_id: str, candidate_id: str) -> str:
    safe_asset = asset_id or "unknown_asset"
    safe_candidate = candidate_id or "unknown_candidate"
    return f"review_{safe_asset}_{safe_candidate}"


def normalize_expected_answer(value: Any) -> str:
    if isinstance(value, bool):
        return "yes" if value else "no"
    if isinstance(value, str):
        normalized = value.strip().lower()
        if normalized in EXPECTED_ANSWERS:
            return normalized
    return "value"


def make_question(
    *,
    question_id: str,
    question: str,
    expected_answer: Any,
    required: bool = True,
    hard_fail_if_mismatch: bool = True,
    actual_answer: Any = "",
    evidence: str = "",
) -> dict[str, Any]:
    return {
        "question_id": question_id,
        "question": question,
        "expected_answer": normalize_expected_answer(expected_answer),
        "actual_answer": actual_answer,
        "required": required,
        "hard_fail_if_mismatch": hard_fail_if_mismatch,
        "evidence": evidence,
    }


def empty_image_review_form(
    *,
    asset_type: str,
    asset_id: str,
    candidate_id: str,
    artifact_id: str,
    expected_canvas_ratio: str = "",
    expected_reference_dependencies: list[str] | None = None,
    questions: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    return {
        "review_id": review_id_for(asset_id, candidate_id),
        "artifact_id": artifact_id,
        "asset_id": asset_id,
        "asset_type": asset_type,
        "candidate_id": candidate_id,
        "image_path": "",
        "expected_canvas_ratio": expected_canvas_ratio,
        "actual_canvas_ratio": "",
        "expected_reference_dependencies": expected_reference_dependencies or [],
        "available_reference_dependencies": [],
        "questions": questions or [],
        "manual_evidence": {},
        "machine_assist": {},
        "reviewer": "",
        "reviewed_at": "",
        "decision": "pending",
        "failure_reasons": [],
        "repair_suggestions": [],
    }
