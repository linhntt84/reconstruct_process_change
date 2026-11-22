### Observed differences

- Activity A05 was executed exactly once in every trace in the earlier window (200 of 200 traces, mean 1.0 occurrence per trace); in the later window it does not appear at all (0 of 200 traces). [OCC001, POS002]
- The routing out of A01 changed completely: in the earlier window every observed outgoing transition of A01 went to A05, while in the later window every one goes directly to A02. [DIR001]
- A05's outgoing flow to A02, seen in the earlier window, is no longer observed, since A05 has no occurrences in the later window. [DIR002]
- Both relations involving A05 flipped from "always together" to "never together": A01 and A05 co-occurred in 100% of traces before (always A01 first) versus 0% after, with A01 now appearing without A05 in all traces; likewise A02 and A05 co-occurred in 100% before (always A05 first) versus 0% after. [REL001, REL002]
- The distance from A01 to A02 shrank from 2 steps in all earlier cases to 1 step in all later cases. [LAG001]
- A02's mean event position moved earlier, from 0.5 to about 0.33 of the trace, with unchanged spread. [POS001]
- Every item shows a difference larger than in about 995 of 1,000 random re-splits of the pooled data, and the two windows each contain 200 traces. [OCC001, DIR001, DIR002, POS001, POS002, REL001, REL002, LAG001]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that A05 — the step that always ran between A01 and A02 — is no longer executed in the later window, so that A01 now leads directly to A02. This is shown directly and consistently: A05 drops from universal participation to zero, A01's successor switches entirely from A05 to A02, both relations with A05 collapse from full co-occurrence to complete separation, the A01→A02 distance contracts from two steps to one, and A02 moves one position earlier — one coherent explanation covering all eight items. [OCC001, DIR001, DIR002, REL001, REL002, LAG001, POS001, POS002]

Limitation: zero participation strictly means only that A05 was not observed in the later window; the evidence cannot rule out that the later sample systematically excludes traces containing A05 (for example through filtering) rather than the step having been removed from the process. [OCC001, POS002]

Other differences: none — all items are consistent with the single change described above. [OCC001, DIR001, DIR002, POS001, POS002, REL001, REL002, LAG001]