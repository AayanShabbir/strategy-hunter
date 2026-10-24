"""Long-only / long-flat deployability check for long-short SDE and swarm survivors (research only; no orders, no broker).

The SDE and swarm score dollar-neutral long-short books, which a long-only account cannot hold. This reports, on a SEARCH-window
panel, what survives when the short leg is removed:
  long_short        the reference book (leverage-normalised, sum|w| = 1, as in src/portfolio/long_short.py)
  long_flat         the LONG LEG of that same book (weights unchanged, so ~0.5 invested, the rest cash = "flat")
  long_only_topq    equal-weight top-q of the signal, fully invested (default q = 20 %)
  benchmark         equal-weight of every tradable name (what a long-only book gets for free from market beta)
plus, for the two long-only variants, excess return / information ratio / beta / alpha against the benchmark, and a boolean
`survives` = net Sharpe of the excess series > 0 for BOTH long variants (alpha that is not just beta). Informational, not a gate.
Inputs: a Panel-like object (data, member, dates), and one of `signal` (D x N, already sign-oriented), `expr`(+`sign`), or `pool`
(list of {expr, sign}, equal-weight combined like Phase 2). `max_date` (default 2020-12-31) makes the function refuse panels that reach
into the sealed holdout; only the vault package passes max_date=None, inside its single-use look."""
from __future__ import annotations
import numpy as np
from src.portfolio.long_short import (K_DAYS, MIN_CROSS_SECTION, backtest, leverage_normalized_weights, metrics, tradable_mask, zscore_rows)

SEARCH_END = "2020-12-31"


def _signal(panel, tradable, signal=None, expr=None, sign=1, pool=None) -> np.ndarray:
    from src.portfolio.combine import combine_equal, factor_matrix, member_signals
    if signal is not None: return np.asarray(signal, float)
    if expr is not None: return sign * zscore_rows(factor_matrix(panel, expr), tradable)
    if pool is not None: return combine_equal(member_signals(panel, pool, tradable, dtype=np.float64))
    raise ValueError("give one of signal / expr / pool")


def top_quantile_weights(sig: np.ndarray, tradable: np.ndarray, q: float = 0.2, min_n: int = MIN_CROSS_SECTION) -> np.ndarray:
    """Equal-weight long book in the top q of the signal each day (sum w = 1); rows with < min_n valid names stay in cash."""
    W = np.zeros(sig.shape); ok = tradable & np.isfinite(sig)
    for t in np.nonzero(ok.sum(1) >= min_n)[0]:
        idx = np.nonzero(ok[t])[0]; k = max(int(np.ceil(q * len(idx))), 1)
        top = idx[np.argsort(-sig[t, idx], kind="stable")[:k]]; W[t, top] = 1.0 / k
    return W


def _ols(y: np.ndarray, x: np.ndarray) -> tuple[float, float]:
    vx = x.var(ddof=1)
    if len(x) < 3 or vx <= 0: return float("nan"), float("nan")
    b = float(np.cov(x, y, ddof=1)[0, 1] / vx); return b, float(y.mean() - b * x.mean())


def _excess(net: np.ndarray, bench: np.ndarray, K: int = K_DAYS) -> dict:
    ok = np.isfinite(net) & np.isfinite(bench); a, b = net[ok], bench[ok]
    if len(a) < 3: return {"n_days": int(len(a))}
    ex = a - b; sd = ex.std(ddof=1); beta, alpha_d = _ols(a, b)
    return {"n_days": int(len(a)), "excess_annual_return": float(K * ex.mean()), "excess_sharpe": float(np.sqrt(K) * ex.mean() / sd) if sd > 0 else float("nan"),
            "beta": beta, "alpha_annual": float(K * alpha_d)}


def long_flat_check(panel, *, signal=None, expr=None, sign: int = 1, pool=None, start: str | None = None, end: str | None = None,
                    cost_bps: float = 5.0, top_q: float = 0.2, max_date: str | None = SEARCH_END, eval_from_idx: int = 0) -> dict:
    """See module docstring. `start`/`end` (ISO) clip the SCORED rows; signals are computed on the whole panel (rolling-window warm-up)."""
    dates = np.asarray(panel.dates).astype("datetime64[D]")
    if max_date is not None and dates.max() > np.datetime64(max_date):
        raise ValueError(f"panel reaches {dates.max()} > {max_date}: deployability checks run on the search window only")
    tr = tradable_mask(panel); close = panel.data["$close"]
    sig = _signal(panel, tr, signal, expr, sign, pool)
    z = zscore_rows(sig, tr)
    W_ls = leverage_normalized_weights(z)
    books = {"long_short": W_ls, "long_flat": np.where(W_ls > 0, W_ls, 0.0), "long_only_topq": top_quantile_weights(z, tr, top_q)}
    n_tr = tr.sum(1, keepdims=True).astype(float)
    books["benchmark"] = np.where(tr & (n_tr >= MIN_CROSS_SECTION), 1.0 / np.maximum(n_tr, 1), 0.0)
    ds = dates[:-1]; m = np.ones(len(ds), bool); m[:max(eval_from_idx, 0)] = False
    if start: m &= ds >= np.datetime64(start)
    if end: m &= ds <= np.datetime64(end)
    out, nets = {}, {}
    for k, W in books.items():
        bt = backtest(W, close, cost_bps); nets[k] = bt["net"][m]
        out[k] = metrics(bt["net"][m], bt["turnover"][m]); out[k]["avg_gross"] = float(bt["gross_leverage"][m].mean())
    for k in ("long_flat", "long_only_topq"): out[k]["vs_benchmark"] = _excess(nets[k], nets["benchmark"])
    ex = [out[k]["vs_benchmark"].get("excess_sharpe", float("nan")) for k in ("long_flat", "long_only_topq")]
    out["survives"] = bool(all(np.isfinite(e) and e > 0 for e in ex))
    out["params"] = {"cost_bps": cost_bps, "top_q": top_q, "start": start, "end": end, "n_scored_days": int(m.sum())}
    return out
