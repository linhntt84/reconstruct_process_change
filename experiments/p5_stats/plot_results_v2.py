#!/usr/bin/env python3
"""Figures for Section VII (Results) of the revision, from archived scores only (no API calls).

Fig. outcome profile   fig_v2_outcome_profile.pdf   share of cases per score outcome, Ostovar 3 / 5 / CDLG,
                                                      GLM, DeepSeek, rule-based interpreter, ProDrift.
Fig. pattern heatmap   fig_v2_pattern_heatmap.pdf   mean PI per Ostovar pattern (sizes 3, 5) and per CDLG
                                                      operation class, same four methods.
Fig. multi-perspective fig_v2_multiperspective.pdf  E4a timing changes detected (by type) and E4b target
                                                      activity claimed (by type).
Fig. ablations         fig_v2_ablation_forest.pdf   paired differences (variant - full pipeline, GLM) with
                                                      95% bootstrap CI, from results/p5_stats/runs3_summary.csv.

LLM values pool runs 1-3 (each case contributes its 3-run mean); the rule-based interpreter (run 1) and ProDrift
are deterministic. CIs: case bootstrap of aggregate_runs.boot_ci (B = 5000, seed per row).
Outputs: results/p5_stats/figures/*.pdf and *.csv; copies to the LaTeX figures folder with --copy.

  python experiments/p5_stats/plot_results_v2.py [--copy]
"""
from __future__ import annotations

import argparse
import csv
import os
import shutil
import sys
import tempfile
from collections import defaultdict
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from aggregate_runs import boot_ci  # noqa: E402

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "pcr-matplotlib"))
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402

P2 = ROOT / "results" / "p2_main"
E1 = ROOT / "results" / "e1_prodrift"
E4A_PD = ROOT / "e4_multiperspective" / "results" / "e4a_time_injection" / "prodrift" / "scores.csv"
SUMMARY = ROOT / "results" / "p5_stats" / "runs3_summary.csv"
OUT = ROOT / "results" / "p5_stats" / "figures"
LATEX = ROOT.parent / "Latex" / "IEEE_Access_2026_revision" / "figures"
PROMPT = "INTERPRET_EVIDENCE_V2_EN_R3_MP_CONC"

# Categorical colours (checked for CVD separation: adjacent ΔE_OKLab >= 13 under protan/deutan/tritan).
METHODS = [("glm", "GLM", "#005580"), ("ds", "DeepSeek", "#56B4E9"),
           ("rule", "Rule-based", "#7F7F7F"), ("pd", "ProDrift", "#E69F00")]
OUTCOMES = [("Ready to use (1, 1, 1)", "#005580"),
            ("Pattern or class partial (1, 1, <1)", "#56B4E9"),
            ("Mechanism or roles wrong (1, <1, ·)", "#D55E00"),
            ("Activities partial (0.5, ·, ·)", "#E69F00"),
            ("Activities missed (0, ·, ·)", "#BDBDBD")]
INK, MUTED, GRID = "#1A1A1A", "#555555", "#DDDDDD"
STYLE = {"font.family": "serif", "font.serif": ["STIXGeneral", "DejaVu Serif"], "mathtext.fontset": "stix",
         "font.size": 8, "axes.titlesize": 8.5, "axes.labelsize": 8, "xtick.labelsize": 7.5,
         "ytick.labelsize": 7.5, "legend.fontsize": 7.5, "pdf.fonttype": 42, "ps.fonttype": 42,
         "axes.edgecolor": MUTED, "axes.linewidth": 0.6, "xtick.color": MUTED, "ytick.color": MUTED,
         "xtick.major.width": 0.6, "ytick.major.width": 0.6, "text.color": INK, "axes.labelcolor": INK}
OSTOVAR_ORDER = ["SerialRemoval", "ParallelRemoval", "ConditionalRemoval", "SerialMove", "ParallelMove",
                 "ConditionalMove", "Swap", "ConditionalToSequence", "ParallelToSequence", "Substitute",
                 "Loop", "Skip", "Frequency"]
OSTOVAR_SHORT = {"ConditionalToSequence": "Cond. to sequence", "ParallelToSequence": "Parallel to sequence",
                 "ConditionalRemoval": "Cond. removal", "ConditionalMove": "Cond. move"}
CDLG_ORDER = ["only_added", "only_deleted", "only_moved", "deleted_and_added", "added_and_moved",
              "deleted_and_moved", "other"]
