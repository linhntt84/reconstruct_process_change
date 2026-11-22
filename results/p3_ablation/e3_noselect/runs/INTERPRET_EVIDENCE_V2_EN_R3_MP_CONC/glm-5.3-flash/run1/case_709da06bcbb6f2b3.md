### Observed differences

- Activity A01 was not observed in any of the 200 earlier traces; in the later window it runs in about 60 in 100 traces (119 of 200), exactly once per trace where it appears. [OCC001]
- In the earlier window, A03 and A10 (each in about 56 in 100 traces, always together) led directly to A04, A07 and to each other. In the later window, about a third of A03's outgoing transitions and about 40 in 100 of A10's go to A01, while their direct shares to A04 and A07 roughly halve (e.g. A03→A04 from about 26 in 100 to 15 in 100, A03→A07 from 29 to 12). A01's own outgoing transitions split between A03 (~32 in 100), A10 (~27), A04 (~23) and A07 (~18). [OCC003, OCC010, DIR001, DIR002, DIR007]
- Relations change accordingly: earlier, A01 never co-occurred with A03, A04, A07 or A10; later it co-occurs with A03 and with A10 in about 60 in 100 traces, in both orders (A01 first in ~26 of 100 traces, the other first in ~34), and with A04 (~32 of 100) and A07 (~28 of 100) always with A01 executed first. A04 and A07 remain mutually exclusive alternatives in both windows. [REL001, REL002, REL003, REL004, REL008]
- The new placement shows downstream: A04 and A07 sit later in the trace (median position from about 0.22 to 0.33 and from 0.50 to 0.75 of the trace), and the step distance from A03/A10 to A04/A07 lengthens — 3-step gaps now occur in about 29–41 of 100 observations where previously at most 2 steps were observed. [POS003, POS004, LAG001, LAG002, LAG005, LAG006]
- Smaller shifts: A03 and A10 are no longer always adjacent (a 2-step gap in about 29–36 of 100 cases, previously 0), A13 occurs somewhat less often, and A09's exits shift from A13 towards A14. [LAG003, LAG004, OCC013, DIR006]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that a new activity, A01, was inserted into the flow between the A03/A10 stage and the A04/A07 exits: in the later window A03 and A10 — which previously led directly to A04, A07 and each other — frequently hand over to A01, and A01 either continues to A04 or A07 or passes back to A03/A10, with A01, A03 and A10 now appearing together in about 60 in 100 traces. [OCC001, DIR001, DIR002, DIR007, REL001, REL004]

The placement is shown directly rather than inferred: new edges appear on both sides of A01, its co-occurrence with the surrounding activities flips from never to about 60 in 100 traces, and exactly the consequences an insertion predicts occur — A04 and A07 are now always preceded by A01, appear later in the trace, and lie one step further from A03/A10. These differences exceed those seen in about 199 of 200 random re-splits of the pooled data. [REL002, REL003, POS003, POS004, LAG001, LAG002, LAG005, LAG006]

Limitations: the earlier-window absence of A01 rests on non-observation in a finite sample, and several items describe the same traces, so they are not fully independent confirmations. A competing explanation the evidence cannot fully exclude is that A01 belongs to a rare variant confined to the later window, although its presence in 119 of 200 traces together with the aligned position and distance shifts makes pure sampling fluctuation unlikely. [OCC001]

Other differences: A13 participates slightly less (about 16 in 100 traces earlier, 14 in 100 later; mean occurrences 0.34 to 0.28) and A09's outgoing share moves from A13 (~54 in 100) towards A14 (~51 in 100); A02 participation dips slightly (44 in 100 to 40 in 100). These changes are small and rest on fewer observations. [OCC013, DIR006, OCC002]