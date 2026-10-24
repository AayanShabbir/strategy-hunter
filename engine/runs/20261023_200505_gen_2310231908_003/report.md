# gen_2310231908_003 — engine run 20261023_200505_gen_2310231908_003

Hypothesis: grammar draw seed=2310231908: supertrend

**0/4 pass.** Ledger N at evaluation: 786. PBO (CSCV) across family: 0.614. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 c2f42e65f9481d20c5731a2f4f7e4ba442da66b22a964cdde7e5d70bb0687d18. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 783 | semis|supertrend(atr_n=7,mult=3) | 28.4/0.72/-17.9 | -38.66 | 2254 | 0.09 | 0.05395 (-33.22) | 1.0 | 0.5446 | 0.1295 | False | cost_stop, holm, dsr, spa, pbo |
| 784 | semis|supertrend(atr_n=7,mult=4) | 7.65/0.32/-24.6 | -38.66 | 2013 | 0.0925 | 0.21479 (-31.69) | 1.0 | 0.355 | 0.1625 | False | cost_stop, walk_forward, holm, dsr, spa, pbo |
| 785 | semis|supertrend(atr_n=14,mult=3) | 4.7/0.26/-21.67 | -38.66 | 2232 | 0.0906 | 0.23277 (-33.11) | 1.0 | 0.3726 | 0.1785 | False | cost_stop, walk_forward, holm, dsr, spa, pbo |
| 786 | semis|supertrend(atr_n=14,mult=4) | 20.96/0.56/-22.05 | -38.66 | 2011 | 0.0925 | 0.11189 (-30.99) | 1.0 | 0.4623 | 0.118 | False | cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
