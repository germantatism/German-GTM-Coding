exec(open("%s/hf_model.py"%__import__('sys').argv[1]).read().split("out=[]")[0])
def r100(x): return int(round(x/100.0))*100
def r1k(x): return int(round(x/1000.0))*1000
res=[]
for (c,sh,a,cc,up,arpu,d,r,f,rem,play) in rows:
    mau=MAU_GLOBAL*sh/100
    if cc is None: res.append(dict(c=c,sh=sh,a=a,mau=mau,play=play,total=0)); continue
    subs=mau*cc; s1=mau*up; a1=s1*arpu
    att=subs/(1-d); s2=(att-subs)*r; a2=s2*arpu*PY
    base=subs+s1+s2; s3=base*f*12*RESCUE; a3=s3*rem*HC
    res.append(dict(c=c,sh=sh,a=a,mau=mau,cc=cc,up=up,arpu=arpu,d=d,r=r,f=f,rem=rem,play=play,subs=subs,s1=s1,a1=a1,s2=s2,a2=a2,s3=s3,a3=a3,total=a1+a2+a3))
res.sort(key=lambda x:-x['total'])
print("| # | Country | Share | Est. MAU (range) | Archetype | Today conv | With-LPM conv | Current paid (est.) | L1 subs | L1 $/yr | L2 recovered | L2 $/yr | L3 rescued/yr | L3 $/yr | Total $/yr | MRR | Total sub impact (L1+L2) |")
for i,x in enumerate(res,1):
    if x['total']==0:
        print(f"| {i} | {x['c']} | {x['sh']:.2f}% | {x['mau']/1e6:.2f}M | {x['a']} | n/a | n/a | n/a | 0 | $0 | 0 | $0 | 0 | $0 | $0 | $0 | {x['play']} |"); continue
    lo,hi=x['mau']*0.85/1e6,x['mau']*1.15/1e6
    print(f"| {i} | {x['c']} | {x['sh']:.2f}% | {x['mau']/1e6:.2f}M ({lo:.2f}–{hi:.2f}M) | {x['a']} | {x['cc']*100:.1f}% | {(x['cc']+x['up'])*100:.1f}% (+{x['up']*100:.1f}pp) | {r100(x['subs']):,} | {r100(x['s1']):,} | ${x['a1']/1e6:.2f}M | {r100(x['s2']):,} | ${x['a2']/1e6:.2f}M | {r100(x['s3']):,} | ${x['a3']/1e6:.2f}M | ${x['total']/1e6:.2f}M | ${x['total']/12e6:.3f}M | {r100(x['s1']+x['s2']):,} |")
T=sum(x['total'] for x in res); 
print(f"\nPortfolio: total ${T/1e6:.2f}M/yr = ${T/12e6:.2f}M/mo")
for a in ["Full-stack","Mature","APM-led"]:
    v=sum(x['total'] for x in res if x['a']==a); print(f"{a}: ${v/1e6:.2f}M/yr = ${v/12e6:.2f}M/mo ({v/T*100:.0f}%)")
addr=[x for x in res if x['total']>0]
print("Top3:",f"{sum(x['total'] for x in addr[:3])/T*100:.0f}%",[x['c'] for x in addr[:3]]," Top10:",f"{sum(x['total'] for x in addr[:10])/T*100:.0f}%")
print("Addressable MAU:",f"{sum(x['mau'] for x in addr)/1e6:.2f}M","| weighted today conv:",f"{sum(x['subs'] for x in addr)/sum(x['mau'] for x in addr)*100:.2f}%","| with-LPM:",f"{sum(x['subs']+x['s1'] for x in addr)/sum(x['mau'] for x in addr)*100:.2f}%")
L1=sum(x['a1'] for x in addr); print("L1 top3 share:",f"{sum(sorted([x['a1'] for x in addr],reverse=True)[:3])/L1*100:.0f}%","| L1 top10:",f"{sum(sorted([x['a1'] for x in addr],reverse=True)[:10])/L1*100:.0f}%")
print("L1 ranking:"); 
for i,x in enumerate(sorted(addr,key=lambda x:-x['a1']),1): print(f"{i:2d} {x['c']:22s} MAU {x['mau']/1e6:.2f}M today {x['cc']*100:.1f}% with-LPM {(x['cc']+x['up'])*100:.1f}% (+{x['up']*100:.1f}pp) users {r100(x['s1']):,} L1 MRR ${x['a1']/12e6:.2f}M")
