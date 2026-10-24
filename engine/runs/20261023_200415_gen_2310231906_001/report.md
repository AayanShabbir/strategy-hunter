# gen_2310231906_001 — engine run 20261023_200415_gen_2310231906_001

Hypothesis: grammar draw seed=2310231906: drop_revert+rsi_band

**0/8 pass.** Ledger N at evaluation: 726. PBO (CSCV) across family: 0.502. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 cb254a9cebf3ba1f2d44c1b305369ddf11001ae959b121daa4d059a191e5ff20. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 719 | hibeta|drop_revert(drop=0.05,hold=3,n=1)+rsi_band(hi=70) | 114.41/1.16/-18.15 | 809.88 | 494 | 0.0161 | 0.88112 (213.66) | 1.0 | 0.8417 | 0.5115 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 720 | hibeta|drop_revert(drop=0.05,hold=3,n=3)+rsi_band(hi=70) | 178.3/1.3/-27.73 | 809.88 | 630 | 0.0185 | 0.62338 (212.23) | 1.0 | 0.8887 | 0.5145 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 721 | hibeta|drop_revert(drop=0.05,hold=10,n=1)+rsi_band(hi=70) | 247.98/1.36/-25.49 | 809.88 | 297 | 0.019 | 0.28971 (212.9) | 1.0 | 0.9013 | 0.507 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 722 | hibeta|drop_revert(drop=0.05,hold=10,n=3)+rsi_band(hi=70) | 235.41/1.22/-34.49 | 809.88 | 311 | 0.0218 | 0.34565 (216.08) | 1.0 | 0.8468 | 0.499 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 723 | hibeta|drop_revert(drop=0.1,hold=3,n=1)+rsi_band(hi=70) | 50.9/1.53/-4.01 | 809.88 | 87 | 0.0113 | 0.98801 (217.51) | 1.0 | 0.971 | 0.506 | False | beats_buy_hold, min_trades, holm, spa, pbo |
| 724 | hibeta|drop_revert(drop=0.1,hold=3,n=3)+rsi_band(hi=70) | 84.48/1.07/-11.76 | 809.88 | 273 | 0.0143 | 0.94505 (219.64) | 1.0 | 0.8103 | 0.505 | False | beats_buy_hold, holm, dsr, spa, pbo |
| 725 | hibeta|drop_revert(drop=0.1,hold=10,n=1)+rsi_band(hi=70) | 70.79/1.35/-8.91 | 809.88 | 69 | 0.0124 | 0.97403 (225.34) | 1.0 | 0.9115 | 0.493 | False | beats_buy_hold, min_trades, holm, dsr, spa, pbo |
| 726 | hibeta|drop_revert(drop=0.1,hold=10,n=3)+rsi_band(hi=70) | 86.54/0.87/-21.86 | 809.88 | 181 | 0.0157 | 0.94805 (223.11) | 1.0 | 0.6601 | 0.508 | False | beats_buy_hold, holm, dsr, spa, pbo |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
