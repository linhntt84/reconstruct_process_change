### Observed differences

- In the earlier window, every one of the 200 traces ran the same four-step sequence: A02 was always followed by A04, A04 always by A05, and A06 always came last; A04, A05 and A06 each appeared exactly once per trace, at relative positions of about one-third, two-thirds and the end of the trace. [OCC003, DIR001, DIR003, POS003, POS004, POS005, REL007, REL011, REL012]

- In the later window, every one of the 200 traces runs a five-step sequence: A02 is now always followed by A03, A03 by A05, and A06 is followed by a new final step A01; A03, A05, A06 and A01 each appear exactly once per trace, at relative positions of about one-quarter, one-half, three-quarters and the end. [OCC001, OCC002, DIR001, DIR002, DIR004, POS001, POS002, POS004, POS005, REL006, REL009, REL005]

- Participation flipped completely for three activities: A01 and A03 were not observed in any earlier trace (0 of 200) but occur in every later trace (200 of 200), while A04 shows the reverse, from 200 of 200 down to 0 of 200; A05 and A06 continue in every trace, so their position shifts only reflect the changed steps around them. [OCC001, OCC002, OCC003, POS004, POS005]

- The pairwise relations flip accordingly: A02–A04, A04–A05 and A04–A06, which co-occurred with A04 first in the earlier window, now appear as separate activities (only A02, only A05, only A06), while A03 now co-occurs with A02, A05 and A06 and always runs before them, and A01 co-occurs with A02, A05 and A06 and always runs last. [REL007, REL011, REL012, REL006, REL009, REL010, REL001, REL004, REL005]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis of a structural change in the control flow: in the later window, the step A04 that previously always ran between A02 and A05 is no longer executed, A03 now runs in that position (A02 before A03 before A05), and a new closing step A01 runs after A06, so traces run A02 → A03 → A05 → A06 → A01. This is not a shift in how often existing paths are taken: A04, A03 and A01 are each fully present in one window and unobserved in the other, which points to a step being dropped, another introduced in its place, and a final step appended. [OCC001, OCC002, OCC003, DIR001, DIR002, DIR003, DIR004, REL006, REL007, REL009, REL011, REL005]

The change is shown directly by the successor evidence (A02's outgoing flow switched entirely from A04 to A03, A03 now leads to A05, A04 no longer leads to any observed activity, A06 now leads to A01) and is internally consistent across the occurrence, direction, position and relation items; every item's difference exceeds those of about 995 in 1000 random re-splits of the pooled data, and each behaviour is uniform across all 200 traces of its window, making sampling noise or a rare variant unlikely explanations. [DIR001, DIR002, DIR003, DIR004, OCC001, OCC002, OCC003, POS001, POS002, POS003, POS004, POS005, REL001, REL002, REL003, REL004, REL005, REL006, REL007, REL008, REL009, REL010, REL011, REL012]

A competing explanation the evidence cannot rule out is that the two windows capture two coexisting process variants with different shares rather than one modified process, since each window shows only a single uniform behaviour; likewise, zero participation strictly means only that an activity was not observed in that window.

Other differences: none beyond the main hypothesis; the relative-position shifts of A05 (about two-thirds to one-half) and A06 (end to about three-quarters) follow from the same change in the surrounding steps. [POS004, POS005]