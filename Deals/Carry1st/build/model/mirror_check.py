#!/usr/bin/env python3
"""Independent Python re-computation of bc_model.xlsx (same inputs from params.py, same logic, no Excel).
Writes model_numbers.json (pricing as in params.py) and model_numbers_alt.json (included block = ALT_INCL_TPV, for the internal memo only).
Usage: python3 mirror_check.py"""
import json, copy
from params import INP as INP0, SCEN, MONTHS, ALT_INCL_TPV, ALT_T1_UP


def run(INP):
    def yuno(tpv):
        incl = min(tpv, INP["incl_tpv"])
        t1 = max(0, min(tpv, INP["t1_up"]) - max(0, incl))
        t2 = max(0, min(tpv, INP["t2_up"]) - max(INP["t1_up"], incl))
        t3 = max(0, tpv - max(INP["t2_up"], incl))
        usage = t1 * INP["t1"] + t2 * INP["t2"] + t3 * INP["t3"]
        return dict(incl=incl, t1=t1, t2=t2, t3=t3, usage=usage, pf=INP["pf"], total=usage + INP["pf"])

    def l4(s):
        return s["integ"] * s["weeks"] * INP["wk_cost"] * (1 + s["maint"] * INP["horizon"] / 12) / INP["horizon"]

    def model(tx, s, ticket=None, take=None, base_cost=None, credit=0.0):
        ticket = INP["ticket"] if ticket is None else ticket
        take = INP["take"] if take is None else take
        base_cost = INP["base_cost"] if base_cost is None else base_cost
        tpv = tx * ticket
        y = yuno(tpv)
        ycost = y["total"] - credit
        a_cost = tpv * base_cost
        b_prov_pct = base_cost - s["mdr"] / 10000
        b_prov = tpv * b_prov_pct
        b_cost = b_prov + ycost
        b_pct = b_cost / tpv
        margin = take - INP["netflag"] * b_pct
        l1 = a_cost - b_prov
        att = tpv / INP["appr"]
        l2g = att * s["uplift"]; l2c = l2g * margin
        l3g = tpv * s["local"]; l3c = l3g * margin
        L4 = l4(s)
        gross_c = l1 + l2c + l3c + L4
        gross_g = l1 + l2g + l3g + L4
        return dict(tx=tx, tpv=tpv, a_cost=a_cost, a_per_k=a_cost / tpv * 1000, b_prov=b_prov, yuno=ycost, yuno_usage=y["usage"],
                    yuno_pct=ycost / tpv, yuno_tx=ycost / tx, b_cost=b_cost, b_per_k=b_cost / tpv * 1000, b_pct=b_pct,
                    l1=l1, att=att, l2g=l2g, l2c=l2c, l3g=l3g, l3c=l3c, l4=L4, gross_c=gross_c, gross_g=gross_g,
                    net_c=gross_c - ycost, net_g=gross_g - ycost,
                    b_after_k=(b_cost - l2c - l3c - L4) / tpv * 1000, delta_k=a_cost / tpv * 1000 - (b_cost - l2c - l3c - L4) / tpv * 1000,
                    roi=gross_c / ycost, incl=y["incl"], t1=y["t1"], t2=y["t2"], t3=y["t3"])

    out = {"inputs": INP, "scenarios": SCEN, "model": {}, "breakeven": {}, "ramp": {}, "ramp_credit": {}, "pricing": {}, "sensitivity": {}}
    for sn, s in SCEN.items():
        out["model"][sn] = {str(tx): model(tx, s) for tx in INP["tiers"]}
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

    def ramp(credit_on):
        res = {}
        for sn, s in SCEN.items():
            rows, cum, payback = [], 0.0, None
            for i in range(INP["ramp_m"]):
                tx = INP["tiers"][0] + (INP["tiers"][3] - INP["tiers"][0]) * i / (INP["ramp_m"] - 1)
                credit = INP["credit"] if (credit_on and i + 1 <= INP["credit_months"]) else 0.0
                m = model(tx, s, credit=credit)
                cum += m["net_c"]
                if payback is None and cum >= 0:
                    payback = MONTHS[i]
                rows.append(dict(month=MONTHS[i], tx=tx, tpv=m["tpv"], yuno=m["yuno"], credit=credit, gross=m["gross_c"], net=m["net_c"], cum=cum, a_cost=m["a_cost"], b_cost=m["b_cost"]))
            res[sn] = dict(rows=rows, payback=payback or "not within the ramp", cum=cum,
                           yuno_total=sum(r["yuno"] for r in rows), credit_total=sum(r["credit"] for r in rows), gross_total=sum(r["gross"] for r in rows),
                           a_total=sum(r["a_cost"] for r in rows), b_total=sum(r["b_cost"] for r in rows))
        return res
    out["ramp"] = ramp(bool(INP["credit_on"]))
    out["ramp_credit"] = ramp(True)

    for key, ticket in (("avg", INP["ticket"]), ("med", INP["median"])):
        out["pricing"][key] = {}
        for tx in INP["tiers"]:
            tpv = tx * ticket
            y = yuno(tpv)
            out["pricing"][key][str(tx)] = dict(tpv=tpv, **y, pct=y["total"] / tpv, per_tx=y["total"] / tx, usage_tx=y["usage"] / tx,
                                                 fixA=tx * INP["fixA"], fixA_pct=tx * INP["fixA"] / tpv, fixB=tx * INP["fixB"], fixB_pct=tx * INP["fixB"] / tpv)
    sens = {"ticket": {}, "take": {}, "base_cost": {}}
    for t in (5.0, 10.0, 15.0):
        sens["ticket"][str(t)] = {}
        for tx in INP["tiers"]:
            tpv = tx * t
            y = yuno(tpv)
            sens["ticket"][str(t)][str(tx)] = dict(tpv=tpv, yuno=y["total"], usage=y["usage"], pct=y["total"] / tpv, ptx=y["total"] / tx, uptx=y["usage"] / tx,
                                                   fa=tx * INP["fixA"], fa_pct=tx * INP["fixA"] / tpv, fb=tx * INP["fixB"], fb_pct=tx * INP["fixB"] / tpv)
    B = SCEN["Base"]
    for tr in (0.10, 0.15, 0.25):
        sens["take"][str(tr)] = {str(tx): model(tx, B, take=tr)["net_c"] for tx in (INP["tiers"][0], INP["tiers"][3])}
    for bc in (0.03, 0.045, 0.06):
        m = model(INP["tiers"][3], B, base_cost=bc)
        sens["base_cost"][str(bc)] = dict(a_per_k=m["a_per_k"], b_per_k=m["b_per_k"], b_after_k=m["b_after_k"], net_c=m["net_c"], net_c_y=m["net_c"] * 12)
    out["sensitivity"] = sens
    # netflag = 0 variant of the base case (for the internal memo)
    INPn = copy.deepcopy(INP); INPn["netflag"] = 0
    out["netflag0_base"] = {}
    # recompute with netflag 0 by temporarily swapping
    saved = INP["netflag"]; INP["netflag"] = 0
    out["netflag0_base"] = {str(tx): model(tx, B)["net_c"] for tx in INP["tiers"]}
    grid = [(tx, model(tx, B)["net_c"]) for tx in range(5000, 500001, 5000)]
    be = None
    for i, (tx, net) in enumerate(grid):
        if net >= 0:
            be = tx if i == 0 else grid[i - 1][0] + (tx - grid[i - 1][0]) * (0 - grid[i - 1][1]) / (net - grid[i - 1][1]); break
    out["netflag0_base_breakeven"] = be
    INP["netflag"] = saved
    return out


