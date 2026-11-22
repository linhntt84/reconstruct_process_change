#!/usr/bin/env python3
"""E1 (matched input): build, for every evaluated drift, a log that contains only the two
windows the pipeline receives, so ProDrift and pipeline v2 see the same traces.

Windows as in PIPELINE_V2_SPEC (section 1): w = 200 traces, guard g = 50,
  L- = [cp - g - w, cp - g),  L+ = [cp_end + g, cp_end + g + w)
with cp_end = cp for sudden changes and the reported end point for gradual ones.
The window log is L- followed by L+ (original trace order and timestamps), so its only
change lies at the junction (trace position w).

Ostovar: cp = 900 / 1900 for drifts 1 / 2. CDLG: the 100 evaluated cases of
data/references/cdlg_case_ground_truth_one_per_log100_v1.csv (change_trace_start/end).
Output: results/e1_prodrift/window_logs/<group>/<case>.<mxml.gz|xes> and an index CSV.

ProDrift cannot characterize such short logs (it needs long streams after a detection), so
--cdlg-isolated builds the variant used for E1 on CDLG: for each evaluated case, the source
log cut to the segment that contains only this change,
  [previous change point + g, next change point - g)
(change points from the official gold_standard.csv; log start/end when there is none).
Every such segment keeps at least 900 traces before and after the change.
"""
from __future__ import annotations

import argparse
import copy
import csv
import gzip
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(HERE))
from pcr.paths import OSTOVAR_FULL, REFERENCES, RESULTS  # noqa: E402
from run_prodrift import CDLG  # noqa: E402

W, G = 200, 50
OUT = RESULTS / "e1_prodrift" / "window_logs"
PATTERNS = ["ConditionalMove", "ConditionalRemoval", "ConditionalToSequence", "Frequency", "Loop",
            "ParallelMove", "ParallelRemoval", "ParallelToSequence", "SerialMove", "SerialRemoval",
            "Skip", "Substitute", "Swap"]


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def windows(start: int, end: int) -> list[int]:
    return list(range(start - G - W, start - G)) + list(range(end + G, end + G + W))


def subset(root: ET.Element, trace_tag: str, keep: list[int]) -> ET.Element:
    """Copy of the log keeping only the traces at the given file positions (0-based)."""
    parent = root if trace_tag == "trace" else next(e for e in root.iter() if local(e.tag) == "Process")
    traces = [e for e in parent if local(e.tag) == trace_tag]
    keep_set = set(keep)
    if max(keep) >= len(traces):
        raise ValueError(f"window beyond log end ({max(keep)} >= {len(traces)})")
    new_root = copy.deepcopy(root)
    new_parent = new_root if trace_tag == "trace" else next(e for e in new_root.iter() if local(e.tag) == "Process")
    for i, elem in enumerate([e for e in new_parent if local(e.tag) == trace_tag]):
        if i not in keep_set:
            new_parent.remove(elem)
    return new_root


