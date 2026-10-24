"""Trader / Combiner Agent: aggregates APPROVED formulas into the active factor pool.

For each approved formula (in ledger order) it computes its cross-sectional z-scored signal on the search window and applies:
  * pairwise correlation limit  rho_ij < 0.30  (absolute value of the mean daily cross-sectional Pearson correlation between the
    candidate's signal and each pool member's signal, both sign-oriented); rejected if ANY pair reaches 0.30;
  * marginal information contribution  dIC = IC(pool + candidate) - IC(pool) > 0, where IC is the mean daily cross-sectional IC of
    the equal-weight sign-oriented z-mean against the 20-day forward return (the SDE's own definitions in src.portfolio.combine).
    The label of day t uses close t+20 and the search panel ends at the validation year's end, so the last 20 days carry no label.
The pool is capped (default 50). Blueprint extras (modified Gram-Schmidt orthogonalisation, mean-variance / ERC weights) are not
implemented: the pool is equal-weighted, which the SDE already uses as its static reference ensemble.
Signals come from a `signal_fn(expression, sign) -> (D,N)` so tests can inject a synthetic panel.
"""
from __future__ import annotations

from typing import Callable, Optional

import numpy as np

from src.portfolio.combine import combine_equal, daily_ic_matrix, label_matrix
from src.portfolio.long_short import tradable_mask, zscore_rows

from .data import SearchPanel
from .shared_ledger import SharedLedger
from .tensor_eval import evaluate_numpy
from src.dsl.grammar import parse_expr

RHO_MAX = 0.30
POOL_CAP = 50


def panel_signal_fn(panel: SearchPanel) -> Callable[[str, int], np.ndarray]:
    trad = tradable_mask(panel)

    def fn(expression: str, sign: int) -> np.ndarray:
        F = evaluate_numpy(parse_expr(expression), panel.data)
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


class Trader:
    def __init__(self, ledger: SharedLedger, signal_fn: Callable[[str, int], np.ndarray], labels: np.ndarray, first: int, last: int,
                 rho_max: float = RHO_MAX, min_delta_ic: float = 0.0, pool_cap: int = POOL_CAP):
        self.ledger, self.signal_fn, self.Y, self.first, self.last = ledger, signal_fn, labels, first, last
        self.rho_max, self.min_delta_ic, self.pool_cap = rho_max, min_delta_ic, pool_cap
        self.signals: dict[str, np.ndarray] = {}                 # ast_hash -> signal of pool members

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

    def consider(self, row: dict) -> dict:
        """Evaluate one approved ledger row; adds it to the pool if it clears both tests. Returns the decision record."""
        hashes = self._load_pool()
        z = self.signal_fn(row["canonical"], int(row["sign"] or 1))
        rhos = {h: pairwise_signal_corr(z, self.signals[h]) for h in hashes}
        worst = max((abs(r) for r in rhos.values() if np.isfinite(r)), default=0.0)
        base = self.pool_ic(hashes)
        with_c = self.pool_ic(hashes, z)
        d_ic = with_c - base
        dec = {"trial_id": row["id"], "ast_hash": row["ast_hash"], "max_abs_rho": worst, "delta_ic": d_ic, "ic_without": base, "ic_with": with_c,
               "pool_size_before": len(hashes)}
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
        self.ledger.set_trader_status(row["id"], dec["decision"])
        return dec

    def run_once(self) -> list[dict]:
        return [self.consider(r) for r in self.ledger.approved_untraded()]
