# gen_2410240603_000 — engine run 20261024_060503_gen_2410240603_000

Hypothesis: grammar draw seed=2410240603: rsi_revert

**0/8 pass.** Ledger N at evaluation: 1914. PBO (CSCV) across family: 0.044. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 a4e5e243904fc5a92d8a24883381229de605b30d3f6cccf614681b34ad52d0f6. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1907 | megacap|rsi_revert(entry=5,exit=60,n=3) | -0.11/0.02/-10.43 | 26.77 | 667 | 0.1179 | 0.87413 (10.21) | 1.0 | 0.0052 | 0.929 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1908 | megacap|rsi_revert(entry=5,exit=60,n=5) | 3.75/1.16/-1.52 | 26.77 | 68 | 0.095 | 0.89211 (13.76) | 1.0 | 0.131 | 0.8695 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1909 | megacap|rsi_revert(entry=5,exit=70,n=3) | 2.75/0.28/-7.43 | 26.77 | 639 | 0.1191 | 0.84016 (9.65) | 1.0 | 0.0128 | 0.907 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1910 | megacap|rsi_revert(entry=5,exit=70,n=5) | 5.57/1.36/-1.21 | 26.77 | 67 | 0.0958 | 0.86114 (12.4) | 1.0 | 0.1738 | 0.863 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1911 | megacap|rsi_revert(entry=20,exit=60,n=3) | -6.13/-0.28/-15.23 | 26.77 | 2437 | 0.1198 | 0.71129 (0.72) | 1.0 | 0.0018 | 0.971 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1912 | megacap|rsi_revert(entry=20,exit=60,n=5) | 7.76/0.51/-10.16 | 26.77 | 1030 | 0.1194 | 0.45954 (7.93) | 1.0 | 0.0273 | 0.8585 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1913 | megacap|rsi_revert(entry=20,exit=70,n=3) | -0.62/0.04/-16.97 | 26.77 | 2115 | 0.1214 | 0.75025 (2.09) | 1.0 | 0.0059 | 0.9365 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1914 | megacap|rsi_revert(entry=20,exit=70,n=5) | 14.28/0.7/-11.79 | 26.77 | 892 | 0.1193 | 0.56244 (8.72) | 1.0 | 0.0453 | 0.8445 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
