### Observed differences

- Both qualifying differences concern the elapsed time between consecutive completions leading into A07, and both lengthened in the later window. For A02→A07, the mean elapsed time rose from about 0.84 hours to about 1.74 hours (median 0.83 vs 1.65 hours; the middle half of pairs moved from roughly 0.75–0.95 hours to 1.58–1.89 hours), based on 30 pairs before and 22 after; fewer than 1 in 1000 random re-splits produced a difference this large. [TWAIT001]
- For A06→A07, the mean elapsed time rose from about 0.11 hours (roughly 6–7 minutes) to about 0.28 hours, the 75th percentile from about 0.17 to 0.47 hours, and the spread grew to roughly two and a half times its earlier size, based on 35 pairs before and 34 after; again fewer than 1 in 1000 random re-splits produced a larger difference. [TWAIT002]
- No control-flow indicator qualified (0 items across 55 tested units, against about 0.27 expected by chance), so no structural, routing or participation difference was detected at these thresholds; the only qualifying items were the two timing items above. [TWAIT001, TWAIT002]

### Inference

Support level: Supported hypothesis

A change in timing around A07 is supported: in the later window, the elapsed time between the completion of A02 and the completion of A07 roughly doubled (mean about 0.84 to 1.74 hours), and the elapsed time between the completion of A06 and the completion of A07 rose from about 0.11 to about 0.28 hours while becoming considerably more variable. [TWAIT001, TWAIT002]

The supporting signs: both items are direct measurements of these intervals, both point in the same direction into A07, each difference exceeded what arose in more than 999 of 1000 random re-splits, and the pair counts behind them are moderate (22–35 per window). The screening yielded 2 time items where only about 0.008 (roughly 1 in 125) were expected if nothing had changed — far beyond what chance produces — while control flow yielded 0 items against about 0.27 expected, so the timing change stands without any detected structural counterpart, which a timing hypothesis does not require. [TWAIT001, TWAIT002]

Limitations: T_WAIT measures elapsed time between consecutive completion events, not pure waiting or service time, so the evidence cannot show whether the added time lies within A07's own execution, in queueing before it, or in work inserted between the two completions. Both items also share A07, so they may reflect one underlying difference rather than two independent confirmations, and the two windows are finite samples. [TWAIT001, TWAIT002]

Other differences: the number of observed A02→A07 pairs fell from 30 to 22 (about 15 vs 11 in 100 traces), but since no control-flow indicator qualified, this may be sampling variation. [TWAIT001]