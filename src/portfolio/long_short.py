"""SDE Phase 3: long-short, leverage-normalized portfolio with transaction costs (blueprint).

Signal s_{t,i} (known at close t)  ->  weights  w_{t,i} = G * (s_{t,i} - mean_t(s)) / sum_j |s_{t,j} - mean_t(s)|
    * dollar-neutral (sum w = 0), gross leverage sum|w| = G (default 1) every day (the "leverage normalization");
    * assets without a valid signal / not tradable at t get weight 0;
    * the position is held over close t -> close t+1 and re-set every day.
Costs follow the Promote paper convention (Benhamou et al. 2026): `cost_bps` per dollar of ONE-WAY turnover, charged on
turnover measured against the DRIFTED pre-trade weights:   pre_t = w_{t-1} (1+r_{t-1}) / (1+R_{t-1}).
Net return of the position set at t:  R_t = sum_i w_{t,i} r_{t,i} - cost_bps/1e4 * sum_i |w_{t,i} - pre_{t,i}|.
Metrics follow AlphaSAGE App. D.1 (K = 252, r_f = 0): AR = K*mean(R), SR = sqrt(K) mean/std, MDD on compounded wealth.
Not modelled (documented): borrow/financing on shorts, spreads/impact beyond cost_bps, limit-up/down and suspensions
beyond "no valid price at t => weight 0", capacity.
"""
from __future__ import annotations
import numpy as np

K_DAYS = 252
MIN_CROSS_SECTION = 30


def zscore_rows(F: np.ndarray, valid: np.ndarray, min_n: int = MIN_CROSS_SECTION) -> np.ndarray:
    """Per-row cross-sectional z-score over valid & finite cells; rows with < min_n cells or zero dispersion -> NaN."""
    ok = valid & np.isfinite(F)
    n = ok.sum(1); f0 = np.where(ok, F, 0.0)
    mu = f0.sum(1) / np.maximum(n, 1)
    c = np.where(ok, F - mu[:, None], 0.0)
    sd = np.sqrt((c * c).sum(1) / np.maximum(n - 1, 1))
    good = (n >= min_n) & (sd > 1e-12)
    out = np.full(F.shape, np.nan)
    out[good] = np.where(ok[good], c[good] / sd[good][:, None], np.nan)
    return out


def leverage_normalized_weights(sig: np.ndarray, gross: float = 1.0) -> np.ndarray:
    """(D,N) signal -> (D,N) dollar-neutral weights with sum|w| = gross on every day that has a valid cross-section."""
    ok = np.isfinite(sig)
    n = ok.sum(1)
    s0 = np.where(ok, sig, 0.0)
    c = np.where(ok, sig - (s0.sum(1) / np.maximum(n, 1))[:, None], 0.0)
    g = np.abs(c).sum(1)
    with np.errstate(all="ignore"):
        w = np.where((g > 1e-12)[:, None], gross * c / g[:, None], 0.0)
    return w


def tradable_mask(panel) -> np.ndarray:
    """Valid price and non-zero volume at t (information available at close t) and point-in-time membership."""
    c, v = panel.data["$close"], panel.data["$volume"]
    return panel.member & np.isfinite(c) & (c > 0) & np.isfinite(v) & (v > 0)


def forward_returns(close: np.ndarray) -> np.ndarray:
    """r[t] = close[t+1]/close[t]-1 (return earned by the position set at close t). Last row NaN. Non-finite -> NaN."""
    r = np.full(close.shape, np.nan)
    with np.errstate(all="ignore"):
        r[:-1] = close[1:] / close[:-1] - 1.0
    r[~np.isfinite(r)] = np.nan
    return r


def backtest(W: np.ndarray, close: np.ndarray, cost_bps: float = 5.0) -> dict:
    """Daily gross/net returns and turnover for weights set at each close. Last row dropped (no next-day return).

    NaN forward returns (suspension, missing) are treated as 0 for P&L; the weights stay as set.
    """
    r = np.nan_to_num(forward_returns(close))[:-1]; W = W[:-1]
    gross = (W * r).sum(1)
    pre = np.zeros_like(W)
    pre[1:] = W[:-1] * (1.0 + r[:-1]) / (1.0 + gross[:-1])[:, None]
    turnover = np.abs(W - pre).sum(1)          # sum |dw|, one-way notional traded per $1 of capital
    net = gross - cost_bps * 1e-4 * turnover
    return dict(gross=gross, net=net, turnover=turnover, gross_leverage=np.abs(W).sum(1), net_exposure=W.sum(1))


def metrics(R: np.ndarray, turnover: np.ndarray | None = None, K: int = K_DAYS) -> dict:
    R = np.asarray(R, float); R = R[np.isfinite(R)]
    if len(R) < 2: return dict(n_days=int(len(R)), sharpe=float("nan"), annual_return=float("nan"), cagr=float("nan"),
                               annual_vol=float("nan"), max_drawdown=float("nan"), turnover_daily=float("nan"), turnover_annual=float("nan"))
    sd = R.std(ddof=1)
    wealth = np.cumprod(1.0 + R); peak = np.maximum.accumulate(np.r_[1.0, wealth])[1:]
    out = dict(n_days=int(len(R)),
               sharpe=float(np.sqrt(K) * R.mean() / sd) if sd > 0 else float("nan"),
               annual_return=float(K * R.mean()),
               cagr=float(wealth[-1] ** (K / len(R)) - 1.0) if wealth[-1] > 0 else -1.0,
               annual_vol=float(sd * np.sqrt(K)),
               max_drawdown=float(-np.max(1.0 - wealth / peak)))
    if turnover is not None:
        t = np.asarray(turnover, float)
        out["turnover_daily"] = float(np.nanmean(t)); out["turnover_annual"] = float(K * np.nanmean(t))
    return out


def sharpe_daily(R: np.ndarray) -> float:
    """Per-period (non-annualized) Sharpe, the unit DSR works in."""
    R = np.asarray(R, float); R = R[np.isfinite(R)]
    sd = R.std(ddof=1) if len(R) > 1 else 0.0
    return float(R.mean() / sd) if sd > 0 else float("nan")
