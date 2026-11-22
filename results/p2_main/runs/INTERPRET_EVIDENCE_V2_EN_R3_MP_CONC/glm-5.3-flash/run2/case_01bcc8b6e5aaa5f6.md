### Observed differences

- In the earlier window, A02 occurred exactly once in every trace (participation 100%, mean 1.0 per trace) and always at or near the start of the case (median position 0). In the later window, A02 was not observed at all — 0 of 200 traces, versus 200 of 200 before. [OCC001, POS001]
- In the earlier window, A02's outgoing transitions went mostly to A03 (about 48 in 100) and A04 (about 42 in 100), with small shares to A06 (about 5), A05 (about 4) and A07 (about 1). In the later window no outgoing transitions of A02 were observed, because A02 itself no longer occurs. [DIR001]
- A02 and A03 went from always occurring together — A02 first in about 89 of 100 cases, A03 first in about 11 — to never occurring together: in the later window A03 appears without A02 in every trace. [REL001]
- The same holds for A02 and A04: always together before (A02 first in about 88 of 100), never together afterwards, with A04 appearing alone in every later trace. [REL002]
- A03 and A04 still occur in every trace, but at earlier positions in the sequence: A03's mean position fell from about 0.27 to about 0.18, and A04's from about 0.29 to about 0.15, with A04's median position dropping from about 0.33 to 0 — it is now often the first event of the case. [POS002, POS003]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that in the later window A02 was no longer executed: it ran once in every earlier case and in none of the 200 later cases, and the activities that used to follow it — A03 and A04 — now begin the case directly, with A04 frequently taking the first position. The participation drop is observed directly with full support in both windows [OCC001], and the relational items show the same change directly: both pairs moved from always co-occurring, with A02 first, to never co-occurring [REL001, REL002]. A02's outgoing edges to A03 and A04 vanished together with the activity [DIR001], and the earlier positions of A03 and A04 are consistent with the former first step being gone [POS002, POS003]. Seven control-flow items qualified where roughly 0.07 would be expected if nothing had changed — far beyond what an unchanged process typically produces [OCC001, DIR001, POS001, POS002, POS003, REL001, REL002].

Limitations: zero participation only means A02 was not observed in the later window, so complete removal cannot be distinguished from A02 becoming rare or optional and going unsampled; a competing explanation the evidence cannot rule out is that the mix of case variants shifted away from traces containing A02. The qualifying items also largely reflect one underlying behaviour, so they are not independent confirmations.

Other differences: none beyond the above; the earlier positioning of A03 and A04 [POS002, POS003] is a knock-on effect of A02's disappearance rather than a separate change.