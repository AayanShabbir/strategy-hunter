# gen_2610241200_000 — engine run 20261024_120721_gen_2610241200_000

Hypothesis: grammar draw seed=2610241200: donchian+relvol

**0/4 pass.** Ledger N at evaluation: 2482. PBO (CSCV) across family: 0.073. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 38a557b2f0938b89ede263bd82080c78ba2ebe3ac687c953a61b9fe07670f9f6. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2479 | crypto|donchian(entry_n=55,exit_n=10)+relvol(min_ratio=1.2) | 1.24/0.13/-14.23 | 434.62 | 204 | 0.0202 | 0.9041 (84.79) | 1.0 | 0.1335 | 0.9075 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 2480 | crypto|donchian(entry_n=55,exit_n=20)+relvol(min_ratio=1.2) | -2.82/-0.05/-16.58 | 434.62 | 265 | 0.0195 | 0.93007 (107.15) | 1.0 | 0.0935 | 0.9075 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 2481 | crypto|donchian(entry_n=100,exit_n=10)+relvol(min_ratio=1.2) | -4.71/-0.29/-12.58 | 434.62 | 144 | 0.021 | 0.94206 (64.72) | 1.0 | 0.0533 | 0.907 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 2482 | crypto|donchian(entry_n=100,exit_n=20)+relvol(min_ratio=1.2) | -9.66/-0.56/-16.49 | 434.62 | 186 | 0.02 | 0.95305 (138.25) | 1.0 | 0.0254 | 0.91 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
