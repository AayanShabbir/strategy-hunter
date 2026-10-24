# gen_2410240517_000 — engine run 20261024_051238_gen_2410240517_000

Hypothesis: grammar draw seed=2410240517: supertrend+relvol

**0/4 pass.** Ledger N at evaluation: 1826. PBO (CSCV) across family: 0.655. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 55206d85fb383ae7151a89f91f64b9b72b711ff1ebfc939450c75735ce47e770. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1823 | BROAD|supertrend(atr_n=10,mult=3)+relvol(min_ratio=1.2) | -9.11/-0.44/-15.19 | 5.92 | 855 | 0.0575 | 0.67932 (-2.1) | 1.0 | 0.0407 | 0.8005 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1824 | BROAD|supertrend(atr_n=10,mult=4)+relvol(min_ratio=1.2) | -4.52/-0.2/-13.45 | 5.92 | 819 | 0.0573 | 0.55744 (-3.03) | 1.0 | 0.0898 | 0.7355 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1825 | BROAD|supertrend(atr_n=14,mult=3)+relvol(min_ratio=1.2) | -9.61/-0.48/-15.42 | 5.92 | 849 | 0.0576 | 0.67133 (-2.53) | 1.0 | 0.0343 | 0.8095 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1826 | BROAD|supertrend(atr_n=14,mult=4)+relvol(min_ratio=1.2) | -3.18/-0.14/-12.76 | 5.92 | 802 | 0.0571 | 0.56643 (-1.58) | 1.0 | 0.1105 | 0.7235 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
