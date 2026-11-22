### Observed differences

- In the earlier window, five activities — A14, A15, A20, A21 and A22 — each ran in a minority of traces (roughly 17–25 in 100, with A21 the most frequent at about 25 in 100). In the later window, none of the five appears in any of the 200 traces. [OCC001, OCC002, OCC003, OCC004, OCC005]
- Earlier, these five behaved as mutually exclusive alternatives: no trace contained more than one of them, A38 always fed into exactly one of the five, and each of the five always led on to A23. [REL001, REL010, REL015, REL019, DIR006, DIR001, DIR005]
- In the later window, all of A38's observed outgoing flow goes directly to A23, and the A38→A23 gap is always one step, whereas earlier it was always two steps (A38 → one of the five → A23). [DIR006, LAG001]
- A23 still occurs in every trace in both windows and now sits slightly earlier within traces (mean relative position about 0.40 earlier vs about 0.38 later). [POS006]
- A41 and A42 now appear in about 67 in 100 traces, up from about 53 in 100 earlier, and they no longer co-occur with any of the five activities that disappeared. [REL008, REL013, REL017, REL023, REL025]
- The elapsed time between consecutive completion events from A16, A17, A18 or A19 to A28 roughly doubled, from about 1.0 hour to about 2.1 hours, consistently across all four pairs (46–53 observations per window). [TWAIT001, TWAIT002, TWAIT003, TWAIT004]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that the block of five alternative activities (A14, A15, A20, A21, A22) between A38 and A23 is no longer executed: in the earlier window A38 branched to exactly one of the five (about 17–25 in 100 of its outgoing transitions each) and each of the five always led to A23, while in the later window none of the five is observed and A38 leads directly to A23 in every case. [OCC001, OCC004, DIR006, LAG001, REL019]

This hypothesis is shown directly by the successor profile of A38 and by the A38→A23 distance change from two steps to one, not inferred from participation alone; the five disappearances are mutually consistent (they were alternatives, so they vanish together), and the volume of flagged items — 44 control-flow items against roughly 0.5 expected without change, and 4 time items against roughly 0.01 — far exceeds what an unchanged process would produce. [DIR006, LAG001, OCC001, TWAIT001]

A limitation: zero participation only means the activities were not observed, so the evidence cannot distinguish a complete removal of the five activities from a bypass in which the path through them is merely skipped, nor rule out that they still occur extremely rarely in the later window. [OCC001, OCC002, OCC003, OCC004, OCC005]

Other differences:
- A timing change in its own right: the elapsed time between consecutive completion events from A16/A17/A18/A19 to A28 rose by about 1 hour (from about 1.0 to about 2.1 hours); the evidence cannot show whether this is connected to the structural change above. [TWAIT001, TWAIT002, TWAIT003, TWAIT004]
- A41 and A42 participation increased from about 53 to about 67 in 100 traces; the evidence does not show what drives this increase. [REL008, REL013, REL017, REL023, REL025]
- A23 occurs slightly earlier within traces in the later window, consistent with shorter traces after the block's removal rather than a relocation of A23 itself. [POS006]