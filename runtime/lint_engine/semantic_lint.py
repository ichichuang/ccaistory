from __future__ import annotations

import re
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

SERIES_CONTINUITY_FIELDS = [
    "previous_page_reference",
    "previous_page_scene_summary",
    "current_page_scene_summary",
    "r00_reference_asset",
    "continuity_from_previous_page",
    "scene_delta_from_previous_page",
    "allowed_progression_delta",
    "forbidden_continuity_breaks",
    "page_hook_question",
    "hook_visual_target",
    "hook_annotation_guidance",
    "escalation_level",
]

HOOK_GUARDRAIL_FIELDS = [
    "hook_failure_mode_to_avoid",
    "symbol_semantics_target",
    "symbol_misread_to_avoid",
    "repair_guardrails",
    "progression_budget_from_previous_page",
    "overcorrection_guardrail",
    "composition_priority_order",
]

EARLY_PAGE_INTENSITY_JUMP_TERMS = [
    "deep dense forest",
    "dense forest tunnel",
    "dense dark forest",
    "fully enclosed dark tunnel",
    "dramatically denser",
    "lamp-lined road",
    "many lamps",
    "too many lamps",
    "deep night",
    "pitch black",
    "full darkness",
    "too black",
    "visually heavy",
    "密林深处",
    "森林隧道",
    "整排路灯",
    "很多路灯",
    "深夜",
    "漆黑一片",
]

GENERIC_HOOK_TERMS = [
    "有点黑",
    "好可怕",
    "it is dark",
    "so dark",
    "very dark",
    "too dark",
    "scary",
    "creepy",
]

HOOK_DOMINANCE_TERMS = [
    "dominates the page",
    "dominates the whole composition",
    "center of the whole composition",
    "main focus of the whole page",
    "large central clue",
    "huge clue",
    "占据画面",
    "成为画面中心",
]


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


def _is_missing(value: Any) -> bool:
    return value in (None, "", [], {})


def _truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "1"}
    return False


def _page_index(spec: dict[str, Any]) -> int | None:
    for field in ("page_index", "page_number"):
        value = spec.get(field)
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.strip().isdigit():
            return int(value.strip())

    page_text = _stringify(
        [
            spec.get("page_or_spread_range", ""),
            spec.get("page", ""),
            spec.get("asset_scope", ""),
            spec.get("source_package_id", ""),
            spec.get("asset_id", ""),
        ]
    ).lower()
    match = re.search(r"\bp(?:age)?[-_ ]?0*(\d{1,3})\b", page_text)
    if match:
        return int(match.group(1))
    return None


def _requires_series_continuity(spec: dict[str, Any]) -> bool:
    has_series_contract_payload = (
        spec.get("continuity_qa_required") is not None
        or spec.get("hook_qa_required") is not None
        or any(not _is_missing(spec.get(field)) for field in SERIES_CONTINUITY_FIELDS)
    )
    if spec.get("_compiled_prompt") and not has_series_contract_payload:
        return False
    if _truthy(spec.get("continuity_qa_required")) or _truthy(spec.get("hook_qa_required")):
        return True
    page_index = _page_index(spec)
    return spec.get("asset_type") == "S_SOURCE_ILLUSTRATION" and page_index is not None and page_index > 1


def _is_early_serial_page(spec: dict[str, Any]) -> bool:
    page_index = _page_index(spec)
    return page_index is not None and 1 < page_index <= 3


def _hook_is_generic(hook: str, target: str) -> bool:
    normalized = hook.strip().lower()
    if not normalized:
        return True
    if normalized in {"黑了", "dark", "scary", "creepy", "好黑", "可怕"}:
        return True
    if any(term in normalized for term in GENERIC_HOOK_TERMS) and not target.strip():
        return True
    return False


def _nonempty_items(value: Any) -> list[str]:
    if isinstance(value, str):
        text = value.strip()
        return [text] if text else []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return []


