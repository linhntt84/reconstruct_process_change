### Observed differences

- In the earlier window, activity A01 was not observed in any of the 200 traces; in the later window it occurs exactly once in every trace (200 of 200), always at the same relative position (mean 1.0 with no spread). [OCC001, POS001]
- Activity A04 is present in every trace in both windows, but its relative position moved from 1.0 in the earlier window to 0.75 in the later one, with the same value in every trace on each side. [POS002]
- In the earlier window the two activities never occurred together: in 200 of 200 traces A04 appeared without A01. In the later window they occur together in 200 of 200 traces, always with A04 before A01. [REL001]
- In the earlier window no outgoing transition from A04 was observed; in the later window every observed outgoing transition of A04 leads to A01 (share 1.0, across 200 traces). [DIR001]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that A01 has become a mandatory step executed directly after A04: in the earlier window, traces contained A04 with no observed successor and no A01, whereas in the later window every trace runs A04 followed by A01, and A04's relative position moved earlier (1.0 to 0.75), consistent with a step having been appended after it. [REL001, DIR001, OCC001, POS001, POS002]

This is more than sampling noise: five control-flow items qualified where roughly 0.02 (about 1 in 50) would be expected by chance at these thresholds, and each item shows an empirical strength of about 0.995, meaning a difference this large arose in only about 1 in 200 random re-splits of unchanged data. [OCC001, POS001, POS002, REL001, DIR001]

Limitation: zero participation in the earlier window only shows that A01 was not observed then, so the evidence cannot distinguish a genuinely new activity from an existing step that was previously never executed and has now become mandatory in every case. [OCC001]

The five items are overlapping views of a single trace-level change rather than independent confirmations, and positions are event positions rather than clock times; the placement claim nevertheless rests on direct relational evidence — the A04→A01 edge and the fixed A04-before-A01 order. [REL001, DIR001, POS001]