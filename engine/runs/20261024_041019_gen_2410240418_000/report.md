# gen_2410240418_000 — engine run 20261024_041019_gen_2410240418_000

Hypothesis: grammar draw seed=2410240418: rsi_revert+relvol

**0/8 pass.** Ledger N at evaluation: 1762. PBO (CSCV) across family: 0.403. Window 2016-01-04..2025-10-22 (pre-vault), OOS from 2022-11-09.
Spec sha256 627c726be703a9689bcc8d3eb489d563b7ae0f8fcf46fdf27451a9a0cf9fae4e. Costs {'fee_bps': 0, 'slippage_bps': 5}. min_trades 100.

| # | variant | OOS ret/Sh/DD | B&H OOS | trades | cost/stop | twin p (rand med%) | Holm | DSR | SPA | pass | failed checks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1755 | SECTORS|rsi_revert(entry=5,exit=70,n=3)+relvol(min_ratio=1.2) | 1.27/0.2/-2.25 | 56.34 | 262 | 0.0609 | 1.0 (25.42) | 1.0 | 0.1148 | 0.5005 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1756 | SECTORS|rsi_revert(entry=5,exit=70,n=5)+relvol(min_ratio=1.2) | 1.67/0.75/-0.61 | 56.34 | 60 | 0.0515 | 1.0 (25.69) | 1.0 | 0.4185 | 0.4965 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1757 | SECTORS|rsi_revert(entry=5,exit=80,n=3)+relvol(min_ratio=1.2) | 2.08/0.32/-1.9 | 56.34 | 337 | 0.0593 | 1.0 (24.41) | 1.0 | 0.1539 | 0.499 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1758 | SECTORS|rsi_revert(entry=5,exit=80,n=5)+relvol(min_ratio=1.2) | 2.19/0.93/-0.61 | 56.34 | 93 | 0.0552 | 1.0 (24.55) | 1.0 | 0.5495 | 0.496 | False | beats_buy_hold, min_trades, cost_stop, holm, dsr, spa |
| 1759 | SECTORS|rsi_revert(entry=10,exit=70,n=3)+relvol(min_ratio=1.2) | 5.85/0.38/-2.99 | 56.34 | 675 | 0.0651 | 1.0 (23.98) | 1.0 | 0.1637 | 0.5005 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1760 | SECTORS|rsi_revert(entry=10,exit=70,n=5)+relvol(min_ratio=1.2) | 1.55/0.29/-1.98 | 56.34 | 226 | 0.0522 | 1.0 (25.18) | 1.0 | 0.1461 | 0.5035 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |
| 1761 | SECTORS|rsi_revert(entry=10,exit=80,n=3)+relvol(min_ratio=1.2) | 5.34/0.34/-4.18 | 56.34 | 841 | 0.0639 | 0.999 (23.39) | 1.0 | 0.1535 | 0.505 | False | beats_buy_hold, cost_stop, holm, dsr, spa |
| 1762 | SECTORS|rsi_revert(entry=10,exit=80,n=5)+relvol(min_ratio=1.2) | 2.65/0.38/-2.03 | 56.34 | 372 | 0.0557 | 0.999 (25.17) | 1.0 | 0.172 | 0.5005 | False | beats_buy_hold, cost_stop, walk_forward, holm, dsr, spa |

Bar: all of OOS>0, OOS>B&H, trades>=min, cost/stop<=3%, every walk-forward fold >0, ledger-wide Holm<0.05 on random-entry twin p, DSR>0.95 at ledger N, SPA vs B&H<0.05, PBO<0.5. Survivors may take ONE `hunt vault-test`.
