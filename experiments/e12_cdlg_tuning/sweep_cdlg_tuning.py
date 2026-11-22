#!/usr/bin/env python3
"""E12: would a CDLG-specific parameter selection change the evidence? (no LLM)

Question (author, 2026-11-18): the frozen v2 parameters were selected on the Ostovar tuning split
(fragment sizes 2 and 4) and applied unchanged to CDLG. Would selecting them on CDLG itself give a
different configuration, and would it raise A* recall / E* coverage on the 99 CDLG evaluation changes?

Tuning pool: the CDLG change episodes that are NOT evaluated (426 episodes in 100 logs, one per log is
evaluated). An episode is used when both windows (w = 200, guard g = 50, as in P2) lie inside the log,
contain no other change transition, and do not overlap the windows of the evaluated episode or of the
evaluation no-change pair of the same log. No-change tuning pairs: one per log, inside a stable segment
(no change transition), outside every evaluation window. The tuning episodes share process models with
the evaluation logs (same 100 logs), so this split is weaker than the Ostovar one; it is used only to
check whether a CDLG-specific selection would differ.

Caches use the E0/P0-B format (sweep_grid_v2.run_pair, permutation reference, strict ties, B = 100), so
experiments/e0_parameter_setting/analyze_grid.py functions apply. Evaluation caches (99 changes, 50
no-change pairs) are computed the same way to compare configurations on the evaluation set.

  python experiments/e12_cdlg_tuning/sweep_cdlg_tuning.py --workers 8
  python experiments/e12_cdlg_tuning/analyze_cdlg_tuning.py
"""
from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import json
import re
import sys
import time
import zipfile
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
for p in ("src", "experiments/e0_parameter_setting", "experiments/p0_evidence_v2", "experiments/e1_prodrift",
          "experiments/p2_main"):
    sys.path.insert(0, str(ROOT / p))

from pcr.paths import REFERENCES, RESULTS  # noqa: E402
from run_prodrift import CDLG  # noqa: E402
from sweep_evidence import seed_for  # noqa: E402

OUT = RESULTS / "e12_cdlg_tuning"
W, G, BS = 200, 50, 100
SPAN = W + G  # distance from the change boundary to the far end of a window


def parse_list(text: str) -> list[str]:
    text = text.strip()[1:-1].strip()
    return [x.strip() for x in text.split(",") if x.strip()] if text else []


def episodes() -> dict[str, list[dict]]:
    """Every change episode of every CDLG log, from the drift:info header."""
    out = {}
    for part in (1, 2):
        with zipfile.ZipFile(CDLG / f"without_noise_part_{part}.zip") as archive:
            for name in archive.namelist():
                head = archive.open(name).read(60000).decode("utf-8", "replace")
                head = head[:head.find("<trace>")]
                blocks = re.split(r'<string key="change_id_\d+" value="info">', head)[1:]
                eps = []
                for block in blocks:
                    get = lambda key: re.search(rf'key="{key}" value="([^"]*)"', block).group(1)  # noqa: E731
                    idx = [int(x) for x in parse_list(get("change_trace_index"))]
                    eps.append({"start": idx[0], "end": idx[-1], "type": get("change_type"),
                                "added": parse_list(get("activities_added")),
                                "deleted": parse_list(get("activities_deleted")),
                                "moved": parse_list(get("activities_moved"))})
                out[name] = eps
    return out


def overlaps(a: tuple[int, int], b: tuple[int, int]) -> bool:
    return a[0] < b[1] and b[0] < a[1]


