### Observed differences

- In the earlier window, A27 was mandatory and singular: it appeared in 100 in 100 traces (mean once per trace), and A26's outgoing flow went to A27 in about 99 in 100 observed transitions, with A28 following; A32, A33 and A38 were never observed. [OCC001, DIR001, REL001, REL005, OCC002, OCC003, OCC004]
- In the later window, A27 appears in only about 51 in 100 traces, while A32, A33 and A38 each appear in about 49–50 in 100 traces, around the middle of the trace (median position about 0.5). [OCC001, OCC002, OCC003, OCC004, POS001, POS002, POS003]
- After A26 the flow now splits: about half of its outgoing transitions still go to A27, and about half go to the new activities (A33 about 17 in 100, A38 about 16, A32 about 15). [DIR001]
- A27 and each of the new activities are now alternatives: they practically never occur in the same trace (co-occurrence at most about 0.5 in 100), whereas before A27 occurred everywhere and the others nowhere. [REL006, REL007, REL008]
- The three new activities run together: each pair co-occurs in about 49 in 100 traces, with no fixed order between them (for A32/A33: A32 first in about 23 in 100 traces, A33 first in about 27 in 100). [REL012, REL013, REL014]
- The new block sits between A26 and A28: A26 precedes each of A32, A33 and A38 in about 49 in 100 traces, and each of them precedes A28 in about 49 in 100 traces. [REL002, REL003, REL004, REL009, REL010, REL011]
- The A26-to-A28 distance reflects this: before it was almost always 2 steps (about 98 in 100); in the later window it is bimodal — 2 steps in about 50 in 100 and 4 steps in about 48 in 100. [LAG001]
- A28 itself is unchanged, occurring in essentially every trace in both windows. [REL005, REL009, REL010, REL011]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis of a structural change in the segment between A26 and A28: in the later window, roughly half of the cases skip A27 there and instead run a group of three activities — A32, A33 and A38 — between A26 and A28, all three within the same case and in varying internal order, while the original A26 → A27 → A28 path continues in the other half of the cases. [REL001, REL006, REL009, REL012, LAG001, DIR001, OCC001, OCC002]

The screening found 27 qualifying control-flow items against roughly 0.57 expected without a change, so the pattern as a whole cannot be explained by random re-splits of stable behaviour. The placement of the new activities is shown directly by relational evidence (after A26, before A28, mutually exclusive with A27), and the occurrence, direction, position and lag indicators all agree; the profiles rest on large supports (about 98–102 traces per item in the later window). [OCC002, DIR001, REL006, REL009, LAG001]

A competing explanation the evidence cannot rule out: zero participation before only shows that A32, A33 and A38 were not observed earlier, so this could be an existing alternative path that was simply never taken before rather than a newly added one. Also, because the three new activities appear in both orders, no fixed sequence within the block can be inferred. [OCC002, OCC003, OCC004, REL012, REL013, REL014]

Other differences: A27's outgoing profile shifted slightly in the later window (to A28 from about 99.5 in 100 down to about 96 in 100, with small new edges to A09, A34 and A25 at about 1–2 in 100 each), and A26 shows a negligible new edge to A23 (about 0.5 in 100); both are very small in magnitude. [DIR002, DIR001]