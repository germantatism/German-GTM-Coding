#!/usr/bin/env python3
"""Independent Python re-computation of bc_model.xlsx (same inputs, same logic, no Excel). Writes model_numbers.json."""
import json

INP = dict(
    ticket=10.0, median=5.0, tiers=[50000, 100000, 200000, 450000], take=0.15, netflag=1,
    base_cost=0.045, base_lo=0.03, base_hi=0.06, appr=0.75, wk_cost=2000.0, horizon=24,
    pf=7500.0, N=50000, t1_up=2_000_000.0, t1=0.0045, t2_up=4_000_000.0, t2=0.0035, t3=0.0030,
    fixA=0.05, fixB=0.10, ramp_m=13,
)
SCEN = {
    "Conservative": dict(mdr=25, uplift=0.015, local=0.005, integ=1, weeks=4, maint=0.20),
    "Base": dict(mdr=50, uplift=0.03, local=0.01, integ=2, weeks=6, maint=0.25),
    "Optimistic": dict(mdr=75, uplift=0.05, local=0.02, integ=3, weeks=8, maint=0.30),
}


def yuno(tx, tpv):
    incl = min(tx, INP["N"]) * tpv / tx
    t1 = max(0, min(tpv, INP["t1_up"]) - max(0, incl))
    t2 = max(0, min(tpv, INP["t2_up"]) - max(INP["t1_up"], incl))
    t3 = max(0, tpv - max(INP["t2_up"], incl))
    usage = t1 * INP["t1"] + t2 * INP["t2"] + t3 * INP["t3"]
    return dict(incl=incl, t1=t1, t2=t2, t3=t3, usage=usage, pf=INP["pf"], total=usage + INP["pf"])


def l4(s):
    return s["integ"] * s["weeks"] * INP["wk_cost"] * (1 + s["maint"] * INP["horizon"] / 12) / INP["horizon"]


def model(tx, s, ticket=None, take=None, base_cost=None):
    ticket = INP["ticket"] if ticket is None else ticket
    take = INP["take"] if take is None else take
    base_cost = INP["base_cost"] if base_cost is None else base_cost
    tpv = tx * ticket
    y = yuno(tx, tpv)
    a_cost = tpv * base_cost
    b_prov_pct = base_cost - s["mdr"] / 10000
    b_prov = tpv * b_prov_pct
    b_cost = b_prov + y["total"]
    b_pct = b_cost / tpv
    margin = take - INP["netflag"] * b_pct
    l1 = a_cost - b_prov
    att = tpv / INP["appr"]
    l2g = att * s["uplift"]; l2c = l2g * margin
    l3g = tpv * s["local"]; l3c = l3g * margin
    L4 = l4(s)
    gross_c = l1 + l2c + l3c + L4
    gross_g = l1 + l2g + l3g + L4
    return dict(tx=tx, tpv=tpv, a_cost=a_cost, a_per_k=a_cost / tpv * 1000, b_prov=b_prov, yuno=y["total"], yuno_usage=y["usage"],
                yuno_pct=y["total"] / tpv, yuno_tx=y["total"] / tx, b_cost=b_cost, b_per_k=b_cost / tpv * 1000, b_pct=b_pct,
                l1=l1, att=att, l2g=l2g, l2c=l2c, l3g=l3g, l3c=l3c, l4=L4, gross_c=gross_c, gross_g=gross_g,
                net_c=gross_c - y["total"], net_g=gross_g - y["total"],
                b_after_k=(b_cost - l2c - l3c - L4) / tpv * 1000, delta_k=a_cost / tpv * 1000 - (b_cost - l2c - l3c - L4) / tpv * 1000,
                roi=gross_c / y["total"], incl=y["incl"], t1=y["t1"], t2=y["t2"], t3=y["t3"])


out = {"inputs": INP, "scenarios": SCEN, "model": {}, "breakeven": {}, "ramp": {}, "pricing": {}, "sensitivity": {}}
for sn, s in SCEN.items():
    out["model"][sn] = {str(tx): model(tx, s) for tx in INP["tiers"]}

# break-even (same grid + interpolation as the sheet)
for sn, s in SCEN.items():
    grid = [(tx, model(tx, s)["net_c"]) for tx in range(5000, 500001, 5000)]
    be = None
    for i, (tx, net) in enumerate(grid):
        if net >= 0:
            if i == 0:
                be = tx
            else:
                tx0, n0 = grid[i - 1]
                be = tx0 + (tx - tx0) * (0 - n0) / (net - n0)
            break
    out["breakeven"][sn] = be if be is not None else "above 500,000"

