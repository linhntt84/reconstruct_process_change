#!/usr/bin/env python3
"""P5: three-run aggregation of P2 (glm-5.3-flash, deepseek-v4-flash) and P3 (glm ablations); no API calls.

Per (method, set) and metric:
  per-run means (runs 1-3), mean and SD across runs, and a 95% case-bootstrap CI of the mean, where each case
  contributes its mean over the three runs (B = 5000; one generator per row seeded by 20261116 and the
  row's values, so rows do not depend on each other).
Paired contrasts (GLM vs DeepSeek in P2; each P3 variant vs P2 GLM on the same cases):
  difference of the per-case three-run means, its 95% bootstrap CI, and the per-run differences (sign stability).
Null sets: share "insufficient" (higher is better) per run.
E5-MP: control-flow and time parts scored separately (analyze_p3.mp_parts) per run.
Inputs: the scores_*.csv written by score_p2.py / cdlg_roles.py for runs 1-3.
Output: results/p5_stats/runs3_summary.md and runs3_summary.csv.
"""
from __future__ import annotations

import csv
import json
import math
import random
import sys
from pathlib import Path
from statistics import mean, stdev

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "experiments" / "p0_llm_calibration"))
sys.path.insert(0, str(ROOT / "experiments" / "p2_main"))
sys.path.insert(0, str(ROOT / "experiments" / "p3_ablation"))

P2 = ROOT / "results" / "p2_main"
P3 = ROOT / "results" / "p3_ablation"
OUT = ROOT / "results" / "p5_stats"
MAIN = "INTERPRET_EVIDENCE_V2_EN_R3_MP_CONC"
GLM, DS = "glm-5.3-flash", "deepseek-v4-flash"
RUNS = (1, 2, 3)
B, SEED = 5000, 20261116
EXPS = ["e3_noselect", "e3b_v2en", "e5_no_occ", "e5_no_dir", "e5_no_pos", "e5_no_rel", "e5_no_lag",
        "e5_no_time", "e5_no_cf", "e8_labels", "e9_shuffle", "e3_full"]
METRICS = {"ostovar3": ("O", "MR", "PI", "RTU", "overclaim", "n_secondary"),
           "ostovar5": ("O", "MR", "PI", "RTU", "overclaim", "n_secondary"),
           "cdlg": ("O", "O_main", "O_F1"),
           "cdlg_roles": ("O", "MR", "PI", "RTU", "overclaim", "RTU_all"),
           "e4a": ("O", "MR", "PI", "time_detected", "time_direction_ok"),
           "e4b": ("target_claimed", "target_main")}
# Ungated scores, reported in the P2 per-model table only (not used in contrasts or ablations).
RAW = {"ostovar3": ("MR_raw", "PI_raw"), "ostovar5": ("MR_raw", "PI_raw"), "e4a": ("MR_raw", "PI_raw"),
       "cdlg_roles": ("MR_raw", "PI_raw")}


def num(x):
    try:
        v = float(x)
        return None if math.isnan(v) else v
    except (TypeError, ValueError):
        return None


def read(path: Path) -> dict:
    if not path.exists():
        return {}
    with path.open(encoding="utf-8") as handle:
        return {r["case_id"]: r for r in csv.DictReader(handle)}


def p2_scores(model: str, run: int, roles: bool = False) -> dict:
    return read(P2 / f"scores_{'cdlg_roles_' if roles else ''}{MAIN}_{model}_run{run}.csv")


def p3_scores(exp: str, run: int, roles: bool = False) -> dict:
    prompt = "INTERPRET_EVIDENCE_V2_EN" if exp == "e3b_v2en" else MAIN
    return read(P3 / exp / f"scores_{'cdlg_roles_' if roles else ''}{prompt}_{GLM}_run{run}.csv")


def value(row: dict, metric: str):
    if metric == "insufficient":
        return float(row["support_level"] == "insufficient")
    return num(row.get(metric))


def per_case(runs: list[dict], ids: list[str], metric: str) -> dict:
    """case -> mean over the runs that have a value."""
    out = {}
    for c in ids:
        vals = [value(r[c], metric) for r in runs if c in r]
        vals = [v for v in vals if v is not None]
        if vals:
            out[c] = mean(vals)
    return out


def boot_ci(values: list[float], rng: random.Random) -> tuple[float, float]:
    n = len(values)
    if n == 0:
        return float("nan"), float("nan")
    # One generator per row, seeded by SEED and the row's own values, so that a change in one row (e.g. an
    # excluded case) does not shift the resamples of the others. The rng argument is kept for the call sites.
    rng = random.Random(f"{SEED}:{[round(v, 6) for v in values]!r}")
    stats = sorted(mean(rng.choices(values, k=n)) for _ in range(B))
    return stats[int(0.025 * B)], stats[int(0.975 * B) - 1]


