"""Google Slides spec with logo chips, from the verified sheet data (csv/deck_data.json, written by make_spec_v3.py).
Per country: slide A = providers (live + homologating) as logo chips; slide B = payment methods as logo chips + the
method -> providers table. Small countries get one combined slide. Logos: scratchpad logos/usable.json + aspect.json.
Usage: python3 make_spec_v4.py <scratchpad_logos_dir>"""
import json, os, sys, re, collections
H = os.path.dirname(os.path.abspath(__file__)); LOG = sys.argv[1]
D = json.load(open(os.path.join(H, 'deck_data.json')))
old = json.load(open(os.path.join(H, '..', 'gs', 'deck_spec.json')))
usable = json.load(open(os.path.join(LOG, 'usable.json'))); aspect = json.load(open(os.path.join(LOG, 'aspect.json')))
fallback = json.load(open(os.path.join(LOG, 'fallback.json'))) if os.path.exists(os.path.join(LOG, 'fallback.json')) else {}
def nk(s): return re.sub(r'[^a-z0-9]', '', (s or '').lower())
ALIAS = {'facfirstatlanticcommerce': 'fac', 'antom': 'antomalipay', 'morepayments': 'morepaymentsuniteller', 'banbajo': 'banbajio', 'thaiqrpromptpay': 'thaiqr', 'ovo': 'ovowallet', 'pagofcil': 'pagofacil'}
def chip(name):
    k = nk(name); k = ALIAS.get(k, k) if ALIAS.get(k, k) in usable else k
    if k in usable: return {'name': name, 'logo': usable[k], 'aspect': aspect.get(k, 1.0)}
    return {'name': name, 'logo': fallback.get(nk(name), ''), 'aspect': 1.0}
LATAM1 = ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Mexico', 'Peru', 'Uruguay']
LATAM2 = ['Bolivia', 'Costa Rica', 'Dominican Republic', 'Ecuador', 'El Salvador', 'Guatemala', 'Honduras', 'Nicaragua', 'Panama', 'Paraguay']
SEA = ['Indonesia', 'Malaysia', 'Philippines', 'Singapore', 'Thailand', 'Vietnam', 'Myanmar']
T = LATAM1 + LATAM2 + SEA + ['Israel']
WALLETS = {'Apple Pay', 'Google Pay', 'PayPal'}
def slug(c): return c.lower().replace(' ', '-')
def pl(n, w): return f"{n} {w}" + ('' if n == 1 else 's')
S = [old['slides'][0]]
def live_in(name): return [c for c in T if name in D[c]['live']]
def cc(lst): return f"{len(lst)}: " + ', '.join(lst)
S.append({"id": "named", "type": "table", "kicker": "COVERAGE › THE PROVIDERS YOU NAMED",
  "headline": "Mercado Pago, dLocal, PayU and 2C2P are live through Yuno; PayPlus would be a new connection.",
  "columns": ["Provider", "Status", "Countries live (of the 25 you asked about)", "Payment methods through Yuno"], "col_widths": [0.13, 0.11, 0.42, 0.34],
  "rows": [["Mercado Pago", {"text": "Live", "bold": True}, cc(live_in('Mercado Pago')), "Cards, Checkout Pro, Mercado Pago Wallet, Mercado Pago QR, PIX, Boleto, PSE by market"],
           ["dLocal", {"text": "Live", "bold": True}, cc(live_in('dLocal')), "Cards plus the local methods of each market: PIX, Boleto, SPEI, OXXO, PSE, Efecty, Yape, Clave, QRIS, FPX, Thai QR, TrueMoney and more"],
           ["PayU", {"text": "Live", "bold": True}, cc(live_in('PayU')), "Cards, PSE, OXXO and cash networks in Mexico"],
           ["2C2P", {"text": "Live", "bold": True}, cc(live_in('2C2P')), "Cards"],
           ["PayPlus", {"text": "On request", "bold": True}, "Israel: not connected yet; scoped and built by Yuno on request", "Cards and local methods per PayPlus scope"]],
  "header_style": "dark", "font_size": 7.5, "bold_first_col": True, "zebra": True,
  "note": "Live means the connection is built and available to process payments through Yuno for this country. Method activation is set per merchant."})
