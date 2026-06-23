from __future__ import annotations

import json
from pathlib import Path
from typing import Any


RUNTIME_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = RUNTIME_ROOT.parent


def resolve_path(path: str | Path) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return PROJECT_ROOT / candidate


def read_json(path: str | Path) -> dict[str, Any]:
    resolved = resolve_path(path)
    with resolved.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"JSON root must be an object: {resolved}")
    return data


def load_json_file(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def print_json(data: Any) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True))


def result(passed: bool, **payload: Any) -> dict[str, Any]:
    return {"status": "pass" if passed else "fail", "passed": passed, **payload}


def find_story_core(project_path: str | Path) -> Path | None:
    base = resolve_path(project_path)
    if base.is_file():
        return base
    for name in ("story_core.json", "故事核心.json"):
        candidate = base / name
        if candidate.exists():
            return candidate
    return None
