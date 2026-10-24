# gen_2310232231_002 — engine run 20261023_220836_gen_2310232231_002

Hypothesis: grammar draw seed=2310232231: drop_revert

**0/8 pass.** Ledger N at evaluation: 1098. PBO (CSCV) across family: 0.277. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 123ab1e939d2718bb37a80cbab12eaaf28ffc2ee2aba31be60f1f7bb3559c0dc. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1091 | crypto|drop_revert(drop=0.05,hold=3,n=3) | 6.45/0.7/-3.45 | 428.6 | 527 | 0.0357 | 0.8991 (216.88) | 1.0 | 0.1586 | 0.903 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1092 | crypto|drop_revert(drop=0.05,hold=3,n=5) | 0.61/0.09/-10.68 | 428.6 | 707 | 0.0427 | 0.89211 (196.03) | 1.0 | 0.0395 | 0.9085 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1093 | crypto|drop_revert(drop=0.05,hold=10,n=3) | -4.05/-0.18/-10.63 | 428.6 | 412 | 0.0403 | 0.92507 (160.81) | 1.0 | 0.0173 | 0.9105 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1094 | crypto|drop_revert(drop=0.05,hold=10,n=5) | -6.89/-0.2/-17.22 | 428.6 | 577 | 0.0473 | 0.95405 (85.8) | 1.0 | 0.0162 | 0.9125 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1095 | crypto|drop_revert(drop=0.1,hold=3,n=3) | 0.46/0.34/-0.71 | 428.6 | 47 | 0.0154 | 0.95804 (233.98) | 1.0 | 0.0556 | 0.909 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1096 | crypto|drop_revert(drop=0.1,hold=3,n=5) | 3.36/0.89/-1.65 | 428.6 | 93 | 0.0216 | 0.88811 (84.31) | 1.0 | 0.2016 | 0.906 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1097 | crypto|drop_revert(drop=0.1,hold=10,n=3) | -1.13/-0.36/-1.92 | 428.6 | 39 | 0.0163 | 0.96104 (196.94) | 1.0 | 0.012 | 0.9095 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1098 | crypto|drop_revert(drop=0.1,hold=10,n=5) | 4.28/0.67/-3.04 | 428.6 | 76 | 0.0239 | 0.87812 (237.81) | 1.0 | 0.1306 | 0.9045 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
