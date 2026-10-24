# gen_2310232111_001 — engine run 20261023_210406_gen_2310232111_001

Hypothesis: grammar draw seed=2310232111: supertrend

**0/4 pass.** Ledger N at evaluation: 918. PBO (CSCV) across family: 0.012. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 d3d408584d13d036befb89eda99275ef25efce38e53f5e4d857edb28331b38d1. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 915 | sectors|supertrend(atr_n=7,mult=2) | 15.86/0.7/-8.91 | 50.2 | 602 | 0.0657 | 0.77223 (20.85) | 1.0 | 0.5824 | 0.4915 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 916 | sectors|supertrend(atr_n=7,mult=4) | 9.21/0.45/-7.41 | 50.2 | 244 | 0.0672 | 0.97902 (22.34) | 1.0 | 0.4141 | 0.495 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 917 | sectors|supertrend(atr_n=10,mult=2) | 18.34/0.78/-9.43 | 50.2 | 601 | 0.0657 | 0.62238 (20.64) | 1.0 | 0.6347 | 0.4875 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 918 | sectors|supertrend(atr_n=10,mult=4) | 8.66/0.42/-8.67 | 50.2 | 243 | 0.0666 | 0.99401 (22.11) | 1.0 | 0.3924 | 0.5015 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
