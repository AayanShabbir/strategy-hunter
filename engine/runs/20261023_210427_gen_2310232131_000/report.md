# gen_2310232131_000 — engine run 20261023_210427_gen_2310232131_000

Hypothesis: grammar draw seed=2310232131: supertrend

**0/4 pass.** Ledger N at evaluation: 958. PBO (CSCV) across family: 0.494. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 4725db6e23005450ab9d3a6506f4a4a80151ff4c6bcf34ea1a3d2cd3407206d0. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 955 | crypto|supertrend(atr_n=7,mult=3) | -5.1/0.08/-43.8 | 428.6 | 1335 | 0.0991 | 0.86513 (66.17) | 1.0 | 0.3164 | 0.923 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 956 | crypto|supertrend(atr_n=7,mult=4) | 3.91/0.25/-42.89 | 428.6 | 886 | 0.0999 | 0.82418 (68.84) | 1.0 | 0.3922 | 0.9215 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 957 | crypto|supertrend(atr_n=14,mult=3) | 0.35/0.19/-41.76 | 428.6 | 1347 | 0.0966 | 0.8042 (96.41) | 1.0 | 0.3642 | 0.92 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 958 | crypto|supertrend(atr_n=14,mult=4) | -13.24/-0.08/-47.58 | 428.6 | 874 | 0.0969 | 0.94106 (131.92) | 1.0 | 0.2495 | 0.9245 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
