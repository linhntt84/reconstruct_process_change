"""Pseudo-window construction for the reference set W0 used by Algorithm 1."""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any, Mapping, Sequence

import numpy as np

from .control_flow_indicators import AnalysisUnit, ControlFlowIndicator, Trace


Context = dict[str, dict[AnalysisUnit, Any]]


def build_control_flow_context(
    traces: Sequence[Trace],
    indicators: Mapping[str, ControlFlowIndicator],
    universes: Mapping[str, Sequence[AnalysisUnit]] | None = None,
) -> Context:
    return {
        code: indicator.build_context(traces, None if universes is None else universes.get(code))
        for code, indicator in indicators.items()
    }


def common_analysis_universes(pre_context: Context, post_context: Context) -> dict[str, list[AnalysisUnit]]:
    return {
        code: sorted(set(pre_context.get(code, {})) | set(post_context.get(code, {})), key=str)
        for code in set(pre_context) | set(post_context)
    }


def bootstrap_reference_context_pairs(
    stable_pre: Sequence[Trace],
    stable_post: Sequence[Trace],
    indicators: Mapping[str, ControlFlowIndicator],
    universes: Mapping[str, Sequence[AnalysisUnit]],
    pairs_per_stable_window: int,
    random_seed: int,
) -> Iterator[tuple[Context, Context]]:
    """Create W0 without ever mixing traces across the true change boundary."""
    if not stable_pre or not stable_post:
        raise ValueError("Both stable windows must be non-empty")
    rng = np.random.default_rng(random_seed)
    for stable in (stable_pre, stable_post):
        n = len(stable)
        for _ in range(pairs_per_stable_window):
            left = [stable[index] for index in rng.integers(0, n, size=n)]
            right = [stable[index] for index in rng.integers(0, n, size=n)]
            yield (
                build_control_flow_context(left, indicators, universes),
                build_control_flow_context(right, indicators, universes),
            )
