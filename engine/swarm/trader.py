"""Trader / Combiner Agent: aggregates APPROVED formulas into the active factor pool.

For each approved formula (in ledger order) it computes its cross-sectional z-scored signal on the search window and applies:
  * pairwise correlation limit  rho_ij < 0.30  (absolute value of the mean daily cross-sectional Pearson correlation between the
    candidate's signal and each pool member's signal, both sign-oriented); rejected if ANY pair reaches 0.30;
  * marginal information contribution  dIC = IC(pool + candidate) - IC(pool) > 0, where IC is the mean daily cross-sectional IC of
    the equal-weight sign-oriented z-mean against the 20-day forward return (the SDE's own definitions in src.portfolio.combine).
    The label of day t uses close t+20 and the search panel ends at the validation year's end, so the last 20 days carry no label.
The pool is capped (default 50). Admission is decided by the two tests above (equal-weight IC, the SDE's static reference ensemble).
Alongside them the Trader now implements the blueprint's combiner maths:
  * modified Gram-Schmidt orthogonalisation of the pool signals (`mgs_orthogonalise`) - each decision records how much of the
    candidate is new (`orth_residual_frac`) and the IC of its orthogonalised residual;
  * risk-optimal factor weights (`allocate`): max-Sharpe mean-variance (long-only simplex, shrinkage covariance, SLSQP) or equal-risk
    contribution (risk parity), computed on the pool members' stored net-return streams; the resulting asset book is capped at 5% per
    name. The allocation is stored in the ledger meta (`allocation`) after every integration. It does not change which factors are admitted.
Signals come from a `signal_fn(expression, sign) -> (D,N)` so tests can inject a synthetic panel.
"""
from __future__ import annotations

from typing import Callable, Optional

import numpy as np

from src.portfolio.combine import combine_equal, daily_ic_matrix, label_matrix
from src.portfolio.long_short import leverage_normalized_weights, tradable_mask, zscore_rows

from .data import SearchPanel
from .shared_ledger import SharedLedger
from .dialect import evaluate_any, parse_any
from .signing import KeyStore, audit_payload

RHO_MAX = 0.30
POOL_CAP = 50


def panel_signal_fn(panel: SearchPanel) -> Callable[[str, int], np.ndarray]:
    trad = tradable_mask(panel)

    def fn(expression: str, sign: int) -> np.ndarray:
        F = evaluate_any(parse_any(expression), panel.data, mask=trad)
        F = np.where(np.isfinite(F) & (np.abs(F) < 1e150), F, np.nan)
        return sign * zscore_rows(F, trad)

    return fn


def pairwise_signal_corr(A: np.ndarray, B: np.ndarray, min_n: int = 30) -> float:
    """Mean over days of the cross-sectional Pearson correlation of two (D,N) signals (days with < min_n common assets skipped)."""
    ok = np.isfinite(A) & np.isfinite(B)
    n = ok.sum(1)
    a, b = np.where(ok, A, 0.0), np.where(ok, B, 0.0)
    a = np.where(ok, a - (a.sum(1) / np.maximum(n, 1))[:, None], 0.0)
    b = np.where(ok, b - (b.sum(1) / np.maximum(n, 1))[:, None], 0.0)
    with np.errstate(all="ignore"):
        r = (a * b).sum(1) / np.sqrt((a * a).sum(1) * (b * b).sum(1))
    r = r[(n >= min_n) & np.isfinite(r)]
    return float(r.mean()) if len(r) else float("nan")


def mean_ic(Z: np.ndarray, Y: np.ndarray, first: int, last: int) -> float:
    """Mean daily cross-sectional IC of a (D,N) signal over rows [first,last)."""
    ic = daily_ic_matrix(Z[None, first:last], Y[first:last])[0]
    ic = ic[np.isfinite(ic)]
    return float(ic.mean()) if len(ic) else float("nan")


def _vec(Z: np.ndarray, first: int, last: int) -> np.ndarray:
    return np.nan_to_num(Z[first:last], nan=0.0, posinf=0.0, neginf=0.0).ravel()


def mgs_orthogonalise(Zs: list[np.ndarray], first: int = 0, last: Optional[int] = None) -> tuple[list[np.ndarray], np.ndarray]:
    """Modified Gram-Schmidt over (D,N) signals, inner product = sum over days and assets (NaN -> 0). Returns the orthogonal
    residuals Q_k (same shape, NaN where the input was NaN) and the matrix R with Z_k = sum_j R[j,k] Q_j (upper triangular).
    MGS (project out each earlier q from the *running* residual) is the numerically stable variant."""
    last = Zs[0].shape[0] if last is None else last
    X = [_vec(z, first, last).astype(float) for z in Zs]
    k = len(X)
    Q, R = [], np.zeros((k, k))
    for i in range(k):
        v = X[i].copy()
        for j in range(len(Q)):
            R[j, i] = Q[j] @ v / (Q[j] @ Q[j])
            v -= R[j, i] * Q[j]
        R[i, i] = 1.0
        Q.append(v)
    out = []
    for i, q in enumerate(Q):
        a = np.full(Zs[i].shape, np.nan)
        a[first:last] = q.reshape(last - first, -1)
        a[~np.isfinite(Zs[i])] = np.nan
        out.append(a)
    return out, R


