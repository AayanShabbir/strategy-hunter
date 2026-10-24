# gen_2310231905_001 — engine run 20261023_200357_gen_2310231905_001

Hypothesis: grammar draw seed=2310231905: donchian+vol_regime

**0/4 pass.** Ledger N at evaluation: 706. PBO (CSCV) across family: 0.441. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 7bb35aba6d16d8e2a340424b92926d23cd78e18d6d1190c6b67c0cd4cc0faeb0. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 703 | crypto|donchian(entry_n=20,exit_n=10)+vol_regime(max_atr_pct=0.06) | -2.64/0.09/-35.62 | 428.6 | 1653 | 0.1027 | 0.8002 (53.47) | 1.0 | 0.0385 | 0.923 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 704 | crypto|donchian(entry_n=20,exit_n=20)+vol_regime(max_atr_pct=0.06) | -5.08/0.08/-45.63 | 428.6 | 1285 | 0.0997 | 0.86613 (60.75) | 1.0 | 0.0385 | 0.922 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 705 | crypto|donchian(entry_n=100,exit_n=10)+vol_regime(max_atr_pct=0.06) | 31.24/0.97/-15.33 | 428.6 | 695 | 0.0988 | 0.66334 (92.96) | 1.0 | 0.2293 | 0.8925 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 706 | crypto|donchian(entry_n=100,exit_n=20)+vol_regime(max_atr_pct=0.06) | 33.55/0.91/-22.39 | 428.6 | 566 | 0.0965 | 0.65335 (177.37) | 1.0 | 0.2114 | 0.891 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
