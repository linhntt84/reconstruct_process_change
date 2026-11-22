### Observed differences

- Activity A01 was not executed at all in the earlier window (0 of 200 traces); in the later window it occurs exactly once in every trace (200 of 200, mean occurrences per trace 1.0, no repetition). [OCC001]
- The outgoing flow of A04 changed completely: in the earlier window A04 ran in every trace but no outgoing transition from it was observed (0 across 200 traces), whereas in the later window all 200 observed outgoing transitions of A04 lead to A01. [DIR001]
- The relationship between the two activities flipped from never co-occurring to always co-occurring in a fixed order: earlier, A04 appeared without A01 in 100 in 100 traces (co-occurrence 0); later, they occur together in 100 in 100 traces and A04 precedes A01 in all of them. [REL001]
- On the event-position scale, A01 now sits at a fixed early position (mean 1.0, no spread), and A04's typical position moved slightly earlier (mean 1.0 to 0.75). [POS001, POS002]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that A01 was added immediately after A04 and is now executed in every case: in the earlier window A01 was entirely absent (0 of 200 traces) while A04 ran in every trace with no observed successor, whereas in the later window A01 runs exactly once per trace, always after A04, and A04's only observed outgoing flow goes to A01. Since A01 was absent earlier, this is a step being added or becoming part of every case, not a shift in how often pre-existing alternative paths are taken. [OCC001, DIR001, REL001, POS001, POS002]

The screening supports this reading: the control-flow family flagged 5 items where about 0.02 would be expected for an unchanged process, far beyond what random re-splits of the pooled data produce, and each individual difference is larger than in about 995 of 1000 random re-splits. The relational and successor evidence shows the A04-then-A01 sequence directly, so the hypothesis does not rest on the position shift alone. [OCC001, DIR001, POS001, POS002, REL001]

Limitations: all five items describe the same underlying A01–A04 difference, so they are not independent confirmations. The evidence also cannot rule out that the earlier window simply did not record A01 or anything after A04 — for example because earlier cases were captured only up to A04, or because the case mix switched entirely to a variant containing A01 — since no successor of A04 was observed at all in that window. [DIR001, REL001]

Other differences: none — every flagged item concerns the A01–A04 pair. [OCC001, DIR001, POS001, POS002, REL001]