BASE = "/Users/germantatis/Desktop/GTMCoding/Deals/Carry1st/build/model/"
out = run(copy.deepcopy(INP0))
json.dump(out, open(BASE + "model_numbers.json", "w"), indent=1, default=float)
alt = copy.deepcopy(INP0); alt["incl_tpv"] = ALT_INCL_TPV
out_alt = run(alt)
json.dump(out_alt, open(BASE + "model_numbers_alt.json", "w"), indent=1, default=float)
alt2 = copy.deepcopy(INP0); alt2["t1_up"] = ALT_T1_UP
out_alt2 = run(alt2)
json.dump(out_alt2, open(BASE + "model_numbers_alt_step2m.json", "w"), indent=1, default=float)

INP = out["inputs"]
print(f"=== pricing: platform ${INP['pf']:,.0f} incl. first ${INP['incl_tpv']:,.0f} Net TPV; ladder {INP['t1']*1e4:.0f}/{INP['t2']*1e4:.0f}/{INP['t3']*1e4:.0f} bps, bands ${INP['t1_up']:,.0f} / ${INP['t2_up']:,.0f} ===")
for tx in INP["tiers"]:
    p = out["pricing"]["avg"][str(tx)]
    print(f"{tx:>8,} tx  TPV ${p['tpv']:>12,.0f}  usage ${p['usage']:>8,.0f} (t1 {p['t1']:,.0f} t2 {p['t2']:,.0f} t3 {p['t3']:,.0f})  total ${p['total']:>9,.0f}  {p['pct']*100:5.3f}% TPV  ${p['per_tx']:.4f}/tx  vs $0.05 {p['fixA_pct']*100:.2f}%  $0.10 {p['fixB_pct']*100:.2f}%")
