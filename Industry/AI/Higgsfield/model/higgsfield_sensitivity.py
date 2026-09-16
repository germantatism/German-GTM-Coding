import importlib.util,sys
spec=importlib.util.spec_from_file_location("m","%s/hf_model.py"%sys.argv[1]); 
# re-implement compactly for variants
rows_base=None
exec(open(sys.argv[1]+"/hf_model.py").read().split("out=[]")[0])  # loads MAU_GLOBAL, PY, HC, RESCUE, rows
def run(rows, mau_global=MAU_GLOBAL, up_mult=1.0, arpu_over=None, dm_up=None, em_up=None, label=""):
    L1=L2=L3=0; l1s=l2s=l3s=0
    for (c,sh,a,cc,up,arpu,d,r,f,rem,play) in rows:
        if cc is None: continue
        mau=mau_global*sh/100
        if dm_up is not None and a in ("Mature","APM-led"): up=dm_up
        if em_up is not None and a=="Full-stack": up=em_up
        up*=up_mult
        if arpu_over: arpu=arpu_over.get(a,arpu); rem=arpu/2
        subs=mau*cc; s1=mau*up; a1=s1*arpu
        att=subs/(1-d); s2=(att-subs)*r; a2=s2*arpu*PY
        base=subs+s1+s2; s3=base*f*12*RESCUE; a3=s3*rem*HC
        L1+=a1;L2+=a2;L3+=a3;l1s+=s1;l2s+=s2;l3s+=s3
    T=L1+L2+L3
    print(f"{label:58s} L1 ${L1/1e6:5.1f}M  L2 ${L2/1e6:4.1f}M  L3 ${L3/1e6:4.1f}M  TOTAL ${T/1e6:5.1f}M/yr  (${T/12e6:4.2f}M/mo) | subs L1 {l1s/1e3:.0f}K L2 {l2s/1e3:.0f}K L3 {l3s/1e3:.0f}K")
run(rows,label="BASE (12M MAU; EM +2.0pp, DM +1.0pp; ARPU 240/300)")
run(rows,mau_global=16e6,label="MAU 16M (30M registered x ~53%)")
run(rows,mau_global=9e6,label="MAU 9M (downside)")
run(rows,em_up=0.035,dm_up=0.03,label="xAI-level uplift (EM +3.5pp, DM +3pp), same ARPU")
run(rows,arpu_over={"Full-stack":300,"Mature":360,"APM-led":360},label="Brief ARPU $300 EM / $360 DM")
run(rows,em_up=0.035,dm_up=0.03,arpu_over={"Full-stack":300,"Mature":360,"APM-led":360},mau_global=16e6,label="ALL at xAI/brief levels + 16M MAU")
run(rows,em_up=0.010,dm_up=0.005,label="Downside uplift (EM +1.0pp, DM +0.5pp)")
