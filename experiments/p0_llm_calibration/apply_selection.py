#!/usr/bin/env python3
"""Copy the thresholds chosen by the pre-registered E0 rule into configs/pipeline_v2.json.

Usage: apply_selection.py <selection json>. Prints the old and new values; writes the
config only if they differ, and records the selection file it came from.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONFIG = ROOT / "configs" / "pipeline_v2.json"


def main():
    selection_path = Path(sys.argv[1])
    selected = json.loads(selection_path.read_text())["selected"]
    config = json.loads(CONFIG.read_text())
    old = {"tau": config["qualification"]["tau"], "tau_loc": config["localization"]["tau_loc"],
           "eps_loc": config["localization"]["eps_loc"], "eps_rel": config["qualification"]["eps_rel"]}
    new = {k: float(selected[k]) for k in old}
    print("current :", old)
    print("selected:", new)
    if new == old:
        print("unchanged")
        return
    config["qualification"]["tau"], config["qualification"]["eps_rel"] = new["tau"], new["eps_rel"]
    config["localization"]["tau_loc"], config["localization"]["eps_loc"] = new["tau_loc"], new["eps_loc"]
    config["threshold_source"] = str(selection_path.relative_to(ROOT))
    CONFIG.write_text(json.dumps(config, indent=2) + "\n")
    print("config updated")


if __name__ == "__main__":
    main()
