# gen_2610240808_000 — engine run 20261024_080402_gen_2610240808_000

Hypothesis: grammar draw seed=2610240808: donchian+rsi_band

**0/4 pass.** Ledger N at evaluation: 2170. PBO (CSCV) across family: 0.579. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 b035e50230d95cce6a11ae93b5d016debf736c250954e07b320c7c4ec38a8e2a. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2167 | crypto|donchian(entry_n=20,exit_n=10)+rsi_band(hi=80) | 197.99/0.81/-35.0 | 428.6 | 1994 | 0.1011 | 0.35265 (106.38) | 1.0 | 0.9096 | 0.5085 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2168 | crypto|donchian(entry_n=20,exit_n=20)+rsi_band(hi=80) | 185.89/0.8/-46.24 | 428.6 | 1618 | 0.0983 | 0.4046 (146.76) | 1.0 | 0.9014 | 0.5015 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 2169 | crypto|donchian(entry_n=100,exit_n=10)+rsi_band(hi=80) | 302.2/0.91/-14.37 | 428.6 | 963 | 0.0961 | 0.17183 (66.37) | 1.0 | 0.9643 | 0.904 | False | beats_buy_hold, cost_stop, holm, spa, pbo |
| 2170 | crypto|donchian(entry_n=100,exit_n=20)+rsi_band(hi=80) | 302.89/0.92/-22.62 | 428.6 | 833 | 0.0947 | 0.18881 (92.05) | 1.0 | 0.9637 | 0.9115 | False | beats_buy_hold, cost_stop, holm, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
