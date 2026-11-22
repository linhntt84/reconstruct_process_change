#!/usr/bin/env python3
"""E4a, rule-based interpreter with the timing rule R09_TWAIT (pre-registered in e4_multiperspective/docs/
NHAT_KY_E4_VI.md, variant v1_time), applied to the same P2 evidence documents as the LLM. No API calls.

R09_TWAIT: when the time family passes the per-family Poisson screening (P(>= n items | lambda) < 0.01, lambda =
items expected without change), every T_WAIT item on a pair A -> B yields the claim "the time into B
increased/decreased" (sign of the median change). Scored deterministically, as ProDrift: time_detected = the target
activity is claimed; direction_ok = and with the injected direction; on no-change pairs, time_false_claim = any
timing claim. Output: results/p5_stats/rule_time_e4a.md
"""
import csv
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from aggregate_runs import boot_ci  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
P2 = ROOT / "results" / "p2_main"
CASES = ROOT / "e4_multiperspective" / "results" / "e4a_time_injection" / "cases.csv"


def tail(n, lam):
    return 1.0 - sum(math.exp(-lam) * lam ** i / math.factorial(i) for i in range(n))


def main():
    rows = []
    for c in csv.DictReader(CASES.open(encoding="utf-8")):
        path = P2 / "evidence" / f"{c['case_id']}.json"
        if c["split"] != "evaluation" or not path.exists():
            continue
        doc = json.loads(path.read_text())
        lm = json.loads((P2 / "audit" / f"{c['case_id']}.json").read_text())["label_map"]
        tw = [e for e in doc["evidence"] if e["indicator"] == "T_WAIT"]
        lam = doc["screening"]["by_family"]["time"]["items_expected_without_change"]
        claims = {}
        if tw and tail(len(tw), lam) < 0.01:
            for e in tw:
                b = e["analysis_unit"]["values"][1]
                up = e["components_after"]["median_hours"] > e["components_before"]["median_hours"]
                claims.setdefault(b, set()).add("increase" if up else "decrease")
        tgt = lm.get(c["time_target"]) if c["time_target"] else None
        rows.append({"case_id": c["case_id"], "type": c["type"], "n_twait": len(tw), "lambda": lam,
                     "time_detected": float(bool(tgt) and tgt in claims),
                     "direction_ok": float(bool(tgt) and claims.get(tgt) == {c["time_direction"]}),
                     "time_false_claim": float(c["type"] == "N" and bool(claims))})
    md = ["# E4a: rule-based interpreter with R09_TWAIT (evaluation set, P2 evidence)", "",
          "| Type | n | time detected [95% CI] | direction correct | false timing claim |", "|---|---|---|---|---|"]
    for t in ("T_SLOW", "T_FAST", "M", "all drift", "N"):
        rs = [r for r in rows if (r["type"] != "N" if t == "all drift" else r["type"] == t)]
        det = [r["time_detected"] for r in rs]
        lo, hi = boot_ci(det, None)
        md.append(f"| {t} | {len(rs)} | {sum(det) / len(rs):.3f} [{lo:.3f}, {hi:.3f}] | "
                  f"{sum(r['direction_ok'] for r in rs) / len(rs):.3f} | "
                  f"{sum(r['time_false_claim'] for r in rs):.0f} |")
    # paired with the LLMs (3-run case means), as in method_contrasts.py
    from method_contrasts import mcnemar
    md += ["", "| LLM | n | LLM time detected | rule | diff [95% CI] | b / c (majority) | McNemar p |",
           "|---|---|---|---|---|---|---|"]
    rule = {r["case_id"]: r for r in rows if r["type"] != "N"}
    for name, model in (("GLM", "glm-5.3-flash"), ("DeepSeek", "deepseek-v4-flash")):
        vals = {}
        for k in (1, 2, 3):
            with (P2 / f"scores_INTERPRET_EVIDENCE_V2_EN_R3_MP_CONC_{model}_run{k}.csv").open() as h:
                for r in csv.DictReader(h):
                    if r["case_id"] in rule:
                        vals.setdefault(r["case_id"], []).append(float(r["time_detected"]))
        ids = sorted(vals)
        diffs = [sum(vals[i]) / 3 - rule[i]["time_detected"] for i in ids]
        lo, hi = boot_ci(diffs, None)
        maj = {i: sum(vals[i]) >= 2 for i in ids}
        b = int(sum(maj[i] and not rule[i]["time_detected"] for i in ids))
        c = int(sum(bool(not maj[i] and rule[i]["time_detected"]) for i in ids))
        md.append(f"| {name} | {len(ids)} | {sum(sum(vals[i]) / 3 for i in ids) / len(ids):.3f} | "
                  f"{sum(rule[i]['time_detected'] for i in ids) / len(ids):.3f} | {sum(diffs) / len(ids):+.3f} "
                  f"[{lo:+.3f}, {hi:+.3f}] | {b} / {c} | {mcnemar(b, c):.2g} |")
    with (ROOT / "results" / "p5_stats" / "rule_time_e4a.csv").open("w", encoding="utf-8", newline="") as h:
        w = csv.DictWriter(h, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    missed = [r for r in rows if r["type"] != "N" and not r["time_detected"]]
    md += ["", f"Missed drift cases: {len(missed)}; T_WAIT items in them: "
           f"{sorted((r['n_twait'], round(r['lambda'], 3)) for r in missed)}"]
    (ROOT / "results" / "p5_stats" / "rule_time_e4a.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
