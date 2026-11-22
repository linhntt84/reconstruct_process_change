### Observed differences

- In the earlier window, the elapsed time between the completion of A20 and the completion of A31 was typically about 0.83 hours (middle half of cases roughly 0.70–0.94 hours); in the later window it was typically about 1.66 hours (roughly 1.50–1.82). The typical gap roughly doubled, and the whole distribution shifted upward, including its spread. This pair occurs in about 38 of 200 traces in each window. [TWAIT001]
- The elapsed time from A37 to A31 was typically about 0.07 hours (about 4 minutes) before and about 0.17 hours (about 10 minutes) after — also roughly doubled, with the upper quartile rising from about 0.11 to about 0.26 hours. This pair occurs in about 43 of 200 traces before and 42 of 200 after. [TWAIT002]
- Both timing differences are larger than in all but about 1 in 2000 random re-splits of the pooled data. [TWAIT001, TWAIT002]
- No control-flow indicator passed the screening threshold (0 items against about 0.28 expected by chance), so no structural difference was flagged. [screening]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility of a timing change centred on A31: in the later window, the elapsed time between the completion of its predecessors A20 and A37 and the completion of A31 is consistently about twice as long as before (A20→A31 median about 0.83 → 1.66 hours; A37→A31 about 0.07 → 0.17 hours). Supporting signs: the time family produced 2 qualifying items where only about 0.02 would be expected if nothing had changed, both items point in the same direction at the same target activity, the shifts cover the entire distribution rather than only extreme cases, and the control-flow family produced no items, so a structural reorganisation is not indicated. Limitations: both items share A31 and may reflect a single underlying difference rather than two independent ones; T_WAIT measures elapsed time between consecutive completion events, so the evidence cannot show whether the extra time comes from longer durations of the activities themselves or from the interval between them; and each pair is observed in only about one in five traces, so the change is characterised on a subset of cases. A competing explanation the evidence cannot fully rule out is a changed mix of traces (for example, different paths into A31) that lengthens these gaps without any timing change on the individual transitions; the clean control-flow screening makes this less likely but does not exclude it.

Other differences: none — no further indicators passed the screening thresholds. [screening]