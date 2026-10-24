# gen_2310232301_003 — engine run 20261023_230754_gen_2310232301_003

Hypothesis: grammar draw seed=2310232301: drop_revert+relvol

**0/8 pass.** Ledger N at evaluation: 1130. PBO (CSCV) across family: 0.122. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 42af299efcd8274fdfde501706fd243d9f440650dc0c228867452f439d00a1b3. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1123 | crypto_d|drop_revert(drop=0.1,hold=3,n=1)+relvol(min_ratio=1.0) | 12.23/0.84/-4.56 | 434.62 | 60 | 0.0102 | 0.86713 (194.43) | 1.0 | 0.5876 | 0.897 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1124 | crypto_d|drop_revert(drop=0.1,hold=3,n=5)+relvol(min_ratio=1.0) | 24.22/0.85/-11.78 | 434.62 | 166 | 0.0121 | 0.74326 (206.5) | 1.0 | 0.5689 | 0.8875 | False | beats_buy_hold, holm, dsr, spa |
| 1125 | crypto_d|drop_revert(drop=0.1,hold=5,n=1)+relvol(min_ratio=1.0) | 5.73/0.41/-4.89 | 434.62 | 73 | 0.0107 | 0.90909 (188.45) | 1.0 | 0.3472 | 0.9045 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1126 | crypto_d|drop_revert(drop=0.1,hold=5,n=5)+relvol(min_ratio=1.0) | 32.74/1.03/-11.78 | 434.62 | 210 | 0.0123 | 0.66134 (69.84) | 1.0 | 0.6525 | 0.882 | False | beats_buy_hold, holm, dsr, spa |
| 1127 | crypto_d|drop_revert(drop=0.15,hold=3,n=1)+relvol(min_ratio=1.0) | 0.65/0.81/-0.02 | 434.62 | 13 | 0.0073 | 1.0 (156.74) | 1.0 | 0.5955 | 0.9055 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1128 | crypto_d|drop_revert(drop=0.15,hold=3,n=5)+relvol(min_ratio=1.0) | 22.86/1.03/-4.96 | 434.62 | 81 | 0.0106 | 0.72128 (70.27) | 1.0 | 0.6848 | 0.8865 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1129 | crypto_d|drop_revert(drop=0.15,hold=5,n=1)+relvol(min_ratio=1.0) | 0.65/0.81/-0.02 | 434.62 | 16 | 0.0072 | 1.0 (52.21) | 1.0 | 0.5955 | 0.9055 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1130 | crypto_d|drop_revert(drop=0.15,hold=5,n=5)+relvol(min_ratio=1.0) | 12.67/0.56/-11.78 | 434.62 | 104 | 0.0107 | 0.8012 (68.61) | 1.0 | 0.4314 | 0.9 | False | beats_buy_hold, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
