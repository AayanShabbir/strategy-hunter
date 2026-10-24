# gen_2310232311_001 — engine run 20261023_230804_gen_2310232311_001

Hypothesis: grammar draw seed=2310232311: donchian+vol_regime

**0/4 pass.** Ledger N at evaluation: 1166. PBO (CSCV) across family: 0.654. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 71dbf48d178db07f890653f645c2488316c0a231c3879760159a2c5366f5ffb6. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1163 | sectors|donchian(entry_n=20,exit_n=10)+vol_regime(max_atr_pct=0.02) | 14.11/0.7/-9.04 | 64.05 | 120 | 0.0607 | 0.86713 (26.84) | 1.0 | 0.755 | 0.5125 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1164 | sectors|donchian(entry_n=20,exit_n=20)+vol_regime(max_atr_pct=0.02) | 20.44/0.8/-9.36 | 64.05 | 103 | 0.0521 | 0.70829 (27.46) | 1.0 | 0.8092 | 0.523 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1165 | sectors|donchian(entry_n=100,exit_n=10)+vol_regime(max_atr_pct=0.02) | 13.33/0.86/-3.81 | 64.05 | 77 | 0.0739 | 0.90509 (27.46) | 1.0 | 0.83 | 0.507 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 1166 | sectors|donchian(entry_n=100,exit_n=20)+vol_regime(max_atr_pct=0.02) | 17.26/0.9/-5.9 | 64.05 | 63 | 0.0648 | 0.86014 (28.39) | 1.0 | 0.8499 | 0.5115 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