def shrink_cov(R: np.ndarray) -> np.ndarray:
    """Ledoit-Wolf shrinkage covariance (sklearn) with a fixed-intensity fallback; R is (T, K)."""
    try:
        from sklearn.covariance import LedoitWolf
        return LedoitWolf().fit(R).covariance_
    except Exception:
        S = np.cov(R, rowvar=False).reshape(R.shape[1], R.shape[1])
        return 0.8 * S + 0.2 * np.trace(S) / len(S) * np.eye(len(S))


def erc_weights(cov: np.ndarray) -> np.ndarray:
    """Equal risk contribution (risk parity), long-only: minimise 0.5 w'Sw - (1/K) sum log w (convex, unique), then normalise."""
    from scipy.optimize import minimize
    K = len(cov)
    if K == 1:
        return np.ones(1)
    s = np.sqrt(np.diag(cov))
    x0 = (1.0 / s) / (1.0 / s).sum()
    f = lambda w: 0.5 * w @ cov @ w - np.log(w).sum() / K
    g = lambda w: cov @ w - 1.0 / (K * w)
    res = minimize(f, x0, jac=g, method="L-BFGS-B", bounds=[(1e-10, None)] * K)
    w = np.maximum(res.x, 1e-12)
    return w / w.sum()


def mvo_weights(mu: np.ndarray, cov: np.ndarray) -> np.ndarray:
    """Max-Sharpe mean-variance weights on the long-only simplex (SLSQP). Falls back to ERC if no factor has positive expected return."""
    from scipy.optimize import minimize
    K = len(mu)
    if K == 1:
        return np.ones(1)
    if not np.any(mu > 0):
        return erc_weights(cov)
    f = lambda w: -(mu @ w) / np.sqrt(max(w @ cov @ w, 1e-18))
    x0 = np.ones(K) / K
    res = minimize(f, x0, method="SLSQP", bounds=[(0.0, 1.0)] * K, constraints=[{"type": "eq", "fun": lambda w: w.sum() - 1.0}],
                   options={"maxiter": 200, "ftol": 1e-10})
    w = np.clip(res.x if res.success else x0, 0.0, None)
    return w / w.sum()


def cap_assets(w: np.ndarray, cap: float = 0.05, iters: int = 50) -> tuple[np.ndarray, int]:
    """Cap |w_i| <= cap, rescaling the uncapped names to keep gross exposure where possible. Returns (weights, #capped)."""
    w = np.nan_to_num(w.copy())
    gross = np.abs(w).sum()
    free = np.ones(len(w), bool)
    for _ in range(iters):
        over = free & (np.abs(w) > cap + 1e-15)
        if not over.any():
            break
        w[over] = np.sign(w[over]) * cap
        free &= ~over
        room = gross - np.abs(w[~free]).sum()
        cur = np.abs(w[free]).sum()
        if cur > 0 and room > 0:
            w[free] *= room / cur
    return w, int((~free).sum())


