### Observed differences

- In the earlier window, A21, A22 and A23 were mandatory: each appeared exactly once in every trace (200 of 200). A14, A15 and A16 were not observed at all. In the later window this flipped: A21, A22 and A23 each appear in only about 1 in 200 traces, while A14, A15 and A16 appear in about 30, 33 and 37 in 100 traces respectively (60, 65 and 74 of 200). [OCC001, OCC002, OCC003, OCC004, OCC005, OCC006]

- The three new activities are mutually exclusive alternatives: no pair of them ever occurs in the same trace, and their shares together cover essentially all traces, so a later case contains exactly one of A14, A15 or A16, occurring once. Earlier, A21, A22 and A23 always ran together in the same trace, in no fixed order among themselves (for example, A21 before A22 in about 53 in 100 traces, A22 before A21 in about 48 in 100). [REL001, REL002, REL010, REL025, REL026, REL031]

- A39's routing changed completely: earlier its outgoing transitions went to A21, A22 and A23 in roughly equal thirds; later they go to A14, A15 and A16 in shares of about 30, 33 and 37 per 100. The new activities in turn lead exclusively to A24. [DIR007, DIR001, DIR002, DIR003]

- The segment between A39 and A24 shortened: the A39-to-A24 distance was 4 event positions in essentially all earlier traces and 2 positions in the later window, and A24's mean position moved earlier (about 0.43 to 0.39 of the trace length). [LAG010, POS007]

- The surrounding order is consistent with a like-for-like replacement: earlier A39 always preceded A21 and A21 always preceded A24; later A39 precedes A14 whenever A14 occurs (about 30 in 100 traces) and A14 precedes A24 in the same traces. [REL028, REL027, REL007, REL006]

- A39 and A40 show only small position shifts (mean position changes of about 0.02), and both remain in every trace in both windows. [POS008, POS009]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the mandatory three-activity block A21, A22 and A23 — executed between A39 and A24 in every case, in no fixed order among themselves — was replaced by a single choice among three mutually exclusive activities, A14, A15 and A16, so that a case now runs A39, then one of A14/A15/A16, then A24, instead of A39, then all of A21/A22/A23 in any order, then A24. This is a replacement of activities (some removed, others added), not a shift in how often existing paths are taken. [OCC001, OCC004, DIR007, DIR001, REL001, LAG010]

The support is direct and consistent across indicator families: the participation flip is near-total on both sides; A39's outgoing transitions moved from the old block to the new activities, which flow exclusively to A24; the relational items show the old trio always co-occurring earlier and never later, and the new trio never co-occurring; and the A39-to-A24 distance shrank from 4 to 2 positions, matching a block that shrank from three activities to one. The screening also produced 71 qualifying items against fewer than 1 expected without change, so chance sampling cannot account for the pattern as a whole. [DIR007, DIR001, REL006, REL007, REL025, REL027, REL028, LAG010]

Limitations: A21, A22 and A23 still appear in one later trace each, so a residual execution of the old block cannot be excluded; the exact split between A14, A15 and A16 (about 30/33/37) rests on a single finite sample; and the position evidence reflects event order, not clock time. A competing explanation the evidence cannot fully rule out is that the two windows draw unevenly from two coexisting process variants rather than reflecting one modification of a single process. [OCC004, OCC005, OCC006, POS007]

Other differences: A41 now appears in about 69 in 100 traces versus about 59 in 100 earlier, and it can co-occur with the new activities (for example with A14 in about 21 in 100 traces), whereas earlier it only ever co-occurred with the old block. [REL030, REL009]