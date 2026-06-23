from __future__ import annotations

import json
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from artifact_registry.artifact_schema import ARTIFACT_STATUSES, validate_artifact_schema
from artifact_registry.validators import validate_artifact
from core.io import RUNTIME_ROOT, resolve_path, result


ARTIFACTS_ROOT = RUNTIME_ROOT / ".artifacts"
DEFAULT_REGISTRY_PATH = ARTIFACTS_ROOT / "registry.json"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _registry_path(path: str | Path | None = None) -> Path:
    if path is None:
        return DEFAULT_REGISTRY_PATH
    return resolve_path(path)


def _empty_registry() -> dict[str, Any]:
    now = _now()
    return {"registry_version": 1, "created_at": now, "updated_at": now, "artifacts": {}}


def load_registry(path: str | Path | None = None) -> dict[str, Any]:
    resolved = _registry_path(path)
    if not resolved.exists():
        resolved.parent.mkdir(parents=True, exist_ok=True)
        registry = _empty_registry()
        _write_registry(registry, resolved)
        return registry
    with resolved.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"registry root must be object: {resolved}")
    artifacts = data.setdefault("artifacts", {})
    if isinstance(artifacts, list):
        data["artifacts"] = {
            item["artifact_id"]: item
            for item in artifacts
            if isinstance(item, dict) and isinstance(item.get("artifact_id"), str)
        }
    elif not isinstance(artifacts, dict):
        raise ValueError(f"registry artifacts must be object: {resolved}")
    data.setdefault("registry_version", 1)
    data.setdefault("created_at", _now())
    data.setdefault("updated_at", data["created_at"])
    return data


def _write_registry(registry: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    registry["updated_at"] = _now()
    path.write_text(json.dumps(registry, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def save_registry(registry: dict[str, Any], path: str | Path | None = None) -> None:
    _write_registry(registry, _registry_path(path))


def _artifact_items(registry: dict[str, Any]) -> dict[str, dict[str, Any]]:
    artifacts = registry.get("artifacts", {})
    if not isinstance(artifacts, dict):
        return {}
    return {key: value for key, value in artifacts.items() if isinstance(value, dict)}


def register_artifact(
    artifact: dict[str, Any],
    *,
    registry_path: str | Path | None = None,
    dry_run: bool = False,
) -> dict[str, Any]:
    registry = load_registry(registry_path)
    artifacts = _artifact_items(registry)
    artifact_id = artifact.get("artifact_id")
    schema_result = validate_artifact_schema(artifact)
    if not schema_result["passed"]:
        return schema_result
    if artifact_id in artifacts:
        return result(False, artifact_id=artifact_id, failures=["duplicate_artifact_id"])

    validation_registry = deepcopy(registry)
    validation_registry["artifacts"] = {**artifacts}
    validation = validate_artifact(artifact, validation_registry)
    if not validation["passed"]:
        return validation

    if not dry_run:
        registry["artifacts"][artifact_id] = deepcopy(artifact)
        save_registry(registry, registry_path)
    return result(
        True,
        artifact_id=artifact_id,
        dry_run=dry_run,
        registry_path=str(_registry_path(registry_path)),
        artifact=artifact,
        failures=[],
    )


def list_artifacts(*, registry_path: str | Path | None = None) -> dict[str, Any]:
    registry = load_registry(registry_path)
    artifacts = list(_artifact_items(registry).values())
    return result(True, artifact_count=len(artifacts), artifacts=artifacts)


def get_artifact(artifact_id: str, *, registry_path: str | Path | None = None) -> dict[str, Any]:
    registry = load_registry(registry_path)
    artifact = _artifact_items(registry).get(artifact_id)
    if artifact is None:
        return result(False, artifact_id=artifact_id, failures=["artifact_not_found"])
    return result(True, artifact_id=artifact_id, artifact=artifact)


def query_artifacts(
    *,
    project_id: str = "",
    asset_id: str = "",
    status: str = "",
    registry_path: str | Path | None = None,
) -> dict[str, Any]:
    artifacts = list(_artifact_items(load_registry(registry_path)).values())
    if project_id:
        artifacts = [artifact for artifact in artifacts if artifact.get("project_id") == project_id]
    if asset_id:
        artifacts = [artifact for artifact in artifacts if artifact.get("asset_id") == asset_id]
    if status:
        artifacts = [artifact for artifact in artifacts if artifact.get("status") == status]
    return result(True, artifact_count=len(artifacts), artifacts=artifacts)


def update_artifact_status(
    artifact_id: str,
    status: str,
    *,
    registry_path: str | Path | None = None,
    dry_run: bool = False,
) -> dict[str, Any]:
    if status not in ARTIFACT_STATUSES:
        return result(False, artifact_id=artifact_id, failures=[f"unknown_status:{status}"])
    registry = load_registry(registry_path)
    artifacts = _artifact_items(registry)
    artifact = artifacts.get(artifact_id)
    if artifact is None:
        return result(False, artifact_id=artifact_id, failures=["artifact_not_found"])
    updated = deepcopy(artifact)
    updated["status"] = status
    validation = validate_artifact(updated, registry)
    if not validation["passed"]:
        return validation
    if not dry_run:
        registry["artifacts"][artifact_id] = updated
        save_registry(registry, registry_path)
    return result(True, artifact_id=artifact_id, status=status, dry_run=dry_run, artifact=updated, failures=[])


def validate_artifact_by_id(artifact_id: str, *, registry_path: str | Path | None = None) -> dict[str, Any]:
    registry = load_registry(registry_path)
    artifact = _artifact_items(registry).get(artifact_id)
    if artifact is None:
        return result(False, artifact_id=artifact_id, failures=["artifact_not_found"])
    return validate_artifact(artifact, registry)


def check_registry(*, registry_path: str | Path | None = None) -> dict[str, Any]:
    registry = load_registry(registry_path)
    artifacts = _artifact_items(registry)
    failures: list[str] = []
    missing_dependencies: list[dict[str, str]] = []
    for artifact_id, artifact in artifacts.items():
        schema_result = validate_artifact_schema(artifact)
        if not schema_result["passed"]:
            failures.extend(f"{artifact_id}:{failure}" for failure in schema_result["failures"])
            continue
        validation = validate_artifact(artifact, registry)
        if not validation["passed"]:
            failures.extend(f"{artifact_id}:{failure}" for failure in validation["failures"])
        for linked_id in [*artifact.get("parent_artifact_ids", []), *artifact.get("dependency_artifact_ids", [])]:
            if linked_id not in artifacts:
                missing_dependencies.append({"artifact_id": artifact_id, "missing_artifact_id": linked_id})
    return result(
        not failures and not missing_dependencies,
        artifact_count=len(artifacts),
        missing_dependencies=missing_dependencies,
        broken_link_count=len(missing_dependencies),
        failures=list(dict.fromkeys(failures)),
        registry_path=str(_registry_path(registry_path)),
    )
