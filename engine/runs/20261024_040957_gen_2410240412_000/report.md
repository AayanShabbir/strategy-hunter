# gen_2410240412_000 — engine run 20261024_040957_gen_2410240412_000

Hypothesis: grammar draw seed=2410240412: drop_revert

**0/8 pass.** Ledger N at evaluation: 1726. PBO (CSCV) across family: 0.625. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 410c897bfe7ac741bca534f07f0e2192cac28abb90f58c339e58143eba07cf78. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1719 | BTC_ETH|drop_revert(drop=0.05,hold=3,n=1) | -12.42/-0.24/-30.86 | 56.21 | 150 | 0.0162 | 0.92507 (26.08) | 1.0 | 0.079 | 0.9145 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1720 | BTC_ETH|drop_revert(drop=0.05,hold=3,n=3) | 1.76/0.19/-19.93 | 56.21 | 186 | 0.0167 | 0.78422 (24.1) | 1.0 | 0.1771 | 0.851 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1721 | BTC_ETH|drop_revert(drop=0.05,hold=5,n=1) | -18.7/-0.31/-36.37 | 56.21 | 126 | 0.0167 | 0.95904 (26.61) | 1.0 | 0.0667 | 0.9305 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1722 | BTC_ETH|drop_revert(drop=0.05,hold=5,n=3) | 9.05/0.34/-25.03 | 56.21 | 150 | 0.0175 | 0.67033 (24.59) | 1.0 | 0.2311 | 0.8465 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1723 | BTC_ETH|drop_revert(drop=0.15,hold=3,n=1) | 0.0/0.0/0.0 | 56.21 | 6 | 0.0081 | 1.0 (36.28) | 1.0 | 0.0 | 0.86 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1724 | BTC_ETH|drop_revert(drop=0.15,hold=3,n=3) | 4.36/0.31/-6.5 | 56.21 | 26 | 0.0122 | 0.76424 (27.02) | 1.0 | 0.2121 | 0.84 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1725 | BTC_ETH|drop_revert(drop=0.15,hold=5,n=1) | 0.0/0.0/0.0 | 56.21 | 6 | 0.0081 | 1.0 (25.91) | 1.0 | 0.0 | 0.86 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1726 | BTC_ETH|drop_revert(drop=0.15,hold=5,n=3) | 0.53/0.1/-7.44 | 56.21 | 25 | 0.0124 | 0.77922 (27.74) | 1.0 | 0.1508 | 0.8555 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
