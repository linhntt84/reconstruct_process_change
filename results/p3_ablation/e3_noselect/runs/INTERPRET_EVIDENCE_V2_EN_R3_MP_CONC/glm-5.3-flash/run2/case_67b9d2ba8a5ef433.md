### Observed differences

- Activity A01 was not observed at all in the earlier window (0 of 200 traces); in the later window it occurs exactly once in every trace (200 of 200), always at the same relative position about 83% of the way through the case. [OCC001, POS001]
- In the earlier window, A05 and A07 both occurred in every case without a fixed order between them (A05 first in about 52 in 100 cases), and A03 followed them directly: A05 led to A03 in about 48 in 100 of its outgoing transitions and to A07 in about 52; A07 led to A03 in about 52 and to A05 in about 48. [REL004, DIR003, DIR004]
- In the later window, the direct transitions from A05 and A07 into A03 are gone: A05 now leads to A01 in about 47 in 100 of its outgoing transitions (A07 in about 53), and A07 leads to A01 in about 53 (A05 in about 47), while A01's only observed outgoing transition goes to A03. [DIR003, DIR004, DIR001]
- The relationship of A01 to the other activities flipped from never co-occurring to always co-occurring in a fixed order: before, A03 always appeared without A01; after, A01 and A03 co-occur in every case with A01 first, and A05 as well as A07 always precede A01. [REL001, REL002, REL003]
- The distance from A05 and A07 to A03 grew by one step: before, A03 followed A05 at 1 step in about 48 in 100 cases and at 2 steps otherwise; after, it follows at 2 steps in about 47 and at 3 steps in about 53, with the same pattern for A07. [LAG001, LAG002]
- A05 and A07 shifted slightly earlier in relative position (mean about 0.70 to about 0.58), consistent with an extra event now following them. [POS002, POS003]
- Two behaviours stayed stable: A04's split between A05 and A07 (about 52/48 to about 53/47) and the unfixed mutual order of A05 and A07 (about 52/48 to about 53/47); both differences are small and unremarkable for an unchanged process. [DIR002, REL004]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that A01 was added as a new step, executed once per case between the A05/A07 stage and A03: in the earlier window cases ran A04, then A05 and A07 in either order, then A03 directly, whereas in the later window A01 runs after both A05 and A07 and before A03, so A03 is reached only through A01. [OCC001, DIR001, DIR003, DIR004, REL001, REL002, REL003, LAG001, LAG002, POS001]

The support is direct and consistent: the placement is shown relationally (A01 went from never co-occurring with A03, A05 and A07 to always co-occurring, positioned after A05/A07 and before A03), structurally (the A05→A03 and A07→A03 transitions were replaced by transitions into A01, and A01 always leads to A03), and by the exactly one-step increase in distance from A05/A07 to A03. Behaviours that this hypothesis predicts should stay stable did stay stable, namely A04's routing and the order-free A05/A07 pair. [POS002, POS003, REL004, DIR002]

Limitations: all items describe one underlying difference, so they are not independent confirmations; zero participation in the earlier window only shows A01 was not observed there, so an extremely rare pre-existing occurrence of A01 cannot be ruled out; and each window is a finite sample of 200 traces. [OCC001]