def _words(value: Any) -> set[str]:
    text = _stringify(value).lower()
    return {item for item in re.split(r"[^a-z0-9\u4e00-\u9fff]+", text) if item}


def lint_asset(spec: dict[str, Any]) -> dict[str, Any]:
    failed: list[str] = []
    asset_scope_conflicts: list[str] = []
    missing_fields: list[str] = []
    risky_terms: list[str] = []
    forbidden_content_violations: list[str] = []
    series_continuity_violations: list[str] = []
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

    if _requires_series_continuity(spec):
        for field in SERIES_CONTINUITY_FIELDS:
            if _is_missing(spec.get(field)):
                missing_fields.append(field)
                series_continuity_violations.append(f"missing_{field}")
                failed.append(f"missing_{field}")
        if not _truthy(spec.get("continuity_qa_required")):
            series_continuity_violations.append("continuity_qa_not_required")
            failed.append("continuity_qa_not_required")
        if not _truthy(spec.get("hook_qa_required")):
            series_continuity_violations.append("hook_qa_not_required")
            failed.append("hook_qa_not_required")

        hook = str(spec.get("page_hook_question", ""))
        hook_target = str(spec.get("hook_visual_target", ""))
        if _hook_is_generic(hook, hook_target):
            series_continuity_violations.append("generic_or_missing_page_hook")
            failed.append("generic_or_missing_page_hook")
            suggestions.append("Replace generic mood hooks with a specific page-turn visual question.")

        if _is_early_serial_page(spec):
            intensity_terms = [term for term in EARLY_PAGE_INTENSITY_JUMP_TERMS if term in positive_text]
            if intensity_terms:
                series_continuity_violations.extend(f"early_page_intensity_jump:{term}" for term in intensity_terms)
                failed.append("early_page_intensity_jump")
                suggestions.append(
                    "Keep early serialized pages to one controlled environment or mystery delta unless the Story Graph explicitly requires more."
                )

        guardrail_payload_present = any(not _is_missing(spec.get(field)) for field in HOOK_GUARDRAIL_FIELDS)
        if guardrail_payload_present:
            symbol_target = spec.get("symbol_semantics_target")
            symbol_misread = spec.get("symbol_misread_to_avoid")
            overcorrection_guardrail = spec.get("overcorrection_guardrail")
            progression_budget = spec.get("progression_budget_from_previous_page")
            repair_guardrails = spec.get("repair_guardrails")
            composition_priority = spec.get("composition_priority_order")

            for field, value in (
                ("symbol_semantics_target", symbol_target),
                ("symbol_misread_to_avoid", symbol_misread),
                ("overcorrection_guardrail", overcorrection_guardrail),
                ("progression_budget_from_previous_page", progression_budget),
                ("composition_priority_order", composition_priority),
            ):
                if _is_missing(value):
                    missing_fields.append(field)
                    series_continuity_violations.append(f"missing_{field}")
                    failed.append(f"missing_{field}")

            if not _nonempty_items(repair_guardrails):
                missing_fields.append("repair_guardrails")
                series_continuity_violations.append("missing_repair_guardrails")
                failed.append("missing_repair_guardrails")

            target_words = _words(symbol_target)
            misread_words = _words(symbol_misread)
            if target_words and misread_words and target_words == misread_words:
                series_continuity_violations.append("symbol_semantics_target_matches_misread")
                failed.append("symbol_semantics_target_matches_misread")
                suggestions.append("Separate the intended clue semantics from the object class it must not be misread as.")

            priority_items = _nonempty_items(composition_priority)
            priority_text = " ".join(priority_items).lower()
            if priority_items and not (("first" in priority_text or "第一" in priority_text) and ("second" in priority_text or "第二" in priority_text)):
                series_continuity_violations.append("composition_priority_missing_read_order")
                failed.append("composition_priority_missing_read_order")
                suggestions.append("State the first read as scene continuity and the second read as hidden clue discovery.")

            if any(term in positive_text for term in HOOK_DOMINANCE_TERMS):
                series_continuity_violations.append("hook_dominates_scene_too_early")
                failed.append("hook_dominates_scene_too_early")
                suggestions.append("Keep the clue integrated into the environment; scene continuity should read before hook discovery.")

            if _is_missing(overcorrection_guardrail) and _nonempty_items(repair_guardrails):
                series_continuity_violations.append("repair_without_overcorrection_guardrail")
                failed.append("repair_without_overcorrection_guardrail")
                suggestions.append("Add an overcorrection guardrail so repairing one issue cannot break previous-page continuity.")

        r00_reference = str(spec.get("r00_reference_asset", ""))
        r00_policy_text = _stringify(
            {
                "r00_dependency_policy": spec.get("r00_dependency_policy"),
                "style_policy": spec.get("style_policy"),
                "reference_dependencies": spec.get("reference_dependencies"),
            }
        ).lower()
        if r00_reference and r00_policy_text and not any(
            term in r00_policy_text
            for term in ("style", "paper", "line", "red-pen", "character", "proportion", "纸", "线", "红笔", "角色", "比例")
        ):
            series_continuity_violations.append("r00_usage_not_limited_to_visual_continuity")
            failed.append("r00_usage_not_limited_to_visual_continuity")
            suggestions.append("Limit R00 usage to visual style, paper, line, red-pen language, character appearance, and proportions.")

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
            "series_continuity_violations": list(dict.fromkeys(series_continuity_violations)),
            "failed_rules": failed_unique,
            "repair_suggestions": list(dict.fromkeys(suggestions)),
        },
    )


