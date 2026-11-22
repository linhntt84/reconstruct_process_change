### Observed differences

- A08 participation increased from about 13% to 30% of traces, and its mean position moved from about 0.49 to 0.34 (earlier). [OCC001, POS001]
- A08 now co-occurs with A26, A27, A28, A32 in about 30% of traces (up from 13%), and in those co-occurrences A08 usually precedes them (about 27% of traces have A08 before, vs 6% before). [REL001-004]
- A19, A20, A25: their outgoing transitions changed from mostly to A28/A32 to almost exclusively to A26 (e.g., A19: before A28 52%, A32 44%; after A26 100%; A20: before A32 52%, A28 47%; after A26 96%; A25: before A32 56%, A28 41%; after A26 97%). [DIR002-004]
- Their positions also moved earlier: A19 mean from 0.59 to 0.32, A20 from 0.60 to 0.33, A25 from 0.61 to 0.32. [POS002-004]
- A27's outgoing transitions changed from a mix (A28 50%, A19 16%, A20 15%, A25 15%) to almost exclusively A28 (97.5%). [DIR005]
- A28's outgoing transitions changed from a mix (A32 48%, A25 20%, A20 18%, A19 14%) to almost exclusively A32 (99%). [DIR006]
- A45's outgoing transitions changed from mostly A26 (91.5%) to a mix of A08 (25%), A19 (23%), A20 (26%), A25 (23%). [DIR007]
- Lag distributions changed for many pairs, e.g., A08-A19 from lag 3 to lag 1, A08-A26 from lags 1/4/5 to lag 2, A19-A26 from lag 4 to lag 1, A45-A26 from lag 1 to lags 2/3, A27-A32 from lag 3 to lag 2, A28-A32 from mixed 1/2 to lag 1. [LAG001, LAG002, LAG007, LAG014, LAG011, LAG013]

### Inference

Support level: Supported hypothesis

The evidence supports a change in the control flow: A19, A20, and A25 now lead to A26 instead of A28/A32, and A08 is now executed earlier and more often, preceding A26/A27/A28/A32. Additionally, A45 now leads to A08/A19/A20/A25 instead of A26. This is supported by the dramatic shift in outgoing transitions of A19/A20/A25 to A26, the earlier positions of A08/A19/A20/A25, the new co-occurrence and ordering of A08 before A26/A27/A28/A32, and the lag changes confirming the new order (e.g., A08-A19 lag 1, A19-A26 lag 1). The number of control-flow items (40) far exceeds the expected 0.72, so the overall difference is unlikely to be due to chance. A competing explanation that cannot be ruled out is that some of these changes reflect sampling variation in rare variants, but the consistency across many indicators makes this unlikely.

Other differences: A27 now goes almost exclusively to A28, and A28 now goes almost exclusively to A32, whereas before they had more varied successors. [DIR005, DIR006]