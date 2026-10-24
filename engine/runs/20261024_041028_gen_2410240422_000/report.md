# gen_2410240422_000 — engine run 20261024_041028_gen_2410240422_000

Hypothesis: grammar draw seed=2410240422: donchian+rsi_band

**0/4 pass.** Ledger N at evaluation: 1774. PBO (CSCV) across family: 0.474. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 68036752d41191c8332c80edd5a1d2c22e83fcbb2f1d3ca1f617262e8d2304b5. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1771 | semis|donchian(entry_n=20,exit_n=10)+rsi_band(hi=80) | 157.01/1.6/-20.63 | 440.15 | 258 | 0.033 | 0.2967 (136.8) | 1.0 | 0.9881 | 0.502 | False | beats_buy_hold, cost_stop, holm, spa |
| 1772 | semis|donchian(entry_n=20,exit_n=20)+rsi_band(hi=80) | 216.03/1.7/-20.41 | 440.15 | 199 | 0.0321 | 0.03796 (136.87) | 1.0 | 0.9907 | 0.5145 | False | beats_buy_hold, cost_stop, holm, spa |
| 1773 | semis|donchian(entry_n=55,exit_n=10)+rsi_band(hi=80) | 101.57/1.45/-16.8 | 440.15 | 202 | 0.0352 | 0.79221 (133.95) | 1.0 | 0.9747 | 0.5055 | False | beats_buy_hold, cost_stop, holm, spa |
| 1774 | semis|donchian(entry_n=55,exit_n=20)+rsi_band(hi=80) | 136.58/1.56/-18.81 | 440.15 | 161 | 0.0344 | 0.48951 (138.35) | 1.0 | 0.9827 | 0.521 | False | beats_buy_hold, cost_stop, holm, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
