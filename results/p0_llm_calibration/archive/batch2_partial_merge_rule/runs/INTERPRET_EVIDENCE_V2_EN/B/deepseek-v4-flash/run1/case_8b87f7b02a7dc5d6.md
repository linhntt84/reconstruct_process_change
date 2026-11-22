### Observed differences

- In the later window, A08 is much more frequent: it appears in about 69% of traces (up from about 24%), and its mean position shifts from about 0.62 to 0.93 of the trace length. [OCC002, POS001]
- A04 becomes less frequent, appearing in about 7% of traces (down from 17%). [OCC001]
- The order of a block of activities reverses: A20, A21, A23, and A24 now occur before A19, A22, A25, A26, A27, A31, and A32, whereas before they occurred after them. For example, A20 preceded A27 in 0% of co-occurring traces before and in about 98% after; A21 preceded A27 in 0% before and about 99% after; A31 preceded A21 in 99% before and 0% after. [REL024, REL029, REL030, REL037, REL041, REL042, REL015-REL020, REL021-REL023, REL026-REL028, REL031-REL034, REL035-REL036, REL039-REL040, REL043-REL046]
- Successor distributions change accordingly: A19, A22, A25, and A26 now go to A32 instead of A27 (e.g., A19 went to A27 in 100% of outgoing transitions before, and to A32 in about 96% after), while A20, A21, A23, and A24 now go to A27 instead of A32. [DIR005, DIR008, DIR011, DIR012, DIR006, DIR007, DIR009, DIR010]
- A08 now more often precedes A48: in co-occurring traces, A08 before A48 rose from about 20% to 65%, and A08's outgoing transition to A48 rose from 38% to 94%. [REL014, LAG001, DIR002]

### Inference

Support level: Supported hypothesis

The evidence supports a structural change in which A08 is executed more often and later in the process, and a block of activities (A20, A21, A23, A24) is now executed before another block (A19, A22, A25, A26, A27, A31, A32) that previously preceded them, with A32 replacing A27 as the successor of the latter block and A27 replacing A32 as the successor of the former block. The order reversal is directly shown by relational and lag items (e.g., A20-A27, A21-A27, A31-A21, A31-A22, A22-A27, A22-A32) and corroborated by position shifts and successor changes. [REL024, REL029, REL030, REL037, REL041, REL042, REL021, REL026, REL031, REL033, REL034, LAG002, LAG003, LAG005, LAG008, POS003, POS004, POS006, POS007, POS002, POS005, POS008, POS009, POS010, POS011, DIR005, DIR008, DIR011, DIR012, DIR006, DIR007, DIR009, DIR010, OCC002, POS001]

A competing explanation is that the differences arise from sampling variation in variant frequencies, but the large, systematic, and mutually consistent changes across many activity pairs and indicators make this unlikely. Some lag estimates have very low support in one window (e.g., LAG002, LAG004, LAG006, LAG007, LAG009 have support 1 after), so those specific lag values are weak, but the relational items with full support confirm the order changes. [LAG002, LAG004, LAG006, LAG007, LAG009, REL024, REL029, REL030, REL037, REL041, REL042]