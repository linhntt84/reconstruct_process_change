### Observed differences

- In the later window, A36's outgoing transitions shifted: the share to A37 rose from about 34% to 62%, while the share to A33 fell from about 59% to 38%; the small shares to A08, A19, A23, A39, and A47 disappeared. [DIR001]
- In the later window, A37's outgoing transitions shifted: the share to A33 rose from about 34% to 58%, while the share to A36 fell from about 62% to 37%; small shares to A04, A10, A15, A40, and A45 appeared. [DIR002]
- In the later window, A36 and A37 are more often adjacent: the share of traces where they are one step apart rose from 94% to 100% (support 33 vs 56). [LAG004]
- In the later window, A32 and A36 are more often adjacent (lag 1 rose from 34% to 62%, lag 2 fell from 66% to 37%), while A32 and A37 are more often separated by one step (lag 2 rose from 33% to 62%, lag 1 fell from 63% to 38%). [LAG002, LAG003]
- In the later window, A07 occurs later in the trace (mean position rose from 0.052 to 0.070) and is more often adjacent to A14 (lag 1 rose from 28% to 46%, lag 3 fell from 42% to 25%). [POS001, LAG001]

### Inference

Support level: Supported hypothesis

The evidence supports a change in the routing among A33, A36, and A37: in the later window, A36 more often leads to A37 (from about 34% to 62% of its outgoing transitions) and A37 more often leads to A33 (from about 34% to 58%), while the reverse direction A37→A36 decreased from about 62% to 37%. This makes the sequence A32→A36→A37 more common: A32 and A36 are more often adjacent (lag 1 rose from 34% to 62%), A32 and A37 are more often separated by one step (lag 2 rose from 33% to 62%), and A36 and A37 are almost always adjacent (100% vs 94%). [DIR001, DIR002, LAG002, LAG003, LAG004] The number of control-flow items (7) far exceeds the 0.48 expected by chance, so this is unlikely to be a random fluctuation. A competing explanation is that the observed shift reflects a different mix of case types, but the evidence does not support that directly.

Other differences: A07 occurs later in the trace (mean position rose from 0.052 to 0.070) and is more often adjacent to A14 (lag 1 rose from 28% to 46%, lag 3 fell from 42% to 25%). [POS001, LAG001] This appears to be a separate change not involving the A33/A36/A37 routing.