# E4a — Ostovar windows with injected time changes


Time changes are injected as in Padella & Vinci (BPM 2026): the time of a target activity
X is multiplied by k for every case after the change point and later events of the case
are shifted accordingly. Ostovar logs only have completion timestamps, so the injected
quantity is the time from the preceding event to the completion of X (what `T_WAIT`
measures). Activity sequences are never changed.

| Type | Windows | Change in L+ | Evaluation (sizes 3, 5) | Tuning (sizes 2, 4) |
|---|---|---|---|---|
| T_SLOW | L− [350, 550), L+ [650, 850) | time into X × 2 | 26 | 6 |
| T_FAST | same | time into X × 0.5 | 26 | 6 |
| N | same windows, paired with T | none | 26 | 6 |
| M | drift 1: L− [650, 850), L+ [950, 1150) | existing control-flow change + time into another activity (13 slow, 13 fast) | 26 | 6 |

Run: `python e4_multiperspective/code/e4a_time_injection/build_e4a.py` (deterministic, seed 20261113, about 1 minute).

Outputs in `e4_multiperspective/results/e4a_time_injection/`:
- `cases.csv`: answer key per case (type, target X, k, direction, predecessors of X,
  control-flow pattern and activities for M, required/optional activities, perspectives);
- `cases/<case_id>.json.gz`: `{"before": [[[activity, iso_timestamp], ...], ...], "after": ...}`;
- `sanity.csv`: activity sequences unchanged, no other directly-follows gap changed, median
  ratio of gaps into X equals k.

Answer key: X is required; its predecessors are optional (a `T_WAIT` item names the pair
predecessor → X). For M, the control-flow required/optional sets of the E0 rule are added.
