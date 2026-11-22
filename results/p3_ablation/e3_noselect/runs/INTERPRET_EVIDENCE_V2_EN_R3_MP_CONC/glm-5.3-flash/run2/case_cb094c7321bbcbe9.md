### Observed differences

- Activity A04 was executed exactly once in every case in the earlier window (in 200 of 200 traces, mean 1.0 occurrence per trace); in the later window it is not observed at all (0 of 200 traces). [OCC001, POS002]
- Before, every observed outgoing transition of A02 led to A04; in the later window no outgoing transitions from A02 are observed at all (200 before, 0 after), so the step A02 → A04 no longer occurs and A02 now ends its trace. [DIR001]
- The pair A02/A04 changed from always being executed together, with A02 before A04 in 100 in 100 cases, to never co-occurring: in the later window A02 occurs alone in every case. [REL001]
- A02 now occurs at the end of the trace: its mean relative position moved from 0.8 (with no variation) to 1.0, the last position, in the later window. [POS001]
- All five items show differences larger than about 995 of 1,000 random re-splits of the pooled data, and together they describe one coherent picture: the final step A04 disappeared and A02 became the terminal activity. [OCC001, DIR001, POS001, POS002, REL001]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that A04, previously a mandatory final step executed after A02 in every case, is no longer executed, so that cases which previously ended with the sequence A02 → A04 now end with A02 as the last activity. This rests on direct participation evidence (A04 in 200 of 200 traces before versus 0 of 200 after), on the simultaneous disappearance of the A02 → A04 transition and of the ordered co-occurrence of the two activities, and on A02 shifting to the terminal position; the items consistently describe this single structural difference rather than unrelated changes. [OCC001, DIR001, POS001, POS002, REL001]

Limitations: zero participation strictly means only that A04 was not observed in the later window; with 200 traces per window a sampling artefact is very unlikely, but the evidence cannot rule out that the later window simply does not capture anything after A02, and it cannot distinguish A04 being skipped in every case from being removed from the flow, as both look identical here. [OCC001, DIR001]