### Observed differences

- Activity A01 was completely absent in the earlier window (0 of 200 traces) and in the later window occurs exactly once in every trace (200 of 200), with no repetitions. [OCC001]
- A01 sits very late in the trace order: its median relative position is 1.0 — the final event in at least half the traces — with a mean of about 0.94. [POS001]
- The outgoing flow of A08 was rerouted. In the earlier window its observed transitions went mainly to A05 (about 51 in 100), A02 (about 24) and A06 (about 20); in the later window about 82 in 100 go to A01, leaving only small direct shares to A05 (about 7), A06 (about 7), A02 (about 2) and A04 (about 2). [DIR002]
- Where A01 has an observed successor (53 of its 200 occurrences; in the rest it has no observed successor, consistent with its position as the final event), it leads to A05 in about 45 in 100 cases and to A06 in about 45 in 100, rarely to A02 or A04 — closely mirroring A08's earlier successor profile. [DIR001]
- Before, A05, A06 and A08 always appeared in traces without A01; in the later window each co-occurs with A01 in all 200 traces. A08 precedes A01 in every trace, A05 precedes A01 in about 87 in 100 traces, and A06 precedes A01 in about 75 in 100. [REL001, REL002, REL003]
- The distance from A08 to A05 and A06 grew: for A08→A05, lag 1 fell from about 66 in 100 observed pairs to about 33 while lags 2–4 now account for the rest; for A08→A06, lag 2 fell from about 52 in 100 to about 23 while lag 3 rose from about 27 to about 46 and lags 4–5 appeared. [LAG001, LAG002]
- A05, A06 and A08 each shifted slightly earlier in relative position (mean about 0.52 to 0.44, 0.74 to 0.66, and 0.87 to 0.77 respectively). [POS002, POS003, POS004]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that A01 was added to the process and inserted as the primary successor of A08, taking over the transitions that previously ran directly from A08 to A05, A06, A02 and A04: before, control passed from A08 straight to those activities, while in the later window it passes to A01 in about 82 in 100 of A08's outgoing transitions, with A01 itself leading on to A05 or A06 where a successor is observed, usually as the last activity of the trace. This rests on direct, mutually consistent signs: participation rising from 0 to 200 of 200 traces, the new A08→A01 edge together with A01's successor profile matching A08's previous one, co-occurrence with A05/A06/A08 going from never to always, and the increased A08→A05/A06 distances consistent with A01 standing between them. With 12 qualifying items against roughly 0.1 expected by chance in the control-flow family, the overall pattern is far beyond what an unchanged process typically produces. [OCC001, DIR001, DIR002, REL001, REL002, REL003, LAG001, LAG002, POS001]

Limitations: in about 18 in 100 of A08's outgoing transitions the old direct links to A05/A06/A02/A04 persist, so the rerouting is not complete; A05 and A06 usually precede A01, so in traces where those activities repeat, the evidence cannot pin down A01's position relative to every occurrence; and a wholesale relabelling of an existing activity as A01 would look identical to an insertion in this evidence. [DIR002, REL001, REL002]

Other differences: the small backward shifts in the relative positions of A05, A06 and A08 (means down by roughly 0.08–0.11) are consistent with traces simply becoming one event longer once A01 is present, and are not treated as separate behavioural changes. [POS002, POS003, POS004]