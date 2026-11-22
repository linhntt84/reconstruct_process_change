### Observed differences

- In the later window, A03 disappears: it occurs in 0% of traces (down from 100% before), and its outgoing edges are no longer observed. [OCC001, DIR001, POS002, REL001, REL003, REL005, REL006]
- In the later window, A07 appears: it occurs in 100% of traces (up from 0% before), and it has a single outgoing edge to A01. [OCC002, DIR003, POS004, REL002, REL004, REL006, REL007]
- A04's routing changes: before, A04 went to A01 in 99% of its outgoing transitions and to A03 in 1%; in the later window it goes to A07 in 100%. [DIR002]
- Ordering changes: before, A03 preceded A02, A04 and A01; after, A02 precedes A07, A04 precedes A07, and A07 precedes A01. A02's mean position moves from 0.215 to 0.0 (first), A04's from 0.746 to 0.5, and A07 sits at 0.75. [POS001, POS003, POS004, REL001–REL007, LAG001–LAG003]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the process changed from a sequence containing A03 to a sequence containing A07, with A04 now routing to A07 instead of A01, and A07 then leading to A01. Before, A03 was present in every trace and preceded A02, A04 and A01; after, A03 is absent, A07 is present in every trace, and the observed order is A02 → A04 → A07 → A01. The large number of consistent control-flow items (19 items vs. 0.13 expected by chance) and the direct relational and positional evidence make this a supported hypothesis. A competing explanation the evidence cannot fully rule out is that A03 and A07 are two labels for the same conceptual activity, but the observed predecessor/successor and position changes are consistent with a structural replacement.