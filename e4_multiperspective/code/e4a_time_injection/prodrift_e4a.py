#!/usr/bin/env python3
"""E4a step 5: ProDrift (E1 configuration, unchanged) on long logs with the E4a time changes.

Long logs (ProDrift needs long streams after a change):
  T_SLOW / T_FAST / N : traces [0, 850) of the noise-free pattern log; time change into X
                        (same X and k as the E4a case) for traces [425, 850); N: none.
  M                   : traces [0, 1850) (control-flow drift 1 at 900); time change into X
                        for traces [950, 1850).
The time change is injected into the MXML itself (timestamps of X and of every later entry of
the trace move by (k - 1) * d, d = gap from the preceding non-technical event), mirroring
build_e4a.py. Technical marker events (DRIFT_*) are removed, as in the pipeline.
Logs: results/e4a_time_injection/prodrift/logs/ (not in Git);
ProDrift output: results/e4a_time_injection/prodrift/raw/e4a/<case_id>/.

  python prodrift_e4a.py build      # write the long logs
  python prodrift_e4a.py run        # run ProDrift (uses experiments/e1_prodrift/run_prodrift.py)
  python prodrift_e4a.py score      # parse and score -> prodrift/scores.csv
"""
from __future__ import annotations

import argparse
import copy
import csv
import gzip
import json
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from e4_common import E4_RESULTS, REPO  # noqa: E402

sys.path.insert(0, str(REPO / "experiments" / "e1_prodrift"))
sys.path.insert(0, str(REPO / "src"))
from pcr.logs import is_technical_activity  # noqa: E402
from pcr.paths import OSTOVAR_FULL  # noqa: E402

DATA = E4_RESULTS / "e4a_time_injection"
OUT = DATA / "prodrift"
K = {"increase": 2.0, "decrease": 0.5}


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def entry_fields(entry):
    name = ts = None
    for child in entry:
        if local(child.tag) == "WorkflowModelElement":
            name = (child.text or "").strip()
        elif local(child.tag) == "timestamp":
            ts = child
    return name, ts


def set_time(entry, value: datetime) -> None:
    text = value.isoformat(timespec="milliseconds")
    for child in entry.iter():
        if local(child.tag) == "timestamp":
            child.text = text
        if local(child.tag) == "attribute" and child.get("name") == "time:timestamp":
            child.text = text


def inject_trace(instance, target: str, k: float) -> None:
    entries = [e for e in instance if local(e.tag) == "AuditTrailEntry"]
    shift, prev_time = timedelta(0), None
    for entry in entries:
        name, ts = entry_fields(entry)
        original = datetime.fromisoformat(ts.text.strip())
        if name == target and prev_time is not None and not is_technical_activity(name):
            shift += (k - 1.0) * (original - prev_time)
        if not is_technical_activity(name or ""):
            prev_time = original
        if shift:
            set_time(entry, original + shift)


