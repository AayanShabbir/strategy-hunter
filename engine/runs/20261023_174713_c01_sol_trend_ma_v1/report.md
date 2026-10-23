# c01_sol_trend_ma_v1 — engine run 20261023_174713_c01_sol_trend_ma_v1

Hypothesis: Long/flat spot SOL (and an alt basket incl. SOL) while fast SMA > slow SMA on UTC daily bars beats buy-and-hold OOS after Alpaca tier-1 taker fee 25 bps + 10 bps slippage per side, because crypto shows time-series momentum and technical trend rules cut its deep drawdowns (Liu & Tsyvinski 2021 RFS; Hudson & Urquhart 2021). Wide 5x ATR stop. Strategy Scout crypto submission.

**0/8 pass.** Ledger N at evaluation: 466. PBO (CSCV) across family: 0.271. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 c206eaae0dfdda78e1d586ee056a3d12e2f252c862d72aa1d16264d63920b6a4. Costs {'fee_bps': 25, 'slippage_bps': 10}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 459 | SOL|sma_cross(fast=1,slow=50) | 26.19/0.47/-34.46 | 923.45 | 34 | 0.0164 | 0.63636 (123.59) | 1.0 | 0.0689 | 0.8805 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 460 | SOL|sma_cross(fast=1,slow=100) | -47.8/-0.59/-54.45 | 923.45 | 35 | 0.0171 | 0.98601 (98.82) | 1.0 | 0.0016 | 0.9235 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 461 | SOL|sma_cross(fast=10,slow=50) | 29.55/0.5/-41.34 | 923.45 | 13 | 0.0199 | 0.69231 (248.32) | 1.0 | 0.0773 | 0.8685 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 462 | SOL|sma_cross(fast=10,slow=100) | -51.41/-0.68/-62.14 | 923.45 | 13 | 0.019 | 0.98901 (266.75) | 1.0 | 0.0009 | 0.9205 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 463 | ALTS|sma_cross(fast=1,slow=50) | 2.71/0.23/-39.86 | 193.2 | 320 | 0.0199 | 0.78222 (59.97) | 1.0 | 0.0352 | 0.9085 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 464 | ALTS|sma_cross(fast=1,slow=100) | 9.48/0.31/-39.82 | 193.2 | 241 | 0.0208 | 0.73826 (54.83) | 1.0 | 0.0471 | 0.891 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 465 | ALTS|sma_cross(fast=10,slow=50) | 30.79/0.52/-33.03 | 193.2 | 128 | 0.0214 | 0.66733 (74.29) | 1.0 | 0.0837 | 0.866 | False | beats_buy_hold, holm, dsr, spa |
| 466 | ALTS|sma_cross(fast=10,slow=100) | 13.73/0.36/-44.98 | 193.2 | 89 | 0.0219 | 0.77822 (90.12) | 1.0 | 0.0541 | 0.887 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
