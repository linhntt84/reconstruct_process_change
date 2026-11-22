### Observed differences

- In the earlier window, virtually every trace executed exactly one of three alternative activities: A19 in about 35% of traces (70 of 200), A20 in about 30% (60) and A21 in about 36% (72), and the three almost never appeared together (about 0.5% co-occurrence). In the later window each of them appears in only 1–2 of 200 traces (about 0.5–1%). [OCC001, OCC002, OCC003, REL001, REL002, REL008]
- A26, A27 and A28 are not observed at all in the earlier window (0 of 200 traces), but in the later window each occurs exactly once in every trace (participation 100%, mean about 1 occurrence per trace). [OCC004, OCC005, OCC006]
- In the earlier window, the chosen alternative ran between A44 and A29: A44 preceded A19 in the traces containing both, and A19 preceded A29; the same held for A20 and A21. [REL006, REL007, REL012, REL017]
- In the later window, A44 precedes each of A26, A27 and A28 in about 99 of 100 traces, and each of the three precedes A29 in about 98 of 100. Among themselves, the three appear in both orders in roughly equal shares (about 50/50), so they run without a fixed order. [REL021, REL022, REL024, REL025, REL026, REL027, REL019, REL020, REL023]
- The new activities occupy the region the old ones used to: A26/A27/A28 sit at about 37–38% of the trace position, close to the roughly 37% where A19/A20/A21 appeared before. [POS001, POS004, POS005, POS006]
- The distance from A44 to A29 grew accordingly: before, it was 2 steps in about 84 of 100 traces (3 steps in about 16); after, it is 4 steps in about 82 of 100 (5 steps in about 18). [LAG001]
- A44 and A29 are present in every trace in both windows; A29's position moved slightly later, from about 40% to about 44% of the trace. [POS007, REL021, REL006]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the segment between A44 and A29 was restructured: in the earlier window every trace executed exactly one of the alternatives A19, A20 or A21 (about one third each) between A44 and A29, whereas in the later window that choice has effectively disappeared — A19/A20/A21 run in only about 1 in 100 traces — and A26, A27 and A28 each run exactly once in every trace, after A44 and before A29, in no fixed order among themselves. [OCC001, OCC002, OCC003, OCC004, OCC005, OCC006, REL021, REL022, REL019, REL023]

The participation changes are large and well supported on both sides (70/60/72 traces before versus 1–2 after; 0 before versus 200 after for each new activity), the relational items show the placement of the new block directly, and the A44→A29 distance grew by about two positions, matching the two additional activities now executed. The screening comparison supports that this is not a sampling artefact: 41 control-flow items qualified against roughly 0.4 expected for an unchanged process, far beyond what random re-splits of stable behaviour produce. [OCC001, OCC004, REL021, LAG001]

Limitations: the two windows are finite samples, so this characterises the observed windows rather than proving when or how a change occurred; the residual occurrences of A19/A20/A21 (1–2 traces each) are too few to establish whether these activities remain rare options; and without direct successor evidence the exact edges into and out of the block are not confirmed. A competing explanation the evidence cannot rule out is that the two windows draw from different process variants or populations rather than reflecting a change at a point in time. [OCC002, OCC003, POS002, POS003]

Other differences: in the few later traces that still contain the old activities, their positions differ from before — A19 now appears around 11% of the trace (versus about 37% before), and single observations put A20 at about 88% and A21 at about 73% — but each of these rests on only 1–2 traces. [POS001, POS002, POS003]