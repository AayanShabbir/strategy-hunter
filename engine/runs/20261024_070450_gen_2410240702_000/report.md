# gen_2410240702_000 — engine run 20261024_070450_gen_2410240702_000

Hypothesis: grammar draw seed=2410240702: drop_revert+trend_sma

**0/8 pass.** Ledger N at evaluation: 2010. PBO (CSCV) across family: 0.674. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 41895e3b64387e8e29113fff2c925b4636e37ad5432df53df0dcbe1bf5fb1cf7. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2003 | crypto_d|drop_revert(drop=0.1,hold=3,n=1)+trend_sma(n=50) | 6.01/0.64/-4.06 | 234.6 | 36 | 0.0099 | 0.9041 (35.77) | 1.0 | 0.4524 | 0.892 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2004 | crypto_d|drop_revert(drop=0.1,hold=3,n=5)+trend_sma(n=50) | 8.29/0.67/-5.16 | 234.6 | 108 | 0.0112 | 0.85415 (120.03) | 1.0 | 0.4715 | 0.89 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2005 | crypto_d|drop_revert(drop=0.1,hold=5,n=1)+trend_sma(n=50) | 6.95/0.7/-5.32 | 234.6 | 37 | 0.0099 | 0.91508 (164.53) | 1.0 | 0.4867 | 0.891 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2006 | crypto_d|drop_revert(drop=0.1,hold=5,n=5)+trend_sma(n=50) | 5.44/0.38/-11.33 | 234.6 | 126 | 0.0113 | 0.84116 (67.71) | 1.0 | 0.3386 | 0.8935 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 2007 | crypto_d|drop_revert(drop=0.15,hold=3,n=1)+trend_sma(n=50) | 3.48/1.12/-0.17 | 234.6 | 8 | 0.0071 | 0.93906 (47.74) | 1.0 | 0.8125 | 0.8945 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2008 | crypto_d|drop_revert(drop=0.15,hold=3,n=5)+trend_sma(n=50) | 4.16/0.68/-2.48 | 234.6 | 47 | 0.0101 | 0.8991 (66.33) | 1.0 | 0.4762 | 0.8935 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2009 | crypto_d|drop_revert(drop=0.15,hold=5,n=1)+trend_sma(n=50) | 2.18/0.65/-1.26 | 234.6 | 8 | 0.0071 | 0.96404 (43.86) | 1.0 | 0.4561 | 0.8945 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2010 | crypto_d|drop_revert(drop=0.15,hold=5,n=5)+trend_sma(n=50) | 3.91/0.51/-4.47 | 234.6 | 56 | 0.0102 | 0.89411 (68.41) | 1.0 | 0.398 | 0.8935 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
