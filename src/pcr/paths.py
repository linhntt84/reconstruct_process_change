"""Repository paths. Raw data live outside Git; override with environment variables."""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
REFERENCES = DATA / "references"
RESULTS = ROOT / "results"

# Full Ostovar "Logs Characterization" benchmark (fragment sizes 1-5, 0/2.5/5% noise).
OSTOVAR_FULL = Path(os.environ.get("PCR_OSTOVAR_FULL", DATA / "raw/ostovar_characterization")) / "FragmentChange"
# Evidence JSON exactly as sent to the LLMs in the submitted manuscript (version 1).
PAPER_V1_EVIDENCE = Path(os.environ.get("PCR_PAPER_V1_EVIDENCE", DATA / "raw/paper_v1_evidence"))
