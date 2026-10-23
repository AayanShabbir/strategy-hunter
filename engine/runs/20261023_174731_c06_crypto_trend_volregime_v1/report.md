# c06_crypto_trend_volregime_v1 — engine run 20261023_174731_c06_crypto_trend_volregime_v1

Hypothesis: Supertrend(10, 3 or 4) long/flat, allowed only when ATR14/price is below 5% or 8% (volatility-regime gate as a long/flat proxy for volatility-managed momentum, Barroso & Santa-Clara 2015; crypto risk-managed momentum, FMPM 2025) beats buy-and-hold OOS on SOL, alts, and BTC+ETH net of 35 bps/side. 5x ATR stop. Strategy Scout crypto submission.

**0/12 pass.** Ledger N at evaluation: 511. PBO (CSCV) across family: 0.762. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 6a9680145e3e80c0fea0d1c0ecc97cc6d63dffcfa955064e4ecafb4069e4dfad. Costs {'fee_bps': 25, 'slippage_bps': 10}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 500 | SOL|supertrend(atr_n=10,mult=3)+vol_regime(max_atr_pct=0.05,n=14) | 33.29/0.98/-11.19 | 923.45 | 3 | 0.0284 | 0.56643 (50.48) | 1.0 | 0.2324 | 0.869 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 501 | SOL|supertrend(atr_n=10,mult=3)+vol_regime(max_atr_pct=0.08,n=14) | 78.15/1.01/-29.54 | 923.45 | 22 | 0.0182 | 0.58042 (301.2) | 1.0 | 0.2542 | 0.8275 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 502 | SOL|supertrend(atr_n=10,mult=4)+vol_regime(max_atr_pct=0.05,n=14) | 23.52/0.77/-11.19 | 923.45 | 3 | 0.0286 | 0.61838 (56.47) | 1.0 | 0.1459 | 0.879 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 503 | SOL|supertrend(atr_n=10,mult=4)+vol_regime(max_atr_pct=0.08,n=14) | 67.61/0.84/-42.1 | 923.45 | 24 | 0.0181 | 0.58641 (298.0) | 1.0 | 0.1789 | 0.8275 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 504 | ALTS|supertrend(atr_n=10,mult=3)+vol_regime(max_atr_pct=0.05,n=14) | -5.27/-0.25/-12.37 | 193.2 | 70 | 0.0289 | 0.98501 (66.15) | 1.0 | 0.007 | 0.9015 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 505 | ALTS|supertrend(atr_n=10,mult=3)+vol_regime(max_atr_pct=0.08,n=14) | 15.74/0.38/-29.19 | 193.2 | 182 | 0.0186 | 0.73127 (85.39) | 1.0 | 0.0598 | 0.8815 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 506 | ALTS|supertrend(atr_n=10,mult=4)+vol_regime(max_atr_pct=0.05,n=14) | -2.39/-0.11/-10.41 | 193.2 | 67 | 0.0286 | 0.97303 (110.85) | 1.0 | 0.0117 | 0.9045 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 507 | ALTS|supertrend(atr_n=10,mult=4)+vol_regime(max_atr_pct=0.08,n=14) | 8.43/0.28/-32.23 | 193.2 | 179 | 0.0182 | 0.79121 (80.11) | 1.0 | 0.0466 | 0.894 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 508 | BTC_ETH|supertrend(atr_n=10,mult=3)+vol_regime(max_atr_pct=0.05,n=14) | -16.54/-0.23/-31.68 | 56.21 | 71 | 0.0288 | 0.8991 (16.7) | 1.0 | 0.0083 | 0.4895 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 509 | BTC_ETH|supertrend(atr_n=10,mult=3)+vol_regime(max_atr_pct=0.08,n=14) | -5.2/0.05/-31.89 | 56.21 | 49 | 0.0305 | 0.8042 (21.73) | 1.0 | 0.022 | 0.9685 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 510 | BTC_ETH|supertrend(atr_n=10,mult=4)+vol_regime(max_atr_pct=0.05,n=14) | -9.87/-0.12/-26.77 | 56.21 | 68 | 0.0287 | 0.85714 (21.92) | 1.0 | 0.012 | 0.957 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 511 | BTC_ETH|supertrend(atr_n=10,mult=4)+vol_regime(max_atr_pct=0.08,n=14) | 5.99/0.24/-26.34 | 56.21 | 42 | 0.0276 | 0.66234 (24.41) | 1.0 | 0.0403 | 0.923 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
