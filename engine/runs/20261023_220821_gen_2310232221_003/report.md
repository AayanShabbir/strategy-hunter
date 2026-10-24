# gen_2310232221_003 — engine run 20261023_220821_gen_2310232221_003

Hypothesis: grammar draw seed=2310232221: drop_revert

**0/8 pass.** Ledger N at evaluation: 1078. PBO (CSCV) across family: 0.505. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 7055433a713dd02e70020957fe04491d8b8ded56753ce21327c8b125ea817439. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1071 | megacap|drop_revert(drop=0.05,hold=3,n=1) | 3.14/0.59/-1.52 | 26.77 | 34 | 0.0455 | 0.91409 (13.07) | 1.0 | 0.5154 | 0.8625 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1072 | megacap|drop_revert(drop=0.05,hold=3,n=3) | 2.21/0.38/-2.43 | 26.77 | 123 | 0.0556 | 0.87912 (12.57) | 1.0 | 0.3939 | 0.886 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1073 | megacap|drop_revert(drop=0.05,hold=5,n=1) | 2.1/0.38/-2.86 | 26.77 | 34 | 0.0455 | 0.93007 (12.77) | 1.0 | 0.3921 | 0.876 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1074 | megacap|drop_revert(drop=0.05,hold=5,n=3) | 4.24/0.85/-1.6 | 26.77 | 121 | 0.0558 | 0.82717 (13.07) | 1.0 | 0.6601 | 0.864 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1075 | megacap|drop_revert(drop=0.1,hold=3,n=1) | 0.87/0.42/-0.92 | 26.77 | 9 | 0.0287 | 0.94006 (13.35) | 1.0 | 0.4248 | 0.896 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1076 | megacap|drop_revert(drop=0.1,hold=3,n=3) | 1.67/0.65/-1.25 | 26.77 | 14 | 0.0274 | 0.94106 (13.14) | 1.0 | 0.5426 | 0.8895 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1077 | megacap|drop_revert(drop=0.1,hold=5,n=1) | 0.93/0.37/-1.25 | 26.77 | 9 | 0.0287 | 0.93706 (13.07) | 1.0 | 0.4044 | 0.898 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1078 | megacap|drop_revert(drop=0.1,hold=5,n=3) | 1.56/0.64/-1.11 | 26.77 | 14 | 0.0274 | 0.92507 (13.04) | 1.0 | 0.5368 | 0.889 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
