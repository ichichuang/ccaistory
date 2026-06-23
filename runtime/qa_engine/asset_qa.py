from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from artifact_registry.hash_utils import json_sha256
from contracts.contract_loader import ContractError, r00_required_questions
from core.io import read_json, result


def _now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


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


def create_asset_qa_artifact_payload(
    qa: dict[str, Any],
    *,
    artifact_id: str,
    project_id: str = "",
    story_id: str = "",
    asset_id: str = "",
    run_id: str = "",
    candidate_id: str = "",
    parent_artifact_ids: list[str] | None = None,
    dependency_artifact_ids: list[str] | None = None,
) -> dict[str, Any]:
    qa_result = qa_asset(qa)
    if not qa_result["passed"]:
        return result(False, failures=["asset_qa_validation_failed"], asset_qa_validation=qa_result)

    content_hash = json_sha256(qa)
    if not content_hash.get("hash"):
        return result(False, failures=content_hash.get("failures", ["asset_qa_hash_failed"]))

    block = qa.get("asset_qa_result", qa)
    artifact = {
        "artifact_id": artifact_id,
        "artifact_type": "asset_qa_result",
        "project_id": project_id,
        "story_id": story_id,
        "asset_id": asset_id or block.get("asset_id", ""),
        "run_id": run_id,
        "candidate_id": candidate_id,
        "source_path": "",
        "content_hash": content_hash,
        "source_hash": content_hash,
        "parent_artifact_ids": parent_artifact_ids or [],
        "dependency_artifact_ids": dependency_artifact_ids or [],
        "created_at": _now(),
        "status": "qa_passed",
        "metadata": {
            "asset_type": block.get("asset_type", ""),
            "decision": qa_result["asset_qa_result"]["decision"],
            "allow_accepted": qa_result["asset_qa_result"]["allow_accepted"],
        },
    }
    return result(True, artifact=artifact, asset_qa_validation=qa_result)
