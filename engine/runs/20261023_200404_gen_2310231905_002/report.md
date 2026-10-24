# gen_2310231905_002 — engine run 20261023_200404_gen_2310231905_002

Hypothesis: grammar draw seed=2310231905: drop_revert+rsi_band

**0/8 pass.** Ledger N at evaluation: 714. PBO (CSCV) across family: 0.018. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 99695249a4ec02f06d80afda78106aedb1a0cbbb938bd851710ad2bf753c8495. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 707 | crypto|drop_revert(drop=0.1,hold=3,n=1)+rsi_band(hi=60) | -0.6/-0.82/-0.6 | 428.6 | 15 | 0.0143 | 0.95604 (47.85) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 708 | crypto|drop_revert(drop=0.1,hold=3,n=3)+rsi_band(hi=60) | 0.46/0.34/-0.71 | 428.6 | 47 | 0.0154 | 0.95904 (232.39) | 1.0 | 0.0122 | 0.909 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 709 | crypto|drop_revert(drop=0.1,hold=5,n=1)+rsi_band(hi=60) | 0.35/0.26/-0.6 | 428.6 | 16 | 0.0146 | 0.96004 (46.47) | 1.0 | 0.0103 | 0.909 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 710 | crypto|drop_revert(drop=0.1,hold=5,n=3)+rsi_band(hi=60) | 1.51/0.69/-0.6 | 428.6 | 46 | 0.0155 | 0.95005 (68.79) | 1.0 | 0.0127 | 0.908 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 711 | crypto|drop_revert(drop=0.15,hold=3,n=1)+rsi_band(hi=60) | 0.0/0.0/0.0 | 428.6 | 4 | 0.0106 | 1.0 (42.03) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 712 | crypto|drop_revert(drop=0.15,hold=3,n=3)+rsi_band(hi=60) | 0.0/0.0/0.0 | 428.6 | 10 | 0.0126 | 1.0 (42.03) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 713 | crypto|drop_revert(drop=0.15,hold=5,n=1)+rsi_band(hi=60) | 0.0/0.0/0.0 | 428.6 | 4 | 0.0106 | 1.0 (312.99) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 714 | crypto|drop_revert(drop=0.15,hold=5,n=3)+rsi_band(hi=60) | 0.0/0.0/0.0 | 428.6 | 10 | 0.0126 | 1.0 (42.03) | 1.0 | 0.0 | 0.909 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
