"""SDE Phase 2: GFlowNet policy over the DSL action space (blueprint 2.3).

* Action space = 24 slots: 4 features, 2 unary ops, 3 binary ops, 4 windows, SEP (=14 real actions) + 10 RESERVED
  slots that are permanently masked (the DSL of blueprint 2.1 defines only 14 tokens; the reserved slots keep the
  policy head at the 24 outputs the plan specifies without inventing semantics).
* A formula is built in prefix (pre-order) order; state = partial AST. The RGCN (Phase 1) embeds the partial AST
  into R^128; an MLP head maps the embedding to 24 logits; invalid actions are masked (arity, window-only slots,
  MaxLen=32 so every partial state can always be completed within 32 nodes).
* Because each state has exactly one parent (prefix construction), P_B = 1 and Trajectory Balance reduces to
      L_TB = ( log Z + sum_t log P_F(a_t | s_t) - log R(x) )^2
  with a learnable log Z (Malkin et al. 2022). Entropy term (AlphaSAGE Eq. 15-16):
      L_final = L_TB + beta * ( - sum_t H(pi(.|s_t)) )
"""
from __future__ import annotations
import torch, torch.nn as nn
from src.dsl.grammar import (ASTGraph, FEATURES, UNARY, BINARY, WINDOWS, MAX_LEN, FEATURE, UNARY_T, BINARY_T, WINDOW,
                             R_OPERAND, R_WINDOW, R_SELF, parse_expr)
from src.models.rgcn_encoder import RGCNEncoder

SEP = "SEP"
TOKENS = list(FEATURES) + list(UNARY) + list(BINARY) + list(WINDOWS) + [SEP]      # 14 real actions
N_ACTIONS = 24
TOKENS = TOKENS + [f"<reserved{i}>" for i in range(N_ACTIONS - len(TOKENS))]
assert len(TOKENS) == N_ACTIONS
TOK_ID = {t: i for i, t in enumerate(TOKENS)}
FEAT_IDS = [TOK_ID[t] for t in FEATURES]
UNARY_IDS = [TOK_ID[t] for t in UNARY]
BINARY_IDS = [TOK_ID[t] for t in BINARY]
WIN_IDS = [TOK_ID[t] for t in WINDOWS]
SEP_ID = TOK_ID[SEP]
MIN_LEN = 2          # root must be an operator (a bare feature is not an alpha formula)
EXPR, WIN = "expr", "win"


class ExprState:
    """Partial formula in prefix order with a stack of open slots."""

    def __init__(self):
        self.tokens: list[str] = []
        self.parent: list[int] = []            # parent node index per token (-1 root)
        self.open: list[tuple] = [(EXPR, -1)]  # stack of (slot kind, parent idx); top = next slot to fill
        self.done = False

    @property
    def size(self): return len(self.tokens)

    def complete(self): return not self.open

    def mask(self) -> torch.Tensor:
        m = torch.zeros(N_ACTIONS, dtype=torch.bool)
        if self.done: return m
        if self.complete():
            m[SEP_ID] = True; return m
        kind, _ = self.open[-1]; n_open = len(self.open)
        if kind == WIN:
            for i in WIN_IDS: m[i] = True            # size+1, open-1: always fits
            return m
        for i in FEAT_IDS:
            if self.size > 0: m[i] = True            # root must not be a bare feature
        if self.size + 1 + n_open <= MAX_LEN:        # Log: closes 1 slot, opens 1
            for i in UNARY_IDS[:1]: m[i] = True
        if self.size + 1 + n_open + 1 <= MAX_LEN:    # TsStd (expr + window) and binaries each open 2, close 1
            m[UNARY_IDS[1]] = True
            for i in BINARY_IDS: m[i] = True
        return m

    def step(self, a: int):
        tok = TOKENS[a]
        if a == SEP_ID:
            assert self.complete(); self.done = True; return
        kind, par = self.open.pop()
        idx = len(self.tokens); self.tokens.append(tok); self.parent.append(par)
        if tok == "Log": self.open.append((EXPR, idx))
        elif tok == "TsStd": self.open.append((WIN, idx)); self.open.append((EXPR, idx))
        elif tok in BINARY: self.open.append((EXPR, idx)); self.open.append((EXPR, idx))

    def graph(self) -> ASTGraph | None:
        """Partial AST as a typed relational graph (pre-order node ids, same typing as parse_ast)."""
        if not self.tokens: return None
        g = ASTGraph(None, "", "", edges={R_OPERAND: [], R_WINDOW: [], R_SELF: []})
        for i, (t, p) in enumerate(zip(self.tokens, self.parent)):
            kind = FEATURE if t in FEATURES else WINDOW if t in WINDOWS else UNARY_T if t in UNARY else BINARY_T
            g.node_type.append(kind); g.node_label.append(t); g.edges[R_SELF].append((i, i))
            if p >= 0: g.edges[R_WINDOW if kind == WINDOW else R_OPERAND].append((p, i))
        return g

    def expr(self) -> str:
        """Complete formula as DSL text (parse_expr canonicalizes it)."""
        assert self.complete() and self.tokens
        pos = [0]
        def rec():
            t = self.tokens[pos[0]]; pos[0] += 1
            if t in FEATURES or t in WINDOWS: return t
            if t == "Log": return f"Log({rec()})"
            if t == "TsStd": a = rec(); return f"TsStd({a}, {rec()})"
            a = rec(); return f"{t}({a}, {rec()})"
        return rec()


