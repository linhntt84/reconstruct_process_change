### Observed differences

- Activity A06 appeared in about 30% of traces before and about 12% after, with mean occurrences per trace dropping from 0.32 to 0.125. [OCC001]
- The outgoing edges of A19, A23, A26, A27 and A28 changed from going almost exclusively to A29 (about 93–98% of their transitions) to going almost exclusively to A34 (about 90–98%). [DIR003, DIR007, DIR010, DIR011, DIR012]
- The outgoing edges of A20, A21, A22, A24 and A25 changed from including A34 (about 13–26% of transitions) to including A29 (about 17–24%), with A34 disappearing from their successors. [DIR004, DIR005, DIR006, DIR008, DIR009]
- A33's successors changed from the A20/A21/A22/A24/A25 group to the A19/A23/A26/A27/A28 group. [DIR013]
- A44's successors changed from the A06/A19/A23/A26/A27/A28 group to the A20/A21/A22/A24/A25 group. [DIR014]
- Positions shifted: A19, A23, A26, A27 and A28 moved later (mean position from about 0.33 to 0.68–0.71), while A20, A21, A22, A24 and A25 moved earlier (mean from about 0.63 to 0.39). A29 moved later (0.36 to 0.48) and A33 moved later (0.54 to 0.67). [POS002, POS006, POS009, POS010, POS011, POS003, POS004, POS005, POS007, POS008, POS012, POS013]
- Order relations reversed: A29 was before A20/A21/A22/A24/A25 before and after them after; A29 was after A19/A23/A26/A27/A28 before and before them after. A19 was before A20/A21/A22/A24/A25 before and after them after. [REL016, REL022, REL028, REL037, REL042, REL010, REL044, REL046, REL048, REL005, REL006, REL007, REL008, REL009]
- Lags changed accordingly, e.g., A19 to A29 from lag 1 to lag 5, A20 to A34 from spread to lag 5, A24 to A34 from spread to lag 1. [LAG001, LAG002, LAG004]

### Inference

Support level: Supported hypothesis

The evidence supports a reordering of two blocks of activities. In the earlier window, activities A19, A23, A26, A27 and A28 occurred early, led to A29, and were followed by A20, A21, A22, A24 and A25, which led to A34. In the later window, the order of these blocks is reversed: A20, A21, A22, A24 and A25 occur earlier and lead to A29, while A19, A23, A26, A27 and A28 occur later and lead to A34. This is directly shown by successor changes (DIR), position shifts (POS), order relations (REL) and lag changes (LAG), all pointing to the same swap. The large number of qualifying items (93 vs. about 1 expected by chance) rules out a chance explanation.

Other differences: A06 participation dropped sharply and its successors changed to a different set (A48, A16, A50, etc.); A44 changed its successor group from the early block to the later block; A33 changed its successor group in the opposite direction. These are consistent with the same reordering but involve additional activities. A competing explanation that cannot be fully ruled out is that the two blocks were not simply swapped but that some activities were added or removed from the process, since participation of A06 changed and some edges disappeared entirely. However, the core ordering reversal is strongly supported.