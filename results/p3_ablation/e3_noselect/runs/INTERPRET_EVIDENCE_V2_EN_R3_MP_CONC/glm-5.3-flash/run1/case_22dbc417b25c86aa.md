### Observed differences

- In the earlier window, A06 was executed in every case — 200 of 200 traces, about one occurrence per trace, typically around one third into the trace. In the later window, A06 does not appear in any of the 200 traces. [OCC001, POS003]
- The flow out of A05 changed completely: before, A05 was always followed by A06; in the later window, A05 is always followed directly by A01. [DIR001]
- A06's own outgoing edge to A01, observed after every A06 before, is no longer seen. [DIR002]
- The gap between A05 and A01 shrank from two positions to one: A01 now immediately follows A05, whereas before one event lay between them. [LAG001]
- The pairwise relations match: before, A06 co-occurred with A01 (A06 first) and with A05 (A05 first) in 100% of traces; in the later window, A01 and A05 each occur without A06 in 100% of traces. [REL001, REL002]
- Event positions shifted slightly: A01's mean position moved from 0.5 to 0.4 and A05's from about 0.17 to 0.2, consistent with traces containing one event fewer. [POS001, POS002]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the step A06 between A05 and A01 is no longer executed: in the earlier window every case ran A05 → A06 → A01, while in the later window A05 leads directly to A01 and A06 is not observed at all. The change is shown directly by the successor change at A05 and the disappearance of A06's edge to A01, and corroborated by A06's participation dropping from 200 of 200 traces to 0, both activity relations collapsing to "one activity only", and the A05→A01 distance shrinking from two positions to one; all nine items describe this single difference, and each difference is larger than in about 199 of 200 random re-splits of the pooled data. [OCC001, DIR001, DIR002, POS003, REL001, REL002, LAG001, POS001, POS002]

One limitation remains: zero participation only means A06 was not observed in the later sample of 200 traces, so the evidence cannot distinguish a complete disappearance of A06 from it still occurring rarely below the detection level. [OCC001, POS003]

Other differences: none — the small position shifts of A01 (mean 0.5 to 0.4) and A05 (about 0.17 to 0.2) follow from the same change rather than being independent differences. [POS001, POS002]