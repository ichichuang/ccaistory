from __future__ import annotations

import json
from pathlib import Path
from typing import Any


RUNTIME_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = RUNTIME_ROOT.parent
CONTRACTS_DIR = RUNTIME_ROOT / "contracts"

REQUIRED_CONTRACT_FILES = [
    "state_machine.json",
    "visual_assets.json",
    "skill_definitions.json",
    "quality_gates.json",
    "pipeline_actions.json",
]


class ContractError(RuntimeError):
    """Raised when a required machine contract is missing or malformed."""


def contract_path(name: str) -> Path:
    normalized = name if name.endswith(".json") else f"{name}.json"
    return CONTRACTS_DIR / normalized


def load_contract(name: str) -> dict[str, Any]:
    path = contract_path(name)
    if not path.exists():
        raise ContractError(f"missing required contract: {path.relative_to(PROJECT_ROOT)}")
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except json.JSONDecodeError as exc:
        raise ContractError(f"invalid JSON contract {path.relative_to(PROJECT_ROOT)}: {exc}") from exc
    if not isinstance(data, dict):
        raise ContractError(f"contract root must be an object: {path.relative_to(PROJECT_ROOT)}")
    return data


def load_all_contracts() -> dict[str, dict[str, Any]]:
    return {name: load_contract(name) for name in REQUIRED_CONTRACT_FILES}


def load_visual_assets_contract() -> dict[str, Any]:
    return load_contract("visual_assets")


def visual_asset_types() -> dict[str, dict[str, Any]]:
    contract = load_visual_assets_contract()
    asset_types = contract.get("asset_types")
    if not isinstance(asset_types, dict):
        raise ContractError("visual_assets.json must contain object key: asset_types")
    return asset_types


def visual_asset_contract(asset_type: str) -> dict[str, Any]:
    asset_types = visual_asset_types()
    item = asset_types.get(asset_type)
    if not isinstance(item, dict):
        raise ContractError(f"visual asset contract not found for asset_type: {asset_type}")
    return item


def r00_contract() -> dict[str, Any]:
    return visual_asset_contract("R00_PAPER_MARK_ANCHOR")


def r00_forbidden_positive_terms() -> list[str]:
    terms = r00_contract().get("forbidden_positive_terms")
    if not isinstance(terms, list) or not all(isinstance(term, str) and term for term in terms):
        raise ContractError("R00_PAPER_MARK_ANCHOR.forbidden_positive_terms must be a non-empty string list")
    return terms


def r00_required_questions() -> list[tuple[str, bool, str]]:
    questions = r00_contract().get("qa_questions")
    if not isinstance(questions, list):
        raise ContractError("R00_PAPER_MARK_ANCHOR.qa_questions must be a list")
    normalized: list[tuple[str, bool, str]] = []
    for item in questions:
        if not isinstance(item, dict):
            raise ContractError("R00_PAPER_MARK_ANCHOR.qa_questions entries must be objects")
        question_id = item.get("question_id")
        expected = item.get("expected")
        question = item.get("question")
        if not isinstance(question_id, str) or not isinstance(expected, bool) or not isinstance(question, str):
            raise ContractError("R00 QA question must contain question_id:string, expected:bool, question:string")
        normalized.append((question_id, expected, question))
    return normalized


def load_skill_definitions() -> list[dict[str, Any]]:
    contract = load_contract("skill_definitions")
    skills = contract.get("skills")
    if not isinstance(skills, list):
        raise ContractError("skill_definitions.json must contain list key: skills")
    if not all(isinstance(skill, dict) for skill in skills):
        raise ContractError("skill_definitions.json skills entries must be objects")
    return skills

