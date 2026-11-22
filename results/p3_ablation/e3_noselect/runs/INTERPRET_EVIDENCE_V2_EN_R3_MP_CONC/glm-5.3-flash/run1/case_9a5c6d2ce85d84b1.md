### Observed differences

- In the later window, activity A01 occurs exactly once in every trace (200 of 200 traces, mean 1.0 occurrence per trace); in the earlier window it was not observed at all (0 of 200 traces). [OCC001]
- Activity A04 is present in every trace in both windows, but its position shifted: in the earlier window it sat at the end of the trace (mean event position 1.0), while in the later window it sits about three-quarters of the way through (0.75) and A01 now occupies the end position (1.0). [POS001, POS002]
- The relationship between the two activities flipped completely: earlier, A04 occurred without A01 in 100 in 100 traces (never together); later, they co-occur in 100 in 100 traces, with A04 executing before A01 every time. [REL001]
- A04's outgoing transitions also changed: none were observed in the earlier window, whereas in the later window every observed outgoing transition of A04 (200 of 200) leads to A01. [DIR001]
- All five items show differences larger than in about 199 of 200 random re-splits of the pooled data (empirical strength ≈ 0.995 each). [OCC001, DIR001, POS001, POS002, REL001]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that, in the later window, a step A01 was appended at the end of the process: A01 now executes once in every case, directly after A04, which previously appeared as the final observed step with no observed successors. The support is direct and consistent — the participation flip for A01 (0 to 200 of 200 traces), the relational flip from never co-occurring to always A04 before A01, the successor change at A04, and the matching position shifts all describe one and the same underlying difference, and each item exceeds about 199 of 200 random re-splits. [OCC001, REL001, DIR001, POS001, POS002]

The evidence covers only A01 and A04, so it cannot show whether other end-of-process behaviour elsewhere was affected or replaced. Strictly speaking, A01's absence in the earlier window means only that it was not observed there; a complete 0-of-200 versus 200-of-200 flip makes a pure sampling explanation implausible, but the evidence cannot fully exclude that A01 belonged to an extremely rare path before. [OCC001, REL001]