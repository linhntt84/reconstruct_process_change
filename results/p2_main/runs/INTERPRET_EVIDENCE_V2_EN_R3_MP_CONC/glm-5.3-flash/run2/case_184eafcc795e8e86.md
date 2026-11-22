### Observed differences

- In the earlier window, A01 and A02 do not appear at all (0 of 200 traces); in the later window, both occur in every trace (200 of 200), exactly once per trace in each case. [OCC001, OCC002]
- In the later window, A01 always leads to A04, and A12 always leads to A02; in the earlier window, no outgoing transitions were observed from A12, which was the last event of every trace (position 1.0 throughout), consistent with its being the closing activity then. [DIR001, DIR003, POS005]
- The exits from the A06/A13 pair were rerouted: earlier, A06 led to A13 in about 50 in 100 cases and to A04 in about 50, and A13 led to A04 in about 50 and to A06 in about 50; in the later window, A06 leads to A13 in about 52 and to A01 in about 48, and A13 leads to A06 in about 48 and to A01 in about 52 — A04 is no longer a direct successor of either. [DIR002, DIR004]
- Positions (event order, not clock time): in the later window A01 sits around three-quarters into the trace (median about 0.75) and A02 is the final event of every trace; A12 now ends around position 0.95 instead of 1.0, and A06 and A13 shifted earlier (medians from about 0.75–0.77 to about 0.67). [POS001, POS002, POS005, POS004, POS006]
- Relations: A01 and A02 now co-occur with A04, A06, A12 and A13 in 100 of 100 later traces, whereas earlier they co-occurred with none of them; the new orders are fixed — A06 before A01, A13 before A01, A01 before A12 and A01 before A02 each in 100 of 100 traces, and A06, A13 and A12 each precede A02 in 100 of 100. [REL001, REL003, REL004, REL005, REL007, REL008, REL009]
- A04's ordering relative to the new activities is less rigid: A01 precedes A04 in about 49 of 100 later traces with about 51 interleaved-or-repeated, and A04 precedes A02 in about 49 with about 51 interleaved-or-repeated. [REL002, REL006]
- Distances grew by roughly one step where the new activities sit: immediate A06→A04 and A13→A04 pairs (distance 1) fell from about 20–21 in 100 to 0, with distances 2–3 now most common; A06→A12 and A13→A12 pairs at distance 2 fell from about 30–33 in 100 to 0, with distances 3–4 now most common. [LAG001, LAG003, LAG002, LAG004]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that two activities were added as mandatory steps: A01 placed between the A06/A13 stage and A04 — A06 and A13, which previously led directly to A04 in about half of their outgoing transitions each, now lead to A01, which always leads to A04 — and A02 placed after A12 as the new closing step, A12 having been the last event in every earlier trace. [OCC001, OCC002, DIR001, DIR002, DIR003, DIR004, POS002, POS005, REL003, REL004, REL005, LAG001, LAG002]

Supporting signs: participation went from 0 to 200 of 200 traces with exactly one occurrence each; new successor edges (A01→A04, A12→A02) appeared while A06→A04 and A13→A04 disappeared; the new order relations hold in 100 of 100 later traces; and the roughly one-step growth in A06/A13-to-A04 and A06/A13-to-A12 distances matches a step inserted between them. With 25 qualifying control-flow items against about 0.19 expected if nothing had changed, chance sampling cannot account for the evidence as a whole. [OCC001, OCC002, DIR001, DIR003, DIR002, DIR004, REL001, LAG001, LAG002]

An important competing explanation remains: zero participation in the earlier window only shows that A01 and A02 were not observed then, so they could have been rare optional steps rather than entirely new activities; relatedly, the mixed ordering between A04 and A01/A02 in about half of the later traces is not resolved further by this evidence. [OCC001, OCC002, REL002, REL006]

Other differences: beyond position shifts that follow from the two additions (A04, A06, A13 and A12 all sitting slightly earlier in the later traces), no further independent differences appear; the split between the A06↔A13 loop and its exit stays about 50/50 in both windows. [POS003, POS004, POS006, DIR002, DIR004]