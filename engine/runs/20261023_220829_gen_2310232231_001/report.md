# gen_2310232231_001 — engine run 20261023_220829_gen_2310232231_001

Hypothesis: grammar draw seed=2310232231: rsi_revert+trend_sma

**0/8 pass.** Ledger N at evaluation: 1090. PBO (CSCV) across family: 0.614. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 199e7b1b25241439634c1cfa9a98898936ecd3acd90dca007170e049e21b4792. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1083 | crypto|rsi_revert(entry=10,exit=60,n=2)+trend_sma(n=100) | -22.16/-1.28/-26.8 | 428.6 | 2475 | 0.1011 | 0.92807 (135.7) | 1.0 | 0.0 | 0.9215 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1084 | crypto|rsi_revert(entry=10,exit=60,n=5)+trend_sma(n=100) | -2.31/-0.95/-2.58 | 428.6 | 97 | 0.1056 | 0.94805 (82.67) | 1.0 | 0.0 | 0.91 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1085 | crypto|rsi_revert(entry=10,exit=80,n=2)+trend_sma(n=100) | -29.65/-1.53/-34.68 | 428.6 | 2605 | 0.1018 | 0.97003 (140.24) | 1.0 | 0.0 | 0.9225 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1086 | crypto|rsi_revert(entry=10,exit=80,n=5)+trend_sma(n=100) | 2.53/0.46/-6.23 | 428.6 | 341 | 0.1122 | 0.90909 (188.4) | 1.0 | 0.0046 | 0.906 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1087 | crypto|rsi_revert(entry=20,exit=60,n=2)+trend_sma(n=100) | -37.59/-1.9/-39.28 | 428.6 | 4713 | 0.1027 | 0.94206 (32.39) | 1.0 | 0.0 | 0.9255 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1088 | crypto|rsi_revert(entry=20,exit=60,n=5)+trend_sma(n=100) | -20.45/-2.16/-22.22 | 428.6 | 845 | 0.098 | 0.98302 (65.6) | 1.0 | 0.0 | 0.917 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1089 | crypto|rsi_revert(entry=20,exit=80,n=2)+trend_sma(n=100) | -35.74/-1.52/-44.08 | 428.6 | 4331 | 0.1034 | 0.93706 (34.51) | 1.0 | 0.0 | 0.925 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1090 | crypto|rsi_revert(entry=20,exit=80,n=5)+trend_sma(n=100) | -23.15/-1.36/-28.09 | 428.6 | 1766 | 0.1029 | 0.95704 (48.28) | 1.0 | 0.0 | 0.9195 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
