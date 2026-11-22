#!/usr/bin/env python3
"""Dataset-independent evidence features for the controlled ACIIDS experiment."""

from __future__ import annotations

from collections import Counter
from dataclasses import asdict, dataclass
from itertools import combinations
from math import sqrt
from typing import Any


@dataclass(frozen=True)
class EvidenceConfig:
    top_activity_changes: int = 5
    top_dfg_changes: int = 10
    max_affected_activities: int = 10
    max_pair_relations: int = 6
    max_position_profiles: int = 5
    max_lag: int = 5
    max_lag_relations: int = 6
    stable_window_size: int = 200

    def to_dict(self) -> dict[str, int]:
        return asdict(self)


def change(before: float | None, after: float | None) -> dict[str, Any]:
    """Return consistent change semantics; undefined comparisons remain null."""
    if before is None or after is None:
        return {"delta": None, "relative_delta": None, "direction": "undefined"}
    delta = after - before
    if before == after:
        direction = "unchanged"
    elif before == 0 and after > 0:
        direction = "appeared"
    elif before > 0 and after == 0:
        direction = "disappeared"
    else:
        direction = "increase" if delta > 0 else "decrease"
    return {
        "delta": round(delta, 6),
        "relative_delta": None if before == 0 else round(delta / abs(before), 6),
        "direction": direction,
    }


def _activities(trace: dict[str, Any]) -> list[str]:
    return [str(value) for value in trace["activities"]]


def neutralize_windows(
    before: list[dict[str, Any]], after: list[dict[str, Any]], enabled: bool = True
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, str]]:
    labels = sorted({activity for trace in before + after for activity in _activities(trace)})
    mapping = {label: f"A{index:02d}" for index, label in enumerate(labels, 1)}
    if not enabled:
        mapping = {label: label for label in labels}

    def convert(traces: list[dict[str, Any]]) -> list[dict[str, Any]]:
        return [{"activities": [mapping[a] for a in _activities(trace)]} for trace in traces]

    return convert(before), convert(after), mapping


def _trace_supports(traces: list[dict[str, Any]]) -> tuple[dict[str, float], dict[tuple[str, str], float]]:
    n = len(traces)
    activity_counts: Counter[str] = Counter()
    edge_counts: Counter[tuple[str, str]] = Counter()
    for trace in traces:
        sequence = _activities(trace)
        activity_counts.update(set(sequence))
        edge_counts.update(set(zip(sequence, sequence[1:])))
    activities = {key: value / n for key, value in activity_counts.items()} if n else {}
    edges = {key: value / n for key, value in edge_counts.items()} if n else {}
    return activities, edges


def _numeric_item(measure: str, entity: dict[str, Any], before: float, after: float, unit: str) -> dict[str, Any]:
    return {
        "measure": measure,
        "entity": entity,
        "before": round(before, 6),
        "after": round(after, 6),
        **change(before, after),
        "unit": unit,
    }


