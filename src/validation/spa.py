"""Hansen (2005) Superior Predictive Ability test (stationary bootstrap, studentised, consistent p-value).

H0: no candidate has expected daily return > benchmark (default: 0).  D is (T, K) of candidate-minus-benchmark daily returns.
T_SPA = max(0, max_k sqrt(T) dbar_k / omega_k); omega_k from the bootstrap variance of sqrt(T)*dbar*_k.
Re-centring: lower  mu_l = min(dbar,0); consistent mu_c = dbar * 1{sqrt(T) dbar/omega <= -sqrt(2 log log T)}; upper mu_u = 0 (White RC).
Reported: p_lower <= p_consistent <= p_upper; the consistent p-value is the headline.
"""
from __future__ import annotations
import numpy as np


def stationary_bootstrap_idx(T: int, B: int, mean_block: float, rng) -> np.ndarray:
    """(B, T) index matrix of the Politis-Romano stationary bootstrap (geometric blocks, circular)."""
    p = 1.0 / mean_block
    start = rng.integers(0, T, size=(B, T)); new = rng.random((B, T)) < p; new[:, 0] = True
    idx = np.empty((B, T), dtype=np.int64); idx[:, 0] = start[:, 0]
    for t in range(1, T):
        idx[:, t] = np.where(new[:, t], start[:, t], (idx[:, t - 1] + 1) % T)
    return idx


def spa_test(D: np.ndarray, B: int = 1000, mean_block: float = 10.0, seed: int = 0) -> dict:
    D = np.nan_to_num(np.asarray(D, float)); T, K = D.shape
    if T < 30 or K < 1: return dict(p_consistent=float("nan"), reason="too little data")
    rng = np.random.default_rng(seed); dbar = D.mean(0)
    idx = stationary_bootstrap_idx(T, B, mean_block, rng)
    bar_star = np.stack([D[idx[b]].mean(0) for b in range(B)])                      # (B, K)
    omega = np.sqrt(np.maximum(T * bar_star.var(0, ddof=1), 1e-20))
    stat = max(0.0, float(np.max(np.sqrt(T) * dbar / omega)))
    thr = -np.sqrt(2.0 * np.log(np.log(T)))
    mus = dict(lower=np.minimum(dbar, 0.0), consistent=np.where(np.sqrt(T) * dbar / omega <= thr, dbar, 0.0), upper=np.zeros(K))
    out = dict(stat=stat, T=int(T), K=int(K), best_candidate=int(np.argmax(dbar)), best_mean_daily=float(dbar.max()), B=B, mean_block=mean_block)
    for name, mu in mus.items():
        tstar = np.maximum(0.0, np.max(np.sqrt(T) * (bar_star - dbar + mu) / omega, axis=1))
        out["p_" + name] = float(np.mean(tstar >= stat))
    return out