def build_tasks() -> list[dict]:
    from build_p2_cases import read_cdlg  # noqa: F401  (imported in workers)
    with (REFERENCES / "cdlg_case_ground_truth_one_per_log100_v1.csv").open(encoding="utf-8-sig") as handle:
        evaluated = {r["case_id"]: r for r in csv.DictReader(handle)}
    eval_by_log = {r["log_name"]: (int(r["change_trace_start"]), int(r["change_trace_end"]))
                   for r in evaluated.values()}
    with (RESULTS / "p2_main" / "cases.csv").open(encoding="utf-8") as handle:
        p2 = list(csv.DictReader(handle))
    null_eval = {r["source"]: int(r["start"]) for r in p2 if r["set"] == "null_cdlg"}
    with (REFERENCES / "cdlg_gold_standard.csv").open(encoding="utf-8-sig") as handle:
        sizes = {r["log_name"]: int(float(r["log_size"])) for r in csv.DictReader(handle)}
    tasks = []
    for log, eps in sorted(episodes().items()):
        n = sizes[log]
        es, ee = eval_by_log[log]
        blocked = [(es - SPAN, ee + SPAN)]
        if log in null_eval:  # evaluation no-change pair: L- = [a - 250, a - 50), L+ = [a + 50, a + 250)
            a = null_eval[log]
            blocked.append((a - SPAN, a + SPAN))
        transitions = [(e["start"], e["end"] + 1) for e in eps]
        for k, e in enumerate(eps):
            if (e["start"], e["end"]) == (es, ee):
                continue
            win = (e["start"] - SPAN, e["end"] + SPAN)
            if win[0] < 0 or win[1] > n:
                continue
            before, after = (e["start"] - SPAN, e["start"] - G), (e["end"] + G, e["end"] + SPAN)
            others = [t for j, t in enumerate(transitions) if j != k]
            if any(overlaps(before, t) or overlaps(after, t) for t in others):
                continue
            if any(overlaps(win, b) for b in blocked):
                continue
            affected = sorted(set(e["added"] + e["deleted"] + e["moved"]))
            cid = "cdlgtune_" + hashlib.sha256(f"{log}::{k}".encode()).hexdigest()[:12]
            tasks.append({"id": cid, "kind": "drift", "split": "tuning", "log": log, "start": e["start"],
                          "end": e["end"], "meta": {"log": log, "episode": k, "change_type": e["type"],
                                                    "affected_activities_real": json.dumps(affected),
                                                    "noise_pct": "0"}})
        # one no-change tuning pair per log: L- = [a - 250, a - 50), L+ = [a + 50, a + 250) in a stable segment
        bounds = sorted(transitions)
        segments, cursor = [], 0
        for s, t in bounds:
            segments.append((cursor, s))
            cursor = max(cursor, t)
        segments.append((cursor, n))
        for s, t in sorted(segments, key=lambda x: -(x[1] - x[0])):
            if t - s < 2 * SPAN:
                continue
            a = s + SPAN
            win = (a - SPAN, a + SPAN)
            while win[1] <= t and any(overlaps(win, b) for b in blocked):
                a += 25
                win = (a - SPAN, a + SPAN)
            if win[1] <= t:
                tasks.append({"id": "cdlgtune_null_" + hashlib.sha256(log.encode()).hexdigest()[:12],
                              "kind": "null", "split": "tuning", "log": log, "start": a, "end": a,
                              "meta": {"log": log, "noise_pct": "0"}})
                break
    # evaluation caches (same computation), for comparing configurations on the evaluated cases
    for cid, r in evaluated.items():
        affected = sorted(set(json.loads(r["activities_added_real"]) + json.loads(r["activities_deleted_real"])
                              + json.loads(r["activities_moved_real"])))
        tasks.append({"id": cid, "kind": "drift", "split": "evaluation", "log": r["log_name"],
                      "start": int(r["change_trace_start"]), "end": int(r["change_trace_end"]),
                      "meta": {"log": r["log_name"], "affected_activities_real": json.dumps(affected),
                               "noise_pct": "0"}})
    for row in p2:
        if row["set"] == "null_cdlg":
            a = int(row["start"])
            tasks.append({"id": row["case_id"], "kind": "null", "split": "evaluation", "log": row["source"],
                          "start": a, "end": a, "meta": {"log": row["source"], "noise_pct": "0"}})
    return tasks


def job(task: dict) -> tuple[str, str]:
    target = OUT / "cache" / task["split"] / f"{task['id']}.json"
    if target.exists():
        return task["id"], "cached"
    from build_p2_cases import read_cdlg
    from sweep_grid_v2 import run_pair
    started = time.perf_counter()
    traces = read_cdlg(task["log"])
    before = traces[task["start"] - G - W:task["start"] - G]
    after = traces[task["end"] + G:task["end"] + G + W]
    if len(before) != W or len(after) != W:
        return task["id"], f"skipped windows {len(before)}/{len(after)}"
    result = run_pair(before, after, BS, seed_for(task["id"]), "permutation")
    result.update({k: task[k] for k in ("id", "kind", "meta")})
    result["elapsed_seconds"] = round(time.perf_counter() - started, 2)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, ensure_ascii=False))
    return task["id"], f"done {result['elapsed_seconds']}s"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--list-only", action="store_true")
    args = parser.parse_args()
    tasks = build_tasks()
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "tasks.json").write_text(json.dumps(tasks, indent=1))
    count = {}
    for t in tasks:
        count[(t["split"], t["kind"])] = count.get((t["split"], t["kind"]), 0) + 1
    print({f"{a}/{b}": v for (a, b), v in sorted(count.items())},
          "tuning logs:", len({t["log"] for t in tasks if t["split"] == "tuning" and t["kind"] == "drift"}))
    if args.list_only:
        return
    started = time.perf_counter()
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(job, t) for t in tasks]
        for done, future in enumerate(as_completed(futures), 1):
            cid, status = future.result()
            print(f"[{done}/{len(tasks)}] {cid} {status}", flush=True)
    print(f"wall {time.perf_counter() - started:.0f}s")


if __name__ == "__main__":
    main()
