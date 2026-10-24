# gen_2610240905_000 — engine run 20261024_091150_gen_2610240905_000

Hypothesis: grammar draw seed=2610240905: supertrend+vol_regime

**0/4 pass.** Ledger N at evaluation: 2214. PBO (CSCV) across family: 0.711. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 84ede1718b13c8762ea27b39585a784f1b6043f3c52fc718269fe90b863b9533. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2211 | crypto|supertrend(atr_n=7,mult=2)+vol_regime(max_atr_pct=0.04) | 5.76/0.35/-9.35 | 637.22 | 38 | 0.0258 | 0.86813 (394.46) | 1.0 | 0.6149 | 0.912 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2212 | crypto|supertrend(atr_n=7,mult=4)+vol_regime(max_atr_pct=0.04) | 6.4/0.36/-13.47 | 637.22 | 31 | 0.0255 | 0.84815 (55.15) | 1.0 | 0.6224 | 0.915 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2213 | crypto|supertrend(atr_n=10,mult=2)+vol_regime(max_atr_pct=0.04) | 6.25/0.37/-9.35 | 637.22 | 38 | 0.026 | 0.86513 (384.52) | 1.0 | 0.6253 | 0.9115 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2214 | crypto|supertrend(atr_n=10,mult=4)+vol_regime(max_atr_pct=0.04) | 5.08/0.3/-14.19 | 637.22 | 31 | 0.0255 | 0.87013 (52.01) | 1.0 | 0.594 | 0.9155 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
