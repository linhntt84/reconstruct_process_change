### Observed differences

- Resource assignment for activities A01, A03 and A07 was redistributed. In the earlier window, a small set of resources carried most of the work: User_19 handled about 11% of A01 and A03, and User_83, User_101, User_102, User_124 and User_90 together handled about 44% of A07. In the later window, those shares dropped to zero or near zero, new resources appeared (User_126 took about 13% of A07, User_28 about 5% of A01 and A03), and the "OTHER" pool (resources with small individual shares) rose from about 45% to 54% for A01, from 45% to 53% for A03, and from 18% to 31% for A07. [ASSIGN001, ASSIGN002, ASSIGN003]
- Activity A24 occurred less often: mean occurrences per trace fell from about 0.60 to 0.36, trace participation from 40% to 29%, and recurrence from 14% to 6%. [OCC001]

### Inference

Support level: Supported hypothesis

The evidence supports a hypothesis that resource allocation for activities A01, A03 and A07 changed: work previously done by a set of resources (e.g., User_19, User_15, User_17, User_60) was redistributed to other resources (e.g., User_28, User_38, User_51, User_126) and to a larger "OTHER" pool. The three resource items far exceed the chance expectation for the resource family (3 items vs 0.004 expected), and all three activities show the same direction of change. [ASSIGN001, ASSIGN002, ASSIGN003]

Other differences: Activity A24 decreased in occurrence (mean per trace from 0.60 to 0.36, participation from 40% to 29%). This is a single control-flow item against 0.16 expected by chance, so it is within what an unchanged process typically produces and does not support a separate hypothesis. [OCC001]

A competing explanation the evidence cannot rule out is that the redistribution reflects a change in the composition of cases reaching these activities rather than a change in how resources are assigned; the evidence does not include structural or timing indicators that would distinguish these.