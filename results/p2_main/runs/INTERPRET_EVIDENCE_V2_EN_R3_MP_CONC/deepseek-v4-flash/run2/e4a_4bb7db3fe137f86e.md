### Observed differences

- In the later window, the outgoing transitions of activity A06 shifted: the share going to A08 dropped from about 52% to 26%, while the share to A07 rose from about 22% to 42% and the share to A09 rose from about 26% to 32%. [DIR001]
- When A07 follows A06, it now does so immediately (lag 1) in about 78% of cases, up from about 43%; a lag of 2 steps dropped from about 57% to 22%. [LAG001]
- The elapsed time between completion of A01 and A03 increased: mean from about 0.87 to 1.78 hours, median from about 0.86 to 1.83 hours, and the number of observed intervals fell from 42 to 26. [TWAIT001]

### Inference

Support level: Supported hypothesis

The evidence supports a change in the control-flow relationship between A06 and A07: in the later window, A07 is more likely to be the immediate successor of A06, and A08 is less likely to be that successor. This is shown directly by the redistribution of A06's outgoing transitions and by the shortening of the lag between A06 and A07. The two control-flow items are consistent and both involve the same pair of activities, so they reinforce each other rather than being independent confirmations. The screening comparison (2 control-flow items vs 0.3 expected by chance) makes it unlikely that these differences are random sampling artefacts.

Other differences: The waiting time between A01 and A03 roughly doubled in the later window, with fewer observed intervals. This is a separate timing change and is not part of the main hypothesis.

A competing explanation that cannot be fully ruled out is that the observed shift reflects a change in the mix of cases entering A06 rather than a change in the routing logic itself, although the similar support sizes (90 vs 96 traces containing A06) make this less likely.