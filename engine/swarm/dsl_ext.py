"""Opt-in EXTENDED formula dialect (the blueprint's operator set). The SDE grammar in `src/dsl/grammar.py` is untouched.

Operators (blueprint draft-07 schema, `RecursiveFactorDSLGrammarSchema`):
  cross-sectional   cs_rank, cs_normalize
  time-series       ts_mean, ts_std, ts_delta, ts_decay_linear      (second argument = integer look-back 1..252)
  arithmetic        multiply, add, subtract, divide, abs, log, sign
  leaves            close, high, low, volume, returns, tp           and numeric constants
`returns` = close/close[t-1] - 1. `tp` = (high+low+close)/3, the typical price. The blueprint's `vwap` needs intraday bars and `open`
is not in the SDE daily panel (only $close/$high/$low/$volume), so neither is available - `tp` is the honest daily stand-in and is
named differently on purpose.
Syntax:  cs_rank(ts_mean(multiply(ts_delta(close, 1), volume), 20))   (no `$` prefix; the SDE dialect always has `$`, which is how
the two dialects are told apart).
Limits (blueprint prompt): operator-chain depth <= 4 (`max_depth`, root = 0) and <= 10 nodes (look-back integers are parameters,
not nodes, matching the blueprint's own node_count example).
`ENode` is duck-compatible with the SDE `Node` for the swarm's novelty machinery: `.op` is the TED label (`ts_mean:20` carries
the window, so a window tweak costs one relabel), `.children`, `.size()` and `.canonical()`.

Evaluation is vectorised with torch `unfold` (no loop over time). A pure-numpy/pandas reference (`evaluate_reference`) is kept for
the cross-check test and the standalone survivor script. NaN policy: rolling windows containing a non-finite value are NaN;
cross-sectional operators ignore NaN/non-members (the blueprint's ffill+median fill is a documented deliberate deviation).
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from typing import Any, Optional

import numpy as np

EPS = 1e-8
MAX_NODES = 10
MAX_DEPTH = 4
MAX_WINDOW = 252
FEATURES = ("close", "high", "low", "volume", "returns", "tp")
CS_OPS = ("cs_rank", "cs_normalize")
TS_OPS = ("ts_mean", "ts_std", "ts_delta", "ts_decay_linear")
UNARY = ("abs", "log", "sign") + CS_OPS
BINARY = ("multiply", "add", "subtract", "divide")
COMMUTATIVE = {"multiply", "add"}
MIN_WINDOW = {"ts_mean": 1, "ts_delta": 1, "ts_std": 2, "ts_decay_linear": 2}
SDE_KEYS = {"close": "$close", "high": "$high", "low": "$low", "volume": "$volume"}


class ExtSyntaxError(ValueError):
    pass


def _fmt(v: float) -> str:
    return repr(int(v)) if float(v).is_integer() else repr(round(float(v), 6))


@dataclass(frozen=True)
class ENode:
    name: str                              # base operator / feature / 'const'
    children: tuple = ()
    param: Optional[int] = None            # look-back window for ts_* operators
    value: Optional[float] = None          # constant value

    @property
    def op(self) -> str:                   # TED label
        if self.name == "const":
            return f"const:{_fmt(self.value)}"
        return f"{self.name}:{self.param}" if self.param is not None else self.name

    def size(self) -> int:
        return 1 + sum(c.size() for c in self.children)

    def depth(self) -> int:
        """Operator-chain depth with the root at 0 (the blueprint's own example, 6 nodes, has depth 3)."""
        ops = [c.depth() for c in self.children if c.children]
        return (1 + max(ops)) if ops else 0

    def canonical(self) -> str:
        if self.name == "const":
            return _fmt(self.value)
        if not self.children:
            return self.name
        parts = [c.canonical() for c in self.children]
        if self.param is not None:
            parts.append(str(self.param))
        return f"{self.name}({', '.join(parts)})"


def _canon(n: ENode) -> ENode:
    kids = tuple(_canon(c) for c in n.children)
    if n.name in COMMUTATIVE:
        kids = tuple(sorted(kids, key=lambda c: c.canonical()))
    return ENode(n.name, kids, n.param, n.value)


def ast_hash(n: ENode) -> str:
    return hashlib.sha256(("ext:" + n.canonical()).encode()).hexdigest()


def is_ext_expr(expression: str) -> bool:
    return "$" not in expression


_TOK = re.compile(r"\s*(-?\d+\.?\d*(?:[eE][-+]?\d+)?|[A-Za-z_][A-Za-z_0-9]*|\(|\)|,)")


def _tokenize(s: str) -> list[str]:
    out, pos = [], 0
    s = s.strip()
    while pos < len(s):
        m = _TOK.match(s, pos)
        if not m:
            raise ExtSyntaxError(f"bad character at {pos}: {s[pos:pos + 12]!r}")
        out.append(m.group(1))
        pos = m.end()
        while pos < len(s) and s[pos].isspace():
            pos += 1
    return out


def check_limits(n: ENode, max_nodes: int = MAX_NODES, max_depth: int = MAX_DEPTH) -> None:
    if n.size() > max_nodes:
        raise ExtSyntaxError(f"{n.size()} nodes > limit {max_nodes}")
    if n.depth() > max_depth:
        raise ExtSyntaxError(f"depth {n.depth()} > limit {max_depth}")


def _build(name: str, kids: list, window: Optional[int] = None) -> ENode:
    if name in TS_OPS:
        if len(kids) != 1 or window is None:
            raise ExtSyntaxError(f"{name} needs (expression, window)")
        if not (MIN_WINDOW[name] <= window <= MAX_WINDOW):
            raise ExtSyntaxError(f"{name} window {window} outside [{MIN_WINDOW[name]}, {MAX_WINDOW}]")
        return ENode(name, tuple(kids), int(window))
    if name in UNARY:
        if len(kids) != 1 or window is not None:
            raise ExtSyntaxError(f"{name} takes exactly one argument")
        return ENode(name, tuple(kids))
    if name in BINARY:
        if len(kids) != 2 or window is not None:
            raise ExtSyntaxError(f"{name} takes exactly two arguments")
        return ENode(name, tuple(kids))
    raise ExtSyntaxError(f"unknown operator {name!r}")


def parse_ext(s: str, max_nodes: int = MAX_NODES, max_depth: int = MAX_DEPTH) -> ENode:
    toks = _tokenize(s)
    i = 0

    def peek():
        return toks[i] if i < len(toks) else None

    def take(t: Optional[str] = None) -> str:
        nonlocal i
        if i >= len(toks) or (t is not None and toks[i] != t):
            raise ExtSyntaxError(f"expected {t!r} at token {i}")
        i += 1
        return toks[i - 1]

    def expr(depth: int = 0) -> ENode:
        if depth > 64:
            raise ExtSyntaxError("absurdly deep expression")
        t = take()
        if re.fullmatch(r"-?\d+\.?\d*(?:[eE][-+]?\d+)?", t):
            v = float(t)
            if not np.isfinite(v) or abs(v) > 1e6:
                raise ExtSyntaxError("constant out of range")
            return ENode("const", value=v)
        if t in FEATURES:
            return ENode(t)
        if peek() != "(":
            raise ExtSyntaxError(f"unknown identifier {t!r}")
        take("(")
        kids, window = [], None
        while True:
            if t in TS_OPS and kids and peek() != ")":
                w = take()
                if not re.fullmatch(r"\d+", w):
                    raise ExtSyntaxError(f"{t} window must be an integer, got {w!r}")
                window = int(w)
            else:
                kids.append(expr(depth + 1))
            if peek() == ",":
                take(",")
                continue
            break
        take(")")
        return _build(t, kids, window)

    n = expr()
    if i != len(toks):
        raise ExtSyntaxError("trailing tokens")
    n = _canon(n)
    check_limits(n, max_nodes, max_depth)
    return n


# ---------------------------------------------------------------------------- blueprint AST JSON (draft-07 schema)
JSON_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#", "title": "RecursiveFactorDSLGrammarSchema", "type": "object",
    "definitions": {"expression": {"type": "object", "properties": {
        "node_type": {"type": "string", "enum": ["operator", "feature", "constant"]},
        "operator": {"type": "string", "enum": list(UNARY + TS_OPS + BINARY)},
        "feature_name": {"type": "string", "enum": list(FEATURES)},
        "constant_value": {"type": "number"},
        "lookback_window": {"type": "integer", "minimum": 1, "maximum": MAX_WINDOW},
        "arguments": {"type": "array", "items": {"$ref": "#/definitions/expression"}, "minItems": 0, "maxItems": 2}},
        "required": ["node_type"]}},
    "properties": {"expression_id": {"type": "string"}, "ast_root": {"$ref": "#/definitions/expression"}},
}


