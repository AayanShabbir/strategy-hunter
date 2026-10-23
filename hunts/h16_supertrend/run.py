import json,numpy as np,pandas as pd,warnings;warnings.filterwarnings("ignore")
from arch.bootstrap import SPA
from scipy.stats import norm,skew,kurtosis
from itertools import combinations
rng=np.random.default_rng(16);FEE=5e-4;N=392;NT=10000
BASK=['AAPL','MSFT','NVDA','AMZN','GOOGL','META','AVGO','JPM','LLY','TSLA']
def supertrend(h,l,c,n,m):
    tr=np.maximum(h-l,np.maximum(abs(h-np.r_[np.nan,c[:-1]]),abs(l-np.r_[np.nan,c[:-1]])));tr[0]=h[0]-l[0]
    atr=pd.Series(tr).ewm(alpha=1/n,adjust=False,min_periods=n).mean().values
    hl=(h+l)/2;bu=hl+m*atr;bl=hl-m*atr;fu=bu.copy();fl=bl.copy();d=np.zeros(len(c))
    for i in range(1,len(c)):
        if np.isnan(atr[i]):continue
        fu[i]=bu[i] if (np.isnan(fu[i-1]) or bu[i]<fu[i-1] or c[i-1]>fu[i-1]) else fu[i-1]
        fl[i]=bl[i] if (np.isnan(fl[i-1]) or bl[i]>fl[i-1] or c[i-1]<fl[i-1]) else fl[i-1]
        if d[i-1]<=0: d[i]=1 if c[i]>fu[i] else -1
        else: d[i]=-1 if c[i]<fl[i] else 1
    return (d>0).astype(float)
d=pd.read_pickle('/workspace/trading-desk/validation/hunt2/d1_500.pkl')
def px(f):x=d[f].unstack(0);x.index=pd.to_datetime(x.index).tz_localize(None).normalize();return x
O,H,L,C=px('open'),px('high'),px('low'),px('close')
R=(O.shift(-1)/O-1).iloc[:-1];days=R.index;nd=len(days);cut=days[int(nd*0.7)];oos=days>=cut
spy=R['SPY'].fillna(0)
def pos_series(s,n,m):
    ok=C[s].dropna().index;p=supertrend(H[s][ok].values,L[s][ok].values,C[s][ok].values,n,m)
    return pd.Series(p,index=ok).shift(1).reindex(days).fillna(0)  # signal at close t-1 -> hold from open t
def sret(P,Rr):return P*Rr.fillna(0)-FEE*P.diff().abs().fillna(0)
rets={};POS={}
for u in ['SPY','QQQ','BASKET']:
    for n in [7,10,14]:
        for m in [2,3,4]:
            k=f'{u}_{n}_{m}';syms=BASK if u=='BASKET' else [u]
            P=pd.DataFrame({s:pos_series(s,n,m) for s in syms});POS[k]=P
            rets[k]=pd.DataFrame({s:sret(P[s],R[s]) for s in syms}).mean(1)
# intraday 15m
I=pd.read_pickle('/workspace/trading-desk/validation/data/ALL_15m.pkl')
irets={};ipos={}
for s in ['SPY','QQQ']:
    x=I.loc[s].copy();x.index=x.index.tz_convert('America/New_York');t=x.index.time
    x=x[(t>=pd.Timestamp('09:30').time())&(t<=pd.Timestamp('15:45').time())]
    sig=supertrend(x.high.values,x.low.values,x.close.values,10,3)
    dd=x.index.normalize();last=pd.Series(x.index.time==pd.Timestamp('15:45').time(),index=x.index)
    p=pd.Series(sig,index=x.index).shift(1).fillna(0)
    newday=pd.Series(dd,index=x.index)!=pd.Series(dd,index=x.index).shift(1)
    p[newday]=0;p[last]=0   # enter at bar open after signal within day; flat at 15:45 open
    r=(x.open.shift(-1)/x.open-1);r[last|(pd.Series(dd,index=x.index)!=pd.Series(dd,index=x.index).shift(-1))]=0
    br=p*r.fillna(0)-FEE*p.diff().abs().fillna(0)
    dr=br.groupby(dd.tz_localize(None)).sum();irets[f'{s}_15m_10_3']=dr
iidx=irets['SPY_15m_10_3'].index;icut=iidx[int(len(iidx)*0.7)]
def st(r):
    r=r.dropna();t=(1+r).prod()-1;sh=r.mean()/r.std()*np.sqrt(252) if r.std()>0 else 0;eq=(1+r).cumprod();dd_=(eq/eq.cummax()-1).min()
    return round(t*100,2),round(sh,2),round(dd_*100,2)
