"""Organizational indicators from Table 2 for resource-aware traces."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Any, Hashable, Iterable, Mapping, Sequence

from .control_flow_indicators import AnalysisUnit, Trace, activities, cosine_dissimilarity


def _normalize(counts: Counter[str]) -> dict[str, float]:
    total = sum(counts.values())
    return {key: value / total for key, value in counts.items()} if total else {}


@dataclass(frozen=True)
class OrganizationalIndicator:
    code: str
    name: str
    unit_kind: str
    change_function: str = "cosine_dissimilarity"

    def build_context(
        self, traces: Sequence[Trace], universe: Iterable[AnalysisUnit] | None = None,
    ) -> dict[AnalysisUnit, Any]:
        if self.code == "O_ASSIGN":
            counts: dict[str, Counter[str]] = {}
            for trace in traces:
                for activity, resource in zip(activities(trace), trace["complete_resources"]):
                    counts.setdefault(activity, Counter())[str(resource)] += 1
            units = list(universe) if universe is not None else sorted(counts)
            return {str(unit): _normalize(counts.get(str(unit), Counter())) for unit in units}

        counts_by_pair: dict[tuple[str, str], Counter[str]] = {}
        for trace in traces:
            sequence = activities(trace)
            resources = [str(value) for value in trace["complete_resources"]]
            for left_a, right_a, left_r, right_r in zip(
                sequence, sequence[1:], resources, resources[1:]
            ):
                if left_r == right_r:
                    continue
                unit = (left_a, right_a)
                counts_by_pair.setdefault(unit, Counter())[f"{left_r}->{right_r}"] += 1
        units = list(universe) if universe is not None else sorted(counts_by_pair, key=str)
        return {tuple(unit): _normalize(counts_by_pair.get(tuple(unit), Counter())) for unit in units}

    def change_magnitude(self, before: Any, after: Any) -> float:
        return cosine_dissimilarity(before, after)

    def explanatory_components(self, representation: Any) -> dict[Hashable, float]:
        ranked = sorted(
            ((str(key), float(value)) for key, value in representation.items()),
            key=lambda item: (-item[1], item[0]),
        )
        retained = dict(ranked[:10])
        remainder = sum(value for _, value in ranked[10:])
        if remainder > 0.0:
            retained["OTHER"] = remainder
        return retained


ORGANIZATIONAL_INDICATORS: dict[str, OrganizationalIndicator] = {
    "O_ASSIGN": OrganizationalIndicator(
        "O_ASSIGN", "Activity-resource assignment", "activity",
    ),
    "O_HAND": OrganizationalIndicator(
        "O_HAND", "Resource handover", "directly_follows_activity_pair",
    ),
}


def eligible_organizational_units(
    before: Sequence[Trace], after: Sequence[Trace], minimum_observations: int,
) -> dict[str, list[AnalysisUnit]]:
    def counts(traces: Sequence[Trace]) -> tuple[Counter[str], Counter[tuple[str, str]]]:
        assignments: Counter[str] = Counter()
        handovers: Counter[tuple[str, str]] = Counter()
        for trace in traces:
            sequence = activities(trace)
            resources = [str(value) for value in trace["complete_resources"]]
            assignments.update(sequence)
            handovers.update(
                (left_a, right_a)
                for left_a, right_a, left_r, right_r in zip(
                    sequence, sequence[1:], resources, resources[1:]
                )
                if left_r != right_r
            )
        return assignments, handovers

    before_assign, before_hand = counts(before)
    after_assign, after_hand = counts(after)
    return {
        "O_ASSIGN": sorted(
            unit for unit in set(before_assign) | set(after_assign)
            if before_assign.get(unit, 0) >= minimum_observations
            and after_assign.get(unit, 0) >= minimum_observations
        ),
        "O_HAND": sorted(
            (unit for unit in set(before_hand) | set(after_hand)
             if before_hand.get(unit, 0) >= minimum_observations
             and after_hand.get(unit, 0) >= minimum_observations),
            key=str,
        ),
    }
