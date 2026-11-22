### Observed differences

- In the later window, three activities that never appeared in the earlier window — A32, A33 and A38 — each run in about 50 in 100 traces (participation from 0 to about 0.49–0.50), positioned around the middle of the trace (mean relative position about 0.51). [OCC004, OCC005, OCC006, POS003, POS004, POS005]
- A27, previously executed exactly once in every trace (participation 1.0, mean 1.0), now runs in only about 52 in 100 traces. [OCC003]
- The routing after A26 split: earlier, about 95 in 100 of A26's observed outgoing transitions went to A27; in the later window only about 50 in 100 do, with the rest going to A33 (about 18 in 100), A38 (about 17 in 100) and A32 (about 15 in 100). [DIR006]
- The new activities form a small, tightly connected group: the dominant outgoing transitions of each lead to the other two and to A28 (from A32, about 35 in 100 go to A38, 34 to A33 and 27 to A28), and any two of them co-occur in about 49 in 100 traces in both orders, so there is no fixed order among them. [DIR007, DIR008, DIR009, REL028, REL029, REL030]
- A27 and the new group are now near-exclusive alternatives: in the later window A27 runs without the group in about 50 in 100 traces and the group without A27 in about 48–49 in 100, while both appear together in at most about 1–2 in 100; earlier, A27 co-occurred with A28 in every trace. [REL021, REL022, REL023, REL024]
- A28 still occurs in every trace in both windows and is now reached either from A27 (as before) or from the new group, which precedes A28 in about 48 in 100 traces. [POS002, REL025, REL026, REL027]
- A04 became much more frequent and earlier: participation rose from about 19 to 60 in 100 traces (mean occurrences 0.2 → 0.63) and its mean position moved from mid-trace (0.54) to early (0.21); A14 now sends about 54 in 100 of its observed outgoing transitions to A04 (previously about 4 in 100, with about 86 in 100 going to A15, now about 44), and A04's outgoing transitions, previously scattered (largest share about 20 in 100 to A15), now go about 86 in 100 to A15. [OCC001, POS001, DIR001, DIR004, REL001, REL002]
- A06 nearly disappeared, from about 19–20 to about 4 in 100 traces. [OCC002]
- Minor shifts: A10's successor mix changed (few observed transitions in both windows), and A44/A46 became slightly more concentrated on A45/A47. [DIR003, DIR010, DIR011]

### Inference

Support level: Supported hypothesis

The screening flagged 52 control-flow items where only about 0.65 would be expected by chance across the 131 tested units, so the volume of flagged behaviour far exceeds what random re-splits of an unchanged process produce. [screening]

The evidence supports the hypothesis that, in the later window, a new alternative route is executed mid-process: after A26, roughly half of the traces no longer run A27 and instead run the newly observed activities A32, A33 and A38 — executed together in varying order — while the other half still follow the earlier A26 → A27 → A28 route, with both routes rejoining at A28. [OCC003, OCC004, OCC005, OCC006, DIR006, POS003, POS004, POS005, REL022, REL023, REL024]

Supporting signs: A26's observed outgoing transitions split about half to A27 and half to the new activities; the new activities' dominant transitions lead to one another and onward to A28, which still runs in every trace; A27 and the new group are nearly mutually exclusive; and the group still executes after A14, A15 and A26, which continue to appear in essentially every trace. [DIR004, DIR005, DIR006, DIR007, DIR008, DIR009, POS002, REL018, REL021, REL025, REL026, REL027]

Limitations: zero participation in the earlier window means only that A32, A33 and A38 were not observed there, so a very low earlier occurrence (below roughly 1–2 in 200 traces) cannot be excluded; the evidence also cannot show whether this new route and the A04 change below occur in the same traces or in different ones. [OCC004, OCC005, OCC006, REL006, REL007, REL008]

Other differences:
- A04 is now often executed between A14 and A15: it runs in about 60 in 100 traces (previously 19), earlier in the trace, A14 routes about half of its observed outgoing transitions to it (previously almost always directly to A15), and A04 in turn leads overwhelmingly to A15. [OCC001, POS001, DIR001, DIR004, REL001, REL002]
- A06 nearly vanished, from about 19–20 to about 4 in 100 traces. [OCC002]
- A10's successor mix also changed, but both windows rest on few observed transitions, so this is weakly supported. [DIR003]