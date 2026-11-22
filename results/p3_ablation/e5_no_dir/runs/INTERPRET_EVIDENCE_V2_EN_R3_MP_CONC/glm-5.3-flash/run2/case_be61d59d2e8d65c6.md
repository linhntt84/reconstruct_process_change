### Observed differences

- In the earlier window, A19, A20 and A25 each ran in a substantial share of traces — about 33, 29 and 40 in 100 respectively, once per trace when present — while in the later window each appears in only about 1 in 200 traces. [OCC001, OCC002, OCC003]
- Before, the three were mutually exclusive alternatives: any pair co-occurred in only about 0.5 in 100 traces, and their exclusive shares (about 32, 28 and 40 in 100) add up to roughly one of them per trace; in the later window, 99 in 100 traces contain none of the three. [REL001, REL002, REL006]
- Before, the alternative always sat between A27 and A29: it followed A27 in essentially every trace where both occurred (about 33 in 100 traces for A19, about 40 for A25) and preceded A29 in essentially every such trace (about 32 and 40 in 100); its order relative to A28 was mixed (for A25, before A28 in about 21 in 100 traces, after it in about 19, and immediately after A28 in the 38 traces where that order was seen). In the later window, A27, A28 and A29 — each still present in every trace — occur without any of the three in about 99.5 in 100 traces. [REL003, REL005, REL010, REL011, REL012, LAG003]
- The span from A27 to A29 shortened by one step: the A27→A29 distance was 3 steps in about 90 in 100 traces before and is 2 steps in about 96 in 100 after; A27→A28 and A28→A29, previously split between 1 and 2 steps (about 52/45 and 43/52 in 100), are now almost always adjacent (about 98 and 96 in 100). [LAG001, LAG002, LAG004]
- Consistently, A27's relative position moved slightly later (mean about 0.46 to 0.48) and A29's slightly earlier (about 0.57 to 0.55), both remaining in every trace in both windows — the footprint of one event disappearing between them. [POS004, POS005]
- The later-window position figures for A19, A20 and A25 each rest on a single trace and carry no weight. [POS001, POS002, POS003]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the alternative step between A27 and A29 — filled before by exactly one of A19, A20 or A25 in nearly every trace — is no longer executed in the later window, so traces run from A27 directly via A28 to A29, with A29 two positions after A27 instead of three. In the earlier window A19, A20 and A25 were mutually exclusive alternatives (about 33, 29 and 40 in 100 traces each, one per trace); in the later window each is observed in about 1 in 200 traces, and A27, A28 and A29 appear without them in about 99.5 in 100 traces. [OCC001, OCC002, OCC003, REL001, REL003, REL005, REL010, REL012, LAG002]

The screening context supports this reading: 24 control-flow items qualified against roughly 0.33 expected if nothing had changed, and the participation collapse is far beyond sampling variation (65, 57 and 81 traces before versus 1 each after, out of 200). The occurrence, relation and distance items all describe the same underlying difference, so they are consistent rather than independent confirmations. [OCC001, OCC002, OCC003, LAG001, LAG002, LAG004]

Because the three activities are nearly absent later, this is a disappearance of that part of the process, not a redistribution of shares among surviving paths. The evidence cannot distinguish removal from the step remaining possible but skipped in virtually every case — the single later occurrences show it can still happen — nor can it show whether the change lies in the block itself or in whatever directed cases into it. [OCC001, OCC002, OCC003, REL001]

Other differences: none that stand apart from this disappearance; the small position shifts of A27 and A29 and the adjacency changes are its direct consequences. [POS004, POS005, LAG001, LAG004]