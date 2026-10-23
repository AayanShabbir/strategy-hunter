import json,numpy as np,pandas as pd,warnings;warnings.filterwarnings("ignore")
from arch.bootstrap import SPA
from scipy.stats import norm,skew,kurtosis
from itertools import combinations
rng=np.random.default_rng(17);FS=7e-4;FC=20e-4;N=392;NT=10000
BASK=['AAPL','MSFT','NVDA','AMZN','GOOGL','META','AVGO','JPM','LLY','TSLA']
def supertrend(h,l,c,n=10,m=3):
    tr=np.maximum(h-l,np.maximum(abs(h-np.r_[np.nan,c[:-1]]),abs(l-np.r_[np.nan,c[:-1]])));tr[0]=h[0]-l[0]
    atr=pd.Series(tr).ewm(alpha=1/n,adjust=False,min_periods=n).mean().values
    hl=(h+l)/2;bu=hl+m*atr;bl=hl-m*atr;fu=bu.copy();fl=bl.copy();d=np.zeros(len(c))
    for i in range(1,len(c)):
        if np.isnan(atr[i]):continue
        fu[i]=bu[i] if (np.isnan(fu[i-1]) or bu[i]<fu[i-1] or c[i-1]>fu[i-1]) else fu[i-1]
        fl[i]=bl[i] if (np.isnan(fl[i-1]) or bl[i]>fl[i-1] or c[i-1]<fl[i-1]) else fl[i-1]
        if d[i-1]<=0: d[i]=1 if c[i]>fu[i] else -1
        else: d[i]=-1 if c[i]<fl[i] else 1
    return d
def raw_pos(df,mode):
    d=supertrend(df.high.values,df.low.values,df.close.values);up=(d>0).astype(float)
    if mode=='LS': p=np.where(d>0,1.,np.where(d<0,-1.,0.))
    elif mode=='SMA200': p=up*(df.close>df.close.rolling(200).mean()).values
    elif mode=='RV':
        rv=(df.volume/df.volume.shift(1).rolling(20).mean()).values;p=np.zeros(len(d));
        for i in range(1,len(d)):
            if up[i]==0:p[i]=0
            elif p[i-1]==1:p[i]=1
            elif up[i-1]==0 and rv[i]>=1.5:p[i]=1
    else: p=up
    return pd.Series(p,index=df.index)
def sret(P,R,fee):return P*R.fillna(0)-fee*P.diff().abs().fillna(P.abs())
# daily stocks
d=pd.read_pickle('/workspace/trading-desk/validation/hunt2/d1_500.pkl')
def px(f):x=d[f].unstack(0);x.index=pd.to_datetime(x.index).tz_localize(None).normalize();return x
F={f:px(f) for f in ['open','high','low','close','volume']}
R=(F['open'].shift(-1)/F['open']-1).iloc[:-1];days=R.index;nd=len(days);cut=days[int(nd*.7)];oos=days>=cut
spy=R['SPY'].fillna(0)
dv=(F['close']*F['volume'])[F['close'].index<cut].median().drop(['SPY','QQQ']);TOP50=list(dv.nlargest(50).index)
def sym_df(s):
    x=pd.DataFrame({f:F[f][s] for f in F}).dropna();return x
rets={};POS={};RR={}
specs={'T1_SPY_LS':(['SPY'],'LS'),'T2_QQQ_LS':(['QQQ'],'LS'),'T3_SPY_SMA200':(['SPY'],'SMA200'),'T4_QQQ_SMA200':(['QQQ'],'SMA200'),
 'T5_BASKET_SMA200':(BASK,'SMA200'),'T6_SPY_RV':(['SPY'],'RV'),'T7_QQQ_RV':(['QQQ'],'RV'),'T8_BASKET_RV':(BASK,'RV'),'T11_TOP50_LF':(TOP50,'LF')}
for k,(syms,mode) in specs.items():
    P=pd.DataFrame({s:raw_pos(sym_df(s),mode).shift(1).reindex(days).fillna(0) for s in syms})
    POS[k]=P;RR[k]=R[syms];rets[k]=pd.DataFrame({s:sret(P[s],R[s],FS) for s in syms}).mean(1)
