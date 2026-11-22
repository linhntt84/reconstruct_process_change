### Observed differences

- A08: A16 changes from 0.195 to 0.125. [DIR001]
- A10: A15 changes from 0.050 to 0.845. [DIR002]
- A14: A10 changes from 0.010 to 0.655. [DIR003]
- A20: A23 changes from 0.995 to 0.668. [DIR004]
- A22: A20 changes from 0.995 to 0.554. [DIR005]
- 77 evidence items qualified; about 1.00 would be expected without any change.

### Inference

Support level: Supported hypothesis

- A20 and A24 change from forward behavior to mixed_order behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL015]
- A20 and A25 change from forward behavior to mixed_order behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL016]
- A20 and A26 change from forward behavior to mixed_order behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL017]
- A22 and A24 change from forward behavior to mixed_order behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL018]
- A22 and A26 change from forward behavior to mixed_order behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL019]
- A23 and A25 change from forward behavior to mixed_order behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL021]
- A23 and A26 change from forward behavior to mixed_order behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL022]
- The order of A23 and A24 reverses. The evidence does not determine which activity moved or whether this is a swap. [REL020]

Rule matches are hypotheses based on the qualified evidence, not proof of the underlying process edit; several matches may reflect one change.
