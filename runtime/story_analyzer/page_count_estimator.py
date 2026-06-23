from __future__ import annotations

from typing import Any

from story_analyzer.story_type_classifier import classify_story_core


RANGES = {
    "micro_story": (6, 8),
    "normal_platform_story": (10, 16),
    "complex_classic_adaptation": (12, 24),
    "long_serial_story": (24, 60),
}


def _as_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _source_length(value: Any) -> int:
    if isinstance(value, str):
        lowered = value.lower().strip()
        named = {"short": 1200, "medium": 5000, "long": 18000, "very_long": 45000}
        if lowered in named:
            return named[lowered]
    return _as_int(value)


def _count(value: Any) -> int:
    if value is None:
        return 0
    if isinstance(value, (list, tuple, set, dict)):
        return len(value)
    return _as_int(value, 1 if value else 0)


def estimate_page_count(
    story_type: str = "unknown",
    source_length_estimate: Any = 0,
    event_count: Any = 0,
    twist_count: Any = 0,
    required_payoffs: Any = None,
) -> dict[str, Any]:
    normalized = (story_type or "unknown").lower()
    source_length = _source_length(source_length_estimate)
    events = _as_int(event_count)
    twists = _as_int(twist_count)
    payoffs = _count(required_payoffs)

    reason_codes: list[str] = []
    risk_if_shortened: list[str] = []

    if "classic" in normalized or "adaptation" in normalized:
        range_name = "complex_classic_adaptation"
        reason_codes.append("complex_classic_adaptation_minimum_12")
        risk_if_shortened.append("classic_adaptation_context_and_payoff_loss")
    elif "long" in normalized or source_length >= 30000 or events >= 18:
        range_name = "long_serial_story"
        reason_codes.append("long_serial_story_scope")
        risk_if_shortened.append("serial_arc_will_collapse")
    elif normalized == "micro_horror" or (events <= 2 and twists <= 1 and payoffs <= 1 and source_length <= 2500):
        range_name = "micro_story"
        reason_codes.append("single_anomaly_single_callback_micro_story")
    else:
        range_name = "normal_platform_story"
        reason_codes.append("normal_platform_story_range")

    minimum, maximum = RANGES[range_name]
    if twists >= 1 and payoffs >= 2 and events >= 5:
        minimum = max(minimum, 10)
        maximum = max(maximum, 16)
        reason_codes.append("foreshadow_repeat_final_twist_minimum_10")
        risk_if_shortened.append("foreshadow_payoff_chain_will_be_underbuilt")

    if range_name == "complex_classic_adaptation":
        minimum = max(minimum, 12)
    if range_name == "micro_story":
        recommended = 8 if twists or payoffs else 6
    else:
        recommended = minimum + max(0, events // 3) + twists * 2 + min(payoffs, 4)
    recommended = max(minimum, min(recommended, maximum))

    return {
        "recommended_pages": recommended,
        "minimum_pages": minimum,
        "maximum_pages": maximum,
        "reason_codes": list(dict.fromkeys(reason_codes)),
        "risk_if_shortened": list(dict.fromkeys(risk_if_shortened)),
    }


def estimate_pages_for_story_core(story_core: dict[str, Any]) -> dict[str, Any]:
    story_type = story_core.get("story_type")
    if not isinstance(story_type, str) or not story_type:
        story_type = classify_story_core(story_core)["story_type"]
    story_graph = story_core.get("story_graph")
    nodes = story_graph.get("nodes", []) if isinstance(story_graph, dict) else []
    return estimate_page_count(
        story_type=story_type,
        source_length_estimate=story_core.get("source_length_estimate") or story_core.get("source_length") or 0,
        event_count=story_core.get("event_count") or len(nodes),
        twist_count=story_core.get("twist_count") or _count(story_core.get("twists")),
        required_payoffs=story_core.get("required_payoffs") or story_core.get("payoff_targets"),
    )