# 1h intraday
I=pd.read_pickle('/workspace/trading-desk/validation/data/ALL_15m.pkl');irets={};ipos={}
for s in ['SPY','QQQ']:
    x=I.loc[s].copy();x.index=x.index.tz_convert('America/New_York');t=x.index.time
    x=x[(t>=pd.Timestamp('09:30').time())&(t<pd.Timestamp('16:00').time())]
    h=x.resample('1h',offset='30min').agg({'open':'first','high':'max','low':'min','close':'last','volume':'sum'}).dropna()
    dd=pd.Series(h.index.normalize(),index=h.index);last=dd!=dd.shift(-1);first=dd!=dd.shift(1)
    sig=supertrend(h.high.values,h.low.values,h.close.values);p=pd.Series((sig>0).astype(float),index=h.index).shift(1).fillna(0)
    p[first]=0;p[last]=0  # enter earliest at 2nd bar open; flat at last bar open of session
    r=(h.open.shift(-1)/h.open-1);r[last]=0
    br=p*r.fillna(0)-FS*p.diff().abs().fillna(0)
    k=f'T{9 if s=="SPY" else 10}_{s}_1h';irets[k]=br.groupby(dd.dt.tz_localize(None)).sum();ipos[k]=p
# crypto
crets={};cpos={};cbh={}
for s in ['BTC','ETH']:
    j=json.load(open(f'/workspace/research_lab/data/crypto/{s}.json'))['bars'][f'{s}/USD']
    x=pd.DataFrame(j).rename(columns=dict(o='open',h='high',l='low',c='close',v='volume'));x.index=pd.to_datetime(x.t).dt.tz_localize(None);x=x[['open','high','low','close','volume']]
    r=(x.open.shift(-1)/x.open-1).iloc[:-1];cbh[s]=r
    for mode,tn in [('LF',12 if s=='BTC' else 13),('LS',14 if s=='BTC' else 15)]:
        p=raw_pos(x,mode).shift(1).reindex(r.index).fillna(0);k=f'T{tn}_{s}_{mode}';cpos[k]=p;crets[k]=sret(p,r,FC)
def st(r,ann=252):
    r=r.dropna();t=(1+r).prod()-1;sh=r.mean()/r.std()*np.sqrt(ann) if r.std()>0 else 0;eq=(1+r).cumprod();m=(eq/eq.cummax()-1).min()
    return dict(ret=round(t*100,2),sharpe=round(sh,2),maxdd=round(m*100,2))
def trades(P,R,fee):
    out=[]
    for s in P.columns:
        p=P[s].values;r=R[s].fillna(0).values;i=0
        while i<len(p):
            if p[i]!=0:
                j=i;g=1.
                while j<len(p) and p[j]==p[i]:g*=1+p[i]*r[j];j+=1
                out.append(g*(1-fee)**2-1);i=j
            else:i+=1
    return len(out),round(100*np.mean(np.array(out)>0),1) if out else 0
def shuffle(v):
    ch=np.r_[0,np.flatnonzero(np.diff(v))+1,len(v)];lens=np.diff(ch);vals=v[ch[:-1]].copy()
    o=rng.permutation(len(lens));out=np.repeat(vals[o],lens[o]);return out
def twin_p(P,R,fee,real):
    Rv=R.fillna(0).values;Pv=P.values;cnt=0
    for _ in range(NT):
        W=np.column_stack([shuffle(Pv[:,j]) for j in range(Pv.shape[1])])
        r=(W*Rv-fee*np.abs(np.diff(np.vstack([W[:1]*0,W]),axis=0))).mean(1);cnt+=np.prod(1+r)-1>=real
    return (cnt+1)/(NT+1)
def dsr(r,v):
    r=r.dropna();T=len(r);sr=r.mean()/r.std();g=0.5772156649
    e=np.sqrt(v)*((1-g)*norm.ppf(1-1/N)+g*norm.ppf(1-1/(N*np.e)))
    return float(norm.cdf((sr-e)*np.sqrt(T-1)/np.sqrt(1-skew(r)*sr+kurtosis(r)/4*sr**2)))
