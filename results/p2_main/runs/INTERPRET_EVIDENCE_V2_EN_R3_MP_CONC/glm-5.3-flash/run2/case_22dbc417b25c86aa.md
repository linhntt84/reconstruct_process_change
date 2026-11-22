### Observed differences

- Activity A06 was executed exactly once in every case in the earlier window (in 200 of 200 traces, mean 1.0 occurrence per trace, always at about one third of the trace); in the later window it is not observed at all (0 of 200 traces). [OCC001, POS003]
- The successor of A05 changed completely: earlier, all of A05's outgoing flow went to A06; in the later window, all of it goes directly to A01. A06's own outgoing edge to A01, which earlier carried all of its flow, is no longer observed. [DIR001, DIR002]
- The pairwise relations changed accordingly: earlier, A05 and A06 always co-occurred with A05 first, and A06 and A01 always co-occurred with A06 first; in the later window neither pair co-occurs — only A05, and only A01, appear. [REL001, REL002]
- The distance from A05 to A01 shrank from two steps to one: earlier A01 followed A05 with a gap of 2 positions (A06 sitting in between); in the later window A01 immediately follows A05. [LAG001]
- A01 and A05 shifted slightly within the trace: A01's mean position moved from 0.5 to 0.4 of the trace length and A05's from about 0.17 to 0.2, consistent with traces now containing one event fewer. [POS001, POS002]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that A06 was dropped from the flow between A05 and A01: in the earlier window every case ran A05 → A06 → A01, while in the later window A05 leads directly to A01 and A06 is not executed in any of the 200 sampled cases. This structural difference is shown directly by the successor change at A05, by the disappearance of the A05–A06 and A06–A01 co-occurrences, and by the A05→A01 gap shrinking from two steps to one; the disappearance of A06 and the small position shifts of A01 and A05 are consistent with the same difference. All nine qualified items come from a screening that expected only about 0.04 items by chance without a change, and every item describes this one difference rather than scattered unrelated effects. [OCC001, DIR001, DIR002, POS001, POS002, POS003, REL001, REL002, LAG001]

Limitations: zero participation only shows that A06 was not observed in the later window, so the evidence cannot distinguish a structural removal of A06 from A06 remaining possible but simply never taken in this sample — that competing explanation cannot be ruled out. Positions are event positions, not clock time, so no claim about timing is implied, and activities other than A01, A05 and A06 were not flagged, so behaviour elsewhere is only unchanged within the tested thresholds. [OCC001, POS001, POS002]