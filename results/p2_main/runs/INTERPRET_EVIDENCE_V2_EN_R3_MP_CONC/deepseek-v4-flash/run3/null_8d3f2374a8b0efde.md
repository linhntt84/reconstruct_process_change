### Observed differences

- In the later window, after activity A22, the share of outgoing transitions going to A21 increased from about 18% to 58%, while the share going to A25 decreased from about 53% to 13%; the share to A23 stayed around 29%. [DIR001]
- In the later window, when A25 follows A22, it tends to appear later: the share with lag 1 dropped from about 53% to 13%, while lag 2 rose from about 24% to 45% and lag 3 from about 22% to 42%. [LAG001]
- The number of traces containing A22 fell from 49 to 31, so the later-window proportions rest on fewer observations. [DIR001, LAG001]

### Inference

Support level: Supported hypothesis

The evidence supports a change in the control-flow routing after activity A22: in the later window, A21 becomes the dominant successor instead of A25, and when A25 still occurs, it is no longer immediately after A22 but appears two or three steps later. This is directly shown by the successor distribution of A22 and by the lag distribution between A22 and A25, which are consistent with each other. The number of evidence items (2) is well above the chance expectation (0.29), and both items point to the same underlying shift. A limitation is that the later window contains only 31 traces with A22, so the proportions are based on a modest sample, and the two items are not independent confirmations. The drop in the number of traces containing A22 itself is not directly tested, so a broader change in the frequency of A22 cannot be ruled out.

Other differences: none.