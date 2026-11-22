### Observed differences

- Activity A02 was executed exactly once in every case in the earlier window (200 of 200 traces, at a very early relative position, about 0.05 into the trace); in the later window it does not appear in any of the 200 traces. [OCC001, POS001]
- The relationship between A02 and A03 changed from "always together" to "never together": earlier, both ran in every trace, with A02 first in about 89 in 100 cases; in the later window, A03 runs alone in every trace. [REL001]
- The same holds for A02 and A04: earlier they always co-occurred, with A02 first in about 88 in 100 cases; in the later window A04 runs alone in every trace. [REL002]
- A02's outgoing transitions: earlier, its observed continuations went to A03 in about 48 in 100 cases and to A04 in about 42, with small shares to A06 (~5), A05 (~4) and A07 (~1); in the later window no outgoing transitions from A02 are observed, because the activity itself is absent. [DIR001]
- The successors now appear earlier in the trace: A03's mean relative position fell from about 0.27 to 0.18, and A04's from about 0.29 to 0.15, with A04's median position now 0 — at the very start of the trace in at least half the cases. [POS002, POS003]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that A02 was removed from the process, or at least is no longer executed in observed cases. In the earlier window A02 was a mandatory first step — present in every trace and followed by A03 in about half of the cases and A04 in about four in ten — while in the later window A02 is entirely absent, and A03 and A04 now run without it, near the start of each case. Seven control-flow items qualified, where about 0.07 would be expected if nothing had changed, and the participation, relational and directional indicators all describe this same disappearance rather than independent phenomena; the position shifts of A03 and A04 are consequences of the same behaviour, not separate confirmations. [OCC001, POS001, REL001, REL002, DIR001]

A limitation: zero participation only shows that A02 was not observed in the later sample, so a complete removal cannot be distinguished from A02 becoming rare enough to miss in 200 traces; the evidence also cannot show whether A02's minor successors (A05, A06, A07) are still reached by some other route. [OCC001, DIR001]

Other differences: none — the earlier positions of A03 and A04 belong to the same change rather than being separate shifts. [POS002, POS003]