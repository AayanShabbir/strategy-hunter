import numpy as np, pytest, torch
from src.dsl.grammar import parse_ast, parse_expr, evaluate, random_expr, DSLSyntaxError, MAX_LEN, R_WINDOW
from src.models.rgcn_encoder import RGCNEncoder


def test_blueprint_assertions():
    encoder = RGCNEncoder(d_in=16, d_out=128)
    ast_1 = parse_ast("Add($close, $volume)"); ast_2 = parse_ast("Add($volume, $close)")
    e_1 = encoder(ast_1); e_2 = encoder(ast_2)
    assert e_1.shape == (128,), f"Expected shape (128,), got {e_1.shape}"
    assert torch.all(torch.isfinite(e_1)), "Non-finite values detected in RGCN embedding"
    assert torch.allclose(e_1, e_2, atol=1e-5), "AST encoder failed commutativity invariance"


def test_canonical_hash_and_noncommutative():
    assert parse_ast("Add($close,$volume)").hash == parse_ast("Add( $volume , $close )").hash
    assert parse_ast("Sub($close,$volume)").hash != parse_ast("Sub($volume,$close)").hash
    assert len(parse_ast("Add($close,$volume)").hash) == 64


def test_graph_typing():
    g = parse_ast("TsStd(Log($close), 20d)")
    assert g.node_type == [1, 1, 0, 3]
    assert g.edges[R_WINDOW] == [(0, 3)]


@pytest.mark.parametrize("bad", ["", "Add($close)", "TsStd($close, 7d)", "$open", "Log($close", "Foo($close)",
                                 "Add($close,$low) $high", "Log(5d)", "Add($close,$low"*1])
def test_invalid_rejected(bad):
    with pytest.raises(DSLSyntaxError):
        parse_ast(bad)


def test_maxlen():
    s = "$close"
    for _ in range(MAX_LEN): s = f"Log({s})"
    with pytest.raises(DSLSyntaxError, match="MaxLen"):
        parse_ast(s)


def _panel(rng, D=120, N=8):
    c = 100 * np.exp(np.cumsum(rng.normal(0, .02, (D, N)), 0))
    return {"$close": c, "$high": c * 1.01, "$low": c * .99, "$volume": rng.lognormal(12, 1, (D, N))}


def test_fuzz_parse_eval_encode():
    rng = np.random.default_rng(7); P = _panel(rng); enc = RGCNEncoder()
    for _ in range(300):
        s = random_expr(rng)
        g = parse_ast(s)
        assert parse_ast(g.canonical).hash == g.hash          # canonical is a fixed point
        z = evaluate(g, P)
        assert z.shape == P["$close"].shape
        assert not np.isinf(z).any()
        # NaN only allowed in TsStd warm-up rows (<= 59 * nesting); never after row 59*k
        assert torch.all(torch.isfinite(enc(g)))


def test_no_lookahead():
    rng = np.random.default_rng(1); P = _panel(rng); t0 = 70
    Q = {k: v.copy() for k, v in P.items()}
    for k in Q: Q[k][t0:] = rng.permutation(Q[k][t0:].ravel()).reshape(Q[k][t0:].shape) * 3.0
    for _ in range(100):
        s = random_expr(rng)
        a, b = evaluate(s, P)[:t0], evaluate(s, Q)[:t0]
        np.testing.assert_array_equal(np.isnan(a), np.isnan(b))
        np.testing.assert_allclose(np.nan_to_num(a), np.nan_to_num(b), rtol=0, atol=0)
