### Observed differences

- The elapsed time from the completion of A26 to the completion of A30 roughly doubled: in the earlier window these consecutive completions were about 0.9 hours apart on average (median ~0.93 h), while in the later window they are about 1.8 hours apart (median ~1.79 h) — an increase of about 0.87 hours, a difference this large arises in fewer than 1 of 1,000 random re-splits of the pooled data. The interval was observed 38 times before and 54 times after (200 traces per window). [TWAIT001]
- The elapsed time from the completion of A31 to the completion of A30 also roughly doubled: from about 0.21 hours on average (median ~0.17 h) to about 0.40 hours (median ~0.31 h), an increase of about 0.19 hours, likewise larger than in fewer than 1 of 1,000 random re-splits; it was observed 53 times before and 54 times after. [TWAIT002]
- Both qualifying items are increases and both intervals end at A30, so in the later window the time before A30's completion lengthened relative to both predecessors, A26 and A31. [TWAIT001, TWAIT002]
- No control-flow differences qualified: 0 of 54 tested units, where about 0.27 would be expected by chance in a stable process. [screening]

### Inference

Support level: Supported hypothesis

The evidence supports a timing change around A30: in the later window, the elapsed time between consecutive completions leading into A30 is consistently longer, whether the preceding completion is A26 (about +0.87 hours, from ~0.9 to ~1.8 hours) or A31 (about +0.19 hours, from ~0.2 to ~0.4 hours). [TWAIT001, TWAIT002]

Supporting signs: the time family produced 2 qualifying items where only about 0.009 were expected by chance (19 units tested), far beyond what an unchanged process typically yields; both items agree in direction and share the endpoint A30; both differences exceed essentially all random re-splits; and the control-flow family produced no items (0 vs ~0.27 expected), consistent with a timing change that needs no structural counterpart. [TWAIT001, TWAIT002, screening]

Limitations: T_WAIT measures elapsed time between consecutive completion events, so the evidence cannot distinguish whether A30's own completion was delayed, whether waiting before it grew, or whether other work was interleaved between A26/A31 and A30; and because both items share A30, they may reflect one underlying shift rather than two independent changes. [TWAIT001, TWAIT002]

Other differences: none — no structural, participation or ordering items qualified in either family. [screening]