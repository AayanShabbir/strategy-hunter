# gen_2310232015_000 — engine run 20261023_201105_gen_2310232015_000

Hypothesis: grammar draw seed=2310232015: drop_revert+rsi_band

**0/8 pass.** Ledger N at evaluation: 842. PBO (CSCV) across family: 0.271. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 5275e1e2e2ce93508163d1d955dc9ff42b53b97384a60820c750f9088bb579a8. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 835 | crypto|drop_revert(drop=0.05,hold=3,n=1)+rsi_band(hi=60) | -2.29/-0.47/-4.38 | 428.6 | 184 | 0.025 | 0.91808 (79.52) | 1.0 | 0.0279 | 0.9095 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 836 | crypto|drop_revert(drop=0.05,hold=3,n=5)+rsi_band(hi=60) | 2.16/0.2/-9.31 | 428.6 | 711 | 0.0426 | 0.89011 (167.66) | 1.0 | 0.1816 | 0.907 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 837 | crypto|drop_revert(drop=0.05,hold=5,n=1)+rsi_band(hi=60) | -1.98/-0.28/-4.02 | 428.6 | 179 | 0.0251 | 0.91808 (236.54) | 1.0 | 0.0632 | 0.909 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 838 | crypto|drop_revert(drop=0.05,hold=5,n=5)+rsi_band(hi=60) | 2.08/0.17/-13.08 | 428.6 | 690 | 0.043 | 0.89311 (185.76) | 1.0 | 0.1769 | 0.9055 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 839 | crypto|drop_revert(drop=0.15,hold=3,n=1)+rsi_band(hi=60) | 0.0/0.0/0.0 | 428.6 | 4 | 0.0106 | 1.0 (42.03) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 840 | crypto|drop_revert(drop=0.15,hold=3,n=5)+rsi_band(hi=60) | -0.37/-0.45/-0.6 | 428.6 | 21 | 0.0132 | 0.93806 (234.93) | 1.0 | 0.0255 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 841 | crypto|drop_revert(drop=0.15,hold=5,n=1)+rsi_band(hi=60) | 0.0/0.0/0.0 | 428.6 | 4 | 0.0106 | 1.0 (312.99) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 842 | crypto|drop_revert(drop=0.15,hold=5,n=5)+rsi_band(hi=60) | -0.42/-0.26/-1.37 | 428.6 | 22 | 0.0133 | 0.93207 (271.64) | 1.0 | 0.0785 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
