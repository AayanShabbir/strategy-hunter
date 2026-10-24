"""Deflated Sharpe Ratio (Bailey & Lopez de Prado 2014). All Sharpe ratios are PER-PERIOD (not annualised).

  SR0   = sqrt(V[SR_n]) * ((1-g) Phi^-1(1-1/N) + g Phi^-1(1-1/(N e)))        (expected max SR of N skill-less trials)
  DSR   = Phi( (SR_hat - SR0) sqrt(T-1) / sqrt(1 - skew*SR_hat + (kurt-1)/4 * SR_hat^2) ),   kurt = raw (normal: 3)
N is the ledger's trial count; V[SR_n] is the cross-trial variance of per-period Sharpe ratios (estimated from a sample of
ledger trials by the caller). N = 1 => SR0 = 0 and DSR = PSR(0).
"""
from __future__ import annotations
import numpy as np
from scipy import stats

EULER = 0.5772156649015329


def expected_max_sr(n_trials: int, var_sr: float) -> float:
    if n_trials <= 1 or not np.isfinite(var_sr) or var_sr <= 0: return 0.0
    N = float(n_trials)
    return float(np.sqrt(var_sr) * ((1 - EULER) * stats.norm.ppf(1 - 1 / N) + EULER * stats.norm.ppf(1 - 1 / (N * np.e))))


def probabilistic_sharpe(sr_hat: float, T: int, skew: float, kurt: float, sr_bench: float = 0.0) -> float:
    denom = 1.0 - skew * sr_hat + (kurt - 1.0) / 4.0 * sr_hat ** 2
    if T < 3 or denom <= 0 or not np.isfinite(sr_hat): return float("nan")
    return float(stats.norm.cdf((sr_hat - sr_bench) * np.sqrt(T - 1) / np.sqrt(denom)))


def deflated_sharpe(R: np.ndarray, n_trials: int, var_sr: float) -> dict:
    R = np.asarray(R, float); R = R[np.isfinite(R)]
    if len(R) < 30 or R.std(ddof=1) == 0:
        return dict(dsr=float("nan"), sr=float("nan"), sr0=float("nan"), n_trials=int(n_trials), T=int(len(R)))
    sr = float(R.mean() / R.std(ddof=1)); skew = float(stats.skew(R)); kurt = float(stats.kurtosis(R, fisher=False))
    sr0 = expected_max_sr(n_trials, var_sr)
    return dict(dsr=probabilistic_sharpe(sr, len(R), skew, kurt, sr0), psr0=probabilistic_sharpe(sr, len(R), skew, kurt, 0.0),
                sr=sr, sr_annual=sr * np.sqrt(252), sr0=sr0, sr0_annual=sr0 * np.sqrt(252), n_trials=int(n_trials),
                var_sr=float(var_sr), T=int(len(R)), skew=skew, kurt=kurt)
