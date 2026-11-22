### Observed differences

- In the earlier window, A01, A05, A08 and A09 each took part in about 45% of traces (about 90 of 200 cases); in the later window, each takes part in about 52–53% (about 104–106 of 200). A06 shows the same rise in participation (about 45% → 53%) while its occurrences per trace stay roughly flat (about 0.97 → 0.94). [OCC001, OCC005, OCC006, OCC008, OCC009]
- In the later window, A02, A04 and A11 each take part in about 47–48% of traces (94–96 of 200), down from about 55% (109–110 of 200) in the earlier window. [OCC002, OCC004, OCC011]
- A03 and A12 take part in fewer traces (about 55% → 47%) and repeat less often: their mean occurrences per trace fall from about 1.2 to about 1.0. [OCC003, OCC012]
- A07 and A10 keep roughly the same share of traces (about 25%) but occur less often per trace (A07 about 0.52 → 0.41; A10 about 0.66 → 0.52), i.e. fewer repetitions within a case. [OCC007, OCC010]
- The clearest routing change sits at A06: in the earlier window about 53% of its outgoing transitions led to A07 and about 44% to A08; in the later window about 41% lead to A07 and about 53% to A08, with a small flow to A09 (about 4%). [DIR006]
- Flows into A03 recede: the share of A09's outgoing transitions leading to A03 falls from about 48% to about 41% (relatively more goes to A01 and A07), and the share of A02's outgoing transitions leading to A03 falls from about 51% to about 42% (relatively more goes to A01 and A06). [DIR009, DIR002]
- A07 still leads back to A06 after almost every execution, but slightly less exclusively (about 99% of its outgoing transitions before, about 96% after), with small flows to A05 (about 2%) and A09 (about 1%) in the later window. [DIR007]
- The dominant directly-follows relations are otherwise essentially unchanged (A03→A12 about 97% in both windows, A10→A03 about 98%, A11→A04 about 99–100%), so no comparable reordering of activities is apparent. [DIR003, DIR010, DIR011]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that, in the later window, existing paths are taken with different frequencies: continuations from A06 shifted from the back-and-forth with A07 toward A08, and flows into A03 receded from both A09 and A02. [DIR006, DIR009, DIR002] Consistent with this rerouting, the side of the process containing A01, A08, A05 and A09 is executed in more traces (about 45% → 52–53%), A02, A04 and A11 in fewer traces (about 55% → 47–48%), and the repeating sequences through A03–A12 (with A10 downstream) and between A06 and A07 repeat less within traces. [OCC001, OCC002, OCC003, OCC004, OCC005, OCC007, OCC008, OCC009, OCC010, OCC011, OCC012]

The routing shift at A06 is measured on about 190 outgoing transitions per window and is larger than about 97 in 100 random re-splits, and the shift in A07's outgoing profile points the same way; every activity involved is observed in about 25–55% of traces in both windows, and the dominant successor relations are stable, so this reads as a shift between existing paths rather than activities appearing, disappearing or being reordered. [DIR006, DIR007, DIR003, DIR010, DIR011, OCC001, OCC002, OCC003, OCC004, OCC005, OCC007, OCC008, OCC009, OCC011, OCC012]

The evidence cannot fully rule out sampling variation: with 200 traces per window, participation differences of about 0.07 can arise without a change, and no baseline for the expected number of flagged items is provided; the directional coherence across related activities and the strongly supported shift at A06 argue against pure chance. The identical statistics of the pairs A01/A08, A05/A09, A04/A11 and A03/A12 also show these activities move together, so there are fewer independent changes than the number of evidence items suggests. [OCC001, OCC003, OCC004, OCC005, OCC008, OCC009, OCC011, OCC012]

Other differences: the successor profiles of A04 and A08 differ between the windows (A04 led only to A09 before and to A09 or A05 after; A08's split between A05 and A09 moved slightly), but they rest on only 1–2 and 3–8 outgoing transitions respectively and are too weak to interpret. [DIR004, DIR008]