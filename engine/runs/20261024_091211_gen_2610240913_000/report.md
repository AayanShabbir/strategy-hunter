# gen_2610240913_000 — engine run 20261024_091211_gen_2610240913_000

Hypothesis: grammar draw seed=2610240913: donchian

**0/4 pass.** Ledger N at evaluation: 2254. PBO (CSCV) across family: 0.748. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 07a36bf4a24454d45f194349db7fed8446ac65f066a831a5bee8cd889ce7ec22. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2251 | crypto|donchian(entry_n=20,exit_n=10) | 3.84/0.24/-19.06 | 434.62 | 66 | 0.02 | 0.90509 (171.24) | 1.0 | 0.354 | 0.912 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2252 | crypto|donchian(entry_n=20,exit_n=20) | 24.28/0.6/-25.97 | 434.62 | 46 | 0.0198 | 0.77123 (121.4) | 1.0 | 0.5253 | 0.907 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2253 | crypto|donchian(entry_n=55,exit_n=10) | 8.89/0.36/-22.01 | 434.62 | 39 | 0.0203 | 0.87712 (189.33) | 1.0 | 0.4107 | 0.9065 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2254 | crypto|donchian(entry_n=55,exit_n=20) | 15.81/0.49/-26.31 | 434.62 | 32 | 0.0201 | 0.82617 (111.18) | 1.0 | 0.4714 | 0.908 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
