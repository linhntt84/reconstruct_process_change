### Observed differences

- In the earlier window, each of the four activities A14, A15, A20 and A21 ran in about 23–26 in 100 traces; they never co-occurred with one another, and their shares sum to about 1.0, so together exactly one of them ran in essentially every trace. In the later window they are nearly absent: A14 appears in 2 of 200 traces, A20 in 1, and A15 and A21 in none. [OCC001, OCC002, OCC003, OCC004, REL001, REL012]

- In the earlier window, the running middle activity always sat inside the span between A23 and A25: A23 preceded it and it preceded A25 in all of its occurrences, it came before A24 in about half of its traces and after A24 in the other half, and each of the four sent about half of its outgoing transitions to A24 and half to A25. In the later window, co-occurrence of each of the four with A23, A24 or A25 drops to about 0–1 in 100 traces. [REL004, REL005, REL006, REL015, REL016, REL018, DIR001, DIR004]

- Routing around A23 and A24 changed accordingly: in the earlier window A23 led to A24 in about half of its outgoing transitions and to one of the four activities in the other half, and A24 led to A25 in about half and to one of the four in the other half; in the later window A23 leads to A24 in about 995 of 1,000 transitions and A24 leads to A25 in about 99 of 100. [DIR005, DIR006]

- The sequence shortened: the distance from A23 to A25 was always three event positions in the earlier window, and in the later window it is two positions (with A24 in between) in about 985 of 1,000 cases; the consecutive pairs A23→A24 and A24→A25, previously direct in only about half of the cases, are now almost always direct. [LAG005, LAG006, LAG007]

- A25 itself still occurs in every trace in both windows, at a slightly earlier relative position in the later window (mean about 0.55 versus 0.56). [POS005]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that the branch in which exactly one of A14, A15, A20 or A21 was executed between A23 and A25 — immediately after A23 in about half of the traces and immediately after A24 in the other half — is no longer taken: in the later window, traces run A23 → A24 → A25 directly, and the four activities together appear in only about 1–2 in 100 traces (3 of 200), down from essentially all traces. The same activities and the same A23–A24–A25 backbone occur in both windows, so this is a shift in how often an existing path is taken, not a replacement of one path by another. [OCC001, OCC002, OCC003, OCC004, DIR005, DIR006, LAG005, LAG006, LAG007]

Supporting signs:
- The number of qualifying items (40) is many times the roughly 0.43 expected for an unchanged process, so the differences as a whole are not what random re-splits of a stable process typically produce. [OCC001, DIR006, REL011, LAG006]
- The participation drop rests on large before-samples (46–52 of 200 traces per activity) against 0–2 after, and the routing shift at A23 and A24 rests on all 200 traces in each window. [OCC002, OCC004, DIR005, DIR006]
- Occurrence, routing, co-occurrence and positional-distance items all describe one and the same shortening of the sequence rather than independent changes. [REL005, DIR005, LAG005, LAG006]

Limitations: the later window still contains a few traces with the branch (2 with A14, 1 with A20), so the evidence shows the branch is now rarely taken, not that it is gone; the evidence also cannot show whether the skipped step's work moved to an activity whose behaviour did not change and that therefore was not flagged. The empty outgoing profiles of A15 and A21 in the later window only reflect that these activities were not observed there. [OCC001, OCC003, DIR002, DIR004]

Other differences: none — the remaining items (the positions and outgoing edges of the four activities, and A25's slightly earlier position) re-describe the same shift. [POS001, POS005, DIR001, LAG001]