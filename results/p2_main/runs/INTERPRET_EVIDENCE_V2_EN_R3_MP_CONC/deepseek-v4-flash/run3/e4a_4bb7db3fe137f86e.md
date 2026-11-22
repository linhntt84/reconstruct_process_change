### Observed differences

- In the later window, the outgoing distribution from A06 shifted: the share going to A08 dropped from about 52% to 26%, while A07 rose from about 22% to 42% and A09 from 26% to 32%. [DIR001]
- In the later window, the gap between A06 and A07 shortened: the share of traces where A07 follows A06 within one step rose from about 43% to 78%, while the two-step share fell from 57% to 22%. [LAG001]
- In the later window, the elapsed time between A01 and A03 increased: the mean rose from about 0.87 hours to 1.78 hours, and the median from 0.86 to 1.83 hours. [TWAIT001]

### Inference

Support level: Supported hypothesis

The evidence supports a change in the routing after A06: in the later window, A06 more often leads directly to A07 and less often to A08, and the A06–A07 pair occurs more tightly together. This is directly shown by the shift in A06's outgoing shares [DIR001] and by the shortened step distance between A06 and A07 [LAG001]. The two indicators are consistent and the number of qualifying control-flow items (2) is well above the chance expectation (0.3). A competing explanation that the LAG change is merely a side effect of the A08 decrease is unlikely because both indicators point to a stronger A06–A07 link.

Other differences: The waiting time between A01 and A03 roughly doubled in the later window [TWAIT001]. This is a separate timing change, supported by a single strong item (empirical strength 0.9995) but based on moderate sample sizes (42 before, 26 after). It is not part of the main routing hypothesis.