# gen_2310231908_002 — engine run 20261023_200502_gen_2310231908_002

Hypothesis: grammar draw seed=2310231908: drop_revert+relvol

**0/8 pass.** Ledger N at evaluation: 782. PBO (CSCV) across family: 0.393. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 f80a0c0dc4a8d91b5efc1574ad1ff69d9261ab1a11e9beb1c2deca07524bdb34. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 775 | semis|drop_revert(drop=0.05,hold=3,n=1)+relvol(min_ratio=1.0) | 1.55/0.57/-1.51 | -38.66 | 33 | 0.0375 | 0.12887 (-21.41) | 1.0 | 0.0033 | 0.2885 | False | min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 776 | semis|drop_revert(drop=0.05,hold=3,n=3)+relvol(min_ratio=1.0) | -0.51/-0.14/-2.63 | -38.66 | 117 | 0.0458 | 0.13287 (-21.9) | 1.0 | 0.0001 | 0.3005 | False | oos_positive, cost_stop, walk_forward, holm, dsr, spa |
| 777 | semis|drop_revert(drop=0.05,hold=10,n=1)+relvol(min_ratio=1.0) | 3.0/0.89/-1.45 | -38.66 | 83 | 0.0391 | 0.11289 (-20.3) | 1.0 | 0.0043 | 0.2795 | False | min_trades, cost_stop, holm, dsr, spa |
| 778 | semis|drop_revert(drop=0.05,hold=10,n=3)+relvol(min_ratio=1.0) | 2.89/0.61/-3.32 | -38.66 | 259 | 0.0471 | 0.09391 (-22.3) | 1.0 | 0.0061 | 0.2785 | False | cost_stop, holm, dsr, spa |
| 779 | semis|drop_revert(drop=0.15,hold=3,n=1)+relvol(min_ratio=1.0) | 0.6/0.82/0.0 | -38.66 | 1 | 0.0014 | 0.0979 (-20.27) | 1.0 | 0.0014 | 0.2945 | False | min_trades, walk_forward, holm, dsr, spa |
| 780 | semis|drop_revert(drop=0.15,hold=3,n=3)+relvol(min_ratio=1.0) | 0.74/0.82/-0.13 | -38.66 | 6 | 0.0284 | 0.13686 (-20.57) | 1.0 | 0.0029 | 0.294 | False | min_trades, holm, dsr, spa |
| 781 | semis|drop_revert(drop=0.15,hold=10,n=1)+relvol(min_ratio=1.0) | 1.69/1.34/-0.03 | -38.66 | 4 | 0.0046 | 0.16284 (-21.03) | 1.0 | 0.0378 | 0.284 | False | min_trades, holm, dsr, spa |
| 782 | semis|drop_revert(drop=0.15,hold=10,n=3)+relvol(min_ratio=1.0) | 3.1/1.72/-0.19 | -38.66 | 10 | 0.0286 | 0.14386 (-21.89) | 1.0 | 0.0548 | 0.2765 | False | min_trades, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
