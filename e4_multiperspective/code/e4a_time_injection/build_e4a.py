#!/usr/bin/env python3
"""E4a: Ostovar windows with injected time changes (design: e4_multiperspective/docs/KE_HOACH_E4_VI.md).

Injection (Padella & Vinci, BPM 2026): for every occurrence of the target activity X in
the after-window L+ that has a preceding event, the time from that event to the completion
of X, d, becomes k*d; X and every later event of the trace move by (k - 1)*d. Ostovar logs
only have completion timestamps, so this is exactly the quantity T_WAIT measures for the
pair (predecessor -> X). Activity sequences are never changed.

Case types (k = 2 slow-down, k = 0.5 speed-up):
  T_SLOW, T_FAST  stable windows of the null shape, L- = [350, 550), L+ = [650, 850)
  N               the same windows, no injection (paired with T)
  M               drift-1 windows, L- = [650, 850), L+ = [950, 1150), the existing
                  control-flow change plus a time change on another activity (half slow,
                  half fast)
Splits: evaluation = sizes 3 and 5, all 13 patterns (26 cases per type);
        tuning = sizes 2 and 4, 3 patterns per size and type (6 cases per type).
Noise-free logs only.

Target X: seeded choice among activities present in >= 30% of L+ traces, that have a
preceding event in >= 90% of their occurrences and a positive preceding gap in >= 90% of
them, and (type M) that are not in the required or optional set of the control-flow change.

Outputs (e4_multiperspective/results/e4a_time_injection/):
  cases/<case_id>.json.gz  {"before": [[[activity, iso_ts], ...], ...], "after": [...]}
  cases.csv                one row per case with the answer key
  sanity.csv               checks per case (see check())
"""
from __future__ import annotations

import csv
import gzip
import hashlib
import json
import random
import statistics
import sys
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]  # repository root
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "experiments" / "e0_parameter_setting"))
sys.path.insert(0, str(HERE.parent))
import build_tuning_references as refrule  # noqa: E402
from e4_common import E4_RESULTS, read_mxml_events  # noqa: E402
from pcr.paths import OSTOVAR_FULL  # noqa: E402

OUT = E4_RESULTS / "e4a_time_injection"
SEED = 20261113
K = {"T_SLOW": 2.0, "T_FAST": 0.5}
NULL_WINDOWS = ((350, 550), (650, 850))
DRIFT1_WINDOWS = ((650, 850), (950, 1150))
EVAL_SIZES, TUNING_SIZES = (3, 5), (2, 4)
TUNING_PER_SIZE = 3
MIN_PRESENCE, MIN_PRED, MIN_POSITIVE = 0.30, 0.90, 0.90


def ts(value: str) -> datetime:
    return datetime.fromisoformat(value)


def case_id(size: int, pattern: str, kind: str) -> str:
    return "e4a_" + hashlib.sha256(f"e4a::size{size}::{pattern}::{kind}".encode()).hexdigest()[:16]


def candidates(after, exclude: set[str]) -> list[str]:
    n = len(after)
    presence, occ, with_pred, positive = {}, {}, {}, {}
    for trace in after:
        for a in {e[0] for e in trace}:
            presence[a] = presence.get(a, 0) + 1
        for i, (a, t) in enumerate(trace):
            occ[a] = occ.get(a, 0) + 1
            if i > 0:
                with_pred[a] = with_pred.get(a, 0) + 1
                if ts(t) > ts(trace[i - 1][1]):
                    positive[a] = positive.get(a, 0) + 1
    return sorted(a for a in presence
                  if a not in exclude and presence[a] / n >= MIN_PRESENCE
                  and with_pred.get(a, 0) / occ[a] >= MIN_PRED
                  and positive.get(a, 0) / max(1, with_pred.get(a, 0)) >= MIN_POSITIVE)


def inject(after, target: str, k: float):
    out = []
    for trace in after:
        new, shift = [], timedelta(0)
        for i, (a, t) in enumerate(trace):
            moment = ts(t) + shift
            if a == target and i > 0:
                gap = ts(t) - ts(trace[i - 1][1])
                shift += (k - 1.0) * gap
                moment = ts(t) + shift
            new.append([a, moment.isoformat()])
        out.append(new)
    return out


def gaps(traces, into: str | None = None) -> dict[tuple[str, str], list[float]]:
    result: dict[tuple[str, str], list[float]] = {}
    for trace in traces:
        for (a, ta), (b, tb) in zip(trace, trace[1:]):
            if into is None or b == into:
                result.setdefault((a, b), []).append((ts(tb) - ts(ta)).total_seconds() / 60)
    return result