def summary(runs: list[dict], ids: list[str], metric: str, rng) -> dict:
    run_means = []
    for r in runs:
        vals = [value(r[c], metric) for c in ids if c in r]
        vals = [v for v in vals if v is not None]
        run_means.append(mean(vals) if vals else float("nan"))
    pc = per_case(runs, ids, metric)
    lo, hi = boot_ci(list(pc.values()), rng)
    return {"runs": run_means, "mean": mean(pc.values()) if pc else float("nan"),
            "sd_runs": stdev(run_means) if len(run_means) > 1 else 0.0, "lo": lo, "hi": hi, "n": len(pc)}


def contrast(a_runs, b_runs, ids, metric, rng) -> dict:
    """b - a on the per-case three-run means (paired by case)."""
    pa, pb = per_case(a_runs, ids, metric), per_case(b_runs, ids, metric)
    common = [c for c in ids if c in pa and c in pb]
    diffs = [pb[c] - pa[c] for c in common]
    lo, hi = boot_ci(diffs, rng)
    per_run = []
    for ra, rb in zip(a_runs, b_runs):
        pairs = [(value(ra[c], metric), value(rb[c], metric)) for c in common if c in ra and c in rb]
        pairs = [(x, y) for x, y in pairs if x is not None and y is not None]
        per_run.append(mean(y - x for x, y in pairs) if pairs else float("nan"))
    return {"a": mean(pa[c] for c in common) if common else float("nan"),
            "b": mean(pb[c] for c in common) if common else float("nan"),
            "diff": mean(diffs) if diffs else float("nan"), "lo": lo, "hi": hi, "per_run": per_run, "n": len(common)}


def f3(x):
    return "–" if x != x else f"{x:.3f}"


def groups(scores: dict) -> list[tuple[str, str]]:
    return sorted({(r["set"], r["kind"]) for r in scores.values()})


def metrics_for(set_: str, kind: str) -> tuple:
    if kind == "null":
        return ("insufficient",) if set_ not in ("e4a", "e4b") else (
            ("time_false_claim",) if set_ == "e4a" else ("n_resource_claims",))
    return METRICS[set_]


def mp_rows(rng) -> list[str]:
    from analyze_p3 import mp_parts
    from score_p2 import e4_cases
    e4 = e4_cases()
    lines = ["## E5-MP (E4a type M, 26 cases): parts scored separately, three runs", "",
             "| Variant | O_cf | PI_cf | time detected | time direction ok | per-run PI_cf | per-run time detected |",
             "|---|---|---|---|---|---|---|"]
    for label, base, exp in (("P2 (both perspectives)", P2, None), ("no time", P3 / "e5_no_time", "e5_no_time"),
                             ("no control-flow", P3 / "e5_no_cf", "e5_no_cf")):
        ids = [c for c in read(P3 / "e5_no_time" / "cases.csv")]
        per_run = []
        for k in RUNS:
            folder = base / "extractions_r5" / MAIN / GLM / f"run{k}"
            parts = []
            for cid in ids:
                path = folder / f"{cid}.json"
                if path.exists():
                    lm = json.loads((P2 / "audit" / f"{cid}.json").read_text(encoding="utf-8"))["label_map"]
                    parts.append(mp_parts(json.loads(path.read_text(encoding="utf-8"))["extraction"], e4[cid], lm))
            per_run.append({k2: mean(p[k2] for p in parts) for k2 in ("O_cf", "PI_cf", "time_detected", "time_ok")})
        avg = {k2: mean(r[k2] for r in per_run) for k2 in per_run[0]}
        lines.append(f"| {label} | {f3(avg['O_cf'])} | {f3(avg['PI_cf'])} | {f3(avg['time_detected'])} | "
                     f"{f3(avg['time_ok'])} | {' / '.join(f3(r['PI_cf']) for r in per_run)} | "
                     f"{' / '.join(f3(r['time_detected']) for r in per_run)} |")
    return lines


