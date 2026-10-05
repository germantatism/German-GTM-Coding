import re, json, os, sys, csv
from collections import defaultdict, OrderedDict
S = sys.argv[1]
def tsv(path):
    rows = [l.rstrip("\n").split("\t") for l in open(path, encoding="utf-8")]
    hdr = rows[0]; out=[]
    for r in rows[1:]:
        r = r + [""]*(len(hdr)-len(r))
        out.append(dict(zip(hdr, r)))
    return hdr, out
LEGAL = r"\b(inc|incorporated|llc|l\.l\.c|ltd|limited|corp|corporation|co|company|group|holdings|holding|plc|s\.?a\.?|ag|gmbh|b\.?v\.?|n\.?v\.?|pte|pty|s\.?r\.?l\.?|sas|the)\b"
SITE = r"\b(world headquarters|headquarters|hq|global hq|usa|us|uk|north america|americas|latam|brasil|brazil|mexico|m[eé]xico|colombia|argentina|chile|peru|canada|europe|emea|apac|international|intl|new york|ny|san francisco|sf|seattle|austin|miami|florham park|sjc10|sjc|hq1|hq2)\b"
def norm(s):
    s = s.lower().strip()
    s = s.replace("&", " and ").replace("+", " plus ")
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"[–—\-]+", " ", s)
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    s = re.sub(LEGAL, " ", s)
    s = re.sub(SITE, " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s
# ---- TCL side
tcl = OrderedDict()  # norm -> {names:set, src:set, rows:[]}
def add_tcl(name, src, row):
    n = norm(name)
    if not n: return
    e = tcl.setdefault(n, {"names": set(), "src": set(), "rows": []})
    e["names"].add(name.strip()); e["src"].add(src); e["rows"].append((src,row))
for tab in ["Final_List", "TCL_v2", "TCL", "Backups"]:
    hdr, rows = tsv(f"{S}/tcl/{tab}.tsv")
    for r in rows:
        if r.get("Company","").strip(): add_tcl(r["Company"], tab, r)
print("TCL distinct normalized:", len(tcl), "| by source:", {t: sum(1 for e in tcl.values() if t in e['src']) for t in ["Final_List","TCL_v2","TCL","Backups"]})
# ---- attendee side: universe = Raw List Tiered; enrich from other tabs
people = OrderedDict()  # key -> dict
def pkey(first,last,company): return (norm(first), norm(last), norm(company))
def add_person(r, tab):
    first=r.get("First Name","").strip(); last=r.get("Last Name","").strip(); comp=r.get("Company","").strip()
    if not comp or not (first or last): return
    k = pkey(first,last,comp)
    p = people.get(k)
    if p is None:
        p = {"first":first,"last":last,"company":comp,"tabs":[], "title":"", "country":"", "company_tier":"", "title_tier":"", "email":"", "linkedin":"", "phone":"", "status":"", "yuno":"", "comments":"", "notes":"", "speaker":""}
        people[k]=p
    p["tabs"].append(tab)
    for src,dst in [("Job Title","title"),("Country","country"),("Company Tier","company_tier"),("Title Tier","title_tier"),("Email","email"),("Linkedin Url","linkedin"),("Phone","phone"),("Status","status"),("Yuno Attendee","yuno"),("Comments","comments"),("Notes","notes"),("Speaker","speaker")]:
        v = r.get(src,"").strip()
        if v and not p[dst]: p[dst]=v
tabs = ["Raw_List_Tiered","Raw_Merchant_List","Raw_FinX_List","Not_ICP","Enriched_Merchant_List","General_Attendees","Important_Attendees","Confirmed_Meetings","Linkedin_pt_1","cadence_1","x_important"]
for tab in tabs:
    hdr, rows = tsv(f"{S}/m2020/{tab}.tsv")
    for r in rows: add_person(r, tab)
# link 2 has no header: Company, Country, Title, First, Last, Email, LinkedIn, Phone
for l in open(f"{S}/m2020/link_2.tsv", encoding="utf-8"):
    c = l.rstrip("\n").split("\t"); c += [""]*(8-len(c))
    add_person({"Company":c[0],"Country":c[1],"Job Title":c[2],"First Name":c[3],"Last Name":c[4],"Email":c[5],"Linkedin Url":c[6],"Phone":c[7]}, "link_2")
print("attendee people:", len(people), "| companies:", len({p['company'] for p in people.values()}))
# ---- match
att_by_norm = defaultdict(list)
for p in people.values(): att_by_norm[norm(p["company"])].append(p)
exact, prefix, fuzzy = OrderedDict(), OrderedDict(), OrderedDict()
tcl_keys = list(tcl.keys())
for an, plist in att_by_norm.items():
    if not an: continue
    if an in tcl: exact[an] = (an, plist); continue
    hits = [t for t in tcl_keys if len(t)>=4 and (an.startswith(t+" ") or t.startswith(an+" "))]
    if hits: prefix[an] = (hits, plist); continue
    a0 = an.split(" ")[0]
    if len(a0) >= 5:
        hits = [t for t in tcl_keys if t.split(" ")[0]==a0]
        if hits: fuzzy[an] = (hits, plist)
def show(title, d, prefix_mode):
    print(f"\n==== {title}: {len(d)} attendee companies ====")
    for an,(t,plist) in d.items():
        comp = plist[0]["company"]
        if prefix_mode:
            tn = " | ".join(f"{h} [{','.join(sorted(tcl[h]['src']))}]" for h in t)
        else:
            tn = f"{sorted(tcl[t]['names'])} [{','.join(sorted(tcl[t]['src']))}]"
        print(f"- {comp!r} ({len(plist)} ppl, tier {plist[0]['company_tier'] or '?'}) -> {tn}")
show("EXACT", exact, False); show("PREFIX", prefix, True); show("FUZZY first-token", fuzzy, True)
json.dump({"exact": {k:[v[0], [dict(p) for p in v[1]]] for k,v in exact.items()},
           "prefix": {k:[v[0], [dict(p) for p in v[1]]] for k,v in prefix.items()},
           "fuzzy": {k:[v[0], [dict(p) for p in v[1]]] for k,v in fuzzy.items()}}, open(f"{S}/match_raw.json","w"), ensure_ascii=False, indent=0)
json.dump({k:{"names":sorted(v["names"]),"src":sorted(v["src"])} for k,v in tcl.items()}, open(f"{S}/tcl_index.json","w"), ensure_ascii=False)