CDLG_LABEL = {"only_added": "Added only", "only_deleted": "Deleted only", "only_moved": "Moved only",
              "deleted_and_added": "Deleted + added", "added_and_moved": "Added + moved",
              "deleted_and_moved": "Deleted + moved", "other": "Other"}


def read(path: Path) -> list[dict]:
    with path.open(encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def write(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def num(x) -> float:
    return float(x) if x not in ("", None, "nan") else float("nan")


def spaced(name: str) -> str:
    return OSTOVAR_SHORT.get(name, "".join(" " + c.lower() if c.isupper() and i else c
                                           for i, c in enumerate(name)))


# ---------------------------------------------------------------- data
def llm_rows(model: str, roles: bool = False) -> list[list[dict]]:
    tag = "cdlg_roles_" if roles else ""
    return [read(P2 / f"scores_{tag}{PROMPT}_{model}_run{k}.csv") for k in (1, 2, 3)]


def rule_rows(roles: bool = False) -> list[list[dict]]:
    return [read(P2 / f"scores_{'cdlg_roles_' if roles else ''}RULE_BASELINE_V2_rule-engine-v1_run1.csv")]


def outcome(o: float, mr: float, pi: float) -> int:
    if o == 0:
        return 4
    if o == 0.5:
        return 3
    if mr < 1:
        return 2
    return 0 if pi == 1 else 1


def case_records() -> dict:
    """{(set, method): [runs: [ {case, group, O, MR, PI} ]]} for Ostovar 3/5 and CDLG drift cases."""
    data = {}
    for key, model in (("glm", "glm-5.3-flash"), ("ds", "deepseek-v4-flash"), ("rule", None)):
        runs = llm_rows(model) if model else rule_rows()
        roles = llm_rows(model, True) if model else rule_rows(True)
        for size in ("ostovar3", "ostovar5"):
            data[(size, key)] = [[{"case": r["case_id"], "group": r["type"], "O": num(r["O"]), "MR": num(r["MR"]),
                                   "PI": num(r["PI"])} for r in run if r["set"] == size and r["kind"] == "drift"]
                                 for run in runs]
        data[("cdlg", key)] = [[{"case": r["case_id"], "group": r["operation_class"], "O": num(r["O"]),
                                 "MR": num(r["MR"]), "PI": num(r["PI"])} for r in run] for run in roles]
    pd = read(E1 / "scores.csv")
    for size, s in (("ostovar3", "3"), ("ostovar5", "5")):
        data[(size, "pd")] = [[{"case": f"{r['pattern']}|{r['noise']}|{r['drift']}", "group": r["pattern"],
                                "O": num(r["O"]), "MR": num(r["MR"]), "PI": num(r["PI"])}
                               for r in pd if r["size"] == s and r["split"] == "evaluation"]]
    data[("cdlg", "pd")] = [[{"case": r["case_id"], "group": r["operation_class"], "O": num(r["O"]),
                              "MR": num(r["MR"]), "PI": num(r["PI"])} for r in read(E1 / "scores_cdlg_isolated.csv")]]
    for (s, m), runs in data.items():
        n = {len(run) for run in runs}
        assert len(n) == 1 and n.pop() == {"ostovar3": 78, "ostovar5": 78, "cdlg": 99}[s], (s, m)
        assert all(r["O"] == r["O"] for run in runs for r in run), (s, m)  # no missing scores
    return data


def per_case_mean(runs: list[list[dict]], metric: str) -> dict:
    vals = defaultdict(list)
    for run in runs:
        for r in run:
            vals[r["case"]].append(r[metric])
    return {c: mean(v) for c, v in vals.items()}


# ---------------------------------------------------------------- figures
def style_axis(ax, grid_axis="y"):
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.set_axisbelow(True)
    if grid_axis:
        ax.grid(axis=grid_axis, color=GRID, linewidth=0.5)
    ax.tick_params(length=2.5)


def fig_outcome_profile(data: dict) -> None:
    sets = [("ostovar3", "(a) Ostovar, fragment size 3 (n = 78)"),
            ("ostovar5", "(b) Ostovar, fragment size 5 (n = 78)"),
            ("cdlg", "(c) CDLG (n = 99)")]
    rows = []
    fig, axes = plt.subplots(1, 3, figsize=(7.16, 2.55), sharey=True)
    fig.subplots_adjust(left=0.065, right=0.995, top=0.90, bottom=0.30, wspace=0.08)
    for ax, (s, title) in zip(axes, sets):
        for x, (m, label, _) in enumerate(METHODS):
            runs = data[(s, m)]
            counts = [0] * len(OUTCOMES)
            for run in runs:
                for r in run:
                    counts[outcome(r["O"], r["MR"], r["PI"])] += 1
            total = sum(counts)
            bottom = 0.0
            for i, (name, color) in enumerate(OUTCOMES):
                share = counts[i] / total
                rows.append({"set": s, "method": label, "outcome": name, "share": round(share, 4),
                             "n_cases": len(runs[0]), "n_runs": len(runs)})
                if share:
                    ax.bar(x, share, bottom=bottom, width=0.72, color=color, edgecolor="white", linewidth=0.8)
                    if share >= 0.07:
                        ax.text(x, bottom + share / 2, f"{100 * share:.0f}", ha="center", va="center",
                                fontsize=7, color="white" if i in (0, 2) else INK)
                bottom += share
        ax.set_title(title, loc="left", pad=4)
        ax.set_xticks(range(len(METHODS)), [m[1] for m in METHODS])
        ax.set_xlim(-0.55, len(METHODS) - 0.45)
        ax.set_ylim(0, 1)
        ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0], ["0", "25", "50", "75", "100"])
        style_axis(ax)
    axes[0].set_ylabel("Share of cases (%)")
    fig.legend([Patch(facecolor=c, edgecolor="none") for _, c in OUTCOMES], [n for n, _ in OUTCOMES],
               loc="lower center", ncol=3, frameon=False, bbox_to_anchor=(0.53, 0.0), handlelength=1.2,
               columnspacing=1.4, title="Outcome (O, MR, PI)", title_fontsize=7.5)
    save(fig, "fig_v2_outcome_profile", rows)


