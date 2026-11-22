### Observed differences

- Activity A01 was not observed in any of the 200 earlier traces; in the later window it appears in all 200 traces, exactly once per case (mean 1.0 occurrence per trace, no repeats). [OCC001]
- In the later window A01 sits early in the case: median position about one-fifth of the way through the trace, with the middle half between roughly 0.11 and 0.40 (event positions, not clock time). [POS001]
- In the earlier window A01 had no observed outgoing transitions; in the later window its flow goes mainly to A02 (about 30 in 100 outgoing transitions) and A12 (about 27 in 100), with smaller shares to A04, A05, A03 and A06. [DIR001]
- New flows into A01 appeared in the later window: about 32 in 100 of A02's outgoing transitions now go to A01 (none before), about 30 in 100 of A12's (none before) and about 26 in 100 of A06's (none before); the direct shares A02→A12 (about 40 down to 24 in 100) and A12→A02 (about 39 down to 28 in 100) shrank accordingly. [DIR002, DIR004, DIR003]
- Before, A02, A04, A05 and A12 each always appeared without A01; in the later window each co-occurs with A01 in every trace. A01 always comes before A04 and before A05; with A02 the order is mixed (about half each way), and with A12 A01 comes first in 46 of 100 traces and after it in 54 of 100. [REL001, REL002, REL003, REL005]
- A06 appeared in about 48 of 100 earlier traces, never together with A01; in the later window A01 and A06 occur together in 59 of 100 traces, with A01 alone in the remaining 41 of 100. [REL004]
- Step distances between pre-existing activities grew by roughly one step: A02→A12 at distance 1 fell from about 82 to 53 in 100, A12→A02 from about 77 to 51 in 100, and A06→A02 from about 61 to 36 in 100, while distances 2–3 gained. [LAG003, LAG008, LAG004]
- Further downstream pairs shifted to larger distances too: A06→A05 moved mostly to distance 5 (from 0 to 37 in 100), A06→A04 shifted from distance 3 to distances 4–5, and A02→A05, A12→A05, A02→A04, A12→A04 and A06→A12 all show smaller upward shifts. [LAG006, LAG005, LAG002, LAG010, LAG001, LAG009, LAG007]
- Existing activities now sit slightly later in the trace: A05's mean position rose from about 0.63 to 0.73 and A12's from about 0.20 to 0.24. [POS002, POS003]

### Inference

Support level: Supported hypothesis

Screening flagged 23 control-flow items where about 0.23 would be expected by chance (47 units tested) — roughly 100 times the chance expectation — so this pattern is not what an unchanged process typically produces. The evidence supports the hypothesis that A01 was added to the process as a new mandatory step, executed exactly once per case and inserted into the early portion of existing flows: it takes over part of the outgoing flow of A02, A12 and A06, hands flow on mainly to A02 and A12 and onward to A04 and A05, always runs before A04 and A05, and its insertion lengthens the step distance between the surrounding activities by about one. [OCC001, POS001, DIR001, DIR002, DIR003, DIR004, REL001, REL002, REL003, REL005, LAG003, LAG004]

The support is direct (A01 goes from 0 of 200 traces to 200 of 200, once per trace, at an early median position) and consistent across relation, direction and distance indicators, and occurrence in every one of 200 later traces rules out a rare-variant explanation. Limitations: the evidence cannot rule out that A01 is a re-labelled existing activity rather than a genuinely new one, and because A01's order relative to A02 and A12 is mixed (about half each way), the data do not pin the insertion to a single fixed point; the many distance shifts are largely downstream consequences of the same insertion rather than independent confirmations. [OCC001, POS001, REL001, REL005]

Other differences: A06 also occurs more often overall — in about 59 of 100 later traces versus about 48 of 100 earlier traces — a participation increase that the insertion of A01 does not by itself explain. [REL004]