# gen_2410240215_000 — engine run 20261024_020833_gen_2410240215_000

Hypothesis: grammar draw seed=2410240215: sma_cross

**0/4 pass.** Ledger N at evaluation: 1590. PBO (CSCV) across family: 0.833. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 2ff544d11c85728ebc3027189468e7f584f93ee993ab1244ad55900a931ee3c3. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1587 | crypto_d|sma_cross(fast=5,slow=50) | 11.81/0.39/-28.07 | 268.18 | 93 | 0.0177 | 0.80519 (102.73) | 1.0 | 0.3342 | 0.8845 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1588 | crypto_d|sma_cross(fast=5,slow=200) | -1.73/0.15/-25.63 | 268.18 | 31 | 0.0191 | 0.89311 (127.13) | 1.0 | 0.2357 | 0.9055 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1589 | crypto_d|sma_cross(fast=10,slow=50) | 22.99/0.56/-28.64 | 268.18 | 77 | 0.0175 | 0.70929 (92.52) | 1.0 | 0.4101 | 0.8595 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 1590 | crypto_d|sma_cross(fast=10,slow=200) | -5.13/0.08/-28.47 | 268.18 | 25 | 0.0197 | 0.91508 (106.21) | 1.0 | 0.2115 | 0.9095 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
