# gen_2310232121_002 — engine run 20261023_210424_gen_2310232121_002

Hypothesis: grammar draw seed=2310232121: drop_revert+rsi_band

**0/8 pass.** Ledger N at evaluation: 954. PBO (CSCV) across family: 0.901. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 38d289afa69ee51f5fb2bb7ae63c3bb2f7979935dcc1c30edc65f6023b1388b8. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 947 | megacap|drop_revert(drop=0.05,hold=5,n=1)+rsi_band(hi=80) | 2.1/0.38/-2.86 | 26.77 | 34 | 0.0455 | 0.93407 (12.62) | 1.0 | 0.3289 | 0.876 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 948 | megacap|drop_revert(drop=0.05,hold=5,n=3)+rsi_band(hi=80) | 4.24/0.85/-1.6 | 26.77 | 121 | 0.0558 | 0.81918 (12.59) | 1.0 | 0.5977 | 0.864 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 949 | megacap|drop_revert(drop=0.05,hold=10,n=1)+rsi_band(hi=80) | 2.14/0.38/-3.23 | 26.77 | 34 | 0.0455 | 0.94306 (13.0) | 1.0 | 0.3366 | 0.8755 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 950 | megacap|drop_revert(drop=0.05,hold=10,n=3)+rsi_band(hi=80) | 5.05/0.73/-3.31 | 26.77 | 117 | 0.0558 | 0.5994 (12.48) | 1.0 | 0.5256 | 0.8465 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 951 | megacap|drop_revert(drop=0.15,hold=5,n=1)+rsi_band(hi=80) | 0.0/0.0/0.0 | 26.77 | 4 | 0.0072 | 0.93806 (13.28) | 1.0 | 0.0 | 0.907 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 952 | megacap|drop_revert(drop=0.15,hold=5,n=3)+rsi_band(hi=80) | 0.89/0.83/0.0 | 26.77 | 9 | 0.0083 | 0.89211 (13.07) | 1.0 | 0.6519 | 0.9015 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 953 | megacap|drop_revert(drop=0.15,hold=10,n=1)+rsi_band(hi=80) | 0.0/0.0/0.0 | 26.77 | 4 | 0.0072 | 0.94505 (13.28) | 1.0 | 0.0 | 0.907 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 954 | megacap|drop_revert(drop=0.15,hold=10,n=3)+rsi_band(hi=80) | 0.83/0.65/-0.38 | 26.77 | 9 | 0.0083 | 0.9031 (12.91) | 1.0 | 0.4832 | 0.9035 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
