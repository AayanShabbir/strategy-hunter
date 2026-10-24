# gen_2310232121_001 — engine run 20261023_210420_gen_2310232121_001

Hypothesis: grammar draw seed=2310232121: rsi_revert+rsi_band

**0/8 pass.** Ledger N at evaluation: 946. PBO (CSCV) across family: 0.005. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 52ebbac2de93318628b115d188594d0db152937ad83de0e7f6ed14581ca88477. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 939 | megacap|rsi_revert(entry=5,exit=60,n=2)+rsi_band(hi=60) | -11.51/-0.92/-15.12 | 26.77 | 2320 | 0.1195 | 0.81918 (0.34) | 1.0 | 0.0 | 0.481 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 940 | megacap|rsi_revert(entry=5,exit=60,n=5)+rsi_band(hi=60) | 3.75/1.16/-1.52 | 26.77 | 68 | 0.095 | 0.87712 (13.17) | 1.0 | 0.005 | 0.8695 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 941 | megacap|rsi_revert(entry=5,exit=70,n=2)+rsi_band(hi=60) | -10.14/-0.69/-13.77 | 26.77 | 2193 | 0.1198 | 0.82817 (1.01) | 1.0 | 0.0 | 0.4925 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 942 | megacap|rsi_revert(entry=5,exit=70,n=5)+rsi_band(hi=60) | 5.57/1.36/-1.21 | 26.77 | 67 | 0.0958 | 0.86414 (12.5) | 1.0 | 0.0058 | 0.863 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 943 | megacap|rsi_revert(entry=20,exit=60,n=2)+rsi_band(hi=60) | -18.68/-0.98/-24.61 | 26.77 | 4315 | 0.1213 | 0.42258 (-8.95) | 1.0 | 0.0 | 0.4865 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 944 | megacap|rsi_revert(entry=20,exit=60,n=5)+rsi_band(hi=60) | 8.06/0.53/-10.16 | 26.77 | 1034 | 0.1194 | 0.42857 (7.53) | 1.0 | 0.0004 | 0.855 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 945 | megacap|rsi_revert(entry=20,exit=70,n=2)+rsi_band(hi=60) | -14.19/-0.64/-24.48 | 26.77 | 3912 | 0.1215 | 0.54046 (-6.88) | 1.0 | 0.0 | 0.506 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 946 | megacap|rsi_revert(entry=20,exit=70,n=5)+rsi_band(hi=60) | 14.84/0.72/-11.79 | 26.77 | 904 | 0.1193 | 0.51948 (8.17) | 1.0 | 0.001 | 0.8355 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
