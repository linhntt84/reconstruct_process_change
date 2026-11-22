### Observed differences

- A10 and A11 each occurred on average 1.88 times per trace in the earlier window and 1.57 times in the later window (about 16% fewer), while still appearing in every trace; the share of traces with repeated occurrences fell from about 47% to 38%. [OCC001, OCC002]
- A14, A15, and A20 changed their outgoing behaviour: in the earlier window they went to A23 and A27 in roughly equal shares (A14: 50/50, A15: 56/44, A20: 52/48); in the later window each goes exclusively to A21. [DIR001, DIR002, DIR003]
- A22 previously split its outgoing transitions among A23 (48%), A14 (19%), A15 (18%), and A20 (16%); in the later window it goes only to A23. [DIR004]
- A23 previously split among A27 (53%), A14 (19%), A20 (15%), and A15 (14%); in the later window it goes only to A27. [DIR005]
- A40 previously went to A21 in all observed transitions; in the later window it splits among A15 (35%), A14 (34%), and A20 (32%). [DIR006]
- A14, A15, and A20 moved from about 60% of the trace length to about 32% (earlier), while A21, A22, and A23 shifted slightly later (A21 from 33% to 35%, A22 from 56% to 59%, A23 from 61% to 62%). [POS001–POS006]
- For the pairs (A14,A21), (A14,A22), (A15,A21), (A15,A22), (A20,A21), and (A20,A22), the order reversed: in the earlier window the second activity (A21 or A22) always preceded the first (A14/A15/A20) when both occurred; in the later window the first always precedes the second. [REL001–REL006]
- Lags between activities tightened: A22–A23 became adjacent (lag 1) in all traces instead of sometimes lag 2; A22–A27 moved from lag 3 to lag 2; A23–A27 became adjacent; A40–A21 moved from lag 1 to lag 2. [LAG001–LAG004]

### Inference

Support level: Supported hypothesis

The evidence supports a restructuring of the control flow in which A14, A15, and A20 now lead to A21 (instead of directly to A23/A27), and the downstream chain A22→A23→A27 became more direct, while A40 no longer connects to A21. This is directly shown by the outgoing-transition changes, the reversal of order between A14/A15/A20 and A21/A22, the earlier positions of A14/A15/A20, and the tightened lags among A22, A23, and A27. The screening comparison (24 control-flow items vs. 0.39 expected by chance) makes it very unlikely that these differences are random sampling artefacts. A separate, unrelated change is the reduced repetition of A10 and A11, which is not part of the main hypothesis.

Other differences: A10 and A11 occurrences per trace decreased, and A40’s outgoing target changed from A21 to a split among A14, A15, and A20. The evidence cannot rule out that the A10/A11 decrease is an independent adjustment rather than a consequence of the rerouting.