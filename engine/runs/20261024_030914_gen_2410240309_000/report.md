# gen_2410240309_000 — engine run 20261024_030914_gen_2410240309_000

Hypothesis: grammar draw seed=2410240309: drop_revert

**0/8 pass.** Ledger N at evaluation: 1614. PBO (CSCV) across family: 0.276. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 4ebaf45ae1f6a618bcef8748c6a26e5c64fd5841f887680ab046effcc4c38e28. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1607 | sectors|drop_revert(drop=0.05,hold=3,n=3) | 8.85/0.47/-4.13 | 57.67 | 157 | 0.0389 | 0.96204 (25.63) | 1.0 | 0.3625 | 0.5005 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1608 | sectors|drop_revert(drop=0.05,hold=3,n=5) | 5.79/0.3/-6.67 | 57.67 | 196 | 0.0419 | 0.99001 (24.97) | 1.0 | 0.2632 | 0.498 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1609 | sectors|drop_revert(drop=0.05,hold=10,n=3) | 20.92/0.86/-5.39 | 57.67 | 116 | 0.042 | 0.68232 (26.08) | 1.0 | 0.6678 | 0.9275 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1610 | sectors|drop_revert(drop=0.05,hold=10,n=5) | 18.09/0.71/-6.08 | 57.67 | 143 | 0.0446 | 0.78621 (25.99) | 1.0 | 0.5515 | 0.9655 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1611 | sectors|drop_revert(drop=0.1,hold=3,n=3) | 4.61/0.31/-3.58 | 57.67 | 19 | 0.0257 | 0.99201 (25.98) | 1.0 | 0.253 | 0.495 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1612 | sectors|drop_revert(drop=0.1,hold=3,n=5) | 7.62/0.49/-3.58 | 57.67 | 30 | 0.0289 | 0.96803 (26.99) | 1.0 | 0.3664 | 0.9795 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1613 | sectors|drop_revert(drop=0.1,hold=10,n=3) | 7.38/0.44/-4.5 | 57.67 | 17 | 0.0269 | 0.97203 (26.26) | 1.0 | 0.3409 | 0.493 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1614 | sectors|drop_revert(drop=0.1,hold=10,n=5) | 7.92/0.48/-4.5 | 57.67 | 24 | 0.0317 | 0.97403 (26.32) | 1.0 | 0.3641 | 0.9805 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
