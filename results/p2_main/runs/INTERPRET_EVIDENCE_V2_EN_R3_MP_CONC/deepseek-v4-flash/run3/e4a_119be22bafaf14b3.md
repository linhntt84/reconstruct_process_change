### Observed differences

- In the later window, after activity A26, the share of transitions to A31 dropped from about 31% to about 17%, while transitions to A30 rose from about 21% to 27% and to A32 from 22% to 30%. [DIR001]
- After A30, the share to A27 dropped from about 60% to 38%, while to A31 rose from about 40% to 62%. [DIR002]
- After A31, the share to A30 dropped from about 60% to 38%, while to A27 rose from about 40% to 62%. [DIR003]
- The distance between A26 and A30 decreased: in the earlier window, about 40% of cases had them one step apart and 60% two steps; in the later window, about 62% one step and 38% two steps. [LAG001]
- The distance between A26 and A31 increased: earlier about 60% one step, 40% two steps; later about 38% one step, 62% two steps. [LAG002]
- The distance between A30 and A27 increased: earlier about 60% one step, 40% two steps; later about 38% one step, 62% two steps. [LAG003]
- The distance between A31 and A27 decreased: earlier about 40% one step, 60% two steps; later about 62% one step, 38% two steps. [LAG004]
- The elapsed time between A01 and A03 increased from about 0.86 hours to about 1.69 hours (roughly doubled). [TWAIT001]

### Inference

Support level: Supported hypothesis

The evidence supports a change in the routing among activities A26, A30, A31, and A27. In the later window, A26 is less likely to go directly to A31 and more likely to go to A30 and A32; A30 is more likely to go to A31; and A31 is more likely to go to A27. This is consistent with a shift from a direct A26→A31 path to a longer path through A30 and A31. The DIR and LAG items all point in the same direction, and the number of control-flow items (7) far exceeds the 0.31 expected by chance. The change appears to be a shift in the frequencies of existing paths, since all involved activities are observed in substantial shares in both windows (e.g., A26 in all 200 traces in each window; A30, A31, A27 in about 103 and 87 traces respectively). A competing explanation that the change is due to random sampling is unlikely given the screening comparison.

Other differences: The elapsed time between A01 and A03 increased from about 0.86 hours to about 1.69 hours, a separate timing change. [TWAIT001]