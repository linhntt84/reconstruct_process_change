### Observed differences

- Activity A27 was executed in every trace in the earlier window (participation 100 in 100 traces, about one occurrence per trace); in the later window it appears in only about 51 in 100 traces. [OCC001]
- Three activities that were absent before — A32, A33 and A38 — each now appear in about 49–50 in 100 traces, roughly once per trace when present. [OCC002, OCC003, OCC004]
- Routing out of A26 changed accordingly: before, about 98 in 100 of its outgoing transitions went to A27; in the later window only about 50 in 100 do, with the rest going to A33 (about 17 in 100), A38 (about 16) and A32 (about 15). [DIR001]
- Each of the three new activities leads both to the other two and to A28 in roughly equal shares; for example, out of A32 about 35 in 100 transitions go to A38, 34 to A33 and 28 to A28. [DIR003, DIR004, DIR005]
- The distance from A26 to A28 was 2 steps in about 98 in 100 traces before; in the later window it is 2 steps in about 50 in 100 traces and 4 steps in about 48 in 100. [LAG001]
- The new activities sit around the middle of the trace (mean normalised position about 0.49–0.50 in the later window; no positions observed before). [POS001, POS002, POS003]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that in the later window about half of the executions insert a block of three new activities — A32, A33 and A38 — between A26 and A28, skipping A27, while the other half keep the original A26 → A27 → A28 path. The signs are direct and mutually consistent: A27's participation fell from all traces to about half [OCC001] exactly as the three new activities appeared in about half [OCC002, OCC003, OCC004]; A26 now routes either to A27 or into the new group [DIR001]; the new activities occur mid-trace [POS001, POS002, POS003] and each feeds into A28 [DIR003, DIR004, DIR005]; and the A26–A28 gap doubled from 2 to 4 steps in almost exactly the share of traces in which A27 is skipped [LAG001]. Screening also supports that this is not sampling noise: 13 control-flow items qualified against about 0.5 expected if nothing had changed, a count far too large to arise by chance [OCC001, OCC002, OCC003, OCC004, DIR001, DIR002, DIR003, DIR004, DIR005, POS001, POS002, POS003, LAG001].

Limitations: the evidence does not establish a fixed order inside the inserted block, since each of A32, A33 and A38 leads to the other two and to A28 in similar proportions [DIR003, DIR004, DIR005]; the per-source transition shares rest on roughly 100 observations each and are therefore approximate. An important competing explanation the evidence cannot rule out is that the later window mixes traces from two coexisting process variants rather than reflecting a single process that changed.

Other differences: A27's outgoing profile shifted slightly — transitions to A28 fell from about 99.5 in 100 to about 96 in 100, with small shares now going to A09, A34 and A25 [DIR002].