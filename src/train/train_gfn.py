"""SDE Phase 2: GFlowNet training on the train split only (blueprint; AlphaSAGE Algorithm 1).

    .venv17/bin/python -m src.train.train_gfn --universe csi300 --episodes 10000 --seed 0

Every sampled formula is written to the append-only ledger (src/audit/ledger.jsonl) before the loop moves on.
Validation/test prices are never loaded here (load_panel(upto='train')); see src/train/evaluate_pool.py.
Hyper-parameters: blueprint/AlphaSAGE Table 4 (hidden 128, entropy 0.01, lr 1e-4, SA weight 1.0, NOV weight 0.3,
pool capacity 50, 10k episodes on CSI300). Unspecified in the blueprint (chosen here, logged in config.json):
update every 16 episodes (loss summed), log Z lr 1e-1 (torchgfn default for lr_Z), KNN K=5, linear annealing of lambda/eta to 0.
"""
from __future__ import annotations
import argparse, json, os, time, csv, warnings
from pathlib import Path
import numpy as np, torch
warnings.filterwarnings("ignore")
from src.audit.ledger import Ledger, DEFAULT_PATH
from src.data.loader import load_panel, SPLITS
from src.dsl.grammar import parse_ast, parse_expr
from src.gflownet.policy import GFlowNetPolicy
from src.rewards.multi_faceted import Cells, FactorPool, MultiFacetedReward, POOL_CAP

ROOT = Path(__file__).resolve().parents[2]


