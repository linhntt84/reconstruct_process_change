### Observed differences

- In the later window, activity A02 appears in about 57% of traces (113/200) and always at the end of the trace (mean position 1.0); it was absent before. [OCC002, POS002]
- Activity A01 appears in 15% of traces (30/200) in the later window, positioned around 0.71 of the trace, and leads to A16; it was absent before. [OCC001, POS001, DIR001]
- A09 and A13 become less frequent: A09 participation drops from 36.5% to 19.5% and mean occurrences from 1.07 to 0.38; A13 participation drops from 23% to 8.5%. [OCC003, OCC004]
- Routing changes: A07 now leads to A14 (about 51%) instead of A09 (about 49% before); A09 now leads to A02 (about 51%) instead of A14 (about 52% before); A10 and A17 now lead to A01 instead of A16; A16 and A19 now lead to A02 (they had no outgoing transitions before). [DIR003, DIR004, DIR005, DIR007, DIR006, DIR008]
- A02 co-occurs with many activities (A03, A07, A09, A10, A13, A14, A16, A19) in the later window, often with A02 after them or interleaved, whereas before A02 was absent. [REL003-REL010]
- A09 and A14 used to co-occur in 36.5% of traces with A09 before A14 or interleaved; in the later window they co-occur in only 12.5%, and A14 appears alone more often. [REL011]
- A09 and A19 no longer co-occur (from 22% to 0%). [REL012]
- A13 and A14 co-occurrence drops from 23% to 4%. [REL013]
- Positions: A09 and A13 move later in the trace (mean position from 0.26 to 0.59 for A09, from 0.28 to 0.54 for A13); A14 moves earlier (from 0.39 to 0.20). [POS003, POS005, POS006]
- Lags: A03-A13 and A03-A14 become closer (lag 2 instead of 3/5); A07-A14 becomes closer (lag 1 appears); A10-A16 shifts to lag 2/4; A14-A14 becomes closer. [LAG001, LAG002, LAG005, LAG007, LAG009]

### Inference

Support level: Supported hypothesis

The evidence supports a change in which a new final activity A02 (and a new activity A01) was introduced, and several existing activities were rerouted to lead to them, while the use of A09 and A13 declined. Specifically, A07 now leads to A14 instead of A09, A09 now leads to A02 instead of A14, A10 and A17 now lead to A01 instead of A16, and A16 and A19 now lead to A02. This is supported by the appearance of A01 and A02, the DIR changes, the REL co-occurrence patterns, and the positional shifts. The evidence is strong (42 items vs 0.44 expected by chance). Limitations: the exact business meaning of the new activities is unknown; the change could be a replacement of a subprocess or a new branch. Also, some items are based on small support (e.g., A01 in 30 traces, A16 in 30, A19 in 44), but the overall pattern is consistent.

Other differences: A09 and A13 become less frequent and move later; A14 moves earlier; A09 and A14 no longer co-occur as often; A09 and A19 stop co-occurring. These are consistent with the rerouting.