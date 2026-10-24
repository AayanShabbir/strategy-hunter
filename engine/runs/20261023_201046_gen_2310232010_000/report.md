# gen_2310232010_000 — engine run 20261023_201046_gen_2310232010_000

Hypothesis: grammar draw seed=2310232010: drop_revert+vol_regime

**0/8 pass.** Ledger N at evaluation: 798. PBO (CSCV) across family: 0.272. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 16762eaafeae6cecfe8cc02c069505248c3d88dba51ed64587dcfd125bac273c. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 791 | crypto_d|drop_revert(drop=0.1,hold=3,n=1)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 268.18 | 0 | inf | 0.94705 (214.85) | 1.0 | 0.0 | 0.892 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 792 | crypto_d|drop_revert(drop=0.1,hold=3,n=5)+vol_regime(max_atr_pct=0.04) | 1.09/0.76/-0.48 | 268.18 | 4 | 0.0255 | 0.89111 (176.43) | 1.0 | 0.5559 | 0.89 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 793 | crypto_d|drop_revert(drop=0.1,hold=5,n=1)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 268.18 | 0 | inf | 0.93906 (214.85) | 1.0 | 0.0 | 0.892 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 794 | crypto_d|drop_revert(drop=0.1,hold=5,n=5)+vol_regime(max_atr_pct=0.04) | 0.88/0.46/-1.56 | 268.18 | 4 | 0.0255 | 0.91508 (44.2) | 1.0 | 0.3983 | 0.892 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 795 | crypto_d|drop_revert(drop=0.15,hold=3,n=1)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 268.18 | 0 | inf | 0.93706 (214.85) | 1.0 | 0.0 | 0.892 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 796 | crypto_d|drop_revert(drop=0.15,hold=3,n=5)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 268.18 | 0 | inf | 0.93706 (32.26) | 1.0 | 0.0 | 0.892 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 797 | crypto_d|drop_revert(drop=0.15,hold=5,n=1)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 268.18 | 0 | inf | 0.93407 (214.85) | 1.0 | 0.0 | 0.892 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |
| 798 | crypto_d|drop_revert(drop=0.15,hold=5,n=5)+vol_regime(max_atr_pct=0.04) | 0.0/0.0/0.0 | 268.18 | 0 | inf | 0.92408 (32.26) | 1.0 | 0.0 | 0.892 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
