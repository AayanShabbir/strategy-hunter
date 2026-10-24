# gen_2410240414_000 — engine run 20261024_041002_gen_2410240414_000

Hypothesis: grammar draw seed=2410240414: drop_revert

**0/8 pass.** Ledger N at evaluation: 1738. PBO (CSCV) across family: 0.141. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 16b5b25728f2d6a496e2a91a5c16501de75df0ae573f9a0811ad113d4ad94209. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1731 | US_INDEX|drop_revert(drop=0.05,hold=3,n=3) | 15.13/0.74/-3.91 | 68.31 | 121 | 0.0421 | 0.94006 (30.0) | 1.0 | 0.4374 | 0.951 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1732 | US_INDEX|drop_revert(drop=0.05,hold=3,n=5) | 9.09/0.47/-5.07 | 68.31 | 163 | 0.0477 | 0.99101 (30.24) | 1.0 | 0.2396 | 0.4965 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1733 | US_INDEX|drop_revert(drop=0.05,hold=5,n=3) | 16.12/0.77/-3.91 | 68.31 | 118 | 0.0425 | 0.9021 (30.34) | 1.0 | 0.4684 | 0.948 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1734 | US_INDEX|drop_revert(drop=0.05,hold=5,n=5) | 11.71/0.57/-5.65 | 68.31 | 159 | 0.048 | 0.98901 (30.52) | 1.0 | 0.3087 | 0.492 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1735 | US_INDEX|drop_revert(drop=0.1,hold=3,n=3) | 1.04/0.09/-4.45 | 68.31 | 16 | 0.0285 | 1.0 (30.82) | 1.0 | 0.1013 | 0.497 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1736 | US_INDEX|drop_revert(drop=0.1,hold=3,n=5) | 8.39/0.45/-3.91 | 68.31 | 23 | 0.031 | 0.98302 (31.1) | 1.0 | 0.2072 | 0.981 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 1737 | US_INDEX|drop_revert(drop=0.1,hold=5,n=3) | 4.04/0.23/-4.45 | 68.31 | 14 | 0.0292 | 0.99101 (30.28) | 1.0 | 0.1417 | 0.49 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1738 | US_INDEX|drop_revert(drop=0.1,hold=5,n=5) | 6.45/0.36/-3.91 | 68.31 | 23 | 0.031 | 0.98901 (31.15) | 1.0 | 0.1669 | 0.4925 | False | beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