def fig_pattern_heatmap(data: dict) -> None:
    cmap = LinearSegmentedColormap.from_list("pi", ["#FFFFFF", "#C6DDEC", "#3F7FA6", "#003F60"])
    rows = []

    def matrix(sets, groups):
        mat = []
        for g in groups:
            line = []
            for s in sets:
                for m, label, _ in METHODS:
                    runs = [[r for r in run if r["group"] == g] for run in data[(s, m)]]
                    v = mean(per_case_mean(runs, "PI").values())
                    line.append(v)
                    rows.append({"set": s, "group": g, "method": label, "PI": round(v, 4), "n_cases": len(runs[0])})
            mat.append(line)
        return mat

    def draw(ax, mat, ylabels, xlabels, title, seps=()):
        # vector cells (pcolormesh), not an embedded raster image, so the PDF stays sharp at any zoom
        nr, nc = len(mat), len(mat[0])
        ax.pcolormesh([j - 0.5 for j in range(nc + 1)], [i - 0.5 for i in range(nr + 1)], mat, cmap=cmap,
                      vmin=0, vmax=1, shading="flat", rasterized=False)
        ax.set_xlim(-0.5, nc - 0.5)
        ax.set_ylim(nr - 0.5, -0.5)
        for i, line in enumerate(mat):
            for j, v in enumerate(line):
                txt = "1" if v >= 0.995 else "0" if v < 0.005 else f"{v:.2f}"[1:]
                ax.text(j, i, txt, ha="center", va="center", fontsize=6.5,
                        color="white" if v >= 0.70 else INK)
        ax.set_yticks(range(len(ylabels)), ylabels)
        ax.set_xticks(range(len(xlabels)), xlabels, rotation=0)
        ax.tick_params(length=0)
        for sp in ax.spines.values():
            sp.set_visible(False)
        ax.set_xticks([j - 0.5 for j in range(1, len(xlabels))], minor=True)
        ax.set_yticks([i - 0.5 for i in range(1, len(ylabels))], minor=True)
        ax.grid(which="minor", color="white", linewidth=1.2)
        ax.tick_params(which="minor", length=0)
        for x in seps:
            ax.axvline(x, color=INK, linewidth=0.8)
        ax.set_title(title, loc="left", pad=15)

    short = ["GLM", "DS", "Rule", "PD"]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.16, 3.05), gridspec_kw={"width_ratios": [8, 4.2]})
    fig.subplots_adjust(left=0.135, right=0.995, top=0.855, bottom=0.075, wspace=0.42)
    mat = matrix(("ostovar3", "ostovar5"), OSTOVAR_ORDER)
    draw(a1, mat, [f"{spaced(p)}" for p in OSTOVAR_ORDER], short * 2,
         "(a) Ostovar patterns, mean PI (6 cases per cell)", seps=(3.5,))
    for x, lab in ((1.5, "Size 3"), (5.5, "Size 5")):
        a1.text(x, -0.62, lab, ha="center", va="bottom", fontsize=7.5, color=MUTED)
    counts = {g: sum(r["group"] == g for r in data[("cdlg", "glm")][0]) for g in CDLG_ORDER}
    mat = matrix(("cdlg",), CDLG_ORDER)
    draw(a2, mat, [f"{CDLG_LABEL[g]} ({counts[g]})" for g in CDLG_ORDER], short,
         "(b) CDLG operation classes, mean PI")
    save(fig, "fig_v2_pattern_heatmap", rows)


