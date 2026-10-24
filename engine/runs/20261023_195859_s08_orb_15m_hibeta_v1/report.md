# s08_orb_15m_hibeta_v1 — engine run 20261023_195859_s08_orb_15m_hibeta_v1

Hypothesis: Opening-range breakout (Zarattini & Aziz 2023, SSRN 4416622 'Can Day Trading Really Be Profitable?'; Crabel 1990): on high-beta liquid names, going long when a 15m close breaks the prior 2- or 4-bar high during 09:45 to 10:30/11:30 ET on above-average volume (relvol >= 1.5), exiting on a 8-bar low or session end, flat by close, beats buy-and-hold after 5 bps/side. Distinct from s01 (last half hour) and s06 (RSI dips). Session filter mandatory. 8x ATR stop for cost <= 3% of stop. Pre-registered 2026-10-23.

**0/4 pass.** Ledger N at evaluation: 687. PBO (CSCV) across family: 0.695. Window 2024-09-03..2025-10-22 (pre-vault), OOS from 2025-06-23.
Spec sha256 89e4b879bd6397ce6fd7bacf89203d9314ea6c1342c23f71b3c69721a80328f7. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 684 | HIBETA|donchian(entry_n=2,exit_n=8)+session(end=10:30,start=09:45)+relvol(min_ratio=1.5,n=20) | 0.88/3.05/-0.14 | -2.96 | 90 | 0.0194 | 0.2028 (-2.33) | 1.0 | 0.9946 | 0.4125 | False | min_trades, holm, spa, pbo |
| 685 | HIBETA|donchian(entry_n=2,exit_n=8)+session(end=11:30,start=09:45)+relvol(min_ratio=1.5,n=20) | 0.93/3.01/-0.14 | -2.96 | 110 | 0.0194 | 0.17283 (-2.63) | 1.0 | 0.9924 | 0.413 | False | holm, spa, pbo |
| 686 | HIBETA|donchian(entry_n=4,exit_n=8)+session(end=10:30,start=09:45)+relvol(min_ratio=1.5,n=20) | 0.88/3.05/-0.14 | -2.96 | 83 | 0.0195 | 0.1978 (-2.71) | 1.0 | 0.9946 | 0.4125 | False | min_trades, holm, spa, pbo |
| 687 | HIBETA|donchian(entry_n=4,exit_n=8)+session(end=11:30,start=09:45)+relvol(min_ratio=1.5,n=20) | 0.93/3.01/-0.14 | -2.96 | 100 | 0.0198 | 0.1998 (-2.86) | 1.0 | 0.9924 | 0.413 | False | holm, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
