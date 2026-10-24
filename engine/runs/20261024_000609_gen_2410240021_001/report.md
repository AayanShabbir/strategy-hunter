# gen_2410240021_001 — engine run 20261024_000609_gen_2410240021_001

Hypothesis: grammar draw seed=2410240021: supertrend+relvol

**0/4 pass.** Ledger N at evaluation: 1334. PBO (CSCV) across family: 0.038. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 305af9c85b66407c59f2cb59a246b9777819f2057867521f99d1e12450b3c4c8. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1331 | sectors|supertrend(atr_n=7,mult=2)+relvol(min_ratio=1.0) | -4.42/-0.4/-7.02 | 50.2 | 2355 | 0.0772 | 1.0 (14.33) | 1.0 | 0.0045 | 0.505 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1332 | sectors|supertrend(atr_n=7,mult=4)+relvol(min_ratio=1.0) | -11.73/-0.99/-14.59 | 50.2 | 2242 | 0.0818 | 1.0 (14.34) | 1.0 | 0.0001 | 0.5045 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1333 | sectors|supertrend(atr_n=14,mult=2)+relvol(min_ratio=1.0) | -4.52/-0.39/-7.72 | 50.2 | 2449 | 0.0768 | 1.0 (14.59) | 1.0 | 0.0051 | 0.504 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1334 | sectors|supertrend(atr_n=14,mult=4)+relvol(min_ratio=1.0) | -11.56/-0.93/-14.5 | 50.2 | 2387 | 0.0805 | 1.0 (14.53) | 1.0 | 0.0002 | 0.515 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
