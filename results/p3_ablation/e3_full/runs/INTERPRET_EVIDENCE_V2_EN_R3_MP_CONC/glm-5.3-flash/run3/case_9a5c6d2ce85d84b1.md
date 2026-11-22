### Observed differences

- Activity A01 is absent from the earlier window — it appears in 0 of 200 traces — while in the later window it occurs exactly once in every trace (200 of 200 traces, mean 1.0 occurrence per trace), always at the final position (mean position 1.0). [OCC001, POS001]
- In the earlier window, traces ended with A04: it sat at the last position (mean 1.0) and no outgoing transition from it was observed. In the later window, A04 sits earlier (mean position 0.75) and all 200 of its observed outgoing transitions lead to A01. [POS003, DIR001]
- In the earlier window, each of A02, A03, A04 and A05 appeared without A01 (in 100 in 100 traces only the other activity was present). In the later window, A01 co-occurs with each of these four activities in 200 of 200 traces and runs after each of them in 100 in 100 cases. [REL001, REL002, REL003, REL004]
- A03, A05 and A04 each occupy earlier positions in the later window (A03 about 0.33 → 0.25, A05 about 0.67 → 0.50, A04 1.0 → 0.75) while their relative order A03 → A05 → A04 is unchanged — the pattern expected when one activity is appended at the end rather than any reordering among them. [POS002, POS003, POS004]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that, in the later window, A01 was added as a new final step executed once at the end of every case: in the earlier window traces ran through A02, A03, A05 and A04 and ended with A04, with A01 never observed, whereas in the later window every trace ends with A01, which directly follows A04 (all observed outgoing transitions of A04) and follows each of A02, A03, A04 and A05 in 100 in 100 co-occurring cases. [OCC001, POS001, DIR001, REL001, REL002, REL003, REL004, POS003]

The supporting signs are direct and consistent: the change is shown relationally and directionally (A01 after every other activity; the new A04 → A01 transition), not only through frequencies, and the occurrence, position, direction and relation indicators all describe one and the same difference. Every item's difference is larger than in about 199 of 200 random re-splits, so sampling fluctuation of a rare variant is an unlikely explanation. [OCC001, DIR001, POS001, REL001, REL002, REL003, REL004]

Limitations: zero participation in the earlier window only establishes that A01 was not observed there, so a newly inserted activity cannot be distinguished from one that already existed but was executed in none of the earlier cases and then became mandatory in every case. The earlier positions of A03, A05 and A04 reflect event-position normalisation after the appended step, not a move of those activities in clock time. [OCC001, POS002, POS003, POS004]