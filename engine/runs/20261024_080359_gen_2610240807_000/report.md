# gen_2610240807_000 — engine run 20261024_080359_gen_2610240807_000

Hypothesis: grammar draw seed=2610240807: drop_revert

**0/8 pass.** Ledger N at evaluation: 2166. PBO (CSCV) across family: 0.206. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 28b3ebfb06b905235e5bae64c5008316fc3dafb817ce081d776439849297426b. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2159 | BROAD|drop_revert(drop=0.05,hold=3,n=1) | -14.73/-0.69/-17.79 | 5.92 | 159 | 0.0202 | 0.88511 (2.74) | 1.0 | 0.0 | 0.8665 | False | oos_positive, beats_buy_hold, walk_forward, holm, dsr, spa |
| 2160 | BROAD|drop_revert(drop=0.05,hold=3,n=5) | 3.68/0.17/-18.78 | 5.92 | 316 | 0.032 | 0.44555 (1.55) | 1.0 | 0.0047 | 0.6075 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2161 | BROAD|drop_revert(drop=0.05,hold=10,n=1) | -8.67/-0.25/-27.86 | 5.92 | 98 | 0.0228 | 0.75325 (2.13) | 1.0 | 0.0005 | 0.803 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2162 | BROAD|drop_revert(drop=0.05,hold=10,n=5) | 5.09/0.19/-19.18 | 5.92 | 208 | 0.0375 | 0.40959 (2.91) | 1.0 | 0.0053 | 0.5715 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 2163 | BROAD|drop_revert(drop=0.15,hold=3,n=1) | -3.05/-0.94/-3.24 | 5.92 | 6 | 0.0118 | 0.60539 (3.23) | 1.0 | 0.0 | 0.682 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2164 | BROAD|drop_revert(drop=0.15,hold=3,n=5) | 3.34/0.3/-6.33 | 5.92 | 36 | 0.0149 | 0.48751 (2.66) | 1.0 | 0.0088 | 0.5995 | False | beats_buy_hold, min_trades, holm, dsr, spa |
| 2165 | BROAD|drop_revert(drop=0.15,hold=10,n=1) | -3.17/-0.72/-3.72 | 5.92 | 5 | 0.0122 | 0.58242 (1.86) | 1.0 | 0.0 | 0.683 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |
| 2166 | BROAD|drop_revert(drop=0.15,hold=10,n=5) | -9.82/-0.59/-17.76 | 5.92 | 28 | 0.0164 | 0.7962 (3.72) | 1.0 | 0.0 | 0.796 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
