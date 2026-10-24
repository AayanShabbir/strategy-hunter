# gen_2610240802_000 — engine run 20261024_080321_gen_2610240802_000

Hypothesis: grammar draw seed=2610240802: donchian+vol_regime

**0/4 pass.** Ledger N at evaluation: 2102. PBO (CSCV) across family: 0.423. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 3806c9a17a9f1cc6e50fb99a68ab723f3133c83da90bba720d3bbd7a3f81248d. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2099 | sectors|donchian(entry_n=20,exit_n=10)+vol_regime(max_atr_pct=0.02) | 11.52/0.72/-5.74 | 50.2 | 378 | 0.0707 | 0.96104 (21.44) | 1.0 | 0.6942 | 0.5035 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2100 | sectors|donchian(entry_n=20,exit_n=20)+vol_regime(max_atr_pct=0.02) | 11.15/0.58/-7.68 | 50.2 | 299 | 0.0624 | 0.97203 (21.78) | 1.0 | 0.6075 | 0.5175 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2101 | sectors|donchian(entry_n=55,exit_n=10)+vol_regime(max_atr_pct=0.02) | 11.16/0.87/-3.85 | 50.2 | 282 | 0.0778 | 0.98102 (22.02) | 1.0 | 0.7774 | 0.4945 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 2102 | sectors|donchian(entry_n=55,exit_n=20)+vol_regime(max_atr_pct=0.02) | 11.04/0.72/-4.44 | 50.2 | 225 | 0.0723 | 0.97702 (22.17) | 1.0 | 0.6951 | 0.5125 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
