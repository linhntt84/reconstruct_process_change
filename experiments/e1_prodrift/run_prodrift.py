#!/usr/bin/env python3
"""E1: run ProDrift 2.5 (event-based detection + fragment-based characterization) on the
Ostovar atomic logs, unchanged, as the non-LLM state-of-the-art baseline.

Configuration (fixed before looking at any evaluation output; follows the ProDrift readme
recommendations for artificial logs):
  -ddm events -dds high -characterization -cm fragment-exhaustive
  noise filters -ddnft/-dcnft = 0.0 for noise-free logs, 0.1 (tool default) for noisy logs.
ProDrift detects the drift points itself; matching detections to the reference drifts and
scoring are done in separate scripts.

The ProDrift JVM does not exit after finishing, so each run is stopped once the final
console line appears (or after --timeout seconds). The log is copied to a work folder
because ProDrift writes its characterization file next to the log.

Outputs: results/e1_prodrift/raw/size<k>/<log stem>/{console.txt, characterization.txt, run.json}
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
from pcr.paths import OSTOVAR_FULL, RESULTS  # noqa: E402

# ProDrift 2.5 jar (not in Git, 300 MB; download from Apromore). Override with PRODRIFT_JAR.
JAR = Path(os.environ.get("PRODRIFT_JAR", Path(__file__).resolve().parents[3] / "ProDrift2.5" / "ProDrift2.5.jar"))
OUT = RESULTS / "e1_prodrift" / "raw"
# CDLG (Ceravolo et al.) evaluation logs, noise-free, 100 XES logs in two zip parts.
CDLG = Path(os.environ.get("PCR_CDLG", ROOT.parent / "GitHub_Master_Results/data/raw_local/Data/"
                           "concept-drift-characterization/evaluation_paper/data_collection/"
                           "datasets_evaluation/without_noise"))
DONE_MARK = "Drift characterization statements are stored in a file next to the log."


def command(log: Path, noisy: bool) -> list[str]:
    nf = "0.1" if noisy else "0.0"
    return ["java", f"-Xmx{os.environ.get('PRODRIFT_XMX', '6g')}", "-jar", str(JAR), "-fp", str(log), "-ddm", "events", "-ddnft", nf,
            "-dds", "high", "-characterization", "-cm", "fragment-exhaustive", "-dcnft", nf]


def run_one(src, size, timeout: int) -> str:
    """src: an Ostovar log path, or (zip path, member) for CDLG; size: fragment size or 'cdlg'."""
    cdlg = size == "cdlg"
    files = isinstance(size, str) and size.startswith("files:")
    name = src[1] if cdlg else src.name
    stem = name.replace(".mxml.gz", "").replace(".xes", "")
    group = "cdlg" if cdlg else size.split(":", 1)[1] if files else f"size{size}"
    target = OUT / group / stem
    if (target / "run.json").exists():
        return f"{group}/{stem} skipped (done)"
    noisy = (not cdlg) and (stem.endswith("_2") or stem.endswith("_5"))
    with tempfile.TemporaryDirectory(prefix="prodrift_") as work:
        log = Path(work) / name
        if cdlg:
            with zipfile.ZipFile(src[0]) as archive, archive.open(src[1]) as handle, log.open("wb") as out:
                shutil.copyfileobj(handle, out)
        else:
            shutil.copy(src, log)
        cmd = command(log, noisy)
        started, t0 = datetime.now(timezone.utc).isoformat(), time.perf_counter()
        console = Path(work) / "console.txt"
        with console.open("w") as handle:
            proc = subprocess.Popen(cmd, stdout=handle, stderr=subprocess.STDOUT, cwd=work)
            status = "timeout"
            while time.perf_counter() - t0 < timeout:
                if proc.poll() is not None:
                    status = f"exited {proc.returncode}"
                    break
                if DONE_MARK in console.read_text(errors="replace"):
                    time.sleep(2)  # let the characterization file be flushed
                    status = "finished"
                    break
                time.sleep(1)
            if proc.poll() is None:
                proc.kill()
                proc.wait()
        latency = round(time.perf_counter() - t0, 1)
        target.mkdir(parents=True, exist_ok=True)
        shutil.copy(console, target / "console.txt")
        chars = list(Path(work).glob("characterizationResults_*.txt"))
        if chars:
            shutil.copy(chars[0], target / "characterization.txt")
        source = (f"{Path(src[0]).name}::{src[1]}" if cdlg else str(src.relative_to(ROOT)) if files
                  else str(src.relative_to(OSTOVAR_FULL)))
        record = {"dataset": "cdlg" if cdlg else group if files else "ostovar", "source_log": source, "size": size, "log": stem,
                  "noisy": noisy, "command": [c if c != str(log) else name for c in cmd],
                  "status": status, "characterization_file": chars[0].name if chars else None,
                  "started_at_utc": started, "wall_seconds": latency}
        (target / "run.json").write_text(json.dumps(record, indent=2), encoding="utf-8")
    return f"{group}/{stem} {status} {latency}s"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", choices=("ostovar", "cdlg", "files"), default="ostovar")
    parser.add_argument("--files-dir", type=Path, help="with --dataset files: folder of logs; its name is the group")
    parser.add_argument("--sizes", type=int, nargs="+", default=[1, 2, 3, 4, 5])
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--timeout", type=int, default=1800)
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()
    jobs = []
    if args.dataset == "cdlg":
        for part in sorted(CDLG.glob("*.zip")):
            with zipfile.ZipFile(part) as archive:
                jobs += [((part, m), "cdlg") for m in sorted(archive.namelist()) if m.endswith(".xes")]
    if args.dataset == "files":
        folder = args.files_dir if args.files_dir.is_absolute() else ROOT / args.files_dir
        jobs += [(p, f"files:{folder.name}") for p in sorted(folder.glob("*.xes")) + sorted(folder.glob("*.mxml.gz"))]
    for size in (args.sizes if args.dataset == "ostovar" else []):
        for src in sorted((OSTOVAR_FULL / f"Size{size}" / "Atomic").glob("*/output/*.mxml.gz")):
            jobs.append((src, size))
    if args.limit:
        jobs = jobs[:args.limit]
    print(f"{len(jobs)} logs, {args.workers} workers, jar {JAR}", flush=True)
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for i, line in enumerate(pool.map(lambda j: run_one(j[0], j[1], args.timeout), jobs), 1):
            print(f"[{i}/{len(jobs)}] {line}", flush=True)


if __name__ == "__main__":
    main()
