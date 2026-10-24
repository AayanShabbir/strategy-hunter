# gen_2410240409_000 — engine run 20261024_040948_gen_2410240409_000

Hypothesis: grammar draw seed=2410240409: rsi_revert+vol_regime

**0/8 pass.** Ledger N at evaluation: 1710. PBO (CSCV) across family: 0.316. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 c45d1d60f2e4b252360c3eae2a725a474626116860650f3f45fc6cb17f883416. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1703 | ALTS|rsi_revert(entry=5,exit=70,n=2)+vol_regime(max_atr_pct=0.06) | 2.15/0.25/-5.19 | 193.2 | 64 | 0.0178 | 0.94406 (116.09) | 1.0 | 0.0398 | 0.897 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1704 | ALTS|rsi_revert(entry=5,exit=70,n=5)+vol_regime(max_atr_pct=0.06) | 0.41/0.35/-0.48 | 193.2 | 3 | 0.017 | 0.99101 (149.91) | 1.0 | 0.0301 | 0.899 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1705 | ALTS|rsi_revert(entry=5,exit=80,n=2)+vol_regime(max_atr_pct=0.06) | 5.31/0.47/-6.1 | 193.2 | 74 | 0.0173 | 0.89411 (54.23) | 1.0 | 0.06 | 0.898 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1706 | ALTS|rsi_revert(entry=5,exit=80,n=5)+vol_regime(max_atr_pct=0.06) | -1.36/-0.39/-3.94 | 193.2 | 8 | 0.0169 | 0.98701 (43.01) | 1.0 | 0.0048 | 0.898 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1707 | ALTS|rsi_revert(entry=10,exit=70,n=2)+vol_regime(max_atr_pct=0.06) | 4.16/0.35/-5.84 | 193.2 | 119 | 0.0183 | 0.93007 (103.15) | 1.0 | 0.0476 | 0.8975 | False | beats_buy_hold, holm, dsr, spa |
| 1708 | ALTS|rsi_revert(entry=10,exit=70,n=5)+vol_regime(max_atr_pct=0.06) | 2.94/1.45/-0.48 | 193.2 | 13 | 0.0172 | 0.97502 (146.62) | 1.0 | 0.3229 | 0.8965 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 1709 | ALTS|rsi_revert(entry=10,exit=80,n=2)+vol_regime(max_atr_pct=0.06) | 6.28/0.44/-7.94 | 193.2 | 128 | 0.0177 | 0.8961 (104.93) | 1.0 | 0.0551 | 0.8975 | False | beats_buy_hold, holm, dsr, spa |
| 1710 | ALTS|rsi_revert(entry=10,exit=80,n=5)+vol_regime(max_atr_pct=0.06) | 4.59/0.61/-8.14 | 193.2 | 25 | 0.017 | 0.94106 (118.75) | 1.0 | 0.094 | 0.892 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