def short_methods(d, k=6):
    ms = [m for m, _ in sorted(d['methods'].items(), key=lambda kv: -len(kv[1])) if m != 'Cards']
    return ' · '.join(ms[:k]) + (f' · +{len(ms) - k} more' if len(ms) > k else '') if ms else 'Cards and wallets'
def overview(id_, kicker, headline, countries):
    rows = [[c, str(len(D[c]['live'])), str(len(D[c]['homolog'])), short_methods(D[c])] if c != 'Israel' else ['Israel', '6', '1', 'Cards and wallets · 2 providers to activate · 9 new connections on request'] for c in countries]
    return {"id": id_, "type": "table", "kicker": kicker, "headline": headline, "columns": ["Country", "Providers live", "Homologating", "Local methods through Yuno"],
            "col_widths": [0.17, 0.12, 0.13, 0.58], "rows": rows, "header_style": "dark", "font_size": 8, "bold_first_col": True, "zebra": True}
S.append(overview("sum-latam1", "OVERVIEW › LATAM CORE MARKETS", "Every core LATAM market has dozens of live providers and its main local methods through Yuno.", LATAM1))
S.append(overview("sum-latam2", "OVERVIEW › LATAM REST OF REGION", "The rest of LATAM is covered with redundancy in every country and local methods where they matter.", LATAM2))
S.append(overview("sum-apac", "OVERVIEW › SOUTHEAST ASIA AND ISRAEL", "Southeast Asia runs on global acquirers plus local wallets and QR; Israel runs on Nuvei and five cross-border acquirers today.", SEA + ['Israel']))
def grouped(d):
    g = collections.defaultdict(list)
    for m, ps in d['methods'].items():
        if m != 'Cards': g[tuple(sorted(ps, key=str.lower))].append(m)
    return sorted(((' · '.join(ms), list(ps)) for ps, ms in g.items()), key=lambda kv: (-len(kv[1]), kv[0]))
def method_table(d, max_rows):
    gr = grouped(d); multi = [(m, p) for m, p in gr if len(p) > 1]; single = [(m, p) for m, p in gr if len(p) == 1]
    signed = sorted(set(list(d['signed_m']) + d['signed']))
    while len(multi) + (1 if single else 0) + (1 if d.get('global_m') else 0) + len(signed) > max_rows and multi:
        single.append(multi.pop())
    rows = []
    for m, p in multi:
        sg = [d['signed_m'].get(x, []) for x in m.split(' · ')]; sg = sorted({y for z in sg for y in z})
        if sg: rows.append([m, f"{', '.join(p)} (integrated) · {', '.join(sg)} (signed)", str(len(p) + len(sg))])
        else: rows.append([m, ', '.join(p), str(len(p))])
    if single: rows.append(["Other local methods", '; '.join(f"{m} ({', '.join(p)})" for m, p in sorted(single)), "1 to 2 each"])
    glob = d.get('global_m', {})
    if glob:
        rows.append(["Wallets and global methods via providers", '; '.join(f"{m} ({', '.join(sorted(ps, key=str.lower))})" for m, ps in sorted(glob.items(), key=lambda kv: (-len(kv[1]), kv[0]))), str(sum(len(v) for v in glob.values()))])
    covered = {x for m, _ in multi for x in m.split(' · ')}
    sg_rows = []
    for m in signed:
        if m in covered: continue
        ps = d['signed_m'].get(m, []); sg_rows.append([f"{m} (signed)", ', '.join(ps) if ps else 'Contracted partners', str(len(ps)) if ps else ''])
    if len(rows) + len(sg_rows) > max_rows and len(sg_rows) > 1:   # fold the signed items into one row when the slide is over its cap
        sg_rows = [["Signed with partners, not yet integrated", '; '.join(f"{r[0][:-9]} ({r[1]})" for r in sg_rows), str(len(sg_rows))]]
    return rows + sg_rows
