"""Temporal indicators from Table 2 for timestamped event-log traces."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from math import sqrt
from typing import Any, Hashable, Iterable, Mapping, Sequence

from .control_flow_indicators import AnalysisUnit, Trace, activities, wasserstein_1d


def _hours(delta: Any) -> float:
    return max(0.0, float(delta.total_seconds()) / 3600.0)


def _summary(values: Sequence[float]) -> dict[Hashable, float]:
    ordered = sorted(map(float, values))
    if not ordered:
        return {"count": 0.0, "mean_hours": 0.0, "std_hours": 0.0,
                "q25_hours": 0.0, "median_hours": 0.0, "q75_hours": 0.0}
    mean = sum(ordered) / len(ordered)
    quantile = lambda p: ordered[round(p * (len(ordered) - 1))]
    std = sqrt(sum((value - mean) ** 2 for value in ordered) / len(ordered))
    return {"count": float(len(ordered)), "mean_hours": mean, "std_hours": std,
            "q25_hours": quantile(.25), "median_hours": quantile(.5),
            "q75_hours": quantile(.75)}


@dataclass(frozen=True)
class TemporalIndicator:
    code: str
    name: str
    unit_kind: str
    change_function: str = "wasserstein_1d_hours"

    def build_context(
        self, traces: Sequence[Trace], universe: Iterable[AnalysisUnit] | None = None,
    ) -> dict[AnalysisUnit, Any]:
        if self.code == "T_CASE":
            values = [
                _hours(trace["end_time"] - trace["start_time"])
                for trace in traces
            ]
            return {"case_duration": {"values_hours": values}}
        waits: defaultdict[tuple[str, str], list[float]] = defaultdict(list)
        for trace in traces:
            sequence = activities(trace)
            timestamps = trace["complete_timestamps"]
            for left, right, left_time, right_time in zip(
                sequence, sequence[1:], timestamps, timestamps[1:]
            ):
                waits[(left, right)].append(_hours(right_time - left_time))
        units = list(universe) if universe is not None else sorted(waits, key=str)
        return {tuple(unit): {"values_hours": waits.get(tuple(unit), [])} for unit in units}

    def change_magnitude(self, before: Any, after: Any) -> float:
        return wasserstein_1d(before.get("values_hours", []), after.get("values_hours", []))

    def explanatory_components(self, representation: Any) -> dict[Hashable, float]:
        return _summary(representation.get("values_hours", []))


TEMPORAL_INDICATORS: dict[str, TemporalIndicator] = {
    "T_CASE": TemporalIndicator("T_CASE", "Case throughput time", "global_case_duration"),
    "T_WAIT": TemporalIndicator("T_WAIT", "Inter-completion waiting time", "directly_follows_pair"),
}


def eligible_wait_units(
    before: Sequence[Trace], after: Sequence[Trace], minimum_observations: int,
) -> list[tuple[str, str]]:
    def counts(traces: Sequence[Trace]) -> dict[tuple[str, str], int]:
        result: defaultdict[tuple[str, str], int] = defaultdict(int)
        for trace in traces:
            sequence = activities(trace)
            for pair in zip(sequence, sequence[1:]):
                result[pair] += 1
        return result

    left, right = counts(before), counts(after)
    return sorted(
        (unit for unit in set(left) | set(right)
         if left.get(unit, 0) >= minimum_observations
         and right.get(unit, 0) >= minimum_observations),
        key=str,
    )
