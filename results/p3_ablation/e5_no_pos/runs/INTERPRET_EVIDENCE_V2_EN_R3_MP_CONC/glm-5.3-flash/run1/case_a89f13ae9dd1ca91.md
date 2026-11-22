### Observed differences

- The always-executed group disappeared: before, A21, A22 and A23 each ran exactly once in all 200 of 200 traces, in no fixed order among themselves; in the later window each appears in only about 1 in 200 traces. [OCC004, OCC005, OCC006, REL025, REL026, REL031]
- Three previously unobserved activities now occupy that slot as alternatives: A14 runs in 60 of 200 later traces (30%), A15 in 65 (about 33%) and A16 in 74 (37%), each at most once per trace, and the three never occur together — in about 995 of 1,000 later traces exactly one of them runs. [OCC001, OCC002, OCC003, REL001, REL002, REL010]
- The frame around the segment is unchanged: A39 and A24 occur in every trace in both windows. Before, A39 always preceded the A21–A23 group and A24 always followed it; in the later window A39's outgoing transitions go to A14, A15 and A16 in shares matching their participation (about 30/33/37), and the chosen activity in turn precedes A24. [DIR007, REL027, REL028, REL006, REL007, REL014, REL015, REL021, REL022]
- The number of events between A39 and A40 shrank: before, A40 followed A39 at a distance of 4 event positions in essentially all traces; in the later window the distance is 2 positions in about 995 of 1,000 cases, consistent with the intervening group shrinking from three activities to one. [LAG010]
- A41's participation rose from about 59 in 100 traces to about 69 in 100, and it now typically runs without A21, whereas before it always co-occurred with A21. [REL030, REL009, REL017]

### Inference

Support level: Supported hypothesis

In the later window, the segment between A39 and A24 changed from executing the group A21, A22, A23 — all three in every case, in varying order — to executing exactly one of the three previously unobserved activities A14, A15 or A16 per case, with A39 still preceding and A24 still following the chosen activity. The support is direct and consistent: participation flips from 100% to about 0.5% for the old trio and from 0% to 30–37% for the new trio; successor evidence shows A39 now leading to A14/A15/A16 and those activities leading to A24; the new trio is mutually exclusive; and the A39-to-A40 event distance shrank from 4 to 2, matching the removal of two intervening activities. Chance is also implausible as a whole: 62 control-flow items qualified where about 0.6 would be expected without a change, roughly 100 times as many. [OCC001, OCC002, OCC003, OCC004, OCC005, OCC006, DIR001, DIR002, DIR003, DIR007, REL001, REL002, REL010, REL006, REL007, LAG010]

Limitations: the evidence cannot show whether A14/A15/A16 are genuinely new steps or relabelled successors of A21/A22/A23, nor fully rule out that the two windows sample different case mixtures; the after-window routing detail for A21–A23 itself rests on a single trace. [OCC004, DIR004]

Other differences: A41 became more frequent (about 59 vs 69 in 100 traces) and now typically occurs without A21, its earlier constant companion; this participation increase is not explained by the main hypothesis. [REL030, REL017, REL024]