# gen_2610241000_000 — engine run 20261024_100927_gen_2610241000_000

Hypothesis: grammar draw seed=2610241000: drop_revert+trend_sma

**0/8 pass.** Ledger N at evaluation: 2278. PBO (CSCV) across family: 0.75. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 5a8bf8024b45fd87a1bdfa8da029a21c397ade124fa2e6b2fc94f142577a54c7. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2271 | crypto|drop_revert(drop=0.05,hold=3,n=3)+trend_sma(n=200) | 10.39/0.5/-9.6 | 434.62 | 103 | 0.0169 | 0.80519 (227.2) | 1.0 | 0.1066 | 0.8965 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2272 | crypto|drop_revert(drop=0.05,hold=3,n=5)+trend_sma(n=200) | -5.19/-0.12/-13.14 | 434.62 | 106 | 0.0175 | 0.94306 (258.43) | 1.0 | 0.0276 | 0.9115 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 2273 | crypto|drop_revert(drop=0.05,hold=5,n=3)+trend_sma(n=200) | -4.54/-0.08/-13.06 | 434.62 | 92 | 0.0172 | 0.92108 (232.92) | 1.0 | 0.0298 | 0.9105 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2274 | crypto|drop_revert(drop=0.05,hold=5,n=5)+trend_sma(n=200) | 8.4/0.37/-14.26 | 434.62 | 103 | 0.0178 | 0.82817 (252.08) | 1.0 | 0.085 | 0.905 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 2275 | crypto|drop_revert(drop=0.15,hold=3,n=3)+trend_sma(n=200) | 8.0/0.84/-1.96 | 434.62 | 7 | 0.0105 | 0.89011 (44.84) | 1.0 | 0.1071 | 0.9015 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2276 | crypto|drop_revert(drop=0.15,hold=3,n=5)+trend_sma(n=200) | 12.17/1.16/-1.96 | 434.62 | 16 | 0.0112 | 0.81518 (245.48) | 1.0 | 0.2505 | 0.896 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2277 | crypto|drop_revert(drop=0.15,hold=5,n=3)+trend_sma(n=200) | 2.74/0.29/-6.67 | 434.62 | 7 | 0.0105 | 0.92408 (312.31) | 1.0 | 0.0562 | 0.9045 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2278 | crypto|drop_revert(drop=0.15,hold=5,n=5)+trend_sma(n=200) | 4.71/0.45/-6.67 | 434.62 | 16 | 0.0112 | 0.88312 (65.06) | 1.0 | 0.0784 | 0.9025 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
