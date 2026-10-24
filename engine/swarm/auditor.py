"""Screener / Auditor Agent: four statistical gates over worker return vectors read from the shared trial database.

A candidate is APPROVED only if ALL gates pass (blueprint Table 3; thresholds are the directive's):
  1. CPCV purging & embargoing - the only thing a parameter-free formula "fits" is its long/short sign. For every CPCV split
     (10 groups, 2 test groups, purge 20 rows = the label horizon, embargo 5) the sign is re-chosen on the PURGED training rows
     and applied to the held-out groups; out-of-sample path Sharpes are assembled from the splits. Gate: median path Sharpe > 0
     and at least `cpcv_min_pos_frac` (80%, our choice, the blueprint gives none) of paths positive. This is the leakage guard.
  2. PBO < 0.10 via CSCV (Bailey et al. 2017; 16 slices -> 12,870 IS/OOS splits) over the COHORT: the candidate plus the most
     recent evaluated trials (up to `cohort_cap`). PBO describes the selection process, so it is a cohort-level number.
  3. DSR p-value < 0.05 (p = 1 - DSR) with the GLOBAL trial count N_trials from the shared ledger (baseline offset included)
     and the cross-trial variance of per-period Sharpe ratios (empirical when >= 10 trials, else the null value 1/T).
  4. Hansen SPA (stationary bootstrap, consistent re-centring) of the cohort against the zero-return benchmark, as a candidate-level
     test: the candidate's studentised statistic is compared with the bootstrap distribution of the MAXIMUM statistic over the whole
     cohort (single-step, family-wise error 5%), so searching many formulas cannot manufacture significance.
Gates are computed for every candidate (cheap ones first, CSCV/SPA once per cohort) so rejected formulas get complete feedback.
Bundles are Ed25519-signed per role (`signing.py`): the Auditor verifies the Worker's signature over the stored return vectors
before auditing, and signs its own verdict for the Trader. Costs come from the Worker's stored per-day `cost` vector (flat +
square-root impact). Turnover (<12x) and net-Sharpe flags are recorded as informational flags, not gates.
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from typing import Optional

import numpy as np

from src.validation.cpcv import cpcv_paths, cpcv_splits, group_bounds
from src.validation.cscv import cscv_pbo
from src.validation.dsr import deflated_sharpe
from src.validation.spa import stationary_bootstrap_idx

from .shared_ledger import SharedLedger
from .signing import KeyStore, audit_payload, result_payload


@dataclass
class AuditConfig:
    pbo_max: float = 0.10
    dsr_p_max: float = 0.05
    spa_p_max: float = 0.05
    cpcv_groups: int = 10
    cpcv_k: int = 2
    cpcv_purge: int = 20
    cpcv_embargo: int = 5
    cpcv_min_pos_frac: float = 0.8
    cohort_cap: int = 100
    min_cohort: int = 5
    cscv_slices: int = 16
    spa_B: int = 1000
    spa_block: float = 10.0
    seed: int = 0


def _sr(r: np.ndarray) -> float:
    sd = r.std(ddof=1)
    return float(r.mean() / sd) if sd > 0 else 0.0


def gate_cpcv(gross: np.ndarray, turnover: np.ndarray, cost_bps: float, cfg: AuditConfig, cost: Optional[np.ndarray] = None) -> dict:
    """Leak-free sign selection inside purged/embargoed CPCV folds; returns path-Sharpe summary and the verdict."""
    T = len(gross)
    splits = cpcv_splits(T, cfg.cpcv_groups, cfg.cpcv_k, cfg.cpcv_purge, cfg.cpcv_embargo)
    cost = cost_bps * 1e-4 * turnover if cost is None else cost          # the Worker's own per-day cost vector (flat + impact) when stored
    rets, signs = [], []
    for s in splits:
        tr = s["train"]
        sign = 1.0 if (gross[tr].sum() >= 0 if tr.any() else True) else -1.0     # learned ONLY from purged training rows
        signs.append(sign)
        rets.append(sign * gross - cost)
    gb = group_bounds(T, cfg.cpcv_groups)                              # list of (start, stop)
    paths = []
    for p in cpcv_paths(splits, cfg.cpcv_groups):
        paths.append(np.concatenate([rets[si][gb[g][0]:gb[g][1]] for g, si in p]))
    ann = np.array([np.sqrt(252) * _sr(p) for p in paths])
    frac = float((ann > 0).mean())
    sign_consistency = float(abs(np.mean(signs)))
    ok = bool(np.median(ann) > 0 and frac >= cfg.cpcv_min_pos_frac)
    return {"pass": ok, "n_splits": len(splits), "n_paths": len(paths), "median_path_sharpe": float(np.median(ann)),
            "min_path_sharpe": float(ann.min()), "frac_paths_positive": frac, "sign_consistency": sign_consistency}


def gate_dsr(net: np.ndarray, n_trials: int, var_sr: float, n_var: int, cfg: AuditConfig) -> dict:
    T = len(net)
    empirical = n_var >= 10 and np.isfinite(var_sr) and var_sr > 0
    v = var_sr if empirical else 1.0 / max(T, 2)
    d = deflated_sharpe(net, n_trials, v)
    dsr = d.get("dsr")
    p = None if dsr is None or not np.isfinite(dsr) else float(1.0 - dsr)
    return {"pass": bool(p is not None and p < cfg.dsr_p_max), "dsr": dsr, "p_value": p, "sr_annual": d.get("sr_annual"),
            "sr0_annual": d.get("sr0_annual"), "n_trials": int(n_trials), "var_sr_used": float(v), "var_source": "empirical" if empirical else "null_1_over_T",
            "n_var_trials": int(n_var), "T": int(T)}


def spa_candidate_pvalues(D: np.ndarray, B: int = 1000, mean_block: float = 10.0, seed: int = 0) -> dict:
    """Hansen (2005) SPA machinery (consistent re-centring) with candidate-level adjusted p-values.

    D is (T, K): candidate minus benchmark daily returns. Returns the cohort p (= `src.validation.spa.spa_test` semantics) and, for
    every candidate k, p_k = P*(max_j t*_j >= t_k): the probability under the re-centred null that the best of the K studentised
    statistics is at least as large as candidate k's own.
    """
    D = np.nan_to_num(np.asarray(D, float))
    T, K = D.shape
    rng = np.random.default_rng(seed)
    dbar = D.mean(0)
    idx = stationary_bootstrap_idx(T, B, mean_block, rng)
    bar_star = np.stack([D[idx[b]].mean(0) for b in range(B)])
    omega = np.sqrt(np.maximum(T * bar_star.var(0, ddof=1), 1e-20))
    t_k = np.sqrt(T) * dbar / omega
    mu_c = np.where(t_k <= -np.sqrt(2.0 * np.log(np.log(T))), dbar, 0.0)
    tstar_max = np.max(np.sqrt(T) * (bar_star - dbar + mu_c) / omega, axis=1)
    tstar_max = np.maximum(tstar_max, 0.0)
    p_k = np.array([float(np.mean(tstar_max >= max(t, 0.0))) for t in t_k])
    stat = max(0.0, float(t_k.max()))
    return {"p_candidate": p_k, "t_stat": t_k, "p_cohort": float(np.mean(tstar_max >= stat)), "K": int(K), "T": int(T), "B": int(B)}


def audit_cohort(items: list[dict], n_trials: int, var_sr: float, n_var: int, cfg: AuditConfig, targets: Optional[set] = None) -> dict:
    """Pure function: items = [{'id','net','gross','turnover','cost_bps','metrics'}...]. Returns {id: audit_bundle}.
    `targets` limits which ids get a verdict (the rest are cohort context only)."""
    targets = targets if targets is not None else {i["id"] for i in items}
    out: dict = {}
    T = min(len(i["net"]) for i in items)
    M = np.column_stack([i["net"][-T:] for i in items])
    S = M.shape[1]
    cohort_ok = S >= cfg.min_cohort
    pbo = cscv_pbo(M, cfg.cscv_slices) if cohort_ok else {"pbo": float("nan"), "reason": f"cohort of {S} < {cfg.min_cohort}"}
    spa = spa_candidate_pvalues(M, cfg.spa_B, cfg.spa_block, cfg.seed) if cohort_ok else None
    for j, it in enumerate(items):
        if it["id"] not in targets:
            continue
        g_cpcv = gate_cpcv(it["gross"][-T:], it["turnover"][-T:], it["cost_bps"], cfg, None if it.get("cost") is None else it["cost"][-T:])
        g_dsr = gate_dsr(it["net"][-T:], n_trials, var_sr, n_var, cfg)
        pbo_v = pbo.get("pbo")
        g_pbo = {"pass": bool(pbo_v is not None and np.isfinite(pbo_v) and pbo_v < cfg.pbo_max), "pbo": None if pbo_v is None or not np.isfinite(pbo_v) else float(pbo_v),
                 "cohort_size": S, "n_splits": pbo.get("n_splits"), "median_logit": pbo.get("median_logit"), "scope": "cohort",
                 **({"reason": pbo["reason"]} if "reason" in pbo else {})}
        if spa is not None:
            pk = float(spa["p_candidate"][j])
            g_spa = {"pass": bool(pk <= cfg.spa_p_max), "p_candidate": pk, "p_cohort": spa["p_cohort"], "t_stat": float(spa["t_stat"][j]), "K": spa["K"], "B": spa["B"]}
        else:
            g_spa = {"pass": False, "p_candidate": None, "p_cohort": None, "reason": "cohort too small"}
        gates = {"cpcv": g_cpcv, "pbo": g_pbo, "dsr": g_dsr, "spa": g_spa}
        failed = [k for k, v in gates.items() if not v["pass"]]
        m = it.get("metrics", {})
        flags = {"turnover_gt_12x": bool((m.get("annualized_turnover") or 0) > 12.0), "net_sharpe_lt_0_8": bool((m.get("search_sharpe") or 0) < 0.8)}
        out[it["id"]] = {"overall_status": "APPROVED" if not failed else "REJECTED", "failed_gates": failed, "gates": gates, "flags": flags,
                         "rejection_reason": None if not failed else {"cpcv": "CPCV_LEAKAGE_OR_UNSTABLE", "pbo": "PBO_EXCEEDED", "dsr": "DSR_TOO_LOW",
                                                                      "spa": "SPA_NOT_SIGNIFICANT"}[failed[0]],
                         "n_trials_at_audit": int(n_trials), "config": asdict(cfg), "ast_hash": it.get("ast_hash"),
                         "scope": "search data only (train 2010-2016 + validation 2017); research candidate, long-short, NOT tradable on the desk"}
    return out


class Auditor:
    def __init__(self, ledger: SharedLedger, cfg: Optional[AuditConfig] = None, keystore: Optional[KeyStore] = None,
                 require_signature: bool = True, coordinator=None, refresh_baseline_s: float = 30.0):
        self.ledger, self.cfg = ledger, cfg or AuditConfig()
        self.keystore, self.require_signature, self.coord, self.refresh_s = keystore, require_signature, coordinator, refresh_baseline_s

    def _item(self, row: dict) -> Optional[dict]:
        r = self.ledger.get_returns(row["id"])
        if r is None:
            return None
        m = json.loads(row["metrics_json"] or "{}")
        return {"id": row["id"], "ast_hash": row["ast_hash"], "net": r["net"], "gross": r["gross"], "turnover": r["turnover"],
                "cost": r.get("cost"), "cost_bps": m.get("cost_bps", 5.0), "metrics": m}

    def _verify_result(self, row: dict, item: dict) -> tuple[bool, str]:
        """Check the Worker's signature over the stored result (metrics + return vectors). Unsigned rows only pass when signatures are optional."""
        if self.keystore is None:
            return True, "signatures off"
        sig = json.loads(row["result_sig"]) if row.get("result_sig") else None
        if sig is None:
            return (not self.require_signature), "unsigned result"
        payload = result_payload(row["id"], row["ast_hash"], json.loads(row["metrics_json"] or "{}").get("worker", ""), item["metrics"],
                                 item["net"], item["gross"], item["turnover"], item["cost"])
        return self.keystore.verify(payload, sig, "worker")

    def audit_pending(self, limit: int = 200) -> dict:
        """Audit every evaluated, un-audited trial (one cohort pass). Returns {'approved': [...ids], 'rejected': [...ids]}.
        The pass holds the (Redis, if configured) audit lock so two auditor processes never audit the same cohort; the baseline is
        re-read live first so N reflects the engine + SDE ledgers as they are now."""
        if self.coord is not None:
            with self.coord.lock("audit", ttl_ms=120_000, wait_s=30.0) as got:
                if not got:
                    return {"approved": [], "rejected": [], "audited": 0, "skipped": "audit lock busy"}
                return self._audit_pending(limit)
        return self._audit_pending(limit)

    def _audit_pending(self, limit: int) -> dict:
        self.ledger.maybe_refresh_baseline(self.refresh_s)
        rows = self.ledger.evaluated_unaudited(limit)
        if not rows:
            return {"approved": [], "rejected": [], "audited": 0}
        ids = {r["id"] for r in rows}
        ctx = self.ledger.recent_evaluated(max(self.cfg.cohort_cap - len(rows), 0), exclude=ids)
        items, bad = [], {}
        for r in rows + ctx:
            it = self._item(r)
            if it is None:
                continue
            ok, why = self._verify_result(r, it)
            if not ok:
                if r["id"] in ids:                              # a target with a bad result signature is rejected outright, never audited
                    bad[r["id"]] = why
                    continue
                continue                                         # a bad context row is simply excluded from the cohort
            items.append(it)
        var_sr, n_var = self.ledger.sharpe_variance()
        res = audit_cohort(items, self.ledger.n_trials(), var_sr, n_var, self.cfg, targets=ids - set(bad)) if items else {}
        approved, rejected = [], []
        for tid, why in bad.items():
            row = next(r for r in rows if r["id"] == tid)
            bundle = {"overall_status": "REJECTED", "failed_gates": ["signature"], "gates": {"signature": {"pass": False, "reason": why}},
                      "rejection_reason": "BAD_RESULT_SIGNATURE", "n_trials_at_audit": int(self.ledger.n_trials()), "ast_hash": row["ast_hash"], "flags": {}}
            res[tid] = bundle
        for tid, bundle in res.items():
            if self.keystore is not None:
                row = next(r for r in rows if r["id"] == tid)
                bundle["signature"] = self.keystore.sign("auditor", audit_payload(tid, row["ast_hash"], bundle))
            self.ledger.set_audit(tid, bundle["overall_status"], bundle)
            (approved if bundle["overall_status"] == "APPROVED" else rejected).append(tid)
        self.ledger.log_event("auditor", "audit_pass", {"audited": len(res), "approved": len(approved), "n_trials": self.ledger.n_trials(),
                                                         "cohort": len(items)})
        return {"approved": approved, "rejected": rejected, "audited": len(res)}
