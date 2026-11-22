### Observed differences

- In the later window, A19 and A20 each appear in nearly every trace (199 of 200), up from about 48 in 100 traces each before. [OCC001, OCC002]
- Traces containing neither A19 nor A20 fall from about 52 in 100 to under 1 in 100. [REL001]
- A25 and A26 each rise from roughly a quarter of traces to about half (25% to 51%, and 24% to 49%), with the split between them staying roughly even; in both windows they never occur in the same trace, so they remain alternatives. [OCC003, OCC004, REL010]
- The main routing difference is at A42: before, its observed outgoing transitions split about 50% to A27 and 44% to A19; in the later window about 92% go to A19 and under 1% to A27. [DIR004]
- The gap from A42 to A27 lengthens accordingly: before, about half of the observed A42→A27 pairs within five steps sit at distance 1 and 44% at distance 4; in the later window, 90% sit at distance 4. [LAG002]
- The relative order of activities stays the same wherever the pairs co-occur: A42 before A19, A19 before A20, A19 before A25 and before A26, A25 and A26 before A20, and A20, A25 and A26 before A27. [REL001, REL002, REL003, REL005, REL006, REL007, REL008, REL011, REL013]
- A27 and A42 occur in every trace in both windows; their relative positions shift only slightly (A27 mean 0.40 to 0.43, A42 mean 0.33 to 0.31). [POS001, POS002]
- Routing elsewhere is stable: A20 leads to A27 in about 99% of its outgoing transitions in both windows, and A25 and A26 lead almost exclusively to A20. [DIR001, DIR002, DIR003]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that the choice at A42 changed: the direct continuation from A42 to A27, used in about half of the executions before, is almost never used in the later window, and nearly all traces now run the full sequence A42 → A19 → A25 or A26 → A20 → A27. [DIR004, LAG002, REL004, REL005, REL009]

The support is direct and consistent: 22 evidence items stand against roughly 0.6 expected by chance across the 121 tested units; the rerouting is observed directly in A42's outgoing transitions and in the A42→A27 distances; the participation gains of A19, A20, A25 and A26 (about 25 to 52 percentage points each) match quantitatively what rerouting half of the traces through this path would produce; and the unchanged relative order indicates the difference is how often the branch is taken, not a reordering of activities. [DIR004, LAG002, OCC001, OCC002, OCC003, OCC004, REL001]

Limitations: the OCC and REL items largely restate the same rerouted traces rather than providing independent confirmation; DIR shares describe usage of outgoing transitions, not case frequencies; and the finite windows cannot rule out that the two samples drew different mixes of two pre-existing variants by chance, although a swing from 96 to 199 of 200 traces — larger than about 199 of 200 random re-splits on these indicators — makes pure sampling noise an unlikely explanation. [OCC001, DIR004, LAG002]