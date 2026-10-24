"""Degenerate-formula detection (dialect-agnostic: works on SDE `Node` and extended-DSL `ENode`).

A formula is *degenerate* when algebra already shows it carries no (or only trivially re-expressible) information:
  * self_cancel      Sub(x, x) / subtract(x, x)        -> constant 0
  * self_ratio       Div(x, x) / divide(x, x)          -> constant 1
  * redundant_term   Sub(Add(x, y), y) -> x (and the mirror images)    (a term that cancels itself)
  * div_by_const0    Div(a, <constant 0>)              -> a / 1e-8 (numerically meaningless, dominated by the guard epsilon)
  * constant         the WHOLE formula reduces to a constant (no cross-sectional variation, so no signal)
The check only inspects structure (no data), so it is applied by the miner BEFORE a formula costs a trial and again by the
worker as a defence in depth. The SDE factor pools contain such members (e.g. `Log(Add($high, Div($high, Sub($close, $close))))`);
they are reported, never silently dropped, and nothing about the SDE's own results changes.
"""
from __future__ import annotations

from typing import Any

SUB = {"Sub", "subtract"}
DIV = {"Div", "divide"}
ADD = {"Add", "add"}
# unary / windowed ops whose output over a constant input is the SAME constant (or zero for the difference/dispersion family)
_ZERO_OVER_CONST = {"TsStd", "ts_std", "ts_delta"}


def _name(n: Any) -> str:
    return getattr(n, "name", None) or n.op.split(":")[0]


def _is_leaf(n: Any) -> bool:
    return not n.children


def _const_state(n: Any, found: list) -> str | None:
    """Returns None (varies), 'zero', 'one' or 'const'. Appends degeneracy findings to `found`."""
    name = _name(n)
    if name == "const":                                   # extended-DSL literal
        v = getattr(n, "value", None)
        return "zero" if v == 0 else "one" if v == 1 else "const"
    if _is_leaf(n):
        return None                                       # a feature, or an SDE window token (handled by its parent)
    kids = [c for c in n.children if not (_is_leaf(c) and c.op.endswith("d") and c.op[:-1].isdigit())]   # skip SDE window tokens
    states = [_const_state(c, found) for c in kids]
    if name in SUB and len(kids) == 2:
        if kids[0].canonical() == kids[1].canonical():
            found.append("self_cancel")
            return "zero"
        for a, b in ((kids[0], kids[1]), (kids[1], kids[0])):          # (x + y) - y  or  (y + x) - y
            if _name(a) in ADD and any(c.canonical() == b.canonical() for c in a.children) and a is kids[0]:
                found.append("redundant_term")
                break
        if states[1] == "zero" and states[0] is not None:
            return states[0]
        if states[0] is not None and states[1] is not None:
            return "const"
        return None
    if name in DIV and len(kids) == 2:
        if kids[0].canonical() == kids[1].canonical():
            found.append("self_ratio")
            return "one"
        if states[1] == "zero":
            found.append("div_by_const0")
            return "const"
        if states[0] == "zero":
            return "zero"
        if states[0] is not None and states[1] is not None:
            return "const"
        return None
    if name in ADD and len(kids) == 2:
        if states[0] == "zero":
            return states[1]
        if states[1] == "zero":
            return states[0]
        if states[0] is not None and states[1] is not None:
            return "const"
        return None
    if name in _ZERO_OVER_CONST:
        return "zero" if states and states[0] is not None else None
    if all(s is not None for s in states) and states:      # any other op over constants only
        return "zero" if name in ("sign", "cs_normalize") and states[0] == "zero" else "const"
    if name in ("multiply",) and len(kids) == 2 and "zero" in states:
        return "zero"
    return None


def degenerate_reasons(node: Any) -> list[str]:
    """[] for a healthy formula, else the sorted unique reasons it is degenerate."""
    found: list[str] = []
    top = _const_state(node, found)
    if top is not None:
        found.append("constant")
    return sorted(set(found))


def is_degenerate(node: Any) -> bool:
    return bool(degenerate_reasons(node))
