# gen_2310231905_000 — engine run 20261023_195909_gen_2310231905_000

Hypothesis: grammar draw seed=2310231905: drop_revert

**0/8 pass.** Ledger N at evaluation: 702. PBO (CSCV) across family: 0.188. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 09264db6e4cd76a9e1bc9bc95c2ec1a6780168f366bc7e4d4ca127b46c598838. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 695 | crypto|drop_revert(drop=0.05,hold=3,n=3) | 6.45/0.7/-3.45 | 428.6 | 527 | 0.0357 | 0.88412 (141.06) | 1.0 | 0.1025 | 0.903 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 696 | crypto|drop_revert(drop=0.05,hold=3,n=5) | 0.61/0.09/-10.68 | 428.6 | 707 | 0.0427 | 0.91209 (182.05) | 1.0 | 0.0212 | 0.9085 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 697 | crypto|drop_revert(drop=0.05,hold=5,n=3) | 14.64/1.01/-5.04 | 428.6 | 482 | 0.0373 | 0.82418 (212.45) | 1.0 | 0.1782 | 0.8955 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 698 | crypto|drop_revert(drop=0.05,hold=5,n=5) | -2.22/-0.04/-14.4 | 428.6 | 675 | 0.0434 | 0.91608 (101.4) | 1.0 | 0.0139 | 0.9095 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 699 | crypto|drop_revert(drop=0.15,hold=3,n=3) | 0.0/0.0/0.0 | 428.6 | 10 | 0.0126 | 1.0 (42.03) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 700 | crypto|drop_revert(drop=0.15,hold=3,n=5) | -0.37/-0.45/-0.6 | 428.6 | 21 | 0.0132 | 0.93806 (253.93) | 1.0 | 0.0009 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 701 | crypto|drop_revert(drop=0.15,hold=5,n=3) | 0.0/0.0/0.0 | 428.6 | 10 | 0.0126 | 1.0 (42.03) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 702 | crypto|drop_revert(drop=0.15,hold=5,n=5) | -0.42/-0.26/-1.37 | 428.6 | 21 | 0.0132 | 0.94106 (259.66) | 1.0 | 0.0084 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
