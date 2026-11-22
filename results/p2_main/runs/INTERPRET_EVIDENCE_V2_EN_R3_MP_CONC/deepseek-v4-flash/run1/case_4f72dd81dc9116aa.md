### Observed differences

- In the earlier window, A05 appeared in every trace (mean 4.15 occurrences per trace); in the later window it appeared in about half the traces (49.5%, mean 2.2), and its position moved from about two-thirds of the trace to about one-third. [OCC001, POS001]
- A08 similarly decreased from 68% participation (mean 2.16) to 34% (mean 1.06), and its position moved from 0.66 to 0.34. [OCC002, POS002]
- A10 increased from 46.5% participation (mean 1.94) to 100% (mean 4.09), and its position moved from 0.32 to 0.67. [OCC003, POS003]
- A16 increased from 29.5% participation (mean 0.89) to 67.5% (mean 2.13), and its position moved from 0.33 to 0.67. [OCC004, POS004]
- The successor of A05 changed: earlier it went to A08 (52%) and A09 (48%); later to A17 (52%) and A08 (48%). [DIR001]
- The successor of A06 changed from always A05 to always A10. [DIR002]
- The successor of A10 changed from A16 (46%) and A17 (54%) to A16 (52%) and A09 (48%). [DIR003]
- The successor of A11 changed from A05 (49%) and A15 (51%) to A15 (46%) and A10 (54%). [DIR004]
- The successor of A14 changed from A10 (51%), A11 (25%), A15 (24%) to A05 (53%), A15 (25%), A11 (21%). [DIR005]
- The successor of A15 changed from A11 (49%) and A05 (51%) to A10 (46%) and A11 (54%). [DIR006]
- A05 co-occurred with A09, A11, A14, and A15 in 100% of traces earlier; later only about 49.5% with each, with A05 alone or neither increasing. [REL003, REL005, REL006, REL007]
- A10 co-occurred with A11, A14, A15, and A09 in 46.5% of traces earlier; later 100% with each. [REL022, REL023, REL024, REL020]
- A16 co-occurred with A09, A11, A14, and A15 in 29.5% of traces earlier; later 67.5% with each. [REL021, REL027, REL028, REL029]
- Lag patterns changed: A14 to A05 shifted from mostly lag 3 (47%) to lag 1 (13%) and lag 3 (5%); A14 to A08 from lag 4 (99%) to lag 2 (29%) and lag 4 (11%); A14 to A10 from lag 1 (16%) and lag 3 (5%) to lag 3 (50%) and lag 5 (17%). [LAG005, LAG006, LAG007]

### Inference

Support level: Supported hypothesis

The evidence supports a change in the control-flow structure: A05 and A08 became less frequent and moved earlier in the trace, while A10 and A16 became more frequent and moved later. The routing around A05 also changed—its successor shifted from A09 to A17, and A06 now leads to A10 instead of A05. This is consistent with a shift from a process where A05 and A08 were mandatory early steps to one where they are optional, with A10 and A16 becoming the main later steps. The large number of qualifying items (55 vs. 0.46 expected by chance) makes it unlikely that these differences are random sampling artefacts. The hypothesis is supported but not confirmed; the evidence is entirely control-flow based, and the exact nature of the new path (e.g., whether A17 replaces A09 as a full alternative) cannot be fully determined from these indicators alone.

Other differences: A14's successor changed from A10 to A05, and A11's successor changed from A05 to A10, reflecting the same routing shift. These are consistent with the main hypothesis and do not require a separate explanation.