# ramp
for sn, s in SCEN.items():
    rows, cum, payback = [], 0.0, None
    labels = ["Dec 2026", "Jan 2027", "Feb 2027", "Mar 2027", "Apr 2027", "May 2027", "Jun 2027", "Jul 2027", "Aug 2027", "Sep 2027", "Oct 2027", "Nov 2027", "Dec 2027"]
    for i in range(INP["ramp_m"]):
        tx = INP["tiers"][0] + (INP["tiers"][3] - INP["tiers"][0]) * i / (INP["ramp_m"] - 1)
        m = model(tx, s)
        cum += m["net_c"]
        if payback is None and cum >= 0:
            payback = labels[i]
        rows.append(dict(month=labels[i], tx=tx, tpv=m["tpv"], yuno=m["yuno"], gross=m["gross_c"], net=m["net_c"], cum=cum, a_cost=m["a_cost"], b_cost=m["b_cost"]))
    out["ramp"][sn] = dict(rows=rows, payback=payback or "not within the ramp", cum=cum,
                           yuno_total=sum(r["yuno"] for r in rows), gross_total=sum(r["gross"] for r in rows),
                           a_total=sum(r["a_cost"] for r in rows), b_total=sum(r["b_cost"] for r in rows))

# pricing at avg and median ticket
for key, ticket in (("avg", INP["ticket"]), ("med", INP["median"])):
    out["pricing"][key] = {}
    for tx in INP["tiers"]:
        tpv = tx * ticket
        y = yuno(tx, tpv)
        out["pricing"][key][str(tx)] = dict(tpv=tpv, **y, pct=y["total"] / tpv, per_tx=y["total"] / tx,
                                             fixA=tx * INP["fixA"], fixA_pct=tx * INP["fixA"] / tpv, fixB=tx * INP["fixB"], fixB_pct=tx * INP["fixB"] / tpv)

# sensitivity
sens = {"ticket": {}, "take": {}, "base_cost": {}}
for t in (5.0, 10.0, 15.0):
    sens["ticket"][str(t)] = {}
    for tx in INP["tiers"]:
        tpv = tx * t
        y = yuno(tx, tpv)
        sens["ticket"][str(t)][str(tx)] = dict(tpv=tpv, yuno=y["total"], pct=y["total"] / tpv, ptx=y["total"] / tx, fa_pct=tx * INP["fixA"] / tpv, fb_pct=tx * INP["fixB"] / tpv)
B = SCEN["Base"]
for tr in (0.10, 0.15, 0.25):
    sens["take"][str(tr)] = {str(tx): model(tx, B, take=tr)["net_c"] for tx in (INP["tiers"][0], INP["tiers"][3])}
for bc in (0.03, 0.045, 0.06):
    m = model(INP["tiers"][3], B, base_cost=bc)
    sens["base_cost"][str(bc)] = dict(a_per_k=m["a_per_k"], b_per_k=m["b_per_k"], b_after_k=m["b_after_k"], net_c=m["net_c"], net_c_y=m["net_c"] * 12)
out["sensitivity"] = sens

with open("/Users/germantatis/Desktop/GTMCoding/Deals/Carry1st/build/model/model_numbers.json", "w") as f:
    json.dump(out, f, indent=1, default=float)

# console summary
print("=== Yuno cost by tier (avg ticket) ===")
for tx in INP["tiers"]:
    p = out["pricing"]["avg"][str(tx)]
    print(f"{tx:>8,} tx  TPV ${p['tpv']:>12,.0f}  usage ${p['usage']:>9,.0f}  total ${p['total']:>9,.0f}  {p['pct']*100:5.2f}% TPV  ${p['per_tx']:.4f}/tx   vs $0.05 ${p['fixA']:,.0f} ({p['fixA_pct']*100:.2f}%)  vs $0.10 ${p['fixB']:,.0f} ({p['fixB_pct']*100:.2f}%)")
print("=== median ticket $5 ===")
for tx in INP["tiers"]:
    p = out["pricing"]["med"][str(tx)]
    print(f"{tx:>8,} tx  TPV ${p['tpv']:>12,.0f}  total ${p['total']:>9,.0f}  {p['pct']*100:5.2f}% TPV  ${p['per_tx']:.4f}/tx   fixed $0.05 = {p['fixA_pct']*100:.2f}%  $0.10 = {p['fixB_pct']*100:.2f}%")
for sn in SCEN:
    print(f"=== {sn} ===")
    for tx in INP["tiers"]:
        m = out["model"][sn][str(tx)]
        print(f"{tx:>8,}  A ${m['a_cost']:>9,.0f} ({m['a_per_k']:.1f}/k)  B ${m['b_cost']:>9,.0f} ({m['b_per_k']:.1f}/k)  Yuno ${m['yuno']:>8,.0f}  L1 {m['l1']:>7,.0f} L2c {m['l2c']:>7,.0f} L3c {m['l3c']:>6,.0f} L4 {m['l4']:>6,.0f}  gross_c {m['gross_c']:>8,.0f}  NET_c {m['net_c']:>8,.0f}  NET_g {m['net_g']:>8,.0f}  B-after {m['b_after_k']:.1f}/k  ROI {m['roi']:.2f}x")
    print(f"   break-even: {out['breakeven'][sn]}   payback: {out['ramp'][sn]['payback']}   ramp cum: {out['ramp'][sn]['cum']:,.0f}")
print("=== sensitivity take (base) ===", json.dumps(sens["take"], indent=0, default=lambda x: round(x)))
print("=== sensitivity base cost (base, 450K) ===", json.dumps(sens["base_cost"], indent=0, default=lambda x: round(x, 2)))
