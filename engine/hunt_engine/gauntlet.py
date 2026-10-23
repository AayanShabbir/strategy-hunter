"""The pass bar, applied automatically. Every check is required."""
import numpy as np, pandas as pd
from itertools import combinations
from scipy.stats import norm, skew, kurtosis
def ann_factor(symbols, tf="1Day"):
    """Daily-return annualisation: crypto trades 365 d/yr (symbols like 'SOL/USD'), equities 252."""
    return 365 if any("/" in str(x) for x in symbols) else 252
def stats(r, ann=252):
    r = r.dropna()
    if len(r) < 2 or r.std() == 0: return dict(ret=round(float((1 + r).prod() - 1) * 100, 2), sharpe=0.0, maxdd=0.0)
    eq = (1 + r).cumprod()
    return dict(ret=round(float(eq.iloc[-1] - 1) * 100, 2), sharpe=round(float(r.mean() / r.std() * np.sqrt(ann)), 2),
                maxdd=round(float((eq / eq.cummax() - 1).min()) * 100, 2))
def _shuffle(v, rng):
    ch = np.r_[0, np.flatnonzero(np.diff(v)) + 1, len(v)]; lens = np.diff(ch); rng.shuffle(lens)
    out = np.empty(len(v)); i = 0; s = rng.integers(0, 2)
    for L in lens: out[i:i + L] = s; i += L; s = 1 - s
    return out
try:
    from numba import njit
except Exception:  # pragma: no cover
    njit = None
def _twin_kernel_py(Wv, Rv, fee_side, n, seed):
    rng = np.random.default_rng(seed); tot = np.empty(n)
    for t in range(n):
        X = np.column_stack([_shuffle(Wv[:, j], rng) for j in range(Wv.shape[1])])
        dX = np.abs(np.diff(np.vstack([np.zeros((1, X.shape[1])), X]), axis=0))
        tot[t] = np.prod(1 + (X * Rv - fee_side * dX).mean(1)) - 1
    return tot
if njit:
    @njit(cache=True)
    def _twin_kernel_nb(Wv, Rv, fee_side, n, seed):
        np.random.seed(seed); T, K = Wv.shape; tot = np.empty(n); X = np.empty((T, K))
        for t in range(n):
            for j in range(K):
                v = Wv[:, j]; ch = [0]
                for i in range(1, T):
                    if v[i] != v[i - 1]: ch.append(i)
                ch.append(T); L = np.diff(np.array(ch)); np.random.shuffle(L)
                s = np.random.randint(0, 2); i = 0
                for l in L:
                    X[i:i + l, j] = s; i += l; s = 1 - s
            eq = 1.0
            for i in range(T):
                acc = 0.0
                for j in range(K):
                    prev = X[i - 1, j] if i > 0 else 0.0
                    acc += X[i, j] * Rv[i, j] - fee_side * abs(X[i, j] - prev)
                eq *= 1 + acc / K
            tot[t] = eq - 1
        return tot
def random_twin(W, R, fee_side, real_total, n=1000, seed=0, fast=True):
    """Random-entry control: shuffled holding run-lengths (same exposure & #switches), same costs.
    Returns (p, median random total return %)."""
    Rv = np.ascontiguousarray(np.nan_to_num(R.values), dtype=np.float64); Wv = np.ascontiguousarray(W.values, dtype=np.float64)
    tot = (_twin_kernel_nb if (fast and njit) else _twin_kernel_py)(Wv, Rv, float(fee_side), int(n), int(seed) % (2**31))
    return float((np.sum(tot >= real_total) + 1) / (n + 1)), round(float(np.median(tot)) * 100, 2)
def holm_adjusted(pvals_by_row, rows):
    """Holm step-down across the whole ledger (m = ledger N). Returns adjusted p for requested rows."""
    items = sorted(pvals_by_row.items(), key=lambda kv: kv[1]); m = len(items); adj = {}; run = 0.0
    for i, (row, p) in enumerate(items):
        run = max(run, min(1.0, (m - i) * p)); adj[row] = run
    return {r: adj[r] for r in rows}
def dsr(r, sr_var, N):
    r = r.dropna(); T = len(r)
    if T < 3 or r.std() == 0: return 0.0
    sr = r.mean() / r.std(); g = 0.5772156649
    e = np.sqrt(sr_var) * ((1 - g) * norm.ppf(1 - 1 / N) + g * norm.ppf(1 - 1 / (N * np.e)))
    den = 1 - skew(r) * sr + kurtosis(r) / 4 * sr ** 2
    return float(norm.cdf((sr - e) * np.sqrt(T - 1) / np.sqrt(max(den, 1e-12))))
def pbo_cscv(M, S=16):
    """CSCV PBO (Bailey et al. 2014). M: T x K returns matrix."""
    M = np.asarray(M); bl = np.array_split(np.arange(len(M)), S); lo = []
    for c in combinations(range(S), S // 2):
        isx = np.concatenate([bl[i] for i in c]); osx = np.concatenate([bl[i] for i in range(S) if i not in c])
        a = M[isx].mean(0) / (M[isx].std(0) + 1e-12); b_ = M[osx].mean(0) / (M[osx].std(0) + 1e-12); b = np.argmax(a)
        w = ((b_ < b_[b]).sum() + 0.5) / len(b_); lo.append(np.log(w / (1 - w)))
    return float(np.mean(np.array(lo) <= 0))
def spa_p(bench, strat, seed=1, reps=2000):
    from arch.bootstrap import SPA
    s = SPA(-np.asarray(bench), -np.asarray(strat).reshape(-1, 1), reps=reps, seed=seed); s.compute()
    return float(s.pvalues["consistent"])
def cpcv(r, n_groups=6, k_test=2, ann=252):
    """Combinatorial purged CV diagnostic (Lopez de Prado, AFML ch.12) on a fixed-rule return series:
    split into n_groups blocks, every C(n,k) choice of k blocks is a test set; returns the distribution of
    test-set Sharpe. Rules are pre-registered (no fitting), so purging/embargo is moot here; it is a
    path-robustness diagnostic reported alongside -- NOT a replacement for -- the pass bar."""
    r = np.asarray(pd.Series(r).dropna()); bl = np.array_split(np.arange(len(r)), n_groups); sh = []
    for c in combinations(range(n_groups), k_test):
        x = r[np.concatenate([bl[i] for i in c])]
        sh.append(float(x.mean() / x.std() * np.sqrt(ann)) if x.std() > 0 else 0.0)
    sh = np.array(sh); return dict(median_sharpe=round(float(np.median(sh)), 2), frac_positive=round(float((sh > 0).mean()), 3), n_paths=len(sh))
BAR = dict(holm=0.05, dsr=0.95, spa=0.05, pbo=0.5, cost_stop=0.03)
def verdict(x, min_trades, pbo):
    checks = dict(oos_positive=x["OOS"]["ret"] > 0, beats_buy_hold=x["OOS"]["ret"] > x["BH_OOS"]["ret"],
                  min_trades=x["trades"] >= min_trades, cost_stop=x["cost_stop"] <= BAR["cost_stop"],
                  walk_forward=all(f > 0 for f in x["WF"]), holm=x["holm"] < BAR["holm"], dsr=x["DSR"] > BAR["dsr"],
                  spa=x["SPA"] < BAR["spa"], pbo=pbo < BAR["pbo"])
    return all(checks.values()), checks
