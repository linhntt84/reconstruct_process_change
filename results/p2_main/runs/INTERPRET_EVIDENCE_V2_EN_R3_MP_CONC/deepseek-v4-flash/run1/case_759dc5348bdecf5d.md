### Observed differences

- Activities A03 and A11 disappear completely in the later window. A03 was present in about 29% of before traces (57/200) with a mean of 1.16 occurrences per trace; in the later window it appears in 0 traces. A11 was present in about 20% of before traces (39/200) with a mean of 0.56; it also appears in 0 traces. [OCC001, OCC002, POS001, POS002]
- The outgoing transitions of A03 and A11 vanish: A03 previously led to A11 (44%), A19 (28%), A12 (22%) and A06 (6%); A11 led to A03 (97%) and A06 (3%). In the later window neither activity has any observed outgoing transitions. [DIR001, DIR003]
- A03 no longer co-occurs with A06, A11, A12 or A19. Before, A03 co-occurred with A06, A12 and A19 in about 29% of traces and with A11 in about 20%; after, co-occurrence is 0% for all pairs. [REL001, REL002, REL003, REL004]
- A06's routing changes: before, about 86% of its outgoing transitions went to A03; after, about 58% go to A19 and 37% to A12, with no transitions to A03. [DIR002]
- The remaining activities A12 and A19 occur earlier and in fewer traces. Their trace participation drops from about 29% to 22% (43/200), and their mean position shifts from about 0.33 to 0.23 (A12) and from 0.32 to 0.22 (A19). [POS003, POS004]
- Repeated occurrences of A06, A12 and A19 become closer together. For example, the share of A06–A06 pairs with a lag of 5 steps drops from about 66% to 3%, while lag 4 rises from 4% to 52%; similar shifts appear for A12–A12 and A19–A19. [LAG001, LAG004, LAG005]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that activities A03 and A11 are no longer executed in the later window. They were present in a substantial share of before traces (about 29% and 20%) and are completely absent in 200 after traces, with no occurrences, no outgoing transitions, and no co-occurrences with any other activity. This is directly shown by occurrence, direction, position and relation indicators. The screening comparison (18 control-flow items vs 0.22 expected by chance) makes it very unlikely that this is a random sampling artefact. A competing explanation that cannot be fully ruled out is that A03 and A11 still exist in the process but occur so rarely that they were not captured in the 200 after traces; however, their previous frequency makes this implausible.

Other differences: A06's outgoing transitions shift from A03 to A19 and A12, and the remaining activities A12 and A19 occur earlier and with closer repetitions. These changes are consistent with the removal of A03 and A11, but they are reported separately because they involve different activities. [DIR002, POS003, POS004, LAG001, LAG004, LAG005]