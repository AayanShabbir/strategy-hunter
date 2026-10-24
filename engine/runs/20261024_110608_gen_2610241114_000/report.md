# gen_2610241114_000 — engine run 20261024_110608_gen_2610241114_000

Hypothesis: grammar draw seed=2610241114: supertrend+relvol

**0/4 pass.** Ledger N at evaluation: 2462. PBO (CSCV) across family: 0.384. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 9077ff578f3a163d9f77320b5f87657ed894e25b07460d25ed634db6e25e6104. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2459 | BROAD|supertrend(atr_n=7,mult=3)+relvol(min_ratio=1.0) | 1.16/0.09/-15.98 | 83.36 | 749 | 0.0881 | 0.98901 (25.15) | 1.0 | 0.4054 | 0.489 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2460 | BROAD|supertrend(atr_n=7,mult=4)+relvol(min_ratio=1.0) | -1.67/-0.03/-18.4 | 83.36 | 767 | 0.0877 | 0.99301 (24.51) | 1.0 | 0.3275 | 0.489 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2461 | BROAD|supertrend(atr_n=10,mult=3)+relvol(min_ratio=1.0) | 1.38/0.1/-16.71 | 83.36 | 754 | 0.0876 | 0.98701 (25.36) | 1.0 | 0.4116 | 0.488 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2462 | BROAD|supertrend(atr_n=10,mult=4)+relvol(min_ratio=1.0) | -0.98/-0.0/-17.61 | 83.36 | 734 | 0.0866 | 0.995 (25.92) | 1.0 | 0.3458 | 0.4915 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
