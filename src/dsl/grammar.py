"""SDE Phase 1: symbolic alpha DSL -> canonical AST -> typed relational graph.

Grammar (blueprint 2.1):
  terminals: $close $high $low $volume
  unary: Log(x) = log(|x|+1e-8);  TsStd(x, w), w in {5d,10d,20d,60d}
  binary: Add, Sub, Div(x,y) = x/(y+sign(y)*1e-8)
Graph node types: Feature=0, Unary=1, Binary=2, Window=3.
Relations: r1 op->operand, r2 op->window, r3 self-loop.
"""
from __future__ import annotations
import hashlib, re
from dataclasses import dataclass, field
import numpy as np

FEATURES = ("$close", "$high", "$low", "$volume")
UNARY = ("Log", "TsStd")
BINARY = ("Add", "Sub", "Div")
WINDOWS = {"5d": 5, "10d": 10, "20d": 20, "60d": 60}
COMMUTATIVE = {"Add"}
MAX_LEN = 32
EPS = 1e-8
FEATURE, UNARY_T, BINARY_T, WINDOW = 0, 1, 2, 3
R_OPERAND, R_WINDOW, R_SELF = 0, 1, 2


class DSLSyntaxError(ValueError):
    pass


@dataclass(frozen=True)
class Node:
    op: str                      # feature name, operator name, or window token
    children: tuple = ()

    @property
    def kind(self) -> int:
        if self.op in FEATURES: return FEATURE
        if self.op in WINDOWS: return WINDOW
        if self.op in UNARY: return UNARY_T
        return BINARY_T

    def canonical(self) -> str:
        if not self.children: return self.op
        return f"{self.op}({', '.join(c.canonical() for c in self.children)})"

    def size(self) -> int:
        return 1 + sum(c.size() for c in self.children)


@dataclass
class ASTGraph:
    root: Node
    canonical: str
    hash: str
    node_type: list = field(default_factory=list)   # per node int type
    node_label: list = field(default_factory=list)  # op/feature/window token
    edges: dict = field(default_factory=dict)       # rel -> list[(op_idx, child_idx)]

    def __len__(self): return len(self.node_type)


_TOK = re.compile(r"\s*(\$[a-z]+|[A-Za-z]+|\d+d|\(|\)|,)")


def _tokenize(s: str):
    pos, out = 0, []
    s = s.strip()
    while pos < len(s):
        m = _TOK.match(s, pos)
        if not m or m.end() == pos:
            raise DSLSyntaxError(f"unexpected character {s[pos]!r} at position {pos}")
        out.append(m.group(1)); pos = m.end()
        while pos < len(s) and s[pos].isspace(): pos += 1
    if not out: raise DSLSyntaxError("empty expression")
    return out


def _canon(n: Node) -> Node:
    kids = tuple(_canon(c) for c in n.children)
    if n.op in COMMUTATIVE:
        kids = tuple(sorted(kids, key=lambda c: c.canonical()))
    return Node(n.op, kids)


def parse_expr(s: str) -> Node:
    toks = _tokenize(s); i = 0

    def expect(t):
        nonlocal i
        if i >= len(toks) or toks[i] != t:
            got = toks[i] if i < len(toks) else "end of input"
            raise DSLSyntaxError(f"expected {t!r}, got {got!r} (token {i})")
        i += 1

    def expr() -> Node:
        nonlocal i
        if i >= len(toks): raise DSLSyntaxError("unexpected end of input")
        t = toks[i]; i += 1
        if t in FEATURES: return Node(t)
        if t.startswith("$"): raise DSLSyntaxError(f"unknown feature {t!r}; allowed {FEATURES}")
        if t in WINDOWS: raise DSLSyntaxError(f"window {t!r} only allowed as TsStd 2nd argument")
        if t == "Log":
            expect("("); a = expr(); expect(")"); return Node(t, (a,))
        if t == "TsStd":
            expect("("); a = expr(); expect(",")
            if i >= len(toks) or toks[i] not in WINDOWS:
                raise DSLSyntaxError(f"TsStd window must be one of {list(WINDOWS)}, got {toks[i] if i < len(toks) else 'end'!r}")
            w = Node(toks[i]); i += 1; expect(")"); return Node(t, (a, w))
        if t in BINARY:
            expect("("); a = expr(); expect(","); b = expr(); expect(")"); return Node(t, (a, b))
        raise DSLSyntaxError(f"unknown token {t!r}")

    n = expr()
    if i != len(toks): raise DSLSyntaxError(f"trailing tokens: {' '.join(toks[i:])}")
    n = _canon(n)
    if n.size() > MAX_LEN: raise DSLSyntaxError(f"expression has {n.size()} nodes > MaxLen={MAX_LEN}")
    return n


def ast_hash(node: Node) -> str:
    return hashlib.sha256(node.canonical().encode()).hexdigest()


def parse_ast(s: str) -> ASTGraph:
    root = parse_expr(s)
    g = ASTGraph(root, root.canonical(), ast_hash(root),
                 edges={R_OPERAND: [], R_WINDOW: [], R_SELF: []})

    def visit(n: Node) -> int:
        idx = len(g.node_type)
        g.node_type.append(n.kind); g.node_label.append(n.op); g.edges[R_SELF].append((idx, idx))
        for c in n.children:
            ci = visit(c)
            g.edges[R_WINDOW if c.kind == WINDOW else R_OPERAND].append((idx, ci))
        return idx

    visit(root)
    return g


# ---------- causal evaluator: panel arrays shaped (dates, assets) ----------
def _ts_std(x: np.ndarray, w: int) -> np.ndarray:
    """Backward-looking rolling sample std (ddof=1); first w-1 rows NaN. No centering."""
    T = x.shape[0]; out = np.full_like(x, np.nan, dtype=float)
    for t in range(w - 1, T):
        out[t] = np.std(x[t - w + 1:t + 1], axis=0, ddof=1)
    return out


def evaluate(node, panel: dict) -> np.ndarray:
    """Evaluate on panel {'$close': (D,N) array, ...}. Row t uses only rows <= t."""
    if isinstance(node, (str, ASTGraph)):
        node = node.root if isinstance(node, ASTGraph) else parse_expr(node)
    op = node.op
    if op in FEATURES: return np.asarray(panel[op], dtype=float)
    with np.errstate(all="ignore"):
        if op == "Log": return np.log(np.abs(evaluate(node.children[0], panel)) + EPS)
        if op == "TsStd": return _ts_std(evaluate(node.children[0], panel), WINDOWS[node.children[1].op])
        a, b = (evaluate(c, panel) for c in node.children)
        if op == "Add": return a + b
        if op == "Sub": return a - b
        if op == "Div":
            s = np.sign(b); s[s == 0] = 1.0   # sign(0)=0 would leave 0 denominator; guard with +eps
            return a / (b + s * EPS)
    raise DSLSyntaxError(f"cannot evaluate {op}")


def random_expr(rng, max_depth: int = 4) -> str:
    """Random syntactically valid expression (used for fuzzing; Phase 2 sampler replaces)."""
    def gen(d):
        r = rng.random()
        if d == 0 or r < 0.3: return FEATURES[rng.integers(4)]
        if r < 0.45: return f"Log({gen(d-1)})"
        if r < 0.6: return f"TsStd({gen(d-1)}, {list(WINDOWS)[rng.integers(4)]})"
        return f"{BINARY[rng.integers(3)]}({gen(d-1)}, {gen(d-1)})"
    while True:
        s = gen(max_depth)
        if parse_expr(s).size() <= MAX_LEN: return s
