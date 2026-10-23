import sys, os, numpy as np, pandas as pd, vectorbt as vbt
H7="/workspace/trading-desk/validation/strategy_hunt_7"; sys.path.insert(0,H7); os.chdir(H7)
from data7 import load
os.chdir(os.path.dirname(os.path.abspath(__file__)))
days,A=load(); ND=len(days); K=int(ND*.7); C=5e-4; idx=pd.to_datetime(pd.Index(days))
rets={}
for s in ("SPY","QQQ","IWM"):
    O,CL=A[s]["open"],A[s]["close"]; e=O[:,25]; x=np.r_[O[1:,0],np.nan]
    sig=(CL[:,24]/O[:,0]-1)< -0.01
    r=np.where(sig&~np.isnan(x)&~np.isnan(e), x/e-1-2*C, 0.0); rets[s]=r
sleeve=pd.Series(sum(rets.values())/3, idx)               # $3.33k each on $10k, non-compounding like hunt7
spy=pd.Series(np.nan_to_num(np.r_[A["SPY"]["open"][1:,0],np.nan]/A["SPY"]["open"][:,0]-1), idx)
def stats(r): r=r.iloc[:-1] if r is sleeve.iloc[K:] else r; return dict(ret_pct=round(r.sum()*100,2) if False else round(float((np.cumprod(1+r.values)[-1]-1)*100),2), sharpe=round(float(r.vbt.returns(freq="D").sharpe_ratio()*np.sqrt(252/365)),2), maxdd_pct=round(float(r.vbt.returns(freq="D").max_drawdown()*100),2))
ois, oos = sleeve.iloc[:K], sleeve.iloc[K:-1]
print("IS ",stats(ois)); print("OOS",stats(oos)); print("OOS trades",int(sum((rets[s][K:-1]!=0).sum() for s in rets)))
blend=0.7*spy.iloc[K:-1]+0.15*oos; core=0.7*spy.iloc[K:-1]
print("blend",stats(blend),"core70",stats(core),"SPY",stats(spy.iloc[K:-1]))
# checks smoke: Holm, SPA, PBO-style, DSR
from statsmodels.stats.multitest import multipletests
from scipy import stats as ss
t=oos.mean()/oos.std()*np.sqrt(len(oos)); p=1-ss.norm.cdf(t)
print("naive p",round(p,4),"Holm reject @N=297:", multipletests([p]+[0.5]*296,method="holm")[0][0])
from arch.bootstrap import SPA
spa=SPA(benchmark=-(0.7*spy.iloc[K:-1]).values*0, models=-(blend-core).values.reshape(-1,1), reps=2000, seed=7); spa.compute(); print("SPA p (blend vs core70)",spa.pvalues.round(3).to_dict())
import quantstats as qs
qs.reports.html(blend.rename("blend"), benchmark=spy.iloc[K:-1].rename("SPY"), output="tearsheet_blend_vs_SPY.html", title="H7 overnight repro blend vs SPY")
print("tearsheet written")