class GFlowNetPolicy(nn.Module):
    def __init__(self, d_emb=128, d_hidden=128, seed=0, encoder: RGCNEncoder | None = None):
        super().__init__()
        torch.manual_seed(seed)
        self.encoder = encoder or RGCNEncoder(d_in=16, d_out=d_emb, seed=seed)
        self.start_emb = nn.Parameter(torch.zeros(d_emb))          # embedding of the empty state
        self.head = nn.Sequential(nn.Linear(d_emb, d_hidden), nn.ReLU(), nn.Linear(d_hidden, N_ACTIONS))
        self.log_z = nn.Parameter(torch.zeros(1))

    def embed(self, st: ExprState) -> torch.Tensor:
        g = st.graph()
        return self.start_emb if g is None else self.encoder(g)

    def logits(self, st: ExprState) -> torch.Tensor:
        return self.head(self.embed(st))

    def sample(self, greedy: bool = False, generator: torch.Generator | None = None):
        """Roll out one trajectory. Returns dict(state, sum_logp, sum_entropy, steps, expr)."""
        st = ExprState(); sum_lp = torch.zeros(()); sum_h = torch.zeros(()); steps = 0
        while not st.done:
            mask = st.mask()
            lg = self.logits(st).masked_fill(~mask, float("-inf"))
            logp = torch.log_softmax(lg, dim=-1)
            p = logp.exp()
            if mask.sum() == 1: a = int(mask.nonzero()[0])                       # forced move: log P_F = 0
            elif greedy: a = int(p.argmax())
            else: a = int(torch.multinomial(p.detach(), 1, generator=generator))
            sum_lp = sum_lp + logp[a]
            lp_safe = logp.masked_fill(~mask, 0.0)          # avoid 0*(-inf)=NaN in forward and backward
            sum_h = sum_h - (p * lp_safe).sum()
            st.step(a); steps += 1
        return {"state": st, "sum_logp": sum_lp, "sum_entropy": sum_h, "steps": steps, "expr": st.expr()}

    def tb_loss(self, sum_logp: torch.Tensor, log_reward: torch.Tensor, sum_entropy: torch.Tensor, beta: float = 0.01):
        """Returns (L_final, L_TB, L_ENT)."""
        l_tb = (self.log_z[0] + sum_logp - log_reward) ** 2
        l_ent = -sum_entropy
        return l_tb + beta * l_ent, l_tb, l_ent

    @staticmethod
    def check(expr: str):
        parse_expr(expr)     # raises DSLSyntaxError if the sampler ever produced an invalid / >MaxLen formula