def main():
    rng = random.Random(SEED)
    OUT.mkdir(parents=True, exist_ok=True)
    csv_rows = []
    md = ["# P5: three runs (runs 1-3), P2 and P3", "",
          "Generated by experiments/p5_stats/aggregate_runs.py (no API calls). Mean = mean over cases of the "
          "per-case three-run mean; 95% CI = case bootstrap (B = 5000); SD = across the three run means.", ""]
    # P2
    md += ["## P2: main results per model", "",
           "| Model | Set | Metric | n | Run 1 / 2 / 3 | Mean | SD (runs) | 95% CI |", "|---|---|---|---|---|---|---|---|"]
    p2 = {m: [p2_scores(m, k) for k in RUNS] for m in (GLM, DS)}
    p2r = {m: [p2_scores(m, k, roles=True) for k in RUNS] for m in (GLM, DS)}
    for m in (GLM, DS):
        for set_, kind in groups(p2[m][0]):
            ids = [c for c, r in p2[m][0].items() if r["set"] == set_ and r["kind"] == kind]
            for metric in metrics_for(set_, kind) + (RAW.get(set_, ()) if kind == "drift" else ()):
                s = summary(p2[m], ids, metric, rng)
                md.append(f"| {m} | {set_} {kind} | {metric} | {s['n']} | {' / '.join(f3(x) for x in s['runs'])} | "
                          f"**{f3(s['mean'])}** | {f3(s['sd_runs'])} | [{f3(s['lo'])}, {f3(s['hi'])}] |")
                csv_rows.append({"part": "P2", "method": m, "set": f"{set_} {kind}", "metric": metric, **s})
        ids = list(p2r[m][0])
        for metric in METRICS["cdlg_roles"] + RAW["cdlg_roles"]:
            s = summary(p2r[m], ids, metric, rng)
            md.append(f"| {m} | cdlg roles (r5a) | {metric} | {s['n']} | {' / '.join(f3(x) for x in s['runs'])} | "
                      f"**{f3(s['mean'])}** | {f3(s['sd_runs'])} | [{f3(s['lo'])}, {f3(s['hi'])}] |")
            csv_rows.append({"part": "P2", "method": m, "set": "cdlg roles", "metric": metric, **s})
    md += ["", "## P2: DeepSeek minus GLM (paired by case)", "",
           "| Set | Metric | n | GLM | DeepSeek | Diff | 95% CI | per-run diff |", "|---|---|---|---|---|---|---|---|"]
    for set_, kind in groups(p2[GLM][0]):
        ids = [c for c, r in p2[GLM][0].items() if r["set"] == set_ and r["kind"] == kind]
        for metric in metrics_for(set_, kind)[:3]:
            c = contrast(p2[GLM], p2[DS], ids, metric, rng)
            md.append(f"| {set_} {kind} | {metric} | {c['n']} | {f3(c['a'])} | {f3(c['b'])} | **{c['diff']:+.3f}** | "
                      f"[{c['lo']:+.3f}, {c['hi']:+.3f}] | {' / '.join(f'{x:+.3f}' for x in c['per_run'])} |")
    for metric in METRICS["cdlg_roles"]:
        c = contrast(p2r[GLM], p2r[DS], list(p2r[GLM][0]), metric, rng)
        md.append(f"| cdlg roles | {metric} | {c['n']} | {f3(c['a'])} | {f3(c['b'])} | **{c['diff']:+.3f}** | "
                  f"[{c['lo']:+.3f}, {c['hi']:+.3f}] | {' / '.join(f'{x:+.3f}' for x in c['per_run'])} |")
    # P3
    md += ["", "## P3: each ablation minus P2 GLM (paired by case, three runs each)", "",
           "Positive = higher in the variant. For null sets the metric is the share 'insufficient'.", "",
           "| Exp | Set | Metric | n | P2 | Variant | Diff | 95% CI | per-run diff |",
           "|---|---|---|---|---|---|---|---|---|"]
    for exp in EXPS:
        var = [p3_scores(exp, k) for k in RUNS]
        for set_, kind in groups(var[0]):
            ids = [c for c, r in var[0].items() if r["set"] == set_ and r["kind"] == kind]
            for metric in metrics_for(set_, kind):
                c = contrast(p2[GLM], var, ids, metric, rng)
                md.append(f"| {exp} | {set_} {kind} | {metric} | {c['n']} | {f3(c['a'])} | {f3(c['b'])} | "
                          f"**{c['diff']:+.3f}** | [{c['lo']:+.3f}, {c['hi']:+.3f}] | "
                          f"{' / '.join(f'{x:+.3f}' for x in c['per_run'])} |")
                csv_rows.append({"part": "P3", "method": exp, "set": f"{set_} {kind}", "metric": metric,
                                 "p2": c["a"], "var": c["b"], "diff": c["diff"], "lo": c["lo"], "hi": c["hi"],
                                 "runs": c["per_run"], "n": c["n"]})
        vr = [p3_scores(exp, k, roles=True) for k in RUNS]
        if vr[0]:
            for metric in METRICS["cdlg_roles"]:
                c = contrast(p2r[GLM], vr, list(vr[0]), metric, rng)
                md.append(f"| {exp} | cdlg roles | {metric} | {c['n']} | {f3(c['a'])} | {f3(c['b'])} | "
                          f"**{c['diff']:+.3f}** | [{c['lo']:+.3f}, {c['hi']:+.3f}] | "
                          f"{' / '.join(f'{x:+.3f}' for x in c['per_run'])} |")
                csv_rows.append({"part": "P3", "method": exp, "set": "cdlg roles", "metric": metric,
                                 "p2": c["a"], "var": c["b"], "diff": c["diff"], "lo": c["lo"], "hi": c["hi"],
                                 "runs": c["per_run"], "n": c["n"]})
    md += [""] + mp_rows(rng)
    (OUT / "runs3_summary.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    fields = list(dict.fromkeys(k for r in csv_rows for k in r))
    with (OUT / "runs3_summary.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(csv_rows)
    print("\n".join(md))


if __name__ == "__main__":
    main()
