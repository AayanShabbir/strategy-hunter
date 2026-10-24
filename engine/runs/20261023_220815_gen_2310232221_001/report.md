# gen_2310232221_001 — engine run 20261023_220815_gen_2310232221_001

Hypothesis: grammar draw seed=2310232221: donchian

**0/4 pass.** Ledger N at evaluation: 1062. PBO (CSCV) across family: 0.325. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 7df32351d2977d7e04cf2a706c20aae2a69b77262876850e8bb336433000ec28. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1059 | megacap|donchian(entry_n=20,exit_n=10) | -8.39/-0.34/-14.91 | 26.77 | 220 | 0.1111 | 0.70629 (12.45) | 1.0 | 0.0001 | 0.9135 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1060 | megacap|donchian(entry_n=20,exit_n=20) | -1.17/0.03/-16.39 | 26.77 | 159 | 0.1097 | 0.27473 (12.43) | 1.0 | 0.0015 | 0.891 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1061 | megacap|donchian(entry_n=55,exit_n=10) | 7.27/1.3/-1.89 | 26.77 | 41 | 0.1094 | 0.83616 (12.3) | 1.0 | 0.0883 | 0.8435 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1062 | megacap|donchian(entry_n=55,exit_n=20) | -3.88/-0.12/-14.84 | 26.77 | 37 | 0.1093 | 0.64935 (13.23) | 1.0 | 0.0005 | 0.914 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
