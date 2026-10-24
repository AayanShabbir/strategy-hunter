# gen_2410240415_000 — engine run 20261024_041006_gen_2410240415_000

Hypothesis: grammar draw seed=2410240415: supertrend+vol_regime

**0/4 pass.** Ledger N at evaluation: 1742. PBO (CSCV) across family: 0.249. Window 2020-07-27..2025-10-22 (pre-vault), OOS from 2024-03-25.
Spec sha256 b075505c7b558c18baca7f5a32f9251fc8a5a33d020290cea1ee70cdeb7063e7. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1739 | MEGA|supertrend(atr_n=7,mult=2)+vol_regime(max_atr_pct=0.06) | -0.7/0.05/-20.28 | 26.86 | 6944 | 0.1268 | 0.86813 (-9.28) | 1.0 | 0.2491 | 0.8815 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1740 | MEGA|supertrend(atr_n=7,mult=3)+vol_regime(max_atr_pct=0.06) | 5.85/0.32/-14.89 | 26.86 | 6332 | 0.1288 | 0.77522 (-7.53) | 1.0 | 0.3402 | 0.8585 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1741 | MEGA|supertrend(atr_n=10,mult=2)+vol_regime(max_atr_pct=0.06) | 1.98/0.16/-19.16 | 26.86 | 6990 | 0.1269 | 0.77922 (-9.11) | 1.0 | 0.3003 | 0.8575 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1742 | MEGA|supertrend(atr_n=10,mult=3)+vol_regime(max_atr_pct=0.06) | -4.35/-0.08/-18.37 | 26.86 | 6323 | 0.1292 | 0.77822 (-7.22) | 1.0 | 0.1926 | 0.9285 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
