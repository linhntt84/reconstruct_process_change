### Observed differences

- Activity A01 was not observed in any of the 200 earlier traces; in the later window it appears in about 48 in 100 traces (95 of 200), exactly once per trace in each case. [OCC001]
- When present, A01 sits late in the case: its median relative position is about 0.85 (roughly 85% of the way through the trace), with a middle 50% range from about 0.59 to 1.0. [POS001]
- The pair A01–A18 changed from never occurring in the same trace (A18 alone in about 40 in 100 traces) to co-occurring in about 48 in 100 traces, and in every such case A18 comes before A01; A01 never appears without A18. [REL001]
- A18's outgoing transitions changed accordingly: earlier they spread over many activities (about 19% to A10, about 13% each to A06 and A12) with no transition to A01 at all; in the later window about 65 in 100 of A18's outgoing transitions go to A01. [DIR004]
- A01's own outgoing transitions, unobserved earlier, now fan out over many successors, mainly A10 (about 17%), A07 (about 15%), A12 (about 14%), and A16 and A17 (about 12% each). [DIR001]
- A02 became a repeated activity: mean occurrences per trace rose from about 0.48 to 1.01 while participation stayed near half of traces (48% to 54%), and about 26 in 100 traces now contain A02 more than once, versus none before. [OCC002]
- A08 moved the opposite way: participation is stable (about 47% in both windows) but mean occurrences fell from 0.87 to 0.48 and repetition disappeared (repeated in about 20 in 100 traces before, none after). [OCC003]
- Routing out of A09 shifted toward A02 (about 38% to 65% of its outgoing transitions), while the transition to A07 (about 17% before) is no longer observed. [DIR002]
- Routing out of A14 diversified: the transition to A08 fell from about 63% to 24% of its outgoing transitions, a transition to A15 appeared at about 19%, and the share to A06 rose from about 5% to 21%. [DIR003]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that a new late-stage activity, A01, was introduced into the process and is executed in roughly half of the cases, always after A18. In the earlier window A01 was entirely absent; in the later window it occurs in about 48 in 100 traces near the end of the case, always preceded by A18, and about 65 in 100 of A18's outgoing transitions now lead directly to A01, from which the flow continues to many different downstream activities. [OCC001, POS001, REL001, DIR004, DIR001]

The change is shown directly rather than inferred: participation rises from zero, positional evidence places A01 late in the trace, relational evidence shows a fixed A18-before-A01 order where the two never co-occurred before, and directional evidence shows the new dominant A18→A01 transition. Nine control-flow items qualified in screening against about 0.2 expected without change, so the set as a whole is unlikely under random re-splits of an unchanged process. [OCC001, POS001, REL001, DIR004, DIR001, DIR002, DIR003, OCC002, OCC003]

Limitations: several items describe overlapping aspects of the same behaviour (OCC001 and POS001 both reflect A01's appearance; REL001 and DIR004 both reflect the A18→A01 link), so they are not independent confirmations. Also, zero participation in the earlier window strictly means only that A01 was not observed there; an extremely rare pre-existing activity cannot be fully ruled out, although the coordinated relational and directional shifts make pure sampling noise an unlikely explanation. [OCC001, POS001, REL001, DIR004]

Other differences: A02 became a repeated activity (mean occurrences about 0.48 to 1.01, repeated in about a quarter of traces) while A08 stopped repeating (mean about 0.87 to 0.48, repetition gone); routing shifted from A09 toward A02, and from A14 away from A08 toward A15 and A06. These are not part of the main hypothesis. [OCC002, OCC003, DIR002, DIR003]