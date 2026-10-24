"""Backtest Worker node: AST JSON in -> per-period return vectors + execution metrics into the shared ledger.

Pipeline (blueprint state GPU_EVAL): validate payload (strict AST JSON, hash must match) -> tensor-evaluate the formula
(`tensor_eval`, torch, CUDA if available) -> cross-sectional z-score -> dollar-neutral, leverage-normalised long-short weights
-> daily backtest with one-way costs (`src.portfolio.long_short`, shared with the SDE so the arithmetic is identical).
Orientation: the sign (long the high or low values) is chosen from the TRAIN period's gross mean only; validation is never
used to pick it. The stored vector covers train+validation (the whole search window) with a common calendar for every
trial, which CSCV/CPCV need. Raw (sign-free) gross returns and turnover are stored too so the Auditor can re-pick the sign
inside purged CPCV folds.
Costs: flat `cost_bps` per dollar traded (SDE convention) plus, when an `ImpactModel` is given, the blueprint's square-root market
impact (`costs.py`); the combined per-day `cost` vector is stored so the Auditor subtracts exactly what the Worker charged.
Not modelled: shorting borrow cost.
Research only: long-short books are not tradable on the paper desk (it blocks shorting).
"""
from __future__ import annotations

import os
import signal
import time
import traceback
from typing import Optional

import numpy as np
from scipy import stats

from src.portfolio.long_short import backtest, leverage_normalized_weights, metrics, tradable_mask, zscore_rows

from .costs import ImpactModel, adv_sigma, check_turnover, impact_cost
from .data import SearchPanel
from .dialect import evaluate_any, hash_any, payload_to_node_any
from .shared_ledger import SharedLedger
from .signing import KeyStore, result_payload, task_payload
from .simplify import degenerate_reasons
from .tensor_eval import pick_device

COST_BPS = 5.0
MIN_VALID_FRACTION = 0.6


class EvalError(Exception):
    pass


def evaluate_formula(node, panel: SearchPanel, device=None, cost_bps: float = COST_BPS, trad: Optional[np.ndarray] = None,
                     impact: Optional[ImpactModel] = None, adv_sig: Optional[tuple] = None) -> dict:
    """Backtest one AST (either dialect) on the search window. Returns arrays + metrics; raises EvalError for unusable formulas.
    `impact`: square-root market-impact model charged on top of the flat `cost_bps` (None = flat cost only, the SDE convention)."""
    reasons = degenerate_reasons(node)
    if reasons:                                           # defence in depth: the Miner already rejects these before they cost a trial
        raise EvalError(f"degenerate formula ({'+'.join(reasons)})")
    trad = tradable_mask(panel) if trad is None else trad
    F = evaluate_any(node, panel.data, device, mask=trad)
    F = np.where(np.isfinite(F) & (np.abs(F) < 1e150), F, np.nan)
    sig = zscore_rows(F, trad)
    a0, a1, D = panel.start_idx, panel.train_end_idx, panel.n_days
    valid = np.isfinite(sig[a0:D - 1]).any(1)
    if valid.mean() < MIN_VALID_FRACTION:
        raise EvalError(f"signal valid on only {valid.mean():.0%} of search days")
    close = panel.data["$close"]
    W = leverage_normalized_weights(sig)

    def book(Wx):
        """gross / turnover / per-day cost of the book `Wx` over the search window (flat cost, plus impact if configured)."""
        bt = backtest(Wx, close, cost_bps)
        gross, turn = bt["gross"][a0:], bt["turnover"][a0:]
        cost, imp = cost_bps * 1e-4 * turn, None
        if impact is not None:
            ic, dw = impact_cost(Wx, close, panel.data["$volume"], impact, adv_sig)
            check_turnover(dw, bt["turnover"])
            cost = cost + ic[a0:]
            imp = float(np.mean(ic[a0:]) * 1e4)
        return gross, turn, cost, imp

    gross, turn, cost, imp_bps = book(W)                                 # the sign +1 book: what the Auditor re-orients per CPCV fold
    train_gross = gross[:a1 - a0]
    sign = 1 if np.nansum(train_gross) >= 0 else -1                      # decided on TRAIN only
    if sign == -1:                                                       # the SDE flips the SIGNAL, and the drifted pre-trade weights (hence
        g2, turn_m, c2, imp_bps = book(-W)                               # turnover and cost) differ at second order: use the exact flipped book
        net = g2 - c2
    else:
        net, turn_m = gross - cost, turn
    n_tr = a1 - a0
    m_all = metrics(net, turn_m)
    m_tr, m_va = metrics(net[:n_tr], turn_m[:n_tr]), metrics(net[n_tr:], turn_m[n_tr:])
    sd = float(np.std(net, ddof=1))
    sr_pos = float(np.mean(gross - cost) / max(np.std(gross - cost, ddof=1), 1e-18))
    metrics_out = {
        "sample_size_T": int(len(net)), "in_sample_sharpe": m_tr["sharpe"], "out_of_sample_sharpe": m_va["sharpe"],
        "search_sharpe": m_all["sharpe"], "annual_return": m_all["annual_return"], "max_drawdown": m_all["max_drawdown"],
        "annualized_turnover": m_all.get("turnover_annual"), "skewness": float(stats.skew(net)),
        "kurtosis": float(stats.kurtosis(net, fisher=False)), "sign": sign, "cost_bps": cost_bps,
        "cost_model": "flat+sqrt_impact" if impact is not None else "flat", "impact": impact.asdict() if impact is not None else None,
        "impact_bps_per_day": imp_bps, "valid_day_fraction": float(valid.mean()), "daily_sd": sd,
        "note": "in_sample = train 2010-2016, out_of_sample = validation 2017 (both are SEARCH data); long-short, not tradable on the desk",
    }
    return {"net": net, "gross": gross, "turnover": turn, "cost": cost, "sign": sign, "sharpe_daily_pos": sr_pos, "metrics": metrics_out}


