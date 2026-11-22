# P3: token usage per ablation (glm-5.3-flash), medians, paired with P2 run 1

Generated from the run records (`usage`, `latency_seconds`). P2 ran without streaming: the API returned only total completion tokens (reasoning + text). P3 ran with streaming (`stream_options.include_usage`), which also reports reasoning and text tokens; cases of a P3 run generated before the switch to streaming have totals only (column 'n stream').

| Exp | Set | n | n stream | Prompt tok P2→var | Completion tok P2→var | Reasoning tok (var) | Text tok (var) | Latency s P2→var | Cost USD (var, sum) |
|---|---|---|---|---|---|---|---|---|---|
| e3_noselect | cdlg | 100 | 100 | 8,676→16,385 | 11,314→14,316 | 12,910 | 1,260 | 65→91 | 1.14 |
| e3_noselect | null_cdlg | 50 | 50 | 1,956→7,556 | 121→12,165 | 11,305 | 907 | 1→74 | 0.35 |
| e3_noselect | null_ostovar3 | 39 | 39 | 1,957→39,184 | 122→31,204 | 28,819 | 2,020 | 1→188 | 0.83 |
| e3_noselect | ostovar3 | 78 | 78 | 18,347→59,082 | 13,772→19,724 | 17,720 | 1,952 | 78→127 | 1.56 |
| e3b_v2en | null_ostovar3 | 39 | 39 | 1,957→1,486 | 122→143 | 108 | 35 | 1→1 | 0.06 |
| e3b_v2en | ostovar3 | 78 | 78 | 18,347→17,876 | 13,772→13,766 | 12,412 | 1,332 | 78→85 | 0.79 |
| e5_no_occ | ostovar3 | 78 | 78 | 18,347→17,758 | 13,772→15,144 | 13,770 | 1,424 | 78→110 | 0.85 |
| e5_no_dir | ostovar3 | 78 | 78 | 18,347→15,764 | 13,772→12,504 | 11,230 | 1,296 | 78→89 | 0.76 |
| e5_no_pos | ostovar3 | 78 | 78 | 18,347→15,794 | 13,772→14,848 | 13,450 | 1,367 | 78→107 | 0.84 |
| e5_no_rel | ostovar3 | 78 | 78 | 18,347→10,652 | 13,772→13,228 | 11,994 | 1,231 | 78→93 | 0.70 |
| e5_no_lag | ostovar3 | 78 | 78 | 18,347→15,303 | 13,772→13,616 | 12,386 | 1,281 | 78→84 | 0.76 |
| e5_no_time | e4a | 26 | 26 | 17,908→16,950 | 15,334→12,898 | 11,733 | 1,285 | 82→76 | 0.26 |
| e5_no_cf | e4a | 26 | 26 | 17,908→2,970 | 15,334→5,500 | 4,893 | 568 | 82→34 | 0.10 |
| e8_labels | e4b | 40 | 40 | 8,192→8,209 | 12,890→12,029 | 11,114 | 966 | 70→73 | 0.30 |
| e9_shuffle | cdlg | 100 | 15 | 8,676→8,676 | 11,314→12,955 | 18,661 | 1,426 | 65→94 | 0.21 |
| e9_shuffle | ostovar3 | 78 | 19 | 18,347→18,347 | 13,772→14,840 | 23,987 | 1,949 | 78→117 | 0.34 |

Total P3 generation cost reported by the API (streamed calls only): 9.85 USD.

Note: in e9_shuffle only the 34 cases regenerated after HTTP 524 errors were streamed; their reasoning medians come from the slowest cases and are not representative.