def shuffle_pos(p):  # random twin: shuffle run lengths of position runs, random start state
    v=p.values;ch=np.r_[0,np.flatnonzero(np.diff(v))+1,len(v)];lens=np.diff(ch);rng.shuffle(lens)
    st0=rng.integers(0,2);out=np.empty(len(v));i=0;s_=st0
    for L_ in lens:out[i:i+L_]=s_;i+=L_;s_=1-s_
    return out
def twin_p(P,Rr,real):
    Rv=Rr.fillna(0).values;Pv=P.values;cnt=0
    for _ in range(NT):
        W=np.column_stack([shuffle_pos(pd.Series(Pv[:,j])) for j in range(Pv.shape[1])])
        r=(W*Rv-FEE*np.abs(np.diff(np.vstack([W[:1]*0,W]),axis=0))).mean(1)
        cnt+=np.prod(1+r)-1>=real
    return (cnt+1)/(NT+1)
def dsr(r,sr0var):
    r=r.dropna();T=len(r);sr=r.mean()/r.std();g=0.5772156649
    e=np.sqrt(sr0var)*((1-g)*norm.ppf(1-1/N)+g*norm.ppf(1-1/(N*np.e)))
    return float(norm.cdf((sr-e)*np.sqrt(T-1)/np.sqrt(1-skew(r)*sr+(kurtosis(r))/4*sr**2)))
df=pd.DataFrame(rets)
srs=pd.concat([df[oos].mean()/df[oos].std()]+[pd.Series({k:v[v.index>=icut].mean()/v[v.index>=icut].std()}) for k,v in irets.items()])
svar=max(srs.var(),1e-8)
# PBO on common period
allr=pd.concat([df,pd.DataFrame(irets)],axis=1).loc[iidx[0]:].dropna()
M=allr.values;S=16;bl=np.array_split(np.arange(len(M)),S);lo=[]
for c in combinations(range(S),S//2):
    isx=np.concatenate([bl[i] for i in c]);osx=np.concatenate([bl[i] for i in range(S) if i not in c])
    a=M[isx].mean(0)/M[isx].std(0);b_=M[osx].mean(0)/M[osx].std(0);b=np.argmax(a)
    w=((b_<b_[b]).sum()+0.5)/len(b_);lo.append(np.log(w/(1-w)))
pbo=float(np.mean(np.array(lo)<=0))
res={}
spyO=st(spy[oos])
for k in df:
    o=df[k][oos];real=(1+o).prod()-1;syms=POS[k].columns
    pv=twin_p(POS[k][oos],R[list(syms)][oos],real)
    s=SPA(-spy[oos].values,-o.values.reshape(-1,1),reps=2000,seed=1);s.compute()
    res[k]=dict(IS=st(df[k][~oos]),OOS=st(o),p_twin=round(pv,4),holm=min(1,round(pv*N,4)),DSR=round(dsr(o,svar),3),SPA_SPY=round(float(s.pvalues['consistent']),3),
      time_in_mkt=round(float(POS[k].mean().mean()),2),switches_per_yr=round(float(POS[k].diff().abs().sum().mean()/(nd/252)),1))
for k,v in irets.items():
    o=v[v.index>=icut];sp=spy.reindex(o.index).fillna(0)
    s=SPA(-sp.values,-o.values.reshape(-1,1),reps=2000,seed=1);s.compute()
    # twin: sign-flip day bootstrap (no intraday shuffle) -> conservative proxy
    bs=np.array([np.prod(1+o.values*rng.choice([-1,1],len(o)))-1 for _ in range(NT)]);real=(1+o).prod()-1
    pv=(np.sum(bs>=real)+1)/(NT+1)
    res[k]=dict(IS=st(v[v.index<icut]),OOS=st(o),p_twin=round(float(pv),4),holm=min(1,round(float(pv)*N,4)),DSR=round(dsr(o,svar),3),SPA_SPY=round(float(s.pvalues['consistent']),3),SPY_same_window=st(sp))
for k in res:
    r=res[k];r['pass']=bool(r['OOS'][0]>0 and r['OOS'][0]>(r.get('SPY_same_window',spyO))[0] and r['holm']<0.05 and r['DSR']>0.95 and r['SPA_SPY']<0.05 and pbo<0.5)
bh={u:st(R[u][oos].fillna(0)) for u in ['SPY','QQQ']};bh['BASKET']=st(R[BASK][oos].fillna(0).mean(1))
bhis={u:st(R[u][~oos].fillna(0)) for u in ['SPY','QQQ']};bhis['BASKET']=st(R[BASK][~oos].fillna(0).mean(1))
res['_bench']=dict(BH_OOS=bh,BH_IS=bhis,IS=f"{days[0].date()}..{days[~oos][-1].date()}",OOS=f"{cut.date()}..{days[-1].date()}",intraday_OOS=f"{icut.date()}..{iidx[-1].date()}",PBO=round(pbo,3),N=N)
json.dump(res,open('results.json','w'),indent=1,default=str);print(json.dumps(res,indent=1,default=str))