def build_cdlg_isolated(limit: int = 0) -> None:
    import ast
    with (REFERENCES / "cdlg_gold_standard.csv").open(encoding="utf-8-sig") as handle:
        gold = {r["log_name"]: r for r in csv.DictReader(handle)}
    with (REFERENCES / "cdlg_case_ground_truth_one_per_log100_v1.csv").open(encoding="utf-8-sig") as handle:
        cases = list(csv.DictReader(handle))
    index = []
    for n, case in enumerate(cases):
        if limit and n >= limit:
            break
        log = case["log_name"]
        cps = ast.literal_eval(gold[log]["change_point"])
        start, end = int(case["change_trace_start"]), int(case["change_trace_end"])
        prev = max((p for p in cps if p < start), default=None)
        nxt = min((p for p in cps if p > end), default=None)
        number = int(log.split("_")[1])
        part = CDLG / f"without_noise_part_{1 if number <= 50 else 2}.zip"
        with zipfile.ZipFile(part) as archive, archive.open(log) as handle:
            root = ET.parse(handle).getroot()
        n_traces = sum(1 for e in root if local(e.tag) == "trace")
        lo = prev + G if prev is not None else 0
        hi = nxt - G if nxt is not None else n_traces
        target = OUT / "cdlg_isolated" / f"{case['case_id']}.xes"
        target.parent.mkdir(parents=True, exist_ok=True)
        ET.ElementTree(subset(root, "trace", list(range(lo, hi)))).write(target, encoding="utf-8",
                                                                       xml_declaration=True)
        index.append({"case": case["case_id"], "source": log, "start": start, "end": end,
                      "segment_start": lo, "segment_end": hi, "path": str(target.relative_to(ROOT))})
    with (OUT / "index_cdlg_isolated.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(index[0]))
        writer.writeheader()
        writer.writerows(index)
    print(f"{len(index)} isolated CDLG logs -> {OUT / 'cdlg_isolated'}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sizes", type=int, nargs="+", default=[2, 3, 4, 5])
    parser.add_argument("--cdlg", action="store_true", help="also build the 100 CDLG window logs")
    parser.add_argument("--cdlg-isolated", action="store_true",
                        help="build the isolated single-change CDLG logs (index_cdlg_isolated.csv)")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()
    ET.register_namespace("", "http://www.xes-standard.org/")
    if args.cdlg_isolated:
        build_cdlg_isolated(args.limit)
        return
    index = []
    jobs = 0
    for size in args.sizes:
        for src in sorted((OSTOVAR_FULL / f"Size{size}" / "Atomic").glob("*/output/*.mxml.gz")):
            stem = src.name.replace(".mxml.gz", "")
            with gzip.open(src, "rb") as handle:
                root = ET.parse(handle).getroot()
            for drift, cp in ((1, 900), (2, 1900)):
                if args.limit and jobs >= args.limit:
                    break
                name = f"{stem}__d{drift}"
                target = OUT / f"size{size}" / f"{name}.mxml.gz"
                target.parent.mkdir(parents=True, exist_ok=True)
                with gzip.open(target, "wb") as handle:
                    ET.ElementTree(subset(root, "ProcessInstance", windows(cp, cp))).write(
                        handle, encoding="utf-8", xml_declaration=True)
                index.append({"group": f"size{size}", "case": name, "source": src.name, "drift": drift,
                              "start": cp, "end": cp, "path": str(target.relative_to(ROOT))})
                jobs += 1
    if args.cdlg:
        with (REFERENCES / "cdlg_case_ground_truth_one_per_log100_v1.csv").open(encoding="utf-8-sig") as handle:
            cases = list(csv.DictReader(handle))
        for case in cases:
            if args.limit and jobs >= args.limit:
                break
            log = case["log_name"]
            number = int(log.split("_")[1])
            part = CDLG / f"without_noise_part_{1 if number <= 50 else 2}.zip"
            with zipfile.ZipFile(part) as archive, archive.open(log) as handle:
                root = ET.parse(handle).getroot()
            start, end = int(case["change_trace_start"]), int(case["change_trace_end"])
            target = OUT / "cdlg" / f"{case['case_id']}.xes"
            target.parent.mkdir(parents=True, exist_ok=True)
            try:
                ET.ElementTree(subset(root, "trace", windows(start, end))).write(
                    target, encoding="utf-8", xml_declaration=True)
                note = ""
            except ValueError as exc:
                note = str(exc)
            index.append({"group": "cdlg", "case": case["case_id"], "source": log, "drift": case["drift_id"],
                          "start": start, "end": end, "path": str(target.relative_to(ROOT)) if not note else "",
                          "note": note})
            jobs += 1
    with (OUT / "index.csv").open("w", encoding="utf-8", newline="") as handle:
        fields = ["group", "case", "source", "drift", "start", "end", "path", "note"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows({k: r.get(k, "") for k in fields} for r in index)
    print(f"{len(index)} window logs -> {OUT}")


if __name__ == "__main__":
    main()
