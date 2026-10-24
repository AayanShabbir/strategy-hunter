"""Build the Phase 3 results tables (markdown) from runs_sde/*/phase3.json.   python -m src.train.phase3_table"""
import json, glob, sys, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]


def f(x, pct=False, d=2):
    if x is None or x != x: return "n/a"
    return f"{100*x:.{d}f}%" if pct else f"{x:.{d}f}"


def table(fname="phase3.json"):
    rows = []; hdr = ("| run | pool | N (total / universe) | combiner | test Sharpe | test AR | test MDD | test turnover/yr | val Sharpe | PBO | DSR test (N total) | SPA p (combined, test) | CPCV mean path SR | e-process (max / bound) |\n"
                      "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for p in sorted(glob.glob(str(ROOT / "runs_sde" / "*" / fname))):
        r = json.loads(Path(p).read_text()); cb = str(r["cost_bps"]); v = r["validity"]; N = r["N"]
        pbo = v["cscv"].get("pbo")
        if not r["portfolio"]:
            rows.append(f"| {r['run_id']} | 0 | {N['ledger_trials_total']} / {N['ledger_trials_universe']} | - | no portfolio (empty pool) | | | | | {f(pbo, True, 1)} | | | | |"); continue
        for name in ("rolling_ols", "equal"):
            m = r["portfolio"][name]["by_cost"][cb]; te, va = m["test"], m["val"]; d = v["dsr"][name]["test_N_ledger_total"]
            last = name == "rolling_ols"
            rows.append(f"| {r['run_id']} | {r['pool_size']} | {N['ledger_trials_total']} / {N['ledger_trials_universe']} | {name} | {f(te['sharpe'])} | {f(te['annual_return'], True)} | {f(te['max_drawdown'], True, 1)} | {f(te['turnover_annual'], d=1)} | {f(va['sharpe'])} | {f(pbo, True, 1)} | "
                        f"{f(d['dsr'], d=3)} | {f(v['spa_combined_test']['p_consistent'], d=3) if last else ''} | {f(v['cpcv']['mean_sharpe']) if last else ''} | {(f(v['eprocess']['max_evidence']) + ' / ' + f(v['eprocess']['boundary'], d=0)) if last else ''} |")
    return hdr + "\n" + "\n".join(rows)


def cost_table(fname="phase3.json"):
    out = ["| run | cost (bps/side) | test Sharpe | test AR | test MDD | test turnover/yr |", "|---|---|---|---|---|---|"]
    for p in sorted(glob.glob(str(ROOT / "runs_sde" / "*" / fname))):
        r = json.loads(Path(p).read_text())
        if not r["portfolio"]: continue
        for c, m in r["portfolio"]["rolling_ols"]["by_cost"].items():
            te = m["test"]; out.append(f"| {r['run_id']} | {float(c):g} | {f(te['sharpe'])} | {f(te['annual_return'], True)} | {f(te['max_drawdown'], True, 1)} | {f(te['turnover_annual'], d=1)} |")
    return "\n".join(out)


def inject(path):
    """Replace the blocks between <!--TABLE:main--> / <!--TABLE:cost--> markers in a markdown file."""
    t = Path(path).read_text()
    for tag, body in (("main", table()), ("cost", cost_table()), ("pit", table("phase3_pit.json"))):
        t = re.sub(r"(<!--TABLE:%s-->).*?(<!--/TABLE:%s-->)" % (tag, tag), lambda m: m.group(1) + "\n" + body + "\n" + m.group(2), t, flags=re.S)
    Path(path).write_text(t)


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--inject": inject(sys.argv[2])
    else: print(table()); print(); print(cost_table())
