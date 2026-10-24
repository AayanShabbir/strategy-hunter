# gen_2410240212_000 — engine run 20261024_020821_gen_2410240212_000

Hypothesis: grammar draw seed=2410240212: supertrend

**0/4 pass.** Ledger N at evaluation: 1570. PBO (CSCV) across family: 0.622. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 89212d665db4424a9da8823180900919ea5abb4bd40bc48f17d3eac6724b837b. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1567 | hibeta|supertrend(atr_n=7,mult=3) | 291.77/1.56/-31.99 | 809.88 | 164 | 0.0236 | 0.2028 (215.41) | 1.0 | 0.9232 | 0.503 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1568 | hibeta|supertrend(atr_n=7,mult=4) | 210.85/1.29/-24.5 | 809.88 | 104 | 0.0231 | 0.47952 (221.67) | 1.0 | 0.8247 | 0.514 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 1569 | hibeta|supertrend(atr_n=10,mult=3) | 355.71/1.77/-23.24 | 809.88 | 162 | 0.024 | 0.07393 (216.81) | 1.0 | 0.9652 | 0.5005 | False | beats_buy_hold, holm, spa, pbo |
| 1570 | hibeta|supertrend(atr_n=10,mult=4) | 222.71/1.33/-26.1 | 809.88 | 105 | 0.0231 | 0.45355 (225.02) | 1.0 | 0.8428 | 0.511 | False | beats_buy_hold, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
