"""SDE Phase 2: multi-faceted reward (blueprint 2.3 / AlphaSAGE Eq. 9-14) and the factor pool.

    R(a, T) = R_IC(a) + lambda(T) * R_SA(a) + eta(T) * R_NOV(a)
    R_IC  = | mean_d Pearson(Z_a(d), y(d)) |                                   (Eq. 12)
    R_NOV = 1 - max_{a' in pool} | corr(a, a') |                                (Eq. 13)
    R_SA  = exp( - sum_{j in KNN_K(e_a)} w_aj * d_behav(a, a_j) )               (Eq. 9-11)
            d_behav = mean squared difference of cross-sectionally z-scored outputs;
            w_aj = softmax_j( -||e_a - e_j||^2 ) over the K nearest pool embeddings.
    lambda(T) = (1 - T/T_anneal) * lambda_max,  eta(T) = (1 - T/T_anneal) * eta_max   (lambda_max=1.0, eta_max=0.3)

Pool admission (blueprint): |IC| >= 0.03 and |ICIR| >= 0.35, and reject any candidate whose |correlation| with an existing
member exceeds 0.70. Capacity 50 (AlphaSAGE Table 4): when full, the weakest member (lowest |IC|) is replaced if the
candidate is stronger. All statistics are computed ONLY on the split passed in (train during search).

Data layout: member-days are flattened to 'cells' (row-major: day, asset), so daily cross-sectional statistics are
np.add.reduceat segment sums. Corr between two factors = mean over days of the daily cross-sectional Pearson (cosine of
per-day z-scores with missing = 0).
"""
from __future__ import annotations
from dataclasses import dataclass, field
import numpy as np
from src.dsl.grammar import evaluate, parse_expr, parse_ast

MIN_CROSS_SECTION = 30
IC_MIN, ICIR_MIN, CORR_MAX = 0.03, 0.35, 0.70
LAMBDA_MAX, ETA_MAX, POOL_CAP, KNN_K = 1.0, 0.3, 50, 5
REWARD_FLOOR = 1e-6


class Cells:
    """Flattened member cells of one split, with per-day segmentation."""

    def __init__(self, panel, start, end):
        mask = panel.split_mask(start, end)
        self.n_assets = mask.shape[1]
        flat = np.flatnonzero(mask.ravel())
        self.flat = flat
        day = flat // self.n_assets
        self.starts = np.flatnonzero(np.r_[True, day[1:] != day[:-1]])
        self.day_of_cell = np.repeat(np.arange(len(self.starts)), np.diff(np.r_[self.starts, len(flat)]))
        self.days = day[self.starts]
        self.D = len(self.starts)
        self.y = None

    def set_label(self, y_full): self.y = y_full.ravel()[self.flat]

    def take(self, arr2d): return arr2d.ravel()[self.flat]

    def seg(self, v): return np.add.reduceat(v, self.starts)

    def zscore(self, f):
        """per-day cross-sectional z-score; invalid -> NaN. Days with < MIN_CROSS_SECTION valid cells -> NaN."""
        ok = np.isfinite(f); f0 = np.where(ok, f, 0.0)
        n = self.seg(ok.astype(float)); mu = self.seg(f0) / np.maximum(n, 1)
        c = np.where(ok, f - mu[self.day_of_cell], 0.0)
        sd = np.sqrt(self.seg(c * c) / np.maximum(n - 1, 1))
        good = (n >= MIN_CROSS_SECTION) & (sd > 1e-12)
        z = np.where(ok & good[self.day_of_cell], c / np.where(good, sd, 1.0)[self.day_of_cell], np.nan)
        return z

    def daily_ic(self, z):
        """Daily Pearson(z, y) over cells where both finite. NaN where < MIN_CROSS_SECTION pairs."""
        ok = np.isfinite(z) & np.isfinite(self.y)
        n = self.seg(ok.astype(float))
        a = np.where(ok, z, 0.0); b = np.where(ok, self.y, 0.0)
        ma = self.seg(a) / np.maximum(n, 1); mb = self.seg(b) / np.maximum(n, 1)
        a = np.where(ok, a - ma[self.day_of_cell], 0.0); b = np.where(ok, b - mb[self.day_of_cell], 0.0)
        cov = self.seg(a * b); va = self.seg(a * a); vb = self.seg(b * b)
        with np.errstate(all="ignore"):
            r = cov / np.sqrt(va * vb)
        r[(n < MIN_CROSS_SECTION) | ~np.isfinite(r)] = np.nan
        return r

    def ic_stats(self, z):
        r = self.daily_ic(z); r = r[np.isfinite(r)]
        if len(r) < 20: return float("nan"), float("nan"), int(len(r))
        sd = r.std(ddof=1)
        return float(r.mean()), float(r.mean() / sd) if sd > 0 else float("nan"), int(len(r))


@dataclass
class Member:
    expr: str; ast_hash: str; emb: np.ndarray; z: np.ndarray; ic: float; icir: float; sign: int
    ss: np.ndarray = None          # per-day sum of z^2 (NaN->0), for correlations

    def z0(self): return self.z


