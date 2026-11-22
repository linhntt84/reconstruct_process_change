### Observed differences

- In the earlier window, A27 was executed in about 49 in 100 traces; in the later window it appears in about 99 in 100 traces, still at most once per trace in both windows. [OCC001]
- Five activities — A32, A33, A38, A39 and A40 — each appeared in about 51 in 100 traces in the earlier window; in the later window each appears in only about 2 in 100 traces (3–5 of 200 traces). [OCC002, OCC003, OCC004, OCC005, OCC006]
- In the earlier window, the segment between A26 and A28 had two mutually exclusive forms: about half the traces ran A26 → A27 → A28, while the other half ran A26, then the five activities together (each pair of them co-occurred in about 51 in 100 traces, in either order roughly 25/25, i.e. with no fixed order among them), then A28; A27 never co-occurred with any of the five. In the later window, A26 precedes A27 in about 99 in 100 traces and A27 precedes A28 in about 99 in 100, while the five activities co-occur with A26, with A28 or with each other in only about 1–2 in 100 traces. [REL001, REL007, REL008, REL012, REL013, REL017, REL018, REL027]
- Outgoing routing from A26 changed accordingly: in the earlier window about 48 in 100 of A26's outgoing transitions went to A27 and about 51 in 100 went to the five block activities (roughly 8–12 in 100 each); in the later window about 99 in 100 go to A27. [DIR001]
- A26 and A28 themselves appear in every trace in both windows, so the difference is confined to the segment between them. The later-window routing, position and lag profiles of the five activities rest on only 1–5 observations and are too thin to describe how the block behaves in the few traces where it still occurs. [POS001, POS002, DIR002, POS003, LAG008]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that, in the later window, the five-activity segment A32, A33, A38, A39, A40 — which previously ran together in about half of all cases between A26 and A28 — is skipped in almost all cases, while the alternative path through A27, previously taken in the other half of the cases, now runs in nearly every case in the fixed order A26 → A27 → A28. [OCC001, OCC002, REL001, REL007, REL018]

The support is direct and consistent: the participation changes are large and measured on 200 traces per window; the relational items show the earlier mutual exclusivity and the later near-universality of A26 → A27 → A28 directly; the routing change at A26 matches; and 63 items qualified in screening against roughly 0.76 expected if nothing had changed, a volume chance sampling cannot explain. The many agreeing items largely describe one underlying trace behaviour rather than independent confirmations, but occurrence, routing and co-occurrence each show the same difference on its own. [DIR001, OCC001, REL007]

Limitations: near-zero participation means the five activities were not observed, not that they were provably removed — they may persist as a rare exception (about 2–3 in 200 later-window traces), and the thin later-window profiles cannot show how the block behaves there. The evidence also cannot show whether the block's work is now performed elsewhere in the trace. [OCC002, DIR002, LAG008]

Other differences: A26's mean relative position moved slightly later (about 0.46 → 0.49) and A28's slightly earlier (about 0.59 → 0.56), consistent with the middle segment shrinking; these are event-position shifts, not clock-time changes. [POS001, POS002]