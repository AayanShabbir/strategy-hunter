# gen_2310232111_000 — engine run 20261023_210404_gen_2310232111_000

Hypothesis: grammar draw seed=2310232111: donchian+vol_regime

**0/4 pass.** Ledger N at evaluation: 914. PBO (CSCV) across family: 0.092. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 4ec01582c1cc955c7b68169755305507d6977952d675eb28ec2f82a2cb6932b3. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 911 | sectors|donchian(entry_n=20,exit_n=10)+vol_regime(max_atr_pct=0.02) | 11.52/0.72/-5.74 | 50.2 | 378 | 0.0707 | 0.95205 (21.34) | 1.0 | 0.6922 | 0.5035 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 912 | sectors|donchian(entry_n=20,exit_n=20)+vol_regime(max_atr_pct=0.02) | 11.15/0.58/-7.68 | 50.2 | 299 | 0.0624 | 0.97203 (21.8) | 1.0 | 0.6053 | 0.5175 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 913 | sectors|donchian(entry_n=100,exit_n=10)+vol_regime(max_atr_pct=0.02) | 5.87/0.54/-3.21 | 50.2 | 245 | 0.0794 | 0.998 (22.46) | 1.0 | 0.5791 | 0.5045 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 914 | sectors|donchian(entry_n=100,exit_n=20)+vol_regime(max_atr_pct=0.02) | 5.18/0.4/-3.92 | 50.2 | 198 | 0.076 | 1.0 (22.19) | 1.0 | 0.4861 | 0.5075 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