ROWS = json.load(open(os.path.join(H, '..', 'sheet', 'rows_final.json')))[1:]
def israel_slide():
    il = [r for r in ROWS if r[0] == 'Israel']
    P = lambda st: [r[3] for r in il if r[2] == 'Provider' and r[5] == st]
    M = lambda st: [r[3] for r in il if r[2] != 'Provider' and r[5] == st]
    live = P('Live') + P('Live (cross-border)'); act = P('Activation on request'); hom = P('Homologating'); req = P('On request') + M('On request'); meth = M('Live')
    secs = [{"header": f"Live through Yuno: Nuvei acquires locally, the others process Israeli cards cross-border ({len(live)})", "chips": [chip(x) for x in live]},
            {"header": f"Wallets and payment methods live ({len(meth)})", "chips": [chip(x) for x in sorted(meth, key=lambda x: (x not in WALLETS, x.lower()))]},
            {"header": f"Integrated with Yuno, activation on request ({len(act)})", "chips": [chip(x) for x in act], "style": "signed"},
            {"header": f"Homologating ({len(hom)})", "chips": [chip(x) for x in hom], "muted": True},
            {"header": f"New connections on request, built by Yuno ({len(req)})", "chips": [chip(x) for x in req], "style": "request"}]
    tbl = {"columns": ["Tier", "What it means for adidas"], "col_widths": [0.26, 0.74], "font_size": 7.5, "rows": [
        ["Activation on request", "Already integrated with Yuno and covering Israel; switched on for adidas without a build. Rapyd holds an Israeli payment licence since July 2025."],
        ["New connection on request", "Not connected yet; Yuno scopes and builds it on request: PayPlus, Isracard, Cal, Max, the local gateways and Bit."]]}
    return {"id": "c-israel", "type": "logo_grid", "kicker": "COUNTRY DETAIL › ISRAEL", "sections": secs, "table": tbl,
            "headline": f"Israel: {len(live)} providers process Israeli cards through Yuno today, {len(act)} more can be activated, and the local acquirers are new connections on request.",
            "notes": "Evidence: Yuno integration matrix (Israeli card traffic through Adyen, Airwallex, Braintree, Stripe, Worldpay), partners database (Israel in the coverage of Airwallex, Braintree, Stripe, Worldline, Worldpay), Nutrameg live on Adyen and PayPal since Aug 2026, Israeli payment licences for Rapyd and Airwallex (Calcalist, Jul 2025). Finaro/Credorax was checked internally in Sep 2026 and is not connected. German's stated build time to Marko: 1 to 2 days plus 2 days of production testing; keep it verbal."}
