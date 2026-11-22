### Observed differences

- In the later window, A01 appears in about 34% of traces (up from 21%) and always at the very start (mean position 0.0, previously 0.63). It no longer co-occurs with A04, A05, A09, A13, or A16; those co-occurrences dropped from about 21% to 0. [POS001, REL001, REL002, REL004, REL005, REL006]
- A17, absent before, appears in about 13% of traces after, late in the process (mean position 0.65), co-occurring with A04, A05, A09, and A13 (about 13% each) and having an outgoing edge to A09. [OCC004, POS002, REL008, REL009, REL010, REL011, DIR008]
- A05's mean occurrences per trace fell from 0.68 to 0.13 (participation from 21% to 6%). Its outgoing edges changed from A16/A01 to A04/A13. [OCC003, DIR003]
- A08's outgoing edges changed from A13/A04 to A16/A17. [DIR004]
- A09's outgoing edges changed from A06/A08/A18/A12 to A05/A18/A06/A12 (A08 replaced by A05). [DIR005]
- A13's outgoing edges changed from A04/A05/A07 to A08/A04/A07 (A05 replaced by A08). [DIR006]
- A16's outgoing edge changed from A05 to A08. [DIR007]
- A01's outgoing edge to A09 disappeared (before 100% of its 74 observed transitions, after none). [DIR001]
- A04's outgoing edges changed from A05/A13/A07 to A13/A07/A08. [DIR002]
- A02 and A03 participation decreased: A02 from 50% to 38%, A03 from 29% to 16%. [OCC001, OCC002]
- Many pairwise orderings reversed, e.g., A04-A05 and A05-A04 swapped from lag 1-3 to lag 4-5 and vice versa; A08-A04 swapped from lag 1-2 to lag 4-5; A08-A13 swapped from lag 1-2 to lag 4-5. [LAG001, LAG003, LAG007, LAG009]

### Inference

Support level: Supported hypothesis

The evidence supports a hypothesis that the process was restructured: A01 moved to the start and became an isolated initial step, while a new late activity A17 was introduced, and the routing among A05, A08, A09, A13, and A16 changed (e.g., A05 no longer leads to A16/A01 but to A04/A13; A08 no longer leads to A13/A04 but to A16/A17; A09 no longer leads to A08 but to A05; A16 now leads to A08 instead of A05; A17 leads to A09). This is supported by 42 control-flow items against 0.39 expected by chance, with direct evidence from successor changes (DIR), position shifts (POS), co-occurrence changes (REL), and order reversals (LAG). The main limitation is that the exact new process structure is not fully specified; we see changes in edges and positions but not the complete model, and some lag items have low support (e.g., 4-6 traces).

Other differences: A02 and A03 participation decreased, and A04's outgoing edges changed; these may be part of the same restructuring or separate adjustments. The evidence cannot rule out that some of the smaller changes (e.g., A02/A03) are due to sampling variation, but the overall pattern is strong.