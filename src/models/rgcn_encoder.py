"""SDE Phase 1: Relational GCN encoder (blueprint 2.2), plain torch, CPU.

h_v^l = ReLU( sum_{r in {r1,r2}} sum_{u in N_v^r} 1/c_{v,r} W_r^l h_u^{l-1} + W_0^l h_v^{l-1} )
Messages on r1/r2 flow child -> operator (src=operand/window, dst=operator); r3 self-loop is W_0.
Graph embedding = element-wise max-pool over nodes -> R^{d_out}.
Node input h^(0) = [e_type (4 one-hot) || e_param (12: feature id 4, op id 5, window w/60, depth, pad)] = 16.
"""
from __future__ import annotations
import torch, torch.nn as nn
from src.dsl.grammar import ASTGraph, FEATURES, UNARY, BINARY, WINDOWS, R_OPERAND, R_WINDOW

OPS = UNARY + BINARY


def node_features(g: ASTGraph, d_in: int = 16) -> torch.Tensor:
    H = torch.zeros(len(g), d_in)
    for i, (t, lab) in enumerate(zip(g.node_type, g.node_label)):
        H[i, t] = 1.0
        if lab in FEATURES: H[i, 4 + FEATURES.index(lab)] = 1.0
        elif lab in OPS: H[i, 8 + OPS.index(lab)] = 1.0
        elif lab in WINDOWS: H[i, 13] = WINDOWS[lab] / 60.0
    return H


class RGCNLayer(nn.Module):
    def __init__(self, d_prev, d_out, rels=(R_OPERAND, R_WINDOW)):
        super().__init__()
        self.rels = rels
        self.W = nn.ModuleDict({str(r): nn.Linear(d_prev, d_out, bias=False) for r in rels})
        self.W0 = nn.Linear(d_prev, d_out, bias=False)

    def forward(self, H, edges):
        out = torch.zeros(H.shape[0], self.W0.out_features)
        for r in self.rels:
            e = edges.get(r, [])
            if not e: continue
            idx = torch.tensor(e, dtype=torch.long)
            dst, src = idx[:, 0], idx[:, 1]            # (op, child): child sends to op
            M = self.W[str(r)](H[src])
            agg = torch.zeros_like(out).index_add_(0, dst, M)
            c = torch.zeros(H.shape[0]).index_add_(0, dst, torch.ones(len(dst))).clamp(min=1)
            out = out + agg / c[:, None]
        return torch.relu(out + self.W0(H))


class RGCNEncoder(nn.Module):
    def __init__(self, d_in=16, d_out=128, d_hidden=128, n_layers=3, seed=0):
        super().__init__()
        torch.manual_seed(seed)
        dims = [d_in] + [d_hidden] * (n_layers - 1) + [d_out]
        self.d_in = d_in
        self.layers = nn.ModuleList(RGCNLayer(a, b) for a, b in zip(dims[:-1], dims[1:]))

    def forward(self, g: ASTGraph) -> torch.Tensor:
        H = node_features(g, self.d_in)
        assert torch.all(torch.isfinite(H)), "non-finite node features"
        for layer in self.layers:
            H = layer(H, g.edges)
            assert torch.all(torch.isfinite(H)), "non-finite hidden state"
        e = torch.max(H, dim=0).values
        assert torch.all(torch.isfinite(e)), "non-finite embedding"
        return e
