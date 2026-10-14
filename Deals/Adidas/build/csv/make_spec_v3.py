"""Deck spec for the adidas Google Slides deck, built from the verified sheet rows (build/sheet/rows_final.json).
Country detail = method -> providers carrying it (from the provider rows' method lists), plus wallets, other direct methods, signed and homologating.
Usage: python3 make_spec_v3.py "Brazil,Colombia,Mexico,Peru"   (countries that get two slides)"""
import json, os, sys, collections, re
H = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(H, '..', 'sheet', 'rows_final.json')))[1:]
old = json.load(open(os.path.join(H, '..', 'gs', 'deck_spec.json')))
SPLIT = set(sys.argv[1].split(',')) if len(sys.argv) > 1 and sys.argv[1] else set()
LATAM1 = ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Mexico', 'Peru', 'Uruguay']
LATAM2 = ['Bolivia', 'Costa Rica', 'Dominican Republic', 'Ecuador', 'El Salvador', 'Guatemala', 'Honduras', 'Nicaragua', 'Panama', 'Paraguay']
SEA = ['Indonesia', 'Malaysia', 'Philippines', 'Singapore', 'Thailand', 'Vietnam', 'Myanmar']
T = LATAM1 + LATAM2 + SEA + ['Israel']
SRC = "y.uno/integrations, Yuno integration matrix and docs.y.uno payment type list, verified against each provider's own coverage, 14 Oct 2026"
WALLETS = {'Apple Pay', 'Google Pay', 'PayPal'}
GLOBAL = WALLETS | {'Alipay', 'WeChat Pay', 'UnionPay', 'Neteller', 'Skrill'}   # not local methods; shown under wallets / other methods
def slug(c): return c.lower().replace(' ', '-')
by = {c: {'live': [], 'homolog': [], 'signed': [], 'direct': [], 'methods': collections.defaultdict(list), 'signed_m': collections.defaultdict(list), 'global_m': collections.defaultdict(list)} for c in T}
for r in R:
    c, typ, name, meths, status = r[0], r[2], r[3], r[4], r[5]
    d = by[c]
    if typ == 'Provider':
        if status == 'Homologating': d['homolog'].append(name); continue
        d['live'].append(name)
        for m in [x for x in meths.split(', ') if x and x != 'Methods confirmed on activation']:
            if m.endswith(' (signed)'): d['signed_m'][m[:-9]].append(name)
            elif m in GLOBAL: d['global_m'][m].append(name)
            elif m not in ('Cards',): d['methods'][m].append(name)
            else: d['methods']['Cards'].append(name)
    else:
        (d['signed'] if status == 'Signed' else d['direct']).append(name)
def grouped(d):
    g = collections.defaultdict(list)
    for m, ps in d['methods'].items():
        if m == 'Cards': continue
        g[tuple(ps)].append(m)
    return sorted(((' · '.join(ms), list(ps)) for ps, ms in g.items()), key=lambda kv: (-len(kv[1]), kv[0]))
S = [old['slides'][0]]
def cc(lst): return f"{len(lst)}: " + ', '.join(lst)
def live_in(name): return [c for c in T if name in by[c]['live']]
mp, dl, pu, c2 = live_in('Mercado Pago'), live_in('dLocal'), live_in('PayU'), live_in('2C2P')
S.append({"id": "named", "type": "table", "kicker": "COVERAGE › THE PROVIDERS YOU NAMED",
  "headline": "Mercado Pago, dLocal, PayU and 2C2P are live through Yuno; PayPlus would be a new connection.",
  "columns": ["Provider", "Status", "Countries live (of the 25 you asked about)", "Payment methods through Yuno"], "col_widths": [0.13, 0.11, 0.42, 0.34],
  "rows": [["Mercado Pago", {"text": "Live", "bold": True}, cc(mp), "Cards, Checkout Pro, Mercado Pago Wallet, Mercado Pago QR, PIX, Boleto, PSE by market"],
           ["dLocal", {"text": "Live", "bold": True}, cc(dl), "Cards plus the local methods of each market: PIX, Boleto, SPEI, OXXO, PSE, Efecty, Yape, Clave, QRIS, FPX, Thai QR, TrueMoney and more"],
           ["PayU", {"text": "Live", "bold": True}, cc(pu), "Cards, PSE, OXXO and cash networks in Mexico"],
           ["2C2P", {"text": "Live", "bold": True}, cc(c2), "Cards"],
           ["PayPlus", {"text": "New connection", "bold": True}, "Not connected and no build in progress", "Scoped on request"]],
  "header_style": "dark", "font_size": 7.5, "bold_first_col": True, "zebra": True,
  "note": "Live means the connection is built and available to process payments through Yuno for this country. Method activation is set per merchant.", "source": SRC})
def short_methods(d, k=6):
    ms = [m for m, _ in sorted(d['methods'].items(), key=lambda kv: -len(kv[1])) if m != 'Cards']
    return ' · '.join(ms[:k]) + (f' · +{len(ms) - k} more' if len(ms) > k else '') if ms else 'Cards and wallets'
def overview(id_, kicker, headline, countries):
    rows = [[c, str(len(by[c]['live'])), str(len(by[c]['homolog'])), short_methods(by[c])] for c in countries]
    return {"id": id_, "type": "table", "kicker": kicker, "headline": headline, "columns": ["Country", "Providers live", "Homologating", "Local methods through Yuno"],
            "col_widths": [0.17, 0.12, 0.13, 0.58], "rows": rows, "header_style": "dark", "font_size": 8, "bold_first_col": True, "zebra": True, "source": SRC}
