# gen_2310232311_003 — engine run 20261023_230809_gen_2310232311_003

Hypothesis: grammar draw seed=2310232311: supertrend

**0/4 pass.** Ledger N at evaluation: 1174. PBO (CSCV) across family: 0.715. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 10581371e63574857e4db2c405509ba5642f1c780499db92bfcd5584f898714d. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1171 | sectors|supertrend(atr_n=10,mult=2) | 21.23/0.7/-11.24 | 64.05 | 213 | 0.0571 | 0.5964 (25.47) | 1.0 | 0.596 | 0.499 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1172 | sectors|supertrend(atr_n=10,mult=3) | 15.56/0.52/-10.92 | 64.05 | 114 | 0.0562 | 0.80619 (26.75) | 1.0 | 0.4778 | 0.501 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1173 | sectors|supertrend(atr_n=14,mult=2) | 22.71/0.73/-11.76 | 64.05 | 216 | 0.0571 | 0.58042 (26.1) | 1.0 | 0.618 | 0.5 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1174 | sectors|supertrend(atr_n=14,mult=3) | 10.77/0.37/-14.75 | 64.05 | 116 | 0.0555 | 0.88012 (27.06) | 1.0 | 0.3764 | 0.5075 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
