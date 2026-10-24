# gen_2310231907_003 — engine run 20261023_200431_gen_2310231907_003

Hypothesis: grammar draw seed=2310231907: donchian

**0/4 pass.** Ledger N at evaluation: 758. PBO (CSCV) across family: 0.53. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 025a665124a9b410fdfd024fce8f26aaefd58525ddfba92f344ba4d064aea425. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 755 | crypto_d|donchian(entry_n=20,exit_n=10) | -8.35/-0.04/-26.1 | 268.18 | 82 | 0.0193 | 0.93806 (81.7) | 1.0 | 0.2206 | 0.905 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 756 | crypto_d|donchian(entry_n=20,exit_n=20) | 0.12/0.2/-33.03 | 268.18 | 59 | 0.0195 | 0.88911 (80.59) | 1.0 | 0.3108 | 0.905 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 757 | crypto_d|donchian(entry_n=100,exit_n=10) | 9.14/0.42/-17.9 | 268.18 | 30 | 0.02 | 0.76923 (168.08) | 1.0 | 0.411 | 0.8885 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 758 | crypto_d|donchian(entry_n=100,exit_n=20) | 5.71/0.28/-20.05 | 268.18 | 26 | 0.02 | 0.82717 (54.19) | 1.0 | 0.3494 | 0.893 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
