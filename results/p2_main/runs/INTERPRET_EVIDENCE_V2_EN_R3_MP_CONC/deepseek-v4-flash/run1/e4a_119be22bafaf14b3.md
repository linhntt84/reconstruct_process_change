### Observed differences

- In the later window, from activity A26, the share of outgoing transitions to A31 dropped from about 31% to 17%, while the share to A30 rose from about 21% to 27% and to A32 from 22% to 30%. [DIR001]
- From A30, the share to A27 dropped from about 60% to 38%, while the share to A31 rose from about 40% to 62%. [DIR002]
- From A31, the share to A30 dropped from about 60% to 38%, while the share to A27 rose from about 40% to 62%. [DIR003]
- The relative positions (lags) changed accordingly: A26 and A30 became closer (lag 1 more often), A26 and A31 became farther apart, A30 and A27 became farther apart, and A31 and A27 became closer. [LAG001, LAG002, LAG003, LAG004]
- The elapsed time between completions of A01 and A03 increased from about 0.86 hours to 1.69 hours on average (median from 0.84 to 1.75 hours). [TWAIT001]

### Inference

Support level: Supported hypothesis

The evidence supports a shift in routing among activities A26, A30, A31, and A27. In the later window, the process more often follows the path A26→A30→A31→A27 and less often uses alternative paths such as A26→A31 or A30→A27. This is directly shown by the changes in outgoing transition shares from A26, A30, and A31, and by the corresponding changes in the relative positions of these activities. All involved activities are present in substantial shares of traces in both windows, so this is a change in how often existing paths are taken rather than an addition or removal of activities. [DIR001, DIR002, DIR003, LAG001, LAG002, LAG003, LAG004]

Other differences: The elapsed time between completions of A01 and A03 increased markedly, from about 0.86 to 1.69 hours on average. This is a separate timing change not involving the control flow activities above. [TWAIT001]

A competing explanation that cannot be fully ruled out is that the routing shift reflects a change in the mix of case types rather than a change in the process logic itself, but the evidence shows a consistent redistribution among existing paths.