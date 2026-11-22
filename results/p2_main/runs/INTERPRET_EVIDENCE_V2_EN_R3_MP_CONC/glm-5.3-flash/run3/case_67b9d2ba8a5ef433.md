### Observed differences

- In the earlier window, A01 was not observed in any of the 200 traces; in the later window it occurs in all 200 traces, exactly once per trace. [OCC001]
- In the later window, A01 always appears at the same relative position, about 83% of the way through the trace, and every observed outgoing transition of A01 leads to A03. [POS001, DIR001]
- The hand-over to A03 now goes through A01. Earlier, A05's outgoing transitions led to A03 in about 48 in 100 cases and to A07 in about 52; later they lead to A01 in about 47 and to A07 in about 53, with no direct A05→A03 transitions observed. A07 mirrors this: earlier about 52 to A03 and 48 to A05; later about 53 to A01 and 47 to A05. [DIR002, DIR003]
- Earlier, A03, A05 and A07 each appeared only in traces without A01; later, A01 co-occurs with each of them in every trace, always after A05 and A07 and always before A03. [REL001, REL002, REL003]
- The distance from A05 to A03 grew by one step, from 1–2 steps (split about 48/52) to 2–3 steps (about 47/53); from A07 to A03 it grew from about 52 at one step to about 53 at two steps. [LAG001, LAG002]
- A05 and A07 now appear slightly earlier within traces (median relative position 0.6 to 0.5 for A05, 0.8 to about 0.67 for A07), as expected when an event is added later in each trace. [POS002, POS003]
- Screening qualified 12 control-flow items where about 0.06 would be expected by chance in an unchanged process. [screening]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that A01 was added to the process and is now executed once per case between the A05/A07 stage and A03. In the earlier window, A05 and A07 appeared together in every case in either order and each passed on directly to A03; in the later window, both instead pass to A01, which is in every case directly followed by A03. The one-step increase in the A05→A03 and A07→A03 distances, the new A01→A03 edge, the order relations (A05 and A07 before A01, A01 before A03), A01's fixed late position, and the slight earlier shift of A05 and A07 all describe the same placement of A01 between the A05/A07 pair and A03, and the 12 qualifying items far exceed the roughly 0.06 expected without a change. [OCC001, DIR001, DIR002, DIR003, POS001, POS002, POS003, REL001, REL002, REL003, LAG001, LAG002]

Limitations: zero participation earlier only shows that A01 was not observed in the 200 before-traces, so a previously very rare use of A01 cannot be excluded; and since A03's incoming side is observed only via A05, A07 and A01, the change is pinned down only between the A05/A07 pair and A03, not further upstream. [OCC001, DIR002, DIR003]