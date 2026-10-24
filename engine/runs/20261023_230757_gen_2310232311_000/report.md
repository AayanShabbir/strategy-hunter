# gen_2310232311_000 — engine run 20261023_230757_gen_2310232311_000

Hypothesis: grammar draw seed=2310232311: drop_revert+day_of_week

**0/32 pass.** Ledger N at evaluation: 1162. PBO (CSCV) across family: 0.729. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 fc01028d05ba572d84a434ba6bc7210d50f752bd58a81ecbb01543aa05c1f4c2. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1131 | sectors|drop_revert(drop=0.05,hold=3,n=3)+day_of_week(days=0) | -2.59/-0.24/-6.56 | 64.05 | 97 | 0.0348 | 0.996 (28.22) | 1.0 | 0.0001 | 0.5045 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1132 | sectors|drop_revert(drop=0.05,hold=3,n=3)+day_of_week(days=1) | 4.58/0.26/-4.44 | 64.05 | 95 | 0.0347 | 0.97003 (28.35) | 1.0 | 0.0019 | 0.496 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa, pbo |
| 1133 | sectors|drop_revert(drop=0.05,hold=3,n=3)+day_of_week(days=2) | -3.12/-0.41/-4.52 | 64.05 | 93 | 0.0344 | 0.99401 (28.15) | 1.0 | 0.0002 | 0.5075 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1134 | sectors|drop_revert(drop=0.05,hold=3,n=3)+day_of_week(days=3) | -0.14/0.0/-5.57 | 64.05 | 92 | 0.0332 | 0.98601 (27.96) | 1.0 | 0.0022 | 0.5065 | False | oos_positive, beats_buy_hold, min_trades, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1135 | sectors|drop_revert(drop=0.05,hold=3,n=5)+day_of_week(days=0) | -2.97/-0.27/-6.6 | 64.05 | 131 | 0.0387 | 0.996 (27.78) | 1.0 | 0.0001 | 0.506 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1136 | sectors|drop_revert(drop=0.05,hold=3,n=5)+day_of_week(days=1) | 1.41/0.1/-7.71 | 64.05 | 142 | 0.0378 | 0.98501 (27.55) | 1.0 | 0.0022 | 0.4945 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1137 | sectors|drop_revert(drop=0.05,hold=3,n=5)+day_of_week(days=2) | -6.21/-0.78/-7.18 | 64.05 | 139 | 0.0383 | 0.999 (27.47) | 1.0 | 0.0 | 0.5105 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1138 | sectors|drop_revert(drop=0.05,hold=3,n=5)+day_of_week(days=3) | -4.14/-0.38/-8.31 | 64.05 | 133 | 0.0363 | 0.999 (27.44) | 1.0 | 0.0001 | 0.5045 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1139 | sectors|drop_revert(drop=0.05,hold=10,n=3)+day_of_week(days=0) | -0.46/-0.02/-7.41 | 64.05 | 224 | 0.0351 | 0.98202 (27.3) | 1.0 | 0.0019 | 0.5045 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1140 | sectors|drop_revert(drop=0.05,hold=10,n=3)+day_of_week(days=1) | 5.66/0.3/-5.0 | 64.05 | 241 | 0.036 | 0.94206 (27.3) | 1.0 | 0.0025 | 0.4915 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1141 | sectors|drop_revert(drop=0.05,hold=10,n=3)+day_of_week(days=2) | -6.62/-0.69/-9.17 | 64.05 | 233 | 0.0357 | 0.999 (26.52) | 1.0 | 0.0 | 0.515 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1142 | sectors|drop_revert(drop=0.05,hold=10,n=3)+day_of_week(days=3) | 7.18/0.58/-5.57 | 64.05 | 234 | 0.0356 | 0.93107 (27.05) | 1.0 | 0.0387 | 0.5045 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1143 | sectors|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=0) | -2.66/-0.19/-7.41 | 64.05 | 290 | 0.0379 | 0.99301 (26.28) | 1.0 | 0.0004 | 0.5055 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1144 | sectors|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=1) | 5.38/0.28/-6.61 | 64.05 | 306 | 0.0385 | 0.94605 (25.85) | 1.0 | 0.0026 | 0.4945 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1145 | sectors|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=2) | -5.8/-0.54/-8.53 | 64.05 | 313 | 0.0386 | 0.997 (25.96) | 1.0 | 0.0001 | 0.516 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa, pbo |
| 1146 | sectors|drop_revert(drop=0.05,hold=10,n=5)+day_of_week(days=3) | 4.16/0.35/-5.57 | 64.05 | 315 | 0.0383 | 0.94306 (26.71) | 1.0 | 0.0142 | 0.506 | False | beats_buy_hold, cost_stop, holm, dsr, spa, pbo |
| 1147 | sectors|drop_revert(drop=0.15,hold=3,n=3)+day_of_week(days=0) | -2.41/-0.75/-2.41 | 64.05 | 6 | 0.0211 | 0.96004 (30.87) | 1.0 | 0.0 | 0.5035 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1148 | sectors|drop_revert(drop=0.15,hold=3,n=3)+day_of_week(days=1) | 2.37/0.41/-0.88 | 64.05 | 5 | 0.0232 | 0.88911 (32.05) | 1.0 | 0.0011 | 0.496 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1149 | sectors|drop_revert(drop=0.15,hold=3,n=3)+day_of_week(days=2) | -1.23/-0.52/-1.36 | 64.05 | 6 | 0.0172 | 0.95704 (31.93) | 1.0 | 0.0 | 0.504 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1150 | sectors|drop_revert(drop=0.15,hold=3,n=3)+day_of_week(days=3) | 0.0/0.0/0.0 | 64.05 | 5 | 0.0127 | 1.0 (22.1) | 1.0 | 0.0 | 0.5015 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1151 | sectors|drop_revert(drop=0.15,hold=3,n=5)+day_of_week(days=0) | -2.41/-0.75/-2.41 | 64.05 | 12 | 0.0149 | 0.94406 (27.3) | 1.0 | 0.0 | 0.5035 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1152 | sectors|drop_revert(drop=0.15,hold=3,n=5)+day_of_week(days=1) | 2.37/0.41/-0.88 | 64.05 | 12 | 0.0185 | 0.87313 (31.21) | 1.0 | 0.0011 | 0.496 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1153 | sectors|drop_revert(drop=0.15,hold=3,n=5)+day_of_week(days=2) | -1.23/-0.52/-1.36 | 64.05 | 7 | 0.0211 | 0.96603 (31.93) | 1.0 | 0.0 | 0.504 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1154 | sectors|drop_revert(drop=0.15,hold=3,n=5)+day_of_week(days=3) | 1.42/0.82/0.0 | 64.05 | 8 | 0.0183 | 0.88911 (31.6) | 1.0 | 0.002 | 0.4985 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1155 | sectors|drop_revert(drop=0.15,hold=10,n=3)+day_of_week(days=0) | -1.61/-0.48/-2.45 | 64.05 | 16 | 0.0203 | 0.96204 (28.09) | 1.0 | 0.0 | 0.505 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1156 | sectors|drop_revert(drop=0.15,hold=10,n=3)+day_of_week(days=1) | 2.68/0.46/-0.88 | 64.05 | 15 | 0.0202 | 0.84615 (30.36) | 1.0 | 0.001 | 0.4965 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1157 | sectors|drop_revert(drop=0.15,hold=10,n=3)+day_of_week(days=2) | -1.32/-0.5/-1.36 | 64.05 | 12 | 0.0201 | 0.95205 (32.84) | 1.0 | 0.0 | 0.505 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1158 | sectors|drop_revert(drop=0.15,hold=10,n=3)+day_of_week(days=3) | 1.47/0.75/-0.36 | 64.05 | 12 | 0.0187 | 0.88611 (30.53) | 1.0 | 0.0135 | 0.4985 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1159 | sectors|drop_revert(drop=0.15,hold=10,n=5)+day_of_week(days=0) | -1.61/-0.48/-2.45 | 64.05 | 19 | 0.0161 | 0.94705 (29.03) | 1.0 | 0.0 | 0.505 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1160 | sectors|drop_revert(drop=0.15,hold=10,n=5)+day_of_week(days=1) | 2.61/0.45/-0.94 | 64.05 | 20 | 0.019 | 0.86314 (30.69) | 1.0 | 0.0012 | 0.4965 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1161 | sectors|drop_revert(drop=0.15,hold=10,n=5)+day_of_week(days=2) | -1.32/-0.5/-1.36 | 64.05 | 19 | 0.0156 | 0.97303 (27.38) | 1.0 | 0.0 | 0.505 | False | oos_positive, beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |
| 1162 | sectors|drop_revert(drop=0.15,hold=10,n=5)+day_of_week(days=3) | 1.47/0.75/-0.36 | 64.05 | 21 | 0.0178 | 0.87313 (26.11) | 1.0 | 0.0135 | 0.4985 | False | beats_buy_hold, min_trades, walk_forward, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
