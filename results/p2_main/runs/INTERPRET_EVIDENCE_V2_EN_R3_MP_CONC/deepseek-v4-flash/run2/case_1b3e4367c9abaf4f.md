### Observed differences

- In the later window, activity A01 appears in every trace (100% participation, mean 1.0) whereas it was absent in the earlier window (0% participation). It is positioned near the end of traces (mean position 0.93). [OCC001, POS001]
- Activities A02, A06 and A12 become mandatory: participation rises from 48%, 52% and 52% respectively to 100% in the later window. A06 also increases its mean occurrences from 1.085 to 2.105 per trace, with recurrence in 53% of traces (up from 26%). [OCC002, OCC003, OCC005]
- A11 participation rises from 26% to 53%, with mean occurrences from 0.565 to 1.105. [OCC004]
- A02's outgoing transitions shift: in the earlier window it went to A03 (56%) and A07 (44%); in the later window it goes to A06 (90.5%) with small shares to A12, A07, A11 and A03. [DIR002]
- A01 has no outgoing transitions in the earlier window; in the later window it goes to A15 (46%) and A16 (54%). [DIR001]
- A15 and A16, which previously went exclusively to each other (A15→A16, A16→A15), now also go to A01 in about half of the cases (A15→A01 50%, A16→A01 51%). [DIR004, DIR005]
- A01 co-occurs with many activities in the later window, whereas it was absent before; for example, A01 and A02 co-occur in 100% of traces with A02 before A01, and A01 with A03, A05, A06, A07, A12, A15, A16 all co-occur in 100% of traces. [REL001, REL002, REL003, REL004, REL005, REL007, REL008, REL009]
- The lag between A02 and A03/A07 increases: in the earlier window they were 1-2 steps apart, in the later window 3-5 steps apart. [LAG001, LAG003]
- The lag between A15 and A16 changes from always 1 step to 1 or 2 steps (about 63-65% at 1, 35-37% at 2). [LAG007, LAG008]

### Inference

Support level: Supported hypothesis

The evidence supports a structural change: a new activity A01 was added and is now executed in every case, and it participates in a loop with A15 and A16. In the earlier window A01 was completely absent; in the later window it appears in all 200 traces, has outgoing transitions to A15 and A16, and receives transitions from A15 and A16 in about half of the cases. The co-occurrence of A01 with many other activities and its position near the end are consistent with this. The large number of evidence items (58 vs 0.53 expected by chance) makes a chance explanation unlikely. A competing explanation that cannot be fully ruled out is that A01 existed but was simply not observed in the earlier window; however, its complete absence in 200 traces and presence in all 200 after makes this implausible.

Other differences: A02's successor changed from A03/A07 to A06, and several activities (A02, A06, A12) became mandatory, with A06 also repeating more often. These are separate from the A01 introduction.