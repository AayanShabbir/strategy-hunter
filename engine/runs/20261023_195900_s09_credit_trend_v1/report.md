# s09_credit_trend_v1 — engine run 20261023_195900_s09_credit_trend_v1

Hypothesis: Bond/credit time-series momentum (Hurst, Ooi & Pedersen 2017 'A Century of Evidence on Trend-Following'; Moskowitz, Ooi & Pedersen 2012): holding credit ETFs (HY, EM debt, IG) only while price > its 50/100/200-day SMA beats buy-and-hold of the same basket OOS after 5 bps/side, by sidestepping credit-spread blowouts. New universe (s05 used TLT/IEF, not credit). Low ETF volatility, so a 10x ATR stop is pre-registered to meet cost <= 3% of stop.

**0/3 pass.** Ledger N at evaluation: 690. PBO (CSCV) across family: 0.861. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 682d1e33d67a70d93d2360e6f5340a5ffb0610d4bfe76eb44bded0e569a8a1ee. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 688 | CREDIT|sma_cross(fast=1,slow=50) | 11.75/0.74/-8.37 | 32.7 | 289 | 0.0199 | 0.52348 (12.25) | 1.0 | 0.7435 | 0.4815 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 689 | CREDIT|sma_cross(fast=1,slow=100) | 9.95/0.61/-8.42 | 32.7 | 177 | 0.0183 | 0.81618 (13.58) | 1.0 | 0.6627 | 0.4975 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 690 | CREDIT|sma_cross(fast=1,slow=200) | 14.39/0.84/-5.42 | 32.7 | 115 | 0.0154 | 0.43057 (13.78) | 1.0 | 0.7923 | 0.5195 | False | beats_buy_hold, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
