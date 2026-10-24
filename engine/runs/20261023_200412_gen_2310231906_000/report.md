# gen_2310231906_000 — engine run 20261023_200412_gen_2310231906_000

Hypothesis: grammar draw seed=2310231906: donchian

**0/4 pass.** Ledger N at evaluation: 718. PBO (CSCV) across family: 0.488. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 d70cbd3f3d7a964ebdf0ae1591ede87a83b7d61f6396595acda964887933a2aa. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 715 | hibeta|donchian(entry_n=20,exit_n=10) | 265.0/1.59/-20.74 | 809.88 | 179 | 0.0255 | 0.26873 (216.09) | 1.0 | 0.9478 | 0.511 | False | beats_buy_hold, holm, dsr, spa |
| 716 | hibeta|donchian(entry_n=20,exit_n=20) | 260.77/1.44/-31.36 | 809.88 | 129 | 0.0228 | 0.27273 (219.03) | 1.0 | 0.9075 | 0.5205 | False | beats_buy_hold, holm, dsr, spa |
| 717 | hibeta|donchian(entry_n=100,exit_n=10) | 145.61/1.59/-11.11 | 809.88 | 86 | 0.029 | 0.80819 (223.92) | 1.0 | 0.9492 | 0.51 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 718 | hibeta|donchian(entry_n=100,exit_n=20) | 96.24/1.13/-18.86 | 809.88 | 67 | 0.0278 | 0.95604 (223.61) | 1.0 | 0.7819 | 0.519 | False | beats_buy_hold, min_trades, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
