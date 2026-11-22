### Observed differences

- Activity A07 disappeared from the observed traces: in the earlier window it ran in about 53 in 100 cases (106 of 200 traces, about 0.5 occurrences per trace), while in the later window it appears in 0 of 200 traces. [OCC001, POS002]
- The routing out of A03 changed: earlier, of A03's observed outgoing transitions, about 56 in 100 went to A05, about 39 to A07 and only about 5 to A06; in the later window none go to A07, and A05 and A06 take roughly equal shares (about 49 and 51 in 100). [DIR001]
- A07's outgoing flow is gone as well: earlier, about 92 in 100 of A07's outgoing transitions led to A06, with small shares to A10 and A09; in the later window A07 shows no outgoing transitions at all. [DIR002]
- The relations to A07 broke off: earlier, A03 and A07 occurred together in about 53 in 100 traces (A03 first in 24, interleaved or repeated in 29), and A06 and A07 together in about 53 in 100 (A07 first in about 21); in the later window neither pair ever co-occurs, with A03 appearing without A07 in about 52 in 100 traces and A06 likewise in about 52. [REL001, REL002]
- The spacing between A03 and A06 changed: earlier, when the two fell within five steps of each other, gaps of 2 and 4 steps dominated (about 23 and 20 in 100); in the later window direct adjacency (gap 1) appears in about 19 in 100 cases, gaps of 3 and 5 emerge, and gaps of 2 and 4 vanish. [LAG001]
- A03 sits slightly later within traces in the later window (mean relative position about 0.43 vs 0.48, median about 0.39 vs 0.45). [POS001]

### Inference

Support level: Supported hypothesis

Eight control-flow items qualified where only about 0.1 would be expected without change, far beyond what chance alone produces, and they converge on one structural difference: in the later window A07 no longer appears, and the flow that previously ran A03 → A07 → A06 is replaced by a direct A03 → A06 step (about 51 in 100 of A03's outgoing transitions, up from about 5), while the route from A03 to A05 continues at a similar share. [OCC001, DIR001, DIR002, REL001, REL002, LAG001]

The support is direct and consistent: A07's participation falls from 106 of 200 traces to zero, A03's transitions to A07 disappear while its transitions to A06 rise roughly tenfold, A07's own outgoing profile (mostly toward A06) vanishes, both relations with A07 drop from about 53 in 100 co-occurrences to zero, and the A03–A06 distance distribution loses exactly the multi-step gaps an intermediate activity would create. [OCC001, DIR001, DIR002, REL001, REL002, LAG001]

Limitations: zero participation strictly shows only that A07 was not observed in the later sample, so the evidence cannot fully rule out that A07 still occurs but was missed, nor distinguish a removed activity from a branch that is simply never taken; most items also describe the same underlying traces, so they are not independent confirmations. [OCC001, DIR002]

Other differences: the slight later placement of A03 within traces (mean relative position about 0.43 → 0.48) is minor and, being based on event positions rather than clock time, does not by itself show that A03 was moved. [POS001]