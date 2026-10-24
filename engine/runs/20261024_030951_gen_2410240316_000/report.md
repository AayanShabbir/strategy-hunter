# gen_2410240316_000 — engine run 20261024_030951_gen_2410240316_000

Hypothesis: grammar draw seed=2410240316: donchian

**0/4 pass.** Ledger N at evaluation: 1666. PBO (CSCV) across family: 0.794. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 6cd6ed2700b22ef0a5f9d0979f0bd1c4f21b02059ef820b65127e449df157cee. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1663 | crypto_d|donchian(entry_n=20,exit_n=10) | -12.9/-0.11/-31.6 | 234.6 | 110 | 0.0173 | 0.97003 (77.95) | 1.0 | 0.0698 | 0.908 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1664 | crypto_d|donchian(entry_n=20,exit_n=20) | -2.02/0.17/-38.62 | 234.6 | 80 | 0.0168 | 0.91608 (77.66) | 1.0 | 0.1263 | 0.91 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1665 | crypto_d|donchian(entry_n=100,exit_n=10) | 15.9/0.55/-21.16 | 234.6 | 39 | 0.0184 | 0.78022 (142.29) | 1.0 | 0.2438 | 0.889 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1666 | crypto_d|donchian(entry_n=100,exit_n=20) | 19.48/0.59/-23.98 | 234.6 | 32 | 0.0186 | 0.71029 (55.56) | 1.0 | 0.2583 | 0.889 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
