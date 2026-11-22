"""Control-flow indicator representations and change functions from Table 2.

The implementation deliberately separates the scalar qualification score from
the signed component changes later exposed as explanatory evidence.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import combinations
from math import nan, sqrt
from typing import Any, Hashable, Iterable, Mapping, Sequence


Trace = Mapping[str, Any]
AnalysisUnit = Hashable


def activities(trace: Trace) -> list[str]:
    return [str(value) for value in trace["activities"]]


def _round(value: float) -> float:
    result = round(float(value), 10)
    return 0.0 if result == -0.0 else result


def cosine_dissimilarity(left: Mapping[Hashable, float], right: Mapping[Hashable, float]) -> float:
    """Cosine dissimilarity after zero-aligning two non-negative profiles."""
    keys = set(left) | set(right)
    dot = sum(float(left.get(key, 0.0)) * float(right.get(key, 0.0)) for key in keys)
    left_norm = sqrt(sum(float(left.get(key, 0.0)) ** 2 for key in keys))
    right_norm = sqrt(sum(float(right.get(key, 0.0)) ** 2 for key in keys))
    if left_norm == 0.0 and right_norm == 0.0:
        return 0.0
    if left_norm == 0.0 or right_norm == 0.0:
        return 1.0
    result = min(1.0, max(0.0, 1.0 - dot / (left_norm * right_norm)))
    return 0.0 if result < 1e-12 else result


def wasserstein_1d(left: Sequence[float], right: Sequence[float]) -> float:
    """Exact first Wasserstein distance between two empirical 1-D samples."""
    if not left and not right:
        return 0.0
    if not left or not right:
        # Absence is maximally different on the normalized [0, 1] domain.
        return 1.0
    xs, ys = sorted(map(float, left)), sorted(map(float, right))
    points = sorted(set(xs) | set(ys))
    if len(points) < 2:
        return 0.0
    i = j = 0
    distance = 0.0
    for lo, hi in zip(points, points[1:]):
        while i < len(xs) and xs[i] <= lo:
            i += 1
        while j < len(ys) and ys[j] <= lo:
            j += 1
        distance += abs(i / len(xs) - j / len(ys)) * (hi - lo)
    return distance


def aligned_component_delta(
    before: Mapping[Hashable, float], after: Mapping[Hashable, float]
) -> dict[Hashable, float]:
    return {
        key: _round(float(after.get(key, 0.0)) - float(before.get(key, 0.0)))
        for key in sorted(set(before) | set(after), key=str)
    }


def normalized_l1(left: Mapping[Hashable, float], right: Mapping[Hashable, float]) -> float:
    """Mean absolute component difference for bounded support profiles."""
    keys = set(left) | set(right)
    if not keys:
        return 0.0
    return sum(abs(float(right.get(key, 0.0)) - float(left.get(key, 0.0))) for key in keys) / len(keys)


def total_variation(left: Mapping[Hashable, float], right: Mapping[Hashable, float]) -> float:
    """Total variation between aligned categorical probability profiles."""
    keys = set(left) | set(right)
    return 0.5 * sum(
        abs(float(right.get(key, 0.0)) - float(left.get(key, 0.0)))
        for key in keys
    )


def normalized_discrete_wasserstein(
    left: Mapping[Hashable, float], right: Mapping[Hashable, float]
) -> float:
    """Wasserstein-1 on ordered conditional profiles, normalized to [0, 1]."""
    if not left or not right:
        return nan
    keys = sorted(set(left) | set(right), key=lambda value: int(value))
    if len(keys) < 2:
        return 0.0
    left_total = sum(float(left.get(key, 0.0)) for key in keys)
    right_total = sum(float(right.get(key, 0.0)) for key in keys)
    if left_total <= 0.0 or right_total <= 0.0:
        return nan
    left_cdf = right_cdf = distance = 0.0
    for key in keys[:-1]:
        left_cdf += float(left.get(key, 0.0)) / left_total
        right_cdf += float(right.get(key, 0.0)) / right_total
        distance += abs(left_cdf - right_cdf)
    return distance / (len(keys) - 1)


@dataclass(frozen=True)
class ControlFlowIndicator:
    code: str
    name: str
    unit_kind: str
    change_function: str

    def build_context(self, traces: Sequence[Trace], universe: Iterable[AnalysisUnit] | None = None) -> dict[AnalysisUnit, Any]:
        builders = {
            "CF_OCC": _occurrence_context,
            "CF_DIR": _directly_follows_context,
            "CF_POS": _position_context,
            "CF_REL": _relational_context,
            "CF_LAG": _lag_context,
        }
        return builders[self.code](traces, universe)

    def change_magnitude(self, before: Any, after: Any) -> float:
        if self.code == "CF_OCC":
            return abs(float(after.get("mean_occurrences_per_trace", 0.0)) - float(before.get("mean_occurrences_per_trace", 0.0)))
        if self.code == "CF_POS":
            return wasserstein_1d(before.get("relative_positions", []), after.get("relative_positions", []))
        if self.code == "CF_LAG":
            return normalized_discrete_wasserstein(before, after)
        if self.code == "CF_REL":
            keys = set(before) | set(after)
            return max((abs(float(after.get(key, 0.0)) - float(before.get(key, 0.0))) for key in keys), default=0.0)
        return cosine_dissimilarity(before, after)

    def explanatory_components(self, representation: Any) -> dict[Hashable, float]:
        if self.code == "CF_POS":
            values = list(map(float, representation.get("relative_positions", [])))
            if not values:
                return {"support": 0.0, "mean": 0.0, "std": 0.0, "q25": 0.0, "median": 0.0, "q75": 0.0}
            ordered = sorted(values)
            quantile = lambda p: ordered[round(p * (len(ordered) - 1))]
            mean = sum(values) / len(values)
            std = sqrt(sum((value - mean) ** 2 for value in values) / len(values))
            return {"support": float(representation.get("trace_support", 0.0)), "mean": mean, "std": std,
                    "q25": quantile(.25), "median": quantile(.5), "q75": quantile(.75)}
        return {key: float(value) for key, value in representation.items()}


CONTROL_FLOW_INDICATORS: dict[str, ControlFlowIndicator] = {
    "CF_OCC": ControlFlowIndicator("CF_OCC", "Activity occurrence", "activity", "absolute_difference"),
    "CF_DIR": ControlFlowIndicator("CF_DIR", "Directly-follows profile", "source_activity", "cosine_dissimilarity"),
    "CF_POS": ControlFlowIndicator("CF_POS", "Activity position", "activity", "wasserstein_1d"),
    "CF_REL": ControlFlowIndicator("CF_REL", "ACIIDS pairwise behavioral profile", "unordered_activity_pair", "max_component_absolute_difference"),
    "CF_LAG": ControlFlowIndicator("CF_LAG", "Conditional lag distribution", "ordered_activity_pair", "normalized_wasserstein_1d"),
}


def _labels(traces: Sequence[Trace]) -> list[str]:
    return sorted({label for trace in traces for label in activities(trace)})


def _occurrence_context(traces: Sequence[Trace], universe: Iterable[AnalysisUnit] | None) -> dict[AnalysisUnit, Any]:
    labels = list(universe) if universe is not None else _labels(traces)
    n = len(traces)
    output = {}
    for label in labels:
        counts = [activities(trace).count(str(label)) for trace in traces]
        output[label] = {
            "mean_occurrences_per_trace": sum(counts) / n if n else 0.0,
            "trace_participation": sum(value > 0 for value in counts) / n if n else 0.0,
            "recurrence_support": sum(value > 1 for value in counts) / n if n else 0.0,
        }
    return output


def _directly_follows_context(traces: Sequence[Trace], universe: Iterable[AnalysisUnit] | None) -> dict[AnalysisUnit, Any]:
    labels = list(universe) if universe is not None else _labels(traces)
    counts: Counter[tuple[str, str]] = Counter()
    for trace in traces:
        counts.update(zip(activities(trace), activities(trace)[1:]))
    output = {}
    for source in labels:
        row = {target: float(count) for (candidate, target), count in counts.items() if candidate == source}
        total = sum(row.values())
        output[source] = {target: value / total for target, value in row.items()} if total else {}
    return output


def _position_context(traces: Sequence[Trace], universe: Iterable[AnalysisUnit] | None) -> dict[AnalysisUnit, Any]:
    labels = list(universe) if universe is not None else _labels(traces)
    positions: dict[str, list[float]] = {str(label): [] for label in labels}
    support = Counter()
    for trace in traces:
        sequence = activities(trace)
        denominator = max(len(sequence) - 1, 1)
        for index, label in enumerate(sequence):
            if label in positions:
                positions[label].append(index / denominator)
        support.update(set(sequence))
    n = len(traces)
    return {label: {"relative_positions": values, "trace_support": support[label] / n if n else 0.0}
            for label, values in positions.items()}


RELATION_COMPONENTS = (
    "cooccurrence", "A_only", "B_only", "neither",
    "A_before_B", "B_before_A", "interleaved_or_repeated",
)


def _relation_state(sequence: list[str], a: str, b: str) -> str:
    pa = [index for index, value in enumerate(sequence) if value == a]
    pb = [index for index, value in enumerate(sequence) if value == b]
    if pa and pb:
        if len(pa) > 1 or len(pb) > 1:
            return "interleaved_or_repeated"
        return "A_before_B" if pa[0] < pb[0] else "B_before_A"
    if pa:
        return "A_only"
    if pb:
        return "B_only"
    return "neither"


def _relational_context(traces: Sequence[Trace], universe: Iterable[AnalysisUnit] | None) -> dict[AnalysisUnit, Any]:
    pairs = list(universe) if universe is not None else list(combinations(_labels(traces), 2))
    output = {}
    sequences = [activities(trace) for trace in traces]
    for raw_a, raw_b in pairs:
        a, b = str(raw_a), str(raw_b)
        counts = Counter(_relation_state(sequence, a, b) for sequence in sequences)
        counts["cooccurrence"] = sum(a in sequence and b in sequence for sequence in sequences)
        denominator = len(sequences)
        output[(a, b)] = {
            component: counts[component] / denominator if denominator else 0.0
            for component in RELATION_COMPONENTS
        }
    return output


def aciids_affected_activities(
    before: Sequence[Trace], after: Sequence[Trace], support_delta_threshold: float = 0.10
) -> list[str]:
    """Rank ACIIDS R candidates by their strongest incident support change."""
    def supports(traces: Sequence[Trace]) -> tuple[dict[str, float], dict[tuple[str, str], float]]:
        activity_counts: Counter[str] = Counter()
        edge_counts: Counter[tuple[str, str]] = Counter()
        for trace in traces:
            sequence = activities(trace)
            activity_counts.update(set(sequence))
            edge_counts.update(set(zip(sequence, sequence[1:])))
        n = len(traces)
        return (
            {key: value / n for key, value in activity_counts.items()} if n else {},
            {key: value / n for key, value in edge_counts.items()} if n else {},
        )

    before_a, before_e = supports(before)
    after_a, after_e = supports(after)
    scores = {
        activity: abs(after_a.get(activity, 0.0) - before_a.get(activity, 0.0))
        for activity in set(before_a) | set(after_a)
    }
    for source, target in set(before_e) | set(after_e):
        delta = abs(after_e.get((source, target), 0.0) - before_e.get((source, target), 0.0))
        scores[source] = max(scores.get(source, 0.0), delta)
        scores[target] = max(scores.get(target, 0.0), delta)
    return sorted(
        (activity for activity, score in scores.items() if score >= support_delta_threshold),
        key=lambda activity: (-scores[activity], activity),
    )


def _lag_context(traces: Sequence[Trace], universe: Iterable[AnalysisUnit] | None, max_lag: int = 5) -> dict[AnalysisUnit, Any]:
    if universe is None:
        units = sorted({(a, b) for trace in traces for lag in range(1, max_lag + 1)
                        for a, b in zip(activities(trace), activities(trace)[lag:])})
    else:
        units = list(universe)
    unit_set = {(str(source), str(target)) for source, target in units}
    profile_sums: Counter[tuple[str, str, int]] = Counter()
    eligible_traces: Counter[tuple[str, str]] = Counter()
    for trace in traces:
        sequence = activities(trace)
        trace_counts: Counter[tuple[str, str, int]] = Counter(
            (a, b, lag)
            for lag in range(1, max_lag + 1)
            for a, b in zip(sequence, sequence[lag:])
            if (a, b) in unit_set
        )
        pair_totals: Counter[tuple[str, str]] = Counter()
        for (source, target, _), count in trace_counts.items():
            pair_totals[(source, target)] += count
        eligible_traces.update(pair_totals)
        for (source, target, lag), count in trace_counts.items():
            profile_sums[(source, target, lag)] += count / pair_totals[(source, target)]
    output = {}
    for source, target in units:
        pair = (str(source), str(target))
        denominator = eligible_traces[pair]
        output[pair] = (
            {str(lag): profile_sums[(pair[0], pair[1], lag)] / denominator for lag in range(1, max_lag + 1)}
            if denominator else {}
        )
    return output