class FactorPool:
    def __init__(self, cells: Cells, capacity=POOL_CAP, ic_min=IC_MIN, icir_min=ICIR_MIN, corr_max=CORR_MAX):
        self.cells, self.capacity = cells, capacity
        self.ic_min, self.icir_min, self.corr_max = ic_min, icir_min, corr_max
        self.members: list[Member] = []
        self.added = self.replaced = self.rejected_corr = 0

    def __len__(self): return len(self.members)

    def corr_with(self, z) -> np.ndarray:
        """|mean_d cosine(z_d, z_member,d)| for every member (missing = 0 in the z-scores)."""
        if not self.members: return np.zeros(0)
        z0 = np.nan_to_num(z).astype(np.float32); ss0 = self.cells.seg(z0.astype(np.float64) ** 2)
        out = np.empty(len(self.members))
        for i, m in enumerate(self.members):
            dot = self.cells.seg((z0 * m.z0()).astype(np.float64))   # float32 products, float64 segment sums
            den = np.sqrt(ss0 * m.ss)
            with np.errstate(all="ignore"): c = dot / den
            c = c[np.isfinite(c)]
            out[i] = abs(c.mean()) if len(c) else 0.0
        return out

    def novelty(self, z) -> float:
        c = self.corr_with(z)
        return 1.0 if len(c) == 0 else float(1.0 - c.max())

    def sa(self, emb: np.ndarray, z) -> float:
        if not self.members: return 0.0
        E = np.stack([m.emb for m in self.members]); d2 = ((E - emb[None]) ** 2).sum(1)
        k = min(KNN_K, len(self.members)); nn = np.argsort(d2)[:k]
        w = np.exp(-(d2[nn] - d2[nn].min())); w /= w.sum()                    # stable softmax of -||e_i-e_j||^2
        z0 = np.nan_to_num(z)
        beh = np.array([float(np.mean((z0 - self.members[j].z0()) ** 2)) for j in nn])
        return float(np.exp(-(w * beh).sum()))

    def try_add(self, expr, ast_hash, emb, z, ic, icir) -> str:
        """Returns 'added' | 'replaced' | 'rejected_threshold' | 'rejected_corr' | 'duplicate' | 'rejected_full'."""
        if any(m.ast_hash == ast_hash for m in self.members): return "duplicate"
        if not (np.isfinite(ic) and np.isfinite(icir)) or abs(ic) < self.ic_min or abs(icir) < self.icir_min:
            return "rejected_threshold"
        if len(self.members) and self.corr_with(z).max() > self.corr_max:
            self.rejected_corr += 1; return "rejected_corr"
        z32 = np.nan_to_num(z).astype(np.float32)
        mem = Member(expr, ast_hash, np.asarray(emb, dtype=float), z32, float(ic), float(icir), 1 if ic >= 0 else -1,
                     ss=self.cells.seg(z32.astype(np.float64) ** 2))
        if len(self.members) < self.capacity:
            self.members.append(mem); self.added += 1; return "added"
        worst = min(range(len(self.members)), key=lambda i: abs(self.members[i].ic))
        if abs(ic) > abs(self.members[worst].ic):
            self.members[worst] = mem; self.replaced += 1; return "replaced"
        return "rejected_full"

    def max_pairwise_corr(self) -> float:
        best = 0.0
        for i, a in enumerate(self.members):
            for b in self.members[i + 1:]:
                dot = self.cells.seg((a.z * b.z).astype(np.float64)); den = np.sqrt(a.ss * b.ss)
                with np.errstate(all="ignore"): c = dot / den
                c = c[np.isfinite(c)]
                best = max(best, abs(c.mean()) if len(c) else 0.0)
        return best


def weights(T: int, T_anneal: int, lam_max=LAMBDA_MAX, eta_max=ETA_MAX):
    f = max(0.0, 1.0 - T / max(T_anneal, 1))
    return f * lam_max, f * eta_max


class MultiFacetedReward:
    def __init__(self, panel, cells: Cells, pool: FactorPool, encoder=None):
        self.panel, self.cells, self.pool, self.encoder = panel, cells, pool, encoder

    def signal(self, expr: str):
        """Evaluate formula on the full loaded panel (causal) and flatten to split cells; returns z-scored vector."""
        f = evaluate(parse_expr(expr), self.panel.data)
        f = np.where(np.isfinite(f) & (np.abs(f) < 1e150), f, np.nan)
        return self.cells.zscore(self.cells.take(f))

    def __call__(self, expr: str, T: int, T_anneal: int, emb: np.ndarray | None = None) -> dict:
        z = self.signal(expr)
        ic, icir, n_days = self.cells.ic_stats(z)
        degenerate = (not np.isfinite(ic)) or np.isfinite(z).mean() < 0.5
        if emb is None:
            import torch
            with torch.no_grad(): emb = self.encoder(parse_ast(expr)).numpy()
        lam, eta = weights(T, T_anneal)
        if degenerate:
            return dict(z=z, ic=float("nan"), icir=float("nan"), r_ic=0.0, r_sa=0.0, r_nov=0.0, lam=lam, eta=eta,
                        reward=REWARD_FLOOR, degenerate=True, emb=emb)
        r_ic = abs(ic); r_nov = self.pool.novelty(z); r_sa = self.pool.sa(emb, z)
        R = max(r_ic + lam * r_sa + eta * r_nov, REWARD_FLOOR)
        return dict(z=z, ic=ic, icir=icir, r_ic=r_ic, r_sa=r_sa, r_nov=r_nov, lam=lam, eta=eta, reward=R, degenerate=False, emb=emb)
