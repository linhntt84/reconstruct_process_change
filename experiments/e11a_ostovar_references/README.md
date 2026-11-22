# E11a — Ostovar references for fragment sizes other than 3

Goal: derive references (affected activities, required / optional) for Ostovar fragment sizes 1, 2, 4 and 5 by a
checkable procedure, since only size 3 had references labelled by the authors. No LLM is used.

## Procedure (5 steps)

1. **Source A — per-activity rule** (`experiments/e0_parameter_setting/build_tuning_references.py`).
   On the noise-free log, two long stable segments are compared (drift 1: [0, 850) vs [1050, 1850); drift 2:
   [1050, 1850) vs [2050, 2999)). An activity is affected if it appears or disappears; the share of traces
   containing it changes by ≥ 0.10; its mean number of occurrences per trace changes by ≥ 0.20; or both its set of
   direct predecessors and its set of direct successors change (edges in > 1% of traces).
2. **Source B — projection** (`derive_projection.py`), based on a different principle: the affected activities are
   those whose removal from every trace makes the behaviour before and after the drift indistinguishable.
   Behaviour = share of traces containing each activity and each directly-follows pair (with start/end).
   Distance D = largest difference. "Indistinguishable": D ≤ δ, where δ is the largest D between the two halves of
   one stable segment (three stable segments per log), i.e. the sampling noise of the same log. **All** minimum
   removal sets are found (exhaustive search by increasing size; the candidate set grows if removing all
   candidates still leaves a difference). Reference = union of the minimum sets (when either block can be removed,
   e.g. parallel → sequence, both blocks are affected). An exact solution was found for 130/130 cases.
3. **Required / optional convention**, applied identically to every source and every scored method: the partner
   branch of a moved or removed activity (Conditional/Parallel Move/Removal), the sibling branch in
   ConditionalToSequence and the re-entry anchor of Skip are **optional** (naming them neither adds nor
   removes credit). Sizes 2–5 share one base model, so the convention is identified by name (o*, p5.., o1).
   Size 1 has a different base model, so the convention is applied **by role**, read from the trace variants (step 5).
4. **Check on size 3** (against the authors' references, version 2): source A agrees on **26/26**; source B on
   **25/26** (difference: ConditionalRemoval drift 2, where B adds w, x because of loop-region fluctuation above δ).
5. **Reconciliation**: cases where A and B give the same required set are accepted; differing cases were read
   directly on the frequent trace variants before and after the drift, and the decision and reason recorded
   (`size1_decisions.json`).

## Results (`results/e11a_ostovar_references/compare_sizes12345.csv`)

| Size | A = B (required set) | Note |
|---|---|---|
| 1 | 21/26 | 5 differing cases, see below |
| 2 | 26/26 | tuning |
| 3 | 25/26 | A = authors 26/26; B = authors 25/26 |
| 4 | 26/26 | tuning |
| 5 | 26/26 | evaluation reference = source A |

Size 1, cases that differ or need the convention by role (size-1 base model: … t n o p u …):

| Pattern | Variant before → after | A | B | Decision (required; optional) |
|---|---|---|---|---|
| ConditionalMove | n o p → o (n ∣ p) | n, p | n, p | n; p (partner branch), o |
| ConditionalRemoval d1 | re in the removed conditional branch | re | re, r | re (r: loop-region fluctuation 0.06 → 0.10) |
| ParallelMove | n o p → o (n ∥ p) | n, p | n | n; p (parallel partner), o |
| ParallelRemoval | (re ∥ z1) → z1 | re, z1 | re | re; z1 (parallel partner) |
| Skip | n can be skipped | n | n | n; o (re-entry anchor, corresponds to o1) |
| Swap | n o p → p o n | n, o, p | n, o, p | n, p; o (stays between the swapped activities) |
| ConditionalToSequence | (p ∣ q) → p q | p, q | p, q | p, q |

Status: size 5 accepted by step 5. **Size 1 is not used in the evaluation** (its base model differs); the table
above and the size-1 reference file are kept for transparency only.

## Files
- Code: `derive_projection.py` (source B), `compare_sources.py` (comparison), `build_eval_references.py` (evaluation references), `size1_decisions.json`.
- Results: `results/e11a_ostovar_references/projection_sizes12345.csv`, `compare_sizes12345.csv`.
- References: `data/references/ostovar_size1_references_v2.csv`, `ostovar_size5_references_v2.csv` (78 rows each = 13 patterns × 2 drifts × 3 noise levels; columns `rule_required`, `projection_required`, `agree_required`, `reference_source`).
- Rerun: `python derive_projection.py --sizes 1 2 3 4 5 && python compare_sources.py && python build_eval_references.py` (about 15 minutes).
