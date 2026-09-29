"""Candidate-universe gate for CF_REL based on qualified DFG-edge changes."""

from __future__ import annotations

from collections import Counter
from dataclasses import asdict, dataclass
from typing import Any, Sequence

import numpy as np

from .control_flow_indicators import Trace, activities


Edge = tuple[str, str]


def directly_follows_trace_support(
    traces: Sequence[Trace], universe: Sequence[Edge] | None = None,
) -> dict[Edge, float]:
    """Proportion of traces containing each directly-follows edge at least once."""
    counts: Counter[Edge] = Counter()
    allowed = set(universe) if universe is not None else None
    for trace in traces:
        observed = set(zip(activities(trace), activities(trace)[1:]))
        counts.update(observed if allowed is None else observed & allowed)
    denominator = len(traces)
    keys = set(counts) if universe is None else set(universe)
    return {edge: counts[edge] / denominator if denominator else 0.0 for edge in keys}


@dataclass(frozen=True)
class RelationalCandidateGateResult:
    activities: list[str]
    qualified_edges: list[dict[str, Any]]
    tested_edge_count: int

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def qualify_relational_candidate_activities_from_directly_follows(
    stable_pre: Sequence[Trace],
    stable_post: Sequence[Trace],
    pairs_per_stable_window: int,
    random_seed: int,
    tau: float = 0.99,
    minimum_support_change: float = 0.10,
) -> RelationalCandidateGateResult:
    """Apply Algorithm 1's empirical qualification to DFG trace-support deltas."""
    before = directly_follows_trace_support(stable_pre)
    after = directly_follows_trace_support(stable_post)
    all_edges = sorted(set(before) | set(after))
    candidates = [
        (edge, abs(after.get(edge, 0.0) - before.get(edge, 0.0)))
        for edge in all_edges
        if abs(after.get(edge, 0.0) - before.get(edge, 0.0)) >= minimum_support_change
    ]
    candidate_edges = [edge for edge, _ in candidates]
    less_or_equal = [0] * len(candidates)
    reference_count = 2 * pairs_per_stable_window
    rng = np.random.default_rng(random_seed)
    for stable in (stable_pre, stable_post):
        n = len(stable)
        for _ in range(pairs_per_stable_window):
            left = [stable[index] for index in rng.integers(0, n, size=n)]
            right = [stable[index] for index in rng.integers(0, n, size=n)]
            left_support = directly_follows_trace_support(left, candidate_edges)
            right_support = directly_follows_trace_support(right, candidate_edges)
            for index, (edge, observed) in enumerate(candidates):
                reference = abs(right_support[edge] - left_support[edge])
                if reference <= observed:
                    less_or_equal[index] += 1

    qualified = []
    for index, (edge, observed) in enumerate(candidates):
        strength = (1 + less_or_equal[index]) / (reference_count + 1)
        if strength >= tau:
            qualified.append({
                "source": edge[0], "target": edge[1],
                "before": before.get(edge, 0.0), "after": after.get(edge, 0.0),
                "absolute_change": observed, "empirical_strength": strength,
            })
    qualified.sort(key=lambda item: (-item["absolute_change"], item["source"], item["target"]))
    selected_activities = sorted({
        activity for edge in qualified for activity in (edge["source"], edge["target"])
    })
    return RelationalCandidateGateResult(selected_activities, qualified, len(all_edges))
