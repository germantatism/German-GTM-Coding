# Higgsfield x Yuno: conservative three-lever model on German's SimilarWeb top-20 (122 countries)
MAU_GLOBAL = 12_000_000
PY = 0.685   # partial-year factor (unchanged from xAI)
HC = 0.78    # incrementality haircut (unchanged)
RESCUE = 0.40
# country, share%, archetype, cur_conv, uplift_pp, arpu, decline, recov, fail_m, remval, play
rows = [
 ("United States",15.13,"Baseline",None,0,0,0,0,0,0,"Stripe direct, unchanged (home market)"),
 ("India",12.54,"Full-stack",0.005,0.020,240,0.25,0.55,0.035,120,"UPI + UPI AutoPay + RuPay/local debit + retries"),
 ("Russia",3.82,"Excluded",None,0,0,0,0,0,0,"Not addressable (Visa/Mastercard suspended, sanctions)"),
 ("United Kingdom",3.76,"Mature",0.03,0.010,300,0.08,0.40,0.025,150,"PayPal + Open Banking + Apple/Google Pay + retries"),
 ("South Korea",3.71,"APM-led",0.025,0.005,300,0.15,0.40,0.025,150,"Toss / Samsung Pay + local card acquiring + retries (Kakao/Naver/PayCo already live via Stripe)"),
 ("Germany",3.35,"Mature",0.03,0.010,300,0.08,0.40,0.025,150,"PayPal + SEPA DD + Klarna recurring + retries"),
 ("Brazil",3.26,"Full-stack",0.015,0.010,240,0.25,0.55,0.035,120,"Pix Automatico + local BRL acquiring + installments (Pix already live via Stripe)"),
 ("Indonesia",2.89,"Full-stack",0.005,0.020,240,0.25,0.55,0.035,120,"QRIS + GoPay/OVO/DANA/ShopeePay + local cards"),
 ("Spain",2.31,"Mature",0.03,0.010,300,0.08,0.40,0.025,150,"Bizum + PayPal + SCA-aware retries"),
 ("Italy",2.19,"Mature",0.03,0.010,300,0.08,0.40,0.025,150,"PayPal + Satispay + Bancomat Pay / PostePay"),
 ("France",2.02,"Mature",0.03,0.010,300,0.08,0.40,0.025,150,"Cartes Bancaires routing + PayPal / SEPA"),
 ("Canada",2.01,"Mature",0.03,0.010,300,0.08,0.40,0.025,150,"Interac e-Transfer + PayPal + local CAD acquiring"),
 ("Turkey",1.96,"Full-stack",0.010,0.020,240,0.25,0.55,0.035,120,"TROY + local installments + FX-aware local acquiring"),
 ("Vietnam",1.63,"Full-stack",0.005,0.020,240,0.25,0.55,0.035,120,"MoMo / ZaloPay + VietQR / NAPAS + local cards"),
 ("Netherlands",1.62,"Mature",0.03,0.010,300,0.08,0.40,0.025,150,"iDEAL + SEPA DD + PayPal"),
 ("United Arab Emirates",1.57,"APM-led",0.02,0.010,300,0.15,0.40,0.025,150,"Local AED acquiring + Apple Pay + Tabby/Tamara"),
 ("China",1.55,"APM-led",0.005,0.005,240,0.15,0.40,0.035,120,"Alipay + WeChat Pay cross-border (WeChat Pay already live via Stripe)"),
 ("Japan",1.53,"Mature",0.02,0.010,300,0.08,0.40,0.025,150,"PayPay + Konbini + JCB local routing"),
 ("Mexico",1.33,"Full-stack",0.010,0.020,240,0.25,0.55,0.035,120,"SPEI + OXXO Pay + Mercado Pago + local MXN acquiring"),
 ("Pakistan",1.27,"Full-stack",0.005,0.015,240,0.25,0.55,0.035,120,"JazzCash / Easypaisa + Raast + PayPak debit"),
]
out=[]; tot=dict(mau=0,subs=0,l1s=0,l1=0,l2s=0,l2=0,l3s=0,l3=0,total=0)
arch=dict()
for (c,sh,a,cc,up,arpu,d,r,f,rem,play) in rows:
    mau = MAU_GLOBAL*sh/100
    if cc is None:
        out.append((c,sh,a,mau,0,0,0,0,0,0,0,0,play)); tot['mau']+=mau; continue
    subs = mau*cc
    l1s = mau*up; l1 = l1s*arpu
    att = subs/(1-d); dec = att-subs; l2s = dec*r; l2 = l2s*arpu*PY
    base = subs+l1s+l2s; failed = base*f*12; l3s = failed*RESCUE; l3 = l3s*rem*HC
    total = l1+l2+l3
    out.append((c,sh,a,mau,subs,l1s,l1,l2s,l2,l3s,l3,total,play))
    for k,v in zip(['mau','subs','l1s','l1','l2s','l2','l3s','l3','total'],[mau,subs,l1s,l1,l2s,l2,l3s,l3,total]): tot[k]+=v
    arch[a]=arch.get(a,0)+total