def spa(bench,o):s=SPA(-bench,-o.reshape(-1,1),reps=2000,seed=1);s.compute();return round(float(s.pvalues['consistent']),3)
OOS={};res={}
for k in rets:OOS[k]=rets[k][oos]
for k in irets:v=irets[k];ic=v.index[int(len(v)*.7)];OOS[k]=v[v.index>=ic]
for k in crets:v=crets[k];cc=v.index[int(len(v)*.7)];OOS[k]=v[v.index>=cc]
srv=max(pd.Series({k:v.mean()/v.std() for k,v in OOS.items()}).var(),1e-8)
for k,o in OOS.items():
    if k in rets:
        P=POS[k][oos];Rk=RR[k][oos];fee=FS;ann=252;IS=rets[k][~oos];b=spy[oos]
    elif k in irets:
        p=ipos[k];ic=o.index[0];P=None;fee=FS;ann=252;IS=irets[k][irets[k].index<ic];b=spy.reindex(o.index).fillna(0)
    else:
        s=k.split('_')[1];v=crets[k];cc=o.index[0];P=cpos[k][cpos[k].index>=cc].to_frame(s);Rk=cbh[s][cbh[s].index>=cc].to_frame(s);fee=FC;ann=365;IS=v[v.index<cc];b=cbh[s].reindex(o.index).fillna(0)
    real=(1+o).prod()-1
    if P is None:
        pp=p[p.index.normalize().tz_localize(None)>=ic];s=k.split('_')[1];x=I.loc[s]
        # twin for 1h: sign-flip day bootstrap (as h16 15m), conservative proxy
        bs=np.array([np.prod(1+o.values*rng.choice([-1,1],len(o)))-1 for _ in range(NT)]);pv=(np.sum(bs>=real)+1)/(NT+1)
        ntr=int(((pp.diff()>0)).sum());wins=None
        dd_=pd.Series(pp.index.normalize(),index=pp.index)
    else:
        pv=twin_p(P,Rk,fee,real);ntr,wins=trades(P,Rk,fee)
    r=dict(IS=st(IS,ann),OOS=st(o,ann),OOS_window=f'{o.index[0].date()}..{o.index[-1].date()}',trades_OOS=ntr,win_pct=wins,
      bench_same_window=st(b,ann),blend70_same_window=st(0.7*b,ann) if k not in crets else None,
      p_twin=round(float(pv),4),holm_N392=min(1.,round(float(pv)*N,4)),DSR=round(dsr(o,srv),3),
      SPA_vs_bench=spa(b.values,o.values),SPA_vs_70_30=spa(0.7*b.values,o.values) if k not in crets else None)
    res[k]=r
# 1h trades & win%: count from position runs
for k in irets:
    p=ipos[k];s=k.split('_')[1];x=I.loc[s]
    ic=OOS[k].index[0];pp=p[p.index.tz_localize(None).normalize()>=ic]
    # recompute per-trade from 1h opens
    xx=x.copy();xx.index=xx.index.tz_convert('America/New_York')
    h=xx[(xx.index.time>=pd.Timestamp('09:30').time())&(xx.index.time<pd.Timestamp('16:00').time())].resample('1h',offset='30min').agg({'open':'first'}).dropna().open
    r=(h.shift(-1)/h-1).reindex(pp.index).fillna(0);n,w=trades(pp.to_frame(s),r.to_frame(s),FS);res[k]['trades_OOS']=n;res[k]['win_pct']=w
# PBO across stock daily trials + 1h (common dates)
allr=pd.concat([pd.DataFrame(rets),pd.DataFrame(irets)],axis=1).dropna();M=allr.values;S=16;bl=np.array_split(np.arange(len(M)),S);lo=[]
for c in combinations(range(S),S//2):
    a_=np.concatenate([bl[i] for i in c]);b_=np.concatenate([bl[i] for i in range(S) if i not in c])
    A=M[a_].mean(0)/M[a_].std(0);B=M[b_].mean(0)/M[b_].std(0);j=np.argmax(A);w=((B<B[j]).sum()+.5)/len(B);lo.append(np.log(w/(1-w)))
pbo=float(np.mean(np.array(lo)<=0))
for k,r in res.items():
    b=r['bench_same_window']['ret'];r['pass']=bool(r['OOS']['ret']>0 and r['OOS']['ret']>b and r['holm_N392']<0.05 and r['DSR']>0.95 and r['SPA_vs_bench']<0.05 and (r['SPA_vs_70_30'] is None or r['SPA_vs_70_30']<0.05) and pbo<0.5)
res['_meta']=dict(N=N,PBO=round(pbo,3),daily_IS=f'{days[0].date()}..{days[~oos][-1].date()}',daily_OOS=f'{cut.date()}..{days[-1].date()}',TOP50=TOP50,
  SPY_OOS=st(spy[oos]),SPY70_OOS=st(0.7*spy[oos]),QQQ_OOS=st(R['QQQ'][oos].fillna(0)),BASKET_BH_OOS=st(R[BASK][oos].fillna(0).mean(1)),TOP50_BH_OOS=st(R[TOP50][oos].fillna(0).mean(1)))
json.dump(res,open('results.json','w'),indent=1,default=str);print(json.dumps(res,indent=1,default=str))
best=max([k for k in res if not k.startswith('_')],key=lambda k:res[k]['OOS']['sharpe'])
import quantstats as qs
o=OOS[best];o.index=pd.to_datetime(o.index)
b=spy.reindex(o.index).fillna(0) if 'BTC' not in best and 'ETH' not in best else cbh[best.split('_')[1]].reindex(o.index).fillna(0)
qs.reports.html(o,benchmark=b,output='tearsheet.html',title=f'h17 best-by-OOS-Sharpe {best}');print('BEST',best)
