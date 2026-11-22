# P0-A — Evidence qualification v2 (no LLM)

Question: why do stable (null) window pairs still yield qualified evidence, and
can the reference set W0 be fixed before prompt calibration?

Observed in the exploratory null run (`GitHub_Master_Results/analysis/outputs/null_api_v2`):
a CF_DIR item on a source activity with 3 outgoing transitions in L- and 9 in
L+, disjoint successors, cosine dissimilarity 1.0 and q = 1.0. Two causes:

1. **Within-window bootstrap.** v1 resamples each window against itself, so a
   reference pair never contains behaviour absent from that window and
   underestimates sample-to-sample differences of rare units.
2. **Ties at a saturated change function.** v1 counts `ref <= r`, so r = 1.0
   gives q = 1 even if all references are 1.0.

Variants compared on the tuning split (Ostovar sizes 2, 4; 156 drift cases,
78 null pairs; window 200, B_S = 100, tau_loc 0.99, eps_loc 0.10, eps_REL 0.10):

| Factor | Levels |
|---|---|
| Reference W0 | `bootstrap` (v1), `permutation` (pool L- ∪ L+, re-split; B = 200) |
| Tie rule | `le` (v1, q = (1+#ref≤r)/(B+1)), `lt` (q = #ref<r/(B+1) = 1 − Monte Carlo p) |
| tau profile | v1 (OCC .95, others .99), all .99, all .95 |
| Minimum support m | 0, 5, 10, 20 (max of unit support in L-, L+) |

Unit support: OCC/POS traces containing the activity; DIR outgoing transitions
of the source; REL traces containing either activity; LAG traces with the
ordered pair within lag 5.

`bootstrap` + `le` reproduces the E0 cache exactly (checked: 95/95 q values on
one case). Code: `src/pcr/evidence/qualification_v2.py` (v1 files untouched).

```bash
python experiments/p0_evidence_v2/sweep_reference_variants.py --reference bootstrap
python experiments/p0_evidence_v2/sweep_reference_variants.py --reference permutation
python experiments/p0_evidence_v2/analyze_variants.py
```

Outputs: `results/p0_evidence_v2/{cache,logs,runtime_log.csv,variants_tuning_sizes24.csv}`.

## Result (2026-11-11, min support 0; full table in `variants_tuning_sizes24.csv`)

| Reference | Ties | tau | A* recall | E* coverage | median \|E*\| | null nonempty E* | null mean \|E*\| |
|---|---|---|---|---|---|---|---|
| bootstrap (v1) | le (v1) | OCC .95, others .99 (v1) | 0.990 | 1.000 | 46 | 0.86 | 3.72 |
| bootstrap | le | all .99 | 0.990 | 1.000 | 44 | 0.72 | 2.21 |
| bootstrap | lt | all .99 | 0.988 | 1.000 | 37 | 0.42 | 0.82 |
| permutation | le | all .99 | 0.990 | 1.000 | 53 | 0.83 | 6.17 |
| permutation | lt | OCC .95, others .99 | 0.990 | 1.000 | 41 | 0.67 | 1.85 |
| **permutation** | **lt** | **all .99** | **0.990** | **1.000** | **39** | **0.37** | **0.72** |

Findings: the tie rule is the dominant factor (change functions are discrete, so
`<=` counts many ties as support); unifying tau_OCC to .99 is second; the
reference construction matters little once ties are conservative; minimum
support adds almost nothing. Remaining null items (≈0.7 per pair) are of the
order expected from testing many units per case at the 1% level.
Runtime: 1240 s (bootstrap) and 1227 s (permutation) wall, 8 workers, Apple M4.
