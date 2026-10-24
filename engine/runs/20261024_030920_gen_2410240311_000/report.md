# gen_2410240311_000 — engine run 20261024_030920_gen_2410240311_000

Hypothesis: grammar draw seed=2410240311: supertrend+trend_sma

**0/4 pass.** Ledger N at evaluation: 1626. PBO (CSCV) across family: 0.455. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 6e4e181d04655a846107dcf37343e02c5ee39e54fc99782bf41ad2896eb9f464. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1623 | crypto|supertrend(atr_n=10,mult=2)+trend_sma(n=50) | -8.58/-0.04/-32.08 | 428.6 | 3240 | 0.1024 | 0.73227 (108.51) | 1.0 | 0.3168 | 0.9225 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1624 | crypto|supertrend(atr_n=10,mult=4)+trend_sma(n=50) | 2.77/0.22/-38.65 | 428.6 | 2505 | 0.1067 | 0.68731 (46.15) | 1.0 | 0.4309 | 0.9205 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1625 | crypto|supertrend(atr_n=14,mult=2)+trend_sma(n=50) | -0.59/0.14/-30.62 | 428.6 | 3241 | 0.1017 | 0.68631 (67.39) | 1.0 | 0.3966 | 0.92 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1626 | crypto|supertrend(atr_n=14,mult=4)+trend_sma(n=50) | -1.79/0.12/-40.68 | 428.6 | 2520 | 0.1054 | 0.75025 (107.31) | 1.0 | 0.3861 | 0.923 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
