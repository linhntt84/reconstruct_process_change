### Observed differences

- In the earlier window, activities A15, A16, A25, A26, and A27 each occurred in all 200 traces; in the later window they occur in none. [OCC002, OCC003, OCC008, OCC009, OCC010]
- In the later window, activities A14, A17, A18, A19, and A20 appear in about 18%, 24%, 21%, 22%, and 16% of traces respectively, and they never co-occur with each other; in the earlier window they were absent. [OCC001, OCC004, OCC005, OCC006, OCC007, REL003, REL029, REL037, REL044]
- The successor of the main block changed: in the earlier window A15, A16, A25, A26, and A27 led to A28 (and others); in the later window A14, A17, A18, A19, and A20 lead to A28. [DIR001, DIR004, DIR005, DIR006, DIR007, DIR002, DIR003, DIR008, DIR009, DIR010]
- A43's outgoing transitions changed from the old set to the new set. [DIR011]
- A28's position moved earlier (mean from 0.46 to 0.39) and A43's later (0.28 to 0.33). [POS011, POS012]

### Inference

Support level: Supported hypothesis

The process likely changed from executing a fixed set of activities (A15, A16, A25, A26, A27) in every case to executing exactly one of a set of alternative activities (A14, A17, A18, A19, A20), with A43 before and A28 after remaining. This is supported by the complete disappearance of the old activities and appearance of the new ones, the mutual exclusivity of the new activities, and the successor changes to A28. The evidence cannot rule out that the new activities are simply renamed versions of the old ones, but the shift from all five being executed together to exactly one being chosen indicates a change in control flow, not just relabeling.

Other differences: A28 and A43 shifted slightly in position, but this is minor and does not affect the main hypothesis.