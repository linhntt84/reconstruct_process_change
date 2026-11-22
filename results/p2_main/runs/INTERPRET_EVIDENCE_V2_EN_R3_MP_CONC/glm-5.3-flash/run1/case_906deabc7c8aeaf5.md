### Observed differences

- Activity A05 was executed exactly once in every earlier-window trace (200 of 200 cases) but appears in none of the 200 later-window traces. [OCC001, POS002]
- In the earlier window, every observed outgoing transition of A01 went to A05, and every observed outgoing transition of A05 went to A02. In the later window, A01 leads directly to A02 in all observed transitions, and A05 has no observed outgoing transitions at all. [DIR001, DIR002]
- The pairs A01–A05 and A02–A05 changed from always co-occurring in a fixed order (A01 before A05, and A05 before A02, in 100 in 100 traces) to never co-occurring: in the later window A01 and A02 each appear without A05 in every trace. [REL001, REL002]
- A02 now follows A01 one step sooner: the A01→A02 distance was 2 steps in all earlier traces and is 1 step in all later traces. [LAG001]
- A02 still occurs in every trace in both windows, but sits earlier in the case: its mean position moved from 0.5 to about 0.33. [POS001]

### Inference

Support level: Supported hypothesis

Main hypothesis: A05 is no longer executed between A01 and A02 — cases that previously ran A01 → A05 → A02 now run A01 → A02 directly, so A05 is skipped or has been taken out of the flow. In the earlier window A05 ran once per case in 100% of traces, always between A01 and A02; in the later window it is absent from all 200 traces, A01 leads straight to A02, and the A01→A02 distance shrank from two steps to one. [OCC001, DIR001, DIR002, REL001, REL002, LAG001, POS002]

The change is shown directly by the successor change at A01 and the collapse of A05's co-occurrence with both neighbours, and all eight qualifying items describe this one difference consistently rather than several unrelated ones; eight items is far above the roughly 0.04 expected by chance for this family, so the set as a whole is not what an unchanged process typically produces. [OCC001, DIR001, DIR002, POS001, POS002, REL001, REL002, LAG001]

Competing explanation the evidence cannot rule out: whether A05 was formally removed, became a branch that is never taken, or was relabelled to another activity code cannot be distinguished here; behaviourally the observed result is the same — A05 is not executed in any later-window case — but the underlying mechanism remains open. [OCC001, DIR001]