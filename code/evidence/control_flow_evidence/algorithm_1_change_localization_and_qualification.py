"""Algorithm 1: Change Localization and Qualification."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from math import isfinite
from typing import Any, Iterable, Mapping, Sequence

from .control_flow_indicators import AnalysisUnit, ControlFlowIndicator


@dataclass(frozen=True)
class QualifiedChange:
    indicator: str
    analysis_unit: AnalysisUnit
    observed_change: float
    empirical_strength: float
    reference_count: int

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def empirical_strength(observed_change: float, reference_changes: Sequence[float]) -> float:
    """Equation 14, including its finite-sample +1 correction and ties."""
    return (1 + sum(float(reference) <= float(observed_change) for reference in reference_changes)) / (len(reference_changes) + 1)


def algorithm_1_change_localization_and_qualification(
    pre_drift_context: Mapping[str, Mapping[AnalysisUnit, Any]],
    post_drift_context: Mapping[str, Mapping[AnalysisUnit, Any]],
    indicators: Mapping[str, ControlFlowIndicator],
    reference_context_pairs: Iterable[tuple[Mapping[str, Mapping[AnalysisUnit, Any]], Mapping[str, Mapping[AnalysisUnit, Any]]]],
    tau: float | Mapping[str, float],
    minimum_observed_change: float | Mapping[str, float] | None = 0.0,
) -> list[QualifiedChange]:
    """Executable Algorithm 1 with an explicit degenerate-zero guard.

    With the manuscript's non-strict empirical CDF, ``r=0`` receives ``q=1``
    whenever every null score is also zero.  The default therefore requires
    ``r > 0``.  Pass ``None`` to reproduce the pseudocode literally.
    """
    if isinstance(tau, Mapping):
        missing = set(indicators) - set(tau)
        if missing:
            raise ValueError(f"Missing indicator thresholds: {sorted(missing)}")
        thresholds = {code: float(tau[code]) for code in indicators}
    else:
        thresholds = {code: float(tau) for code in indicators}
    if any(not 0.0 <= value <= 1.0 for value in thresholds.values()):
        raise ValueError("Every tau must lie in [0, 1]")
    if isinstance(minimum_observed_change, Mapping):
        missing = set(indicators) - set(minimum_observed_change)
        if missing:
            raise ValueError(f"Missing indicator materiality thresholds: {sorted(missing)}")
        materiality = {code: float(minimum_observed_change[code]) for code in indicators}
    elif minimum_observed_change is None:
        materiality = None
    else:
        materiality = {code: float(minimum_observed_change) for code in indicators}
    candidates: list[tuple[str, AnalysisUnit, float]] = []
    for code, indicator in indicators.items():
        before = pre_drift_context.get(code, {})
        after = post_drift_context.get(code, {})
        units = sorted(set(before) | set(after), key=str)
        for unit in units:
            left = before.get(unit, {})
            right = after.get(unit, {})
            observed = indicator.change_magnitude(left, right)
            if not isfinite(observed):
                continue
            if materiality is not None and observed < materiality[code]:
                continue
            # The zero guard remains strict even when the configured threshold
            # is zero; r=0 with an all-zero null otherwise receives q=1.
            if materiality is not None and materiality[code] == 0.0 and observed == 0.0:
                continue
            candidates.append((code, unit, observed))

    # Consume W0 once and retain only rank counters. Memory is O(number of
    # candidates), not O(B * number of candidates).
    less_or_equal = [0] * len(candidates)
    reference_counts = [0] * len(candidates)
    for ref_before, ref_after in reference_context_pairs:
        for index, (code, unit, observed) in enumerate(candidates):
            reference_change = indicators[code].change_magnitude(
                ref_before.get(code, {}).get(unit, {}),
                ref_after.get(code, {}).get(unit, {}),
            )
            if isfinite(reference_change):
                reference_counts[index] += 1
                if reference_change <= observed:
                    less_or_equal[index] += 1

    qualified: list[QualifiedChange] = []
    for index, (code, unit, observed) in enumerate(candidates):
        count = reference_counts[index]
        if not count:
            continue
        strength = (1 + less_or_equal[index]) / (count + 1)
        if strength >= thresholds[code]:
            qualified.append(QualifiedChange(code, unit, observed, strength, count))
    return qualified
