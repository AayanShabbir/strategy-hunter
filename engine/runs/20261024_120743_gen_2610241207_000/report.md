# gen_2610241207_000 — engine run 20261024_120743_gen_2610241207_000

Hypothesis: grammar draw seed=2610241207: rsi_revert+vol_regime

**0/8 pass.** Ledger N at evaluation: 2518. PBO (CSCV) across family: 0.414. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 0a0f3041d9deb79d1f7e9eb2b6edc25e736db6ab5e75cc6c0f3f529821d97f34. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2511 | sectors|rsi_revert(entry=5,exit=70,n=3)+vol_regime(max_atr_pct=0.02) | 2.48/0.67/-1.66 | 94.31 | 32 | 0.0691 | 0.996 (40.65) | 1.0 | 0.4522 | 0.496 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2512 | sectors|rsi_revert(entry=5,exit=70,n=5)+vol_regime(max_atr_pct=0.02) | 1.01/0.39/-1.22 | 94.31 | 5 | 0.0644 | 0.94605 (41.72) | 1.0 | 0.2772 | 0.495 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2513 | sectors|rsi_revert(entry=5,exit=80,n=3)+vol_regime(max_atr_pct=0.02) | 3.83/0.85/-1.53 | 94.31 | 38 | 0.0611 | 0.998 (41.55) | 1.0 | 0.5895 | 0.499 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2514 | sectors|rsi_revert(entry=5,exit=80,n=5)+vol_regime(max_atr_pct=0.02) | 1.82/0.66/-1.22 | 94.31 | 5 | 0.0644 | 0.94605 (39.98) | 1.0 | 0.4551 | 0.497 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2515 | sectors|rsi_revert(entry=10,exit=70,n=3)+vol_regime(max_atr_pct=0.02) | 7.69/0.69/-3.59 | 94.31 | 88 | 0.0693 | 0.997 (39.86) | 1.0 | 0.4767 | 0.4995 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2516 | sectors|rsi_revert(entry=10,exit=70,n=5)+vol_regime(max_atr_pct=0.02) | 2.97/0.75/-1.22 | 94.31 | 23 | 0.0554 | 0.97802 (41.51) | 1.0 | 0.5153 | 0.494 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2517 | sectors|rsi_revert(entry=10,exit=80,n=3)+vol_regime(max_atr_pct=0.02) | 14.39/1.02/-4.19 | 94.31 | 96 | 0.0662 | 0.97702 (38.82) | 1.0 | 0.6921 | 0.5045 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2518 | sectors|rsi_revert(entry=10,exit=80,n=5)+vol_regime(max_atr_pct=0.02) | 4.35/1.01/-1.22 | 94.31 | 28 | 0.0514 | 0.97802 (39.03) | 1.0 | 0.701 | 0.4975 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