def run(args):
    torch.set_num_threads(1); torch.manual_seed(args.seed); np.random.seed(args.seed)
    run_id = args.run_id or f"{args.universe}_s{args.seed}_{time.strftime('%Y%m%d_%H%M%S')}"
    out = ROOT / "runs_sde" / run_id; out.mkdir(parents=True, exist_ok=True)
    ledger = Ledger(args.ledger)
    t0 = time.time()
    panel = load_panel(args.universe, upto="train")
    s, e = SPLITS[args.universe]["train"]
    cells = Cells(panel, s, e); cells.set_label(panel.label(e))
    pool = FactorPool(cells, capacity=POOL_CAP)
    policy = GFlowNetPolicy(seed=args.seed)
    reward = MultiFacetedReward(panel, cells, pool, policy.encoder)
    opt = torch.optim.Adam([{"params": [p for n, p in policy.named_parameters() if n != "log_z"], "lr": args.lr},
                            {"params": [policy.log_z], "lr": args.lr_logz}])
    cfg = dict(vars(args), run_id=run_id, split_train=[s, e], n_assets=len(panel.assets), n_cells=int(len(cells.flat)),
               n_days=int(cells.D), data_meta=panel.meta, ledger=str(args.ledger))
    (out / "config.json").write_text(json.dumps(cfg, indent=2, default=str))
    seen = {x["ast_hash"] for x in ledger.entries() if x.get("kind") == "trial" and x.get("universe") == args.universe}
    print(f"[{run_id}] data {panel.data['$close'].shape} cells={len(cells.flat)} days={cells.D}; load {time.time()-t0:.1f}s; "
          f"ledger N so far={ledger.count()}", flush=True)
    curve = csv.writer(open(out / "curve.csv", "w")); curve.writerow(
        ["episode", "elapsed_s", "mean_reward", "mean_abs_ic", "best_abs_ic", "pool", "added", "replaced", "rej_corr", "distinct_frac", "mean_nodes", "entropy", "loss", "log_z"])
    win = dict(r=[], ic=[], nodes=[], h=[], loss=[], new=0); batch = []; best_ic = 0.0; t_start = time.time()
    for ep in range(1, args.episodes + 1):
        roll = policy.sample()
        expr = roll["expr"]; g = parse_ast(expr)
        status, res = "error", None
        try:
            with torch.no_grad(): emb = policy.encoder(g).numpy()
            res = reward(expr, ep, args.episodes, emb)
            status = "degenerate" if res["degenerate"] else pool.try_add(g.canonical, g.hash, emb, res["z"], res["ic"], res["icir"])
        finally:
            ledger.append(dict(
                kind="trial", run_id=run_id, universe=args.universe, split="train", episode=ep, seed=args.seed,
                ast=g.canonical, ast_hash=g.hash, n_nodes=len(g), dup=g.hash in seen,
                ic=res and res["ic"], icir=res and res["icir"], r_ic=res and res["r_ic"], r_sa=res and res["r_sa"],
                r_nov=res and res["r_nov"], lam=res and res["lam"], eta=res and res["eta"], reward=res and res["reward"],
                pool_status=status, pool_size=len(pool)))
        seen.add(g.hash)
        batch.append(policy.tb_loss(roll["sum_logp"], torch.log(torch.tensor(res["reward"])), roll["sum_entropy"], args.entropy)[0])
        if len(batch) == args.update_every:
            loss = torch.stack(batch).sum(); opt.zero_grad(); loss.backward()
            torch.nn.utils.clip_grad_norm_(policy.parameters(), 10.0); opt.step()
            win["loss"].append(loss.item() / args.update_every); batch = []
        win["r"].append(res["reward"]); win["nodes"].append(len(g)); win["h"].append(float(roll["sum_entropy"]))
        if np.isfinite(res["ic"]): win["ic"].append(abs(res["ic"])); best_ic = max(best_ic, abs(res["ic"]))
        if ep % args.log_every == 0 or ep == args.episodes:
            row = [ep, round(time.time() - t_start, 1), np.mean(win["r"]), np.mean(win["ic"]) if win["ic"] else float("nan"), best_ic,
                   len(pool), pool.added, pool.replaced, pool.rejected_corr, len(seen) / max(ep, 1), np.mean(win["nodes"]),
                   np.mean(win["h"]), np.mean(win["loss"]) if win["loss"] else float("nan"), float(policy.log_z)]
            curve.writerow(row); print(" ".join(f"{x:.4g}" if isinstance(x, float) else str(x) for x in row), flush=True)
            win = dict(r=[], ic=[], nodes=[], h=[], loss=[], new=0)
            (out / "curve.csv").open("a").close()
        if ep % args.ckpt_every == 0 or ep == args.episodes:
            torch.save(policy.state_dict(), out / "policy.pt")
            save_pool(pool, out / "pool.json", ep)
    ledger.append(dict(kind="run_end", run_id=run_id, universe=args.universe, episodes=args.episodes, pool_size=len(pool),
                       elapsed_s=round(time.time() - t_start, 1)))
    print(f"[{run_id}] done in {time.time()-t_start:.0f}s; pool={len(pool)} added={pool.added} replaced={pool.replaced} "
          f"rej_corr={pool.rejected_corr}; ledger verify={ledger.verify()}", flush=True)
    return out


def save_pool(pool: FactorPool, path: Path, episode: int):
    mem = [dict(expr=m.expr, ast_hash=m.ast_hash, train_ic=m.ic, train_icir=m.icir, sign=m.sign) for m in pool.members]
    path.write_text(json.dumps(dict(episode=episode, size=len(mem), max_pairwise_corr=pool.max_pairwise_corr() if len(mem) > 1 else 0.0,
                                    members=mem), indent=1))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--universe", default="csi300"); ap.add_argument("--episodes", type=int, default=10000)
    ap.add_argument("--seed", type=int, default=0); ap.add_argument("--run-id", default=None)
    ap.add_argument("--lr", type=float, default=1e-4); ap.add_argument("--lr-logz", type=float, default=1e-1)
    ap.add_argument("--entropy", type=float, default=0.01); ap.add_argument("--update-every", type=int, default=16)
    ap.add_argument("--log-every", type=int, default=100); ap.add_argument("--ckpt-every", type=int, default=500)
    ap.add_argument("--ledger", default=str(DEFAULT_PATH))
    run(ap.parse_args())
