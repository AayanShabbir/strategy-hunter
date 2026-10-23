# Hunt #13 — 15-minute top-scorer (research only, no orders, nothing changed on desk)

**Verdict: FAIL, 0/3 variants.** Every variant lost money in-sample and out-of-sample after costs. SPY core stays the engine.

Rules pre-registered in `prereg.yaml` before any results (one bug fix after a debug run on partial data, not a rule change: arch SPA expects losses, so returns are negated).

- Data: Alpaca IEX 15m, RTH, 474 of the liquid-500 (2026-10-16 list; 26 had no data or are desk-blocked). Survivorship-biased. Fetched to `research_lab/data/alpaca/h13_15m/`.
- Score each bar: cross-sectional ranks of trend ((close−EMA20)/ATR), candle ((C−O)/(H−L)), VWAP distance (/ATR), times relative-volume rank. V0 = continuation, V1 = fade, V2 = continuation without candle.
- Trade only the single top |score| name when it is ≥ the IS 90th percentile (V0/V1 0.9418, V2 0.9844). Enter next-bar open; 1.5×ATR stop filled at the bar extreme, checked before the 2R target; flat at the 15:45 bar close; one position at a time; 10% size; 5 bps fee + 2 bps slippage per side.
- Split: IS 2024-10-15..2026-03-16 (70%), OOS 2026-03-17..2026-10-21 (newest 30%, ~7 months).

| Variant | OOS trades | Win % | Avg win / loss (bps) | Avg net (bps) | IS ret % | OOS ret % | OOS Sharpe | OOS MaxDD % | p | Holm@327 | DSR | SPA p vs SPY / 70-30 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| V0_cont | 222 | 31.5 | +156.8 / −137.5 | −44.7 | −16.43 | −9.48 | −4.94 | −9.28 | 0.9999 | 1.0 | 0.00 | 0.52 / 0.52 |
| V1_fade | 211 | 45.5 | +163.4 / −147.1 | −5.9 | −16.46 | −1.27 | −0.58 | −3.16 | 0.662 | 1.0 | 0.00 | 0.93 / 0.92 |
| V2_cont_no_candle | 180 | 40.6 | +186.5 / −173.6 | −27.6 | −12.85 | −4.89 | −2.35 | −6.41 | 0.943 | 1.0 | 0.00 | 0.51 / 0.51 |
| SPY buy & hold | | | | | | **+15.57** | 1.90 | −5.77 | | | | |
| 70% SPY + 30% cash | | | | | | **+10.78** | 1.90 | −4.06 | | | | |

(Strategy returns are on total equity at 10% sizing; IS trades: 475 / 473 / 407.) PBO (CSCV, 16 blocks, 3 variants) = 0.708. CPCV not run separately: the PBO's CSCV gives the combinatorial split view. Tearsheet: `tearsheet.html` (V1_fade OOS vs SPY).

Why it fails: when the top-scored name breaks out, the continuation bet loses (V0 wins only 31%), and the fade loses less but still can't cover 14 bps round trip plus stop fills at the bar extreme. Ledger N 324 → **327** (rows 325–327), synced in both ledgers by hand; hunt3 eng3.ledger() was not run. Jev (TypeSafe) is untested: waitlist only, no access.

Files: `prereg.yaml`, `fetch.py`, `run.py`, `run.log`, `results.json`, `trades.parquet`, `tearsheet.html`, `HUNT_LEDGER_snapshot.md`.
