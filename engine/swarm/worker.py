"""Backtest Worker node: AST JSON in -> per-period return vectors + execution metrics into the shared ledger.

Pipeline (blueprint state GPU_EVAL): validate payload (strict AST JSON, hash must match) -> tensor-evaluate the formula
(`tensor_eval`, torch, CUDA if available) -> cross-sectional z-score -> dollar-neutral, leverage-normalised long-short weights
-> daily backtest with one-way costs (`src.portfolio.long_short`, shared with the SDE so the arithmetic is identical).
Orientation: the sign (long the high or low values) is chosen from the TRAIN period's gross mean only; validation is never
used to pick it. The stored vector covers train+validation (the whole search window) with a common calendar for every
trial, which CSCV/CPCV need. Raw (sign-free) gross returns and turnover are stored too so the Auditor can re-pick the sign
inside purged CPCV folds.
Not modelled: shorting borrow cost, spread/impact beyond `cost_bps` (the blueprint's square-root impact is listed as skipped).
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

from .ast_json import node_hash, payload_to_node
from .data import SearchPanel
from .shared_ledger import SharedLedger
from .tensor_eval import evaluate_numpy, pick_device

COST_BPS = 5.0
MIN_VALID_FRACTION = 0.6


class EvalError(Exception):
    pass


def evaluate_formula(node, panel: SearchPanel, device=None, cost_bps: float = COST_BPS, trad: Optional[np.ndarray] = None) -> dict:
    """Backtest one AST on the search window. Returns arrays + metrics; raises EvalError for unusable formulas."""
    trad = tradable_mask(panel) if trad is None else trad
    F = evaluate_numpy(node, panel.data, device)
    F = np.where(np.isfinite(F) & (np.abs(F) < 1e150), F, np.nan)
    sig = zscore_rows(F, trad)
    a0, a1, D = panel.start_idx, panel.train_end_idx, panel.n_days
    valid = np.isfinite(sig[a0:D - 1]).any(1)
    if valid.mean() < MIN_VALID_FRACTION:
        raise EvalError(f"signal valid on only {valid.mean():.0%} of search days")
    close = panel.data["$close"]
    bt = backtest(leverage_normalized_weights(sig), close, cost_bps)      # sign +1
    gross, turn = bt["gross"][a0:], bt["turnover"][a0:]
    train_gross = gross[:a1 - a0]
    sign = 1 if np.nansum(train_gross) >= 0 else -1                      # decided on TRAIN only
    net = sign * gross - cost_bps * 1e-4 * turn
    n_tr = a1 - a0
    m_all = metrics(net, turn)
    m_tr, m_va = metrics(net[:n_tr], turn[:n_tr]), metrics(net[n_tr:], turn[n_tr:])
    sd = float(np.std(net, ddof=1))
    sr_pos = float(np.mean(gross - cost_bps * 1e-4 * turn) / max(np.std(gross - cost_bps * 1e-4 * turn, ddof=1), 1e-18))
    metrics_out = {
        "sample_size_T": int(len(net)), "in_sample_sharpe": m_tr["sharpe"], "out_of_sample_sharpe": m_va["sharpe"],
        "search_sharpe": m_all["sharpe"], "annual_return": m_all["annual_return"], "max_drawdown": m_all["max_drawdown"],
        "annualized_turnover": m_all.get("turnover_annual"), "skewness": float(stats.skew(net)),
        "kurtosis": float(stats.kurtosis(net, fisher=False)), "sign": sign, "cost_bps": cost_bps,
        "valid_day_fraction": float(valid.mean()), "daily_sd": sd,
        "note": "in_sample = train 2010-2016, out_of_sample = validation 2017 (both are SEARCH data); long-short, not tradable on the desk",
    }
    return {"net": net, "gross": gross, "turnover": turn, "sign": sign, "sharpe_daily_pos": sr_pos, "metrics": metrics_out}


class Worker:
    """One worker process/loop. `run_once` claims and evaluates a single task; `run_loop` runs until `stop()` is true."""

    def __init__(self, ledger: SharedLedger, panel: SearchPanel, worker_id: str, device=None, cost_bps: float = COST_BPS):
        self.ledger, self.panel, self.id = ledger, panel, worker_id
        self.device = device or pick_device()
        self.cost_bps = cost_bps
        self.trad = tradable_mask(panel)

    def run_once(self, lease_s: float = 300.0) -> Optional[int]:
        task = self.ledger.claim_task(self.id, lease_s)
        if task is None:
            return None
        tid = task["trial_id"]
        try:
            node = payload_to_node(task["ast"])
            if node_hash(node) != task["ast_hash"]:
                raise EvalError("AST hash mismatch (payload tampered or corrupted)")
            r = evaluate_formula(node, self.panel, self.device, self.cost_bps, self.trad)
            r["metrics"]["worker"] = self.id
            r["metrics"]["device"] = str(self.device)
            self.ledger.complete_task(tid, self.id, metrics=r["metrics"], net=r["net"], gross=r["gross"], turnover=r["turnover"],
                                      sharpe_daily=r["sharpe_daily_pos"], sign=r["sign"])
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
                panel_spec: Optional[dict] = None) -> None:
    """multiprocessing entry point."""
    signal.signal(signal.SIGINT, signal.SIG_IGN)                         # the coordinator owns shutdown
    signal.signal(signal.SIGTERM, lambda *_: stop_event.set())
    from .data import build_search_panel, synthetic_panel
    led = SharedLedger(db_path)
    panel = synthetic_panel(**panel_spec) if panel_spec else build_search_panel(panel_cache)       # panel_spec: tests / smoke runs only
    w = Worker(led, panel, worker_id, device=pick_device(device))
    w.run_loop(stop_event, parent_pid=parent_pid)
    led.close()
