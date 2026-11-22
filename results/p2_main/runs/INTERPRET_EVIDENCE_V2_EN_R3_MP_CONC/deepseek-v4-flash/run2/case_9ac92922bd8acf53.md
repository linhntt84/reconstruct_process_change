### Observed differences

- In the earlier window, activities A27, A36, A37, A42, A43, and A44 each appeared in about 100% of traces; in the later window they appear in about 45–55% of traces (A27 45.5%, the others ~55%). [OCC002, OCC003, OCC004, OCC005, OCC006, OCC007]
- A25's outgoing transitions changed: before it went to A36, A37, A42, A43, and A44 (each ~17–24%); after it goes almost exclusively to A28 (98.5%). [DIR003]
- A26's outgoing transitions changed: before it went to A27 (97.5%); after it goes to A27 (44.5%) and to A37, A43, A44, A36, and A42 (together ~55%). [DIR004]
- The order between A26 and the block (A36, A37, A42, A43, A44) reversed: before these activities came before A26 (B_before_A ~0.98); after A26 comes before them (A_before_B ~0.545). Similarly, A28 now comes before these activities, whereas before they came before A28. [REL026, REL027, REL028, REL029, REL030, REL038, REL039, REL040, REL041, REL042]
- A31 now co-occurs with the block in about half the traces, whereas before it did not co-occur with them (cooccurrence ~0.55 after vs ~0 before). [REL043, REL044, REL045, REL046, REL047, LAG013, LAG015, LAG017, LAG019]
- A10 participation dropped from 32% to 13%. [OCC001]

### Inference

Support level: Supported hypothesis

The process changed from a single mandatory path where activities A25, A26, A27, A28, A31, A36, A37, A42, A43, and A44 were always executed in a fixed order, to a process where a block of activities (A27, A36, A37, A42, A43, A44) is executed in only about half the cases, and the routing around them changed: A25 now leads to A28 instead of to the block, A26 now leads to the block instead of to A27, and A28 now precedes the block while A31 follows it. The evidence is direct and consistent: the participation drop of the block, the successor changes of A25 and A26, the order reversals between A26/A28 and the block, and the new co-occurrence of A31 with the block all point to the same structural change. The screening shows 106 control-flow items against 1.18 expected by chance, so the overall difference is not a sampling artifact. A competing explanation that cannot be fully ruled out is that the later window contains a different mix of case types, but the magnitude and coherence of the changes make this unlikely.

Other differences: A10 participation dropped from 32% to 13%. [OCC001]