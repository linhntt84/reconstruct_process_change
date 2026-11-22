### Observed differences

- In the earlier window, A15 and A16 each occurred in every trace, about 1.45 times per trace on average, and repeated within a trace in roughly 30 in 100 traces; in the later window both still occur in every trace but average about 1.8 occurrences per trace and repeat in about 44 in 100 traces. [OCC001, OCC002]
- A16's outgoing flow was redistributed: in the earlier window about 30% of its observed outgoing transitions led to A15 and about 37% led to A42, whereas in the later window about 44% lead to A15 and only about 26% lead to A42; the number of observed outgoing transitions rose from 291 to 361, in line with A16 occurring more often. [DIR001, OCC002]
- The ordered pair "A15 then A16" became less tightly coupled: immediate succession (one step apart) accounts for about 28 in 100 observed pairs in the later window, down from about 43 in 100, with slightly more pairs at distances of two to five steps. [LAG001]
- A few of A16's very rare outgoing transitions, each carrying well under 1% of its traffic, appear or disappear between the windows. [DIR001]

### Inference

Support level: Supported hypothesis

Main hypothesis: in the later window, repetition involving A15 and A16 intensified and their sequencing loosened. In the earlier window both activities ran about 1.45 times per trace and repeated in roughly 30% of traces; in the later window both run about 1.8 times per trace and repeat in about 44% of traces. At the same time, A16 continues back to A15 far more often (about 44% of its outgoing transitions, up from about 30%) and continues onward to A42 less often (about 26%, down from about 37%), while A15 is less often immediately followed by A16 (about 28% of pairs versus 43%), consistent with the extra repetitions being spread out rather than forming tight back-to-back cycles. [OCC001, OCC002, DIR001, LAG001]

Supporting signs: four control-flow items qualified against roughly 0.47 expected by chance across 95 tested units — a count many times the chance expectation — and all four point consistently at the same two activities with agreeing directions. Both activities are present in every trace in both windows, so this is a change in repetition and continuation, not in appearance or disappearance. [OCC001, OCC002, DIR001, LAG001]

Limitations: the lag evidence uses event positions, not clock time, and the evidence cannot show whether the reduced immediate A15→A16 succession reflects other activities being inserted between the two or simply the higher number of occurrences; the drop for A42 is measured only as a share of A16's outgoing transitions, so whether A42's overall execution changed is not established. [LAG001, DIR001]

Other differences: only the appearance or disappearance of A16's very rare outgoing transitions (each well under 1% of its traffic), which is at the level an unchanged process typically produces. [DIR001]