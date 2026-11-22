### Observed differences

- A10 participation dropped from about 71% of traces to about 25%, and its mean occurrences per trace fell from 0.78 to 0.285. [OCC005, POS001, REL001, REL002, REL004, REL005, REL006, REL007, REL008, REL009, REL010, REL011, REL012, REL013]
- A30, A31, A36, A37 and A38 each increased from about 1 occurrence per trace to about 3, and the share of traces with repeated occurrences rose from near 0% to about 67%. [OCC006, OCC007, OCC008, OCC009, OCC010]
- A02, A04, A06 and A08 increased participation: A02 from 4.5% to 17.5%, A04 from 5.5% to 22.5%, A06 from 9% to 25.5%, A08 from 6.5% to 19.5%. [OCC001, OCC002, OCC003, OCC004]
- Order relations among the group A14, A15, A28, A30, A31, A36, A37, A38, A44, A45, A46, A47 changed from a fixed sequence to interleaved/repeated execution. For example, A14 before A30 occurred in 97.5% of traces before, but only 33% after, with 67% interleaved/repeated; similar shifts appear for many pairs in this group. [REL014, REL015, REL016, REL017, REL018, REL019, REL020, REL021, REL022, REL023, REL029, REL030, REL031, REL032, REL033, REL034, REL035, REL036, REL037, REL040, REL041, REL042, REL043, REL044, REL047, REL048, REL050, REL053, REL054, REL055, REL058, REL059, REL062, REL063]
- A10's co-occurrence with these activities dropped from about 70% to about 25% or lower, and its position moved earlier (mean normalized position from 0.85 to 0.48). [REL001, REL002, REL004, REL005, REL006, REL007, REL008, REL009, REL010, REL011, REL012, REL013, POS001]

### Inference

Support level: Supported hypothesis

The evidence supports a change from a single sequential execution of a block of activities to a repeated, interleaved execution of that block, with A10 largely dropping out. Specifically, activities A30, A31, A36, A37 and A38 (together with related activities such as A14, A15, A28, A44, A45, A46 and A47) now occur about three times per trace instead of once, and their order is no longer fixed but interleaved or repeated. A10, which previously appeared in about 70% of traces before these activities, now appears in only 25% and no longer co-occurs with them. The number of qualifying evidence items (114 vs 1.2 expected by chance) makes it very unlikely that these differences are random sampling artefacts. A limitation is that the exact mechanism (e.g., a loop added) is not directly observed, but the repetition and loss of fixed ordering are consistent with such a change.

Other differences: A02, A04, A06 and A08 increased their participation in the later window, and A10's position shifted earlier in the traces where it still occurs.