def fig_multiperspective() -> None:
    rows = []
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.16, 2.2), gridspec_kw={"width_ratios": [1, 1]})
    fig.subplots_adjust(left=0.065, right=0.995, top=0.86, bottom=0.25, wspace=0.18)
    width = 0.2

    def bars(ax, metric, groups, sources, title, xlabels, set_name):
        for j, (m, label, color) in enumerate(METHODS):
            src = sources.get(m)
            offset = (j - 1.5) * width
            for i, g in enumerate(groups):
                if src is None:
                    ax.text(i + offset, 0.02, "n/a", rotation=90, ha="center", va="bottom", fontsize=6,
                            color=MUTED)
                    continue
                vals = src(g)
                v = mean(vals)
                lo, hi = boot_ci(vals, None)
                rows.append({"set": set_name, "group": g, "method": label, "metric": metric,
                             "value": round(v, 4), "lo": round(lo, 4), "hi": round(hi, 4), "n_cases": len(vals)})
                ax.bar(i + offset, v, width=width * 0.92, color=color, edgecolor="none")
                if hi > lo:
                    ax.errorbar(i + offset, v, yerr=[[v - lo], [hi - v]], fmt="none", ecolor=INK,
                                elinewidth=0.6, capsize=1.5, capthick=0.6)
                if v == 0:
                    ax.text(i + offset, 0.02, "0", ha="center", va="bottom", fontsize=6, color=MUTED)
        ax.set_xticks(range(len(groups)), xlabels)
        ax.set_ylim(0, 1.05)
        ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0], ["0", ".25", ".50", ".75", "1"])
        ax.set_title(title, loc="left", pad=4)
        style_axis(ax)

    # E4a: time detected per type (LLM: 3-run case means)
    def llm(model, set_name, metric):
        runs = llm_rows(model)
        def get(g):
            sel = [[r for r in run if r["set"] == set_name and r["kind"] == "drift" and r["type"] == g]
                   for run in runs]
            pc = defaultdict(list)
            for run in sel:
                for r in run:
                    pc[r["case_id"]].append(num(r[metric]))
            return [mean(v) for v in pc.values()]
        return get

    def rule(set_name, metric):
        run = rule_rows()[0]
        return lambda g: [num(r[metric]) for r in run if r["set"] == set_name and r["kind"] == "drift"
                          and r["type"] == g]

    pd = [r for r in read(E4A_PD) if r["split"] == "evaluation"]
    e4a = {"glm": llm("glm-5.3-flash", "e4a", "time_detected"), "ds": llm("deepseek-v4-flash", "e4a", "time_detected"),
           # rule-based interpreter with the pre-registered timing rule R09_TWAIT (rule_time_e4a.py)
           "rule": lambda g: [num(r["time_detected"]) for r in read(ROOT / "results" / "p5_stats" / "rule_time_e4a.csv")
                              if r["type"] == g],
           "pd": lambda g: [num(r["time_detected"]) for r in pd if r["type"] == g]}
    bars(a1, "time_detected", ["T_SLOW", "T_FAST", "M"], e4a,
         "(a) Ostovar-Time: timing change detected (26 per type)", ["Slower", "Faster", "Mixed (CF + time)"], "e4a")
    e4b = {"glm": llm("glm-5.3-flash", "e4b", "target_claimed"), "ds": llm("deepseek-v4-flash", "e4b", "target_claimed"),
           "rule": rule("e4b", "target_claimed"), "pd": None}
    bars(a2, "target_claimed", ["R1_REASSIGN", "R2_CONSOLIDATE", "R4_SHRINK"], e4b,
         "(b) BPI17-Resource: target activity claimed (10 per type)", ["Reassignment", "Handover", "Concentration"], "e4b")
    a1.set_ylabel("Share of changes")
    fig.legend([Patch(facecolor=c) for _, _, c in METHODS], [l for _, l, _ in METHODS], loc="lower center",
               ncol=4, frameon=False, bbox_to_anchor=(0.53, 0.0), handlelength=1.2, columnspacing=1.6)
    save(fig, "fig_v2_multiperspective", rows)


