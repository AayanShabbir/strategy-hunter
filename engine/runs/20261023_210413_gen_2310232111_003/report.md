# gen_2310232111_003 — engine run 20261023_210413_gen_2310232111_003

Hypothesis: grammar draw seed=2310232111: rsi_revert+trend_sma

**0/8 pass.** Ledger N at evaluation: 934. PBO (CSCV) across family: 0.143. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 835b70209494eed2047b37b65798f210fff615f972589035578b8c20e97677cd. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 927 | sectors|rsi_revert(entry=5,exit=70,n=2)+trend_sma(n=50) | 2.18/0.59/-1.08 | 50.2 | 244 | 0.0779 | 1.0 (22.47) | 1.0 | 0.0512 | 0.4945 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 928 | sectors|rsi_revert(entry=5,exit=70,n=5)+trend_sma(n=50) | -0.13/-0.47/-0.2 | 50.2 | 2 | 0.0576 | 1.0 (22.96) | 1.0 | 0.0 | 0.496 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 929 | sectors|rsi_revert(entry=5,exit=80,n=2)+trend_sma(n=50) | 1.66/0.4/-1.27 | 50.2 | 293 | 0.0765 | 1.0 (22.37) | 1.0 | 0.0275 | 0.4995 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 930 | sectors|rsi_revert(entry=5,exit=80,n=5)+trend_sma(n=50) | 0.65/0.81/-0.25 | 50.2 | 22 | 0.0457 | 0.999 (22.99) | 1.0 | 0.0707 | 0.498 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 931 | sectors|rsi_revert(entry=10,exit=70,n=2)+trend_sma(n=50) | 5.35/0.83/-1.92 | 50.2 | 556 | 0.0783 | 0.997 (21.09) | 1.0 | 0.1138 | 0.5025 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 932 | sectors|rsi_revert(entry=10,exit=70,n=5)+trend_sma(n=50) | 0.0/0.01/-0.2 | 50.2 | 28 | 0.0587 | 0.999 (22.91) | 1.0 | 0.0054 | 0.4975 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 933 | sectors|rsi_revert(entry=10,exit=80,n=2)+trend_sma(n=50) | 3.53/0.49/-2.28 | 50.2 | 621 | 0.0775 | 1.0 (20.23) | 1.0 | 0.0385 | 0.4985 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 934 | sectors|rsi_revert(entry=10,exit=80,n=5)+trend_sma(n=50) | 1.96/0.85/-0.9 | 50.2 | 121 | 0.0603 | 1.0 (22.92) | 1.0 | 0.0958 | 0.501 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
