# gen_2310232211_001 — engine run 20261023_220802_gen_2310232211_001

Hypothesis: grammar draw seed=2310232211: donchian+trend_sma

**0/4 pass.** Ledger N at evaluation: 1038. PBO (CSCV) across family: 0.635. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 531923890a4eac937e65ba3acb17e4562e2430c97ce932e674e66b8b2cc21b88. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1035 | sectors|donchian(entry_n=20,exit_n=10)+trend_sma(n=200) | 7.67/0.49/-5.74 | 50.2 | 387 | 0.0703 | 0.99101 (21.9) | 1.0 | 0.5158 | 0.499 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1036 | sectors|donchian(entry_n=20,exit_n=20)+trend_sma(n=200) | 5.59/0.32/-7.86 | 50.2 | 343 | 0.0657 | 0.998 (21.53) | 1.0 | 0.3981 | 0.503 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1037 | sectors|donchian(entry_n=55,exit_n=10)+trend_sma(n=200) | 8.56/0.65/-5.2 | 50.2 | 272 | 0.0773 | 0.99001 (21.88) | 1.0 | 0.6198 | 0.5005 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1038 | sectors|donchian(entry_n=55,exit_n=20)+trend_sma(n=200) | 9.0/0.58/-5.86 | 50.2 | 223 | 0.0749 | 0.99201 (21.84) | 1.0 | 0.5734 | 0.508 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
