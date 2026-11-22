#!/usr/bin/env python3
"""P5: analyses of the LLM step on archived outputs (no API calls). Reviewer points: R4 #3c, R4 #7, R4 minor 2,
R6 #5a, R5 (failures), plus two author checks (secondary claims, false alarms on no-change pairs).

A. API metadata per model and run: dates, endpoint, returned model id, transport, retries, finish reasons, latency,
   tokens (P2, 528 cases per run; Qwen E6 one run).
B. Evidence families in correct vs incorrect reconstructions (Ostovar sizes 3 and 5, GLM and DeepSeek, runs 1-3):
   families present in E* and families cited in the explanation, split by PI = 1 vs PI < 1.
C. Secondary claims outside the reference (overclaim): is each extra activity the unit of a qualified evidence item
   (the claim reports a qualified difference) and is it inside the localized region A*?
D. No-change pairs declared as changed (Ostovar size 3 and 5): evidence counts versus the screening expectation,
   per log, and agreement across models and runs.
Output: results/p5_stats/llm_step_analyses.md
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean, median

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "experiments" / "p2_main"))
from score_p2 import ostovar_references  # noqa: E402

P2 = ROOT / "results" / "p2_main"
OUT = ROOT / "results" / "p5_stats"
PROMPT = "INTERPRET_EVIDENCE_V2_EN_R3_MP_CONC"
MODELS = ("glm-5.3-flash", "deepseek-v4-flash")
RUNS = (1, 2, 3)
FAMS = ("OCC", "DIR", "POS", "REL", "LAG")
ID_RE = re.compile(r"\b(OCC|DIR|POS|REL|LAG|TWAIT|ASSIGN|CONC)(\d{3})\b")


def records(model: str, k: int):
    for p in sorted((P2 / "runs" / PROMPT / model / f"run{k}").glob("*.json")):
        yield json.loads(p.read_text())


def usage(r: dict) -> dict:
    u = r.get("usage") or {}
    if isinstance(u, str):
        try:
            u = json.loads(u.replace("'", '"').replace("None", "null"))
        except json.JSONDecodeError:
            u = {}
    return u


def q(xs, p):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(p * len(xs)))] if xs else float("nan")


def part_a() -> list[str]:
    md = ["## A. API calls: dates, endpoint, model id, latency, tokens", "",
          "| Model | Run | n | Success | Dates (UTC) | Endpoint | Returned model | Transport | Calls with retries | "
          "finish_reason ≠ stop | Latency s median / p90 / max | Prompt tok median | Completion tok median | "
          "Reasoning tok median |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    combos = [(m, k) for m in MODELS for k in RUNS] + [("qwen3.8-27b-uncensored", 1)]
    for m, k in combos:
        rs = list(records(m, k))
        if not rs:
            continue
        ok = [r for r in rs if r.get("status") == "success"]
        dates = sorted(r["started_at_utc"][:10] for r in rs if r.get("started_at_utc"))
        lat = [r["latency_seconds"] for r in ok if r.get("latency_seconds") is not None]
        us = [usage(r) for r in ok]
        pt = [u.get("prompt_tokens") for u in us if u.get("prompt_tokens")]
        ct = [u.get("completion_tokens") for u in us if u.get("completion_tokens")]
        rt = [(u.get("completion_tokens_details") or {}).get("reasoning_tokens") for u in us]
        rt = [x for x in rt if x]
        md.append(f"| {m} | {k} | {len(rs)} | {len(ok)} | {dates[0]} – {dates[-1]} | "
                  f"{', '.join(sorted({r.get('endpoint', '').split('//')[-1].split('/')[0] for r in rs}))} | "
                  f"{', '.join(sorted({str(r.get('response_model')) for r in ok}))} | "
                  f"{', '.join(f'{t} {n}' for t, n in Counter(r.get('transport', 'non-stream') for r in rs).items())} | "
                  f"{sum(bool(r.get('attempt_errors')) for r in rs)} | "
                  f"{sum(r.get('finish_reason') not in ('stop', None) for r in ok)} | "
                  f"{median(lat):.0f} / {q(lat, 0.9):.0f} / {max(lat):.0f} | {median(pt):,.0f} | {median(ct):,.0f} | "
                  + (f"{median(rt):,.0f} (n = {len(rt)}) |" if rt else "not reported |"))
    md += ["", "Run 1 of GLM and DeepSeek used the non-streaming transport for most calls; the API then reports only "
           "total completion tokens (reasoning + text). Calls with retries: at least one failed attempt (e.g. HTTP 524 "
           "at the gateway's 120 s limit) before the recorded outcome.", ""]
    return md


def cited(text: str) -> set:
    return {f"{a}{b}" for a, b in ID_RE.findall(text)}


def part_b(refs) -> list[str]:
    md = ["## B. Evidence families in correct vs incorrect reconstructions (Ostovar 3 + 5, runs 1-3)", "",
          "Available = share of explanations whose E* contains the family; cited = share citing at least one item "
          "of the family; items = mean number of qualified items in E*.", "",
          "| Model | Outcome | n | Items in E* | " + " | ".join(f"{f} avail / cited" for f in FAMS) + " |",
          "|---|---|---|---|" + "---|" * len(FAMS)]
    for m in MODELS:
        groups = defaultdict(list)
        for k in RUNS:
            with (P2 / f"scores_{PROMPT}_{m}_run{k}.csv").open(encoding="utf-8") as handle:
                sc = {r["case_id"]: r for r in csv.DictReader(handle)}
            for r in records(m, k):
                cid = r["case_id"]
                s = sc.get(cid)
                if not s or s["set"] not in ("ostovar3", "ostovar5") or s["kind"] != "drift":
                    continue
                ev = json.loads((P2 / "evidence" / f"{cid}.json").read_text())["evidence"]
                avail = {e["id"].rstrip("0123456789") for e in ev}
                cit = {i.rstrip("0123456789") for i in cited(r.get("text", ""))} if r.get("status") == "success" else set()
                outcome = "PI = 1" if s["PI"] not in ("", "nan") and float(s["PI"]) == 1.0 else "PI < 1"
                groups[outcome].append((len(ev), avail, cit))
        for outcome in ("PI = 1", "PI < 1"):
            g = groups[outcome]
            cells = [f"{mean(f in a for _, a, _ in g):.2f} / {mean(f in c for _, _, c in g):.2f}" for f in FAMS]
            md.append(f"| {m} | {outcome} | {len(g)} | {mean(n for n, _, _ in g):.1f} | " + " | ".join(cells) + " |")
    return md + [""]


def part_c(refs) -> list[str]:
    md = ["## C. Secondary claims outside the reference (Ostovar 3 + 5, runs 1-3)", "",
          "Extra activity = in secondary_activities but neither required nor optional in the reference. In evidence = "
          "the activity is the unit (or one of the two units) of at least one qualified item. In A* = inside the "
          "localized region.", "",
          "| Model | Explanations | With extra activities | Extra activities | In evidence | In A* | In neither |",
          "|---|---|---|---|---|---|---|"]
    for m in MODELS:
        n_expl = n_with = 0
        cnt = Counter()
        for k in RUNS:
            folder = P2 / "extractions_r5" / PROMPT / m / f"run{k}"
            for p in folder.glob("*.json"):
                cid = p.stem
                if cid not in refs:
                    continue
                audit = json.loads((P2 / "audit" / f"{cid}.json").read_text())
                lm = audit["label_map"]
                _, req, opt = refs[cid]
                ref = {lm[a] for a in list(req) + list(opt) if a in lm}
                e = json.loads(p.read_text())["extraction"]
                extra = set(e.get("secondary_activities", [])) - set(e["central_activities"]) - ref
                n_expl += 1
                n_with += bool(extra)
                if not extra:
                    continue
                ev = json.loads((P2 / "evidence" / f"{cid}.json").read_text())["evidence"]
                units = set()
                for it in ev:
                    u = it["analysis_unit"]
                    units |= {u["value"]} if "value" in u else set(u.get("values", []))
                loc = set(audit.get("localized_activities") or [])
                for a in extra:
                    cnt["all"] += 1
                    cnt["ev"] += a in units
                    cnt["loc"] += a in loc
                    cnt["none"] += a not in units and a not in loc
        md.append(f"| {m} | {n_expl} | {n_with} ({n_with / n_expl:.2f}) | {cnt['all']} | "
                  f"{cnt['ev']} ({cnt['ev'] / cnt['all']:.2f}) | {cnt['loc']} ({cnt['loc'] / cnt['all']:.2f}) | "
                  f"{cnt['none']} |")
    return md + [""]


def part_d() -> list[str]:
    with (P2 / "cases.csv").open(encoding="utf-8") as handle:
        cases = {r["case_id"]: r for r in csv.DictReader(handle) if r["set"] in ("null_ostovar3", "null_ostovar5")}
    claims = defaultdict(list)
    for m in MODELS:
        for k in RUNS:
            with (P2 / f"scores_{PROMPT}_{m}_run{k}.csv").open(encoding="utf-8") as handle:
                for r in csv.DictReader(handle):
                    if r["case_id"] in cases:
                        claims[r["case_id"]].append(r["support_level"])
    rule = {}
    path = P2 / "scores_RULE_BASELINE_V2_rule-engine-v1_run1.csv"
    if path.exists():
        with path.open(encoding="utf-8") as handle:
            rule = {r["case_id"]: r["support_level"] for r in csv.DictReader(handle)}
    md = ["## D. No-change pairs declared as changed (Ostovar 3 + 5)", "",
          "Columns: claims = number of the 6 explanations (2 models × 3 runs) that are not 'insufficient'; items = "
          "qualified items; expected = items expected without change (screening).", "",
          "| Set | Log (type) | Claims / 6 | Items | Expected | Items by family | Max observed change | Rule |",
          "|---|---|---|---|---|---|---|---|"]
    rows = []
    for cid, c in cases.items():
        n = sum(lvl != "insufficient" for lvl in claims[cid])
        if not n:
            continue
        doc = json.loads((P2 / "evidence" / f"{cid}.json").read_text())
        fam = Counter(e["id"].rstrip("0123456789") for e in doc["evidence"])
        mx = max((e.get("observed_change", 0) for e in doc["evidence"]), default=0)
        rows.append((c["set"], c["type"], n, len(doc["evidence"]),
                     doc.get("screening", {}).get("items_expected_without_change", ""), dict(fam), mx,
                     rule.get(cid, "")))
    for r in sorted(rows, key=lambda x: (-x[2], x[0])):
        md.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]:.2f} | {r[7]} |")
    total = len(cases)
    md += ["", f"{len(rows)} of {total} no-change pairs have at least one 'changed' conclusion; "
           f"{sum(r[2] == 6 for r in rows)} are declared changed by all six explanations.", ""]
    return md


def main():
    refs = ostovar_references()
    md = ["# P5: analyses of the LLM step (archived outputs, no API calls)", "",
          "Generated by experiments/p5_stats/llm_step_analyses.py.", ""]
    md += part_a() + part_b(refs) + part_c(refs) + part_d()
    (OUT / "llm_step_analyses.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
