### Observed differences

- In the earlier window, A04 was executed exactly once in every trace (200 of 200, mean occurrences per trace 1.0) and always as the final event of the trace (mean relative position 1.0). In the later window, A04 was not observed in any trace (0 of 200). [OCC001, POS002]
- In the earlier window, A02 occurred in every trace at a fixed relative position of 0.8, and all of its observed outgoing transitions led to A04, so traces consistently ended with the pair A02 → A04. In the later window, A02 still occurs in every trace but sits at the end of the trace (relative position moved from 0.8 to 1.0), and no outgoing transition from A02 was observed at all. [DIR001, POS001]
- The relationship between the two activities changed accordingly: earlier, A02 and A04 always co-occurred with A02 first (co-occurrence and A02-before-A04 each in 200 of 200 traces); later, A02 occurs alone while A04 is absent (A02-only in 200 of 200, co-occurrence 0 of 200). [REL001]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the closing activity A04 was dropped from the observed executions, leaving A02 as the new final step: before, every trace ended with the fixed sequence A02 → A04; in the later window A04 is unobserved, A02 occurs in every trace at the trace's end, and the A02 → A04 relation is gone. This is a disappearance of an activity from the observed behaviour, not a shift in how often existing alternatives are taken. [OCC001, DIR001, POS001, POS002, REL001]

Supporting signs: the change is shown directly by the relational and directional items (A02 no longer followed by A04; A02 now alone in traces) and all five items describe one coherent picture, each with an empirical strength of about 0.995, meaning the differences are larger than in roughly 995 of 1000 random re-splits of the pooled traces. Limitations: all items reflect the same underlying difference, so they are not independent confirmations, and zero participation establishes only that A04 was not observed in the later 200-trace sample — a residual, very rare execution of A04 cannot be ruled out. The main competing explanation, that A04 still occurs but was missed by chance, is difficult to reconcile with its presence in all 200 earlier traces, but a finite sample cannot exclude it entirely. [OCC001, REL001, DIR001]