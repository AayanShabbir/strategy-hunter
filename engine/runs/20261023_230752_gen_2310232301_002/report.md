# gen_2310232301_002 — engine run 20261023_230752_gen_2310232301_002

Hypothesis: grammar draw seed=2310232301: drop_revert

**0/8 pass.** Ledger N at evaluation: 1122. PBO (CSCV) across family: 0.528. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 e0c1e48f5e10dec4ee2a7a73a320c10cabeeff2aed7d23b55546804d2360ff00. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1115 | crypto_d|drop_revert(drop=0.05,hold=5,n=3) | 15.43/0.45/-33.32 | 434.62 | 225 | 0.0158 | 0.7962 (132.66) | 1.0 | 0.3473 | 0.9055 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1116 | crypto_d|drop_revert(drop=0.05,hold=5,n=5) | 3.07/0.26/-33.84 | 434.62 | 220 | 0.0163 | 0.8971 (119.47) | 1.0 | 0.2663 | 0.9115 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1117 | crypto_d|drop_revert(drop=0.05,hold=10,n=3) | 23.93/0.55/-43.62 | 434.62 | 134 | 0.0168 | 0.75924 (220.78) | 1.0 | 0.3955 | 0.905 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1118 | crypto_d|drop_revert(drop=0.05,hold=10,n=5) | 32.24/0.64/-40.72 | 434.62 | 131 | 0.0176 | 0.7013 (187.25) | 1.0 | 0.4375 | 0.887 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1119 | crypto_d|drop_revert(drop=0.1,hold=5,n=3) | -5.0/0.02/-26.11 | 434.62 | 126 | 0.012 | 0.94306 (92.09) | 1.0 | 0.1841 | 0.908 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 1120 | crypto_d|drop_revert(drop=0.1,hold=5,n=5) | 17.32/0.51/-20.0 | 434.62 | 144 | 0.012 | 0.80619 (92.0) | 1.0 | 0.3752 | 0.896 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1121 | crypto_d|drop_revert(drop=0.1,hold=10,n=3) | 14.03/0.44/-26.83 | 434.62 | 102 | 0.0129 | 0.8012 (99.23) | 1.0 | 0.342 | 0.8935 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1122 | crypto_d|drop_revert(drop=0.1,hold=10,n=5) | 37.03/0.79/-29.19 | 434.62 | 110 | 0.0134 | 0.69431 (190.81) | 1.0 | 0.5083 | 0.874 | False | beats_buy_hold, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
