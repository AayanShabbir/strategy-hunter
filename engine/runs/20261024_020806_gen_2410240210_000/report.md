# gen_2410240210_000 — engine run 20261024_020806_gen_2410240210_000

Hypothesis: grammar draw seed=2410240210: drop_revert

**0/8 pass.** Ledger N at evaluation: 1526. PBO (CSCV) across family: 0.346. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 3b21b211f14869a2f49e2d43e3d7d82ec360dd93055c53e29b1ab72b008f9460. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1519 | sectors|drop_revert(drop=0.05,hold=3,n=1) | 2.85/0.27/-2.54 | 50.2 | 50 | 0.0305 | 0.999 (23.08) | 1.0 | 0.539 | 0.498 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1520 | sectors|drop_revert(drop=0.05,hold=3,n=5) | 5.76/0.36/-5.1 | 50.2 | 284 | 0.0438 | 0.998 (22.38) | 1.0 | 0.6086 | 0.502 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1521 | sectors|drop_revert(drop=0.05,hold=5,n=1) | 4.7/0.34/-3.02 | 50.2 | 45 | 0.0315 | 0.999 (22.96) | 1.0 | 0.5998 | 0.4975 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1522 | sectors|drop_revert(drop=0.05,hold=5,n=5) | 7.65/0.45/-5.73 | 50.2 | 272 | 0.0438 | 0.99201 (22.55) | 1.0 | 0.6786 | 0.505 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1523 | sectors|drop_revert(drop=0.1,hold=3,n=1) | 0.0/0.0/0.0 | 50.2 | 9 | 0.0153 | 1.0 (23.47) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1524 | sectors|drop_revert(drop=0.1,hold=3,n=5) | 5.25/0.43/-2.63 | 50.2 | 45 | 0.0291 | 0.996 (23.12) | 1.0 | 0.6706 | 0.498 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1525 | sectors|drop_revert(drop=0.1,hold=5,n=1) | 0.0/0.0/0.0 | 50.2 | 8 | 0.0163 | 1.0 (23.37) | 1.0 | 0.0 | 0.495 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1526 | sectors|drop_revert(drop=0.1,hold=5,n=5) | 4.44/0.37/-2.63 | 50.2 | 42 | 0.0317 | 0.999 (23.31) | 1.0 | 0.6191 | 0.498 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
