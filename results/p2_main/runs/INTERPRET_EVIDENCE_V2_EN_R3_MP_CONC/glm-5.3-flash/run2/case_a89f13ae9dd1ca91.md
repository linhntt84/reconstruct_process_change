### Observed differences

- In the earlier window, A21, A22 and A23 were mandatory and always executed together: each appeared exactly once in all 200 traces, with no fixed order among themselves (A21 preceded A22 in about 53 of 100 traces and followed it in about 48; the other pairs are similar). In the later window, each of the three appears in only about 1 of 200 traces. [OCC004, OCC005, OCC006, REL025, REL026, REL031]

- In the earlier window, A39 fed this block: its outgoing transitions led to A21, A22 and A23 in roughly equal shares (about 35, 30 and 35 of 100), and A24 followed the block. In the later window, A39's outgoing transitions lead instead to A14 (about 30 of 100), A15 (about 33) and A16 (about 37). [DIR007, REL027, REL028]

- A14, A15 and A16 were not observed at all in the earlier window. In the later window, A14 runs in 30 of 100 traces, A15 in 33 and A16 in 37, each at most once per trace; the three never occur together, so exactly one of them runs in essentially every later trace. [OCC001, OCC002, OCC003, REL001, REL002, REL010]

- In the later window, the chosen activity sits between A39 and A24: A39 precedes it, and it precedes A24, in every trace in which it occurs. [REL006, REL007, REL014, REL015, REL021, REL022]

- The span from A39 to A24 shortened accordingly: it covered 4 event positions in virtually all earlier traces and 2 positions in about 995 of 1000 later traces; A24's mean position moved earlier (about 0.43 to 0.39 of the trace) and A39's slightly later (about 0.31 to 0.33). [LAG010, POS007, POS008]

- A41 appeared in about 59 of 100 earlier traces and about 69 of 100 later traces; earlier it always co-occurred with A21, whereas in the later window it runs without A21. [REL009, REL030]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the segment between A39 and A24 was restructured: the earlier behaviour, in which A21, A22 and A23 each executed once per trace in varying order, was replaced in the later window by exactly one execution of a single activity chosen among A14, A15 and A16, taken in roughly 30, 33 and 37 of 100 traces respectively. [OCC001, OCC002, OCC003, OCC004, OCC005, OCC006, DIR007, LAG010]

This is more than sampling noise: 71 control-flow items qualified against roughly 0.64 expected if nothing had changed, far beyond what random re-splits of stable traces produce. The hypothesis is direct and internally consistent: A39's successor profile switched from the old trio to the new trio, the new activities are mutually exclusive alternatives, they are relationally placed between A39 and A24, the old trio lost participation, and the A39-to-A24 distance halved from 4 to 2 positions. [REL001, REL002, REL010, REL006, REL007, REL014, REL015, REL021, REL022]

Limitations: the evidence cannot show whether A14, A15 and A16 are genuinely new activities or relabelled replacements of A21, A22 and A23; the shares of the new activities rest on 60–74 traces each; and one later trace in 200 still contains the old trio, so their removal is not absolute. [OCC001, OCC002, OCC003, OCC004]

Other differences: A41's participation rose from about 59 to about 69 of 100 traces and it now runs without A21, a shift the main hypothesis does not cover. [REL009, REL030]