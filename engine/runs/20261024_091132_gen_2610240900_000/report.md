# gen_2610240900_000 — engine run 20261024_091132_gen_2610240900_000

Hypothesis: grammar draw seed=2610240900: donchian

**0/4 pass.** Ledger N at evaluation: 2190. PBO (CSCV) across family: 0.491. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 526c23dbfc8205f2052bf2bc1a20efb1e9f8cdb45079dc75dc1b6a775f02f523. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2187 | crypto|donchian(entry_n=20,exit_n=10) | 6.16/0.29/-23.85 | 56.21 | 48 | 0.0223 | 0.72228 (25.71) | 1.0 | 0.4089 | 0.8935 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2188 | crypto|donchian(entry_n=20,exit_n=20) | 24.86/0.62/-26.12 | 56.21 | 34 | 0.0221 | 0.49351 (25.77) | 1.0 | 0.5665 | 0.824 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2189 | crypto|donchian(entry_n=100,exit_n=10) | 13.94/0.52/-18.64 | 56.21 | 20 | 0.0224 | 0.67433 (28.7) | 1.0 | 0.5184 | 0.8355 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2190 | crypto|donchian(entry_n=100,exit_n=20) | 12.91/0.47/-23.93 | 56.21 | 18 | 0.0224 | 0.63736 (25.52) | 1.0 | 0.4957 | 0.8415 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
