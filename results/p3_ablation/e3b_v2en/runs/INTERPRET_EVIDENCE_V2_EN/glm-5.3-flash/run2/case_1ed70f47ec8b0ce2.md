### Observed differences

- The dominant change is a reversal of execution order between two groups of activities. In the earlier window, A14, A16 and A19 came before A15, A17, A18, A20 and A24 in every trace where they co-occurred: A20 came before A15 in 200 of 200 traces, A24 came before A15 in 200 of 200, and A16 came before A17 in about 35 in 100. In the later window all of these relations are inverted: A15 came before A20 and before A24 in 200 of 200 traces, and A15 came before A16 in about 29 in 100. [REL001-REL021]

- Event positions moved consistently with this reversal. A14, A16 and A19 shifted from about one third of the trace length to about two thirds (mean relative position roughly 0.34 to roughly 0.67), A15, A17 and A18 shifted the opposite way (roughly 0.64 to roughly 0.38), and A20 and A24 moved slightly later (about 0.38 to 0.44, and 0.57 to 0.64). [POS001-POS008]

- Routing at the edges of the two groups flipped. In the later window, A14, A16 and A19 each flow exclusively to A25, where before they flowed exclusively to A20; A15, A17 and A18 now send roughly three in ten of their outgoing transitions to A20 (before: roughly three in ten to A25, with the rest going to each other); A24 now routes only to A14, A16 and A19 (before: only to A15, A17 and A18); and A35 now routes only to A15, A17 and A18 (before: only to A14, A16 and A19). [DIR001-DIR008]

- Typical distances changed in the same direction: A24 and A25 are now 2 steps apart in all 200 traces (before: 4 steps in all 200), and A35 and A20 are now 4 steps apart in all 200 traces (before: 2 steps). [LAG001, LAG002]

- Participation itself hardly moved: A15, A17, A18, A20 and A24 appear in every trace in both windows, while A14, A16 and A19 each appear in roughly 30-38 in 100 traces in both windows, consistent with one of the three being selected per case. [POS001-POS008]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that two activity blocks exchanged their positions. In the earlier window the behaviour reads as A35, then one activity chosen from {A14, A16, A19}, then A20, later A24, then the triple {A15, A17, A18} in varying order, then A25; in the later window the blocks are swapped, so that A35 is followed by the full triple {A15, A17, A18} before A20, and A24 is followed by one of {A14, A16, A19} before A25. [DIR001-DIR008, LAG001, LAG002, REL008, REL009, POS001-POS008]

The support is direct and consistent: every order relation between the two groups and against A20/A24 flipped, including complete reversals present in all 200 traces of both windows (for example A20 before A15 in the earlier window, A15 before A20 in the later), which random re-splits of an unchanged process do not produce; the position shifts, the mirrored successor profiles at A35 and A24, and the distance changes (A24 to A25 shortening from 4 to 2 steps, A35 to A20 lengthening from 2 to 4) all follow from the same rearrangement. The number of qualifying items (39, against roughly 0.5 expected when nothing has changed) also cannot be explained by chance as a whole. [DIR001-DIR008, POS001-POS008, REL001-REL021, LAG001, LAG002]

Limitations: the items overlap strongly — the 21 relation items, the position items and the routing items largely describe this one rearrangement, so they should be read as a single coherent change rather than independent confirmations. The evidence cannot show what happens between A20 and A24, nor the exact order inside the {A15, A17, A18} triple or the selection probabilities within {A14, A16, A19}, which rest on roughly 58-77 traces per activity; sampling differences between the finite windows cannot be ruled out for those finer proportions, although they cannot plausibly explain the complete order reversals. [REL001-REL021, DIR001, DIR003, DIR006, POS001, POS003, POS006]