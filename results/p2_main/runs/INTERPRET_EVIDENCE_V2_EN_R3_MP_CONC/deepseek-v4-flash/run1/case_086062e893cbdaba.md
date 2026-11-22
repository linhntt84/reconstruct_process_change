### Observed differences

- In the later window, activity A01 appears in about 46% of traces (mean 0.96 occurrences per trace), whereas it was completely absent in the earlier window. [OCC001, POS001]
- In the later window, A01 is reached from A03 (about 35% of A03's outgoing transitions), A05 (about 47%), A06 (about 48%), and A11 (about 24%). In the earlier window, none of these activities had A01 as a successor. [DIR002, DIR003, DIR004, DIR005]
- In the later window, A01 leads to A05 (about 53% of its outgoing transitions) and A10 (about 47%). [DIR001]
- In the later window, A01 co-occurs with A03, A05, A06, and A10 in about 28%, 46%, 33%, and 46% of traces respectively; in the earlier window these pairs never co-occurred. [REL001, REL002, REL003, REL004]
- The distance between several activity pairs increases in the later window: for example, A03–A05 now have a lag of 3 in about 15% of cases (previously none), A03–A10 now have a lag of 4 in about 31% (previously none), A05–A06 now have a lag of 5 in about 32% (previously none), A05–A10 now have a lag of 2 in about 25% (previously none), A06–A05 now have a lag of 2 in about 27% (previously none), and A06–A10 now have a lag of 3 in about 61% (previously lag 2 in 76%). [LAG001, LAG002, LAG003, LAG004, LAG005, LAG006]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that a new activity, A01, was added to the process in the later window. A01 appears in about 46% of traces, is reached from A03, A05, A06, and A11, and leads to A05 and A10. The increased lags between existing activities are consistent with an extra step being inserted between them. The routing shifts (e.g., A03's outgoing to A05 dropping from 51% to 16%, A05's outgoing to A10 dropping from 100% to 53%) are direct consequences of A01 taking over part of the flow. A competing explanation that A01 existed but was simply not sampled in the earlier window is unlikely given its complete absence in 200 traces and its substantial presence later.