for c in T:
    if c == 'Israel': S.append(israel_slide()); continue
    d = D[c]; live = sorted(d['live'], key=str.lower); hom = sorted(d['homolog'], key=str.lower)
    cards = d['methods'].get('Cards', []); direct = sorted(d['direct'], key=lambda x: (x not in WALLETS, x.lower())); signed = sorted(d['signed'])
    nloc = len(grouped(d)) + len(signed)
    headA = f"{c}: {pl(len(live), 'provider')} live through Yuno, {len(cards)} for cards" + (f", {pl(len(hom), 'more provider')} in homologation." if hom else ".")
    secA = [{"header": f"Live through Yuno ({len(live)})", "chips": [chip(x) for x in live]}]
    if hom: secA.append({"header": f"Homologating ({len(hom)})", "chips": [chip(x) for x in hom], "muted": True})
    secB = [{"header": f"Wallets and payment methods available ({len(direct)})", "chips": [chip(x) for x in direct]}]
    if signed: secB.append({"header": f"Signed with partners, not yet integrated ({len(signed)})", "chips": [chip(x) for x in signed], "style": "signed"})
    tbl = {"columns": ["Local method", "Providers carrying it through Yuno", "#"], "col_widths": [0.22, 0.72, 0.06], "font_size": 7.5}
    small = len(live) + len(hom) <= 16 and len(direct) <= 10
    if small:
        rows = method_table(d, 4)
        s = {"id": "c-" + slug(c), "type": "logo_grid", "kicker": "COUNTRY DETAIL › " + c.upper(), "headline": headA, "sections": secA + secB}
        if rows: s["table"] = dict(tbl, rows=rows)
        S.append(s)
    else:
        S.append({"id": "c-" + slug(c), "type": "logo_grid", "kicker": "COUNTRY DETAIL › " + c.upper() + " › PROVIDERS", "headline": headA, "sections": secA})
        headB = f"{c}: {pl(len(direct), 'payment method')} available and {pl(nloc, 'local method')} carried by the providers." if nloc else f"{c}: {pl(len(direct), 'payment method')} available through Yuno."
        s = {"id": "c-" + slug(c) + "-methods", "type": "logo_grid", "kicker": "COUNTRY DETAIL › " + c.upper() + " › PAYMENT METHODS", "headline": headB, "sections": secB}
        if len(direct) > 24:   # dense markets (Mexico): the table gets its own slide
            S.append(s)
            rows = method_table(d, 9)
            if rows: S.append({"id": "c-" + slug(c) + "-local", "type": "table", "kicker": "COUNTRY DETAIL › " + c.upper() + " › LOCAL METHODS",
                               "headline": f"{c}: local methods through Yuno, and which providers carry each one.", **tbl, "rows": rows, "header_style": "dark", "bold_first_col": True, "zebra": True})
        else:
            rows = method_table(d, 6 if len(direct) <= 14 else 5)
            if rows: s["table"] = dict(tbl, rows=rows)
            S.append(s)
signed_all = sorted({(c, m) for c in T for m in D[c]['signed']})
S.append({"id": "next-wave", "type": "two_column", "kicker": "WHAT COMES NEXT",
  "headline": "Israel is a build-on-request market; nine local methods are signed with partners and 41 providers are in homologation.",
  "cols": [{"header": "PAYPLUS AND SIGNED METHODS", "items": [
      {"title": "Israel", "body": "Six providers process Israeli cards today; Rapyd and Worldline can be activated; PayPlus and the local card companies and gateways are new connections Yuno builds on request."},
      {"title": "Signed, not yet integrated", "body": '; '.join(f"{c}: {m}" for c, m in signed_all)}]},
    {"header": "HOMOLOGATING PROVIDERS", "items": [
      {"title": "What it means", "body": "Listed on y.uno/integrations with a partnership in place; the Yuno integration is not live yet. Methods are confirmed on activation."},
      {"title": "Where", "body": ', '.join(f"{c} ({len(D[c]['homolog'])})" for c in T if D[c]['homolog'])}]}],
  "bar": "In every country you asked about, cards already have several live providers; the items above add local depth, they do not fill a gap in card coverage."})
S.append(old['slides'][-1])
for _s in S: _s.pop('source', None)
json.dump({"presentation_id": old['presentation_id'], "merchant": "adidas", "footer": "", "slides": S}, open(os.path.join(H, '..', 'gs', 'deck_spec_v4.json'), 'w'), indent=1, ensure_ascii=False)
print(len(S), 'slides;', sum(1 for s in S if s['type'] == 'logo_grid'), 'logo slides;', sum(len(ch) for s in S if s['type'] == 'logo_grid' for sec in s['sections'] for ch in [sec['chips']]), 'chips;',
      sum(1 for s in S if s['type'] == 'logo_grid' for sec in s['sections'] for ch in sec['chips'] if ch['logo']), 'with logo')
