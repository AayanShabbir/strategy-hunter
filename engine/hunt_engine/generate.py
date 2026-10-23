"""Grammar-based spec generator (LLM-ready). Draws valid specs from the IDEAS x FILTERS grammar with a seeded RNG,
so a large automated search stays pre-registered: every generated spec still goes through `hunt run`, which
reserves ledger N before any result. `schema()` emits the grammar as JSON so an LLM proposer (Alpha-GPT /
RD-Agent style) can be asked to emit specs that `spec.validate` will accept."""
import json, os, numpy as np, yaml
from . import spec as specmod
GRAMMAR = dict(
    ideas=dict(sma_cross=dict(fast=[5, 10, 20, 50], slow=[50, 100, 150, 200]), donchian=dict(entry_n=[20, 55, 100], exit_n=[10, 20]),
               rsi_revert=dict(n=[2, 3, 5], entry=[5, 10, 20], exit=[60, 70, 80]), supertrend=dict(atr_n=[7, 10, 14], mult=[2, 3, 4]),
               drop_revert=dict(n=[1, 3, 5], drop=[0.05, 0.1, 0.15], hold=[3, 5, 10])),
    filters=dict(trend_sma=dict(n=[50, 100, 200]), vol_regime=dict(max_atr_pct=[0.02, 0.04, 0.06]), rsi_band=dict(hi=[60, 70, 80]),
                 relvol=dict(min_ratio=[1.0, 1.2]), day_of_week=dict(days=[[0, 1, 2, 3], [1, 2, 3, 4], [0, 1, 2, 3, 4]])))
def schema(): return dict(grammar=GRAMMAR, limits=dict(max_filters=specmod.MAX_FILTERS, max_variants=specmod.MAX_VARIANTS, min_trades=specmod.MIN_TRADES_FLOOR,
                          direction="long_flat only"), required=["id", "hypothesis", "base", "universe", "timeframe", "costs"])
def _pick(rng, grid, k): return {p: sorted(set(rng.choice(len(v), size=min(k, len(v)), replace=False).tolist())) for p, v in grid.items()}
def generate(n, universe, timeframe="1Day", costs=None, seed=0, prefix="gen", max_filters=1):
    rng = np.random.default_rng(seed); out = []; costs = costs or dict(fee_bps=0, slippage_bps=5)
    while len(out) < n:
        idea = rng.choice(sorted(GRAMMAR["ideas"])); g = GRAMMAR["ideas"][idea]
        params = {p: [g[p][i] for i in ix] for p, ix in _pick(rng, g, 2).items()}
        nf = int(rng.integers(0, max_filters + 1)); fl = []
        for fn in rng.choice(sorted(GRAMMAR["filters"]), size=nf, replace=False):
            fg = GRAMMAR["filters"][fn]; p = next(iter(fg)); fl.append(dict(name=str(fn), params={p: fg[p][int(rng.integers(len(fg[p])))]}))
        s = dict(id=f"{prefix}_{seed}_{len(out):03d}", hypothesis=f"grammar draw seed={seed}: {idea}" + "".join("+" + f["name"] for f in fl),
                 base=dict(idea=str(idea), params=params), filters=fl, universe=universe, timeframe=timeframe, costs=costs, min_trades=100)
        try: specmod.validate(s); out.append(s)
        except specmod.SpecError: continue
    return out
def write(specs, outdir):
    os.makedirs(outdir, exist_ok=True); fs = []
    for s in specs:
        f = os.path.join(outdir, s["id"] + ".yaml"); open(f, "w").write(yaml.safe_dump(s, sort_keys=False)); fs.append(f)
    return fs
if __name__ == "__main__": print(json.dumps(schema(), indent=1))
