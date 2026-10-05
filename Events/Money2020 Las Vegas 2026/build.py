import json, sys, re
S=sys.argv[1]
exec(open(f"{S}/match.py").read().split("# ---- match")[0])
tcl_index = json.load(open(f"{S}/tcl_index.json"))
# attendee-company-norm -> (TCL display name, note)
INC = {
 "coinbase":("Coinbase",""), "walmart":("Walmart",""), "paypal":("PayPal",""), "coins ph":("Coins.ph",""), "elevenlabs":("ElevenLabs",""),
 "copa airlines":("Copa Airlines",""), "affirm":("Affirm",""), "airbnb":("Airbnb",""), "airbnb vacation home nomad dr spicewood tx":("Airbnb","Entrada rara en la lista (Airbnb)"),
 "nordstrom":("Nordstrom",""), "nordstrom card services":("Nordstrom",""), "ifood":("iFood",""), "wix":("Wix",""), "intuit":("Intuit",""), "intuit building 20":("Intuit",""),
 "twilio":("Twilio",""), "toptal":("Toptal",""), "nium":("Nium",""), "shopify":("Shopify",""), "remitly":("Remitly",""),
 "current":("Current",""), "uphold":("Uphold",""), "ebay":("eBay",""), "airalo":("Airalo",""), "gen digital":("Gen Digital (Norton/Avast/AVG)",""),
 "doordash":("DoorDash",""), "remote":("Remote",""), "kikoff":("Kikoff",""), "discord":("Discord",""), "western union":("Western Union",""),
 "wise":("Wise (US)",""), "webull":("Webull",""), "webull financial":("Webull",""), "openai":("OpenAI",""), "cloudflare":("Cloudflare",""), "fastly":("Fastly",""),
 "fanatics":("Fanatics",""), "hubspot":("HubSpot",""), "fareportal":("Fareportal",""), "mercari":("Mercari (US)",""), "adobe":("Adobe",""), "instacart":("Instacart",""),
 "roku":("Roku",""), "wirex":("Wirex",""), "fanduel":("FanDuel",""), "kraken":("Kraken",""), "upwork":("Upwork",""), "klover":("Klover",""), "tesla":("Tesla",""),
 "at and t":("AT&T",""), "airtm":("Airtm",""), "robinhood":("Robinhood",""), "robinhood markets":("Robinhood",""), "perplexity":("Perplexity",""),
 "bitdefender":("Bitdefender",""), "bytedance":("ByteDance (TikTok / CapCut)",""), "chime":("Chime",""), "united airlines":("United Airlines",""),
 "cash app and afterpay":("Cash App",""), "viator tripadvisor":("Viator (Tripadvisor)",""), "progressive insurance":("Progressive",""), "level 20 at progressive":("Progressive","Level 20 = lab de innovación de Progressive"),
 "stonex payments":("StoneX Group",""), "t mobile corporate office":("T-Mobile",""), "bitso business":("Bitso",""), "oficinas bitso":("Bitso",""), "sofi tech solutions":("SoFi",""),
 "booking financial services":("Booking.com","Booking Holdings Financial Services (brazo fintech de Booking Holdings)"), "taco bell corportate yum brands":("Yum! Brands","Taco Bell / Yum! Brands"),
 "warner brothers discovery":("HBO Max (WBD)",""), "max":("HBO Max (WBD)","Verificar: aparece solo como 'Max'"), "credit sesame":("Sesame (Credit Sesame)",""),
 "apple":("Apple Services",""), "apple park":("Apple Services",""), "apple pay":("Apple Services",""), "apple infinite loop campus":("Apple Services",""),
 "amazon":("Amazon",""), "amazon com":("Amazon",""), "amazon business":("Amazon","Amazon Business"), "amazon busienss":("Amazon","Amazon Business"), "amazon locker ruby":("Amazon",""), "amazon services":("Amazon","Amazon UK"),
 "amazon web services":("Amazon","AWS (equipo FSI/ventas cloud, no el equipo de pagos retail)"),
 "rain":("Rain","⚠️ La lista mezcla dos empresas 'Rain': Rain EWA (CEO Alex Bradford = la de la TCL) y Rain stablecoin cards (CEO Farooq Malik). Verificar persona por persona"),
 "paysend":("Paysend",""), "picpay":("PicPay",""), "mixpanel":("Mixpanel",""), "yellow card":("Yellow Card",""),
}
# verify every INC key exists among attendee norms
att_norms = {}
for p in people.values(): att_norms.setdefault(norm(p["company"]), []).append(p)
missing_keys=[k for k in INC if k not in att_norms]
print("INC keys not found among attendees:", missing_keys)
# TCL source lookup by display name
def tcl_src(name):
    n=norm(name)
    if n in tcl_index: return ",".join(s.replace("_"," ") for s in tcl_index[n]["src"])
    # try names list
    for k,v in tcl_index.items():
        if name in v["names"]: return ",".join(s.replace("_"," ") for s in v["src"])
    return "?"
def fl_row(name):
    for r in tsv(f"{S}/tcl/Final_List.tsv")[1]:
        if r["Company"].strip()==name: return r
    return None
FL = {r["Company"].strip(): r for r in tsv(f"{S}/tcl/Final_List.tsv")[1]}
out=[]
for an,(tname,note) in INC.items():
    for p in att_norms.get(an,[]):
        fl = FL.get(tname) or {}
        out.append({
          "tcl_company": tname, "entity": p["company"], "first": p["first"], "last": p["last"], "title": p["title"], "country": p["country"],
          "linkedin": p["linkedin"], "email": p["email"], "company_tier": p["company_tier"].replace(".0",""), "title_tier": p["title_tier"].replace(".0",""),
          "status": p["status"], "yuno": p["yuno"], "comments": p["comments"], "tabs": sorted(set(p["tabs"])),
          "tcl_src": tcl_src(tname), "tcl_industry": fl.get("Industry",""), "tcl_rating": fl.get("Rating (1-10)",""), "tcl_tier": fl.get("Tier",""), "tcl_sf": fl.get("SalesForce Status",""), "tcl_prio": fl.get("Priority Tier",""), "tcl_sdr": fl.get("SDR",""), "note": note})
# sort: by tcl company then title tier then last name
out.sort(key=lambda r:(r["tcl_company"].lower(), r["title_tier"] or "9", r["last"].lower()))
json.dump(out, open(f"{S}/matched.json","w"), ensure_ascii=False, indent=0)
comps = sorted({r["tcl_company"] for r in out}, key=str.lower)
print("companies:", len(comps)); print("people:", len(out)); print("with linkedin:", sum(1 for r in out if r["linkedin"])); print("missing linkedin:", sum(1 for r in out if not r["linkedin"]))
from collections import Counter
print(Counter(r["tcl_company"] for r in out).most_common(80))
# batches for LinkedIn lookup
miss=[r for r in out if not r["linkedin"]]
import math
B=6; n=math.ceil(len(miss)/B)
for i in range(B):
    chunk=miss[i*n:(i+1)*n]
    json.dump([{"id":f"{i}-{j}","first":r["first"],"last":r["last"],"company":r["entity"],"title":r["title"],"country":r["country"]} for j,r in enumerate(chunk)], open(f"{S}/li_batch_{i}.json","w"), ensure_ascii=False, indent=0)
    print(f"batch {i}: {len(chunk)}")
