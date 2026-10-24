# gen_2310232131_002 — engine run 20261023_210437_gen_2310232131_002

Hypothesis: grammar draw seed=2310232131: rsi_revert+trend_sma

**0/8 pass.** Ledger N at evaluation: 970. PBO (CSCV) across family: 0.429. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 0a13b104e1c59c86174ef79c0274f486ab2a4ab6eeba5fe19748d967493a22f5. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 963 | crypto|rsi_revert(entry=5,exit=60,n=3)+trend_sma(n=200) | -3.7/-0.67/-4.62 | 428.6 | 289 | 0.1028 | 0.94106 (191.75) | 1.0 | 0.0114 | 0.9115 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 964 | crypto|rsi_revert(entry=5,exit=60,n=5)+trend_sma(n=200) | -2.43/-1.23/-2.68 | 428.6 | 22 | 0.1303 | 0.97702 (231.96) | 1.0 | 0.0 | 0.9105 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 965 | crypto|rsi_revert(entry=5,exit=80,n=3)+trend_sma(n=200) | -4.13/-0.5/-10.18 | 428.6 | 411 | 0.0972 | 0.94805 (200.89) | 1.0 | 0.0256 | 0.9105 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 966 | crypto|rsi_revert(entry=5,exit=80,n=5)+trend_sma(n=200) | -3.25/-1.24/-3.96 | 428.6 | 31 | 0.1157 | 0.96304 (60.82) | 1.0 | 0.0001 | 0.911 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 967 | crypto|rsi_revert(entry=20,exit=60,n=3)+trend_sma(n=200) | -16.1/-0.89/-21.44 | 428.6 | 2405 | 0.1037 | 0.89211 (37.59) | 1.0 | 0.0074 | 0.919 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 968 | crypto|rsi_revert(entry=20,exit=60,n=5)+trend_sma(n=200) | -4.72/-0.32/-11.04 | 428.6 | 937 | 0.1023 | 0.91009 (84.91) | 1.0 | 0.0436 | 0.9105 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 969 | crypto|rsi_revert(entry=20,exit=80,n=3)+trend_sma(n=200) | -18.67/-0.73/-28.88 | 428.6 | 2346 | 0.1037 | 0.92607 (62.07) | 1.0 | 0.0124 | 0.9205 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 970 | crypto|rsi_revert(entry=20,exit=80,n=5)+trend_sma(n=200) | -12.46/-0.56/-21.61 | 428.6 | 1403 | 0.1023 | 0.92607 (122.48) | 1.0 | 0.0229 | 0.918 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
