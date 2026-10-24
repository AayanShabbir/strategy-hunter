# Third-party licenses — research_lab (private, paper-only research)

| Package | Version | License | Source | Use |
|---|---|---|---|---|
| vectorbt (free, not PRO) | 1.2.0 | Apache-2.0 + Commons Clause (no selling a product built on it) | https://github.com/polakowo/vectorbt | backtest engine |
| alpaca-py | 0.44.0 | Apache-2.0 | https://github.com/alpacahq/alpaca-py | market data (paper keys only) |
| pyarrow | 26.0.0 | Apache-2.0 | https://github.com/apache/arrow | parquet cache |
| skfolio | 1.9.11 | BSD-3-Clause | https://github.com/skfolio/skfolio | CombinatorialPurgedCV (CPCV), walk-forward |
| statsmodels | 0.15.0 | BSD-3-Clause | https://github.com/statsmodels/statsmodels | Holm / multipletests |
| arch | 8.0.0 | NCSA (University of Illinois/NCSA) | https://github.com/bashtage/arch | Hansen SPA, bootstrap |
| quantstats | 0.0.86 | Apache-2.0 | https://github.com/ranaroussi/quantstats | tearsheets vs SPY |
| empyrical-reloaded | 0.7.0 | Apache-2.0 | https://github.com/stefan-jansen/empyrical-reloaded | perf metrics |
| pypbo | git 4d723f06498267a2a6280cb9d7d5649348e961d1 (vendored in vendor/pypbo, not on PyPI) | AGPL-3.0 | https://github.com/esvhd/pypbo | PBO (CSCV), DSR, PSR |

Notes: pypbo is AGPL-3.0 — fine for private use; if this code is ever hosted as a service or distributed, its source obligations apply. Full dependency pins: requirements.lock.txt. Original license texts ship inside each package's dist-info (and vendor/pypbo/LICENSE).

## Ideas adapted into Arena v2 prompts (/workspace/arena_v2) — no code copied
| Project | Commit | License | Source | What was adapted |
|---|---|---|---|---|
| claude-trading-skills | e8f5503e9b86d5c2710b0c76b1f686703968c9df | MIT, Copyright (c) 2026 TraderMonty | https://github.com/tradermonty/claude-trading-skills | pre-trade-discipline-gate (GO/NO_GO/REVIEW_REQUIRED checklist), drawdown-circuit-breaker (2% daily, 2-loss cooldown, 5% weekly, 8% monthly, fail closed on bad data), position-sizer (fixed-fractional/ATR/half-Kelly ceiling, sector cap), backtest-expert (stress tests, plateaus, OOS ≥50% IS, ≥30 trades), signal-postmortem idea |
| TradingAgents | cb0f3aadffed6d1089db4b224162c964368baa46 | Apache-2.0 | https://github.com/TauricResearch/TradingAgents | role structure: analyst → bull/bear researcher debate + research manager → trader → aggressive/conservative/neutral risk debate → portfolio manager rating (Buy/Overweight/Hold/Underweight/Sell); memory/reflection |
If any code from these repos is ever copied in, keep the MIT notice (claude-trading-skills) and include the Apache-2.0 LICENSE/NOTICE plus change notes (TradingAgents).

## TA-Lib (added 2026-10-22, Hunt #11 / desk candle_setups.py)
- TA-Lib Python wrapper `TA-Lib` 0.8.2 - BSD-2-Clause - https://github.com/TA-Lib/ta-lib-python (installed from PyPI binary wheel)
- TA-Lib C library (bundled in the wheel) - BSD-3-Clause - https://ta-lib.org / https://github.com/TA-Lib/ta-lib
- Used: CDLENGULFING, CDLHAMMER, CDLSHOOTINGSTAR, EMA, ATR. Unmodified.

## NautilusTrader 1.231.0
LGPL-3.0, (c) Nautech Systems Pty Ltd. https://github.com/nautechsystems/nautilus_trader. Installed unmodified in research_lab/nautilus/.venv (backtest only).

## SDE design credits (no code vendored)
- PyTorch (BSD-3) — tensor/NN runtime for `src/models`.
- AlphaGen (Yu et al., KDD 2023, "Generating Synergistic Formulaic Alpha Collections via RL", MIT) — synergy pool / formulaic alpha idea.
- GFlowNets (Bengio et al. 2021; Malkin et al. 2022 Trajectory Balance) and GFlowNet alpha-mining work (e.g. AlphaSAGE) — Phase 2 design.
- R-GCN (Schlichtkrull et al. 2018); reimplemented in plain torch, PyG not used.
- Benhamou et al. 2026 (anytime-valid e-process promotion) — Phase 4 design.

## SDE Phase 2 (added 2026-10-23)
- AlphaSAGE (Chen et al., ICLR 2026, arXiv:2509.25055; repo BerkinChen/AlphaSAGE has no license file) — algorithm, reward and Table 4 hyper-parameters followed from the paper; **no code copied**.
- Qlib public data via chenditc/investment_data (Apache-2.0) — downloaded to gitignored data/sde/; read with our own binary reader. yfinance (Apache-2.0), akshare (MIT), pandas/numpy/scipy (BSD-3).
