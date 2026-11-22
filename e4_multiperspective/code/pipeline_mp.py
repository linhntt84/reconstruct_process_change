"""Multi-perspective extension of pipeline v2, developed inside the E4 folder.

The control-flow part is exactly `pcr.pipeline.build_evidence` (not modified, called as is).
Temporal evidence (T_WAIT) is appended with the same qualification machinery:
permutation references (B = 2 * pairs_per_stable_window), q = #{ref < r} / (B + 1), the shared
tau; units are directly-follows pairs (A, B) with at least `min_obs` observations in each window;
r is the Wasserstein distance between the inter-completion times (hours) of the pair.
T_WAIT is not gated by the localized region A* (a pure time change leaves the DFG unchanged).
`eps_time` is a scale-free minimum effect: r / median of the pooled times of the unit.

    from pipeline_mp import build_evidence_mp
    doc = build_evidence_mp(before_events, after_events, config, seed, case_id,
                            time_params={"min_obs": 10, "eps_time": 0.0})

before_events / after_events: lists of traces, each a list of (activity, ISO timestamp).
"""
from __future__ import annotations

import hashlib
import math
import statistics
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Sequence

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "src"))
from pcr.evidence.algorithm_1_change_localization_and_qualification import QualifiedChange  # noqa: E402
from pcr.evidence.algorithm_2_evidence_construction_from_qualified_changes import (  # noqa: E402
    algorithm_2_evidence_construction_from_qualified_changes)
from pcr.evidence.qualification_v2 import (  # noqa: E402
    qualification_rank_counts, reference_context_pairs, strength)
from pcr.evidence.organizational_indicators import (  # noqa: E402
    ORGANIZATIONAL_INDICATORS, eligible_organizational_units)
from pcr.evidence.temporal_indicators import TEMPORAL_INDICATORS, eligible_wait_units  # noqa: E402
from pcr.pipeline import build_evidence  # noqa: E402

TWAIT = {"T_WAIT": TEMPORAL_INDICATORS["T_WAIT"]}


class ConcentrationIndicator:
    """O_CONC (E4 extension): change in how concentrated an activity is on few resources.
    Representation = resource distribution of the activity (as O_ASSIGN);
    r = |HHI(after) - HHI(before)|, HHI = sum of squared shares (Herfindahl-Hirschman index)."""
    code, name, unit_kind = "O_CONC", "Resource concentration", "activity"
    change_function = "concentration_index_difference"

    def build_context(self, traces, universe=None):
        return ORGANIZATIONAL_INDICATORS["O_ASSIGN"].build_context(traces, universe)

    @staticmethod
    def hhi(distribution) -> float:
        return float(sum(v * v for v in distribution.values()))

    def change_magnitude(self, before, after) -> float:
        return abs(self.hhi(after) - self.hhi(before))

    def explanatory_components(self, distribution):
        return {"concentration_index": round(self.hhi(distribution), 4),
                "top_resource_share": round(max(distribution.values(), default=0.0), 4),
                "distinct_resources": len(distribution)}


ORG = {k: ORGANIZATIONAL_INDICATORS[k] for k in ("O_ASSIGN", "O_HAND")}
ORG["O_CONC"] = ConcentrationIndicator()


def eligible_org_units(pre, post, min_obs: int) -> dict:
    """v1 eligibility; O_CONC uses the O_ASSIGN units (activities with >= min_obs events in each window)."""
    units = eligible_organizational_units(pre, post, min_obs)
    units["O_CONC"] = list(units["O_ASSIGN"])
    return units


def to_traces(events: Sequence[Sequence[Sequence[str]]]) -> list[dict[str, Any]]:
    """Events are (activity, ISO timestamp) or (activity, ISO timestamp, resource)."""
    traces = []
    for trace in events:
        t = {"activities": [e[0] for e in trace],
             "complete_timestamps": [datetime.fromisoformat(e[1]) for e in trace]}
        if trace and len(trace[0]) > 2:
            t["complete_resources"] = [e[2] for e in trace]
        traces.append(t)
    return traces


def org_seed(seed: int) -> int:
    return int(hashlib.sha256(f"ORG::{seed}".encode()).hexdigest()[:8], 16)


