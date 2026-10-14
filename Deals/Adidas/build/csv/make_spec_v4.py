"""Google Slides spec with logo chips, from the verified sheet data (csv/deck_data.json, written by make_spec_v3.py).
Per country: slide A = providers (live + homologating) as logo chips; slide B = payment methods as logo chips + the
method -> providers table. Small countries get one combined slide. Logos: scratchpad logos/usable.json + aspect.json.
Usage: python3 make_spec_v4.py <scratchpad_logos_dir>"""
import json, os, sys, re, collections
H = os.path.dirname(os.path.abspath(__file__)); LOG = sys.argv[1]
D = json.load(open(os.path.join(H, 'deck_data.json')))
old = json.load(open(os.path.join(H, '..', 'gs', 'deck_spec.json')))
usable = json.load(open(os.path.join(LOG, 'usable.json'))); aspect = json.load(open(os.path.join(LOG, 'aspect.json')))
def nk(s): return re.sub(r'[^a-z0-9]', '', (s or '').lower())
ALIAS = {'facfirstatlanticcommerce': 'fac', 'antom': 'antomalipay', 'morepayments': 'morepaymentsuniteller', 'banbajo': 'banbajio', 'thaiqrpromptpay': 'thaiqr', 'ovo': 'ovowallet', 'pagofcil': 'pagofacil'}
def chip(name):
    k = nk(name); k = ALIAS.get(k, k) if ALIAS.get(k, k) in usable else k
    return {'name': name, 'logo': usable.get(k, ''), 'aspect': aspect.get(k, 1.0)}
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
           ["PayPlus", {"text": "New connection", "bold": True}, "Not connected and no build in progress", "Scoped on request"]],
  "header_style": "dark", "font_size": 7.5, "bold_first_col": True, "zebra": True,
  "note": "Live means the connection is built and available to process payments through Yuno for this country. Method activation is set per merchant."})
def short_methods(d, k=6):
    ms = [m for m, _ in sorted(d['methods'].items(), key=lambda kv: -len(kv[1])) if m != 'Cards']
    return ' · '.join(ms[:k]) + (f' · +{len(ms) - k} more' if len(ms) > k else '') if ms else 'Cards and wallets'
def overview(id_, kicker, headline, countries):
    rows = [[c, str(len(D[c]['live'])), str(len(D[c]['homolog'])), short_methods(D[c])] for c in countries]
    return {"id": id_, "type": "table", "kicker": kicker, "headline": headline, "columns": ["Country", "Providers live", "Homologating", "Local methods through Yuno"],
            "col_widths": [0.17, 0.12, 0.13, 0.58], "rows": rows, "header_style": "dark", "font_size": 8, "bold_first_col": True, "zebra": True}
S.append(overview("sum-latam1", "OVERVIEW › LATAM CORE MARKETS", "Every core LATAM market has dozens of live providers and its main local methods through Yuno.", LATAM1))
S.append(overview("sum-latam2", "OVERVIEW › LATAM REST OF REGION", "The rest of LATAM is covered with redundancy in every country and local methods where they matter.", LATAM2))
S.append(overview("sum-apac", "OVERVIEW › SOUTHEAST ASIA AND ISRAEL", "Southeast Asia runs on global acquirers plus local wallets and QR; Israel runs on Nuvei today.", SEA + ['Israel']))
def grouped(d):
    g = collections.defaultdict(list)
    for m, ps in d['methods'].items():
        if m != 'Cards': g[tuple(sorted(ps, key=str.lower))].append(m)
    return sorted(((' · '.join(ms), list(ps)) for ps, ms in g.items()), key=lambda kv: (-len(kv[1]), kv[0]))
def method_table(d, max_rows):
    gr = grouped(d); multi = [(m, p) for m, p in gr if len(p) > 1]; single = [(m, p) for m, p in gr if len(p) == 1]
    signed = sorted(set(list(d['signed_m']) + d['signed']))
    while len(multi) + (1 if single else 0) + len(signed) > max_rows and multi:
        single.append(multi.pop())
    rows = []
    for m, p in multi:
        sg = [d['signed_m'].get(x, []) for x in m.split(' · ')]; sg = sorted({y for z in sg for y in z})
        if sg: rows.append([m, f"{', '.join(p)} (integrated) · {', '.join(sg)} (signed)", str(len(p) + len(sg))])
        else: rows.append([m, ', '.join(p), str(len(p))])
    if single: rows.append(["Other local methods", '; '.join(f"{m} ({', '.join(p)})" for m, p in sorted(single)), "1 to 2 each"])
    covered = {x for m, _ in multi for x in m.split(' · ')}
    for m in signed:
        if m in covered: continue
        ps = d['signed_m'].get(m, []); rows.append([f"{m} (signed)", ', '.join(ps) if ps else 'Contracted partners', str(len(ps)) if ps else ''])
    return rows
for c in T:
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
            rows = method_table(d, 10)
            if rows: S.append({"id": "c-" + slug(c) + "-local", "type": "table", "kicker": "COUNTRY DETAIL › " + c.upper() + " › LOCAL METHODS",
                               "headline": f"{c}: local methods through Yuno, and which providers carry each one.", **tbl, "rows": rows, "header_style": "dark", "bold_first_col": True, "zebra": True})
        else:
            rows = method_table(d, 7 if len(direct) <= 14 else 5)
            if rows: s["table"] = dict(tbl, rows=rows)
            S.append(s)
signed_all = sorted({(c, m) for c in T for m in D[c]['signed']})
S.append({"id": "next-wave", "type": "two_column", "kicker": "WHAT COMES NEXT",
  "headline": "PayPlus would be a new connection; nine local methods are signed with partners and 41 providers are in homologation.",
  "cols": [{"header": "PAYPLUS AND SIGNED METHODS", "items": [
      {"title": "PayPlus (Israel)", "body": "No connection built and none in progress. Built as a new connection on request; scope and timeline confirmed with Yuno's integrations team."},
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
