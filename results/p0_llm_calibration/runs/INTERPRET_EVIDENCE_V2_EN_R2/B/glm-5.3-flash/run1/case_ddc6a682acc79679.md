### Observed differences

- In the earlier window, A20 and A21 each ran exactly once in every trace (200 of 200); in the later window each appears in only about 1 in 100 traces (2 of 200). [OCC003, OCC004]
- A14 and A15 were not observed at all in the earlier window; in the later window A14 runs in about 48 in 100 traces (96 of 200) and A15 in about 51 in 100 (102 of 200), once per trace when present. [OCC001, OCC002]
- The outgoing transitions of A37 — which ran in every trace in both windows — shifted from A21 (about 54 in 100) and A20 (about 46 in 100) in the earlier window to A15 (about 51 in 100) and A14 (about 48 in 100) in the later window, with transitions to A20/A21 nearly gone. [DIR003]
- In the later window, A14 and A15 behave as mutually exclusive alternatives: about 48 in 100 traces contain only A14, about 51 in 100 only A15, and virtually none contain both; when present, each is preceded by A37 and followed by A22. [REL001, DIR001, DIR002, REL004, REL005, REL008, REL009]
- The earlier relation pattern around A20/A21 collapsed: they used to always co-occur with each other in both orders (about 46 vs 54 in 100, no fixed order between them), always after A37 and before A22; in the later window they almost never co-occur with each other, A37 or A22. [REL010, REL011, REL012, REL013, REL014]
- The event distance from A37 to A22 shortened from 3 steps in all earlier traces to 2 steps in about 99 in 100 later traces, and A22's mean relative position moved slightly earlier (about 0.41 to 0.39). [LAG001, POS005]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that the segment between A37 and A22 was restructured: in the earlier window every trace executed A37, then both A20 and A21 in either order, then A22, whereas in the later window A37 is followed by exactly one of the mutually exclusive alternatives A14 or A15 — chosen in roughly equal shares — and then A22, with A20 and A21 almost never executed. [OCC001, OCC002, OCC003, OCC004, DIR003, REL001, REL004, REL005, REL008, REL009, LAG001]

The change is shown directly by A37's successor profile and by the relational items placing A14/A15 between A37 and A22; it is consistent across the participation, routing, relation and lag indicators, and the 27 evidence items far exceed the roughly 0.42 expected by chance, with the participation changes backed by all 200 traces in each window. [DIR003, REL004, REL005, REL008, REL009, LAG001, OCC003, OCC004]

Limitations: the items largely describe one underlying trace behaviour rather than independent confirmations; zero earlier participation shows only that A14/A15 were not observed before, so the evidence cannot establish whether they are new activities or previously rare paths, and the roughly 50/50 split between them rests on a single window. [OCC001, OCC002]

A competing explanation the evidence cannot fully rule out is that A14/A15 already existed as rare, unsampled branch choices whose selection rose while A20/A21 stopped being chosen; a path taken in about half of the later traces being missed across 200 earlier traces makes this unlikely but not impossible. [OCC001, OCC002, DIR003]