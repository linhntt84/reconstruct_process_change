### Observed differences

- In the earlier window, A14, A15 and A20 were mutually exclusive alternatives: A14 ran in about 35 in 100 traces, A15 in about 30 in 100 and A20 in about 35 in 100, no two of them ever appeared in the same trace, and together they covered essentially every case. In the later window, none of the three is observed at all (0 of 200 traces each). [OCC001, OCC002, OCC003, REL001, REL003, REL008]
- Routing out of A36 changed accordingly: before, A36's observed outgoing transitions split between A20 (about 35%), A15 (about 30%) and A14 (about 35%); in the later window, A36 leads to A21 in effectively all cases. [DIR004]
- The three activities previously sat between A36 and the rest of the process: A36 consistently came before them, each had A21 as its only observed successor, and they ran before A21 and A26. In the later window, A21 and A26 still occur in every trace, but never together with A14, A15 or A20. [DIR001, DIR002, DIR003, REL004, REL006, REL013, REL015]
- Two small positional shifts accompany this: A21's mean relative position moved slightly earlier (about 0.39 to 0.37 of the trace) while A36's moved slightly later (about 0.32 to 0.33); both activities occur in every trace in both windows. These are event positions, not clock times. [POS004, POS005]
- A19 occurs somewhat more often in the later window (about 49 in 100 traces before, about 56 in 100 after), and its earlier co-occurrence with A20 (about 17 in 100 traces) no longer happens. [REL002, REL007, REL012]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that, in the later window, the choice block between A36 and A21 is skipped: the mutually exclusive activities A14, A15 and A20, of which every trace previously executed exactly one after A36, are no longer executed, and A36 now leads directly to A21, while A21 and A26 continue unchanged in every trace. [DIR004, OCC001, OCC002, OCC003, REL004, REL013]

Supporting signs: the routing change is observed directly on A36, whose successor profile went from a three-way split to A21 alone with full support in both windows; the three activities' only observed successor was A21 and A36 consistently preceded them, so their disappearance removes exactly the segment between A36 and A21; the opposite small position shifts of A36 (later) and A21 (earlier) fit a shorter segment between them; and with 27 qualifying items against roughly 0.4 expected without a change, chance sampling cannot account for the pattern as a whole. [DIR004, DIR001, DIR002, DIR003, POS004, POS005]

Limitations: zero participation only means A14, A15 and A20 were not observed in the later window, so the evidence cannot distinguish a genuine removal from the block still existing but being skipped in every sampled case; several items also describe the same underlying traces and are not independent confirmations. [OCC001, OCC002, OCC003]

Other differences: A19's participation rose from about 49 to about 56 in 100 traces and it no longer co-occurs with A20; this looks like a secondary effect of the main difference rather than a separate change, and no participation item for A19 itself qualified. [REL002, REL007, REL012]