def m(x): return f"${x/1e6:.2f}M"
def k(x): return f"{x/1e3:.0f}K"
print(f"{'Country':22s}{'Share':>7s}{'Arch':>11s}{'MAU':>8s}{'Subs':>7s}{'L1subs':>8s}{'L1$/yr':>9s}{'L2rec':>7s}{'L2$/yr':>9s}{'L3resc':>8s}{'L3$/yr':>9s}{'Total/yr':>10s}{'MRR':>9s}")
for (c,sh,a,mau,subs,l1s,l1,l2s,l2,l3s,l3,total,play) in sorted(out,key=lambda x:-x[11]):
    print(f"{c:22s}{sh:6.2f}%{a:>11s}{mau/1e6:7.2f}M{k(subs):>7s}{k(l1s):>8s}{m(l1):>9s}{k(l2s):>7s}{m(l2):>9s}{k(l3s):>8s}{m(l3):>9s}{m(total):>10s}{m(total/12):>9s}")
print("\nTOTALS  MAU top20:",f"{tot['mau']/1e6:.2f}M","| addressable (ex US, ex RU):",f"{(tot['mau']-12e6*(15.13+3.82)/100)/1e6:.2f}M")
print("current paid subs (addressable):",k(tot['subs']),"| L1 subs:",k(tot['l1s']),"| L2 recovered:",k(tot['l2s']),"| L3 rescued/yr:",k(tot['l3s']))
print("L1:",m(tot['l1']),"| L2:",m(tot['l2']),"| L3:",m(tot['l3']),"| TOTAL:",m(tot['total']),"/yr =",m(tot['total']/12),"/mo")
print("Archetype split:",{a:f"{m(v)} ({v/tot['total']*100:.0f}%)" for a,v in arch.items()})
srt=sorted([o for o in out if o[11]>0],key=lambda x:-x[11])
top3=sum(o[11] for o in srt[:3]); top10=sum(o[11] for o in srt[:10])
print("Top3 share:",f"{top3/tot['total']*100:.0f}%",[o[0] for o in srt[:3]],"| Top10 share:",f"{top10/tot['total']*100:.0f}%")
# sanity checks
pool=210e6
print(f"\nHero as % of ~$210M consumer pool: {tot['total']/pool*100:.1f}% | per registered user/mo (30M): ${tot['total']/30e6/12:.3f} | vs May-2025 ARR $11M: {tot['total']/11e6:.1f}x")
# cost of delay: competitor captures share of L1 subs (OpenAI deck ratios 11/44/72/86%) ; cumulative lost revenue with linear ramp, blended monthly ARPU
blend_arpu = tot['l1']/tot['l1s']/12
pts={0:0,6:0.11,12:0.44,18:0.72,24:0.86}
import bisect
cum=0; ks=sorted(pts)
for mth in range(1,25):
    i=bisect.bisect_right(ks,mth)-1; a0,a1=ks[i],ks[min(i+1,len(ks)-1)]
    frac = pts[a0] if a1==a0 else pts[a0]+(pts[a1]-pts[a0])*(mth-a0)/(a1-a0)
    cum += frac*tot['l1s']*blend_arpu
    if mth in (6,12,18,24): print(f"month {mth}: competitor takes {frac*tot['l1s']/1e3:.0f}K subs | cumulative lost ${cum/1e6:.1f}M")
print(f"blended L1 monthly ARPU ${blend_arpu:.2f}")
