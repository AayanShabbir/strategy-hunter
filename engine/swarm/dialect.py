"""One door for the two formula dialects: the SDE grammar (`$close`, `TsStd(x, 20d)`, default) and the opt-in extended dialect
(`dsl_ext`: `cs_rank(ts_mean(close, 20))`). Everything else in the swarm calls these functions, so a new dialect is a local change.
The dialect of a formula is `ext` iff its text contains no `$` (the SDE dialect always writes `$feature`)."""
from __future__ import annotations

from typing import Any

from src.dsl.grammar import MAX_LEN, DSLSyntaxError
from src.dsl.grammar import parse_expr as _sde_parse

from . import dsl_ext
from .ast_json import node_hash as _sde_hash
from .ast_json import node_to_json as _sde_to_json
from .ast_json import payload_to_node as _sde_payload
from .dsl_ext import ExtSyntaxError

SyntaxErrors = (DSLSyntaxError, ExtSyntaxError)
SDE, EXT = "sde", "ext"


def dialect_of_expr(expression: str) -> str:
    return EXT if dsl_ext.is_ext_expr(expression) else SDE


def dialect_of_node(node: Any) -> str:
    return EXT if isinstance(node, dsl_ext.ENode) else SDE


def parse_any(expression: str, max_nodes: int = MAX_LEN, allow_ext: bool = True) -> Any:
    if dialect_of_expr(expression) == EXT:
        if not allow_ext:
            raise DSLSyntaxError("extended dialect is not enabled for this run (formulas need `$feature` names; see --dsl)")
        return dsl_ext.parse_ext(expression, max_nodes=min(max_nodes, dsl_ext.MAX_NODES))
    n = _sde_parse(expression)
    if n.size() > max_nodes:
        raise DSLSyntaxError(f"{n.size()} nodes > limit {max_nodes}")
    return n


def hash_any(node: Any) -> str:
    return dsl_ext.ast_hash(node) if dialect_of_node(node) == EXT else _sde_hash(node)


def to_json_any(node: Any) -> dict:
    return dsl_ext.node_to_json(node) if dialect_of_node(node) == EXT else _sde_to_json(node)


def payload_to_node_any(ast_json: Any, dialect: str = SDE) -> Any:
    return dsl_ext.payload_to_node(ast_json) if dialect == EXT else _sde_payload(ast_json)


def evaluate_any(node: Any, panel_data: dict, device=None, mask=None) -> Any:
    if dialect_of_node(node) == EXT:
        return dsl_ext.evaluate_numpy(node, panel_data, device, mask)
    from .tensor_eval import evaluate_numpy
    return evaluate_numpy(node, panel_data, device)
