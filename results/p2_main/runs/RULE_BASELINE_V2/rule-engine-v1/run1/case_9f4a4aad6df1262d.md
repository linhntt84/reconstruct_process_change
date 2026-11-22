### Observed differences

- A20: A23 changes from 0.990 to 0.668. [DIR001]
- A22: A20 changes from 0.995 to 0.560. [DIR002]
- A23: A24 changes from 1.000 to 0.149. [DIR003]
- A24: A26 changes from 0.990 to 0.604. [DIR004]
- A25: A32 changes from 0.930 to 0.425. [DIR005]
- 49 evidence items qualified; about 0.66 would be expected without any change.

### Inference

Support level: Supported hypothesis

- A20 and A24 change from forward behavior to mixed_order behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL001]
- A20 and A25 change from forward behavior to mixed_order behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL002]
- A20 and A26 change from forward behavior to mixed_order behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL003]
- A22 and A24 change from forward behavior to mixed_order behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL004]
- A22 and A26 change from forward behavior to mixed_order behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL005]
- A23 and A25 change from forward behavior to mixed_order behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL007]
- A23 and A26 change from forward behavior to mixed_order behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL008]
- The order of A23 and A24 reverses. The evidence does not determine which activity moved or whether this is a swap. [REL006]

Rule matches are hypotheses based on the qualified evidence, not proof of the underlying process edit; several matches may reflect one change.
