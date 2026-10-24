# gen_2310232321_001 — engine run 20261023_230814_gen_2310232321_001

Hypothesis: grammar draw seed=2310232321: drop_revert

**0/8 pass.** Ledger N at evaluation: 1186. PBO (CSCV) across family: 0.6. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 be0afb40d5700622e2c5589be3199925e0a3cfd281ed82c88faf6b121749439d. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1179 | megacap|drop_revert(drop=0.1,hold=3,n=1) | 0.74/0.2/-1.83 | 51.37 | 4 | 0.007 | 0.97702 (23.41) | 1.0 | 0.077 | 0.9645 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1180 | megacap|drop_revert(drop=0.1,hold=3,n=3) | 0.69/0.17/-2.5 | 51.37 | 5 | 0.0082 | 0.96603 (22.9) | 1.0 | 0.0789 | 0.965 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1181 | megacap|drop_revert(drop=0.1,hold=10,n=1) | 1.51/0.36/-1.91 | 51.37 | 4 | 0.007 | 0.95604 (22.96) | 1.0 | 0.098 | 0.9595 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1182 | megacap|drop_revert(drop=0.1,hold=10,n=3) | 2.08/0.46/-1.8 | 51.37 | 5 | 0.0082 | 0.97003 (22.59) | 1.0 | 0.1232 | 0.9575 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1183 | megacap|drop_revert(drop=0.15,hold=3,n=1) | 0.0/0.0/0.0 | 51.37 | 2 | 0.004 | 1.0 (34.92) | 1.0 | 0.0 | 0.9715 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1184 | megacap|drop_revert(drop=0.15,hold=3,n=3) | 0.63/0.81/0.0 | 51.37 | 3 | 0.0041 | 0.93107 (22.2) | 1.0 | 0.1101 | 0.9705 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1185 | megacap|drop_revert(drop=0.15,hold=10,n=1) | 0.0/0.0/0.0 | 51.37 | 2 | 0.004 | 1.0 (34.92) | 1.0 | 0.0 | 0.9715 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1186 | megacap|drop_revert(drop=0.15,hold=10,n=3) | -0.4/-0.39/-0.76 | 51.37 | 3 | 0.0041 | 1.0 (23.22) | 1.0 | 0.0071 | 0.971 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
