### Observed differences

- In the earlier window, three activities — A14, A15 and A20 — each ran in a minority of cases (about 32, 28 and 40 in 100 traces respectively) and were mutually exclusive alternatives: no trace contained more than one of them, and one of the three appeared in essentially every trace (their shares sum to 100 in 100). In the later window none of the three is observed at all (0 of 200 traces). [OCC001, OCC002, OCC003, REL001, REL002, REL006]

- In the earlier window the chosen alternative always sat between A22 and A24: A22 preceded it and A24 followed it in every case where it ran, and it sat directly after A22 in about 45 in 100 cases and directly after A23 in about 55 in 100. Accordingly, A22's outgoing transitions went to one of the three in about 45 in 100 observations (A20 about 21, A14 about 14, A15 about 11) and straight to A23 in about 55 in 100, while A23 went to one of the three in about 55 in 100 and straight to A24 in about 45 in 100. [DIR004, DIR005, REL003, REL004, REL005, REL010, REL011, REL012, LAG001, LAG003]

- In the later window, A22 leads directly to A23 and A23 leads directly to A24 in all of their observed outgoing transitions (100 in 100 each), and A14, A15 and A20 show no observed outgoing transitions at all. [DIR001, DIR002, DIR003, DIR004, DIR005]

- All relations involving the three activities collapsed: pairs that were always together with A22/A23/A24 before (co-occurrence about 28–40 in 100) now never co-occur, and pairs among A14/A15/A20 that were alternatives before now show "neither present" in 100 in 100 traces. [REL001, REL002, REL003, REL004, REL005, REL006, REL007, REL008, REL009, REL010, REL011, REL012]

- Event distances contracted: the gap from A22 to A24 was always 3 positions in the earlier window and is always 2 in the later window; the gaps A22→A23 and A23→A24, previously split between 1 and 2 positions (about 55/45 and 45/55 in 100), are now always 1. [LAG001, LAG002, LAG003]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that in the later window the process no longer executes the block of three alternative activities A14, A15 and A20, which in the earlier window ran exactly once per case between A22 and A24 — in about 45 in 100 cases between A22 and A23, otherwise between A23 and A24 — so that every case now proceeds directly A22 → A23 → A24. [OCC001, OCC002, OCC003, DIR004, DIR005, LAG002, REL003, REL005, REL010, REL012]

Supporting signs: the participation of all three activities fell from 28–40 in 100 traces to 0 of 200, a participation change observed directly rather than inferred from indirect relations; A22 and A23 now route exclusively to A23 and A24; every co-occurrence and ordering relation with the three vanished; and the A22→A24 distance shortened from 3 to 2 positions, exactly what dropping one inserted step predicts. The 23 qualifying control-flow items far exceed the roughly 0.36 expected by chance for this family, and 0 occurrences in 200 later traces makes a sampling explanation for the disappearance implausible. [OCC001, OCC002, OCC003, DIR004, DIR005, LAG001, LAG002, LAG003, REL003, REL005, REL010, REL012]

Limitations: the items overlap heavily and largely describe one underlying difference, so they are not independent confirmations; and because only activity codes are observed, the evidence cannot rule out that the step was renamed or absorbed into A23 or A24 rather than genuinely skipped. [OCC001, DIR004, DIR005]