class Trader:
    def __init__(self, ledger: SharedLedger, signal_fn: Callable[[str, int], np.ndarray], labels: np.ndarray, first: int, last: int,
                 rho_max: float = RHO_MAX, min_delta_ic: float = 0.0, pool_cap: int = POOL_CAP, allocation: str = "mvo",
                 asset_cap: float = 0.05, keystore: Optional[KeyStore] = None, require_signature: bool = True):
        self.ledger, self.signal_fn, self.Y, self.first, self.last = ledger, signal_fn, labels, first, last
        self.rho_max, self.min_delta_ic, self.pool_cap = rho_max, min_delta_ic, pool_cap
        self.signals: dict[str, np.ndarray] = {}                 # ast_hash -> signal of pool members
        self.allocation_method, self.asset_cap = allocation, asset_cap
        self.keystore, self.require_signature = keystore, require_signature

    @classmethod
    def from_panel(cls, ledger: SharedLedger, panel: SearchPanel, **kw) -> "Trader":
        Y = label_matrix(panel.data["$close"], tradable_mask(panel))
        return cls(ledger, panel_signal_fn(panel), Y, panel.start_idx, panel.n_days, **kw)

    def _load_pool(self) -> list[str]:
        for m in self.ledger.pool_members():
            if m["ast_hash"] not in self.signals:
                self.signals[m["ast_hash"]] = self.signal_fn(m["canonical"], int(m["sign"] or 1))
        return [m["ast_hash"] for m in self.ledger.pool_members()]

    def pool_ic(self, hashes: list[str], extra: Optional[np.ndarray] = None) -> float:
        Zs = [self.signals[h] for h in hashes] + ([extra] if extra is not None else [])
        if not Zs:
            return 0.0
        return mean_ic(combine_equal(np.stack(Zs)), self.Y, self.first, self.last)

    def _verify_verdict(self, row: dict) -> tuple[bool, str]:
        if self.keystore is None:
            return True, "signatures off"
        import json
        audit = json.loads(row["audit_json"]) if row.get("audit_json") else {}
        sig = audit.get("signature")
        if sig is None:
            return (not self.require_signature), "unsigned verdict"
        return self.keystore.verify(audit_payload(row["id"], row["ast_hash"], audit), sig, "auditor")

    def allocate(self, method: Optional[str] = None) -> Optional[dict]:
        """Risk-optimal factor weights for the current pool (MVO / ERC / equal) from the members' stored net returns, plus the
        resulting asset book (last day) capped per name. Stored in ledger meta `allocation`. None if returns are unavailable."""
        method = method or self.allocation_method
        members = self.ledger.pool_members()
        if not members:
            return None
        series = []
        for m in members:
            r = self.ledger.get_returns(m["trial_id"])
            if r is None or r.get("net") is None:
                return None
            series.append(r["net"])
        T = min(len(s) for s in series)
        R = np.column_stack([s[-T:] for s in series])
        mu, cov = R.mean(0), shrink_cov(R)
        w = {"equal": lambda: np.ones(len(mu)) / len(mu), "erc": lambda: erc_weights(cov), "mvo": lambda: mvo_weights(mu, cov)}[method]()
        hashes = [m["ast_hash"] for m in members]
        out = {"method": method, "n_factors": len(members), "weights": {h: float(x) for h, x in zip(hashes, w)},
               "exp_daily_return": float(mu @ w), "daily_vol": float(np.sqrt(w @ cov @ w)),
               "risk_contrib": {h: float(x) for h, x in zip(hashes, w * (cov @ w) / max(w @ cov @ w, 1e-30))}}
        if all(h in self.signals for h in hashes):
            book = sum(wk * leverage_normalized_weights(self.signals[h])[-1] for wk, h in zip(w, hashes))
            capped, n_cap = cap_assets(book, self.asset_cap)
            out.update(asset_cap=self.asset_cap, n_assets_capped=n_cap, gross_before_cap=float(np.abs(np.nan_to_num(book)).sum()),
                       gross_after_cap=float(np.abs(capped).sum()), max_abs_asset_weight=float(np.abs(capped).max()))
        self.ledger.set_meta("allocation", out)
        return out

    def consider(self, row: dict) -> dict:
        """Evaluate one approved ledger row; adds it to the pool if it clears both tests. Returns the decision record."""
        ok, why = self._verify_verdict(row)
        if not ok:
            dec = {"trial_id": row["id"], "ast_hash": row["ast_hash"], "decision": "REJECTED_BAD_SIGNATURE", "reason": why}
            self.ledger.set_trader_status(row["id"], dec["decision"])
            return dec
        hashes = self._load_pool()
        z = self.signal_fn(row["canonical"], int(row["sign"] or 1))
        rhos = {h: pairwise_signal_corr(z, self.signals[h]) for h in hashes}
        worst = max((abs(r) for r in rhos.values() if np.isfinite(r)), default=0.0)
        base = self.pool_ic(hashes)
        with_c = self.pool_ic(hashes, z)
        d_ic = with_c - base
        dec = {"trial_id": row["id"], "ast_hash": row["ast_hash"], "max_abs_rho": worst, "delta_ic": d_ic, "ic_without": base, "ic_with": with_c,
               "pool_size_before": len(hashes)}
        if hashes:                                               # how much of the candidate is NOT explained by the pool (MGS residual)
            Q, _ = mgs_orthogonalise([self.signals[h] for h in hashes] + [z], self.first, self.last)
            n_full, n_res = np.linalg.norm(_vec(z, self.first, self.last)), np.linalg.norm(_vec(Q[-1], self.first, self.last))
            dec["orth_residual_frac"] = float(n_res / n_full) if n_full > 0 else float("nan")
            dec["orth_residual_ic"] = mean_ic(Q[-1], self.Y, self.first, self.last)
        if len(hashes) >= self.pool_cap:
            dec.update(decision="REJECTED_POOL_FULL")
        elif worst >= self.rho_max:
            dec.update(decision="REJECTED_CORRELATED")
        elif not np.isfinite(d_ic) or d_ic <= self.min_delta_ic:
            dec.update(decision="REJECTED_NO_DELTA_IC")
        else:
            dec.update(decision="INTEGRATED")
            self.signals[row["ast_hash"]] = z
            self.ledger.add_to_pool(row["id"], row["ast_hash"], d_ic, worst, dec)
            dec["allocation"] = (self.allocate() or {}).get("weights")
        self.ledger.set_trader_status(row["id"], dec["decision"])
        return dec

    def run_once(self) -> list[dict]:
        return [self.consider(r) for r in self.ledger.approved_untraded()]
