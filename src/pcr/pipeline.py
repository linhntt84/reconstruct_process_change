"""Pipeline v2: single entry point from two trace windows to the evidence JSON.

Implements docs/PIPELINE_V2_SPEC_VI.md with parameters from configs/pipeline_v2.json.

    from pcr.pipeline import load_config, build_evidence
    result = build_evidence(before, after, load_config(), seed=..., case_id="...")

``before`` and ``after`` are lists of traces, each a list of activity labels.
"""
from __future__ import annotations

import hashlib
import json
import math
from itertools import combinations
from pathlib import Path
from typing import Any, Sequence

from .evidence.algorithm_1_change_localization_and_qualification import QualifiedChange
from .evidence.algorithm_2_evidence_construction_from_qualified_changes import (
    algorithm_2_evidence_construction_from_qualified_changes)
from .evidence.control_flow_indicators import CONTROL_FLOW_INDICATORS
from .evidence.qualification_v2 import (
    localization_rank_counts, qualification_rank_counts, reference_context_pairs, strength, support_table)
from .evidence.reference_windows import build_control_flow_context, common_analysis_universes
from .logs import neutralize_windows
from .paths import ROOT

DEFAULT_CONFIG = ROOT / "configs" / "pipeline_v2.json"
SCHEMA_VERSION = "pcr-evidence-2.1"


def load_config(path: Path | str = DEFAULT_CONFIG) -> dict[str, Any]:
    config = json.loads(Path(path).read_text(encoding="utf-8"))
    config["_sha256"] = hashlib.sha256(Path(path).read_bytes()).hexdigest()
    return config


def windows_around(traces: Sequence, change_point: int, config: dict[str, Any],
                   change_end: int | None = None) -> tuple[list, list]:
    """Cut L- and L+ around a reported change point with the fixed guard band.

    L- = [cp - g - w, cp - g), L+ = [cp_end + g, cp_end + g + w); cp_end = cp for sudden drifts.
    """
    w, g = config["window_traces"], config["guard_traces"]
    end = change_point if change_end is None else change_end
    if change_point - g - w < 0 or end + g + w > len(traces):
        raise ValueError("not enough traces around the change point for the configured windows")
    return list(traces[change_point - g - w:change_point - g]), list(traces[end + g:end + g + w])


def build_evidence(before: Sequence[Sequence[str]], after: Sequence[Sequence[str]], config: dict[str, Any],
                   seed: int, case_id: str = "", dataset: str = "") -> dict[str, Any]:
    """Return the LLM-facing evidence document plus a private audit section."""
    ref, loc, qual = config["reference"], config["localization"], config["qualification"]
    mode, bs, ties = ref["mode"], ref["pairs_per_stable_window"], ref["ties"]
    pre, post, label_map = neutralize_windows([{"activities": list(t)} for t in before],
                                              [{"activities": list(t)} for t in after],
                                              config.get("anonymize_activities", True))

    # Stage 1: localization A*.
    edges = localization_rank_counts(pre, post, bs, seed, loc["eps_loc"], mode)
    for edge in edges:
        edge["q"] = strength(edge["lt"], edge["le"], edge["n"], ties)
    qualified_edges = [e for e in edges if e["q"] >= loc["tau_loc"] and e["d"] >= loc["eps_loc"]]
    region = sorted({a for e in qualified_edges for a in (e["s"], e["t"])})

    # Stage 2: candidate universes, references, qualification.
    families = {k: CONTROL_FLOW_INDICATORS[k] for k in qual["families"]}
    ungated = {k: v for k, v in families.items() if k != "CF_REL"}
    universes = {k: list(v) for k, v in common_analysis_universes(
        build_control_flow_context(pre, ungated), build_control_flow_context(post, ungated)).items()}
    rset = set(region)
    gated = set(qual["gated_by_localization"])
    if "CF_POS" in gated:
        universes["CF_POS"] = [u for u in universes.get("CF_POS", []) if u in rset]
    if "CF_REL" in families:
        universes["CF_REL"] = list(combinations(region, 2))
    if "CF_LAG" in gated:
        universes["CF_LAG"] = [u for u in universes.get("CF_LAG", []) if u[0] in rset and u[1] in rset]
    before_ctx = build_control_flow_context(pre, families, universes)
    after_ctx = build_control_flow_context(post, families, universes)
    references = reference_context_pairs(pre, post, families, universes, bs, seed, mode)
    candidates = qualification_rank_counts(before_ctx, after_ctx, families, references)

    # Units that could qualify at all: r > 0 (and r >= eps_REL for REL). Under no change, each
    # qualifies with probability at most P(#ref < r >= k) = (B + 1 - k) / (B + 1), k = ceil(tau (B + 1)).
    eligible = [c for c in candidates if not (c["j"] == "CF_REL" and c["r"] < qual["eps_rel"])]
    n_refs = 2 * bs
    k_min = math.ceil(qual["tau"] * (n_refs + 1) - 1e-9)
    p_chance = max(0, n_refs + 1 - k_min) / (n_refs + 1)

    kept = []
    for c in candidates:
        c["q"] = strength(c["lt"], c["le"], c["n"], ties)
        if c["q"] < qual["tau"]:
            continue
        if c["j"] == "CF_REL" and c["r"] < qual["eps_rel"]:
            continue
        kept.append(c)
    changes = [QualifiedChange(c["j"], c["u"], c["r"], c["q"], c["n"]) for c in kept]
    items = algorithm_2_evidence_construction_from_qualified_changes(before_ctx, after_ctx, changes, families)
    units = [(c["j"], c["u"]) for c in kept]
    support_before, support_after = support_table(units, pre), support_table(units, post)
    for item, unit in zip(items, units):
        item["support"] = {"before": support_before[unit], "after": support_after[unit]}

    return {
        "schema_version": SCHEMA_VERSION,
        "case": {"case_id": case_id, "dataset": dataset},
        "windows": {"before_traces": len(pre), "after_traces": len(post)},
        "screening": {"units_tested": len(eligible),
                      "items_expected_without_change": round(len(eligible) * p_chance, 2)},
        "evidence": items,
        "_audit": {
            "spec_version": config["spec_version"], "config_sha256": config.get("_sha256"), "seed": seed,
            "label_map": label_map, "localized_activities": region,
            "qualified_edges": [{k: e[k] for k in ("s", "t", "d", "q")} for e in qualified_edges],
            "stage2_candidates": len(candidates),
        },
    }


def llm_payload(document: dict[str, Any]) -> dict[str, Any]:
    """The part sent to the LLM: no audit section and no dataset name (benchmark names can leak labels)."""
    payload = {k: v for k, v in document.items() if not k.startswith("_")}
    payload["case"] = {"case_id": document["case"]["case_id"]}
    return payload
