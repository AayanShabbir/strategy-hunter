# gen_2610241205_000 — engine run 20261024_120736_gen_2610241205_000

Hypothesis: grammar draw seed=2610241205: donchian+trend_sma

**0/4 pass.** Ledger N at evaluation: 2506. PBO (CSCV) across family: 0.173. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 70ee677192ad71f4d59995231999b7c9dbfddf6d465b0c271234e9fd61134369. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2503 | crypto|donchian(entry_n=55,exit_n=10)+trend_sma(n=200) | 16.85/0.7/-13.83 | 434.62 | 32 | 0.0208 | 0.8002 (186.85) | 1.0 | 0.5645 | 0.9015 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2504 | crypto|donchian(entry_n=55,exit_n=20)+trend_sma(n=200) | 20.98/0.7/-12.98 | 434.62 | 29 | 0.0206 | 0.78721 (134.94) | 1.0 | 0.5664 | 0.8995 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2505 | crypto|donchian(entry_n=100,exit_n=10)+trend_sma(n=200) | 7.77/0.39/-13.83 | 434.62 | 24 | 0.0208 | 0.85115 (258.76) | 1.0 | 0.4187 | 0.907 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2506 | crypto|donchian(entry_n=100,exit_n=20)+trend_sma(n=200) | 11.57/0.46/-15.15 | 434.62 | 21 | 0.0206 | 0.80619 (201.51) | 1.0 | 0.4495 | 0.907 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
