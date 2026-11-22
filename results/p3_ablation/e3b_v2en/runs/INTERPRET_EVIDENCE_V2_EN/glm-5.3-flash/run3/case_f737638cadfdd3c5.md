### Observed differences

- In the earlier window, A19, A20 and A25 never appear in any of the 200 traces. In the later window they run in about 37, 29 and 34 in 100 traces respectively (74, 57 and 68 of 200), each occurring at most once per trace. [OCC001, OCC002, OCC003]
- The three activities are mutually exclusive: in the later window essentially every trace executes exactly one of them — A19 and A20 never co-occur, A20 and A25 never, and A19/A25 co-occur in only about 1 in 200 traces. [REL001, REL002, REL007]
- A41's outgoing transitions shifted from about 93 in 100 going to A26 in the earlier window to about 92 in 100 going to the three new activities in the later window (A19 about 34, A25 about 31, A20 about 27), leaving A26 with about 1 in 100. [DIR004]
- Each of A19, A20 and A25 leads to A26 in about 96–98 in 100 of its observed outgoing transitions. [DIR001, DIR002, DIR003]
- Wherever one of the three runs, it sits after A41 and before A26 (and before A31): A41 precedes A19, A20 and A25 in about 37, 28 and 33 in 100 traces, and each of them precedes A26 in the same traces. [REL006, REL010, REL014, REL003, REL008, REL011, REL004, REL009, REL012]
- The distance from A41 to A26 changed from one step in about 94 in 100 cases before to two steps in about 90 in 100 cases after. [LAG002]
- The new activities sit at roughly 0.35–0.36 of the trace length; A26 and A31 keep 100% participation in both windows but shifted slightly later (mean +0.02 and +0.015) with narrower spread. [POS001, POS002, POS003, POS004, POS005]
- Separately, the A31→A35 distance moved from one step (about 55 in 100 cases) to two steps (about 62 in 100 cases). [LAG001]
- Every flagged item shows a difference larger than in about 995 of 1,000 random re-splits of the pooled windows, so these differences are unusual even for finite samples of this size. [OCC001, DIR004, REL003, LAG002]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that, in the later window, an exclusive three-way choice among A19, A20 and A25 was inserted between A41 and A26 (upstream of A31): A41 now routes about 92 in 100 of its outgoing transitions to exactly one of the three, each of the three leads almost always back to A26, and the A41→A26 distance moved from one step to two. The placement is shown directly by relational, directional and distance evidence rather than by participation alone, the picture is consistent across all items, and the item count (28 versus roughly 0.57 expected by chance in a stable process) cannot be explained by sampling as a whole. [DIR004, DIR001, REL006, REL003, LAG002, OCC001]

The main competing explanation the evidence cannot rule out is a routing-frequency shift on a path that already existed: zero participation in the earlier window only shows that A19, A20 and A25 were not observed there, so a previously rare variant now executed far more often would look identical, and variant frequencies can differ between finite samples even without a structural addition. The A31→A35 distance change is not explained by this insertion and may be a separate difference, and many items describe the same traces (for example the A19 participation, direction and relation items), so they are not independent confirmations. [OCC001, OCC002, OCC003, LAG001, REL001]