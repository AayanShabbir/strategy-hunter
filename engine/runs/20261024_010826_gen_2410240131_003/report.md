# gen_2410240131_003 — engine run 20261024_010826_gen_2410240131_003

Hypothesis: grammar draw seed=2410240131: supertrend+vol_regime

**0/4 pass.** Ledger N at evaluation: 1498. PBO (CSCV) across family: 0.344. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 86011a87fdda13c704d7f401e57ead130c91313abd5b6aa45e338b2fa830f777. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1495 | sectors|supertrend(atr_n=10,mult=2)+vol_regime(max_atr_pct=0.06) | 18.34/0.78/-9.43 | 50.2 | 603 | 0.0656 | 0.60739 (20.75) | 1.0 | 0.838 | 0.4875 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1496 | sectors|supertrend(atr_n=10,mult=3)+vol_regime(max_atr_pct=0.06) | 16.41/0.72/-7.36 | 50.2 | 349 | 0.0645 | 0.79221 (22.04) | 1.0 | 0.8108 | 0.501 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1497 | sectors|supertrend(atr_n=14,mult=2)+vol_regime(max_atr_pct=0.06) | 20.22/0.83/-10.15 | 50.2 | 606 | 0.0653 | 0.53746 (21.31) | 1.0 | 0.8571 | 0.4925 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1498 | sectors|supertrend(atr_n=14,mult=3)+vol_regime(max_atr_pct=0.06) | 16.65/0.7/-8.46 | 50.2 | 353 | 0.063 | 0.76024 (21.5) | 1.0 | 0.8034 | 0.496 | False | beats_buy_hold, cost_stop, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
