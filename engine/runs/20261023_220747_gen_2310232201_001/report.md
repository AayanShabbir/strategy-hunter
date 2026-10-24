# gen_2310232201_001 — engine run 20261023_220747_gen_2310232201_001

Hypothesis: grammar draw seed=2310232201: drop_revert+trend_sma

**0/8 pass.** Ledger N at evaluation: 1006. PBO (CSCV) across family: 0.458. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 dc7c827ce6adf676530ff746d6eb7f656e6ec8e9063b75b2ba5655f5a8b88a11. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 999 | crypto_d|drop_revert(drop=0.1,hold=5,n=3)+trend_sma(n=100) | 14.29/0.71/-10.48 | 234.6 | 112 | 0.0111 | 0.8042 (119.32) | 1.0 | 0.3496 | 0.884 | False | beats_buy_hold, holm, dsr, spa |
| 1000 | crypto_d|drop_revert(drop=0.1,hold=5,n=5)+trend_sma(n=100) | 16.6/0.77/-10.3 | 234.6 | 130 | 0.0114 | 0.77223 (72.34) | 1.0 | 0.3795 | 0.885 | False | beats_buy_hold, holm, dsr, spa |
| 1001 | crypto_d|drop_revert(drop=0.1,hold=10,n=3)+trend_sma(n=100) | 35.78/1.14/-18.85 | 234.6 | 120 | 0.0117 | 0.62438 (93.15) | 1.0 | 0.5582 | 0.868 | False | beats_buy_hold, holm, dsr, spa |
| 1002 | crypto_d|drop_revert(drop=0.1,hold=10,n=5)+trend_sma(n=100) | 22.58/0.79/-16.17 | 234.6 | 140 | 0.0122 | 0.72028 (61.37) | 1.0 | 0.3867 | 0.8805 | False | beats_buy_hold, holm, dsr, spa |
| 1003 | crypto_d|drop_revert(drop=0.15,hold=5,n=3)+trend_sma(n=100) | 0.14/0.05/-3.6 | 234.6 | 38 | 0.0095 | 0.96903 (48.04) | 1.0 | 0.1194 | 0.8975 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1004 | crypto_d|drop_revert(drop=0.15,hold=5,n=5)+trend_sma(n=100) | 9.08/0.71/-8.11 | 234.6 | 57 | 0.0103 | 0.83716 (61.3) | 1.0 | 0.3526 | 0.888 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1005 | crypto_d|drop_revert(drop=0.15,hold=10,n=3)+trend_sma(n=100) | 5.24/0.47/-7.16 | 234.6 | 43 | 0.0101 | 0.91409 (38.8) | 1.0 | 0.2479 | 0.893 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1006 | crypto_d|drop_revert(drop=0.15,hold=10,n=5)+trend_sma(n=100) | 12.89/0.78/-9.77 | 234.6 | 59 | 0.0109 | 0.8022 (117.92) | 1.0 | 0.3837 | 0.885 | False | beats_buy_hold, min_trades, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
