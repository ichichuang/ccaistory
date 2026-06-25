from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any


RUNTIME_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = RUNTIME_ROOT.parent
if str(RUNTIME_ROOT) not in sys.path:
    sys.path.insert(0, str(RUNTIME_ROOT))

from contracts.contract_loader import r00_forbidden_positive_terms, r00_required_questions
from contracts.validate_contracts import validate_contracts, validate_skill_definitions
from core.io import result
from lint_engine.semantic_lint import get_r00_forbidden_positive_terms
from qa_engine.asset_qa import get_r00_required_questions


# R00 drift sources — active canonical docs only. The two legacy copies
# (legacy-prompt-library/R00纸张笔触锚图锁.md, legacy-control/状态机与门禁.md)
# were removed in the hard cleanup; the same R00 forbidden-content terms are
# still enforced across these active canonical files (logic unchanged).
R00_MARKDOWN_FILES = [
    "02-wiki/story-lab/80-skills-tools-workflows/structure-specs/视觉资产本体结构规范.md",
    "02-wiki/story-lab/80-skills-tools-workflows/structure-specs/源插图语义Lint结构规范.md",
    "02-wiki/story-lab/80-skills-tools-workflows/acceptance-checklists/R00纸张笔触锚图验收清单.md",
    "02-wiki/story-lab/80-skills-tools-workflows/acceptance-checklists/源插图语义Lint验收清单.md",
]

R00_MARKDOWN_REQUIRED_TERMS = {
    "人物": ["人物"],
    "火柴人": ["火柴人"],
    "完整场景": ["完整场景", "场景清单"],
    "道具集合": ["道具集合", "道具清单"],
    "符号散点表": ["符号散点表", "符号表"],
}


def _relative(path: Path) -> str:
    return str(path.relative_to(PROJECT_ROOT))


def _markdown_r00_drift() -> list[str]:
    failures: list[str] = []
    for name in R00_MARKDOWN_FILES:
        path = PROJECT_ROOT / name
        if not path.exists():
            failures.append(f"markdown_missing:{name}")
            continue
        text = path.read_text(encoding="utf-8")
        for canonical, aliases in R00_MARKDOWN_REQUIRED_TERMS.items():
            if not any(alias in text for alias in aliases):
                failures.append(f"markdown_r00_term_missing:{name}:{canonical}")
    return failures


def _target_exists(target: str, source: Path) -> bool:
    if target.startswith(("http://", "https://")):
        return True
    cleaned = target.split("#", 1)[0].strip()
    if not cleaned:
        return True
    candidates = []
    if "/" in cleaned:
        candidates.append(PROJECT_ROOT / cleaned)
        candidates.append(PROJECT_ROOT / f"{cleaned}.md")
    else:
        candidates.append(source.parent / cleaned)
        candidates.append(source.parent / f"{cleaned}.md")
    return any(candidate.exists() for candidate in candidates)


def check_markdown_links() -> dict[str, Any]:
    broken: list[dict[str, str]] = []
    for path in sorted(PROJECT_ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for match in re.finditer(r"\[\[([^\]|]+)", text):
            target = match.group(1).strip()
            if not _target_exists(target, path):
                broken.append({"source": _relative(path), "target": target})
    return {"broken_link_count": len(broken), "broken_links": broken}


def check_contract_drift() -> dict[str, Any]:
    failures: list[str] = []
    contract_validation = validate_contracts()
    if not contract_validation["passed"]:
        failures.append("contracts_invalid")

    if get_r00_forbidden_positive_terms() != r00_forbidden_positive_terms():
        failures.append("python_semantic_lint_r00_forbidden_terms_drift")
    if get_r00_required_questions() != r00_required_questions():
        failures.append("python_asset_qa_r00_questions_drift")

    skill_failures: list[str] = []
    validate_skill_definitions(skill_failures)
    if skill_failures:
        failures.append("skill_definitions_registry_drift")

    failures.extend(_markdown_r00_drift())
    link_result = check_markdown_links()
    if link_result["broken_link_count"]:
        failures.append("markdown_broken_links")

    return result(
        not failures,
        contract_validation=contract_validation,
        link_check=link_result,
        failures=list(dict.fromkeys(failures)),
    )


def main() -> int:
    from core.io import print_json

    payload = check_contract_drift()
    print_json(payload)
    return 0 if payload["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