class Worker:
    """One worker process/loop. `run_once` claims and evaluates a single task; `run_loop` runs until `stop()` is true."""

    def __init__(self, ledger: SharedLedger, panel: SearchPanel, worker_id: str, device=None, cost_bps: float = COST_BPS,
                 impact: Optional[ImpactModel] = None, keystore: Optional[KeyStore] = None, require_signature: bool = True, coordinator=None):
        self.ledger, self.panel, self.id = ledger, panel, worker_id
        self.device = device or pick_device()
        self.cost_bps = cost_bps
        self.trad = tradable_mask(panel)
        self.impact, self.keystore, self.require_signature, self.coord = impact, keystore, require_signature, coordinator
        self.adv_sig = adv_sigma(panel.data["$close"], panel.data["$volume"], impact.window) if impact is not None else None

    def run_once(self, lease_s: float = 300.0) -> Optional[int]:
        hint = self.coord.pop_task() if self.coord is not None else None        # Redis queue hint (optional); SQLite still decides
        task = self.ledger.claim_task(self.id, lease_s, hint_id=hint)
        if task is None:
            return None
        tid = task["trial_id"]
        try:
            if self.keystore is not None and self.require_signature:
                ok, why = self.keystore.verify(task_payload(task), task.get("signature"), "miner")
                if not ok:
                    raise EvalError(f"task bundle rejected: {why}")
            node = payload_to_node_any(task["ast"], task.get("dsl", "sde"))
            if hash_any(node) != task["ast_hash"]:
                raise EvalError("AST hash mismatch (payload tampered or corrupted)")
            r = evaluate_formula(node, self.panel, self.device, self.cost_bps, self.trad, self.impact, self.adv_sig)
            r["metrics"]["worker"] = self.id
            r["metrics"]["device"] = str(self.device)
            sig = None
            if self.keystore is not None:
                sig = self.keystore.sign("worker", result_payload(tid, task["ast_hash"], self.id, r["metrics"], r["net"], r["gross"], r["turnover"], r["cost"]))
            self.ledger.complete_task(tid, self.id, metrics=r["metrics"], net=r["net"], gross=r["gross"], turnover=r["turnover"],
                                      sharpe_daily=r["sharpe_daily_pos"], sign=r["sign"], cost=r["cost"], result_sig=sig)
        except EvalError as e:
            self.ledger.fail_task(tid, self.id, f"EvalError: {e}")
        except Exception as e:                                           # never let one formula kill a worker
            self.ledger.fail_task(tid, self.id, f"{type(e).__name__}: {e}\n{traceback.format_exc(limit=3)}")
        return tid

    def run_loop(self, stop, idle_sleep: float = 0.5, parent_pid: Optional[int] = None) -> int:
        """`stop` is a callable or multiprocessing.Event-like. Exits if the parent process disappears (no orphans)."""
        done = 0
        is_stop = stop.is_set if hasattr(stop, "is_set") else stop
        while not is_stop():
            if parent_pid is not None and os.getppid() != parent_pid:
                break
            if self.run_once() is None:
                time.sleep(idle_sleep)
            else:
                done += 1
        return done


def worker_main(db_path: str, worker_id: str, stop_event, parent_pid: int, panel_cache: Optional[str] = None, device: Optional[str] = None,
                panel_spec: Optional[dict] = None, impact: Optional[dict] = None, key_dir: Optional[str] = None, redis_url: Optional[str] = None,
                redis_prefix: str = "swarm") -> None:
    """multiprocessing entry point."""
    signal.signal(signal.SIGINT, signal.SIG_IGN)                         # the coordinator owns shutdown
    signal.signal(signal.SIGTERM, lambda *_: stop_event.set())
    from .data import build_search_panel, synthetic_panel
    led = SharedLedger(db_path)
    panel = synthetic_panel(**panel_spec) if panel_spec else build_search_panel(panel_cache)       # panel_spec: tests / smoke runs only
    coord = None
    if redis_url:
        from .redis_coord import Coordinator
        coord = Coordinator(redis_url, redis_prefix)
    w = Worker(led, panel, worker_id, device=pick_device(device), impact=ImpactModel(**impact) if impact else None,
               keystore=KeyStore(key_dir) if key_dir else None, coordinator=coord)
    w.run_loop(stop_event, parent_pid=parent_pid)
    led.close()
