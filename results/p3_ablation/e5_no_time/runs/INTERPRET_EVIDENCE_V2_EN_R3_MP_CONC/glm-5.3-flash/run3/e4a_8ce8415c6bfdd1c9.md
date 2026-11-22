### Observed differences

- Activity A22 ran in every one of the 200 earlier traces but in only about 57 in 100 traces in the later window (about 113 of 200); it occurs at most once per trace in both windows. [OCC001]
- Activities A27, A28, A33, A34 and A35 were not observed in any earlier trace; in the later window each appears in about 44 in 100 traces (87 of 200), once per trace, around the middle of the trace (mean relative position about 0.52). [OCC002, OCC003, OCC004, OCC005, OCC006, POS002, POS003, POS004, POS005, POS006]
- Before, A21's only observed successor was A22 (100% of its outgoing transitions). Afterwards about 57 in 100 of those transitions still go to A22, with the remainder split roughly evenly over the five new activities (about 7–11% each). [DIR001]
- Each new activity's observed outgoing transitions lead to A23 and to the other four new activities in broadly similar shares (for A27, for example: about 28% to A28, 25% to A34, 17% to A23, 17% to A35, 13% to A33). [DIR002, DIR003, DIR004, DIR005, DIR006]
- Before, A21, A22 and A23 always occurred together in the fixed order A21 → A22 → A23. Afterwards, in about 43 in 100 traces A21 occurs without A22 [REL001], A23 occurs without A22 having run [REL007], and A21, the new activities and A23 occur together with A21 first and A23 last [REL002, REL003, REL004, REL005, REL006, REL013, REL014, REL015, REL016, REL017]. The new activities never co-occur with A22. [REL008, REL009, REL010, REL011, REL012]
- Pairs among the five new activities co-occur in every trace containing them, but both orders appear in similar proportions (about 20 in 100 traces each way), i.e. they run without a fixed order between them; before, neither activity of any such pair was observed. [REL018, REL019, REL020, REL021, REL022, REL023, REL024, REL025, REL026, REL027]
- A21's mean relative position moved slightly earlier, from about 0.49 to about 0.46. [POS001]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that a new alternative branch was inserted between A21 and A23: in about 44 in 100 later cases the A22 segment is bypassed, and A21 instead leads to the five activities A27, A28, A33, A34 and A35, which run between A21 and A23 without a fixed order among themselves before reaching A23; in the remaining about 57 in 100 cases the original sequence A21 → A22 → A23 runs unchanged, and A23 itself continues to occur in every trace. [OCC001, OCC002, OCC003, OCC004, OCC005, OCC006, DIR001, DIR002, DIR003, DIR004, DIR005, DIR006, REL001, REL007, REL013, REL018]

Supporting signs: 45 control-flow items qualified against roughly 0.5 expected if nothing had changed, so chance sampling cannot account for the set as a whole; participation, routing, relational and positional evidence all describe the same behaviour with one consistent share (about 43.5% of traces); and the new activities always co-occur with A21 and A23 while never co-occurring with A22, which places them precisely in the bypassed segment. [DIR001, REL002, REL008, REL013, REL018]

Limitations: zero participation in the earlier window shows only that the new activities were not observed then, so a rare pre-existing path that later became frequent cannot be fully ruled out; the mixed ordering shows the five activities lack a fixed order, but whether they execute in parallel cannot be decided from these indicators. [OCC002, OCC003, OCC004, OCC005, OCC006, REL018, REL019, REL020, REL021, REL022, REL023, REL024, REL025, REL026, REL027]

Other differences: A21's mean relative position shifted slightly earlier (about 0.49 to 0.46), consistent with more activity now following it in the new branch. [POS001]