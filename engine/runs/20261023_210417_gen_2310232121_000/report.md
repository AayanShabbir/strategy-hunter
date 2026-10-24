# gen_2310232121_000 — engine run 20261023_210417_gen_2310232121_000

Hypothesis: grammar draw seed=2310232121: supertrend+vol_regime

**0/4 pass.** Ledger N at evaluation: 938. PBO (CSCV) across family: 0.252. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 f46570f523962db100bce6a6c2e30c910c8317e58795cac550840970e7996d22. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 935 | megacap|supertrend(atr_n=10,mult=2)+vol_regime(max_atr_pct=0.06) | 9.45/0.47/-17.47 | 26.77 | 3681 | 0.1261 | 0.76823 (-6.97) | 1.0 | 0.0674 | 0.864 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 936 | megacap|supertrend(atr_n=10,mult=3)+vol_regime(max_atr_pct=0.06) | -13.32/-0.35/-28.81 | 26.77 | 3232 | 0.129 | 0.87612 (-4.96) | 1.0 | 0.0063 | 0.947 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 937 | megacap|supertrend(atr_n=14,mult=2)+vol_regime(max_atr_pct=0.06) | 9.54/0.48/-16.54 | 26.77 | 3700 | 0.1262 | 0.75824 (-7.52) | 1.0 | 0.0703 | 0.8565 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 938 | megacap|supertrend(atr_n=14,mult=3)+vol_regime(max_atr_pct=0.06) | -16.81/-0.5/-27.96 | 26.77 | 3241 | 0.1291 | 0.91209 (-4.89) | 1.0 | 0.003 | 0.96 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
