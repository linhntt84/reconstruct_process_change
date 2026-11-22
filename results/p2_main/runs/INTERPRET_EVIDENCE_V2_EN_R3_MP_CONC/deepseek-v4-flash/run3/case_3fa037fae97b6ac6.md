### Observed differences

- In the later window, activity A01 appears in all 200 traces (mean 1.0 per trace), whereas it was absent in the earlier window (0 traces). [OCC001, POS001]
- A01 is typically early: its mean position is about 0.25 of the trace length. [POS001]
- A01 is followed by many existing activities: from A01, about 30% go to A02, 27% to A12, 13% to A04, 10% to A05, 8% to A03, 7% to A06, and smaller shares to A07, A11, A08. [DIR001]
- Existing activities now often lead to A01: A02 goes to A01 in about 32% of its outgoing transitions (previously A02 never went to A01), A06 in about 26%, A12 in about 30%. [DIR002, DIR003, DIR004]
- A01 co-occurs with A02, A04, A05, A12 in all traces (previously those activities occurred without A01). With A06, co-occurrence rose from 0% to 59% of traces. [REL001, REL002, REL003, REL004, REL005]
- The order between A01 and A02 and between A01 and A12 is mixed (about half each direction), while A01 always precedes A04 and A05. [REL001, REL002, REL003, REL005]
- Positions of existing activities shifted later: A05's mean position moved from about 0.63 to 0.73, and A12's from 0.20 to 0.24. [POS002, POS003]
- Lags between many activity pairs increased: for example, the share of A02→A04 pairs with lag 2 dropped from 40% to 30% while lag 5 rose from 4% to 13%; A02→A05 lag 1 dropped from 24% to 12% while lag 4 rose from 12% to 21%; A06→A05 lag 5 rose from 0% to 37%. [LAG001, LAG002, LAG005, LAG006, LAG010]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that a new activity A01 was introduced in the later window, appearing in every trace, typically early, and it is followed by many existing activities (A02, A12, A04, A05, A06, etc.), while existing activities' positions and lags shifted later. The direct evidence includes A01's presence, its outgoing edges, incoming edges from existing activities, and co-occurrence relations. The order between A01 and A02 and between A01 and A12 is mixed, so A01 is not strictly placed before them, but it always precedes A04 and A05. The increased lags between many pairs are consistent with the insertion of A01 early in the process, though they could also reflect other timing changes. The evidence cannot rule out that A01 was always part of the process but was not observed in the earlier window, but its appearance in all 200 later traces and the large number of qualifying items (23 vs 0.23 expected by chance) make this unlikely.

Other differences: The positions of A05 and A12 shifted later, and lags between many pairs increased, which is consistent with the insertion of A01 but could also reflect other timing changes.