def org_candidates(pre: list[dict], post: list[dict], config: dict, seed: int, min_obs: int,
                   pairs_per_window: int) -> list[dict]:
    """O_ASSIGN (unit = activity) and O_HAND (unit = directly-follows pair with a handover):
    cosine dissimilarity of resource / handover profiles, permutation references."""
    ref = dict(config["reference"])
    ref["pairs_per_stable_window"] = pairs_per_window
    universes = {k: list(v) for k, v in eligible_org_units(pre, post, min_obs).items() if k in ORG}
    if not any(universes.values()):
        return []
    before_ctx = {k: ORG[k].build_context(pre, universes.get(k, [])) for k in ORG}
    after_ctx = {k: ORG[k].build_context(post, universes.get(k, [])) for k in ORG}
    refs = reference_context_pairs(pre, post, ORG, universes, ref["pairs_per_stable_window"], org_seed(seed), ref["mode"])
    candidates = qualification_rank_counts(before_ctx, after_ctx, ORG, refs)
    for c in candidates:
        c["q"] = strength(c["lt"], c["le"], c["n"], ref["ties"])
    return [{**c, "_ctx_before": before_ctx, "_ctx_after": after_ctx} for c in candidates]


def time_seed(seed: int) -> int:
    return int(hashlib.sha256(f"T_WAIT::{seed}".encode()).hexdigest()[:8], 16)


def twait_candidates(pre: list[dict], post: list[dict], config: dict, seed: int, min_obs: int,
                     pairs_per_window: int | None = None) -> list[dict]:
    """Every T_WAIT unit with r > 0: rank counts, q, effect size and observation counts.
    pairs_per_window overrides the reference size for T_WAIT (B = 2 * pairs_per_window)."""
    ref = dict(config["reference"])
    if pairs_per_window:
        ref["pairs_per_stable_window"] = pairs_per_window
    units = eligible_wait_units(pre, post, min_obs)
    if not units:
        return []
    universes = {"T_WAIT": units}
    before_ctx = {"T_WAIT": TWAIT["T_WAIT"].build_context(pre, units)}
    after_ctx = {"T_WAIT": TWAIT["T_WAIT"].build_context(post, units)}
    refs = reference_context_pairs(pre, post, TWAIT, universes, ref["pairs_per_stable_window"],
                                   time_seed(seed), ref["mode"])
    candidates = qualification_rank_counts(before_ctx, after_ctx, TWAIT, refs)
    for c in candidates:
        values_b = before_ctx["T_WAIT"][c["u"]]["values_hours"]
        values_a = after_ctx["T_WAIT"][c["u"]]["values_hours"]
        pooled = statistics.median(values_b + values_a) if (values_b or values_a) else 0.0
        c["q"] = strength(c["lt"], c["le"], c["n"], ref["ties"])
        c["effect"] = c["r"] / pooled if pooled > 0 else math.inf
        c["obs_before"], c["obs_after"] = len(values_b), len(values_a)
    return [{**c, "_ctx_before": before_ctx, "_ctx_after": after_ctx} for c in candidates]


def _org_support(traces: list[dict], code: str, units: list[str]) -> int:
    """ASSIGN/CONC: events of the activity; HAND: directly-follows occurrences of the pair with a handover."""
    if code in ("O_ASSIGN", "O_CONC"):
        return sum(a == units[0] for t in traces for a in t["activities"])
    a, b = units
    return sum(1 for t in traces for (x, y, rx, ry) in zip(t["activities"], t["activities"][1:],
                                                           t["complete_resources"], t["complete_resources"][1:])
               if x == a and y == b and rx != ry)


