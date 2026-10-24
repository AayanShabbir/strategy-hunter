# gen_2310232231_003 — engine run 20261023_220842_gen_2310232231_003

Hypothesis: grammar draw seed=2310232231: sma_cross+trend_sma

**0/4 pass.** Ledger N at evaluation: 1102. PBO (CSCV) across family: 0.555. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 d5dcec326c08abe8ac6710786b5cce4344359478fbc51d466ed93030e615aa03. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1099 | crypto|sma_cross(fast=20,slow=50)+trend_sma(n=100) | -24.21/-0.41/-47.22 | 428.6 | 1983 | 0.1073 | 0.95005 (121.13) | 1.0 | 0.0448 | 0.924 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1100 | crypto|sma_cross(fast=20,slow=200)+trend_sma(n=100) | -14.62/-0.17/-42.0 | 428.6 | 1690 | 0.1071 | 0.88911 (141.12) | 1.0 | 0.0789 | 0.9225 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1101 | crypto|sma_cross(fast=50,slow=50)+trend_sma(n=100) | 0.0/0.0/0.0 | 428.6 | 0 | inf | 1.0 (42.03) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1102 | crypto|sma_cross(fast=50,slow=200)+trend_sma(n=100) | 1.81/0.19/-36.56 | 428.6 | 1601 | 0.1085 | 0.75225 (65.65) | 1.0 | 0.1643 | 0.918 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
