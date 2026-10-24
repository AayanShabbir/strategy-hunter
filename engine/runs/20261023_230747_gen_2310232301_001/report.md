# gen_2310232301_001 — engine run 20261023_230747_gen_2310232301_001

Hypothesis: grammar draw seed=2310232301: drop_revert+relvol

**0/8 pass.** Ledger N at evaluation: 1114. PBO (CSCV) across family: 0.163. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 037702077bd58dd7fd47a8d6a0e327d189b51cd5906435e4678c4b0d493541a6. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1107 | crypto_d|drop_revert(drop=0.1,hold=5,n=3)+relvol(min_ratio=1.0) | 19.17/0.7/-11.78 | 434.62 | 176 | 0.012 | 0.7962 (88.34) | 1.0 | 0.1831 | 0.8925 | False | beats_buy_hold, holm, dsr, spa |
| 1108 | crypto_d|drop_revert(drop=0.1,hold=5,n=5)+relvol(min_ratio=1.0) | 32.74/1.03/-11.78 | 434.62 | 210 | 0.0123 | 0.66034 (77.67) | 1.0 | 0.3053 | 0.882 | False | beats_buy_hold, holm, dsr, spa |
| 1109 | crypto_d|drop_revert(drop=0.1,hold=10,n=3)+relvol(min_ratio=1.0) | 49.85/1.31/-11.78 | 434.62 | 253 | 0.0126 | 0.59341 (101.92) | 1.0 | 0.4332 | 0.865 | False | beats_buy_hold, holm, dsr, spa |
| 1110 | crypto_d|drop_revert(drop=0.1,hold=10,n=5)+relvol(min_ratio=1.0) | 57.28/1.45/-11.78 | 434.62 | 289 | 0.0131 | 0.57842 (197.21) | 1.0 | 0.5013 | 0.857 | False | beats_buy_hold, holm, dsr, spa |
| 1111 | crypto_d|drop_revert(drop=0.15,hold=5,n=3)+relvol(min_ratio=1.0) | -0.11/0.07/-11.85 | 434.62 | 59 | 0.0102 | 0.92408 (207.01) | 1.0 | 0.0501 | 0.9065 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1112 | crypto_d|drop_revert(drop=0.15,hold=5,n=5)+relvol(min_ratio=1.0) | 12.67/0.56/-11.78 | 434.62 | 104 | 0.0107 | 0.81019 (81.78) | 1.0 | 0.1431 | 0.9 | False | beats_buy_hold, holm, dsr, spa |
| 1113 | crypto_d|drop_revert(drop=0.15,hold=10,n=3)+relvol(min_ratio=1.0) | 14.88/0.68/-11.78 | 434.62 | 94 | 0.01 | 0.80519 (224.72) | 1.0 | 0.189 | 0.894 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1114 | crypto_d|drop_revert(drop=0.15,hold=10,n=5)+relvol(min_ratio=1.0) | 18.33/0.72/-11.78 | 434.62 | 147 | 0.0108 | 0.76224 (183.9) | 1.0 | 0.1929 | 0.8925 | False | beats_buy_hold, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
