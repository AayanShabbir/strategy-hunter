"""AST <-> JSON payloads (the Miner -> Worker contract).

Shape (modelled on the blueprint's `ast_root`, adapted to the SDE grammar's actual operators):
  {"node_type":"operator","operator":"Div","arguments":[ ... 2 children ... ]}
  {"node_type":"feature","feature_name":"$close"}
  {"node_type":"window","lookback_window":20,"token":"20d"}        (only as the 2nd argument of TsStd)
`json_to_node` validates strictly and rebuilds a canonical `Node`; anything off-grammar raises DSLSyntaxError.
"""
from __future__ import annotations

from typing import Any

from src.dsl.grammar import BINARY, FEATURES, MAX_LEN, UNARY, WINDOWS, DSLSyntaxError, Node, _canon, ast_hash


def node_to_json(n: Node) -> dict[str, Any]:
    if n.op in FEATURES:
        return {"node_type": "feature", "feature_name": n.op}
    if n.op in WINDOWS:
        return {"node_type": "window", "lookback_window": WINDOWS[n.op], "token": n.op}
    return {"node_type": "operator", "operator": n.op, "arguments": [node_to_json(c) for c in n.children]}


def json_to_node(d: Any, _depth: int = 0) -> Node:
    if _depth > 64 or not isinstance(d, dict):
        raise DSLSyntaxError("AST JSON node must be an object (and not absurdly deep)")
    t = d.get("node_type")
    if t == "feature":
        if d.get("feature_name") not in FEATURES:
            raise DSLSyntaxError(f"unknown feature {d.get('feature_name')!r}")
        return Node(d["feature_name"])
    if t == "window":
        tok = d.get("token")
        if tok not in WINDOWS or WINDOWS[tok] != d.get("lookback_window"):
            raise DSLSyntaxError(f"bad window {tok!r}/{d.get('lookback_window')!r}")
        return Node(tok)
    if t == "operator":
        op, args = d.get("operator"), d.get("arguments")
        if not isinstance(args, list):
            raise DSLSyntaxError("operator needs an arguments list")
        kids = tuple(json_to_node(a, _depth + 1) for a in args)
        if op in UNARY and op == "Log" and len(kids) == 1 and kids[0].op not in WINDOWS:
            return Node(op, kids)
        if op == "TsStd" and len(kids) == 2 and kids[1].op in WINDOWS and kids[0].op not in WINDOWS:
            return Node(op, kids)
        if op in BINARY and len(kids) == 2 and all(k.op not in WINDOWS for k in kids):
            return Node(op, kids)
        raise DSLSyntaxError(f"bad operator/arity: {op!r} with {len(kids)} args")
    raise DSLSyntaxError(f"unknown node_type {t!r}")


def payload_to_node(ast_json: Any) -> Node:
    """Strict entry point: rebuild, canonicalise and enforce the node limit."""
    n = _canon(json_to_node(ast_json))
    if n.size() > MAX_LEN:
        raise DSLSyntaxError(f"expression has {n.size()} nodes > MaxLen={MAX_LEN}")
    return n


def node_hash(n: Node) -> str:
    return ast_hash(n)
