"""CSCV / Probability of Backtest Overfitting (Bailey, Borwein, Lopez de Prado, Zhu 2017).

M is (T, S): T daily returns of S candidate strategies. Rows are cut into `n_slices` (default 16) equal blocks; for every
choice of n_slices/2 blocks as in-sample (IS) the remaining blocks are out-of-sample (OOS). The IS-best strategy (Sharpe)
has OOS relative rank w in (0,1); logit = ln(w/(1-w)); PBO = share of splits with logit <= 0 (IS winner at or below the OOS
median). Blueprint pass bar: PBO < 0.10.
"""
from __future__ import annotations
from itertools import combinations
import numpy as np


def cscv_pbo(M: np.ndarray, n_slices: int = 16) -> dict:
    M = np.asarray(M, float)
    T, S = M.shape
    if S < 2 or T < n_slices * 2: return dict(pbo=float("nan"), n_splits=0, S=S, T=T, reason="need >=2 strategies and >=2 rows per slice")
    M = np.nan_to_num(M); L = T // n_slices; M = M[T - L * n_slices:]            # drop the oldest remainder
    blocks = M.reshape(n_slices, L, S)
    s1 = blocks.sum(1); s2 = (blocks ** 2).sum(1)                                   # (n_slices, S)
    half = n_slices // 2; logits = []; deg = []
    def sharpe(idx):
        n = L * len(idx); m = s1[list(idx)].sum(0) / n; v = s2[list(idx)].sum(0) / n - m ** 2
        return m / np.sqrt(np.maximum(v, 1e-18))
    allb = set(range(n_slices))
    for IS in combinations(range(n_slices), half):
        OOS = tuple(sorted(allb - set(IS)))
        sr_is = sharpe(IS); sr_oos = sharpe(OOS)
        best = int(np.argmax(sr_is))
        rank = 1 + np.sum(sr_oos < sr_oos[best]) + 0.5 * (np.sum(sr_oos == sr_oos[best]) - 1)   # 1..S, ties averaged
        w = rank / (S + 1.0); logits.append(np.log(w / (1.0 - w))); deg.append((sr_is[best], sr_oos[best]))
    logits = np.array(logits); deg = np.array(deg)
    slope = float(np.polyfit(deg[:, 0], deg[:, 1], 1)[0]) if deg[:, 0].std() > 0 else float("nan")
    return dict(pbo=float(np.mean(logits <= 0)), n_splits=int(len(logits)), S=int(S), T=int(L * n_slices),
                median_logit=float(np.median(logits)), prob_oos_loss=float(np.mean(deg[:, 1] < 0)),
                perf_degradation_slope=slope, mean_is_sr=float(deg[:, 0].mean()), mean_oos_sr=float(deg[:, 1].mean()))
