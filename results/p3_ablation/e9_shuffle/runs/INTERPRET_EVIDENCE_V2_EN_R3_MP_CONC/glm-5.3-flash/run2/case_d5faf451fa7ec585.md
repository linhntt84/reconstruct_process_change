### Observed differences

- In the earlier window, every trace contained A22, A23 and A24 plus exactly one "intermediate" activity: A14 in about 32 of 100 traces, A15 in about 28 and A20 in about 40; these three never appeared together in the same trace. In the later window, A22, A23 and A24 still appear in all traces, while A14, A15 and A20 are not observed in any of the 200 traces. [OCC001, OCC002, OCC003, REL001, REL002, REL006, POS004, POS005]

- Earlier, the route from A22 to A24 spanned three steps: A22 led to A23 in about 55 of 100 outgoing transitions and to one of A14/A15/A20 otherwise; A23 led to A24 in about 45 of 100 and to one of the three otherwise; A24 always sat three positions after A22. In the later window, A22 leads only to A23, A23 leads only to A24, and A24 sits two positions after A22 in every trace. [DIR004, DIR005, DIR001, DIR002, DIR003, LAG001, LAG002, LAG003]

- Earlier, the intermediate activity co-occurred with the fixed activities whenever it ran (for example A20 with A23 in 40 of 100 traces, before A23 in 21 and after it in 19). In the later window these pairs never co-occur: A22, A23 and A24 appear only without A14, A15 or A20. [REL011, REL010, REL012, REL003, REL004, REL005, REL007, REL008, REL009]

- The two fixed activities shifted slightly: A24's mean relative position moved a little earlier (about 0.57 to 0.55 of the trace) and A22's a little later (about 0.46 to 0.47), consistent with the segment between them shortening by one step. [POS004, POS005]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that the intermediate step — exactly one of A14, A15 or A20 per case, executed between A22 and A24 (before or after A23) — is no longer executed, so that cases in the later window run directly from A22 through A23 to A24. Before, this step was mandatory: it appeared in every trace, while in the later window none of the three activities is observed, A22 and A23 each lead to a single successor, and the A22-to-A24 distance compressed from three steps to two. This is a removal/bypass of a block rather than a re-weighting of existing paths, since the step was present in 100 of 100 earlier traces and absent from the observed later ones. [OCC001, OCC002, OCC003, DIR004, DIR005, LAG001, LAG002, LAG003]

The screening found 28 qualifying control-flow items against roughly 0.4 expected for an unchanged process, so the set of differences is far larger than random re-splits produce; occurrence, direction, relation, position and distance indicators all describe this one underlying difference consistently. [screening, REL003, REL005, REL011, POS001, POS002, POS003]

The main competing explanation that cannot be fully ruled out is sampling: zero participation only means A14, A15 and A20 were not observed in the 200 later traces, so a rare variant still executing them could in principle be missed — unlikely, given that every earlier trace contained one of them, but not excluded. The evidence also cannot distinguish whether the steps were removed from the flow altogether or only bypassed in the observed variants. [OCC001, OCC002, OCC003]