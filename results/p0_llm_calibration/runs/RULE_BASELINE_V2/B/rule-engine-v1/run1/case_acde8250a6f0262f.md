### Observed differences

- A15: A19 changes from 0.265 to 0.490. [DIR001]
- A16: A15 changes from 0.275 to 0.490. [DIR002]
- A18: A15 changes from 0.330 to 0.510. [DIR003]
- A19: A20 changes from 0.090 to 1.000. [DIR004]
- A20: A22 changes from 0.325 to 0.510. [DIR005]
- 68 evidence items qualified; about 0.58 would be expected without any change.

### Inference

Support level: Supported hypothesis

- A15 and A20 change from mixed_order behavior to forward behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL001]
- A15 and A22 change from mixed_order behavior to forward behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL002]
- A15 and A23 change from mixed_order behavior to forward behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL003]
- A16 and A20 change from mixed_order behavior to forward behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL004]
- A16 and A22 change from mixed_order behavior to forward behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL005]
- A16 and A23 change from mixed_order behavior to forward behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL006]
- A18 and A20 change from mixed_order behavior to forward behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL007]
- A18 and A22 change from mixed_order behavior to forward behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL008]
- A18 and A23 change from mixed_order behavior to forward behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL009]
- A19 and A21 change from mixed_order behavior to forward behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL011]
- A19 and A22 change from mixed_order behavior to forward behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL012]
- A19 and A23 change from mixed_order behavior to forward behavior. A parallel/sequential change is a candidate, but mixed trace order alone cannot establish concurrency. [REL013]
- The order of A19 and A20 reverses. The evidence does not determine which activity moved or whether this is a swap. [REL010]

Rule matches are hypotheses based on the qualified evidence, not proof of the underlying process edit; several matches may reflect one change.
