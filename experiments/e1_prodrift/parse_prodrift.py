#!/usr/bin/env python3
"""E1 step 2: parse ProDrift console and characterization output into one table.

For each log: the detected drift points (event index in ProDrift's time-ordered event
stream) converted to a trace position (number of traces started up to that event's
timestamp), and for each detected drift its natural-language characterization statements
and the fragment trees they refer to.

Output: results/e1_prodrift/detections.csv (one row per detected drift) and
results/e1_prodrift/detections.jsonl (same, with statements and fragment trees).
Matching detections to the reference drifts and scoring are separate steps.
"""
from __future__ import annotations

import csv
import gzip
import json
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from bisect import bisect_right
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
from pcr.paths import OSTOVAR_FULL, RESULTS  # noqa: E402

RAW = RESULTS / "e1_prodrift" / "raw"
sys.path.insert(0, str(HERE))
from run_prodrift import CDLG  # noqa: E402
DETECTION = re.compile(r"\((\d+)\) Drift detected at event: (\d+) .* after reading (\d+) events")


def event_stream_xes(zip_path: Path | None, member: str) -> tuple[list[float], list[float]]:
    """XES log inside a zip archive (CDLG) or, with zip_path None, a plain XES file.
    Same output as event_stream."""
    events, starts = [], []
    with (zipfile.ZipFile(zip_path).open(member) if zip_path else open(member, "rb")) as handle:
        first = None
        for _, elem in ET.iterparse(handle, events=("end",)):
            tag = elem.tag.rsplit("}", 1)[-1]
            if tag == "event":
                for child in elem:
                    if child.tag.rsplit("}", 1)[-1] == "date" and child.get("key") == "time:timestamp":
                        ts = datetime.fromisoformat(child.get("value")).timestamp()
                        events.append(ts)
                        first = ts if first is None else min(first, ts)
                elem.clear()
            elif tag == "trace":
                if first is not None:
                    starts.append(first)
                first = None
                elem.clear()
    return sorted(events), sorted(starts)


def event_stream(log: Path) -> tuple[list[float], list[float]]:
    """Return (sorted event timestamps, sorted trace start timestamps) in epoch seconds."""
    events, starts = [], []
    with gzip.open(log, "rb") as handle:
        first = None
        for _, elem in ET.iterparse(handle, events=("end",)):
            if elem.tag == "timestamp":
                ts = datetime.fromisoformat(elem.text.strip()).timestamp()
                events.append(ts)
                first = ts if first is None else min(first, ts)
            elif elem.tag == "ProcessInstance":
                if first is not None:
                    starts.append(first)
                first = None
                elem.clear()
    return sorted(events), sorted(starts)


def parse_characterization(path: Path) -> list[dict]:
    """Blocks are separated by a line of asterisks, one block per detected drift, in order."""
    if not path.exists():
        return []
    blocks = [b for b in path.read_text(errors="replace").split("*" * 47) if b.strip()]
    out = []
    for block in blocks:
        statements = re.findall(r"^\d+\. (.+)$", block, flags=re.M)
        fragments = {}
        # a fragment may have only a left tree (removed) or only a right tree (inserted)
        for part in re.split(r"\n(?=Fragment \d+\n)", block):
            m = re.match(r"(Fragment \d+)\n", part)
            if not m:
                continue
            left = re.search(r"^Left tree: (.+)$", part, flags=re.M)
            right = re.search(r"^Right tree: (.+)$", part, flags=re.M)
            fragments[m.group(1)] = {"left": left.group(1) if left else "", "right": right.group(1) if right else ""}
        n = re.search(r"# of statements: (\d+)", block)
        out.append({"statements": statements, "fragments": fragments,
                    "n_statements": int(n.group(1)) if n else len(statements)})
    return out


def main():
    rows = []
    for run in sorted(RAW.glob("*/*/run.json")):
        meta = json.loads(run.read_text())
        folder = run.parent
        console = (folder / "console.txt").read_text(errors="replace")
        detections = {}
        for idx, event, read in DETECTION.findall(console):
            detections[int(idx)] = (int(event), int(read))  # console repeats lines; keep unique
        chars = parse_characterization(folder / "characterization.txt")
        if meta.get("dataset") == "cdlg":
            zip_name, member = meta["source_log"].split("::")
            events, starts = event_stream_xes(CDLG / zip_name, member)
        elif meta["source_log"].endswith(".xes"):
            events, starts = event_stream_xes(None, str(ROOT / meta["source_log"]))
        else:
            events, starts = event_stream(OSTOVAR_FULL / meta["source_log"])
        for idx in sorted(detections):
            event, read = detections[idx]
            ts = events[min(event, len(events)) - 1]
            ts_read = events[min(read, len(events)) - 1]
            char = chars[idx - 1] if idx - 1 < len(chars) else {"statements": [], "fragments": {}, "n_statements": 0}
            rows.append({"dataset": meta.get("dataset", "ostovar"), "size": meta["size"], "log": meta["log"],
                         "status": meta["status"], "drift_index": idx, "detected_event": event, "read_events": read,
                         "detected_trace": bisect_right(starts, ts), "reported_after_trace": bisect_right(starts, ts_read),
                         "n_traces": len(starts), "n_statements": char["n_statements"],
                         "statements": char["statements"], "fragments": char["fragments"]})
        if not detections:
            rows.append({"dataset": meta.get("dataset", "ostovar"), "size": meta["size"], "log": meta["log"],
                         "status": meta["status"], "drift_index": 0,
                         "detected_event": "", "read_events": "", "detected_trace": "", "reported_after_trace": "",
                         "n_traces": len(starts), "n_statements": 0, "statements": [], "fragments": {}})
    out = RESULTS / "e1_prodrift"
    with (out / "detections.jsonl").open("w", encoding="utf-8") as handle:
        for r in rows:
            handle.write(json.dumps(r, ensure_ascii=False) + "\n")
    fields = [k for k in rows[0] if k not in ("statements", "fragments")] + ["first_statement"]
    with (out / "detections.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for r in rows:
            writer.writerow({**{k: r[k] for k in fields if k != "first_statement"},
                             "first_statement": r["statements"][0] if r["statements"] else ""})
    print(f"{len(rows)} rows -> {out / 'detections.csv'}")


if __name__ == "__main__":
    main()
