# gen_2610240811_000 — engine run 20261024_080412_gen_2610240811_000

Hypothesis: grammar draw seed=2610240811: rsi_revert+vol_regime

**0/8 pass.** Ledger N at evaluation: 2186. PBO (CSCV) across family: 0.254. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 cc1c34a66bcb4892531bbb767a6f47a27b88acaad754b3f3cde9b3dab18bbfbf. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2179 | BROAD|rsi_revert(entry=10,exit=60,n=2)+vol_regime(max_atr_pct=0.04) | 17.93/1.01/-4.3 | 5.92 | 448 | 0.053 | 0.10589 (0.58) | 1.0 | 0.4172 | 0.4015 | False | cost_stop, holm, dsr, spa |
| 2180 | BROAD|rsi_revert(entry=10,exit=60,n=3)+vol_regime(max_atr_pct=0.04) | 18.46/1.36/-4.15 | 5.92 | 180 | 0.0495 | 0.0999 (1.28) | 1.0 | 0.6774 | 0.399 | False | cost_stop, holm, dsr, spa |
| 2181 | BROAD|rsi_revert(entry=10,exit=70,n=2)+vol_regime(max_atr_pct=0.04) | 22.42/1.11/-4.19 | 5.92 | 432 | 0.0526 | 0.04795 (-0.4) | 1.0 | 0.493 | 0.357 | False | cost_stop, holm, dsr, spa |
| 2182 | BROAD|rsi_revert(entry=10,exit=70,n=3)+vol_regime(max_atr_pct=0.04) | 25.28/1.6/-3.88 | 5.92 | 174 | 0.0476 | 0.04895 (1.99) | 1.0 | 0.8206 | 0.322 | False | cost_stop, holm, dsr, spa |
| 2183 | BROAD|rsi_revert(entry=20,exit=60,n=2)+vol_regime(max_atr_pct=0.04) | 19.15/0.89/-5.83 | 5.92 | 704 | 0.0539 | 0.07992 (-1.06) | 1.0 | 0.3392 | 0.3895 | False | cost_stop, holm, dsr, spa |
| 2184 | BROAD|rsi_revert(entry=20,exit=60,n=3)+vol_regime(max_atr_pct=0.04) | 32.22/1.46/-4.52 | 5.92 | 399 | 0.0524 | 0.01499 (0.9) | 1.0 | 0.7312 | 0.266 | False | cost_stop, holm, dsr, spa |
| 2185 | BROAD|rsi_revert(entry=20,exit=70,n=2)+vol_regime(max_atr_pct=0.04) | 23.16/0.99/-6.21 | 5.92 | 659 | 0.0534 | 0.04795 (-0.86) | 1.0 | 0.4042 | 0.348 | False | cost_stop, holm, dsr, spa |
| 2186 | BROAD|rsi_revert(entry=20,exit=70,n=3)+vol_regime(max_atr_pct=0.04) | 47.31/1.78/-4.14 | 5.92 | 365 | 0.0522 | 0.003 (-0.1) | 1.0 | 0.8794 | 0.142 | False | cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