def build() -> None:
    with (DATA / "cases.csv").open(encoding="utf-8") as handle:
        cases = list(csv.DictReader(handle))
    (OUT / "logs").mkdir(parents=True, exist_ok=True)
    index = []
    for case in cases:
        src = OSTOVAR_FULL / case["source_log"]
        with gzip.open(src, "rb") as handle:
            root = ET.parse(handle).getroot()
        process = next(e for e in root.iter() if local(e.tag) == "Process")
        instances = [e for e in process if local(e.tag) == "ProcessInstance"]
        end, change = (1850, 950) if case["type"] == "M" else (850, 425)
        for inst in instances[end:]:
            process.remove(inst)
        # Drop technical marker events (DRIFT_*), as the pipeline does: a time shift could move an
        # activity before a marker and ProDrift would read the swapped order as a structural change.
        for inst in instances[:end]:
            for entry in [e for e in inst if local(e.tag) == "AuditTrailEntry"]:
                name, _ = entry_fields(entry)
                if is_technical_activity(name or ""):
                    inst.remove(entry)
        if case["time_target"]:
            k = K[case["time_direction"]]
            for inst in instances[change:end]:
                inject_trace(inst, case["time_target"], k)
        target = OUT / "logs" / f"{case['case_id']}.mxml.gz"
        with gzip.open(target, "wb") as handle:
            ET.ElementTree(root).write(handle, encoding="utf-8", xml_declaration=True)
        index.append({"case_id": case["case_id"], "split": case["split"], "type": case["type"],
                      "traces": end, "time_change_trace": change if case["time_target"] else "",
                      "cf_change_trace": 900 if case["type"] == "M" else ""})
        print(case["case_id"], case["type"], end, flush=True)
    with (OUT / "index.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(index[0]))
        writer.writeheader()
        writer.writerows(index)


def run(workers: int) -> None:
    """Reuse run_one of the E1 runner (unchanged file) with its output folder redirected here."""
    from concurrent.futures import ThreadPoolExecutor
    import run_prodrift as rp
    rp.OUT = OUT / "raw"
    logs = sorted((OUT / "logs").glob("*.mxml.gz"))
    print(f"{len(logs)} logs, {workers} workers, jar {rp.JAR}", flush=True)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        for i, line in enumerate(pool.map(lambda p: rp.run_one(p, "files:e4a", 1800), logs), 1):
            print(f"[{i}/{len(logs)}] {line}", flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("build", "run", "score"))
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()
    if args.action == "build":
        build()
    elif args.action == "run":
        run(args.workers)


if __name__ == "__main__":
    main()


def score() -> None:
    """Parse ProDrift output and score (design in docs/NHAT_KY_E4_VI.md, step 5)."""
    import re as _re
    from bisect import bisect_right
    import parse_prodrift as pp
    import score_prodrift as sp
    from score import PATTERN_FAMILY, object_score
    with (DATA / "cases.csv").open(encoding="utf-8") as handle:
        cases = {r["case_id"]: r for r in csv.DictReader(handle)}
    time_words = _re.compile(r"\b(time|duration|slower|faster|longer|shorter|delay|wait)", _re.I)
    rows = []
    for run_json in sorted((OUT / "raw" / "e4a").glob("*/run.json")):
        meta = json.loads(run_json.read_text())
        cid = meta["log"].replace(".mxml", "")
        case = cases[cid]
        console = (run_json.parent / "console.txt").read_text(errors="replace")
        detections = {int(i): (int(e), int(r)) for i, e, r in pp.DETECTION.findall(console)}
        chars = pp.parse_characterization(run_json.parent / "characterization.txt")
        events, starts = pp.event_stream(OUT / "logs" / f"{cid}.mxml.gz")
        found = []
        for idx in sorted(detections):
            event, _ = detections[idx]
            trace = bisect_right(starts, events[min(event, len(events)) - 1])
            char = chars[idx - 1] if idx - 1 < len(chars) else {"statements": [], "fragments": {}}
            found.append({"trace": trace, **char})
        cp = 900 if case["type"] == "M" else 425
        hit = next((d for d in found if cp <= d["trace"] < cp + 500), None)
        statements = hit["statements"] if hit else []
        x = case["time_target"]
        time_detected = float(bool(x) and any(time_words.search(s) and x in s for s in statements))
        row = {"case_id": cid, "split": case["split"], "type": case["type"], "n_detections": len(found),
               "detected_in_window": bool(hit), "n_statements": len(statements),
               "any_time_statement": float(any(time_words.search(s) for s in statements)),
               "time_detected": time_detected if x else ""}
        if case["type"] == "M":
            ch = sp.characterize(statements, hit["fragments"]) if hit else {"pattern": "none", "central": set()}
            required, optional = set(json.loads(case["cf_required"])), set(json.loads(case["cf_optional"]))
            o = object_score(ch["central"], required, optional) if ch["central"] else 0.0
            truth, pred = PATTERN_FAMILY[case["cf_pattern"]], PATTERN_FAMILY.get(ch["pattern"], "")
            row.update({"cf_pattern_predicted": ch["pattern"], "cf_O": o, "cf_MR": min(o, float(pred == truth))})
        rows.append(row)
    with (OUT / "scores.csv").open("w", encoding="utf-8", newline="") as handle:
        fields = sorted({k for r in rows for k in r}, key=lambda k: list(rows[0]).index(k) if k in rows[0] else 99)
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    from statistics import mean
    for split in ("evaluation", "tuning"):
        for kind in ("T_SLOW", "T_FAST", "M", "N"):
            items = [r for r in rows if r["split"] == split and r["type"] == kind]
            text = (f"{split:10s} {kind:6s} n={len(items):2d} drift detected in window={mean(r['detected_in_window'] for r in items):.2f} "
                    f"any detection={mean(r['n_detections'] > 0 for r in items):.2f} "
                    f"time statements={mean(r['any_time_statement'] for r in items):.2f}")
            if kind != "N":
                text += f" time_detected={mean(r['time_detected'] for r in items):.2f}"
            if kind == "M":
                text += f" cf_O={mean(r['cf_O'] for r in items):.2f} cf_MR={mean(r['cf_MR'] for r in items):.2f}"
            print(text)


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "score":
    sys.path.insert(0, str(REPO / "experiments" / "p0_llm_calibration"))
    score()
