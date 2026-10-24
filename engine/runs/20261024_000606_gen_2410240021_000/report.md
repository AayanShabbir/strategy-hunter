# gen_2410240021_000 — engine run 20261024_000606_gen_2410240021_000

Hypothesis: grammar draw seed=2410240021: supertrend+rsi_band

**0/4 pass.** Ledger N at evaluation: 1330. PBO (CSCV) across family: 0.425. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 fca3039385b1c3c17edfd753b87580db4c3040f5f2fe0a569252227a8663c832. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1327 | sectors|supertrend(atr_n=10,mult=3)+rsi_band(hi=60) | 6.5/0.47/-5.81 | 50.2 | 1285 | 0.0743 | 0.97602 (17.75) | 1.0 | 0.3822 | 0.5055 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1328 | sectors|supertrend(atr_n=10,mult=4)+rsi_band(hi=60) | 1.39/0.12/-6.64 | 50.2 | 1072 | 0.0781 | 0.998 (18.7) | 1.0 | 0.1843 | 0.5075 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1329 | sectors|supertrend(atr_n=14,mult=3)+rsi_band(hi=60) | 7.05/0.48/-6.44 | 50.2 | 1303 | 0.0741 | 0.96803 (18.08) | 1.0 | 0.3865 | 0.498 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1330 | sectors|supertrend(atr_n=14,mult=4)+rsi_band(hi=60) | 1.98/0.16/-7.61 | 50.2 | 1115 | 0.0765 | 1.0 (18.49) | 1.0 | 0.2023 | 0.512 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
