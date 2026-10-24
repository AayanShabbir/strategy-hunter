# gen_2610240809_000 — engine run 20261024_080407_gen_2610240809_000

Hypothesis: grammar draw seed=2610240809: donchian

**0/4 pass.** Ledger N at evaluation: 2174. PBO (CSCV) across family: 0.896. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 2d451de6e9b562521b628ae700ef5f0fd66254b81ea43426286a8ba9dbe032a3. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2171 | crypto|donchian(entry_n=20,exit_n=10) | 6.16/0.29/-23.85 | 56.21 | 48 | 0.0223 | 0.73526 (28.33) | 1.0 | 0.1155 | 0.8935 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 2172 | crypto|donchian(entry_n=20,exit_n=20) | 24.86/0.62/-26.12 | 56.21 | 34 | 0.0221 | 0.50749 (27.16) | 1.0 | 0.2092 | 0.824 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2173 | crypto|donchian(entry_n=55,exit_n=10) | 38.79/1.02/-15.0 | 56.21 | 28 | 0.0218 | 0.3966 (28.03) | 1.0 | 0.3716 | 0.7445 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 2174 | crypto|donchian(entry_n=55,exit_n=20) | 45.08/1.08/-14.84 | 56.21 | 24 | 0.0218 | 0.33566 (27.81) | 1.0 | 0.3991 | 0.7205 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
