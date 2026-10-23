# Crypto research note — spot, long/flat only (Strategy Scout scope, added 2026-10-23)
Research side only. No desk orders, no margin, no shorts (cash-only spot long/flat). Data: Alpaca crypto bars (market data only).

## How to trade crypto systematically — takeaways
1. **24/7 market, define the day explicitly.** No open/close; we use UTC-midnight daily bars (Alpaca's native crypto day). Weekends are real bars. Shen, Urquhart & Wang (2022) had to proxy "open" by volume spikes and "close" by the CME 5 pm ET break — stock session ideas don't port directly.
2. **Costs are 10–50x stocks.** Alpaca crypto is maker/taker by 30-day volume: tier 1 = 0.15% maker / **0.25% taker**, down to 0%/0.10% above $100M. We pre-register 25 bps fee + 10 bps slippage **per side** (~70 bps round trip). Consequence: intraday/hourly rules can't meet the cost <= 3% of stop rule (needs ~23%+ stop). Daily bars with ~5x ATR stops only.
3. **Trend/time-series momentum is the best-documented edge.** Liu & Tsyvinski (2021, RFS) find strong TSMOM in BTC/ETH/XRP at 1–4 week horizons; Liu, Tsyvinski & Wu (2022, JF) find market, size and momentum factors price coins. Hudson & Urquhart (2021) test ~15k technical rules with data-snooping controls: rules work and cut drawdowns, **but BTC showed no out-of-sample predictability** — expect decay.
4. **Mean reversion is mostly a small/illiquid-coin effect.** Kozlowski et al. (2021) find daily-to-monthly reversals across 200 coins, strongest in small/illiquid ones; Zaremba et al. (2021) find the largest, most liquid coins show **daily momentum, not reversal**. So "buy the sharp drop" on SOL is a genuine, likely-to-fail test.
5. **Risk management matters more than signal.** Kurtosis is extreme (crypto momentum ~120); volatility-managed momentum reduces crashes (FMPM 2025; Barroso & Santa-Clara 2015 for equities). The engine has no position sizing, so we proxy with a volatility-regime gate + wide ATR stops. Long/flat drawdown control vs buy-and-hold (-80%+ in 2022) is the main practical benefit.
6. **Weekend effect:** recent BTC evidence (2014–2024) finds no weekend return gap, just lower weekend volatility/volume — not tested as a separate hypothesis.
7. **Funding/regime:** perp funding is a sentiment/leverage gauge, but we can't trade perps (no margin/shorts) and have no funding data in Alpaca; not used.
8. **Backtest pitfalls:** survivorship (only coins listed on Alpaca today; dead coins absent — so we stick to large caps and say so), short histories (SOL on Alpaca from 2021, with gaps: 1,704 daily bars vs 2,122 for BTC; XRP only from 2024, excluded), lookahead (signals on close, fill next open), overfitting (every variant counts in ledger N; Holm/DSR/PBO/SPA), regime dependence (2021 bull, 2022 crash dominate IS). Sharpe in reports annualizes with sqrt(252); crypto would be sqrt(365) — cosmetic, the tests use per-bar returns.

## What was queued (engine/specs/scout/crypto, author: scout)
c01 SOL trend SMA | c02 SOL Donchian breakout | c03 SOL drop-revert | c04 SOL vs BTC/ETH relative strength | c05 short-horizon TSMOM (SOL, alts, BTC+ETH) | c06 Supertrend + vol-regime gate. Baskets: SOL alone; ALTS = SOL, ETH, AVAX, LINK, DOGE, LTC; BTC_ETH. 53 variants total. Vault: bars from 2025-10-23 sealed.
Engine additions (2026-10-23, backups `*.bak_20261023_crypto`): crypto fetch via alpaca-py `CryptoHistoricalDataClient` for `XXX/USD` symbols (cache files `XXX_USD.parquet`, UTC days), ideas `rel_strength(bench, n, abs_filter)` and `drop_revert(n, drop, hold)`.

## Sources
- Alpaca crypto fees: https://docs.alpaca.markets/us/docs/crypto-fees ; https://alpaca.markets/support/crypto-maker-taker-gmt-faq
- Liu & Tsyvinski, Risks and Returns of Cryptocurrency, RFS 2021: https://academic.oup.com/rfs/article/34/6/2689/5912024 (NBER w24877)
- Liu, Tsyvinski & Wu, Common Risk Factors in Cryptocurrency, JF 2022: https://doi.org/10.1111/jofi.13119
- Hudson & Urquhart, Technical trading and cryptocurrencies, Annals of OR 2021: https://link.springer.com/article/10.1007/s10479-019-03357-1
- Shen, Urquhart & Wang, Bitcoin intraday time series momentum, Financial Review 2022: https://doi.org/10.1111/fire.12290
- Kozlowski, Puleo & Zhou, Cryptocurrency return reversals, Applied Econ Letters 2021: https://doi.org/10.1080/13504851.2020.1784831
- Zaremba et al., Up or down? Short-term reversal, momentum, and liquidity effects in cryptocurrency markets, IRFA 2021: https://www.sciencedirect.com/science/article/pii/S1057521921002349
- Kaya & Mostowfi, Low-volatility strategies for highly liquid cryptocurrencies, FRL 2022: https://www.sciencedirect.com/science/article/pii/S1544612321004116
- Cryptocurrency momentum has (not) its moments, FMPM 2025: https://link.springer.com/article/10.1007/s11408-025-00474-9
- Bitcoin's Weekend Effect 2014–2024: https://bbwpublisher.com/journal/PBES/8/5/10.26689/pbes.v8i5.11691
Tools credited: alpaca-py, vectorbt, arch (SPA), pypbo/CSCV (Bailey et al. 2014), DSR (Bailey & Lopez de Prado 2014).
