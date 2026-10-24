# gen_2610241115_000 — engine run 20261024_110611_gen_2610241115_000

Hypothesis: grammar draw seed=2610241115: supertrend+relvol

**0/4 pass.** Ledger N at evaluation: 2466. PBO (CSCV) across family: 0.641. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 0265ad897e76e53eab788cdb3c1a952d138a40883835f36b9a52a6157450e034. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2463 | crypto|supertrend(atr_n=10,mult=2)+relvol(min_ratio=1.0) | 6.05/0.29/-15.59 | 434.62 | 427 | 0.0202 | 0.85814 (89.88) | 1.0 | 0.4964 | 0.911 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2464 | crypto|supertrend(atr_n=10,mult=4)+relvol(min_ratio=1.0) | 3.01/0.2/-17.04 | 434.62 | 439 | 0.0198 | 0.88212 (132.49) | 1.0 | 0.4531 | 0.9095 | False | beats_buy_hold, walk_forward, holm, dsr, spa, pbo |
| 2465 | crypto|supertrend(atr_n=14,mult=2)+relvol(min_ratio=1.0) | 8.23/0.36/-15.24 | 434.62 | 404 | 0.0206 | 0.82917 (78.08) | 1.0 | 0.5289 | 0.908 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 2466 | crypto|supertrend(atr_n=14,mult=4)+relvol(min_ratio=1.0) | 9.49/0.4/-17.04 | 434.62 | 414 | 0.0203 | 0.81119 (112.14) | 1.0 | 0.547 | 0.906 | False | beats_buy_hold, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
