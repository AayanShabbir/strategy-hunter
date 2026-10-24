"""Vectorised tensor evaluation of a DSL AST on [T, N] panels (torch; CUDA if present, else CPU).

No Python loop runs over time: rolling windows use `Tensor.unfold` (causal: window t covers rows t-w+1..t, so row t never
sees t+1). Assets are processed in column blocks only to bound memory; on an out-of-memory error the block is halved and
the evaluation retried (blueprint failure-mode table). Numerically equivalent to `src.dsl.grammar.evaluate` (tested to 1e-6).
"""
from __future__ import annotations

import numpy as np
import torch

from src.dsl.grammar import EPS, FEATURES, WINDOWS, DSLSyntaxError, Node


def pick_device(prefer: str | None = None) -> torch.device:
    if prefer:
        return torch.device(prefer)
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def ts_std(x: torch.Tensor, w: int, block: int = 128) -> torch.Tensor:
    """Backward-looking rolling sample std (ddof=1); first w-1 rows and any window containing a non-finite value are NaN."""
    T, N = x.shape
    out = torch.full_like(x, float("nan"))
    if T < w:
        return out
    x = torch.where(torch.isfinite(x), x, torch.full_like(x, float("nan")))
    for a in range(0, N, block):
        win = x[:, a:a + block].unfold(0, w, 1)           # [T-w+1, nb, w] view, no copy
        out[w - 1:, a:a + block] = win.std(dim=-1, unbiased=True)
    return out


def evaluate_tensor(node: Node, feats: dict[str, torch.Tensor], block: int = 128) -> torch.Tensor:
    op = node.op
    if op in FEATURES:
        return feats[op]
    if op == "Log":
        return torch.log(torch.abs(evaluate_tensor(node.children[0], feats, block)) + EPS)
    if op == "TsStd":
        return ts_std(evaluate_tensor(node.children[0], feats, block), WINDOWS[node.children[1].op], block)
    if op in ("Add", "Sub", "Div"):
        a, b = (evaluate_tensor(c, feats, block) for c in node.children)
        if op == "Add":
            return a + b
        if op == "Sub":
            return a - b
        s = torch.sign(b)
        s = torch.where(s == 0, torch.ones_like(s), s)
        return a / (b + s * EPS)
    raise DSLSyntaxError(f"cannot evaluate {op}")


def evaluate_numpy(node: Node, panel_data: dict[str, np.ndarray], device: torch.device | None = None, block: int = 128,
                   dtype=torch.float64) -> np.ndarray:
    """Evaluate on {'$close': (T,N) ndarray ...} and return an ndarray; halves `block` on OOM and retries."""
    device = device or pick_device()
    feats = {k: torch.as_tensor(np.asarray(v), dtype=dtype, device=device) for k, v in panel_data.items() if k in FEATURES}
    while True:
        try:
            with torch.no_grad():
                out = evaluate_tensor(node, feats, block).cpu().numpy()
            return out
        except (torch.OutOfMemoryError, MemoryError, RuntimeError) as e:        # RuntimeError covers CUDA OOM on older torch
            if "out of memory" not in str(e).lower() and not isinstance(e, (torch.OutOfMemoryError, MemoryError)):
                raise
            if block <= 1:
                raise
            block //= 2
            if device.type == "cuda":
                torch.cuda.empty_cache()