print("=== median ticket $5 ===")
for tx in INP["tiers"]:
    p = out["pricing"]["med"][str(tx)]
    print(f"{tx:>8,} tx  TPV ${p['tpv']:>12,.0f}  usage ${p['usage']:>8,.0f}  total ${p['total']:>9,.0f}  {p['pct']*100:5.3f}% TPV  ${p['per_tx']:.4f}/tx  usage/tx ${p['usage_tx']:.4f}")
for sn in SCEN:
    print(f"=== {sn} ===")
    for tx in INP["tiers"]:
        m = out["model"][sn][str(tx)]
        print(f"{tx:>8,}  A ${m['a_cost']:>9,.0f} ({m['a_per_k']:.1f}/k)  B ${m['b_cost']:>9,.0f} ({m['b_per_k']:.2f}/k)  Yuno ${m['yuno']:>8,.0f}  L1 {m['l1']:>7,.0f} L2c {m['l2c']:>7,.0f} L3c {m['l3c']:>6,.0f} L4 {m['l4']:>6,.0f}  gross_c {m['gross_c']:>8,.0f}  NET_c {m['net_c']:>8,.0f}  NET_g {m['net_g']:>8,.0f}  B-after {m['b_after_k']:.2f}/k  ROI {m['roi']:.2f}x")
    print(f"   break-even: {out['breakeven'][sn]}   payback: {out['ramp'][sn]['payback']}   ramp cum: {out['ramp'][sn]['cum']:,.0f}   yuno over ramp: {out['ramp'][sn]['yuno_total']:,.0f}   | with credit: payback {out['ramp_credit'][sn]['payback']}, cum {out['ramp_credit'][sn]['cum']:,.0f}, credit total {out['ramp_credit'][sn]['credit_total']:,.0f}")
print("netflag0 base:", {k: round(v) for k, v in out["netflag0_base"].items()}, "BE", out["netflag0_base_breakeven"])
print("=== ALT (included block ${:,.0f}) ===".format(ALT_INCL_TPV))
for tx in INP["tiers"]:
    p = out_alt["pricing"]["avg"][str(tx)]; mb = out_alt["model"]["Base"][str(tx)]
    print(f"{tx:>8,} tx  Yuno ${p['total']:>8,.0f} ({p['pct']*100:.3f}%, ${p['per_tx']:.4f}/tx)  base NET_c {mb['net_c']:>8,.0f}")
print("ALT break-even:", out_alt["breakeven"], "payback:", {k: v["payback"] for k, v in out_alt["ramp"].items()})
