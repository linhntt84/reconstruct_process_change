### Observed differences

- Activity A02 disappears: it occurred in about 27 in 100 traces before and in none after; all its outgoing edges (to A03, A05, A07, A08, A13) vanish. [OCC001, DIR002, POS002, REL001, REL004, REL005, REL006, REL007, REL008]
- A01 moves from late to early: its mean position drops from 0.815 to 0, and its successor changes from A05 to A06. [POS001, DIR001]
- A11 and A12 now lead to A05 instead of A01: A11's outgoing share to A01 falls from 57% to 0 and to A05 rises to 70%; A12's to A01 falls from 43% to 0 and to A05 rises to 30%. [DIR004, DIR005]
- The order between A01 and A11/A12 reverses: before, A11/A12 preceded A01 in 27% of traces; after, A01 precedes A11/A12 in about 22% of traces. [REL002, REL003]
- A05 now occurs closer after A11 and A12 (lag 1–2 instead of 2–3), while the gap between A01 and A05 widens from lag 1 to lag 4. [LAG004, LAG005, LAG001]
- A07 no longer leads to A02 and now more often leads to A03 and A13; A05 follows A07 more closely (lag 2 instead of a spread over lags 1–4). [DIR003, LAG003]

### Inference

Support level: Supported hypothesis

The evidence supports a structural change in which A01 moved from a late position after A11/A12 to an early position, its successor changed from A05 to A06, and A11/A12 now lead to A05 instead of A01; A02 is no longer executed. This is directly shown by positional, relational and successor evidence, and the number of qualifying items (25) far exceeds the 0.22 expected by chance. A competing explanation that this is a rare sampling artefact is ruled out by the screening comparison. Other differences: A07's routing shifted away from A02 and toward A03/A13, and A05's lag relative to A07 shortened, both consistent with the removal of A02 and the new path to A05.