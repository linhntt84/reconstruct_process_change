### Observed differences

- A01 did not occur at all in the earlier window (0 of 200 traces) but appears in every trace of the later window (200 of 200), exactly once per trace, always at about 0.6 of the trace position. [OCC001, POS001]
- In the earlier window, A05's only observed outgoing transition was to A06, and the two activities were one step apart; in the later window, A05's only observed successor is A01, and the A05–A06 distance is two steps. [DIR002, LAG001]
- In the later window, A01's only observed outgoing transition is to A06, seen in all 200 traces; in the earlier window A01 had no observed transitions because it never occurred. [DIR001, OCC001]
- The relations of A01 with A05 and A06 changed from "never together" (A05 alone and A06 alone in 100% of earlier traces) to "always together in a fixed order": A05 precedes A01 in 100% of later traces, and A01 precedes A06 in 100%. [REL001, REL002]
- A05's mean position moved slightly earlier (0.5 to 0.4) and A06's slightly later (0.75 to 0.8), consistent with an activity appearing between them rather than with either activity being repositioned on its own. [POS002, POS003]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that A01 was inserted into the flow between A05 and A06 and is now executed in every case. In the earlier window the flow ran directly from A05 to A06 with A01 absent; in the later window every trace runs A05 → A01 → A06, with A01 occurring exactly once between them. [OCC001, DIR001, DIR002, REL001, REL002, LAG001]

The hypothesis is shown directly by relational evidence, not only by frequency counts: A05's observed successor changed from A06 to A01, A01's observed successor is A06, both pairs moved from never co-occurring to always co-occurring in a fixed order, and the A05–A06 gap grew from one to two steps. All items describe one coherent picture, each is backed by all 200 traces in both windows, and every difference is larger than essentially all reference comparisons (empirical strength about 0.995), so a rare variant or sampling fluctuation is effectively ruled out. [DIR001, DIR002, REL001, REL002, LAG001, OCC001, POS001]

Limitations: zero participation in the earlier window only means A01 was not observed there, so the evidence cannot distinguish a newly added activity from one that already existed but was skipped in all earlier cases; the evidence also covers only the A05–A01–A06 segment and says nothing about the rest of the process. [OCC001]