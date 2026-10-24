# gen_2310232016_000 — engine run 20261023_201113_gen_2310232016_000

Hypothesis: grammar draw seed=2310232016: supertrend

**0/4 pass.** Ledger N at evaluation: 846. PBO (CSCV) across family: 0.609. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 592a49880eb9887c1c76683b9a0151a32b9febf1f47d9edcaf82b4fb0b67bada. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 843 | crypto_d|supertrend(atr_n=7,mult=3) | 5.54/0.28/-29.93 | 268.18 | 75 | 0.0184 | 0.84815 (117.51) | 1.0 | 0.45 | 0.8865 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 844 | crypto_d|supertrend(atr_n=7,mult=4) | -1.28/0.18/-27.09 | 268.18 | 53 | 0.0189 | 0.9031 (75.97) | 1.0 | 0.4014 | 0.9045 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 845 | crypto_d|supertrend(atr_n=14,mult=3) | -7.44/0.03/-30.33 | 268.18 | 75 | 0.0183 | 0.93906 (108.86) | 1.0 | 0.3325 | 0.904 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 846 | crypto_d|supertrend(atr_n=14,mult=4) | 5.23/0.28/-24.16 | 268.18 | 47 | 0.0189 | 0.84515 (123.56) | 1.0 | 0.4496 | 0.8945 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
