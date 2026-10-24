# gen_2610241206_000 — engine run 20261024_120738_gen_2610241206_000

Hypothesis: grammar draw seed=2610241206: supertrend+relvol

**0/4 pass.** Ledger N at evaluation: 2510. PBO (CSCV) across family: 0.926. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 a9ce7db39745e8c625a430183fa6b8be017414b3b4e3b6cfd0ab77807fef8e41. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2507 | megacap|supertrend(atr_n=7,mult=2)+relvol(min_ratio=1.2) | 1.73/0.12/-10.4 | 118.49 | 293 | 0.0572 | 0.98701 (42.84) | 1.0 | 0.4011 | 0.482 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2508 | megacap|supertrend(atr_n=7,mult=3)+relvol(min_ratio=1.2) | 0.44/0.06/-8.36 | 118.49 | 305 | 0.0586 | 0.995 (44.83) | 1.0 | 0.3566 | 0.4865 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2509 | megacap|supertrend(atr_n=10,mult=2)+relvol(min_ratio=1.2) | 1.79/0.13/-10.67 | 118.49 | 300 | 0.0567 | 0.98202 (41.61) | 1.0 | 0.4027 | 0.4785 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2510 | megacap|supertrend(atr_n=10,mult=3)+relvol(min_ratio=1.2) | -1.19/-0.04/-9.06 | 118.49 | 317 | 0.0578 | 0.997 (43.99) | 1.0 | 0.3003 | 0.4925 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
