# gen_2310231907_002 — engine run 20261023_200428_gen_2310231907_002

Hypothesis: grammar draw seed=2310231907: supertrend

**0/4 pass.** Ledger N at evaluation: 754. PBO (CSCV) across family: 0.428. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 f42f907f664baa73bb5fcd6faf9fb37427b4a448b2bdb895578b796bd9d32f19. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 751 | crypto_d|supertrend(atr_n=7,mult=2) | -9.09/0.01/-37.93 | 268.18 | 133 | 0.0173 | 0.93307 (83.88) | 1.0 | 0.2559 | 0.913 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 752 | crypto_d|supertrend(atr_n=7,mult=3) | 5.54/0.28/-29.93 | 268.18 | 75 | 0.0184 | 0.85714 (140.33) | 1.0 | 0.3715 | 0.8865 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 753 | crypto_d|supertrend(atr_n=14,mult=2) | 9.38/0.35/-27.1 | 268.18 | 128 | 0.0174 | 0.83916 (136.95) | 1.0 | 0.4024 | 0.8865 | False | beats_buy_hold, holm, dsr, spa |
| 754 | crypto_d|supertrend(atr_n=14,mult=3) | -7.44/0.03/-30.33 | 268.18 | 75 | 0.0183 | 0.93506 (128.89) | 1.0 | 0.2627 | 0.904 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
