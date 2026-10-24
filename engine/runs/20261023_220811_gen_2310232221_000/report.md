# gen_2310232221_000 — engine run 20261023_220811_gen_2310232221_000

Hypothesis: grammar draw seed=2310232221: drop_revert

**0/8 pass.** Ledger N at evaluation: 1058. PBO (CSCV) across family: 0.776. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 fcbc286a5585109db6e77ee3e42edfc76e5c5fd859c31768b6ea013965d47b04. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1051 | megacap|drop_revert(drop=0.05,hold=3,n=1) | 3.14/0.59/-1.52 | 26.77 | 34 | 0.0455 | 0.92408 (12.9) | 1.0 | 0.2905 | 0.8625 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1052 | megacap|drop_revert(drop=0.05,hold=3,n=3) | 2.21/0.38/-2.43 | 26.77 | 123 | 0.0556 | 0.89411 (12.46) | 1.0 | 0.2278 | 0.886 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1053 | megacap|drop_revert(drop=0.05,hold=10,n=1) | 2.14/0.38/-3.23 | 26.77 | 34 | 0.0455 | 0.92707 (12.67) | 1.0 | 0.2318 | 0.8755 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1054 | megacap|drop_revert(drop=0.05,hold=10,n=3) | 5.05/0.73/-3.31 | 26.77 | 116 | 0.0558 | 0.6024 (12.75) | 1.0 | 0.4146 | 0.8465 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1055 | megacap|drop_revert(drop=0.15,hold=3,n=1) | 0.0/0.0/0.0 | 26.77 | 4 | 0.0072 | 0.93307 (13.28) | 1.0 | 0.0 | 0.907 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1056 | megacap|drop_revert(drop=0.15,hold=3,n=3) | 0.79/1.12/0.0 | 26.77 | 9 | 0.0083 | 0.9031 (13.21) | 1.0 | 0.7144 | 0.901 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1057 | megacap|drop_revert(drop=0.15,hold=10,n=1) | 0.0/0.0/0.0 | 26.77 | 4 | 0.0072 | 0.94006 (13.17) | 1.0 | 0.0 | 0.907 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1058 | megacap|drop_revert(drop=0.15,hold=10,n=3) | 0.83/0.65/-0.38 | 26.77 | 9 | 0.0083 | 0.8981 (13.08) | 1.0 | 0.3424 | 0.9035 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
