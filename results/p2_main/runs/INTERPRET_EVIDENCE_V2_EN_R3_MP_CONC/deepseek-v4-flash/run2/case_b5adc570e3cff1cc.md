### Observed differences

- A10 and A11: mean occurrences per trace fell from about 1.88 to 1.57, while still appearing in every trace; the share of traces with repeated occurrences fell from about 47% to 38%. [OCC001, OCC002]
- A14, A15, A20: their mean position in the trace moved from about 0.60–0.61 to about 0.32, i.e. they now occur earlier. [POS001, POS002, POS003]
- A14, A15, A20: their outgoing transitions changed from a split between A23 and A27 to always going to A21. [DIR001, DIR002, DIR003]
- A22: outgoing transitions changed from a split among A23, A15, A14, A20 to always A23. [DIR004]
- A23: outgoing transitions changed from a split among A15, A27, A20, A14 to always A27. [DIR005]
- A40: outgoing transitions changed from always A21 to a split among A15, A14, A20. [DIR006]
- For the pairs (A14,A21), (A14,A22), (A15,A21), (A15,A22), (A20,A21), (A20,A22), the order reversed: previously the second activity (A21 or A22) came before the first (A14/A15/A20) in about 30–38% of traces; now the first comes before the second in about 31–35% of traces. [REL001–REL006]
- Distances: A22–A23 and A23–A27 are now always adjacent (lag 1) instead of sometimes lag 2; A22–A27 distance decreased from lag 3 to lag 2; A40–A21 distance increased from lag 1 to lag 2. [LAG001–LAG004]

### Inference

Support level: Supported hypothesis

The evidence supports a change in the control-flow structure: a block of activities (A14, A15, A20) moved from after A21/A22 to before them, and their outgoing edges changed from A23/A27 to A21. In the earlier window, A14/A15/A20 appeared later in the trace, were preceded by A21/A22, and led to A23 or A27; in the later window they appear earlier, precede A21/A22, and lead to A21. Concurrently, A22 now always leads to A23, A23 always leads to A27, and A40 now leads to A14/A15/A20 instead of A21. This is directly shown by the routing (DIR), order (REL), position (POS) and lag (LAG) indicators, and the number of qualifying items (24) far exceeds the 0.39 expected by chance. A competing explanation that cannot be fully ruled out is that the observed windows sample different process variants, but the consistency across many indicators makes a genuine change the more plausible interpretation.

Other differences: A10 and A11 show a decrease in repetition (mean occurrences per trace from 1.88 to 1.57) without a change in participation, which is not part of the main reordering hypothesis. [OCC001, OCC002]