### Observed differences

- In the earlier window, A01, A03, A05 and A06 were absent from all 200 traces; in the later window, each of them occurs exactly once in every trace (200 of 200, mean 1.0 occurrence per trace, never repeated within a trace). [OCC001, OCC002, OCC003, OCC004]
- In the earlier window, A04's only observed successor was A07 (100% of its outgoing transitions), with A04 at normalized event position 0.5 and A07 the final event (position 1.0); in the later window, A04 always leads to A03 instead, and the transitions A03→A05, A05→A06, A06→A07 and A07→A01 are each observed in 100% of outgoing transitions. [DIR002, DIR001, DIR003, DIR004, DIR005, POS003, POS006]
- The distance from A04 to A07 grew from immediate succession (1 step in all 200 earlier traces) to 4 steps (in all 200 later traces), so three events now lie between them. [LAG001]
- In the later window the six activities occupy one fixed sequence of event positions: A04 at 0.167, A03 at 0.333, A05 at 0.5, A06 at 0.667, A07 at 0.833 and A01 at 1.0. [POS003, POS002, POS004, POS005, POS006, POS001]
- All fourteen tested activity pairs involving a new activity moved from disjoint or one-sided occurrence (for example A04 without A05, A01 with neither partner) to co-occurrence in 200 of 200 later traces, always in the same direction, spelling out the single order A04 → A03 → A05 → A06 → A07 → A01. [REL001, REL002, REL003, REL004, REL005, REL006, REL007, REL008, REL009, REL010, REL011, REL012, REL013, REL014]

### Inference

Support level: Supported hypothesis

Thirty evidence items qualified, all in the control-flow family, where only about 0.15 items would be expected by chance if nothing had changed; a count roughly 200 times that expectation cannot be explained as chance sampling differences, even though the items describe one underlying difference. [screening]

The evidence supports the hypothesis that steps were added to the flow between A04 and A07 and a closing step appended: in the earlier window A04 was always followed directly by A07, which ended the trace, while in the later window A04 leads to A03, then A05, then A06, then A07, and A01 runs last. [DIR002, DIR001, DIR003, DIR004, DIR005, POS006] The four added activities (A01, A03, A05, A06) went from not being observed at all to running exactly once in every trace, in a fixed order. [OCC001, OCC002, OCC003, OCC004] The change is shown directly by the successor change at A04 and the new transitions, and corroborated by the A04→A07 distance growing from 1 to 4 steps, by the position shifts, and by the pairwise orders; each item's difference exceeds about 995 of 1000 random re-splits. [LAG001, POS001, POS002, POS003, POS004, POS005, POS006, REL001, REL007, REL012, REL014]

The evidence cannot rule out that both windows sample two pre-existing variants — a short route ending at A07 and an extended route — whose shares flipped completely between the windows; with only these two windows, a modified flow and such a complete variant-mix flip look alike. Absence in the earlier window also only means A01, A03, A05 and A06 were not observed there, and nothing is shown about activities outside the tested units, for example what precedes A04. [OCC001, OCC002, OCC003, OCC004, DIR002]

Other differences: none — the position shifts of A04 and A07 and the longer A04→A07 distance are consequences of the added steps rather than independent changes. [POS003, POS006, LAG001]