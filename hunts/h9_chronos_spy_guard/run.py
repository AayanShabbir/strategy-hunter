import sys,json,numpy as np,pandas as pd,vectorbt as vbt
sys.path.insert(0,'/workspace/research_lab/vendor/pypbo'); import importlib; pb=importlib.import_module("pypbo.pbo")
from scipy import stats as ss
from statsmodels.stats.multitest import multipletests
from arch.bootstrap import SPA
from skfolio.model_selection import CombinatorialPurgedCV
o=pd.read_pickle('/workspace/trading-desk/validation/data/ALL_1d.pkl').loc['SPY']
f=pd.read_parquet('forecasts.parquet').set_index('ts')
O=o['open']; C=5e-4; N=298
sig={'V1_chronos_median_trend':(f.q50>=f.close).astype(float),
     'V2_chronos_q10_guard':(~(f.q10/f.close-1< -0.04)).astype(float)}
oi=O.loc[f.index[0]:]                       # open prices from first signal day
res={}; R={}
for k,s in sig.items():
    tgt=s.reindex(oi.index).shift(1)        # decided at close t, executed at open t+1
    pf=vbt.Portfolio.from_orders(oi,size=tgt,size_type='targetpercent',fees=C,init_cash=1e4,freq='1D')
    R[k]=pf.returns().iloc[1:]
    res[k]={'pct_time_in_SPY':round(float(s.mean()*100),1),'switches':int(s.diff().abs().sum())}
spy=oi.pct_change().iloc[1:]; R=pd.DataFrame(R); R['SPY']=spy; R['SPY70_cash30']=0.7*spy
R.index=R.index.tz_localize(None).normalize(); K=int(len(R)*.7); IS,OOS=R.iloc[:K],R.iloc[K:]
def st(r): a=np.cumprod(1+r.values); return dict(ret_pct=round(float((a[-1]-1)*100),2),cagr_pct=round(float((a[-1]**(252/len(r))-1)*100),2),sharpe=round(float(r.mean()/r.std()*np.sqrt(252)),2),maxdd_pct=round(float(((a/np.maximum.accumulate(a))-1).min()*100),2))
out={'periods':{'IS':[str(IS.index[0].date()),str(IS.index[-1].date())],'OOS':[str(OOS.index[0].date()),str(OOS.index[-1].date())]}}
for c in R: out[c]={'IS':st(IS[c]),'OOS':st(OOS[c]),**res.get(c,{})}
# desk context: 70% sleeve guarded vs 70% SPY core (rest cash)
for k in sig: out[k]['desk70_OOS']=st(0.7*OOS[k])
# p-values: OOS excess vs SPY, one-sided
pv={}
for k in sig:
    d=OOS[k]-OOS.SPY; pv[k]=float(1-ss.t.cdf(d.mean()/d.std(ddof=1)*np.sqrt(len(d)),len(d)-1))
    out[k]['p_excess_vs_SPY']=round(pv[k],4)
    out[k]['holm_p_adj']=round(float(multipletests([pv[k]]+[1.0]*(N-1),method='holm')[1][0]),4)
# CPCV path Sharpes
cv=CombinatorialPurgedCV(n_folds=6,n_test_folds=2,purged_size=5)
X=R.values
for k in sig:
    j=list(R).index(k); sh=[]
    for tr,te in cv.split(X):
        for t in te: r=X[t,j]; sh.append(r.mean()/r.std()*np.sqrt(252))
    s_spy=[]
    for tr,te in cv.split(X):
        for t in te: r=X[t,list(R).index('SPY')]; s_spy.append(r.mean()/r.std()*np.sqrt(252))
    d=np.array(sh)-np.array(s_spy)
    out[k]['cpcv']={'paths':len(sh),'median_sharpe':round(float(np.median(sh)),2),'spy_median_sharpe':round(float(np.median(s_spy)),2),'frac_paths_beat_spy':round(float((d>0).mean()),2)}
# PBO over the candidate set
p=pb.pbo(R[list(sig)+['SPY']].values,S=8,metric_func=lambda x:np.asarray(x).mean(axis=0)/np.asarray(x).std(axis=0)*np.sqrt(252),threshold=0,n_jobs=1)
out['PBO']=round(float(p.pbo),3)
# DSR at N
srs=[R[k].mean()/R[k].std() for k in sig]
for k in sig:
    r=OOS[k]; out[k]['DSR']=round(float(pb.dsr(r.mean()/r.std(),max(np.std(srs,ddof=1),1e-4),N,len(r),ss.skew(r),ss.kurtosis(r,fisher=False))),3)
# SPA vs both benchmarks (loss = -return)
for bn in ['SPY','SPY70_cash30']:
    spa=SPA(-OOS[bn].values,-OOS[list(sig)].values,reps=5000,seed=11); spa.compute()
    out[f'SPA_p_vs_{bn}']={kk:round(float(v),4) for kk,v in spa.pvalues.items()}
for k in sig:
    o2=out[k]; o2['PASS']=bool(o2['OOS']['sharpe']>out['SPY']['OOS']['sharpe'] and o2['OOS']['ret_pct']>0 and o2['IS']['sharpe']>out['SPY']['IS']['sharpe'] and o2['holm_p_adj']<.05 and max(out['SPA_p_vs_SPY']['consistent'],out['SPA_p_vs_SPY70_cash30']['consistent'])<.05 and out['PBO']<.5 and o2['DSR']>.95)
json.dump(out,open('results.json','w'),indent=1); print(json.dumps(out,indent=1))
import quantstats as qs
for k in sig: qs.reports.html(OOS[k].rename(k),benchmark=OOS.SPY.rename('SPY'),output=f'tearsheet_{k}_OOS_vs_SPY.html',title=f'{k} OOS vs SPY')
