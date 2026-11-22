# E0 — Parameter setting on a held-out tuning split

Addresses reviewer comments R2 #1, R4 #5, R6 #1(c) and R7 (B_S): state every Stage 1–2
parameter, show how it was chosen, and show it was not tuned on the evaluation cases.

| Split | Data | Use |
|---|---|---|
| Tuning | Ostovar fragment sizes 2, 4 × 13 patterns × 2 drifts × 3 noise levels = 156 cases, plus 78 no-drift (null) window pairs | select parameters (`analyze_grid.py --sizes 2 4`) |
| Evaluation | Ostovar sizes 1, 3, 5 and CDLG (100) | untouched; sensitivity description only (size 5 is in the sweep cache but never used for selection) |

Decision 2026-11-11: tune on sizes 2 and 4; sizes 1, 3, 5 are evaluation sets. Size 1 uses a
different base model, so its references need their own construction and human check (E11a).

## Selection criterion (LLM-free, fixed before running)

Per case and configuration: A* recall and precision against the reference activities;
E* coverage (share of reference activities mentioned by at least one evidence item);
|E*| and estimated evidence tokens; |E*| on null pairs.
Feasible = pooled mean A* recall ≥ 0.95 and E* coverage ≥ 0.95. Choose the feasible
configuration with the smallest median |E*|; ties → lower null |E*|; then closest to the
current configuration.

Grid: τ (DIR/POS/REL/LAG) and τ_OCC ∈ {0.90, 0.95, 0.975, 0.99, 0.995}; τ_loc ∈ {0.95, 0.975,
0.99, 0.995}; ε_loc and ε_REL ∈ {0.05, 0.10, 0.15, 0.20} (1,600 configurations, filtered
offline from one bootstrap per case); window |L±| ∈ {100, 150, 200, 300}; B_S ∈ {50, 100, 200}.

## Scripts (run from the repository root)

| Script | Purpose |
|---|---|
| `build_tuning_references.py` | Derive reference activities for sizes 2, 4, 5 from the noise-free logs with a deterministic rule; validates the rule by reproducing the frozen size-3 references (25/26; see note) |
| `sweep_evidence.py` | Run Stages 1–2 once per case with zero threshold floors and cache every candidate's r, q and serialized size, for every distinct A* in the (τ_loc, ε_loc) grid; records run time |
| `check_adapter.py` | Apply the manuscript configuration to the size-3 cache and compare with the evidence sent to the LLMs |
| `analyze_grid.py` | Offline grid, proxy metrics, pre-registered selection, one-at-a-time sensitivity |
| `backfill_runtime.py` | Add a runtime row for sweeps started before timing was recorded |

```bash
pip install -e .            # or: pip install -r requirements.txt (scripts add src/ to sys.path)
python experiments/e0_parameter_setting/build_tuning_references.py
python experiments/e0_parameter_setting/sweep_evidence.py --mode tuning --workers 8
python experiments/e0_parameter_setting/sweep_evidence.py --mode size3  --workers 8
python experiments/e0_parameter_setting/check_adapter.py
for w in 100 150 300; do python experiments/e0_parameter_setting/sweep_evidence.py --mode tuning --window $w --current-loc-only; done
for b in 50 200;      do python experiments/e0_parameter_setting/sweep_evidence.py --mode tuning --bs $b --current-loc-only; done
python experiments/e0_parameter_setting/analyze_grid.py --mode tuning
python experiments/e0_parameter_setting/analyze_grid.py --mode size3
```

## Outputs (`results/e0_parameter_setting/`)

| File | Content |
|---|---|
| `tuning_references.csv` | 234 tuning cases with reference activities and the evidence for each |
| `size3_reference_rule_validation.csv` | derived vs frozen size-3 references |
| `grid_<mode>_w<W>_b<B>.csv` | every configuration with pooled proxy metrics |
| `oat_<mode>_w<W>_b<B>.csv` | one-at-a-time sensitivity around the manuscript configuration, pooled and per noise level |
| `selection_<mode>_w<W>_b<B>.json` | selected configuration, manuscript configuration, ties |
| `runtime_log.csv` | wall time and summed task time per sweep, hardware |
| `cache/`, `logs/` | per-case candidates and progress logs (not in Git; regenerate with `sweep_evidence.py`) |

## Reproducibility checks

- Size-3 MXML logs equal the cdrift-evaluation XES logs used in the manuscript (2999/2999 traces).
- With the manuscript configuration, the cached size-3 candidates reproduce the archived
  evidence exactly (same units, r and q).
- Seeds: tuning `20261111 + first 8 hex of SHA256(case_id)`; size 3 `20260910 + case index`, as in the manuscript.

## Note on the frozen size-3 reference

Frequency, drift 1: the frozen reference lists `p1, q1, q2`. The logs and the evidence show
all six activities `p1–p3, q1–q3` changing identically, and drift 2 of the same pattern
lists all six. Left unchanged here; to be decided by the authors.
