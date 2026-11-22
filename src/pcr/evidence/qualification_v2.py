"""Pipeline v2 qualification: reference construction, tie handling, unit support.

v1 (files kept verbatim) builds the reference set W0 by bootstrap-resampling
*within* each comparison window and counts ties in favour of qualification
(``reference <= observed``). Two consequences on stable (null) pairs:

* a resample of one window can never contain behaviour absent from that window,
  so W0 underestimates sample-to-sample differences for rare units (e.g. a
  source activity with three outgoing transitions whose successors differ
  completely between L- and L+);
* when the change function saturates (cosine 1.0, Wasserstein 1.0), ties at the
  maximum give q = 1 even if every reference also reached the maximum.

This module adds, without changing v1 behaviour:

* ``permutation`` references: pool L- and L+ and re-split them at random into
  windows of the original sizes (a two-sample permutation null);
* rank counts with both ``<`` and ``<=`` so either tie rule can be applied;
* per-unit support counts (how many traces/transitions stand behind a profile).

Empirical strength under the conservative tie rule is
``q = 1 - p`` with the Monte Carlo p-value ``p = (1 + #{ref >= r}) / (B + 1)``,
i.e. ``q = #{ref < r} / (B + 1)``.
"""
from __future__ import annotations

from collections import Counter
from collections.abc import Iterator
from math import isfinite
from typing import Any, Mapping, Sequence

import numpy as np

from .control_flow_indicators import AnalysisUnit, ControlFlowIndicator, Trace, activities
from .reference_windows import Context, build_control_flow_context
from .relational_candidate_gate import directly_follows_trace_support

REFERENCE_MODES = ("bootstrap", "permutation")
TIE_RULES = ("le", "lt")


def strength(n_lt: int, n_le: int, count: int, ties: str) -> float:
    """Empirical strength from rank counts; ``le`` reproduces v1 exactly."""
    if not count:
        return 0.0
    if ties == "le":
        return (1 + n_le) / (count + 1)
    if ties == "lt":
        return n_lt / (count + 1)
    raise ValueError(ties)


def _window_pairs(stable_pre: Sequence[Trace], stable_post: Sequence[Trace], pairs_per_stable_window: int,
                  rng: np.random.Generator, mode: str) -> Iterator[tuple[list[Trace], list[Trace]]]:
    if mode == "bootstrap":
        # Identical RNG consumption to v1 reference_windows / relational_candidate_gate.
        for stable in (stable_pre, stable_post):
            n = len(stable)
            for _ in range(pairs_per_stable_window):
                left = [stable[index] for index in rng.integers(0, n, size=n)]
                right = [stable[index] for index in rng.integers(0, n, size=n)]
                yield left, right
    elif mode == "permutation":
        pooled = list(stable_pre) + list(stable_post)
        cut = len(stable_pre)
        for _ in range(2 * pairs_per_stable_window):
            order = rng.permutation(len(pooled))
            yield [pooled[i] for i in order[:cut]], [pooled[i] for i in order[cut:]]
    else:
        raise ValueError(mode)


def reference_context_pairs(stable_pre, stable_post, indicators, universes, pairs_per_stable_window: int,
                            random_seed: int, mode: str = "bootstrap") -> Iterator[tuple[Context, Context]]:
    rng = np.random.default_rng(random_seed)
    for left, right in _window_pairs(stable_pre, stable_post, pairs_per_stable_window, rng, mode):
        yield (build_control_flow_context(left, indicators, universes),
               build_control_flow_context(right, indicators, universes))


