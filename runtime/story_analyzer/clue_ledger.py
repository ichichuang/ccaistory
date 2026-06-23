from __future__ import annotations

from typing import Any


INTRO_KEYS = ("introduced_clues", "clue_introductions", "setup_clues", "planted_clues")
REPEAT_KEYS = ("repeated_clues", "clue_repeats", "echoed_clues")
PAYOFF_KEYS = ("paid_off_clues", "payoff_clues", "clue_payoffs", "payoffs")


def _nodes_from_graph(story_graph: dict[str, Any]) -> list[dict[str, Any]]:
    if isinstance(story_graph.get("nodes"), list):
        return [node for node in story_graph["nodes"] if isinstance(node, dict)]
    nested = story_graph.get("story_graph")
    if isinstance(nested, dict) and isinstance(nested.get("nodes"), list):
        return [node for node in nested["nodes"] if isinstance(node, dict)]
    return []


def _edges_from_graph(story_graph: dict[str, Any]) -> list[dict[str, Any]]:
    if isinstance(story_graph.get("edges"), list):
        return [edge for edge in story_graph["edges"] if isinstance(edge, dict)]
    nested = story_graph.get("story_graph")
    if isinstance(nested, dict) and isinstance(nested.get("edges"), list):
        return [edge for edge in nested["edges"] if isinstance(edge, dict)]
    return []


def _node_id(node: dict[str, Any]) -> str:
    return str(node.get("node_id") or node.get("id") or node.get("page_id") or node.get("page_index") or "")


def _clue_id(item: Any) -> str:
    if isinstance(item, dict):
        value = item.get("clue_id") or item.get("id") or item.get("name") or item.get("target")
        return str(value or "").strip()
    return str(item or "").strip()


def _stage(item: Any, default: str) -> str:
    if not isinstance(item, dict):
        return default
    raw = str(item.get("status") or item.get("stage") or item.get("role") or item.get("type") or default).lower()
    if any(token in raw for token in ("payoff", "paid", "resolve", "callback", "回扣", "应验")):
        return "payoff"
    if any(token in raw for token in ("repeat", "echo", "recur", "再次", "重复")):
        return "repeat"
    return "introduction"


def _entries(value: Any, default_stage: str) -> list[tuple[str, str, Any]]:
    if value is None:
        return []
    raw_items = value if isinstance(value, list) else [value]
    entries: list[tuple[str, str, Any]] = []
    for item in raw_items:
        clue_id = _clue_id(item)
        if clue_id:
            entries.append((clue_id, _stage(item, default_stage), item))
    return entries


def _has_escalation(item: Any, node: dict[str, Any]) -> bool:
    if isinstance(item, dict):
        for key in ("escalation", "information_gain", "threat_delta", "new_information"):
            value = item.get(key)
            if value not in (None, "", False, 0):
                return True
    for key in ("information_gain", "threat_delta", "escalation_delta"):
        value = node.get(key)
        if value not in (None, "", False, 0):
            return True
    return False


def _empty_record(clue_id: str) -> dict[str, Any]:
    return {
        "clue_id": clue_id,
        "introduced_at": "",
        "repeated_at": [],
        "paid_off_at": "",
        "_repeat_without_escalation": [],
    }


def analyze_clue_ledger(story_graph: dict[str, Any]) -> dict[str, Any]:
    records: dict[str, dict[str, Any]] = {}
    for node in _nodes_from_graph(story_graph):
        node_id = _node_id(node)
        collected: list[tuple[str, str, Any]] = []
        for key in INTRO_KEYS:
            collected.extend(_entries(node.get(key), "introduction"))
        for key in REPEAT_KEYS:
            collected.extend(_entries(node.get(key), "repeat"))
        for key in PAYOFF_KEYS:
            collected.extend(_entries(node.get(key), "payoff"))
        collected.extend(_entries(node.get("clues"), "introduction"))
        if node.get("payoff_target"):
            collected.extend(_entries(node.get("payoff_target"), "payoff"))

        for clue_id, stage, item in collected:
            record = records.setdefault(clue_id, _empty_record(clue_id))
            if stage == "payoff":
                record["paid_off_at"] = record["paid_off_at"] or node_id
            elif stage == "repeat":
                if node_id not in record["repeated_at"]:
                    record["repeated_at"].append(node_id)
                if not _has_escalation(item, node):
                    record["_repeat_without_escalation"].append(node_id)
            else:
                record["introduced_at"] = record["introduced_at"] or node_id

    for edge in _edges_from_graph(story_graph):
        clue_id = _clue_id(edge)
        if not clue_id:
            continue
        stage = _stage(edge, "repeat")
        node_id = str(edge.get("to") or edge.get("target") or "")
        record = records.setdefault(clue_id, _empty_record(clue_id))
        if stage == "payoff":
            record["paid_off_at"] = record["paid_off_at"] or node_id
        elif stage == "repeat":
            if node_id and node_id not in record["repeated_at"]:
                record["repeated_at"].append(node_id)
            if not _has_escalation(edge, {}):
                record["_repeat_without_escalation"].append(node_id)
        else:
            record["introduced_at"] = record["introduced_at"] or str(edge.get("from") or edge.get("source") or "")

    failures: list[str] = []
    repairs: list[dict[str, Any]] = []
    clues: list[dict[str, Any]] = []
    for clue_id in sorted(records):
        record = records[clue_id]
        introduced = bool(record["introduced_at"])
        paid = bool(record["paid_off_at"])
        repeated = bool(record["repeated_at"])
        if paid and not introduced:
            status = "orphan"
            failures.append(f"orphan_clue:{clue_id}")
            repairs.append({"clue_id": clue_id, "repair_action": "plant_clue_before_payoff"})
        elif introduced and not paid:
            status = "unpaid"
            failures.append(f"unpaid_clue:{clue_id}")
            repairs.append({"clue_id": clue_id, "repair_action": "add_payoff_or_remove_clue"})
        elif paid:
            status = "paid_off"
        elif repeated:
            status = "repeated"
        else:
            status = "introduced"
        if record["_repeat_without_escalation"]:
            failures.append(f"repeated_without_escalation:{clue_id}")
            repairs.append({"clue_id": clue_id, "repair_action": "add_new_information_to_repeat"})
        clues.append(
            {
                "clue_id": clue_id,
                "introduced_at": record["introduced_at"],
                "repeated_at": record["repeated_at"],
                "paid_off_at": record["paid_off_at"],
                "status": status,
            }
        )

    return {
        "clues": clues,
        "failures": list(dict.fromkeys(failures)),
        "recommended_repairs": repairs,
    }
