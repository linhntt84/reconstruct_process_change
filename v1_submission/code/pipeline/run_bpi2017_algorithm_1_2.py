#!/usr/bin/env python3
"""Construct Algorithm 1--2 control-flow and temporal evidence for BPI 2017."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
EXPERIMENT = HERE.parent
WORKSPACE = EXPERIMENT.parents[1]
ACIIDS_CODE = WORKSPACE / "Experiments/ACIIDS_2027/Code"
if str(ACIIDS_CODE) not in sys.path:
    sys.path.insert(0, str(ACIIDS_CODE))

from detect_bpi2017_control_flow_change_points import load_complete_traces  # noqa: E402
from control_flow_evidence import (  # noqa: E402
    algorithm_1_change_localization_and_qualification,
    algorithm_2_evidence_construction_from_qualified_changes,
)
from control_flow_evidence.control_flow_indicators import CONTROL_FLOW_INDICATORS  # noqa: E402
from control_flow_evidence.reference_windows import (  # noqa: E402
    bootstrap_reference_context_pairs,
    build_control_flow_context,
    common_analysis_universes,
)
from control_flow_evidence.relational_candidate_gate import (  # noqa: E402
    qualify_relational_candidate_activities_from_directly_follows,
)
from control_flow_evidence.temporal_indicators import (  # noqa: E402
    TEMPORAL_INDICATORS,
    eligible_wait_units,
)
from control_flow_evidence.organizational_indicators import (  # noqa: E402
    ORGANIZATIONAL_INDICATORS,
    eligible_organizational_units,
)


INDICATORS = {
    **CONTROL_FLOW_INDICATORS,
    **TEMPORAL_INDICATORS,
    **ORGANIZATIONAL_INDICATORS,
}


DEFAULT_LOG = WORKSPACE / "Data/BPI2017/BPI Challenge 2017.csv"
DEFAULT_CANDIDATES = EXPERIMENT / "artifacts/official/bpi2017_control_flow_detection_v1/candidate_change_points.csv"
DEFAULT_OUTPUT = EXPERIMENT / "artifacts/official/bpi2017_b200_tau_0p99_algorithm_1_2_v1"


def write_json(path: Path, value: object) -> int:
    text = json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return len(text)


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def public_case_id(boundary: int, timestamp: str) -> str:
    digest = hashlib.sha256(f"BPI2017:{boundary}:{timestamp}".encode()).hexdigest()[:16]
    return f"case_{digest}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--log", type=Path, default=DEFAULT_LOG)
    parser.add_argument("--candidates", type=Path, default=DEFAULT_CANDIDATES)
    parser.add_argument("--window-size", type=int, default=200)
    parser.add_argument("--tau", type=float, default=0.99)
    parser.add_argument("--reference-pairs-per-state", type=int, default=100)
    parser.add_argument("--seed", type=int, default=20260913)
    parser.add_argument("--rel-gate-tau", type=float, default=0.99)
    parser.add_argument("--rel-gate-minimum-edge-change", type=float, default=0.10)
    parser.add_argument("--rel-minimum-component-change", type=float, default=0.10)
    parser.add_argument("--minimum-dir-source-transitions", type=int, default=10)
    parser.add_argument("--minimum-wait-observations-per-window", type=int, default=10)
    parser.add_argument("--minimum-wait-change-hours", type=float, default=0.10)
    parser.add_argument("--minimum-organizational-observations-per-window", type=int, default=50)
    parser.add_argument("--minimum-organizational-change", type=float, default=0.10)
    parser.add_argument("--boundary-source-label", default="detected control-flow candidates")
    parser.add_argument(
        "--boundary-semantics", default="detected candidate boundaries; not ground truth",
    )
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    traces = load_complete_traces(args.log)
    raw_resources = sorted(
        {resource for trace in traces for resource in trace["complete_resources"]},
        key=lambda value: [int(part) if part.isdigit() else part for part in re.split(r"(\d+)", value)],
    )
    resource_aliases = {resource: f"R{index:03d}" for index, resource in enumerate(raw_resources, 1)}
    write_json(args.output / "private_resource_aliases.json", resource_aliases)
    with args.candidates.open(encoding="utf-8-sig", newline="") as handle:
        candidates = sorted(csv.DictReader(handle), key=lambda row: int(row["boundary_case_index"]))
    if not candidates:
        raise SystemExit("No candidate boundaries")

    minimum_changes = {code: 0.0 for code in INDICATORS}
    minimum_changes["CF_REL"] = args.rel_minimum_component_change
    minimum_changes["T_WAIT"] = args.minimum_wait_change_hours
    minimum_changes["O_ASSIGN"] = args.minimum_organizational_change
    minimum_changes["O_HAND"] = args.minimum_organizational_change
    summary: list[dict[str, Any]] = []
    private_rows: list[dict[str, Any]] = []
    temporal_rows: list[dict[str, Any]] = []
    organizational_rows: list[dict[str, Any]] = []

    for candidate_index, candidate in enumerate(candidates):
        boundary = int(candidate["boundary_case_index"])
        before_raw = traces[boundary - args.window_size:boundary]
        after_raw = traces[boundary:boundary + args.window_size]
        if len(before_raw) != args.window_size or len(after_raw) != args.window_size:
            raise SystemExit(f"Incomplete windows at boundary {boundary}")
        before = [{
            "activities": trace["activities"],
            "complete_timestamps": trace["complete_timestamps"],
            "start_time": trace["start_time"],
            "end_time": trace["end_time"],
            "complete_resources": [resource_aliases[value] for value in trace["complete_resources"]],
        } for trace in before_raw]
        after = [{
            "activities": trace["activities"],
            "complete_timestamps": trace["complete_timestamps"],
            "start_time": trace["start_time"],
            "end_time": trace["end_time"],
            "complete_resources": [resource_aliases[value] for value in trace["complete_resources"]],
        } for trace in after_raw]

        non_relational = {
            code: indicator for code, indicator in CONTROL_FLOW_INDICATORS.items()
            if code != "CF_REL"
        }
        preliminary_before = build_control_flow_context(before, non_relational)
        preliminary_after = build_control_flow_context(after, non_relational)
        universes = common_analysis_universes(preliminary_before, preliminary_after)
        def outgoing_transition_counts(window: list[dict[str, Any]]) -> Counter[str]:
            result: Counter[str] = Counter()
            for trace in window:
                result.update(trace["activities"][:-1])
            return result

        before_outgoing = outgoing_transition_counts(before)
        after_outgoing = outgoing_transition_counts(after)
        dir_candidates_before_gate = len(universes["CF_DIR"])
        universes["CF_DIR"] = [
            activity for activity in universes["CF_DIR"]
            if max(before_outgoing[activity], after_outgoing[activity])
            >= args.minimum_dir_source_transitions
        ]
        gate = qualify_relational_candidate_activities_from_directly_follows(
            before, after, args.reference_pairs_per_state, args.seed + candidate_index,
            tau=args.rel_gate_tau,
            minimum_support_change=args.rel_gate_minimum_edge_change,
        )
        affected = gate.activities
        affected_set = set(affected)
        universes["CF_REL"] = list(combinations(affected, 2))
        pos_before_gate = len(universes["CF_POS"])
        universes["CF_POS"] = [activity for activity in universes["CF_POS"] if activity in affected_set]
        lag_before_gate = len(universes["CF_LAG"])
        universes["CF_LAG"] = [
            unit for unit in universes["CF_LAG"]
            if unit[0] in affected_set and unit[1] in affected_set
        ]

        universes["T_CASE"] = ["case_duration"]
        universes["T_WAIT"] = eligible_wait_units(
            before, after, args.minimum_wait_observations_per_window,
        )
        organizational_units = eligible_organizational_units(
            before, after, args.minimum_organizational_observations_per_window,
        )
        universes.update(organizational_units)

        before_context = build_control_flow_context(before, INDICATORS, universes)
        after_context = build_control_flow_context(after, INDICATORS, universes)
        references = bootstrap_reference_context_pairs(
            before, after, INDICATORS, universes,
            args.reference_pairs_per_state, args.seed + candidate_index,
        )
        calibrated = algorithm_1_change_localization_and_qualification(
            before_context, after_context, INDICATORS, references,
            {code: args.tau for code in INDICATORS},
            minimum_observed_change=minimum_changes,
        )
        qualified = [change for change in calibrated if change.empirical_strength >= args.tau]
        evidence = algorithm_2_evidence_construction_from_qualified_changes(
            before_context, after_context, qualified, INDICATORS,
        )
        counts = Counter(item["indicator"] for item in evidence)
        case_id = public_case_id(boundary, candidate["first_after_start_time"])
        for item in evidence:
            if item["indicator"] not in TEMPORAL_INDICATORS:
                continue
            unit = item["analysis_unit"].get("values", item["analysis_unit"].get("value"))
            if isinstance(unit, list):
                unit = " -> ".join(map(str, unit))
            temporal_rows.append({
                "case_id": case_id,
                "boundary_case_index": boundary,
                "week_label": candidate.get("week_label", ""),
                "evidence_id": item["id"],
                "indicator": item["indicator"],
                "analysis_unit": unit,
                "wasserstein_hours": item["observed_change"],
                "empirical_strength": item["empirical_strength"],
                "before_count": item["components_before"].get("count", ""),
                "after_count": item["components_after"].get("count", ""),
                "before_mean_hours": item["components_before"].get("mean_hours", ""),
                "after_mean_hours": item["components_after"].get("mean_hours", ""),
                "before_median_hours": item["components_before"].get("median_hours", ""),
                "after_median_hours": item["components_after"].get("median_hours", ""),
            })
        for item in evidence:
            if item["indicator"] not in ORGANIZATIONAL_INDICATORS:
                continue
            unit = item["analysis_unit"].get("values", item["analysis_unit"].get("value"))
            if isinstance(unit, list):
                unit = " -> ".join(map(str, unit))
            organizational_rows.append({
                "case_id": case_id,
                "boundary_case_index": boundary,
                "week_label": candidate.get("week_label", ""),
                "evidence_id": item["id"],
                "indicator": item["indicator"],
                "analysis_unit": unit,
                "cosine_dissimilarity": item["observed_change"],
                "empirical_strength": item["empirical_strength"],
                "components_before_json": json.dumps(
                    item["components_before"], ensure_ascii=False, sort_keys=True,
                ),
                "components_after_json": json.dumps(
                    item["components_after"], ensure_ascii=False, sort_keys=True,
                ),
            })
        payload = {
            "schema_version": "ieee-access-algorithm-1-2-evidence-1.1",
            "case": {"case_id": case_id, "dataset": "BPI Challenge 2017"},
            "algorithm_1": {
                "tau": args.tau,
                "reference_pairs": 2 * args.reference_pairs_per_state,
                "candidate_units": sum(map(len, universes.values())),
                "qualification": "q_j_u >= tau",
                "finite_sample_correction": True,
                "minimum_observed_change_by_indicator": minimum_changes,
            },
            "algorithm_2": {
                "evidence_count": len(evidence),
                "evidence_id_format": "OCC/DIR/POS/REL/LAG/TCASE/TWAIT/ASSIGN/HAND + within-indicator index",
            },
            "relational_candidate_gate": {
                "method": "qualified_dir_edges",
                "support_delta_threshold": args.rel_gate_minimum_edge_change,
                "tau": args.rel_gate_tau,
                "tested_edge_count": gate.tested_edge_count,
                "qualified_edge_count": len(gate.qualified_edges),
                "selected_activities": affected,
                "candidate_pair_count": len(universes["CF_REL"]),
            },
            "directly_follows_candidate_gate": {
                "minimum_source_transitions_in_either_window": args.minimum_dir_source_transitions,
                "candidate_source_activities_before_gate": dir_candidates_before_gate,
                "candidate_source_activities": len(universes["CF_DIR"]),
                "reason": "avoid unstable conditional profiles from rare source activities",
            },
            "lag_candidate_gate": {
                "method": "both_endpoints_in_qualified_dir_activities",
                "candidate_pair_count_before_gate": lag_before_gate,
                "candidate_pair_count": len(universes["CF_LAG"]),
            },
            "position_candidate_gate": {
                "method": "qualified_dir_activities",
                "candidate_activity_count_before_gate": pos_before_gate,
                "candidate_activity_count": len(universes["CF_POS"]),
            },
            "temporal_candidate_gate": {
                "T_CASE_units": 1,
                "T_WAIT_minimum_observations_per_window": args.minimum_wait_observations_per_window,
                "T_WAIT_minimum_wasserstein_hours": args.minimum_wait_change_hours,
                "T_WAIT_candidate_pairs": len(universes["T_WAIT"]),
                "T_WAIT_measurement": "hours between consecutive complete events",
            },
            "organizational_candidate_gate": {
                "minimum_observations_per_window": args.minimum_organizational_observations_per_window,
                "O_ASSIGN_candidate_activities": len(universes["O_ASSIGN"]),
                "O_HAND_candidate_activity_pairs": len(universes["O_HAND"]),
                "O_HAND_self_handovers_excluded": True,
                "resource_identifiers": "stable pseudonyms R001, R002, ...",
                "minimum_cosine_dissimilarity": args.minimum_organizational_change,
                "explanatory_components": "top 10 probabilities plus OTHER; qualification uses full profile",
            },
            "indicator_change_functions": {
                code: indicator.change_function for code, indicator in INDICATORS.items()
            },
            "evidence": evidence,
        }
        tau_tag = f"{args.tau:.2f}".replace(".", "p")
        characters = write_json(args.output / "evidence" / f"tau_{tau_tag}" / f"{case_id}.json", payload)
        summary.append({
            "case_id": case_id,
            "tau": args.tau,
            "reference_pairs": 2 * args.reference_pairs_per_state,
            "candidate_units": sum(map(len, universes.values())),
            "evidence_items": len(evidence),
            **{f"n_{code}": counts[code] for code in INDICATORS},
            "serialized_characters": characters,
            "estimated_tokens": math.ceil(characters / 4),
        })
        private_rows.append({
            "case_id": case_id,
            **candidate,
            "last_before_case_id": before_raw[-1]["case_id"],
            "first_after_case_id_verified": after_raw[0]["case_id"],
        })
        print(f"[{candidate_index + 1}/{len(candidates)}] {case_id}: {len(evidence)} items", flush=True)

    write_csv(args.output / "evidence_item_summary.csv", summary)
    write_csv(args.output / "private_candidate_coordinates.csv", private_rows)
    if temporal_rows:
        write_csv(args.output / "temporal_evidence_summary.csv", temporal_rows)
    if organizational_rows:
        write_csv(args.output / "organizational_evidence_summary.csv", organizational_rows)
    write_json(args.output / "run_metadata.json", {
        "dataset": "BPI Challenge 2017",
        "source": str(args.log.resolve()),
        "candidate_source": str(args.candidates.resolve()),
        "candidate_count": len(candidates),
        "boundary_source_label": args.boundary_source_label,
        "boundary_semantics": args.boundary_semantics,
        "event_filter": "lifecycle:transition == complete",
        "window_size_cases_per_side": args.window_size,
        "tau": args.tau,
        "reference_pairs_per_stable_state": args.reference_pairs_per_state,
        "total_reference_pairs": 2 * args.reference_pairs_per_state,
        "random_seed": args.seed,
        "activity_labels": "original BPI 2017 labels retained",
        "minimum_change_by_indicator": minimum_changes,
        "rel_gate_tau": args.rel_gate_tau,
        "rel_gate_minimum_edge_change": args.rel_gate_minimum_edge_change,
        "directly_follows_gate": {
            "minimum_source_transitions_in_either_window": args.minimum_dir_source_transitions,
            "semantics": "retain appearance/disappearance when one window has sufficient support",
        },
        "pos_gate": "activities incident to qualified DIR edges",
        "rel_gate": "pairs among activities incident to qualified DIR edges",
        "lag_gate": "both endpoints incident to qualified DIR edges",
        "temporal_indicators": {
            "T_CASE": "end-to-end duration from first to last event, in hours",
            "T_WAIT": "time between consecutive complete events for an ordered directly-follows pair, in hours",
            "T_WAIT_minimum_observations_per_window": args.minimum_wait_observations_per_window,
            "T_WAIT_minimum_wasserstein_hours": args.minimum_wait_change_hours,
        },
        "organizational_indicators": {
            "O_ASSIGN": "per-activity resource-assignment probability distribution",
            "O_HAND": "resource-to-resource handover probability distribution per directly-follows activity pair",
            "minimum_observations_per_window": args.minimum_organizational_observations_per_window,
            "self_handovers_excluded": True,
            "resource_identifiers": "stable pseudonyms; private mapping stored separately",
            "minimum_cosine_dissimilarity": args.minimum_organizational_change,
            "explanatory_components": "top 10 probabilities plus OTHER; qualification uses full profile",
        },
        "indicator_change_functions": {
            code: indicator.change_function for code, indicator in INDICATORS.items()
        },
    })
    print(f"Wrote {args.output / 'evidence_item_summary.csv'}")


if __name__ == "__main__":
    main()
