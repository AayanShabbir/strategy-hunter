# gen_2410240527_000 — engine run 20261024_051307_gen_2410240527_000

Hypothesis: grammar draw seed=2410240527: supertrend

**0/4 pass.** Ledger N at evaluation: 1890. PBO (CSCV) across family: 0.712. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 f131ddb7b479f61d8147320ed0739100a6020ac1af0392669998a5be1e344e10. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1887 | crypto|supertrend(atr_n=7,mult=2) | 1.98/0.22/-36.38 | 434.62 | 105 | 0.0188 | 0.92607 (184.25) | 1.0 | 0.379 | 0.9205 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1888 | crypto|supertrend(atr_n=7,mult=3) | 14.1/0.44/-22.62 | 434.62 | 57 | 0.0198 | 0.83816 (108.71) | 1.0 | 0.4834 | 0.9125 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1889 | crypto|supertrend(atr_n=14,mult=2) | 8.75/0.34/-27.63 | 434.62 | 104 | 0.0185 | 0.87113 (98.31) | 1.0 | 0.4358 | 0.915 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1890 | crypto|supertrend(atr_n=14,mult=3) | -2.86/0.12/-29.83 | 434.62 | 59 | 0.0195 | 0.92907 (77.38) | 1.0 | 0.337 | 0.922 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
