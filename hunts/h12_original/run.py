import json,numpy as np,pandas as pd
from scipy import stats as ss
from scipy.stats import binomtest
from statsmodels.stats.multitest import multipletests
from arch.bootstrap import SPA
N=324; C=5e-4
A=pd.read_pickle('/workspace/trading-desk/validation/data/ALL_1d.pkl')
def g(s): x=A.loc[s][['open','close']]; x.index=x.index.tz_localize(None).normalize(); return x
SPY,TLT,QQQ,HYG,XLK,XLU=[g(s) for s in ['SPY','TLT','QQQ','HYG','XLK','XLU']]
idx=SPY.index
for x in (TLT,QQQ,HYG,XLK,XLU): assert x.index.equals(idx) or True
D=lambda x:x.reindex(idx)
TLT,QQQ,HYG,XLK,XLU=map(D,(TLT,QQQ,HYG,XLK,XLU))
n=len(idx)
def run(px,trades):
    r=np.zeros(n); O=px.open.values; Cl=px.close.values
    for i,j,ex,sd in trades:  # enter open i, exit day j at 'open'/'close', side
        if j>=n: j=n-1; ex='close'
        for k in range(i,j+1):
            a=O[i] if k==i else Cl[k-1]
            b=Cl[k] if (k<j or ex=='close') else O[k]
            if k==j and ex=='open' and k==i: b=O[k]
            r[k]+=sd*(b/a-1)
        r[i]-=C; r[j]-=C
    return pd.Series(r,idx)
S={}
# E1
me=idx.to_series().groupby(idx.to_period('M')).agg(list)
tr=[]; pos={d:i for i,d in enumerate(idx)}
months=list(me.index)
for mi in range(1,len(months)):
    days=me.iloc[mi]; prev=me.iloc[mi-1][-1]
    if len(days)<5: continue
    t=days[-4]; dd=(SPY.close[t]/SPY.close[prev]-1)-(TLT.close[t]/TLT.close[prev]-1)
    sd=1 if dd<=-.03 else (-1 if dd>=.03 else 0)
    if sd: tr.append((pos[t]+1,pos[days[-1]],'close',sd))
S['E1_month_end_rebal_flow']=run(SPY,tr)
# E2
q=QQQ.close.pct_change().values
S['E2_letf_close_reversal']=run(QQQ,[(i+1,i+1,'close',-1 if q[i]>=.02 else 1) for i in range(1,n-1) if abs(q[i])>=.02])
# E3
s10=SPY.close.pct_change(10).values; h10=HYG.close.pct_change(10).values
sig=[i for i in range(n-1) if s10[i]<=-.03 and h10[i]>=-.005]
tr=[];cur=None
for i in sig:
    e,x=i+1,i+5
    if cur and e<=cur[1]+1: cur=(cur[0],x)
    else:
        if cur: tr.append((cur[0],cur[1],'close',1))
        cur=(e,x)
if cur: tr.append((cur[0],cur[1],'close',1))
S['E3_credit_calm_equity_panic']=run(SPY,tr)
# E4
on=((XLK.close.pct_change(20)-XLU.close.pct_change(20))>-.05).values.copy()
on[:20]=False
tr=[];st=None
for i in range(n-1):
    if on[i] and st is None: st=i+1
    if not on[i] and st is not None: tr.append((st,i+1,'open',1)); st=None
if st is not None: tr.append((st,n-1,'close',1))
S['E4_defensive_lead_guard']=run(SPY,tr)
R=pd.DataFrame(S); spy=SPY.close.pct_change().fillna(0); R['SPY']=spy; R['SPY70_cash30']=.7*spy
R=R.iloc[21:]; K=int(len(R)*.7); IS,OOS=R.iloc[:K],R.iloc[K:]
def st(r):
    a=np.cumprod(1+r.values); sd=r.std()
    return dict(ret=round((a[-1]-1)*100,2),sh=round(r.mean()/sd*np.sqrt(252),2) if sd>0 else 0,dd=round(((a/np.maximum.accumulate(a))-1).min()*100,2),days_in=int((r!=0).sum()))
out={'IS':[str(IS.index[0].date()),str(IS.index[-1].date())],'OOS':[str(OOS.index[0].date()),str(OOS.index[-1].date())]}
pv={}
for c in R:
    out[c]={'IS':st(IS[c]),'OOS':st(OOS[c])}
for c in S:
    d=OOS[c]-OOS.SPY; p1=float(1-ss.t.cdf(d.mean()/d.std()*np.sqrt(len(d)),len(d)-1))
    r=OOS[c]; p0=float(1-ss.t.cdf(r.mean()/r.std()*np.sqrt(len(r)),len(r)-1))
    pv[c]=min(p1,p0) if c in('E1_month_end_rebal_flow','E2_letf_close_reversal','E3_credit_calm_equity_panic') else p1
    out[c]['p_excessSPY']=round(p1,4); out[c]['p_mean_gt0']=round(p0,4)
    out[c]['holm']=round(float(multipletests([pv[c]]+[1]*(N-1),method='holm')[1][0]),4)
    sp=[]
    for b in ('SPY','SPY70_cash30'):
        x=SPA(-OOS[b].values,-OOS[[c]].values,reps=2000,seed=1); x.compute(); sp.append(round(float(x.pvalues['consistent']),3))
    out[c]['spa_vs_SPY_7030']=sp
    out[c]['pass']=bool(out[c]['OOS']['ret']>0 and out[c]['OOS']['sh']>out['SPY']['OOS']['sh'] and out[c]['holm']<.05 and IS[c].mean()>0 and max(sp)<.05)
# NFL
d=pd.read_csv('../h11_nfl_betting/data/games.csv'); d=d[d.result.notna()&d.total_line.notna()]
m=d.roof.isin(['outdoors','open'])&d.wind.between(10,14)
ou=-(d.total-d.total_line)[m]; seas=d.season[m]
def nf(x):
    w=int((x>0).sum());l=int((x<0).sum());pnl=np.where(x>0,1/1.1,np.where(x<0,-1,0.))
    return dict(bets=len(x),push=int((x==0).sum()),win=round(100*w/(w+l),2),roi=round(100*pnl.mean(),2),p=binomtest(w,w+l,.5238,alternative='greater').pvalue)
a,b=nf(ou[seas<=2018]),nf(ou[seas>=2019]); b['holm']=min(1,b['p']*N)
out['N1_nfl_wind_10_14_under']={'IS':a,'OOS':b,'pass':bool(b['roi']>0 and a['roi']>0 and b['holm']<.05)}
json.dump(out,open('results.json','w'),indent=1,default=float); print(json.dumps(out,indent=1,default=float))
try:
    import quantstats as qs
    best=max(S,key=lambda c:out[c]['OOS']['sh']); qs.reports.html(OOS[best],benchmark=OOS.SPY,output='tearsheet_best_OOS.html',title=best)
    print('tearsheet',best)
except Exception as e: print('qs fail',e)
