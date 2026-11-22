### Observed differences

- In the earlier window, A01 opened about half of all traces (101 of 200) and always flowed on to A02; in the later window, A01 does not appear in a single one of the 200 traces, and its only observed outgoing flow (A01 → A02) is gone. [OCC001, DIR001, POS001, REL001]
- A02 used to close every trace (relative position 1.0 in all 200 earlier traces); in the later window it is the first event in about 54 in 100 traces and appears without any of A01, A03, A04, A05 or A06, consistent with the short path now starting directly at A02. [POS002, REL001, REL006, REL008, REL009]
- A05 shows the mirror image: absent from the earlier window, it occurs in 92 of 200 later traces (about 46 in 100), always between A04 and A02 — all of A04's observed outgoing flow moved from A02 (earlier) to A05 (later), and all of A05's observed outgoing flow goes to A02. [OCC004, DIR002, DIR003, REL008]
- The longer path, followed by roughly half of the traces in each window, changed from A03 → A06 → A04 → A02 to A03 → A06 → A04 → A05 → A02: the step distance from A04, A06 and A03 to A02 each grew by exactly one, and A05's relative position (about 0.75) sits between A04 (0.5) and A02 (1.0). [REL010, REL012, REL014, LAG001, LAG002, LAG003, POS003, POS004, POS005]
- Minor shifts: participation in A03, A04 and A06 slipped from about 50 in 100 traces to 46 in 100, and the short path's share moved from about 50 in 100 to 54 in 100; differences of this size arise in roughly half of random re-splits of unchanged data, so they are consistent with sampling noise. [OCC002, OCC003, OCC005, REL006, REL010]

### Inference

Support level: Supported hypothesis

The evidence supports a structural change in the control flow involving A01, A04, A05 and A02: in the later window, A01 is no longer executed, so the former short path A01 → A02 runs as A02 alone, and A05 appears as a new step inserted between A04 and A02, turning the longer path A03 → A06 → A04 → A02 into A03 → A06 → A04 → A05 → A02. [OCC001, OCC004, DIR001, DIR002, DIR003, POS002, POS004, LAG002, REL008]

The support is direct and consistent across all five indicator families: both participation swings are maximal (about 50 in 100 to zero, and zero to 46 in 100) and exceed the difference seen in 199 of 200 random re-splits; the rerouting is observed directly in the successor profiles of A04 and A05 rather than inferred from positions alone; and the positional, step-distance and relational evidence all match an insertion between A04 and A02, with A05 co-occurring with A03, A04 and A06 in exactly the later long-path traces and in the expected order. [OCC001, OCC004, DIR002, DIR003, POS004, LAG001, LAG002, LAG003, REL011, REL013, REL015]

Limitations: zero participation only shows that A01 was not observed in the later sample, so a very rare continuation of A01 cannot be excluded; the reading that the later A02-only traces are the former A01 → A02 traces minus A01 is inferred from the overall variant structure rather than traced case by case, and a competing reading — that the old short path disappeared and a separate A02-only path appeared — cannot be ruled out; the small shift in the two paths' shares (about 50 to 54 in 100) remains within random-sampling variation. [OCC001, POS002, REL006]

Other differences: none beyond the slight participation dip of A03, A04 and A06 and the small share shift noted above, both of which stay within the range expected for unchanged data. [OCC002, OCC003, OCC005, REL010]