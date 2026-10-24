# gen_2410240513_000 — engine run 20261024_051230_gen_2410240513_000

Hypothesis: grammar draw seed=2410240513: drop_revert+trend_sma

**0/8 pass.** Ledger N at evaluation: 1814. PBO (CSCV) across family: 0.233. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 011bf831cc2857ac90c4ac7485f82b2350732472d877f50dd26ca9276af458dd. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1807 | BROAD|drop_revert(drop=0.05,hold=3,n=1)+trend_sma(n=100) | 0.0/0.0/0.0 | 23.43 | 2 | 0.0297 | 1.0 (11.06) | 1.0 | 0.0 | 0.956 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1808 | BROAD|drop_revert(drop=0.05,hold=3,n=5)+trend_sma(n=100) | 0.0/0.0/0.0 | 23.43 | 2 | 0.041 | 1.0 (11.4) | 1.0 | 0.0 | 0.956 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1809 | BROAD|drop_revert(drop=0.05,hold=10,n=1)+trend_sma(n=100) | 0.0/0.0/0.0 | 23.43 | 1 | 0.038 | 1.0 (11.4) | 1.0 | 0.0 | 0.956 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1810 | BROAD|drop_revert(drop=0.05,hold=10,n=5)+trend_sma(n=100) | 0.13/0.44/-0.04 | 23.43 | 3 | 0.0621 | 0.99001 (11.34) | 1.0 | nan | 0.956 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1811 | BROAD|drop_revert(drop=0.15,hold=3,n=1)+trend_sma(n=100) | 0.0/0.0/0.0 | 23.43 | 0 | inf | 1.0 (11.49) | 1.0 | 0.0 | 0.956 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1812 | BROAD|drop_revert(drop=0.15,hold=3,n=5)+trend_sma(n=100) | 0.0/0.0/0.0 | 23.43 | 0 | inf | 1.0 (11.4) | 1.0 | 0.0 | 0.956 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1813 | BROAD|drop_revert(drop=0.15,hold=10,n=1)+trend_sma(n=100) | 0.0/0.0/0.0 | 23.43 | 0 | inf | 1.0 (11.4) | 1.0 | 0.0 | 0.956 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1814 | BROAD|drop_revert(drop=0.15,hold=10,n=5)+trend_sma(n=100) | 0.0/0.0/0.0 | 23.43 | 0 | inf | 1.0 (11.16) | 1.0 | 0.0 | 0.956 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
