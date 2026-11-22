### Observed differences

- In the earlier window, A05 appeared in every trace (about 200 in 200 cases, once per trace, at roughly a quarter into the trace). In the later window, A05 was not observed in any of the 200 traces. [OCC001, POS002]
- A01's outgoing flow changed completely: earlier, A01 was always followed by A05; in the later window, A01 was always followed directly by A02. [DIR001]
- The gap between A01 and A02 shrank accordingly: earlier, A02 followed A01 two steps later in all traces; later, it followed immediately, one step after, in all traces. [LAG001]
- The pairwise relations match: earlier, A01 and A05 always occurred together (A01 first) and A05 and A02 always occurred together (A05 first); later, both pairs appear only as single activities — A01 without A05, and A02 without A05. [REL001, REL002]
- A02 moved earlier in the trace: from about halfway through (mean relative position 0.5) to about a third (0.33), with no variation in either window. [POS001]
- A05's outgoing edge to A02, observed earlier, is no longer observed, consistent with A05 not occurring. [DIR002]
- All eight items describe one coherent picture: the A05 step between A01 and A02 is gone in the later window. [OCC001, POS001, POS002, LAG001, REL001, REL002, DIR001, DIR002]

### Inference

Support level: Supported hypothesis

Main hypothesis: in the later window, A05 is no longer part of the executed flow — it was not observed in any of 200 traces after appearing in all of them — and A01 now leads directly to A02, so A02 takes place earlier in each trace. Earlier, every trace contained the sequence A01 → A05 → A02; in the later window, every observed trace contains A01 → A02 without A05. [OCC001, DIR001, LAG001, REL001, REL002, POS001]

Supporting signs: the change is shown directly by the successor change at A01 and the shortened A01→A02 gap, and consistently by A05's participation dropping from all traces to none, the co-occurrence changes and A02's earlier position; the relational and positional items rest on all 200 traces in each window, and every item's difference is unusual for random re-splits of the pooled data (strength about 0.995). Screening found 8 qualifying control-flow items where roughly 0.04 would be expected without a change, so chance alone cannot explain the set. [DIR001, LAG001, OCC001, REL001, REL002, POS001]

Limitations: zero participation only establishes that A05 was not observed in the later window; the evidence cannot distinguish a complete removal of A05 from it becoming rare (for example an optional step simply never taken in this sample). The eight items also largely reflect the same underlying trace change and are not independent confirmations, and since positions and gaps are measured in event positions, no statement about clock timing is implied. [OCC001, POS002]