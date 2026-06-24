from __future__ import annotations

from typing import Any

from core.io import read_json, result


SUPPORTED_ASSET_TYPES = {
    "R00_PAPER_MARK_ANCHOR",
    "R01_CHARACTER_ANCHOR",
    "R02_SCENE_PROP_ANCHOR",
    "P01_PLATFORM_LAYOUT_SAMPLE",
    "S_SOURCE_ILLUSTRATION",
}

REQUIRED_SPEC_FIELDS = [
    "asset_id",
    "asset_type",
    "asset_scope",
    "allowed_content",
    "forbidden_content",
    "visual_center",
    "density_range",
    "composition_mode",
    "text_policy",
    "paper_policy",
    "style_policy",
    "reference_dependencies",
    "acceptance_questions",
    "repair_policy",
]


def _is_missing_required(value: Any) -> bool:
    return value in (None, "", [], {})


def _is_missing_spec_field(spec: dict[str, Any], field: str) -> bool:
    if field == "reference_dependencies":
        return field not in spec or not isinstance(spec.get(field), list)
    return _is_missing_required(spec.get(field))


def compile_asset(spec: dict[str, Any]) -> dict[str, Any]:
    missing = [field for field in REQUIRED_SPEC_FIELDS if _is_missing_spec_field(spec, field)]
    asset_type = spec.get("asset_type")
    if asset_type not in SUPPORTED_ASSET_TYPES:
        missing.append("asset_type:supported")
    if missing:
        return result(False, missing_fields=missing)

    allowed_content = spec.get("allowed_content", [])
    if isinstance(allowed_content, str):
        allowed_content = [allowed_content]

    prompt_sections = {
        "asset_type": asset_type,
        "visual_center": spec["visual_center"],
        "allowed_content": allowed_content,
        "density_range": spec["density_range"],
        "composition_mode": spec["composition_mode"],
        "text_policy": spec["text_policy"],
        "paper_policy": spec["paper_policy"],
        "style_policy": spec["style_policy"],
        "reference_dependencies": spec["reference_dependencies"],
        "negative_constraints_ref": "Use forbidden_content as blocking constraints; do not render them as requested content.",
    }
    compiled_prompt = (
        f"Asset type: {asset_type}. "
        f"Visual center: {spec['visual_center']}. "
        f"Allowed content: {'; '.join(map(str, allowed_content))}. "
        f"Density: {spec['density_range']}. "
        f"Composition: {spec['composition_mode']}. "
        f"Text policy: {spec['text_policy']}. "
        f"Paper policy: {spec['paper_policy']}. "
        f"Style policy: {spec['style_policy']}."
    )
    criteria = asset_acceptance_criteria(asset_type)
    return result(
        True,
        compiled_prompt={
            "asset_id": spec.get("asset_id"),
            "asset_type": asset_type,
            "asset_scope": spec.get("asset_scope"),
            "compiled_prompt": compiled_prompt,
            "prompt_sections": prompt_sections,
            "forbidden_content": spec.get("forbidden_content", []),
            "asset_specific_acceptance_criteria": criteria,
            "canvas_ratio": spec.get("canvas_ratio"),
            "reference_dependencies": spec.get("reference_dependencies", []),
            "text_policy": spec.get("text_policy"),
            "paper_policy": spec.get("paper_policy"),
            "style_policy": spec.get("style_policy"),
            "acceptance_questions": spec.get("acceptance_questions", spec.get("acceptance_criteria", [])),
            "repair_policy": spec.get("repair_policy"),
        },
    )


def asset_acceptance_criteria(asset_type: str) -> list[str]:
    criteria = {
        "R00_PAPER_MARK_ANCHOR": [
            "no_person",
            "no_stick_figure",
            "clean_white_paper",
            "controlled_child_handwriting_sample",
            "usable_as_reference_asset",
        ],
        "R01_CHARACTER_ANCHOR": ["single_character_focus", "no_complete_plot_payload"],
        "R02_SCENE_PROP_ANCHOR": ["scene_or_prop_focus", "no_mainline_event_payload"],
        "P01_PLATFORM_LAYOUT_SAMPLE": ["canvas_ratio_9_16", "layout_sample_only"],
        "S_SOURCE_ILLUSTRATION": ["single_page_semantics", "no_long_handwritten_body"],
    }
    return criteria.get(asset_type, [])


def compile_asset_file(path: str) -> dict[str, Any]:
    return compile_asset(read_json(path))
