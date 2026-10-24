# gen_2410240706_000 — engine run 20261024_070504_gen_2410240706_000

Hypothesis: grammar draw seed=2410240706: supertrend+trend_sma

**0/4 pass.** Ledger N at evaluation: 2026. PBO (CSCV) across family: 0.055. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 abeda84459c4df98904f0feb683099608a1e8eb9a9514161f3e33a00ab37d8f4. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2023 | sectors|supertrend(atr_n=10,mult=2)+trend_sma(n=50) | 10.18/0.55/-6.87 | 50.2 | 730 | 0.0665 | 0.95604 (20.21) | 1.0 | 0.6768 | 0.4895 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2024 | sectors|supertrend(atr_n=10,mult=4)+trend_sma(n=50) | 7.64/0.4/-7.82 | 50.2 | 466 | 0.072 | 0.98302 (21.26) | 1.0 | 0.583 | 0.4985 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2025 | sectors|supertrend(atr_n=14,mult=2)+trend_sma(n=50) | 11.25/0.59/-6.86 | 50.2 | 735 | 0.0659 | 0.93207 (19.8) | 1.0 | 0.7028 | 0.495 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2026 | sectors|supertrend(atr_n=14,mult=4)+trend_sma(n=50) | 10.08/0.51/-7.69 | 50.2 | 488 | 0.0694 | 0.97103 (21.02) | 1.0 | 0.6524 | 0.497 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