def node_to_json(n: ENode) -> dict:
    if n.name == "const":
        return {"node_type": "constant", "constant_value": n.value}
    if not n.children:
        return {"node_type": "feature", "feature_name": n.name}
    d: dict[str, Any] = {"node_type": "operator", "operator": n.name, "arguments": [node_to_json(c) for c in n.children]}
    if n.param is not None:
        d["lookback_window"] = n.param
    return d


def json_to_node(d: Any, _depth: int = 0) -> ENode:
    if _depth > 64 or not isinstance(d, dict):
        raise ExtSyntaxError("AST JSON node must be an object")
    t = d.get("node_type")
    if t == "constant":
        v = d.get("constant_value")
        if isinstance(v, bool) or not isinstance(v, (int, float)) or not np.isfinite(v):
            raise ExtSyntaxError("bad constant")
        return ENode("const", value=float(v))
    if t == "feature":
        if d.get("feature_name") not in FEATURES:
            raise ExtSyntaxError(f"unknown feature {d.get('feature_name')!r}")
        return ENode(d["feature_name"])
    if t == "operator":
        args = d.get("arguments")
        if not isinstance(args, list):
            raise ExtSyntaxError("operator needs arguments")
        w = d.get("lookback_window")
        if w is not None and (isinstance(w, bool) or not isinstance(w, int)):
            raise ExtSyntaxError("lookback_window must be an integer")
        return _build(str(d.get("operator")), [json_to_node(a, _depth + 1) for a in args], w)
    raise ExtSyntaxError(f"unknown node_type {t!r}")