def build_evidence_mp(before_events, after_events, config: dict, seed: int, case_id: str = "",
                      dataset: str = "", time_params: dict | None = None,
                      precomputed: list[dict] | None = None, org_params: dict | None = None,
                      precomputed_org: list[dict] | None = None) -> dict[str, Any]:
    time_params = time_params or {"min_obs": 10, "eps_time": 0.0}
    tau_time = time_params.get("tau", config["qualification"]["tau"])
    pairs_time = time_params.get("pairs_per_window", config["reference"]["pairs_per_stable_window"])
    pre, post = to_traces(before_events), to_traces(after_events)
    document = build_evidence([t["activities"] for t in pre], [t["activities"] for t in post], config,
                              seed=seed, case_id=case_id, dataset=dataset)
    label_map = document["_audit"]["label_map"]
    candidates = precomputed if precomputed is not None else twait_candidates(
        pre, post, config, seed, time_params["min_obs"], pairs_time)
    candidates = [c for c in candidates
                  if c["obs_before"] >= time_params["min_obs"] and c["obs_after"] >= time_params["min_obs"]]
    eligible = [c for c in candidates if c["effect"] >= time_params["eps_time"]]
    kept = [c for c in eligible if c["q"] >= tau_time]
    items = []
    if kept:
        before_ctx, after_ctx = kept[0]["_ctx_before"], kept[0]["_ctx_after"]
        changes = [QualifiedChange("T_WAIT", c["u"], c["r"], c["q"], c["n"]) for c in kept]
        items = algorithm_2_evidence_construction_from_qualified_changes(before_ctx, after_ctx, changes, TWAIT)
        for item, c in zip(items, kept):
            item["analysis_unit"] = {"values": [label_map[str(v)] for v in c["u"]]}
            item["support"] = {"before": c["obs_before"], "after": c["obs_after"]}
    # Resources (only when the traces carry resources).
    org_items, org_eligible, org_params = [], [], org_params or {}
    if org_params and pre and "complete_resources" in pre[0]:
        tau_org = org_params.get("tau", tau_time)
        pairs_org = org_params.get("pairs_per_window", pairs_time)
        org = precomputed_org if precomputed_org is not None else org_candidates(
            pre, post, config, seed, org_params["min_obs"], pairs_org)
        units_ok = eligible_org_units(pre, post, org_params["min_obs"])
        families = set(org_params.get("families", ORG))
        allowed = {(k, u) for k, us in units_ok.items() if k in families for u in us}
        eps_by = {k: org_params.get("eps_by_family", {}).get(k, org_params.get("eps", 0.0)) for k in ORG}
        org_eligible = [c for c in org if (c["j"], c["u"]) in allowed and c["r"] >= eps_by[c["j"]]]
        org_kept = [c for c in org_eligible if c["q"] >= tau_org]
        if org_kept:
            changes = [QualifiedChange(c["j"], c["u"], c["r"], c["q"], c["n"]) for c in org_kept]
            org_items = algorithm_2_evidence_construction_from_qualified_changes(
                org_kept[0]["_ctx_before"], org_kept[0]["_ctx_after"], changes, ORG)
            for item, c in zip(org_items, org_kept):
                if item["id"].startswith("O_CONC"):
                    item["id"] = item["id"].replace("O_CONC", "CONC", 1)
                values = c["u"] if isinstance(c["u"], tuple) else (c["u"],)
                mapped = [label_map[str(v)] for v in values]
                item["analysis_unit"] = {"values": mapped} if len(mapped) > 1 else {"value": mapped[0]}
                units = [str(v) for v in values]
                item["support"] = {"before": _org_support(pre, c["j"], units), "after": _org_support(post, c["j"], units)}
        document["_audit"]["resources"] = {"params": org_params, "units_tested": len(org_eligible),
                                           "items": len(org_items),
                                           "units": [[c["j"], c["u"] if isinstance(c["u"], str) else list(c["u"])]
                                                     for c in org_kept]}
    # Screening per family: each family has its own chance rate (B + 1 - k) / (B + 1), k = ceil(tau (B + 1)).
    def chance(tau: float, pairs: int) -> float:
        n_refs = 2 * pairs
        return max(0, n_refs + 1 - math.ceil(tau * (n_refs + 1) - 1e-9)) / (n_refs + 1)
    cf = document["screening"]
    time_expected = len(eligible) * chance(tau_time, pairs_time)
    org_expected = len(org_eligible) * chance(org_params.get("tau", tau_time), org_params.get("pairs_per_window", pairs_time)) if org_params else 0.0
    document["screening"] = {
        "units_tested": cf["units_tested"] + len(eligible) + len(org_eligible),
        "items_expected_without_change": round(cf["items_expected_without_change"] + time_expected + org_expected, 2),
        "by_family": {
            "control_flow": {"units_tested": cf["units_tested"], "items": len(document["evidence"]),
                             "items_expected_without_change": cf["items_expected_without_change"]},
            "time": {"units_tested": len(eligible), "items": len(items),
                     "items_expected_without_change": round(time_expected, 3)},
        },
    }
    if org_params and pre and "complete_resources" in pre[0]:
        document["screening"]["by_family"]["resources"] = {
            "units_tested": len(org_eligible), "items": len(org_items),
            "items_expected_without_change": round(org_expected, 3)}
    document["evidence"] = document["evidence"] + items + org_items
    document["_audit"]["time"] = {"params": time_params, "twait_units_tested": len(eligible),
                                  "twait_items": len(items), "tau_time": tau_time, "pairs_per_window_time": pairs_time,
                                  "twait_units": [[label_map[str(v)] for v in c["u"]] for c in kept]}
    return document
