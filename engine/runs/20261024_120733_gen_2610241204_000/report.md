# gen_2610241204_000 — engine run 20261024_120733_gen_2610241204_000

Hypothesis: grammar draw seed=2610241204: donchian

**0/4 pass.** Ledger N at evaluation: 2502. PBO (CSCV) across family: 0.233. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 cf6172334278d9e53422fdaa33e12037a5c6703476aa446fa8d7926cc0db3395. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2499 | BROAD|donchian(entry_n=55,exit_n=10) | 5.09/0.24/-14.67 | 83.36 | 81 | 0.085 | 0.99001 (33.8) | 1.0 | 0.1185 | 0.495 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2500 | BROAD|donchian(entry_n=55,exit_n=20) | 24.13/0.75/-8.35 | 83.36 | 59 | 0.08 | 0.78921 (34.38) | 1.0 | 0.3738 | 0.4825 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 2501 | BROAD|donchian(entry_n=100,exit_n=10) | 4.12/0.22/-15.86 | 83.36 | 62 | 0.0954 | 0.998 (34.86) | 1.0 | 0.1104 | 0.496 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 2502 | BROAD|donchian(entry_n=100,exit_n=20) | 17.66/0.62/-10.35 | 83.36 | 44 | 0.09 | 0.95305 (35.31) | 1.0 | 0.2942 | 0.486 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
