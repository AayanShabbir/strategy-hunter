# gen_2410240703_000 — engine run 20261024_070453_gen_2410240703_000

Hypothesis: grammar draw seed=2410240703: supertrend

**0/4 pass.** Ledger N at evaluation: 2014. PBO (CSCV) across family: 0.776. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 dbc33d271d902d7557c2bb6ddff94c8cf3be4c418336bb12eb82bcf7378db1f2. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2011 | BROAD|supertrend(atr_n=7,mult=2) | 32.86/1.25/-6.21 | 78.13 | 361 | 0.0821 | 0.41059 (30.94) | 1.0 | 0.9618 | 0.497 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 2012 | BROAD|supertrend(atr_n=7,mult=3) | 35.38/1.26/-7.12 | 78.13 | 210 | 0.081 | 0.33766 (31.78) | 1.0 | 0.9627 | 0.492 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 2013 | BROAD|supertrend(atr_n=10,mult=2) | 29.4/1.12/-7.62 | 78.13 | 365 | 0.0811 | 0.56743 (31.45) | 1.0 | 0.939 | 0.5 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 2014 | BROAD|supertrend(atr_n=10,mult=3) | 34.44/1.21/-7.52 | 78.13 | 215 | 0.0797 | 0.40659 (32.43) | 1.0 | 0.955 | 0.496 | False | beats_buy_hold, cost_stop, holm, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
