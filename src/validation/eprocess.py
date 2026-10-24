"""Ville e-process promotion gate on the append-only ledger ("Promote", Benhamou et al. 2026, doi:10.36287/setsci.25.3.001).

Implemented as published in the paper text:
  score    s_t = clip(R_net_t / scale, -1, 1)           scale = max(50 bp, training 99.5th pct |R_net|), predictable
  null     E[s_t | F_{t-1}] <= 0 for every post-birth date t
  process  E_t(lam) = prod_{u=birth+1..t} (1 + lam s_u),  E_bar_t = mean over Lambda = {.025,.05,.10,.20,.35}; E_birth = 1
  budget   candidate h receives mass m_h, sum_h m_h <= 1 for the program's lifetime (nonrefundable debit)
  promote  first t with E_bar_t >= 1/(alpha m_h)   => P(any false promotion) <= alpha (Ville + union bound, any dependence)
  clock    crossing at close t -> execute at close t+1 -> first credited return ends t+2
Evidence starts at 1 at birth and only post-birth scores are used. Registration, debit and every score are appended to the
same hash-chained ledger (kinds "candidate" and "escore"); a birth that would push the cumulative debit above 1 is rejected,
and a row is idempotent on (candidate, event_time, data_version).
"""
from __future__ import annotations
import hashlib, json
import numpy as np
from src.audit.ledger import Ledger

LAMBDAS = (0.025, 0.05, 0.10, 0.20, 0.35)
MIN_SCALE = 0.005   # 50 bp


def predictable_scale(train_net: np.ndarray) -> float:
    a = np.abs(np.asarray(train_net, float)); a = a[np.isfinite(a)]
    return float(max(MIN_SCALE, np.percentile(a, 99.5))) if len(a) else MIN_SCALE


def scores(net: np.ndarray, scale: float) -> np.ndarray:
    return np.clip(np.asarray(net, float) / scale, -1.0, 1.0)


def mixture_path(s: np.ndarray, lambdas=LAMBDAS) -> np.ndarray:
    """E_bar_t for t = 1..len(s) (excludes the initial 1). Computed in logs for stability."""
    s = np.asarray(s, float)
    logs = np.stack([np.cumsum(np.log1p(lam * s)) for lam in lambdas])           # (L, T)   (|lam s| <= .35 < 1)
    return np.exp(logs).mean(0)


def boundary(alpha: float, mass: float) -> float:
    return 1.0 / (alpha * mass)


def first_crossing(path: np.ndarray, bound: float):
    hit = np.flatnonzero(path >= bound)
    return int(hit[0]) if len(hit) else None


def naive_repeated_test(net: np.ndarray, alpha: float = 0.05, min_n: int = 63) -> dict:
    """The paper's deliberately naive comparator: repeated one-sided t-test, no multiplicity / optional-stopping correction."""
    from scipy import stats
    net = np.asarray(net, float); c1 = np.cumsum(net); c2 = np.cumsum(net ** 2); first = None
    for n in range(max(min_n, 3), len(net) + 1):
        var = (c2[n - 1] - c1[n - 1] ** 2 / n) / (n - 1)
        if var <= 0: continue
        z = np.sqrt(n) * (c1[n - 1] / n) / np.sqrt(var)
        if 1 - stats.norm.cdf(z) <= alpha: first = n; break
    return dict(crossed=first is not None, first_session=first)


def candidate_fingerprint(package: dict) -> str:
    return hashlib.sha256(json.dumps(package, sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


def cumulative_debit(ledger: Ledger, program: str) -> float:
    return float(sum(e.get("mass", 0.0) for e in ledger.entries() if e.get("kind") == "candidate" and e.get("program") == program))


def register_candidate(ledger: Ledger, program: str, package: dict, parent: str | None, birth: str, mass: float, scale: float,
                       alpha: float, data_version: str, extra: dict | None = None) -> dict:
    """Freeze + fingerprint the executable package, debit `mass` from the lifetime account (<= 1)."""
    fp = candidate_fingerprint(package)
    for e in ledger.entries():
        if e.get("kind") == "candidate" and e.get("program") == program and e.get("fingerprint") == fp:
            return e                                               # idempotent: same identity is never re-debited
    if cumulative_debit(ledger, program) + mass > 1.0 + 1e-12:
        raise ValueError(f"birth rejected: cumulative debit would exceed 1 (program {program})")
    return ledger.append(dict(kind="candidate", program=program, fingerprint=fp, parent=parent, birth=birth, mass=mass,
                              scale=scale, alpha=alpha, lambdas=list(LAMBDAS), boundary=boundary(alpha, mass), data_version=data_version,
                              package=package, **(extra or {})))


def score_candidate(ledger: Ledger, program: str, fingerprint: str, dates, net: np.ndarray, cost: np.ndarray, scale: float, mass: float,
                    alpha: float, data_version: str, write_rows: bool = True) -> dict:
    """Post-birth scoring. `dates[i]` is the date the return `net[i]` is realised (strictly after birth). Appends one row per event."""
    s = scores(net, scale); path = mixture_path(s); bound = boundary(alpha, mass)
    seen = {(e.get("candidate"), e.get("event_time"), e.get("data_version")) for e in ledger.entries() if e.get("kind") == "escore"} if write_rows else set()
    cross = first_crossing(path, bound)
    if write_rows:
        for i, d in enumerate(dates):
            key = (fingerprint, str(d), data_version)
            if key in seen: continue
            ledger.append(dict(kind="escore", program=program, candidate=fingerprint, event_time=str(d), data_version=data_version,
                               score=float(s[i]), net_return=float(net[i]), cost=float(cost[i]), evidence=float(path[i]), boundary=bound,
                               decision="promote" if (cross is not None and i == cross) else "hold",
                               first_executable_session=str(dates[cross + 2]) if (cross is not None and i == cross and cross + 2 < len(dates)) else None))
    return dict(final_evidence=float(path[-1]) if len(path) else 1.0, max_evidence=float(path.max()) if len(path) else 1.0, boundary=bound,
                promoted=cross is not None, crossing_index=cross, crossing_date=str(dates[cross]) if cross is not None else None,
                first_executable_session=str(dates[cross + 2]) if cross is not None and cross + 2 < len(dates) else None,
                n_scores=int(len(s)), mean_score=float(s.mean()) if len(s) else float("nan"), scale=scale, mass=mass, alpha=alpha,
                naive=naive_repeated_test(np.asarray(net, float)))
