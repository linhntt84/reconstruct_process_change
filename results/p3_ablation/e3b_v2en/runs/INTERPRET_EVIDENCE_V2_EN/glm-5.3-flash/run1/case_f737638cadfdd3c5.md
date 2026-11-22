### Observed differences

- In the later window, three activities that were absent from the earlier window occur regularly: A19 in about 37 of 100 traces, A25 in about 34 and A20 in about 29, each appearing at most once per trace. They behave as mutually exclusive alternatives — A19 with A20 and A20 with A25 never share a trace, A19 with A25 co-occur in only about 1 of 200 traces — and together they cover roughly 99 of 100 later traces, against none earlier. [OCC001, OCC002, OCC003, REL001, REL002, REL007]
- A41's routing changed: earlier, about 93 in 100 of its outgoing transitions went directly to A26; in the later window, about 92 in 100 go to the new activities (about 35 to A19, 31 to A25, 27 to A20) and only about 1 in 100 still go straight to A26, while A41 itself keeps occurring roughly once per trace. [DIR004]
- The new activities lead almost exclusively to A26: about 96 in 100 of A19's observed outgoing transitions go to A26, about 98 of A20's and 97 of A25's. [DIR001, DIR002, DIR003]
- The ordering fits a single added step: whenever one of the three occurs, A41 precedes it and it precedes A26 in essentially every such trace (co-occurrence in about 37 of 100 traces for A19, 29 for A20, 34 for A25, matching their participation). [REL003, REL006, REL008, REL010, REL011, REL014]
- Consistent with one extra event, the step distance from A41 to A26 grew from predominantly one step (about 94 of 100) to predominantly two steps (about 90 of 100); the new activities sit at about 0.36 of the relative trace position, and downstream activities shifted slightly later (A26 median from about 0.36 to 0.38; A31 mean from about 0.69 to 0.71) with unchanged participation. [LAG002, POS001, POS002, POS003, POS004, POS005]
- Separately, the step distance from A31 to A35 moved from mostly one step (about 55 of 100) to mostly two steps (about 62 of 100). [LAG001]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that, in the later window, a per-case choice among three mutually exclusive activities — A19, A20 and A25 — appears between A41 and A26, replacing the previously dominant direct A41→A26 transition. The signs are direct and consistent: A41's outgoing traffic moved from about 93 in 100 to A26 to about 92 in 100 to the three alternatives, each of which leads back to A26 in about 96–98 of 100 transitions; A41 precedes the chosen activity and the chosen activity precedes A26 whenever they co-occur; and the A41→A26 distance grew from one to two steps while A26 and A31 moved slightly later in the trace. [DIR004, DIR001, DIR002, DIR003, LAG002, REL003, REL006, REL008, REL010, REL011, REL014, POS004, POS005]

The near-zero co-occurrence among A19, A20 and A25, combined with their presence in about 99 of 100 later traces (against 0 of 200 earlier), fits a per-case selection of exactly one alternative rather than repetition or parallel execution. [REL001, REL002, REL007, OCC001, OCC002, OCC003]

With 28 qualifying items against roughly 0.57 expected for an unchanged process, the pattern as a whole cannot be attributed to chance screening noise. [OCC001, OCC002, OCC003, DIR001, DIR002, DIR003, DIR004, POS001, POS002, POS003, POS004, POS005, REL001, REL002, REL003, REL004, REL005, REL006, REL007, REL008, REL009, REL010, REL011, REL012, REL013, REL014, LAG001, LAG002]

Limitations: the branch shares (about 37, 29 and 34 per 100 traces) are sample estimates and may differ from the underlying probabilities; zero participation earlier strictly means only that these activities were not observed in that window, although a rise from 0 of 200 to about 99 of 100 traces is far beyond ordinary sampling variation in variant frequencies. [OCC001, OCC002, OCC003]

The evidence also does not explain the A31→A35 distance shift, which could reflect a further positional change between those two activities or a side effect that the current items do not identify. [LAG001]