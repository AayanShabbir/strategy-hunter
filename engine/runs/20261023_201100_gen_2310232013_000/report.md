# gen_2310232013_000 — engine run 20261023_201100_gen_2310232013_000

Hypothesis: grammar draw seed=2310232013: sma_cross+vol_regime

**0/4 pass.** Ledger N at evaluation: 826. PBO (CSCV) across family: 0.491. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 d7e97c82a1eca8cacfeb292bfd952229a436e1388a931b88a1c9d8559b01b10d. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 823 | defensive|sma_cross(fast=20,slow=50)+vol_regime(max_atr_pct=0.02) | 37.47/1.69/-4.97 | 104.36 | 140 | 0.052 | 0.61638 (41.59) | 1.0 | 0.9876 | 0.5005 | False | beats_buy_hold, cost_stop, holm, spa |
| 824 | defensive|sma_cross(fast=20,slow=200)+vol_regime(max_atr_pct=0.02) | 43.79/1.88/-4.06 | 104.36 | 105 | 0.0511 | 0.4975 (43.4) | 1.0 | 0.9947 | 0.501 | False | beats_buy_hold, cost_stop, holm, spa |
| 825 | defensive|sma_cross(fast=50,slow=50)+vol_regime(max_atr_pct=0.02) | 0.0/0.0/0.0 | 104.36 | 0 | inf | 1.0 (56.9) | 1.0 | 0.0 | 0.502 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 826 | defensive|sma_cross(fast=50,slow=200)+vol_regime(max_atr_pct=0.02) | 43.73/1.92/-4.28 | 104.36 | 97 | 0.0511 | 0.45954 (41.69) | 1.0 | 0.9957 | 0.5075 | False | beats_buy_hold, min_trades, cost_stop, holm, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