ABLATIONS = [  # (metric group, set, metric, method, label)
    ("Ready to use, Ostovar size 3", "ostovar3 drift", "RTU", "e3_noselect", "No qualification"),
    ("Ready to use, Ostovar size 3", "ostovar3 drift", "RTU", "e3b_v2en", "No reading rules"),
    ("Ready to use, Ostovar size 3", "ostovar3 drift", "RTU", "e5_no_occ", "Without OCC"),
    ("Ready to use, Ostovar size 3", "ostovar3 drift", "RTU", "e5_no_dir", "Without DIR"),
    ("Ready to use, Ostovar size 3", "ostovar3 drift", "RTU", "e5_no_pos", "Without POS"),
    ("Ready to use, Ostovar size 3", "ostovar3 drift", "RTU", "e5_no_rel", "Without REL"),
    ("Ready to use, Ostovar size 3", "ostovar3 drift", "RTU", "e5_no_lag", "Without LAG"),
    ("Ready to use, Ostovar size 3", "ostovar3 drift", "RTU", "e9_shuffle", "Shuffled evidence order"),
    ("Overclaim, Ostovar 3 (↓ better)", "ostovar3 drift", "overclaim", "e3_noselect", "No qualification"),
    ("Overclaim, Ostovar 3 (↓ better)", "ostovar3 drift", "overclaim", "e3b_v2en", "No reading rules"),
    ("Ready to use, CDLG", "cdlg roles", "RTU", "e3_noselect", "No qualification"),
    ("Ready to use, CDLG", "cdlg roles", "RTU", "e3_full", "No localization, no qualification"),
    ("Ready to use, CDLG", "cdlg roles", "RTU", "e9_shuffle", "Shuffled evidence order"),
    ("Abstention on no-change pairs", "null_ostovar3 null", "insufficient", "e3_noselect", "No qualification, Ostovar 3"),
    ("Abstention on no-change pairs", "null_cdlg null", "insufficient", "e3_noselect", "No qualification, CDLG"),
    ("Abstention on no-change pairs", "null_cdlg null", "insufficient", "e3_full", "No loc., no qual., CDLG"),
    ("Abstention on no-change pairs", "null_ostovar3 null", "insufficient", "e3b_v2en", "No reading rules, Ostovar 3"),
    ("Timing detected, Ostovar-Time", "e4a drift", "time_detected", "e5_no_time", "Mixed, without timing family"),
    ("Timing detected, Ostovar-Time", "e4a drift", "time_detected", "e5_no_cf", "Mixed, without control-flow families"),
    ("Target claimed, BPI17-Resource", "e4b drift", "target_claimed", "e8_labels", "Original activity names"),
]


# Overview of the ablations: one row per component, three outcomes, every set on which the component was ablated.
# Values are the BENEFIT of the component: full pipeline minus variant (for additional claims: variant minus full),
# so that a point to the right means that removing the component makes the result worse.
ABL_ROWS = [("qual", "Qualification (Stage 2)"), ("locqual", "Localization and qualification"),
            ("rules", "Reading rules of the prompt"), ("occ", "OCC family"), ("dir", "DIR family"),
            ("pos", "POS family"), ("rel", "REL family"), ("lag", "LAG family"),
            ("time", "Timing family (mixed changes)"), ("cf", "Control-flow families (mixed)"),
            ("anon", "Anonymous activity codes"), ("order", "Fixed evidence order")]
ABL_SETS = [("ostovar3", "Ostovar 3", "#005580", "o"), ("cdlg", "CDLG", "#E69F00", "s"),
            ("e4a", "Ostovar-Time", "#56B4E9", "^"), ("e4b", "BPI17-Resource", "#7F7F7F", "D")]