def payload_to_node(ast_json: Any, max_nodes: int = MAX_NODES, max_depth: int = MAX_DEPTH) -> ENode:
    n = _canon(json_to_node(ast_json))
    check_limits(n, max_nodes, max_depth)
    return n


def validate_schema(payload: dict) -> None:
    """Validate a full {'expression_id', 'ast_root'} payload against the blueprint's draft-07 schema (raises on failure)."""
    import jsonschema
    jsonschema.Draft7Validator(JSON_SCHEMA).validate(payload)


# ---------------------------------------------------------------------------- torch evaluation (unfold, no time loops)
def ext_features(panel_data: dict, xp=np) -> dict:
    """Map the SDE panel arrays ({'$close',...}) to the dialect's leaf features (all causal)."""
    c, h, l, v = (np.asarray(panel_data[SDE_KEYS[k]], float) for k in ("close", "high", "low", "volume"))
    ret = np.full_like(c, np.nan)
    ret[1:] = c[1:] / c[:-1] - 1.0
    return {"close": c, "high": h, "low": l, "volume": v, "returns": ret, "tp": (h + l + c) / 3.0}


def _clean(x):
    import torch
    return torch.where(torch.isfinite(x), x, torch.full_like(x, float("nan")))


def _rolling(x, w: int, fn, budget: float = 3e7):
    import torch
    T, N = x.shape
    out = torch.full_like(x, float("nan"))
    if T < w:
        return out
    x = _clean(x)
    block = max(1, int(budget // max(T * w, 1)))
    for a in range(0, N, block):
        out[w - 1:, a:a + block] = fn(x[:, a:a + block].unfold(0, w, 1))
    return out


def _cs_rank(x, mask):
    import torch
    x = _clean(x)
    if mask is not None:
        x = torch.where(mask, x, torch.full_like(x, float("nan")))
    fin = torch.isfinite(x)
    n = fin.sum(1, keepdim=True)
    srt = torch.sort(torch.where(fin, x, torch.full_like(x, float("inf"))), dim=1).values.contiguous()
    v = torch.where(fin, x, torch.zeros_like(x)).contiguous()
    lo = torch.searchsorted(srt, v, right=False).to(x.dtype)
    hi = torch.searchsorted(srt, v, right=True).to(x.dtype)
    r = ((lo + 1 + hi) / 2) / n.clamp(min=1)
    return torch.where(fin, r, torch.full_like(x, float("nan")))


def _cs_norm(x, mask):
    import torch
    x = _clean(x)
    if mask is not None:
        x = torch.where(mask, x, torch.full_like(x, float("nan")))
    fin = torch.isfinite(x)
    n = fin.sum(1, keepdim=True).to(x.dtype)
    z = torch.where(fin, x, torch.zeros_like(x))
    mu = z.sum(1, keepdim=True) / n.clamp(min=1)
    d = torch.where(fin, x - mu, torch.zeros_like(x))
    sd = torch.sqrt((d * d).sum(1, keepdim=True) / (n - 1).clamp(min=1))
    out = d / (sd + EPS)
    return torch.where(fin & (n > 1), out, torch.full_like(x, float("nan")))


def _guard_div(a, b):
    import torch
    s = torch.sign(b)
    s = torch.where(s == 0, torch.ones_like(s), s)
    return a / (b + s * EPS)


def evaluate_tensor(n: ENode, feats: dict, mask=None):
    import torch
    if n.name == "const":
        return torch.full_like(feats["close"], n.value)
    if not n.children:
        return feats[n.name]
    a = [evaluate_tensor(c, feats, mask) for c in n.children]
    nm = n.name
    if nm == "cs_rank":
        return _cs_rank(a[0], mask)
    if nm == "cs_normalize":
        return _cs_norm(a[0], mask)
    if nm == "ts_mean":
        return _rolling(a[0], n.param, lambda w: w.mean(-1))
    if nm == "ts_std":
        return _rolling(a[0], n.param, lambda w: w.std(dim=-1, unbiased=True))
    if nm == "ts_decay_linear":
        wts = torch.arange(1, n.param + 1, dtype=a[0].dtype, device=a[0].device)
        wts = wts / wts.sum()
        return _rolling(a[0], n.param, lambda w: (w * wts).sum(-1))
    if nm == "ts_delta":
        x = _clean(a[0])
        out = torch.full_like(x, float("nan"))
        if x.shape[0] > n.param:
            out[n.param:] = x[n.param:] - x[:-n.param]
        return out
    if nm == "abs":
        return torch.abs(a[0])
    if nm == "log":
        return torch.log(torch.abs(a[0]) + EPS)
    if nm == "sign":
        return torch.where(torch.isnan(a[0]), a[0], torch.sign(a[0]))      # torch.sign(nan) is 0, numpy keeps NaN
    if nm == "multiply":
        return a[0] * a[1]
    if nm == "add":
        return a[0] + a[1]
    if nm == "subtract":
        return a[0] - a[1]
    if nm == "divide":
        return _guard_div(a[0], a[1])
    raise ExtSyntaxError(f"cannot evaluate {nm}")


def evaluate_numpy(n: ENode, panel_data: dict, device=None, mask: Optional[np.ndarray] = None, dtype=None) -> np.ndarray:
    import torch
    dtype = dtype or torch.float64
    device = device or torch.device("cuda" if torch.cuda.is_available() else "cpu")
    feats = {k: torch.as_tensor(v, dtype=dtype, device=device) for k, v in ext_features(panel_data).items()}
    m = None if mask is None else torch.as_tensor(np.asarray(mask, bool), device=device)
    with torch.no_grad():
        return evaluate_tensor(n, feats, m).cpu().numpy()


# ---------------------------------------------------------------------------- independent numpy reference (pandas rolling / scipy rank)
def evaluate_reference(n: ENode, panel_data: dict, mask: Optional[np.ndarray] = None) -> np.ndarray:
    """Slow, loop-based, deliberately different implementation: the oracle for tests and the standalone survivor script."""
    import pandas as pd
    from scipy.stats import rankdata
    feats = ext_features(panel_data)

    def ev(m: ENode) -> np.ndarray:
        if m.name == "const":
            return np.full_like(feats["close"], m.value)
        if not m.children:
            return feats[m.name].copy()
        a = [np.where(np.isfinite(ev(c)), ev(c), np.nan) for c in m.children]
        x = a[0]
        nm = m.name
        if nm in ("cs_rank", "cs_normalize"):
            if mask is not None:
                x = np.where(mask, x, np.nan)
            out = np.full_like(x, np.nan)
            for t in range(x.shape[0]):
                f = np.isfinite(x[t])
                k = int(f.sum())
                if k == 0:
                    continue
                if nm == "cs_rank":
                    out[t, f] = rankdata(x[t, f], method="average") / k
                elif k > 1:
                    out[t, f] = (x[t, f] - x[t, f].mean()) / (x[t, f].std(ddof=1) + EPS)
            return out
        if nm in ("ts_mean", "ts_std"):
            r = pd.DataFrame(x).rolling(m.param, min_periods=m.param)
            return (r.mean() if nm == "ts_mean" else r.std(ddof=1)).to_numpy()
        if nm == "ts_decay_linear":
            w = np.arange(1, m.param + 1, dtype=float)
            w /= w.sum()
            return pd.DataFrame(x).rolling(m.param, min_periods=m.param).apply(lambda v: float(np.dot(v, w)), raw=True).to_numpy()
        if nm == "ts_delta":
            return x - pd.DataFrame(x).shift(m.param).to_numpy()
        if nm == "abs":
            return np.abs(x)
        if nm == "log":
            return np.log(np.abs(x) + EPS)
        if nm == "sign":
            return np.sign(x)
        b = a[1]
        if nm == "multiply":
            return x * b
        if nm == "add":
            return x + b
        if nm == "subtract":
            return x - b
        if nm == "divide":
            s = np.where(np.sign(b) == 0, 1.0, np.sign(b))
            return x / (b + s * EPS)
        raise ExtSyntaxError(nm)

    return ev(n)


# ---------------------------------------------------------------------------- generator
EXT_PERSONA = {
    # persona -> (features, ts ops, arithmetic ops, windows)
    "momentum": (["returns", "close", "returns", "tp"], ["ts_delta", "ts_mean", "ts_decay_linear"], ["subtract", "divide", "multiply"], [5, 10, 20, 60, 120]),
    "mean_reversion": (["close", "returns", "tp"], ["ts_mean", "ts_delta", "ts_std"], ["subtract", "divide", "multiply"], [3, 5, 10, 20]),
    "volatility": (["returns", "high", "low", "close"], ["ts_std", "ts_mean"], ["divide", "subtract", "multiply"], [5, 10, 20, 60]),
    "liquidity": (["volume", "close", "returns", "volume"], ["ts_mean", "ts_delta", "ts_std"], ["multiply", "divide", "subtract"], [5, 10, 20, 60]),
    "range_microstructure": (["high", "low", "close", "tp", "volume"], ["ts_mean", "ts_delta", "ts_std"], ["subtract", "divide", "multiply"], [2, 5, 10, 20]),
    "cross_contrast": (list(FEATURES), list(TS_OPS), list(BINARY), [2, 3, 5, 10, 20, 40, 60, 120, 252]),
}


class ExtGenerator:
    """Random grammar-directed generator for the extended dialect (always within the 10-node / depth-4 limits)."""

    def __init__(self, seed: int = 0):
        self.rng = np.random.default_rng(seed)

    def sample(self, persona: str = "cross_contrast", temperature: float = 0.5) -> str:
        feats, tsops, arith, wins = EXT_PERSONA.get(persona, EXT_PERSONA["cross_contrast"])
        rng = self.rng
        if temperature >= 0.9:                           # reheat: widen everything
            feats, tsops, arith, wins = list(FEATURES), list(TS_OPS), list(BINARY), EXT_PERSONA["cross_contrast"][3]
        pick = lambda xs: xs[int(rng.integers(len(xs)))]  # noqa: E731
        max_depth = 3 + int(round(temperature))

        def gen(d: int) -> str:
            if d == 0 or rng.random() < 0.2 + 0.1 * (max_depth - d):
                return pick(feats) if rng.random() > 0.08 else _fmt(pick([0.5, 1, 2, 10]))
            k = rng.random()
            if k < 0.35:
                return f"{pick(tsops)}({gen(d - 1)}, {pick(wins)})"
            if k < 0.45:
                return f"{pick(['abs', 'log', 'sign'])}({gen(d - 1)})"
            return f"{pick(arith)}({gen(d - 1)}, {gen(d - 1)})"

        for _ in range(300):
            core = gen(max_depth)
            s = f"{pick(CS_OPS)}({core})" if rng.random() < 0.55 else core
            try:
                n = parse_ext(s)
            except ExtSyntaxError:
                continue
            if n.size() >= 4 and any(x in n.canonical() for x in TS_OPS):
                return n.canonical()
        return "cs_rank(ts_delta(close, 5))"
