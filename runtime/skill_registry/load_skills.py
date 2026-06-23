from __future__ import annotations

from pathlib import Path
from typing import Any

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
    skills_path = Path(path) if path else SKILLS_FILE
    data = load_json_file(skills_path)
    if isinstance(data, dict):
        skills = data.get("skills", [])
    else:
        skills = data
    if not isinstance(skills, list):
        raise ValueError("skills.json must contain a list or a {skills: [...]} object")
    return skills


def validate_skills(skills: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    loaded = skills if skills is not None else load_skills()
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
