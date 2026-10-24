# gen_2410240001_002 — engine run 20261024_000539_gen_2410240001_002

Hypothesis: grammar draw seed=2410240001: donchian+trend_sma

**0/4 pass.** Ledger N at evaluation: 1302. PBO (CSCV) across family: 0.551. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 0660872cb1f098ea5418c36d84e3c617e0c4e62ef0c66bb1cfb07ee7113857ee. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1299 | crypto_d|donchian(entry_n=20,exit_n=10)+trend_sma(n=100) | 6.75/0.3/-27.82 | 234.6 | 111 | 0.0173 | 0.86114 (74.72) | 1.0 | 0.5733 | 0.8975 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1300 | crypto_d|donchian(entry_n=20,exit_n=20)+trend_sma(n=100) | 10.51/0.37/-27.82 | 234.6 | 124 | 0.0172 | 0.82917 (120.52) | 1.0 | 0.6064 | 0.899 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1301 | crypto_d|donchian(entry_n=55,exit_n=10)+trend_sma(n=100) | 6.74/0.3/-29.59 | 234.6 | 66 | 0.0175 | 0.86513 (116.7) | 1.0 | 0.5734 | 0.8955 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1302 | crypto_d|donchian(entry_n=55,exit_n=20)+trend_sma(n=100) | 10.75/0.38/-30.69 | 234.6 | 71 | 0.0176 | 0.83217 (73.57) | 1.0 | 0.6116 | 0.8985 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