def localization_rank_counts(stable_pre, stable_post, pairs_per_stable_window: int, random_seed: int,
                             minimum_support_change: float, mode: str = "bootstrap") -> list[dict[str, Any]]:
    """Stage 1 (DFG trace-support change) with rank counts instead of a fixed tau."""
    before = directly_follows_trace_support(stable_pre)
    after = directly_follows_trace_support(stable_post)
    candidates = [(edge, abs(after.get(edge, 0.0) - before.get(edge, 0.0)))
                  for edge in sorted(set(before) | set(after))]
    candidates = [(edge, d) for edge, d in candidates if d >= minimum_support_change]
    edges = [edge for edge, _ in candidates]
    n_lt, n_le = [0] * len(candidates), [0] * len(candidates)
    count = 0
    rng = np.random.default_rng(random_seed)
    for left, right in _window_pairs(stable_pre, stable_post, pairs_per_stable_window, rng, mode):
        count += 1
        ls = directly_follows_trace_support(left, edges)
        rs = directly_follows_trace_support(right, edges)
        for index, (edge, observed) in enumerate(candidates):
            reference = abs(rs[edge] - ls[edge])
            n_lt[index] += reference < observed
            n_le[index] += reference <= observed
    return [{"s": edge[0], "t": edge[1], "d": d, "lt": n_lt[i], "le": n_le[i], "n": count}
            for i, (edge, d) in enumerate(candidates)]


def qualification_rank_counts(pre_context, post_context, indicators: Mapping[str, ControlFlowIndicator],
                              reference_pairs) -> list[dict[str, Any]]:
    """Algorithm 1 with zero thresholds, returning rank counts for every r > 0 candidate."""
    candidates = []
    for code, indicator in indicators.items():
        before, after = pre_context.get(code, {}), post_context.get(code, {})
        for unit in sorted(set(before) | set(after), key=str):
            observed = indicator.change_magnitude(before.get(unit, {}), after.get(unit, {}))
            if isfinite(observed) and observed > 0.0:
                candidates.append((code, unit, observed))
    n_lt, n_le, counts = [0] * len(candidates), [0] * len(candidates), [0] * len(candidates)
    for ref_before, ref_after in reference_pairs:
        for index, (code, unit, observed) in enumerate(candidates):
            reference = indicators[code].change_magnitude(ref_before.get(code, {}).get(unit, {}),
                                                          ref_after.get(code, {}).get(unit, {}))
            if isfinite(reference):
                counts[index] += 1
                n_lt[index] += reference < observed
                n_le[index] += reference <= observed
    return [{"j": code, "u": unit, "r": observed, "lt": n_lt[i], "le": n_le[i], "n": counts[i]}
            for i, (code, unit, observed) in enumerate(candidates) if counts[i]]


def unit_support(code: str, unit: AnalysisUnit, traces: Sequence[Trace], max_lag: int = 5) -> int:
    """Number of observations behind a unit's profile in one window.

    OCC, POS: traces containing the activity. DIR: outgoing directly-follows
    transitions of the source. REL: traces containing at least one of the two
    activities. LAG: traces in which the ordered pair occurs within max_lag.
    """
    sequences = [activities(trace) for trace in traces]
    if code in ("CF_OCC", "CF_POS"):
        return sum(str(unit) in s for s in sequences)
    if code == "CF_DIR":
        return sum(a == str(unit) for s in sequences for a in s[:-1])
    a, b = (str(v) for v in unit)
    if code == "CF_REL":
        return sum(a in s or b in s for s in sequences)
    if code == "CF_LAG":
        return sum(any(x == a and y == b for lag in range(1, max_lag + 1) for x, y in zip(s, s[lag:]))
                   for s in sequences)
    raise ValueError(code)


def support_table(units: Sequence[tuple[str, AnalysisUnit]], traces: Sequence[Trace]) -> dict:
    """Support for many units at once (activity-level counts are shared)."""
    sequences = [activities(trace) for trace in traces]
    trace_has: Counter[str] = Counter()
    dir_out: Counter[str] = Counter()
    for s in sequences:
        trace_has.update(set(s))
        dir_out.update(s[:-1])
    output = {}
    for code, unit in units:
        if code in ("CF_OCC", "CF_POS"):
            output[(code, unit)] = trace_has[str(unit)]
        elif code == "CF_DIR":
            output[(code, unit)] = dir_out[str(unit)]
        else:
            output[(code, unit)] = unit_support(code, unit, traces)
    return output
