### Observed differences

- Activity A05 disappeared from the flow: in the earlier window it ran exactly once in every one of the 200 traces (100% participation, mean 1.0 occurrence per trace), while in the later window it appears in none of them (0 of 200). [OCC001, POS003]
- The connection around A05 changed accordingly: earlier, every observed transition out of A01 went to A05, and every transition out of A05 went to A02; in the later window, every transition out of A01 goes directly to A02. [DIR001, DIR002]
- A05's relations with the rest of the process collapsed: earlier it co-occurred with A01, A02, A03 and A04 in 100% of traces, always after A01 and before each of the other three; in the later window it never co-occurs with any of them, and A01, A02, A03 and A04 each appear without it in essentially all traces. [REL001, REL002, REL003, REL004]
- The remaining activities each sit one step earlier relative to A01: A02's mean normalized position fell from 0.50 to about 0.33 and A04's from 0.75 to about 0.67; the gap from A01 to A02 shrank from 2 steps to 1, from A01 to A04 from 3 steps to 2, and from A01 to A03 from 4 steps to 3. [POS001, POS002, LAG001, LAG002, LAG003]
- Every item's difference is larger than in about 995 of 1,000 random re-splits of the pooled data, but the items above describe overlapping aspects of the same traces rather than independent changes. [OCC001, DIR001, DIR002, POS001, POS002, POS003, REL001, REL002, REL003, REL004, LAG001, LAG002, LAG003]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the step A05, which previously always executed between A01 and A02, is no longer part of the observed flow: the segment A01 → A05 → A02 became A01 → A02, with A02, A03 and A04 unchanged in content but each occurring one position earlier. This is shown directly and consistently: A05 ran in every earlier trace and in none of the later ones; A01's outgoing flow switched entirely from A05 to A02; all four activity pairs involving A05 changed from always executing together in a fixed order to never meeting; and the position and step-gap shifts are all exactly one step, the pattern expected when a single step is removed rather than when existing paths are taken with different frequencies or activities are reordered. [OCC001, DIR001, DIR002, REL001, REL002, REL003, REL004, POS001, POS002, LAG001, LAG002, LAG003]

Limitations: zero participation only shows that A05 was not observed in the later window, so the evidence cannot distinguish a permanent removal from A05 being skipped throughout the sampled period or being recorded under a different label, and it says nothing about the cause. The items are also not independent confirmations, since the relation, position and lag changes largely restate the same single removal.

Other differences: none — all thirteen items describe aspects of the same disappearance of A05. [OCC001, DIR001, DIR002, POS001, POS002, POS003, REL001, REL002, REL003, REL004, LAG001, LAG002, LAG003]