def activity_and_dfg_candidates(
    before: list[dict[str, Any]], after: list[dict[str, Any]]
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    before_a, before_e = _trace_supports(before)
    after_a, after_e = _trace_supports(after)
    activities = [
        _numeric_item("activity_trace_support", {"activity": a}, before_a.get(a, 0.0), after_a.get(a, 0.0), "proportion_of_traces")
        for a in sorted(set(before_a) | set(after_a))
    ]
    edges = [
        _numeric_item(
            "dfg_trace_support",
            {"source": source, "target": target},
            before_e.get((source, target), 0.0),
            after_e.get((source, target), 0.0),
            "proportion_of_traces",
        )
        for source, target in sorted(set(before_e) | set(after_e))
    ]
    return activities, edges


def _rank_numeric(items: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    return sorted(
        items,
        key=lambda x: (-abs(float(x["delta"])), x["measure"], tuple(sorted(x["entity"].items()))),
    )[:limit]


def select_core_evidence(
    activities: list[dict[str, Any]], edges: list[dict[str, Any]], config: EvidenceConfig
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[str]]:
    selected_a = _rank_numeric(activities, config.top_activity_changes)
    selected_e = _rank_numeric(edges, config.top_dfg_changes)
    candidates = {item["entity"]["activity"] for item in selected_a}
    for item in selected_e:
        candidates.update((item["entity"]["source"], item["entity"]["target"]))
    scores: dict[str, float] = {activity: 0.0 for activity in candidates}
    for item in activities:
        activity = item["entity"]["activity"]
        if activity in scores:
            scores[activity] = max(scores[activity], abs(float(item["delta"])))
    for item in edges:
        for activity in (item["entity"]["source"], item["entity"]["target"]):
            if activity in scores:
                scores[activity] = max(scores[activity], abs(float(item["delta"])))
    affected = sorted(candidates, key=lambda a: (-scores[a], a))[: config.max_affected_activities]
    return selected_a, selected_e, affected


PAIR_STATES = ("cooccurrence", "A_only", "B_only", "neither", "A_before_B", "B_before_A", "interleaved_or_repeated")


def _pair_snapshot(traces: list[dict[str, Any]], a: str, b: str) -> dict[str, float]:
    counts = Counter({state: 0 for state in PAIR_STATES})
    for trace in traces:
        seq = _activities(trace)
        pa = [i for i, value in enumerate(seq) if value == a]
        pb = [i for i, value in enumerate(seq) if value == b]
        if pa and pb:
            counts["cooccurrence"] += 1
            if len(pa) > 1 or len(pb) > 1:
                counts["interleaved_or_repeated"] += 1
            elif max(pa) < min(pb):
                counts["A_before_B"] += 1
            elif max(pb) < min(pa):
                counts["B_before_A"] += 1
            else:
                counts["interleaved_or_repeated"] += 1
        elif pa:
            counts["A_only"] += 1
        elif pb:
            counts["B_only"] += 1
        else:
            counts["neither"] += 1
    n = len(traces)
    return {state: round(counts[state] / n, 6) if n else 0.0 for state in PAIR_STATES}


def pair_relation_candidates(
    before: list[dict[str, Any]], after: list[dict[str, Any]], affected: list[str], limit: int
) -> list[dict[str, Any]]:
    items = []
    for a, b in combinations(sorted(affected), 2):
        before_values, after_values = _pair_snapshot(before, a, b), _pair_snapshot(after, a, b)
        changes = {state: round(after_values[state] - before_values[state], 6) for state in PAIR_STATES}
        score = max(abs(float(value)) for value in changes.values())
        items.append({
            "measure": "pairwise_behavior_profile",
            "entity": {"activity_A": a, "activity_B": b},
            "before": before_values,
            "after": after_values,
            "changes": changes,
            "unit": "proportion_of_traces",
            "_rank": score,
        })
    items.sort(key=lambda x: (-x["_rank"], x["entity"]["activity_A"], x["entity"]["activity_B"]))
    for item in items:
        item.pop("_rank")
    return items[:limit]


POSITION_FIELDS = ("mean_occurrences", "first_relative_position", "last_relative_position", "mean_relative_position", "position_std")


def _position_snapshot(traces: list[dict[str, Any]], activity: str) -> dict[str, float | None]:
    present = 0
    occurrence_counts: list[int] = []
    firsts: list[float] = []
    lasts: list[float] = []
    positions: list[float] = []
    for trace in traces:
        seq = _activities(trace)
        denominator = max(len(seq) - 1, 1)
        found = [i / denominator for i, value in enumerate(seq) if value == activity]
        occurrence_counts.append(len(found))
        if found:
            present += 1
            firsts.append(found[0]); lasts.append(found[-1]); positions.extend(found)
    n = len(traces)
    mean = sum(positions) / len(positions) if positions else None
    std = sqrt(sum((x - mean) ** 2 for x in positions) / len(positions)) if positions else None
    rounded = lambda x: None if x is None else round(x, 6)
    return {
        "trace_support": round(present / n, 6) if n else 0.0,
        "mean_occurrences": round(sum(occurrence_counts) / n, 6) if n else 0.0,
        "first_relative_position": rounded(sum(firsts) / len(firsts) if firsts else None),
        "last_relative_position": rounded(sum(lasts) / len(lasts) if lasts else None),
        "mean_relative_position": rounded(mean),
        "position_std": rounded(std),
    }


def position_profiles(
    before: list[dict[str, Any]], after: list[dict[str, Any]], affected: list[str], limit: int
) -> list[dict[str, Any]]:
    output = []
    for activity in affected:
        before_values = _position_snapshot(before, activity)
        after_values = _position_snapshot(after, activity)
        before_public = {field: before_values[field] for field in POSITION_FIELDS}
        after_public = {field: after_values[field] for field in POSITION_FIELDS}
        deltas = {
            field: None if before_values[field] is None or after_values[field] is None
            else round(float(after_values[field]) - float(before_values[field]), 6)
            for field in POSITION_FIELDS
        }
        comparable = [abs(float(value)) for value in deltas.values() if value is not None]
        appeared_or_disappeared = any(
            (before_values[field] is None) != (after_values[field] is None)
            for field in POSITION_FIELDS if field != "mean_occurrences"
        )
        output.append({
            "measure": "activity_relative_position_profile",
            "entity": {"activity": activity},
            "before": before_public,
            "after": after_public,
            "delta": deltas,
            "unit": "relative_event_position",
            "_rank": 1.0 if appeared_or_disappeared else max(comparable, default=0.0),
        })
    output.sort(key=lambda x: (-x["_rank"], x["entity"]["activity"]))
    for item in output:
        item.pop("_rank")
    return output[:limit]


def lagged_relation_candidates(
    before: list[dict[str, Any]], after: list[dict[str, Any]], affected: list[str], max_lag: int, limit: int
) -> list[dict[str, Any]]:
    affected_set = set(affected)

    def supports(traces: list[dict[str, Any]]) -> dict[tuple[str, str, int], float]:
        counts: Counter[tuple[str, str, int]] = Counter()
        for trace in traces:
            seq = _activities(trace)
            observed = set()
            for lag in range(1, max_lag + 1):
                observed.update((a, b, lag) for a, b in zip(seq, seq[lag:]) if a in affected_set or b in affected_set)
            counts.update(observed)
        n = len(traces)
        return {key: value / n for key, value in counts.items()} if n else {}

    before_s, after_s = supports(before), supports(after)
    items = [
        _numeric_item(
            "exact_lag_trace_support",
            {"source": source, "target": target, "event_lag": lag},
            before_s.get((source, target, lag), 0.0),
            after_s.get((source, target, lag), 0.0),
            "proportion_of_traces",
        )
        for source, target, lag in sorted(set(before_s) | set(after_s))
    ]
    return _rank_numeric(items, limit)


def assign_opaque_ids(families: dict[str, list[dict[str, Any]]]) -> None:
    counter = 1
    for family in ("activity", "dfg", "relational", "position", "lagged"):
        for item in families[family]:
            item["evidence_id"] = f"E{counter:03d}"
            counter += 1


def build_candidate_evidence(
    before: list[dict[str, Any]], after: list[dict[str, Any]], config: EvidenceConfig
) -> tuple[dict[str, list[dict[str, Any]]], dict[str, Any]]:
    all_activities, all_edges = activity_and_dfg_candidates(before, after)
    activities, edges, affected = select_core_evidence(all_activities, all_edges, config)
    families = {
        "activity": activities,
        "dfg": edges,
        "relational": pair_relation_candidates(before, after, affected, config.max_pair_relations),
        "position": position_profiles(before, after, affected, config.max_position_profiles),
        "lagged": lagged_relation_candidates(before, after, affected, config.max_lag, config.max_lag_relations),
    }
    assign_opaque_ids(families)
    empirical_reference = {"activity_changes": all_activities, "dfg_changes": all_edges}
    return families, {"affected_activities": affected, "empirical_change_reference": empirical_reference}
