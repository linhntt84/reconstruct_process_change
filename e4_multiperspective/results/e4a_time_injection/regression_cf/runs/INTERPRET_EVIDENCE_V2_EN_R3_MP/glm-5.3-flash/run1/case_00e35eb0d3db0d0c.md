### Observed differences

- **A25 and A26 now repeat within cases.** Earlier, each occurred exactly once in every trace (mean 1.0 occurrences, participation 100 in 100, no repetition). In the later window both still occur in every trace, but each averages about 1.6 occurrences and recurs within a trace in about 37 in 100 cases (recurrence support rose from 0 to about 0.37). [OCC001, OCC002]

- **A26 gained a transition back to A25.** Earlier, every observed outgoing transition of A26 went to A20; in the later window about 36 in 100 go to A25 (not observed before) and about 64 in 100 to A20. The 312 outgoing transitions observed after, versus 200 before, match A26's higher occurrence rate. [DIR002, OCC002]

- **The fixed order and adjacency of the pair loosened.** Earlier, A25 and A26 always co-occurred with A25 strictly before A26, immediately adjacent (lag 1 in 100 in 100 cases). In the later window the strict A25-before-A26 order holds in about 64 in 100 traces while about 37 in 100 show the pair interleaved or repeated, and only about 37 in 100 of the measured pairs are adjacent, with gaps of 3 positions (about 5 in 100) and 5 positions (about 1 in 100) appearing. [REL001, LAG001]

- **Routing shares at A01 shifted.** A01 → A04 fell from about 42 to about 20 in 100 outgoing transitions, A01 → A05 rose from about 24 to about 45, and A01 → A03 stayed at about 34; all three successors were well observed in both windows. [DIR001]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the step pair A25 → A26 changed from a single, fixed, adjacent execution to a repeatable one: previously both activities ran exactly once per case with A25 immediately before A26 and A26 always continuing to A20, whereas in the later window both recur in about 37 in 100 traces (mean occurrences about 1.6 versus 1.0), A26 flows back to A25 in about 36 in 100 of its outgoing transitions, the strict A25-before-A26 order holds in only about 64 in 100 traces, and the two are adjacent in only about 37 in 100 cases. [OCC001, OCC002, DIR002, REL001, LAG001]

This is supported directly and consistently: the new A26 → A25 transition, the shift from fixed order to interleaved/repeated execution, the loss of adjacency and the recurrence increase for both activities all describe the same pattern, six items qualified against roughly 0.29 expected by chance at these thresholds (about twenty times the expectation), and each item exceeds about 995 in 1,000 random re-splits of the pooled data. The recurrence appears in roughly 73 of the 200 later traces, so a rare variant surfacing by chance is unlikely. Limitations: these items are largely views of the same trace behaviour rather than independent confirmations, and the exact shape of the repetition remains open — A25's outgoing transitions were not profiled, and the position gaps of 3 and 5 suggest other activities can sit between repeats, so a strict A25 → A26 → A25 cycle cannot be distinguished from a looser interleaving. [OCC001, OCC002, DIR002, REL001, LAG001]

Other differences: At A01, existing paths are taken with different frequencies (A01 → A04 down from about 42 to about 20 in 100, A01 → A05 up from about 24 to about 45, A01 → A03 stable), which the evidence cannot link to the A25/A26 repetition; as a single item it could also still be a sampling difference that a stable process occasionally produces. [DIR001]