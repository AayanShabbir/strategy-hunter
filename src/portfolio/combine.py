"""SDE Phase 3: pool combination step.

The blueprint's combination stage follows AlphaForge (AlphaSAGE Sec. 3.5): "instead of fixing a static set of alphas, the
framework performs a dynamic re-selection and linear combination of mined alphas. At each period, recently effective alphas
are filtered and re-weighted through simple linear regression, yielding a time-varying Mega-Alpha."  `combine_rolling_ols`
implements exactly that: at every refresh date t
  1. FILTER : keep pool members whose trailing mean daily rank-free IC (sign-oriented) over the window is > ic_min;
  2. WEIGHT : ordinary (ridge-stabilised) least squares of the cross-sectionally z-scored 20-day forward return on the kept
              members' z-scores, pooled over the window's (day, asset) cells, no intercept;
  3. the Mega-Alpha for days t .. t+refresh-1 is  sum_k beta_k z_k.
Causality: labels used at refresh t only include days d <= t-20 (their 20-day label is fully known at close t).
Unspecified by the text we have (so chosen and logged, not tuned): lookback=250 days, refresh=20 days, ic_min=0,
ridge=1e-6. `combine_equal` (sign-oriented equal-weight mean of z) is the Phase 2 ensemble, kept as a static reference.
"""
from __future__ import annotations
import numpy as np
from src.dsl.grammar import evaluate, parse_expr
from src.portfolio.long_short import zscore_rows, forward_returns

HORIZON = 20
DEFAULTS = dict(lookback=250, refresh=20, ic_min=0.0, ridge=1e-6)


def factor_matrix(panel, expr: str) -> np.ndarray:
    f = evaluate(parse_expr(expr), panel.data)
    return np.where(np.isfinite(f) & (np.abs(f) < 1e150), f, np.nan)


def member_signals(panel, members, tradable, dtype=np.float32) -> np.ndarray:
    """(K, D, A) sign-oriented row-z-scored member signals (NaN where invalid)."""
    out = np.full((len(members), *tradable.shape), np.nan, dtype=dtype)
    for k, m in enumerate(members):
        out[k] = (m["sign"] * zscore_rows(factor_matrix(panel, m["expr"]), tradable)).astype(dtype)
    return out


def label_matrix(close: np.ndarray, tradable: np.ndarray, h: int = HORIZON) -> np.ndarray:
    """Cross-sectionally z-scored h-day forward return (NaN where unknown). Row d needs close[d+h]."""
    y = np.full(close.shape, np.nan)
    with np.errstate(all="ignore"):
        y[:-h] = close[h:] / close[:-h] - 1.0
    y[~np.isfinite(y)] = np.nan
    return zscore_rows(y, tradable)


def daily_ic_matrix(Z: np.ndarray, Y: np.ndarray) -> np.ndarray:
    """(K, D) cross-sectional Pearson corr(Z_k[d], Y[d]) over cells where both are finite (NaN if < 30)."""
    K, D, A = Z.shape; out = np.full((K, D), np.nan)
    for k in range(K):
        z = Z[k].astype(float); ok = np.isfinite(z) & np.isfinite(Y); n = ok.sum(1)
        a = np.where(ok, z, 0.0); b = np.where(ok, Y, 0.0)
        a = np.where(ok, a - (a.sum(1) / np.maximum(n, 1))[:, None], 0.0); b = np.where(ok, b - (b.sum(1) / np.maximum(n, 1))[:, None], 0.0)
        with np.errstate(all="ignore"): r = (a * b).sum(1) / np.sqrt((a * a).sum(1) * (b * b).sum(1))
        r[(n < 30) | ~np.isfinite(r)] = np.nan; out[k] = r
    return out


def combine_equal(Z: np.ndarray) -> np.ndarray:
    """Sign-oriented equal-weight mean of z (Phase 2 ensemble). All-NaN rows stay NaN."""
    if Z.shape[0] == 0: return np.full(Z.shape[1:], np.nan)
    ok = np.isfinite(Z); s = np.where(ok, Z, 0.0).sum(0, dtype=np.float64)
    return np.where(ok.any(0), s / Z.shape[0], np.nan)


def combine_rolling_ols(Z: np.ndarray, Y: np.ndarray, first_day: int = 0, horizon: int = HORIZON, lookback: int = 250,
                        refresh: int = 20, ic_min: float = 0.0, ridge: float = 1e-6, return_info: bool = False):
    """AlphaForge-style dynamic filter + OLS combination. Returns (sig (D,A) float64 with NaN where flat, info)."""
    K, D, A = Z.shape
    sig = np.full((D, A), np.nan); info = dict(refresh_idx=[], n_kept=[], betas=[], kept=[])
    if K == 0: return (sig, info) if return_info else sig
    IC = daily_ic_matrix(Z, Y)
    t0 = first_day + lookback + horizon
    for t in range(t0, D, refresh):
        hi = t - horizon + 1                       # exclusive end of label-known days (d <= t-horizon)
        lo = max(first_day, hi - lookback)
        with np.errstate(all="ignore"): ic_tr = np.nanmean(IC[:, lo:hi], axis=1)
        keep = np.flatnonzero(np.isfinite(ic_tr) & (ic_tr > ic_min))
        info["refresh_idx"].append(t); info["n_kept"].append(int(len(keep))); info["kept"].append(keep.tolist())
        end = min(t + refresh, D)
        if len(keep) == 0: info["betas"].append([]); continue
        Zw = np.nan_to_num(Z[keep, lo:hi].astype(np.float64)); Yw = Y[lo:hi]
        okc = np.isfinite(Yw)
        X = Zw[:, okc]; y = Yw[okc]                                      # (k, cells), (cells,)
        XtX = X @ X.T; Xty = X @ y; n = X.shape[1]
        beta = np.linalg.solve(XtX + ridge * n * np.eye(len(keep)), Xty)
        info["betas"].append(beta.tolist())
        comb = np.einsum("k,kda->da", beta, np.nan_to_num(Z[keep, t:end].astype(np.float64)))
        anyv = np.isfinite(Z[keep, t:end]).any(0)
        sig[t:end] = np.where(anyv, comb, np.nan)
    return (sig, info) if return_info else sig
