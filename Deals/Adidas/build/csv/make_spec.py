"""Build gs/deck_spec.json for the adidas deck from build/csv/by_country.json (Payments Concierge CSV, 14 Oct 2026)."""
import json, collections, os
H = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(H, 'by_country.json')))
old = json.load(open(os.path.join(H, '..', 'gs', 'deck_spec.json')))
SRC = "Yuno integration matrix (product_matrix.matrix_v1) and Yuno integration code, via Payments Concierge, 14 Oct 2026"
LIVE = "Live means the provider has processed production payments through Yuno for this country, cross-border acquiring included. Method activation is set per merchant."
LATAM1 = ['Argentina','Brazil','Chile','Colombia','Mexico','Peru','Uruguay']
LATAM2 = ['Bolivia','Costa Rica','Dominican Republic','Ecuador','El Salvador','Guatemala','Honduras','Nicaragua','Panama','Paraguay']
SEA = ['Indonesia','Malaysia','Philippines','Singapore','Thailand','Vietnam','Myanmar']
ISR = ['Israel']
import sys
SPLIT = set(sys.argv[1].split(',')) if len(sys.argv) > 1 and sys.argv[1] else set()
def by_method(d):
    m = collections.defaultdict(list)
    for prov, meths in d['local'].items():
        for x in meths: m[x].append(prov)
    return sorted(m.items(), key=lambda kv: (-len(kv[1]), kv[0]))
def grouped(d):
    g = collections.defaultdict(list)
    for meth, provs in by_method(d): g[tuple(provs)].append(meth)
    return sorted(((' · '.join(ms), list(pv)) for pv, ms in g.items()), key=lambda kv: (-len(kv[1]), kv[0]))
def methods_short(d, k=6):
    ms = [x for x, _ in by_method(d)]
    return ' · '.join(ms[:k]) + (f' · +{len(ms) - k} more' if len(ms) > k else '') if ms else 'Cards and wallets only'
def slug(c): return c.lower().replace(' ', '-')
S = [old['slides'][0]]  # cover unchanged
named = {'Mercado Pago': [], 'dLocal': [], 'PayU': []}
for c, d in D.items():
    for p in named:
        if p in d['cards'] or p in d['local']: named[p].append(c)
def cc(lst): return f"{len(lst)}: " + ', '.join(lst)
S.append({"id": "named", "type": "table", "kicker": "COVERAGE › THE PROVIDERS YOU NAMED",
  "headline": "Mercado Pago, dLocal and PayU are live through Yuno; 2C2P is integrated but not yet in production, and PayPlus would be new.",
  "columns": ["Provider", "Status", "Countries live (of the 25 you asked about)", "Local methods through Yuno"], "col_widths": [0.13, 0.15, 0.4, 0.32],
  "rows": [
    ["Mercado Pago", {"text": "Live", "bold": True}, cc(named['Mercado Pago']), "Cards, Checkout Pro, Mercado Pago Wallet, PIX, Boleto, PSE"],
    ["dLocal", {"text": "Live", "bold": True}, cc(named['dLocal']), "Cards plus local methods in each market: PIX, Boleto, SPEI, OXXO, PSE, Efecty, Yape, QRIS, FPX, GCash, Thai QR, TrueMoney and more"],
    ["PayU", {"text": "Live", "bold": True}, cc(named['PayU']), "Cards, PSE"],
    ["2C2P", {"text": "Integrated, no production traffic yet", "bold": True}, "Card integration built; no live payments recorded", "Cards only. No local methods connected"],
    ["PayPlus", {"text": "New connection", "bold": True}, "Not connected and no build in progress", "Scoped on request"]],
  "header_style": "dark", "font_size": 7.5, "bold_first_col": True, "zebra": True,
  "note": LIVE, "source": SRC,
  "notes": "2C2P: the integration matrix shows card integration code only, with zero recorded production transactions in any country. Earlier we told adidas 2C2P is live with many SEA merchants; this corrects it."})
def summary(id_, kicker, headline, countries):
    rows = [[c, str(D[c]['n_providers']), methods_short(D[c])] for c in countries]
    return {"id": id_, "type": "table", "kicker": kicker, "headline": headline, "columns": ["Country", "Providers live", "Local methods available"],
            "col_widths": [0.18, 0.12, 0.7], "rows": rows, "header_style": "dark", "font_size": 8, "bold_first_col": True, "zebra": True, "note": LIVE, "source": SRC}
