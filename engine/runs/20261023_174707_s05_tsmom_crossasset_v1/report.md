# s05_tsmom_crossasset_v1 — engine run 20261023_174707_s05_tsmom_crossasset_v1

Hypothesis: Time-series momentum across asset classes (Moskowitz, Ooi & Pedersen 2012, JFE; Faber 2007): holding non-equity-index ETFs (metals, miners, oil, REITs, Treasuries, intl equity, small caps) only when price > its 6- or 12-month SMA beats buy-and-hold of the same basket OOS after 5 bps/side, because trend persistence in these markets is less arbitraged than in megacap US stocks (which already failed in h16/h17). Long/flat only, wide 4x ATR stop.

**0/4 pass.** Ledger N at evaluation: 454. PBO (CSCV) across family: 0.523. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 9c24c49f796ace9fbd9579640b16afbbfaeb2b3ecc259cc6c43beadf15eea1c1. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 451 | REAL|sma_cross(fast=1,slow=126) | 19.78/0.5/-19.44 | 86.94 | 293 | 0.0129 | 0.86314 (34.8) | 1.0 | 0.3687 | 0.49 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 452 | REAL|sma_cross(fast=1,slow=252) | 25.04/0.6/-14.36 | 86.94 | 216 | 0.0132 | 0.78821 (36.17) | 1.0 | 0.4283 | 0.496 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 453 | BONDS_INTL|sma_cross(fast=1,slow=126) | 2.39/0.14/-12.12 | 40.38 | 250 | 0.0215 | 0.98302 (16.56) | 1.0 | 0.1684 | 0.497 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 454 | BONDS_INTL|sma_cross(fast=1,slow=252) | 2.9/0.17/-11.54 | 40.38 | 195 | 0.0218 | 0.99101 (16.95) | 1.0 | 0.1796 | 0.5045 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
