#!/usr/bin/env python3
"""P6: generation for the four BPI 2017 change points with the P2 code (run_p2.py pointed at results/p6_bpi2017).
  python experiments/p6_bpi2017/run_bpi.py generate --model glm-5.3-flash --run-index k --stream   (PAID API CALLS)
Same frozen prompt (R3-MP-CONC) and settings as P2."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "experiments" / "p2_main"))
import run_p2  # noqa: E402

run_p2.OUT = ROOT / "results" / "p6_bpi2017"
run_p2.main()