S.append(summary("sum-latam1", "OVERVIEW › LATAM CORE MARKETS", "Every core LATAM market has dozens of live providers and its main local methods through Yuno.", LATAM1))
S.append(summary("sum-latam2", "OVERVIEW › LATAM REST OF REGION", "The rest of LATAM is covered too, with redundancy in every country and local methods where they matter.", LATAM2))
S.append(summary("sum-apac", "OVERVIEW › SOUTHEAST ASIA AND ISRAEL", "Southeast Asia and Israel run on global acquirers and wallets, with local methods in five SEA markets.", SEA + ISR))
for c in LATAM1 + LATAM2 + SEA + ISR:
    d = D[c]; bm = by_method(d)
    card_rows = [["Cards", ', '.join(d['cards']), str(len(d['cards']))], ["Wallets", ', '.join(d['wallets']), str(len(d['wallets']))]]
    gr = grouped(d)
    if c in SPLIT and len(gr) > 10:
        multi = [(m, p) for m, p in gr if len(p) > 1]; single = [(m, p) for m, p in gr if len(p) == 1]
        loc_rows = [[m, ', '.join(p), str(len(p))] for m, p in multi]
        loc_rows.append(["Other local methods", '; '.join(f"{m} ({p[0]})" for m, p in single), "1 each"])
    else:
        loc_rows = [[m, ', '.join(p), str(len(p))] for m, p in gr]
    loc = f"{len(bm)} local methods" if bm else "no local method connected yet"
    head = f"{c}: {d['n_providers']} providers live through Yuno, {len(d['cards'])} for cards and {loc}."
    base = {"type": "table", "columns": ["Method", "Providers live through Yuno", "#"], "col_widths": [0.2, 0.74, 0.06],
            "header_style": "dark", "font_size": 7.5, "bold_first_col": True, "zebra": True, "note": LIVE, "source": SRC}
    if c in SPLIT:
        S.append(dict(base, id="c-" + slug(c), kicker="COUNTRY DETAIL › " + c.upper() + " › CARDS AND WALLETS", headline=head, rows=card_rows))
        S.append(dict(base, id="c-" + slug(c) + "-local", kicker="COUNTRY DETAIL › " + c.upper() + " › LOCAL METHODS",
                      headline=f"{c}: local methods live through Yuno, and which providers carry each one.", rows=loc_rows))
    else:
        S.append(dict(base, id="c-" + slug(c), kicker="COUNTRY DETAIL › " + c.upper(), headline=head, rows=card_rows[:1] + loc_rows + card_rows[1:]))
S.append({"id": "gaps", "type": "two_column", "kicker": "WHAT IS NOT LIVE YET",
  "headline": "2C2P and PayPlus are not processing through Yuno today, and five integrations are built but not yet live.",
  "cols": [
    {"header": "2C2P AND PAYPLUS", "items": [
      {"title": "2C2P", "body": "Card integration built, no production payments recorded in any country. No local methods (PromptPay, TrueMoney and others) connected. In SEA those run through dLocal, Xendit and others today."},
      {"title": "PayPlus (Israel)", "body": "No connection built and none in progress. Built as a new connection on request; scope and timeline confirmed with Yuno's integrations team."}]},
    {"header": "BUILT, NOT YET LIVE", "items": [
      {"title": "MPGS", "body": "Brazil and Ecuador, cards"},
      {"title": "Vindi", "body": "Brazil, cards"},
      {"title": "Yappy", "body": "Chile and Uruguay"}]}],
  "bar": "In every country you asked about, cards already have several live providers, so none of these gaps leaves a market without coverage.",
  "source": SRC,
  "notes": "Owner and usual timeline for new connection requests are not recorded in the data; ask the Partnerships/Integrations team before committing a PayPlus date."})
S.append(old['slides'][-1])
for _s in S: _s.pop("source", None)
spec = {"presentation_id": old['presentation_id'], "merchant": "adidas", "footer": "", "slides": S}
json.dump(spec, open(os.path.join(H, '..', 'gs', 'deck_spec_v2.json'), 'w'), indent=1, ensure_ascii=False)
print(len(S), 'slides')