# (panel, row, set key, experiment, summary set, metric, sign); summary diff = variant - full
ABL_ITEMS = [
    (0, "qual", "ostovar3", "e3_noselect", "ostovar3 drift", "RTU", -1),
    (0, "qual", "cdlg", "e3_noselect", "cdlg roles", "RTU", -1),
    (0, "locqual", "cdlg", "e3_full", "cdlg roles", "RTU", -1),
    (0, "rules", "ostovar3", "e3b_v2en", "ostovar3 drift", "RTU", -1),
    (0, "occ", "ostovar3", "e5_no_occ", "ostovar3 drift", "RTU", -1),
    (0, "dir", "ostovar3", "e5_no_dir", "ostovar3 drift", "RTU", -1),
    (0, "pos", "ostovar3", "e5_no_pos", "ostovar3 drift", "RTU", -1),
    (0, "rel", "ostovar3", "e5_no_rel", "ostovar3 drift", "RTU", -1),
    (0, "lag", "ostovar3", "e5_no_lag", "ostovar3 drift", "RTU", -1),
    (0, "time", "e4a", "e5_no_time", "e4a drift", "time_detected", -1),
    (0, "cf", "e4a", "e5_no_cf", "e4a drift", "time_detected", -1),
    (0, "anon", "e4b", "e8_labels", "e4b drift", "target_claimed", -1),
    (0, "order", "ostovar3", "e9_shuffle", "ostovar3 drift", "RTU", -1),
    (0, "order", "cdlg", "e9_shuffle", "cdlg roles", "RTU", -1),
    (1, "qual", "ostovar3", "e3_noselect", "ostovar3 drift", "overclaim", 1),
    (1, "rules", "ostovar3", "e3b_v2en", "ostovar3 drift", "overclaim", 1),
    (1, "occ", "ostovar3", "e5_no_occ", "ostovar3 drift", "overclaim", 1),
    (1, "dir", "ostovar3", "e5_no_dir", "ostovar3 drift", "overclaim", 1),
    (1, "pos", "ostovar3", "e5_no_pos", "ostovar3 drift", "overclaim", 1),
    (1, "rel", "ostovar3", "e5_no_rel", "ostovar3 drift", "overclaim", 1),
    (1, "lag", "ostovar3", "e5_no_lag", "ostovar3 drift", "overclaim", 1),
    (1, "order", "ostovar3", "e9_shuffle", "ostovar3 drift", "overclaim", 1),
    (1, "qual", "cdlg", "e3_noselect", "cdlg roles", "overclaim", 1),
    (1, "locqual", "cdlg", "e3_full", "cdlg roles", "overclaim", 1),
    (1, "order", "cdlg", "e9_shuffle", "cdlg roles", "overclaim", 1),
    (2, "qual", "ostovar3", "e3_noselect", "null_ostovar3 null", "insufficient", -1),
    (2, "qual", "cdlg", "e3_noselect", "null_cdlg null", "insufficient", -1),
    (2, "locqual", "cdlg", "e3_full", "null_cdlg null", "insufficient", -1),
    (2, "rules", "ostovar3", "e3b_v2en", "null_ostovar3 null", "insufficient", -1),
]
ABL_PANELS = ["(a) Correct reconstruction", "(b) Fewer additional claims", "(c) Abstention without a change"]


def pooled_benefit(exp: str, pairs: list[tuple[str, str, bool]], metric: str) -> tuple[float, float, float, int]:
    """Benefit (full minus variant) pooled over the cases of several sets, case bootstrap as in aggregate_runs."""
    import random
    from aggregate_runs import GLM, RUNS, p2_scores, p3_scores, per_case
    full, var = [{} for _ in RUNS], [{} for _ in RUNS]
    ids = []
    for set_name, kind, roles in pairs:
        for k, run in enumerate(RUNS):
            a, b = p2_scores(GLM, run, roles=roles), p3_scores(exp, run, roles=roles)
            keep = (lambda r: True) if roles else (lambda r: r["set"] == set_name and r["kind"] == kind)
            full[k].update({c: r for c, r in a.items() if keep(r)})
            var[k].update({c: r for c, r in b.items() if keep(r)})
        ids += [c for c in full[0] if c not in ids]
    pa, pb = per_case(full, ids, metric), per_case(var, ids, metric)
    common = [c for c in ids if c in pa and c in pb]
    diffs = [pa[c] - pb[c] for c in common]
    lo, hi = boot_ci(diffs, random.Random(0))
    return mean(diffs), lo, hi, len(common)


ABL_POOLED = [  # (panel, row, experiment, [(set, kind, roles)], metric)
    (0, "qual", "e3_noselect", [("ostovar3", "drift", False), ("cdlg", "drift", True)], "RTU"),
    (0, "order", "e9_shuffle", [("ostovar3", "drift", False), ("cdlg", "drift", True)], "RTU"),
    (1, "qual", "e3_noselect", [("ostovar3", "drift", False), ("cdlg", "drift", True)], "overclaim"),
    (2, "qual", "e3_noselect", [("null_ostovar3", "null", False), ("null_cdlg", "null", False)], "insufficient"),
]


