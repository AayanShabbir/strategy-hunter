"""Spec = one base idea + bounded grid + <=4 filters. Validated before pre-registration."""
import itertools, yaml
from .signals import IDEAS, FILTERS
MAX_FILTERS, MIN_TRADES_FLOOR, MAX_VARIANTS = 4, 100, 200
TIMEFRAMES = {"1Day", "1Hour", "15Min"}
class SpecError(ValueError): pass
def _grid(params):
    params = params or {}
    keys = sorted(params); vals = [v if isinstance(v, list) else [v] for v in (params[k] for k in keys)]
    return [dict(zip(keys, c)) for c in itertools.product(*vals)]
def load(path):
    raw = open(path, "rb").read(); s = yaml.safe_load(raw); validate(s); return s, raw
def validate(s):
    for k in ["id", "hypothesis", "base", "universe", "timeframe", "costs"]:
        if k not in s: raise SpecError(f"missing field: {k}")
    if s["base"].get("idea") not in IDEAS: raise SpecError(f"unknown idea {s['base'].get('idea')}; known: {sorted(IDEAS)}")
    f = s.get("filters") or []
    if len(f) > MAX_FILTERS: raise SpecError(f"{len(f)} filters > max {MAX_FILTERS}")
    for x in f:
        if x.get("name") not in FILTERS: raise SpecError(f"unknown filter {x.get('name')}; known: {sorted(FILTERS)}")
    if s["timeframe"] not in TIMEFRAMES: raise SpecError(f"timeframe must be one of {TIMEFRAMES}")
    if int(s.get("min_trades", MIN_TRADES_FLOOR)) < MIN_TRADES_FLOOR: raise SpecError("min_trades floor is 100")
    if s.get("direction", "long_flat") != "long_flat": raise SpecError("only long_flat allowed (shorts blocked: no written short plan)")
    u = s["universe"]
    if not isinstance(u, dict) or not u or not all(isinstance(v, list) and v for v in u.values()):
        raise SpecError("universe must be a map of basket_name -> [symbols]")
    n = len(variants(s))
    if n < 2: raise SpecError("need >=2 variants (PBO needs a family)")
    if n > min(MAX_VARIANTS, int(s.get("max_variants", MAX_VARIANTS))): raise SpecError(f"{n} variants exceeds bound")
def variants(s):
    out = []
    bg = _grid(s["base"].get("params")); fl = s.get("filters") or []
    fgrids = [[(x["name"], g) for g in _grid(x.get("params"))] for x in fl]
    for basket in s["universe"]:
        for b in bg:
            for fc in itertools.product(*fgrids) if fgrids else [()]:
                name = basket + "|" + s["base"]["idea"] + "(" + ",".join(f"{k}={v}" for k, v in b.items()) + ")" + \
                       "".join("+" + fn + "(" + ",".join(f"{k}={v}" for k, v in g.items()) + ")" for fn, g in fc)
                out.append(dict(name=name, basket=basket, base=b, filters=list(fc)))
    return out
