# gen_2310232331_002 — engine run 20261023_230833_gen_2310232331_002

Hypothesis: grammar draw seed=2310232331: rsi_revert+day_of_week

**0/40 pass.** Ledger N at evaluation: 1254. PBO (CSCV) across family: 0.351. Window 2021-01-01..2025-10-22 (pre-vault), OOS from 2024-05-14.
Spec sha256 a0a2c0b5f2a7971e5c117464a837b0bb38499887ebeeaeaff3d4ba8f227a59a5. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1215 | crypto|rsi_revert(entry=10,exit=60,n=2)+day_of_week(days=0) | -14.57/-0.91/-17.12 | 428.6 | 970 | 0.1017 | 0.95405 (169.18) | 1.0 | 0.0 | 0.916 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1216 | crypto|rsi_revert(entry=10,exit=60,n=2)+day_of_week(days=1) | -11.08/-0.75/-14.59 | 428.6 | 925 | 0.0906 | 0.94306 (133.31) | 1.0 | 0.0 | 0.91 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1217 | crypto|rsi_revert(entry=10,exit=60,n=2)+day_of_week(days=2) | 13.48/1.31/-6.06 | 428.6 | 942 | 0.0938 | 0.77722 (171.22) | 1.0 | 0.0245 | 0.902 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1218 | crypto|rsi_revert(entry=10,exit=60,n=2)+day_of_week(days=3) | -9.03/-0.59/-11.56 | 428.6 | 951 | 0.09 | 0.93506 (91.41) | 1.0 | 0.0 | 0.9125 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1219 | crypto|rsi_revert(entry=10,exit=60,n=2)+day_of_week(days=4) | -4.71/-0.43/-6.42 | 428.6 | 908 | 0.091 | 0.91808 (95.46) | 1.0 | 0.0 | 0.913 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1220 | crypto|rsi_revert(entry=10,exit=60,n=3)+day_of_week(days=0) | -1.96/-0.09/-10.87 | 428.6 | 468 | 0.0967 | 0.92208 (210.43) | 1.0 | 0.0001 | 0.9105 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1221 | crypto|rsi_revert(entry=10,exit=60,n=3)+day_of_week(days=1) | -8.43/-0.65/-12.14 | 428.6 | 414 | 0.0916 | 0.95704 (69.64) | 1.0 | 0.0 | 0.911 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1222 | crypto|rsi_revert(entry=10,exit=60,n=3)+day_of_week(days=2) | 6.32/0.91/-4.88 | 428.6 | 414 | 0.0884 | 0.87413 (192.63) | 1.0 | 0.008 | 0.907 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1223 | crypto|rsi_revert(entry=10,exit=60,n=3)+day_of_week(days=3) | 2.11/0.28/-6.45 | 428.6 | 413 | 0.087 | 0.9031 (99.46) | 1.0 | 0.0007 | 0.9075 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1224 | crypto|rsi_revert(entry=10,exit=60,n=3)+day_of_week(days=4) | 6.02/0.57/-7.04 | 428.6 | 413 | 0.0819 | 0.87213 (83.45) | 1.0 | 0.0016 | 0.907 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1225 | crypto|rsi_revert(entry=10,exit=70,n=2)+day_of_week(days=0) | -12.84/-0.67/-17.04 | 428.6 | 946 | 0.1016 | 0.95504 (82.96) | 1.0 | 0.0 | 0.9165 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1226 | crypto|rsi_revert(entry=10,exit=70,n=2)+day_of_week(days=1) | -9.78/-0.64/-15.01 | 428.6 | 892 | 0.0902 | 0.94406 (180.41) | 1.0 | 0.0 | 0.9105 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1227 | crypto|rsi_revert(entry=10,exit=70,n=2)+day_of_week(days=2) | 19.84/1.7/-6.19 | 428.6 | 926 | 0.0933 | 0.71329 (87.96) | 1.0 | 0.0544 | 0.899 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1228 | crypto|rsi_revert(entry=10,exit=70,n=2)+day_of_week(days=3) | -10.48/-0.65/-14.05 | 428.6 | 927 | 0.0902 | 0.94505 (112.8) | 1.0 | 0.0 | 0.914 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1229 | crypto|rsi_revert(entry=10,exit=70,n=2)+day_of_week(days=4) | 3.26/0.29/-6.59 | 428.6 | 896 | 0.0909 | 0.86713 (175.3) | 1.0 | 0.0006 | 0.909 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1230 | crypto|rsi_revert(entry=10,exit=70,n=3)+day_of_week(days=0) | -3.47/-0.16/-13.34 | 428.6 | 480 | 0.0981 | 0.91708 (84.99) | 1.0 | 0.0 | 0.9105 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1231 | crypto|rsi_revert(entry=10,exit=70,n=3)+day_of_week(days=1) | -6.19/-0.43/-14.08 | 428.6 | 438 | 0.0903 | 0.93906 (83.08) | 1.0 | 0.0 | 0.9095 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1232 | crypto|rsi_revert(entry=10,exit=70,n=3)+day_of_week(days=2) | 11.51/1.5/-5.35 | 428.6 | 427 | 0.0894 | 0.84216 (72.2) | 1.0 | 0.0404 | 0.9015 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1233 | crypto|rsi_revert(entry=10,exit=70,n=3)+day_of_week(days=3) | -3.52/-0.3/-9.46 | 428.6 | 428 | 0.0865 | 0.94106 (153.34) | 1.0 | 0.0 | 0.911 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1234 | crypto|rsi_revert(entry=10,exit=70,n=3)+day_of_week(days=4) | 1.08/0.13/-11.56 | 428.6 | 426 | 0.0846 | 0.91508 (102.75) | 1.0 | 0.0004 | 0.9115 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1235 | crypto|rsi_revert(entry=20,exit=60,n=2)+day_of_week(days=0) | -22.69/-1.18/-27.76 | 428.6 | 1548 | 0.1027 | 0.97602 (149.58) | 1.0 | 0.0 | 0.92 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1236 | crypto|rsi_revert(entry=20,exit=60,n=2)+day_of_week(days=1) | -11.59/-0.61/-15.49 | 428.6 | 1573 | 0.0937 | 0.92707 (133.3) | 1.0 | 0.0 | 0.912 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1237 | crypto|rsi_revert(entry=20,exit=60,n=2)+day_of_week(days=2) | 22.27/1.61/-5.44 | 428.6 | 1542 | 0.0922 | 0.65834 (66.45) | 1.0 | 0.0437 | 0.8955 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1238 | crypto|rsi_revert(entry=20,exit=60,n=2)+day_of_week(days=3) | -17.06/-1.04/-18.19 | 428.6 | 1547 | 0.0912 | 0.93606 (79.99) | 1.0 | 0.0 | 0.9185 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1239 | crypto|rsi_revert(entry=20,exit=60,n=2)+day_of_week(days=4) | -4.73/-0.3/-9.69 | 428.6 | 1462 | 0.0923 | 0.87812 (96.16) | 1.0 | 0.0 | 0.9115 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1240 | crypto|rsi_revert(entry=20,exit=60,n=3)+day_of_week(days=0) | -12.33/-0.59/-18.54 | 428.6 | 889 | 0.1017 | 0.95504 (77.5) | 1.0 | 0.0 | 0.9165 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1241 | crypto|rsi_revert(entry=20,exit=60,n=3)+day_of_week(days=1) | -9.17/-0.53/-14.37 | 428.6 | 849 | 0.0904 | 0.92807 (76.33) | 1.0 | 0.0 | 0.9105 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1242 | crypto|rsi_revert(entry=20,exit=60,n=3)+day_of_week(days=2) | 16.05/1.4/-5.72 | 428.6 | 893 | 0.0941 | 0.76224 (83.12) | 1.0 | 0.0269 | 0.9015 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1243 | crypto|rsi_revert(entry=20,exit=60,n=3)+day_of_week(days=3) | -15.63/-1.12/-19.61 | 428.6 | 882 | 0.0902 | 0.96503 (74.72) | 1.0 | 0.0 | 0.9175 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1244 | crypto|rsi_revert(entry=20,exit=60,n=3)+day_of_week(days=4) | 5.26/0.43/-7.26 | 428.6 | 826 | 0.0886 | 0.84515 (167.1) | 1.0 | 0.0012 | 0.9085 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1245 | crypto|rsi_revert(entry=20,exit=70,n=2)+day_of_week(days=0) | -20.97/-0.95/-28.89 | 428.6 | 1436 | 0.1043 | 0.96903 (181.03) | 1.0 | 0.0 | 0.9195 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1246 | crypto|rsi_revert(entry=20,exit=70,n=2)+day_of_week(days=1) | -6.6/-0.29/-12.86 | 428.6 | 1440 | 0.093 | 0.88112 (88.11) | 1.0 | 0.0 | 0.9105 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1247 | crypto|rsi_revert(entry=20,exit=70,n=2)+day_of_week(days=2) | 28.57/1.78/-6.94 | 428.6 | 1444 | 0.0931 | 0.61638 (93.2) | 1.0 | 0.0578 | 0.8925 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1248 | crypto|rsi_revert(entry=20,exit=70,n=2)+day_of_week(days=3) | -17.5/-0.97/-20.67 | 428.6 | 1448 | 0.0918 | 0.95504 (119.86) | 1.0 | 0.0 | 0.919 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1249 | crypto|rsi_revert(entry=20,exit=70,n=2)+day_of_week(days=4) | 3.7/0.28/-8.73 | 428.6 | 1389 | 0.0927 | 0.8022 (61.87) | 1.0 | 0.0006 | 0.908 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1250 | crypto|rsi_revert(entry=20,exit=70,n=3)+day_of_week(days=0) | -9.39/-0.36/-21.04 | 428.6 | 840 | 0.1019 | 0.94705 (75.93) | 1.0 | 0.0 | 0.9155 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1251 | crypto|rsi_revert(entry=20,exit=70,n=3)+day_of_week(days=1) | -7.58/-0.37/-16.5 | 428.6 | 806 | 0.0915 | 0.93007 (207.47) | 1.0 | 0.0 | 0.91 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1252 | crypto|rsi_revert(entry=20,exit=70,n=3)+day_of_week(days=2) | 17.86/1.36/-7.77 | 428.6 | 839 | 0.093 | 0.73526 (133.87) | 1.0 | 0.0269 | 0.8985 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1253 | crypto|rsi_revert(entry=20,exit=70,n=3)+day_of_week(days=3) | -25.27/-1.63/-26.5 | 428.6 | 825 | 0.0904 | 0.99301 (197.0) | 1.0 | 0.0 | 0.9205 | False | oos_positive, beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1254 | crypto|rsi_revert(entry=20,exit=70,n=3)+day_of_week(days=4) | 6.89/0.49/-8.91 | 428.6 | 795 | 0.0886 | 0.82717 (66.49) | 1.0 | 0.0019 | 0.907 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
