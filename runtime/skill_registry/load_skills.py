from __future__ import annotations

from pathlib import Path
from typing import Any

from contracts.contract_loader import ContractError, load_skill_definitions
from core.io import RUNTIME_ROOT, load_json_file, result


SKILLS_FILE = RUNTIME_ROOT / "skill_registry" / "skills.json"

REQUIRED_FIELDS = [
    "skill_id",
    "display_name",
    "applies_to",
    "input_fields",
    "output_fields",
    "graph_fields_affected",
    "validation_questions",
    "hard_failures",
    "repair_actions",
    "compatible_skills",
    "forbidden_uses",
]


def load_skills(path: str | Path | None = None) -> list[dict[str, Any]]:
    if path is None:
        return load_skill_definitions()
    skills_path = Path(path)
    data = load_json_file(skills_path)
    if isinstance(data, dict):
        skills = data.get("skills", [])
    else:
        skills = data
    if not isinstance(skills, list):
        raise ValueError("skills.json must contain a list or a {skills: [...]} object")
    return skills


def validate_skill_contract_consistency(contract_skills: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    try:
        loaded_contract_skills = contract_skills if contract_skills is not None else load_skill_definitions()
    except ContractError as exc:
        return result(False, skill_count=0, failures=[{"skill_id": "<contract>", "missing_fields": [str(exc)]}])

    registry_skills = load_skills(SKILLS_FILE)
    contract_by_id = {skill.get("skill_id"): skill for skill in loaded_contract_skills}
    registry_by_id = {skill.get("skill_id"): skill for skill in registry_skills}
    failures: list[dict[str, Any]] = []
    if len(loaded_contract_skills) != 12:
        failures.append({"skill_id": "<contract>", "missing_fields": [f"skill_count:12:{len(loaded_contract_skills)}"]})
    if set(contract_by_id) != set(registry_by_id):
        failures.append(
            {
                "skill_id": "<contract>",
                "missing_fields": [
                    f"skill_id_set:{sorted(set(registry_by_id) - set(contract_by_id))}:{sorted(set(contract_by_id) - set(registry_by_id))}"
                ],
            }
        )
    for skill_id, contract_skill in contract_by_id.items():
        registry_skill = registry_by_id.get(skill_id)
        if registry_skill is None:
            continue
        mismatched = [
            field
            for field in ("input_fields", "output_fields", "hard_failures", "repair_actions")
            if contract_skill.get(field) != registry_skill.get(field)
        ]
        if mismatched:
            failures.append({"skill_id": str(skill_id), "missing_fields": [f"contract_mismatch:{field}" for field in mismatched]})
    return result(not failures, skill_count=len(loaded_contract_skills), registry_skill_count=len(registry_skills), failures=failures)


def validate_skills(skills: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    if skills is None:
        consistency = validate_skill_contract_consistency()
        if not consistency["passed"]:
            return consistency
        loaded = load_skills()
    else:
        loaded = skills
    failures: list[dict[str, Any]] = []
    seen: set[str] = set()
    for skill in loaded:
        missing = [field for field in REQUIRED_FIELDS if field not in skill]
        skill_id = str(skill.get("skill_id", ""))
        if not skill_id:
            missing.append("skill_id:value")
        if skill_id in seen:
            missing.append("skill_id:unique")
        seen.add(skill_id)
        if missing:
            failures.append({"skill_id": skill_id or "<missing>", "missing_fields": missing})
    return result(not failures, skill_count=len(loaded), failures=failures)


def skill_map() -> dict[str, dict[str, Any]]:
    return {skill["skill_id"]: skill for skill in load_skills()}