S.append(overview("sum-latam1", "OVERVIEW › LATAM CORE MARKETS", "Every core LATAM market has dozens of live providers and its main local methods through Yuno.", LATAM1))
S.append(overview("sum-latam2", "OVERVIEW › LATAM REST OF REGION", "The rest of LATAM is covered with redundancy in every country and local methods where they matter.", LATAM2))
S.append(overview("sum-apac", "OVERVIEW › SOUTHEAST ASIA AND ISRAEL", "Southeast Asia runs on global acquirers plus local wallets and QR; Israel runs on Nuvei today.", SEA + ['Israel']))
base = {"type": "table", "columns": ["Method", "Providers through Yuno", "#"], "col_widths": [0.2, 0.74, 0.06], "header_style": "dark", "font_size": 7.5, "bold_first_col": True, "zebra": True, "source": SRC}
for c in T:
    d = by[c]; gr = grouped(d)
    cards = sorted(d['methods'].get('Cards', []), key=str.lower)
    wallets = sorted(x for x in d['direct'] if x in WALLETS); other = sorted(x for x in d['direct'] if x not in WALLETS)
    head_rows = [["Cards", ', '.join(cards), str(len(cards))]]
    if wallets: head_rows.append(["Wallets", ', '.join(wallets), str(len(wallets))])
    if other: head_rows.append(["Other payment methods", ', '.join(other), str(len(other))])
    if d['homolog']: head_rows.append(["Homologating providers", ', '.join(sorted(d['homolog'], key=str.lower)), str(len(d['homolog'])) ])
    MAXROWS = 10
    multi = [(m, p) for m, p in gr if len(p) > 1]; single = [(m, p) for m, p in gr if len(p) == 1]
    n_signed = len(set(list(d['signed_m']) + d['signed']))
    while len(multi) + (1 if single else 0) + n_signed > MAXROWS and multi:   # collapse the thinnest rows until the local slide fits
        m, p = multi.pop(); single.append((m, p))
    loc = [[m, ', '.join(p), str(len(p))] for m, p in multi]
    if single: loc.append(["Other local methods", '; '.join(f"{m} ({', '.join(p)})" for m, p in sorted(single)), "1 to 2 each"])
    for m in sorted(set(list(d['signed_m']) + d['signed'])):
        ps = d['signed_m'].get(m, [])
        loc.append([f"{m} (signed)", ', '.join(ps) if ps else 'Contracted partners', str(len(ps)) if ps else ''])
    nloc = len([m for m, _ in gr]) + len(d['signed'])
    pl = lambda n, w: f"{n} {w}" + ("" if n == 1 else "s")
    head = f"{c}: {pl(len(d['live']), 'provider')} live through Yuno, {len(cards)} for cards and {pl(nloc, 'local method')}." if nloc else f"{c}: {pl(len(d['live']), 'provider')} live through Yuno, {len(cards)} for cards."
    if (c in SPLIT or len(head_rows) + len(loc) > MAXROWS) and loc:
        S.append(dict(base, id="c-" + slug(c), kicker="COUNTRY DETAIL › " + c.upper() + " › CARDS, WALLETS AND PROVIDERS", headline=head, rows=head_rows))
        S.append(dict(base, id="c-" + slug(c) + "-local", kicker="COUNTRY DETAIL › " + c.upper() + " › LOCAL METHODS", headline=f"{c}: local methods through Yuno, and which providers carry each one.", rows=loc))
    else:
        S.append(dict(base, id="c-" + slug(c), kicker="COUNTRY DETAIL › " + c.upper(), headline=head, rows=head_rows[:1] + loc + head_rows[1:]))
signed_all = sorted({(c, m) for c in T for m in by[c]['signed']})
S.append({"id": "next-wave", "type": "two_column", "kicker": "WHAT COMES NEXT",
  "headline": "PayPlus would be a new connection; nine local methods are signed with partners and 41 providers are in homologation.",
  "cols": [
    {"header": "PAYPLUS AND SIGNED METHODS", "items": [
      {"title": "PayPlus (Israel)", "body": "No connection built and none in progress. Built as a new connection on request; scope and timeline confirmed with Yuno's integrations team."},
      {"title": "Signed, not yet integrated", "body": '; '.join(f"{c}: {m}" for c, m in signed_all)}]},
    {"header": "HOMOLOGATING PROVIDERS", "items": [
      {"title": "What it means", "body": "Listed on y.uno/integrations with a partnership in place; the Yuno integration is not live yet. Methods are confirmed on activation."},
      {"title": "Where", "body": ', '.join(f"{c} ({len(by[c]['homolog'])})" for c in T if by[c]['homolog'])}]}],
  "bar": "In every country you asked about, cards already have several live providers; the items above add local depth, they do not fill a gap in card coverage.",
  "source": SRC})
S.append(old['slides'][-1])
for _s in S: _s.pop("source", None)   # German: no source lines on slides
json.dump({c: {k: (dict(v) if isinstance(v, collections.defaultdict) else v) for k, v in d.items()} for c, d in by.items()}, open(os.path.join(H, "deck_data.json"), "w"), indent=1, ensure_ascii=False)
json.dump({"presentation_id": old['presentation_id'], "merchant": "adidas", "footer": "", "slides": S}, open(os.path.join(H, '..', 'gs', 'deck_spec_v3.json'), 'w'), indent=1, ensure_ascii=False)
print(len(S), 'slides')
