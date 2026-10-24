# gen_2610240800_000 — engine run 20261024_080310_gen_2610240800_000

Hypothesis: grammar draw seed=2610240800: supertrend+relvol

**0/4 pass.** Ledger N at evaluation: 2094. PBO (CSCV) across family: 0.792. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 9a536ad8f6d5c17a4d1ac081837bf8fedbf34041eb787f1552a1c0ba09aa7a9b. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2091 | crypto|supertrend(atr_n=7,mult=3)+relvol(min_ratio=1.2) | -54.62/-2.7/-58.67 | 428.6 | 8076 | 0.1032 | 0.88212 (-2.04) | 1.0 | 0.0038 | 0.93 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2092 | crypto|supertrend(atr_n=7,mult=4)+relvol(min_ratio=1.2) | -54.47/-2.95/-57.55 | 428.6 | 8140 | 0.1034 | 0.88911 (-11.3) | 1.0 | 0.0008 | 0.929 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2093 | crypto|supertrend(atr_n=10,mult=3)+relvol(min_ratio=1.2) | -56.97/-2.85/-60.54 | 428.6 | 8141 | 0.103 | 0.90909 (-24.78) | 1.0 | 0.0029 | 0.931 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2094 | crypto|supertrend(atr_n=10,mult=4)+relvol(min_ratio=1.2) | -57.46/-3.23/-59.97 | 428.6 | 8200 | 0.1037 | 0.92507 (12.05) | 1.0 | 0.0005 | 0.93 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
