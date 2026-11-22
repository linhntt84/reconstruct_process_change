"""Algorithm 2: Evidence Construction from Qualified Changes."""

from __future__ import annotations

from collections import Counter
from typing import Any, Mapping, Sequence

from .algorithm_1_change_localization_and_qualification import QualifiedChange
from .control_flow_indicators import AnalysisUnit, ControlFlowIndicator, aligned_component_delta


def _json_unit(unit: AnalysisUnit) -> dict[str, Any]:
    if isinstance(unit, tuple):
        return {"values": list(unit)}
    return {"value": unit}


def _characterize(delta: Mapping[Any, float]) -> dict[str, Any]:
    increased = [str(key) for key, value in delta.items() if value > 0]
    decreased = [str(key) for key, value in delta.items() if value < 0]
    if increased and decreased:
        direction = "redistributed"
    elif increased:
        direction = "increased"
    elif decreased:
        direction = "decreased"
    else:
        direction = "unchanged_components"
    return {"direction": direction, "increased_components": increased, "decreased_components": decreased}


def algorithm_2_evidence_construction_from_qualified_changes(
    pre_drift_context: Mapping[str, Mapping[AnalysisUnit, Any]],
    post_drift_context: Mapping[str, Mapping[AnalysisUnit, Any]],
    qualified_changes: Sequence[QualifiedChange],
    indicators: Mapping[str, ControlFlowIndicator],
) -> list[dict[str, Any]]:
    """Construct E* while retaining both score r and empirical strength q."""
    evidence = []
    indicator_indices: Counter[str] = Counter()
    for change in qualified_changes:
        indicator_indices[change.indicator] += 1
        id_prefix = {
            "T_CASE": "TCASE",
            "T_WAIT": "TWAIT",
            "O_ASSIGN": "ASSIGN",
            "O_HAND": "HAND",
        }.get(change.indicator, change.indicator.removeprefix("CF_"))
        evidence_id = f"{id_prefix}{indicator_indices[change.indicator]:03d}"
        indicator = indicators[change.indicator]
        raw_before = pre_drift_context.get(change.indicator, {}).get(change.analysis_unit, {})
        raw_after = post_drift_context.get(change.indicator, {}).get(change.analysis_unit, {})
        before = indicator.explanatory_components(raw_before)
        after = indicator.explanatory_components(raw_after)
        delta = aligned_component_delta(before, after)
        evidence.append({
            "id": evidence_id,
            "indicator": change.indicator,
            "analysis_unit": _json_unit(change.analysis_unit),
            "change_function": indicator.change_function,
            "components_before": {str(key): value for key, value in before.items()},
            "components_after": {str(key): value for key, value in after.items()},
            "component_differences": {str(key): value for key, value in delta.items()},
            "observed_change": change.observed_change,
            "empirical_strength": change.empirical_strength,
            "reference_count": change.reference_count,
            "characterization": _characterize(delta),
        })
    return evidence
