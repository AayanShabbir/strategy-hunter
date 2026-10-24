# gen_2410240410_000 — engine run 20261024_040953_gen_2410240410_000

Hypothesis: grammar draw seed=2410240410: rsi_revert+vol_regime

**0/8 pass.** Ledger N at evaluation: 1718. PBO (CSCV) across family: 0.719. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 ba25faf73843b1d9b536e15f9b3df37b6c6ba83548e9fc5861d731be0cd233a8. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1711 | COUNTRIES|rsi_revert(entry=5,exit=70,n=2)+vol_regime(max_atr_pct=0.06) | 5.31/0.32/-8.62 | 64.42 | 377 | 0.0675 | 0.99401 (27.53) | 1.0 | 0.2926 | 0.498 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1712 | COUNTRIES|rsi_revert(entry=5,exit=70,n=3)+vol_regime(max_atr_pct=0.06) | 7.84/0.66/-4.32 | 64.42 | 96 | 0.0634 | 0.98601 (28.87) | 1.0 | 0.5305 | 0.5045 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 1713 | COUNTRIES|rsi_revert(entry=5,exit=80,n=2)+vol_regime(max_atr_pct=0.06) | 12.13/0.59/-8.62 | 64.42 | 347 | 0.0682 | 0.95604 (27.35) | 1.0 | 0.4798 | 0.4995 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1714 | COUNTRIES|rsi_revert(entry=5,exit=80,n=3)+vol_regime(max_atr_pct=0.06) | 8.1/0.61/-4.51 | 64.42 | 95 | 0.063 | 0.98202 (29.12) | 1.0 | 0.488 | 0.5025 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 1715 | COUNTRIES|rsi_revert(entry=10,exit=70,n=2)+vol_regime(max_atr_pct=0.06) | 10.62/0.48/-10.49 | 64.42 | 648 | 0.0665 | 0.94406 (24.87) | 1.0 | 0.3983 | 0.4965 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1716 | COUNTRIES|rsi_revert(entry=10,exit=70,n=3)+vol_regime(max_atr_pct=0.06) | 17.27/0.86/-8.62 | 64.42 | 243 | 0.0657 | 0.88112 (27.5) | 1.0 | 0.6745 | 0.971 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1717 | COUNTRIES|rsi_revert(entry=10,exit=80,n=2)+vol_regime(max_atr_pct=0.06) | 19.46/0.74/-11.09 | 64.42 | 574 | 0.0666 | 0.73127 (25.41) | 1.0 | 0.5798 | 0.503 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1718 | COUNTRIES|rsi_revert(entry=10,exit=80,n=3)+vol_regime(max_atr_pct=0.06) | 19.12/0.85/-8.62 | 64.42 | 222 | 0.067 | 0.80519 (27.31) | 1.0 | 0.6607 | 0.9725 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