def fig_ablation_forest() -> None:
    summary = {(r["method"], r["set"], r["metric"]): r for r in read(SUMMARY) if r["part"] == "P3"}
    ypos = {key: i for i, (key, _) in enumerate(ABL_ROWS)}
    offs = {"ostovar3": -0.22, "cdlg": 0.0, "e4a": 0.0, "e4b": 0.0}
    fig, axes = plt.subplots(1, 3, figsize=(7.16, 3.35), sharey=True,
                             gridspec_kw={"width_ratios": [1.35, 1.0, 1.0], "wspace": 0.16})
    fig.subplots_adjust(left=0.205, right=0.995, top=0.90, bottom=0.215)
    rows = []
    for panel, row, setkey, exp, sname, metric, sign in ABL_ITEMS:
        r = summary.get((exp, sname, metric))
        if r is None:
            print(f"missing P3 row {exp} {sname} {metric}; skipped")
            continue
        d, lo, hi = sign * float(r["diff"]), sign * float(r["lo"]), sign * float(r["hi"])
        lo, hi = min(lo, hi), max(lo, hi)
        sig = lo > 0 or hi < 0
        _, _, color, marker = next(x for x in ABL_SETS if x[0] == setkey)
        y = ypos[row] + (offs[setkey] if setkey in ("ostovar3", "cdlg") and row in ("qual", "order") else 0)
        ax = axes[panel]
        ax.plot([lo, hi], [y, y], color=color, linewidth=1.1, solid_capstyle="butt", alpha=1 if sig else 0.55)
        ax.plot(d, y, marker, markersize=4.2, color=color if sig else "white", markeredgecolor=color,
                markeredgewidth=0.9)
        rows.append({"panel": ABL_PANELS[panel], "component": dict(ABL_ROWS)[row], "set": setkey, "experiment": exp,
                     "metric": metric, "benefit": round(d, 4), "lo": round(lo, 4), "hi": round(hi, 4), "n": r["n"]})
    for panel, row, exp, pairs, metric in ABL_POOLED:
        d, lo, hi, n = pooled_benefit(exp, pairs, metric)
        if panel == 1:  # additional claims: benefit = variant minus full
            d, lo, hi = -d, -hi, -lo
        y = ypos[row] + 0.24
        ax = axes[panel]
        ax.plot([lo, hi], [y, y], color=INK, linewidth=1.1, solid_capstyle="butt")
        sig = lo > 0 or hi < 0
        ax.plot(d, y, "D", markersize=3.6, color=INK if sig else "white", markeredgecolor=INK, markeredgewidth=0.9)
        rows.append({"panel": ABL_PANELS[panel], "component": dict(ABL_ROWS)[row], "set": "pooled",
                     "experiment": exp, "metric": metric, "benefit": round(d, 4), "lo": round(lo, 4),
                     "hi": round(hi, 4), "n": n})
    axes[0].text(0.24, ypos["locqual"], "Ostovar: not feasible\n(prompt > context window)",
                 fontsize=6.6, color=MUTED, va="center", ha="left", style="italic", linespacing=0.95)
    lims = [(-0.3, 1.04), (-0.3, 0.62), (-0.3, 0.84)]
    for ax, title, (a, b) in zip(axes, ABL_PANELS, lims):
        ax.axvline(0, color=INK, linewidth=0.6)
        ax.set_xlim(a, b)
        ax.set_title(title, loc="left")
        style_axis(ax, grid_axis="x")
        ax.spines["left"].set_visible(False)
        ax.tick_params(axis="y", length=0)
        ticks = [t / 4 for t in range(-1, int(b * 4) + 1)]
        ax.set_xticks(ticks, ["0" if t == 0 else "+1" if t == 1 else f"{t:+.2f}".replace("0.", ".").replace("-", "−")
                           for t in ticks])
    axes[0].set_yticks(range(len(ABL_ROWS)), [lab for _, lab in ABL_ROWS])
    axes[0].set_ylim(len(ABL_ROWS) - 0.5, -0.6)
    for sep in (2.5, 7.5, 9.5):
        for ax in axes:
            ax.axhline(sep, color=GRID, linewidth=0.6)
    fig.text(0.6, 0.085, "Benefit of the component: full pipeline minus variant (95% CI); right = component helps",
             ha="center", fontsize=8)
    handles = [plt.Line2D([], [], marker=m, linestyle="", color=c, markeredgecolor=c, markersize=4.6, label=l)
               for _, l, c, m in ABL_SETS]
    handles.append(plt.Line2D([], [], marker="D", linestyle="", color=INK, markersize=4, label="Pooled over sets"))
    handles.append(plt.Line2D([], [], marker="o", linestyle="", color="white", markeredgecolor=MUTED,
                              markersize=4.6, label="Interval includes 0"))
    fig.legend(handles=handles, loc="lower center", ncol=6, frameon=False, bbox_to_anchor=(0.6, -0.005),
               handletextpad=0.3, columnspacing=1.2)
    save(fig, "fig_v2_ablation_forest", rows)