def lint_compiled_prompt(compiled: dict[str, Any]) -> dict[str, Any]:
    prompt_sections = compiled.get("prompt_sections", {})
    if not isinstance(prompt_sections, dict):
        prompt_sections = {}
    series_continuity = prompt_sections.get("series_continuity", {})
    if not isinstance(series_continuity, dict):
        series_continuity = {}

    def continuity_field(name: str) -> Any:
        return compiled.get(name, series_continuity.get(name))

    spec = {
        "asset_type": compiled.get("asset_type"),
        "_compiled_prompt": True,
        "asset_id": compiled.get("asset_id"),
        "asset_scope": compiled.get("asset_scope"),
        "source_package_id": compiled.get("source_package_id"),
        "page_index": compiled.get("page_index"),
        "page_or_spread_range": compiled.get("page_or_spread_range"),
        "allowed_content": prompt_sections.get("allowed_content", []),
        "forbidden_content": compiled.get("forbidden_content", []),
        "visual_center": prompt_sections.get("visual_center"),
        "density_range": prompt_sections.get("density_range"),
        "composition_mode": prompt_sections.get("composition_mode"),
        "acceptance_questions": compiled.get("acceptance_questions") or compiled.get("asset_specific_acceptance_criteria"),
        "canvas_ratio": compiled.get("canvas_ratio"),
        "compiled_prompt": compiled.get("compiled_prompt", ""),
        "style_instruction": compiled.get("style_instruction"),
        "style_policy": compiled.get("style_policy", prompt_sections.get("style_policy")),
        "reference_dependencies": compiled.get("reference_dependencies", prompt_sections.get("reference_dependencies")),
        "r00_dependency_policy": compiled.get("r00_dependency_policy"),
        "continuity_qa_required": continuity_field("continuity_qa_required"),
        "hook_qa_required": continuity_field("hook_qa_required"),
    }
    for field in SERIES_CONTINUITY_FIELDS:
        spec[field] = continuity_field(field)
    for field in HOOK_GUARDRAIL_FIELDS:
        spec[field] = continuity_field(field)
    return lint_asset(spec)


def lint_asset_file(path: str) -> dict[str, Any]:
    return lint_asset(read_json(path))


def lint_compiled_file(path: str) -> dict[str, Any]:
    return lint_compiled_prompt(read_json(path))
