### Observed differences

- In the earlier window, A02 was executed in every case — 200 of 200 traces, exactly once per case on average — and always near the start of the case (mean relative position about 0.05). In the later window, A02 is not observed in any of the 200 traces. [OCC001, POS001]
- Before, A02 and A03 occurred together in every case, with A02 first in about 89 in 100 cases; afterwards they never co-occur, and A03 appears without A02 in every case. The same pattern holds for A02 and A04: always together before, A02 first in about 88 in 100 cases; afterwards A04 occurs alone in every case. [REL001, REL002]
- A02's outgoing transitions, which before led to A03 in about 48 in 100 cases and to A04 in about 42 in 100 (with small shares to A06, A05 and A07), are no longer observed, because A02 itself no longer occurs. [DIR001]
- A03 and A04 still occur in every case in both windows, but they sit earlier in the case afterwards: A03's mean relative position fell from about 0.27 to 0.18, and A04's from about 0.29 to 0.15 (median from about 0.33 to 0.0). This shift is consistent with the loss of the early A02 rather than an independent rearrangement. [POS002, POS003]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that A02, previously executed once in every case at the start of the process, is no longer executed in the later window — in behavioural terms, the step is skipped in all observed cases. Participation fell from 200 of 200 traces to 0 of 200, and the relational items show the direct consequence: A03 and A04, which previously ran after A02 in about 89 and 88 in 100 cases respectively, now run without it in every case. Chance is an unlikely explanation for the set of differences as a whole: 7 control-flow items qualified where only about 0.07 were expected for the 15 units tested, and each item's difference exceeds about 99 of 100 random re-splits. Note that the occurrence, position, relation and direction items all describe this single disappearance, so they converge on one difference rather than confirming it independently. [OCC001, POS001, REL001, REL002, DIR001, screening]

The earlier positions of A03 and A04 in the later window fit the same hypothesis as a consequence of losing the early A02, not as a separate change. [POS002, POS003]

Competing explanation: zero participation only means A02 was not observed in the later window; the evidence cannot exclude that A02 still executes in a share of cases too small to appear in a 200-trace sample, nor distinguish a permanent removal from a routing change that bypasses A02 in every observed case. [OCC001]