from __future__ import annotations

from typing import Any

from contracts.contract_loader import ContractError, r00_forbidden_positive_terms
from core.io import read_json, result


REQUIRED_FIELDS = [
    "asset_type",
    "allowed_content",
    "forbidden_content",
    "visual_center",
    "density_range",
    "composition_mode",
    "acceptance_questions",
]

AUTHOR_STYLE_TERMS = ["style of", "by artist", "模仿", "仿照", "作者风格", "以某作者"]


def get_r00_forbidden_positive_terms() -> list[str]:
    return r00_forbidden_positive_terms()


def _stringify(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return " ".join(_stringify(item) for item in value)
    if isinstance(value, dict):
        return " ".join(_stringify(item) for item in value.values())
    return str(value)


def _positive_text(spec: dict[str, Any]) -> str:
    fields = [
        "allowed_content",
        "visual_center",
        "composition_mode",
        "description",
        "positive_prompt",
        "compiled_prompt",
    ]
    return " ".join(_stringify(spec.get(field, "")) for field in fields).lower()


def lint_asset(spec: dict[str, Any]) -> dict[str, Any]:
    failed: list[str] = []
    asset_scope_conflicts: list[str] = []
    missing_fields: list[str] = []
    risky_terms: list[str] = []
    forbidden_content_violations: list[str] = []
    suggestions: list[str] = []
    asset_type = spec.get("asset_type")

    for field in REQUIRED_FIELDS:
        if spec.get(field) in (None, "", []):
            rule = f"missing_{field}"
            missing_fields.append(field)
            failed.append(rule)
            suggestions.append(f"Fill required field: {field}")

    positive_text = _positive_text(spec)
    if asset_type == "R00_PAPER_MARK_ANCHOR":
        try:
            forbidden_terms = get_r00_forbidden_positive_terms()
        except ContractError as exc:
            failed.append("contract_missing")
            suggestions.append(str(exc))
        else:
            for term in forbidden_terms:
                if term.lower() in positive_text:
                    asset_scope_conflicts.append(term)
                    failed.append("r00_scope_conflict")
                    suggestions.append(
                        "Remove characters, stick figures, scenes, prop sets, and symbol sheets from R00 positive scope."
                    )
                    break

    if asset_type == "R01_CHARACTER_ANCHOR" and any(term in positive_text for term in ("完整剧情", "主线剧情", "complete plot")):
        asset_scope_conflicts.append("complete_plot_payload")
        failed.append("r01_complete_plot_payload")
        suggestions.append("Limit R01 to character anchor facts only.")

    if asset_type == "R02_SCENE_PROP_ANCHOR" and any(term in positive_text for term in ("主线事件", "关键剧情", "mainline event")):
        asset_scope_conflicts.append("mainline_event_payload")
        failed.append("r02_mainline_event_payload")
        suggestions.append("Limit R02 to scene or prop anchor facts only.")

    if asset_type == "S_SOURCE_ILLUSTRATION" and any(term in positive_text for term in ("长手写正文", "long handwritten body")):
        asset_scope_conflicts.append("long_handwritten_body")
        failed.append("s_long_handwritten_body")
        suggestions.append("Keep S page handwriting short and clue-like.")

    if asset_type == "P01_PLATFORM_LAYOUT_SAMPLE" and str(spec.get("canvas_ratio")) != "9:16":
        asset_scope_conflicts.append("canvas_ratio_not_9_16")
        failed.append("p01_not_9_16")
        suggestions.append("Set P01 canvas_ratio to 9:16.")

    style_text = _stringify(
        {
            "style_instruction": spec.get("style_instruction"),
            "style_reference": spec.get("style_reference"),
            "author_name": spec.get("author_name"),
        }
    ).lower()
    if spec.get("style_reference_type") == "author_name" or any(term in style_text for term in AUTHOR_STYLE_TERMS):
        risky_terms.append("author_name_style_instruction")
        failed.append("author_name_as_style_instruction")
        suggestions.append("Replace author-name style instruction with abstract technique requirements.")

    forbidden = spec.get("forbidden_content", [])
    if isinstance(forbidden, str):
        forbidden = [forbidden]
    compiled_prompt = str(spec.get("compiled_prompt", "")).lower()
    for item in forbidden:
        if item and str(item).lower() in compiled_prompt:
            forbidden_content_violations.append(str(item))
            failed.append("forbidden_content_in_compiled_prompt")
            suggestions.append("Move forbidden content to lint constraints, not the positive compiled prompt.")
            break

    failed_unique = list(dict.fromkeys(failed))
    return result(
        not failed_unique,
        semantic_lint_result={
            "asset_scope_conflicts": list(dict.fromkeys(asset_scope_conflicts)),
            "missing_fields": list(dict.fromkeys(missing_fields)),
            "risky_terms": list(dict.fromkeys(risky_terms)),
            "forbidden_content_violations": list(dict.fromkeys(forbidden_content_violations)),
            "failed_rules": failed_unique,
            "repair_suggestions": list(dict.fromkeys(suggestions)),
        },
    )


def lint_compiled_prompt(compiled: dict[str, Any]) -> dict[str, Any]:
    spec = {
        "asset_type": compiled.get("asset_type"),
        "allowed_content": compiled.get("prompt_sections", {}).get("allowed_content", []),
        "forbidden_content": compiled.get("forbidden_content", []),
        "visual_center": compiled.get("prompt_sections", {}).get("visual_center"),
        "density_range": compiled.get("prompt_sections", {}).get("density_range"),
        "composition_mode": compiled.get("prompt_sections", {}).get("composition_mode"),
        "acceptance_questions": compiled.get("acceptance_questions") or compiled.get("asset_specific_acceptance_criteria"),
        "canvas_ratio": compiled.get("canvas_ratio"),
        "compiled_prompt": compiled.get("compiled_prompt", ""),
        "style_instruction": compiled.get("style_instruction"),
    }
    return lint_asset(spec)


def lint_asset_file(path: str) -> dict[str, Any]:
    return lint_asset(read_json(path))


def lint_compiled_file(path: str) -> dict[str, Any]:
    return lint_compiled_prompt(read_json(path))
