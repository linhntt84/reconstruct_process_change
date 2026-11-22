### Observed differences

- The two windows show a clean swap in which activities run between A44 and A29. In the earlier window, A19, A20 and A21 each appeared in about a third of the traces (roughly 35, 30 and 36 in 100) and never repeated within a trace, while A26, A27 and A28 were not observed at all (0 of 200 traces). In the later window, A19, A20 and A21 each appear in only 1–2 of 200 traces, while A26, A27 and A28 run in every trace (200 of 200), about once per case with almost no repetition. [OCC001, OCC002, OCC003, OCC004, OCC005, OCC006]

- In the earlier window, A19, A20 and A21 behaved as alternatives: each pair co-occurred in only about 0.5 in 100 traces, and exactly one of the three ran in nearly every case. In the later window, A26, A27 and A28 always run together (co-occurrence in 100 of 100 traces) and in no fixed order among themselves — for example, A26 precedes A27 in about 51 in 100 traces and follows it in about 49 in 100; each of the three is followed by one of the other two or by A29 in roughly equal shares (about 30–36 in 100 each). [REL001, REL002, REL008, REL019, REL020, REL023, DIR004, DIR005, DIR006]

- A44's routing moved with this swap: earlier, its outgoing transitions went mainly to A19 (about 31 in 100), A21 (about 30) and A20 (about 24); later, they go to A26 (about 31), A27 (about 27) and A28 (about 26). [DIR007]

- The new block sits where the old step did. Earlier, A44 preceded A19/A20/A21 in essentially all traces containing them, and each of the three preceded A29 in nearly all of its occurrences (about 95–99 in 100 of its outgoing transitions led to A29). Later, A44 precedes each of A26, A27 and A28 in about 98–99 in 100 traces, and each of the three precedes A29 in about 98 in 100. [REL007, REL013, REL018, REL006, REL012, REL017, DIR001, DIR002, DIR003, REL022, REL025, REL027, REL021, REL024, REL026]

- The positional distance from A44 to A29 widened: earlier it was mostly 2 steps (about 84 in 100) or 3 steps (about 16 in 100); later it is mostly 4 steps (about 82 in 100) or 5 steps (about 18 in 100), matching three activities now sitting between them. [LAG001]

- A44 and A29 themselves still run in every trace in both windows; A29's mean position shifted only slightly later, from about 0.40 to about 0.44 of the trace. [POS007, DIR007]

### Inference

Support level: Supported hypothesis

The evidence supports a structural change in the segment between A44 and A29: in the earlier window, each case ran exactly one alternative chosen from A19, A20 and A21 between A44 and A29, whereas in the later window that single step no longer occurs and every case runs a block of three activities, A26, A27 and A28, between A44 and A29, with the three executed in varying internal order and each completed before A29. Since A26–A28 were not observed earlier and A19–A21 are nearly unobserved later, this is a replacement of one segment by another (activities withdrawn, others now mandatory in every case), not a shift in how often existing paths are taken. [OCC001, OCC004, DIR007, REL019, REL021, REL022, LAG001]

Supporting signs: the screening flagged 48 control-flow items where fewer than 1 (0.65) would be expected by chance across 131 tested units, so the volume of findings cannot be explained by random sampling of an unchanged process; the change is shown directly by relational and directional evidence rather than by marginals alone; and the occurrence, direction, position and relation indicators all describe the same swap, with the widened A44–A29 distance matching the three activities now inserted. [OCC001, OCC004, DIR007, REL019, REL021, REL022, REL024, REL027, LAG001]

Limitations: the finite windows cannot rule out that both behaviour patterns coexisted before and after and only their mix moved from essentially only the old pattern to only the new one; 0 of 200 versus 200 of 200 makes pure sampling noise implausible, but a rare third pattern could be missed in windows of this size. [OCC001, OCC004]

Other differences: the 1–2 later traces that still contain A19, A20 or A21 show successors (A09/A10, A45, A34) that were negligible earlier, but these profiles rest on one or two traces and cannot be characterised; likewise, the large position shifts reported for A19–A21 in the later window are computed from 1–2 occurrences and should not be read as relocations. [DIR001, DIR002, DIR003, POS001, POS002, POS003]