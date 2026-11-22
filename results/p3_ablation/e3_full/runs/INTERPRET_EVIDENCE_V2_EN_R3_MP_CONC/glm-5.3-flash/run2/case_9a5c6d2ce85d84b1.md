### Observed differences

- Activity A01 was completely absent in the earlier window (0 of 200 traces, 0 occurrences per trace) and appears exactly once in every trace of the later window (200 of 200 traces, mean 1.0 per trace); this difference exceeds about 995 of 1,000 random re-splits of the pooled data. [OCC001]
- In the later window, A01 always sits at the final event position (mean normalized position 1.0, with no variation across traces); it was never observed in the earlier window. [POS001]
- The outgoing behaviour of A04 changed: in the earlier window no outgoing transition from A04 was observed (it was the last step of the trace), while in the later window all observed outgoing transitions of A04 lead to A01. [DIR001]
- For each pair of A01 with A02, A03, A04 and A05: in the earlier window only the partner activity occurred (A01 co-occurred in 0 of 200 traces), while in the later window both activities always occur together and the partner always comes before A01 (200 of 200 traces for all four pairs). [REL001, REL002, REL003, REL004]
- The normalized positions of A03, A04 and A05 each decreased modestly and uniformly (mean about 0.33→0.25, 1.0→0.75, and 0.67→0.5, with zero spread in both windows), a pattern consistent with one event being appended after them rather than with these activities being moved. [POS002, POS003, POS004]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that in the later window every case ends with activity A01 as a new final step, executed exactly once after A04, which was the last observed step in the earlier window. This is shown directly: A01 rises from 0 to 200 of 200 traces with exactly one occurrence each [OCC001], it occupies the final event position in every later trace [POS001], and all observed outgoing transitions of A04 now lead to A01 [DIR001]. All four relation checks agree that A02, A03, A04 and A05 each co-occur with A01 and precede it in 200 of 200 later traces, after never co-occurring with it before [REL001, REL002, REL003, REL004]. The small, uniform position decreases for A03, A04 and A05 fit an event appended at the end rather than a reordering of the existing steps [POS002, POS003, POS004].

Limitations: the relation, position and direction items largely restate the same trace-level behaviour as the occurrence item, so they are consistent with it but not independent confirmations [OCC001, REL001, POS001, DIR001]. The earlier-window absence strictly means only that A01 was not observed in that sample, and the evidence cannot distinguish a genuinely new activity from a renamed existing one, since the activity codes are anonymous [OCC001].