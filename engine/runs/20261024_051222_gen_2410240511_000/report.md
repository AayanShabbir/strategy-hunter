# gen_2410240511_000 — engine run 20261024_051222_gen_2410240511_000

Hypothesis: grammar draw seed=2410240511: supertrend+relvol

**0/4 pass.** Ledger N at evaluation: 1802. PBO (CSCV) across family: 0.413. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 62edf9bc36e140b56cfeeabb6505df5009284b76654108829d02124514d5c4db. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1799 | crypto|supertrend(atr_n=7,mult=2)+relvol(min_ratio=1.2) | -4.64/-0.07/-17.98 | 434.62 | 357 | 0.02 | 0.92108 (83.93) | 1.0 | 0.3768 | 0.914 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1800 | crypto|supertrend(atr_n=7,mult=4)+relvol(min_ratio=1.2) | -5.67/-0.1/-19.45 | 434.62 | 397 | 0.0192 | 0.92108 (205.32) | 1.0 | 0.3628 | 0.9115 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1801 | crypto|supertrend(atr_n=10,mult=2)+relvol(min_ratio=1.2) | -6.09/-0.13/-17.98 | 434.62 | 368 | 0.02 | 0.94206 (107.41) | 1.0 | 0.3512 | 0.915 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1802 | crypto|supertrend(atr_n=10,mult=4)+relvol(min_ratio=1.2) | -8.19/-0.2/-21.64 | 434.62 | 393 | 0.0194 | 0.94206 (166.64) | 1.0 | 0.3192 | 0.913 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