def fig_open_weight() -> None:
    """E6: mean PI per Ostovar size-3 pattern for GLM, DeepSeek and Qwen, run 1 of each on the same 78 changes."""
    models = [("GLM", "glm-5.3-flash"), ("DeepSeek", "deepseek-v4-flash"), ("Qwen 27B", "qwen3.8-27b-uncensored")]
    runs = {}
    for label, model in models:
        rows_ = [r for r in read(P2 / f"scores_{PROMPT}_{model}_run1.csv") if r["set"] == "ostovar3" and r["kind"] == "drift"]
        assert len(rows_) == 78, (model, len(rows_))
        runs[label] = rows_
    cmap = LinearSegmentedColormap.from_list("pi", ["#FFFFFF", "#C6DDEC", "#3F7FA6", "#003F60"])
    mat, out = [], []
    for g in OSTOVAR_ORDER:
        line = []
        for label, _ in models:
            v = mean(num(r["PI"]) for r in runs[label] if r["type"] == g)
            line.append(v)
            out.append({"row": g, "model": label, "value": round(v, 4), "n": 6})
        mat.append(line)
    summary = [("Mean PI", "PI"), ("RTU", "RTU")]
    for name, metric in summary:
        line = [mean(num(r[metric]) for r in runs[label]) for label, _ in models]
        mat.append(line)
        out += [{"row": name, "model": label, "value": round(v, 4), "n": 78} for (label, _), v in zip(models, line)]
    labels = [spaced(p) for p in OSTOVAR_ORDER] + [n for n, _ in summary]
    nr, nc = len(mat), len(models)
    fig, ax = plt.subplots(figsize=(3.5, 3.7))
    fig.subplots_adjust(left=0.40, right=0.98, top=0.93, bottom=0.04)
    ax.pcolormesh([j - 0.5 for j in range(nc + 1)], [i - 0.5 for i in range(nr + 1)], mat, cmap=cmap, vmin=0, vmax=1,
                  shading="flat")
    ax.set_xlim(-0.5, nc - 0.5)
    ax.set_ylim(nr - 0.5, -0.5)
    for i, line in enumerate(mat):
        for j, v in enumerate(line):
            txt = "1" if v >= 0.995 else "0" if v < 0.005 else f"{v:.2f}"[1:]
            ax.text(j, i, txt, ha="center", va="center", fontsize=6.8, color="white" if v >= 0.70 else INK,
                    fontweight="bold" if i >= len(OSTOVAR_ORDER) else "normal")
    ax.set_yticks(range(nr), labels)
    ax.xaxis.tick_top()
    ax.set_xticks(range(nc), [m for m, _ in models])
    ax.tick_params(length=0)
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_xticks([j - 0.5 for j in range(1, nc)], minor=True)
    ax.set_yticks([i - 0.5 for i in range(1, nr)], minor=True)
    ax.grid(which="minor", color="white", linewidth=1.2)
    ax.tick_params(which="minor", length=0)
    ax.axhline(len(OSTOVAR_ORDER) - 0.5, color=INK, linewidth=0.8)
    save(fig, "fig_v2_open_weight", out)


def save(fig, name: str, rows: list[dict]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / f"{name}.pdf")
    fig.savefig(OUT / f"{name}.png", dpi=220)
    plt.close(fig)
    write(OUT / f"{name}.csv", rows)
    print(f"-> {OUT / name}.pdf")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--copy", action="store_true", help="copy the PDFs to the LaTeX figures folder")
    args = parser.parse_args()
    with plt.rc_context(STYLE):
        data = case_records()
        fig_outcome_profile(data)
        fig_pattern_heatmap(data)
        fig_multiperspective()
        fig_ablation_forest()
        fig_open_weight()
    if args.copy:
        for p in OUT.glob("fig_v2_*.pdf"):
            shutil.copy2(p, LATEX / p.name)
        print(f"copied to {LATEX}")


if __name__ == "__main__":
    main()
