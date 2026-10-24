# gen_2610240911_000 — engine run 20261024_091208_gen_2610240911_000

Hypothesis: grammar draw seed=2610240911: supertrend

**0/4 pass.** Ledger N at evaluation: 2250. PBO (CSCV) across family: 0.508. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 fee0f29db860b5b1a53a0211dd76eb5cb32589a828d0de992272c49833994a3a. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2247 | sectors|supertrend(atr_n=10,mult=2) | 40.09/1.15/-11.25 | 90.03 | 258 | 0.0562 | 0.35964 (36.21) | 1.0 | 0.7384 | 0.486 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2248 | sectors|supertrend(atr_n=10,mult=4) | 22.32/0.75/-8.16 | 90.03 | 97 | 0.0553 | 0.9001 (37.68) | 1.0 | 0.4819 | 0.522 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 2249 | sectors|supertrend(atr_n=14,mult=2) | 40.86/1.14/-12.96 | 90.03 | 261 | 0.0561 | 0.32567 (36.04) | 1.0 | 0.7314 | 0.485 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2250 | sectors|supertrend(atr_n=14,mult=4) | 24.08/0.77/-9.77 | 90.03 | 93 | 0.0551 | 0.87113 (38.16) | 1.0 | 0.4967 | 0.528 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
