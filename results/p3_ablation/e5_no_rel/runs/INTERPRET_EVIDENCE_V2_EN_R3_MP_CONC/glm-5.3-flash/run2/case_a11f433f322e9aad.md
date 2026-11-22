### Observed differences

- In the earlier window, A27 was executed in every trace (200 of 200, once per trace); in the later window it appears in only about half of the traces (about 102 of 200, 51%), still once per trace and still followed by A28 in about 96 in 100 of its outgoing transitions. [OCC001, DIR002]
- A32, A33 and A38 are absent from the earlier window (0 of 200 traces) but each occurs in about half of the later-window traces (about 98–99 of 200, roughly 49 in 100), once per trace when present. [OCC002, OCC003, OCC004]
- In the earlier window, about 99 in 100 of A26's outgoing transitions went to A27; in the later window only about 50 in 100 do, with the remainder going to A33 (about 17 in 100), A38 (about 16) and A32 (about 15). [DIR001]
- In the later window the three new activities run together as a block in varying order: each pair occurs in both directions (for example A32→A33 in about 34 in 100 of A32's outgoing transitions and A33→A32 in about 43 in 100 of A33's), and each of the three can be the last one, leading on to A28 (about 28, 27 and 43 in 100 for A32, A33 and A38 respectively). [DIR003, DIR004, DIR005]
- The new activities sit around the middle of the trace in the later window (median normalised position about 0.5); they had no position distribution at all before. [POS001, POS002, POS003]
- The distance from A26 to A28 was 2 positions in about 98 in 100 of earlier cases (one activity, A27, between them); in the later window it is 2 positions in about 50 in 100 and 4 positions in about 48 in 100, i.e. three activities between them in roughly half the cases. [LAG001]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that, in the later window, a block of three activities — A32, A33 and A38 — is executed between A26 and A28 in about half of the cases, as an alternative to A27: the earlier pattern A26 → A27 → A28 still runs in roughly half of the later traces, while in the other half A27 is not executed and A32, A33 and A38 all run, in no fixed order among themselves, before A28. [DIR001, DIR003, DIR004, DIR005, LAG001, OCC001, OCC002, OCC003, OCC004]

The signs are direct and mutually consistent: the split is observed directly in A26's outgoing transitions; the block's internal edges and its edges to A28 show where it sits; the A26→A28 distance grows from one intervening activity to three in about half the cases, matching a three-activity insertion; and A27's participation falls from all traces to about half while its own edge to A28 is essentially unchanged. Thirteen control-flow items qualified against roughly 0.5 expected by chance in an unchanged process, so sampling noise cannot explain the ensemble as a whole — though the occurrence, direction, position and lag items partly describe the same traces, so they are consistent rather than independent confirmations. [OCC001, OCC002, OCC003, OCC004, DIR001, DIR002, DIR003, DIR004, DIR005, POS001, POS002, POS003, LAG001]

Limitations: the evidence cannot show what determines whether a case takes the A27 path or the new block, nor distinguish a modification at this point from a shift in the mix of coexisting variants — although zero occurrences of A32, A33 or A38 in 200 earlier traces makes a stable variant mix unlikely. Because each pair of the new activities appears in both orders, no fixed sequence within the block can be claimed. [OCC002, OCC003, OCC004, DIR003, DIR004, DIR005]

Other differences: a few weak new edges appear in the later window (A26→A23, A27→A09/A34/A25, A32→A06/A25, A38→A02) at roughly 1–2 in 100 outgoing transitions each; these are small and may reflect sampling variation. [DIR001, DIR002, DIR003, DIR005]