def check(original_after, injected_after, target: str | None, k: float | None) -> dict:
    """Sanity: (1) activity sequences unchanged; (2) gaps into X scaled by k (median ratio);
    (3) every other directly-follows gap unchanged."""
    same_sequences = all([e[0] for e in a] == [e[0] for e in b] for a, b in zip(original_after, injected_after))
    before_g, after_g = gaps(original_after), gaps(injected_after)
    other_changed = 0
    ratio = None
    for pair, values in before_g.items():
        if target is not None and pair[1] == target:
            continue
        if any(abs(x - y) > 1e-6 for x, y in zip(values, after_g[pair])):
            other_changed += 1
    if target is not None:
        into_before = [v for p, vs in before_g.items() if p[1] == target for v in vs]
        into_after = [v for p, vs in after_g.items() if p[1] == target for v in vs]
        ratio = statistics.median(into_after) / statistics.median(into_before)
    return {"sequences_unchanged": same_sequences, "other_gaps_changed": other_changed,
            "median_ratio_into_target": round(ratio, 4) if ratio is not None else "",
            "expected_ratio": k if k is not None else ""}


def write_case(cid: str, before, after) -> None:
    (OUT / "cases").mkdir(parents=True, exist_ok=True)
    with gzip.open(OUT / "cases" / f"{cid}.json.gz", "wt", encoding="utf-8") as handle:
        json.dump({"before": before, "after": after}, handle)


def main():
    rng = random.Random(SEED)
    patterns = refrule.PATTERNS
    plan = []  # (split, size, pattern, kind)
    for kind in ("T_SLOW", "T_FAST", "N", "M"):
        for size in EVAL_SIZES:
            plan += [("evaluation", size, p, kind) for p in patterns]
        for size in TUNING_SIZES:
            plan += [("tuning", size, p, kind) for p in sorted(rng.sample(patterns, TUNING_PER_SIZE))]
    m_direction = {}
    for split in ("evaluation", "tuning"):
        m_cases = [(s, p) for sp, s, p, kd in plan if sp == split and kd == "M"]
        flags = ["T_SLOW", "T_FAST"] * (len(m_cases) // 2) + (["T_SLOW"] if len(m_cases) % 2 else [])
        rng.shuffle(flags)  # exactly half slow, half fast
        m_direction.update({c: flags[i] for i, c in enumerate(m_cases)})

    rows, sanity, logs = [], [], {}
    for split, size, pattern, kind in plan:
        key = (size, pattern)
        if key not in logs:
            logs[key] = read_mxml_events(OSTOVAR_FULL / f"Size{size}/Atomic/{pattern}/output/{pattern}.mxml.gz")
        traces = logs[key]
        (b0, b1), (a0, a1) = DRIFT1_WINDOWS if kind == "M" else NULL_WINDOWS
        before, after = traces[b0:b1], traces[a0:a1]
        cid = case_id(size, pattern, kind)
        cf_required, cf_optional, cf_pattern = [], [], ""
        if kind == "M":
            changed = refrule.changed_activities([[e[0] for e in t] for t in traces], 1)
            cf_required, cf_optional = refrule.required_optional(pattern, size, changed)
            cf_pattern = pattern
        target, k, direction, preds = "", None, "", []
        injected = [[list(e) for e in t] for t in after]
        if kind != "N":
            time_kind = m_direction[(size, pattern)] if kind == "M" else kind
            k = K[time_kind]
            direction = "increase" if k > 1 else "decrease"
            pool = candidates(after, set(cf_required) | set(cf_optional))
            target = random.Random(f"{SEED}:{cid}").choice(pool)
            injected = inject(after, target, k)
            preds = sorted({t[i - 1][0] for t in after for i, e in enumerate(t) if e[0] == target and i > 0})
        write_case(cid, [[list(e) for e in t] for t in before], injected)
        required = sorted(set(cf_required) | ({target} if target else set()))
        optional = sorted((set(cf_optional) | set(preds)) - set(required))
        perspectives = (["control_flow"] if kind == "M" else []) + (["time"] if target else [])
        rows.append({"case_id": cid, "split": split, "type": kind, "fragment_size": size, "pattern_log": pattern,
                     "window_before": f"[{b0},{b1})", "window_after": f"[{a0},{a1})",
                     "time_target": target, "k": k if k else "", "time_direction": direction,
                     "time_predecessors": json.dumps(preds), "cf_pattern": cf_pattern,
                     "cf_required": json.dumps(cf_required), "cf_optional": json.dumps(cf_optional),
                     "required_activities_real": json.dumps(required),
                     "optional_activities_real": json.dumps(optional),
                     "perspectives": json.dumps(perspectives),
                     "source_log": f"Size{size}/Atomic/{pattern}/output/{pattern}.mxml.gz"})
        sanity.append({"case_id": cid, "type": kind, **check(after, injected, target or None, k)})
    for name, data in (("cases.csv", rows), ("sanity.csv", sanity)):
        with (OUT / name).open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(data[0]))
            writer.writeheader()
            writer.writerows(data)
    bad = [s for s in sanity if not s["sequences_unchanged"] or s["other_gaps_changed"]]
    off = [s for s in sanity if s["expected_ratio"] and abs(s["median_ratio_into_target"] - s["expected_ratio"]) > 0.05]
    print(f"{len(rows)} cases -> {OUT}; sanity failures: {len(bad)}; ratio off by > 0.05: {len(off)}")


if __name__ == "__main__":
    main()
