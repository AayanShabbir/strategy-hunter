# gen_2410240519_000 — engine run 20261024_051244_gen_2410240519_000

Hypothesis: grammar draw seed=2410240519: drop_revert+rsi_band

**0/8 pass.** Ledger N at evaluation: 1842. PBO (CSCV) across family: 0.448. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 08304097483df4fed10330fbf8c8939c4a35f4716000bd3eaca813984d0e882a. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1835 | crypto|drop_revert(drop=0.05,hold=3,n=1)+rsi_band(hi=80) | 2.0/0.18/-24.25 | 434.62 | 251 | 0.0126 | 0.89411 (122.65) | 1.0 | 0.0736 | 0.904 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 1836 | crypto|drop_revert(drop=0.05,hold=3,n=5)+rsi_band(hi=80) | -8.1/0.03/-34.55 | 434.62 | 265 | 0.0154 | 0.96104 (101.29) | 1.0 | 0.0531 | 0.9175 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1837 | crypto|drop_revert(drop=0.05,hold=10,n=1)+rsi_band(hi=80) | -24.09/-0.28/-39.44 | 434.62 | 130 | 0.0162 | 0.997 (108.45) | 1.0 | 0.0238 | 0.9225 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 1838 | crypto|drop_revert(drop=0.05,hold=10,n=5)+rsi_band(hi=80) | 32.98/0.65/-40.72 | 434.62 | 135 | 0.0172 | 0.68731 (71.98) | 1.0 | 0.1886 | 0.8855 | False | beats_buy_hold, walk_forward, holm, dsr, spa |
| 1839 | crypto|drop_revert(drop=0.1,hold=3,n=1)+rsi_band(hi=80) | 11.68/0.77/-5.29 | 434.62 | 61 | 0.01 | 0.84116 (69.66) | 1.0 | 0.1797 | 0.8985 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1840 | crypto|drop_revert(drop=0.1,hold=3,n=5)+rsi_band(hi=80) | 17.61/0.53/-22.52 | 434.62 | 152 | 0.0118 | 0.81319 (187.41) | 1.0 | 0.1511 | 0.8935 | False | beats_buy_hold, holm, dsr, spa |
| 1841 | crypto|drop_revert(drop=0.1,hold=10,n=1)+rsi_band(hi=80) | -3.05/-0.0/-21.5 | 434.62 | 50 | 0.0106 | 0.94605 (196.53) | 1.0 | 0.0488 | 0.9065 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 1842 | crypto|drop_revert(drop=0.1,hold=10,n=5)+rsi_band(hi=80) | 37.03/0.79/-29.19 | 434.62 | 113 | 0.0131 | 0.66334 (93.38) | 1.0 | 0.2375 | 0.874 | False | beats_buy_hold, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
