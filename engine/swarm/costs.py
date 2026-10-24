"""Square-root market-impact execution cost (blueprint section 1):

    slippage_{i,t} = eta * (OrderVolume_{i,t} / ADV_{i,t})^alpha * sigma_{i,t}        alpha = 0.5

OrderVolume_{i,t} = |w_{t,i} - pre_{t,i}| * AUM (dollars traded in asset i at close t, `pre` = the drifted pre-trade weight, exactly the
SDE backtest's definition so that sum_i |dw_{t,i}| equals the SDE turnover - asserted by `check_turnover`), ADV$_{i,t} = trailing 20-day
mean of close*volume and sigma_{i,t} = trailing 20-day std of daily returns, both through t-1 (known before the trade).
Cost of day t as a fraction of capital:  sum_i |dw_{t,i}| * slippage_{i,t}. It is charged IN ADDITION to the SDE's flat `cost_bps`
per dollar (commission + half-spread); the impact term models the size-dependent part the flat charge cannot. Defaults: eta = 1.0
(order-one, as in the empirical square-root law), AUM = $50M. Both are configuration, not fitted - recorded in every trial's metrics.
NaN ADV/sigma cells (new listings) take the day's cross-sectional median, so an untradable-looking cell is never free.
The cost does not depend on the long/short sign (|dw| is symmetric), so the Auditor can subtract it after re-choosing signs.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass

import numpy as np

from src.portfolio.long_short import forward_returns

WINDOW = 20


@dataclass(frozen=True)
class ImpactModel:
    eta: float = 1.0
    alpha: float = 0.5
    aum: float = 50e6
    window: int = WINDOW

    def asdict(self) -> dict:
        return asdict(self)


def _trailing(x: np.ndarray, w: int, fn) -> np.ndarray:
    """Trailing statistic through t-1 (NaN for the first w rows); fn reduces the last axis of a (T-w+1, N, w) view."""
    T, N = x.shape
    out = np.full((T, N), np.nan)
    if T > w:
        win = np.lib.stride_tricks.sliding_window_view(x, w, axis=0)          # (T-w+1, N, w); row k covers x[k:k+w]
        out[w:] = fn(win[:T - w])                                              # row t uses rows t-w..t-1
    return out


def adv_sigma(close: np.ndarray, volume: np.ndarray, window: int = WINDOW) -> tuple[np.ndarray, np.ndarray]:
    dollar = np.where(np.isfinite(close) & np.isfinite(volume), close * volume, np.nan)
    adv = _trailing(dollar, window, lambda w: w.mean(-1))
    ret = np.full_like(close, np.nan)
    with np.errstate(all="ignore"):
        ret[1:] = close[1:] / close[:-1] - 1.0
    ret[~np.isfinite(ret)] = np.nan
    sig = _trailing(ret, window, lambda w: w.std(-1, ddof=1))
    return adv, sig


def trades(W: np.ndarray, close: np.ndarray) -> np.ndarray:
    """(D-1, N) per-asset |w_t - pre_t| using the SDE backtest's drift convention; rows align with `backtest()` output."""
    r = np.nan_to_num(forward_returns(close))[:-1]
    W = W[:-1]
    gross = (W * r).sum(1)
    pre = np.zeros_like(W)
    pre[1:] = W[:-1] * (1.0 + r[:-1]) / (1.0 + gross[:-1])[:, None]
    return np.abs(W - pre)


def _fill_row_median(x: np.ndarray, default: float) -> np.ndarray:
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', RuntimeWarning)
        med = np.nanmedian(np.where(np.isfinite(x), x, np.nan), axis=1) if x.size else np.zeros(len(x))
    med = np.where(np.isfinite(med), med, default)
    return np.where(np.isfinite(x) & (x > 0), x, med[:, None])


def impact_cost(W: np.ndarray, close: np.ndarray, volume: np.ndarray, model: ImpactModel, adv_sig: tuple | None = None) -> tuple[np.ndarray, np.ndarray]:
    """Returns (cost per day as a fraction of capital, per-asset trade matrix). Pass `adv_sig` to reuse the (adv, sigma) arrays."""
    adv, sig = adv_sig if adv_sig is not None else adv_sigma(close, volume, model.window)
    dw = trades(W, close)
    n = dw.shape[0]
    adv, sig = _fill_row_median(adv[:n], 1e6), _fill_row_median(sig[:n], 0.02)
    ratio = dw * model.aum / adv
    slip = model.eta * np.power(ratio, model.alpha) * sig                    # fraction of the traded notional
    return (dw * slip).sum(1), dw


def check_turnover(dw: np.ndarray, turnover: np.ndarray, tol: float = 1e-9) -> None:
    """Guard: the per-asset trades must add up to the backtest's turnover (otherwise the cost would price a different book)."""
    if not np.allclose(dw.sum(1), turnover, rtol=0, atol=tol):
        raise ValueError(f"per-asset trades do not sum to backtest turnover (max diff {np.abs(dw.sum(1) - turnover).max():.3g})")
