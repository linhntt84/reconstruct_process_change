### Observed differences

- In the later window, A01 and A02 are no longer executed at all: earlier each ran in about 50 of 100 traces (about one occurrence per trace, and the two always appeared together); now neither appears in any of the 200 traces. Their outgoing edges disappeared with them — A01 previously fed A07 (about 45%), A10 (about 27%) and A08 (about 24%) of its outgoing transitions, and A02 always led to A14. [OCC001, OCC002, DIR001, DIR002, REL001]

- In the later window, A09 is newly present: it was absent earlier and now runs in about 24 of 100 traces (about 0.4 occurrences per trace), sits around the middle of the trace, and leads to A11 (about 46%), A12 (about 44%) and A07 (about 10%) of its outgoing transitions. [OCC005, POS005, DIR007]

- In the later window several successor relations changed: A08 now always leads to A10 (earlier always A05); A06 now always leads to A14 (earlier split between A13, about 51%, and A02, about 49%); A13 now always leads to A14 (earlier about 99% to A06); A04 now leads to A13 in about 39% of its outgoing transitions (earlier about 99% to A06); A14 now leads to A08 (about 56%) and A07 (about 35%) instead of always A01. [DIR006, DIR004, DIR010, DIR003, DIR011]

- Further downstream, A07 now sends about 48% of its outgoing transitions to A09 (earlier about 92% to A12), A11 sends about 52% to A13 (earlier about 97% to A06), and A12 sends about 42% to A09 (earlier about 95% to A11). [DIR005, DIR008, DIR009]

- The rewiring also shows in co-occurrence and spacing: A08 and A10, which never appeared together earlier, now occur together in about 50 of 100 traces with A08 first in all of them; A09 now co-occurs with A07, A08, A10, A11, A12 and A14 in roughly 18–24 of 100 traces (earlier never); typical distances shortened, e.g. A04 then A08 within five steps now at 3 steps apart (earlier 5) and A06 then A08 at 2 (earlier 4). [REL039, REL037, REL038, REL041, REL042, REL043, REL045, LAG003, LAG009]

- Frequencies shifted as well: A08 and A10 now run in about 50 of 100 traces (earlier about 24 and 26); A06 now runs in about 36 of 100 traces (earlier about 50) and repeats far less (mean about 2.0 → 0.5 occurrences per trace); A13 now runs in about 28 of 100 traces with mean occurrences down from 1.0 to about 0.4. [OCC003, OCC004, OCC006, OCC007]

### Inference

Support level: Supported hypothesis

The evidence supports a structural reorganisation of the control flow: A01 and A02 are no longer executed, A09 is newly executed, and the surrounding flow was rewired — A08 now leads to A10 instead of A05, A06 and A13 now lead to A14, A04 frequently leads to A13, A14 leads to A08 and A07 instead of A01, and A07 and A12 frequently lead to the new A09 while A11 frequently leads to A13. The change is shown directly by occurrence counts (99 vs 0 traces for A01 and A02; 0 vs 47 for A09), by successor-profile changes resting on roughly 79–200 observed outgoing transitions per window, and by co-occurrence and distance items moving in the same direction; 107 qualifying control-flow items against roughly 0.64 expected without change in that family means chance sampling cannot account for the pattern as a whole. [OCC001, OCC002, OCC005, DIR003, DIR004, DIR006, DIR007, DIR010, DIR011, REL039, LAG003, screening]

The main competing explanation the evidence cannot rule out is that the two windows draw from different case populations or variant mixes rather than a modified process; also, zero participation strictly means only that A01 and A02 were not observed in the later sample. [OCC001, OCC002]

Other differences: A08 and A10 now run in about half of all traces (earlier about a quarter each); A07, A08, A10, A12 and A14 sit slightly earlier within the trace by event position (for example A08's median position about 0.92 → 0.60), which on its own does not establish a move in clock time. [OCC004, OCC006, POS003, POS004, POS006, POS007, POS008]