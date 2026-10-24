# gen_2610240805_000 — engine run 20261024_080353_gen_2610240805_000

Hypothesis: grammar draw seed=2610240805: drop_revert+trend_sma

**0/8 pass.** Ledger N at evaluation: 2150. PBO (CSCV) across family: 0.514. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 fdf6867d378ea834c016cfeb71088ccde4312b6f229f1c31385ad76a3d178e4f. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2143 | crypto|drop_revert(drop=0.05,hold=3,n=3)+trend_sma(n=200) | 9.64/0.48/-11.27 | 56.21 | 76 | 0.0183 | 0.72128 (27.23) | 1.0 | 0.0897 | 0.82 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2144 | crypto|drop_revert(drop=0.05,hold=3,n=5)+trend_sma(n=200) | 4.71/0.27/-12.71 | 56.21 | 82 | 0.0192 | 0.75524 (26.89) | 1.0 | 0.0557 | 0.859 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2145 | crypto|drop_revert(drop=0.05,hold=5,n=3)+trend_sma(n=200) | -5.31/-0.11/-12.9 | 56.21 | 71 | 0.0183 | 0.83716 (25.11) | 1.0 | 0.0215 | 0.8935 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2146 | crypto|drop_revert(drop=0.05,hold=5,n=5)+trend_sma(n=200) | 21.99/0.74/-14.45 | 56.21 | 83 | 0.0191 | 0.53946 (26.62) | 1.0 | 0.1496 | 0.792 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2147 | crypto|drop_revert(drop=0.1,hold=3,n=3)+trend_sma(n=200) | 10.11/0.9/-2.83 | 56.21 | 20 | 0.0159 | 0.72428 (25.91) | 1.0 | 0.1402 | 0.818 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2148 | crypto|drop_revert(drop=0.1,hold=3,n=5)+trend_sma(n=200) | 24.96/1.32/-5.89 | 56.21 | 28 | 0.0171 | 0.53546 (28.57) | 1.0 | 0.3531 | 0.746 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2149 | crypto|drop_revert(drop=0.1,hold=5,n=3)+trend_sma(n=200) | 8.04/0.56/-7.17 | 56.21 | 22 | 0.0161 | 0.76024 (27.76) | 1.0 | 0.096 | 0.8255 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2150 | crypto|drop_revert(drop=0.1,hold=5,n=5)+trend_sma(n=200) | 21.82/1.05/-7.17 | 56.21 | 29 | 0.0176 | 0.58242 (27.28) | 1.0 | 0.242 | 0.76 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
