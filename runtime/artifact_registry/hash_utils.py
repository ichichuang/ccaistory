from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from core.io import PROJECT_ROOT, resolve_path, result


def _digest_bytes(data: bytes) -> dict[str, str]:
    return {"hash": hashlib.sha256(data).hexdigest(), "algorithm": "sha256"}


def _is_relative_to(child: Path, parent: Path) -> bool:
    try:
        child.relative_to(parent)
    except ValueError:
        return False
    return True


def string_sha256(content: str) -> dict[str, Any]:
    if not isinstance(content, str) or content == "":
        return result(False, failures=["empty_string_input"], hash="", algorithm="sha256")
    return _digest_bytes(content.encode("utf-8"))


def json_sha256(payload: Any) -> dict[str, Any]:
    if payload in (None, "", [], {}):
        return result(False, failures=["empty_json_input"], hash="", algorithm="sha256")
    try:
        canonical = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    except TypeError as exc:
        return result(False, failures=[f"json_not_serializable:{exc}"], hash="", algorithm="sha256")
    return _digest_bytes(canonical.encode("utf-8"))


def file_sha256(path: str | Path) -> dict[str, Any]:
    resolved = resolve_path(path).resolve()
    project_root = PROJECT_ROOT.resolve()
    if not _is_relative_to(resolved, project_root):
        return result(False, failures=["file_outside_project_root"], hash="", algorithm="sha256")
    if not resolved.is_file():
        return result(False, failures=["file_not_found"], hash="", algorithm="sha256")

    data = resolved.read_bytes()
    if not data:
        return result(False, failures=["empty_file_input"], hash="", algorithm="sha256")
    return _digest_bytes(data)
