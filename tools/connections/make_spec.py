"""make_spec.py <config.json> : build/data/rows.json -> build/gs/deck_spec.json (adidas v4 format: logo chips per country).
Fit is rehearsed offline with the deal's gs_engine (DryDeck): a country gets one combined slide when it fits, otherwise two."""
import json, os, sys, re, collections
ROOT = '/Users/germantatis/Desktop/GTMCoding'
CFG = json.load(open(sys.argv[1])); DEAL = os.path.join(ROOT, CFG['deal_dir']); GS = os.path.join(DEAL, 'build', 'gs')
sys.path.insert(0, GS); import gs_engine as GE
sys.path.insert(0, os.path.join(ROOT, 'tools', 'connections')); import lib
LOG = os.environ.get('LOGO_DIR') or os.path.join(ROOT, 'tools', 'connections', 'logos')
usable = json.load(open(os.path.join(LOG, 'usable.json'))); aspect = json.load(open(os.path.join(LOG, 'aspect.json')))
SLIDES_BAD = json.load(open(os.path.join(LOG, 'slides_bad.json'))) if os.path.exists(os.path.join(LOG, 'slides_bad.json')) else {}   # urls Google's image fetcher rejects (preflight_slides.py)
DIRW = {lib.nk(d['name']): (d.get('website') or '') for d in lib.load_directory()}
REC = CFG.get('recurring_only', False)
R = json.load(open(os.path.join(DEAL, 'build', 'data', 'rows.json')))
T = [c for rg in CFG['regions'] for c in rg['countries']]
def nk(s): return lib.nk(s)
def dcountry(c): return lib.DISPLAY_COUNTRY.get(c, c)
def chip(name, key=None):
    k = key or nk(name)
    if k in usable and usable[k] not in SLIDES_BAD: return {'name': name, 'logo': usable[k], 'aspect': aspect.get(k, 1.0)}
    w = DIRW.get(k, ''); dom = re.sub(r'^https?://(www\.)?', '', w).split('/')[0] or lib.CODE_ONLY_DOMAIN.get(k, '')
    url = f'https://www.google.com/s2/favicons?domain={dom}&sz=128' if dom else ''
    return {'name': name, 'logo': '' if url in SLIDES_BAD else url, 'aspect': 1.0}
WALLETS = {'Apple Pay', 'Google Pay', 'PayPal'}
GLOBAL = WALLETS | {'Alipay', 'WeChat Pay', 'UnionPay', 'Neteller', 'Skrill', 'Samsung Pay', 'AstroPay'}
by = {c: {'live': [], 'homolog': [], 'code': [], 'code_m': {}, 'signed': [], 'direct': [], 'xborder': [], 'activate': [], 'request': [], 'methods': collections.defaultdict(list), 'global_m': collections.defaultdict(list), 'key': {}, 'nodata': []} for c in T}
for c, typ, name, meths, status, key in R:
    d = by[c]; d['key'][name] = key
    if status == 'On request': d['request'].append(name); continue
    if typ == 'Provider':
        if status == 'Homologating': d['homolog'].append(name); continue
        if status == 'Integrated (code)': d['code'].append(name); d['code_m'][name] = meths; continue
        if status == 'Activation on request': d['activate'].append(name); continue
        if status == 'Live (cross-border)': d['xborder'].append(name)
        d['live'].append(name)
        if not meths: d['nodata'].append(name)
        for m in meths:
            if m in GLOBAL: d['global_m'][m].append(name)
            else: d['methods'][m].append(name)
    else: (d['signed'] if status == 'Signed' else d['direct']).append(name)
def slug(c): return c.lower().replace(' ', '-')
def pl(n, w): return f"{n} {w}" + ('' if n == 1 else 's')
def grouped(d):
    g = collections.defaultdict(list)
    for m, ps in d['methods'].items():
        if m != 'Cards': g[tuple(sorted(ps, key=str.lower))].append(m)
    return sorted(((' · '.join(sorted(ms)), list(ps)) for ps, ms in g.items()), key=lambda kv: (-len(kv[1]), kv[0]))
def method_table(d, max_rows):
    gr = grouped(d); multi = [(m, p) for m, p in gr if len(p) > 1]; single = [(m, p) for m, p in gr if len(p) == 1]
    while len(multi) + (1 if single else 0) + (1 if d['global_m'] else 0) > max_rows and multi: single.append(multi.pop())
    rows = [[m, ', '.join(p), str(len(p))] for m, p in multi]
    if single: rows.append(["Other local methods" if not REC else "Other recurring methods", '; '.join(f"{m} ({', '.join(p)})" for m, p in sorted(single)), "1 to 2 each"])
    if d['global_m']:
        rows.append(["Wallets and global methods via providers", '; '.join(f"{m} ({', '.join(sorted(ps, key=str.lower))})" for m, ps in sorted(d['global_m'].items(), key=lambda kv: (-len(kv[1]), kv[0]))), str(sum(len(v) for v in d['global_m'].values()))])
    cm = {p: ms for p, ms in d['code_m'].items() if ms}
    if cm:
        rows.append(["Via providers integrated in code, not yet listed", '; '.join(f"{p}: {', '.join(ms)}" for p, ms in sorted(cm.items())), str(len(cm))])
    return rows
def short_methods(d, k=6):
    ms = [m for m, _ in sorted(d['methods'].items(), key=lambda kv: -len(kv[1])) if m != 'Cards']
    glob = [m for m in ('Apple Pay', 'Google Pay', 'PayPal') if m in d['global_m'] or m in d['direct']]
    allm = ms + [g for g in glob if g not in ms]
    if not allm: return 'Cards'
    return ' · '.join(allm[:k]) + (f' · +{len(allm) - k} more' if len(allm) > k else '')
def fits(s):
    deck = GE.DryDeck()
    try: GE.RENDERERS[s['type']](deck, s, 'c01', 1, ''); return True
    except GE.FitError: return False
S = []
cv = CFG['cover']; S.append({"id": "cover", "type": "cover", "title": cv['title'], "subtitle": cv['subtitle'], "presenter": cv['presenter'], "logo_url": CFG['logo_url']})
SRC_NOTE = ("Sources: y.uno/integrations directory (export of 14 Oct 2026), docs.y.uno Payment Type list and API enums (22 Oct 2026), Yuno integration code scan and repo inventory (Caio Freitas, payment-method-coverage-gaps, 14 Oct 2026, re-read 22 Oct); "
            "Payments Concierge integration matrix for the Latin American markets; Apple Pay availability per Apple (22 Oct 2026). "
            "Live = the connection is built and available to process through Yuno for this country; method activation is set per merchant.")
# ---- markets slide (Waymo) ----
if CFG.get('markets'):
    rows = []
    for c, region, status in CFG['markets']:
        d = by[c]; rows.append([c, region, status, str(len(d['live'])), short_methods(d, 5)])
    S.append({"id": "markets", "type": "table", "kicker": "WAYMO'S ANNOUNCED MARKETS OUTSIDE THE US", "headline": CFG['markets_headline'],
              "columns": ["Market", "Region", "What Waymo has announced", "Providers live", "Local methods and wallets through Yuno"], "col_widths": [0.12, 0.1, 0.42, 0.08, 0.28],
              "rows": rows, "header_style": "dark", "font_size": 7.5, "bold_first_col": True, "zebra": True, "note": CFG['markets_note'], "notes": CFG.get('markets_sources', '') + ' ' + SRC_NOTE})
# ---- basis slide (HBO Max) ----
if CFG.get('basis'):
    S.append({"id": "basis", "type": "two_column", "kicker": "WHAT COUNTS AS RECURRING IN THIS DECK",
      "headline": "Only methods that Yuno can bill again without the subscriber present are shown; one-time methods are left out.",
      "cols": [{"header": "RECURRING THROUGH YUNO TODAY", "items": [
          {"title": "Subscriptions engine", "body": "Yuno bills on the schedule you set: cards, PayPal (billing agreement) and Pix Automático in Brazil, all on a vaulted token."},
          {"title": "Stored credentials", "body": "Cards plus Apple Pay and Google Pay tokens, with the network transaction id stored on the token so renewals can be routed or retried on any connected provider."},
          {"title": "Enrollable local methods", "body": "A vaulted token after a one-time consent: SEPA, Bacs, Autogiro, Betalingsservice, BECS and PAD direct debits, iDEAL, Bancontact, Klarna, Afterpay, TWINT, Revolut Pay, NuPay, Daviplata, Nequi, Mercado Pago Wallet, Yape, Smart PIX, AstroPay, GCash, DANA, GoPay, ShopeePay and Touch 'n Go."}]},
        {"header": "LEFT OUT ON PURPOSE", "items": [
          {"title": "One-time methods", "body": "Cash and vouchers, QR codes, one-shot bank transfers and wallets without an enrollment flow (BLIK, Swish, MobilePay, OXXO, one-time Pix and similar)."},
          {"title": "How to read the country slides", "body": "Live = built and available through Yuno for that country; every live card processor supports recurring card billing. Outlined chips = integration code exists but y.uno/integrations does not list the provider yet (integrated, not live). Local methods appear only where Yuno's catalog has an enrollment or recurring flow."}]}],
      "bar": "Basis: docs.y.uno subscriptions, stored credentials and enrollment pages, Yuno's catalog of enrollment types and integration repo inventory, read on 22 October 2026.", "notes": SRC_NOTE})
# ---- overview tables per region ----
def overview(rg):
    cs = rg['countries']; chunks = [cs[i:i + 10] for i in range(0, len(cs), 10)]
    for i, ch in enumerate(chunks):
        rows = [[dcountry(c), str(len(by[c]['live'])), f"{len(by[c]['homolog'])} · {len(by[c]['code'])}", short_methods(by[c])] for c in ch]
        s = {"id": f"sum-{slug(rg['name'])}-{i + 1}", "type": "table", "kicker": f"OVERVIEW › {rg['name'].upper()}" + (f" ({i + 1} OF {len(chunks)})" if len(chunks) > 1 else ""),
             "headline": rg['headline'], "columns": ["Country", "Providers live", "Homologating · in code", "Recurring methods and wallets through Yuno" if REC else "Local methods and wallets through Yuno"],
             "col_widths": [0.17, 0.11, 0.14, 0.58], "rows": rows, "header_style": "dark", "font_size": 8, "bold_first_col": True, "zebra": True, "note": (rg.get('note', '') + " In code = integration repo exists, not listed on y.uno/integrations yet.").strip(), "notes": SRC_NOTE}
        if not fits(s): s['font_size'] = 7.5
        if not fits(s): s['font_size'] = 7
        S.append(s)
for rg in CFG['regions']: overview(rg)
# ---- country slides ----
def country_slides(c):
    d = by[c]; live = sorted(d['live'], key=str.lower); hom = sorted(d['homolog'], key=str.lower)
    cards = d['methods'].get('Cards', []); direct = sorted(d['direct'], key=lambda x: (x not in WALLETS, x.lower()))
    gr = grouped(d); nloc = len(gr); cn = dcountry(c); code = sorted(d['code'], key=str.lower); signed = sorted(d['signed'], key=str.lower)
    if REC:
        headA = f"{cn}: {pl(len(live), 'provider')} live through Yuno, {len(cards)} for recurring card billing" + (f", {pl(len(hom), 'more')} in homologation." if hom else ".")
        headB = f"{cn}: {pl(len(direct), 'recurring-capable payment method')} available and {pl(nloc, 'recurring local method')} carried by the providers." if nloc else f"{cn}: {pl(len(direct), 'recurring-capable payment method')} available through Yuno."
        secB_h = f"Recurring-capable wallets and payment methods ({len(direct)})"; tcols = ["Recurring method", "Providers carrying it through Yuno", "#"]
    else:
        headA = f"{cn}: {pl(len(live), 'provider')} live through Yuno, {len(cards)} for cards" + (f", {pl(len(hom), 'more provider')} in homologation." if hom else ".")
        headB = f"{cn}: {pl(len(direct), 'payment method')} available and {pl(nloc, 'local method')} carried by the providers." if nloc else f"{cn}: {pl(len(direct), 'payment method')} available through Yuno."
        secB_h = f"Wallets and payment methods available ({len(direct)})"; tcols = ["Local method", "Providers carrying it through Yuno", "#"]
    if not live and not hom: headA = f"{cn}: no provider lists this market on y.uno/integrations yet; {pl(len(direct), 'global payment method')} available." + (f" {pl(len(code), 'provider')} integrated in code." if code else "")
    live_h = f"Live through Yuno ({len(live)})"
    if d['xborder']: live_h = f"Live through Yuno: {', '.join(x for x in live if x not in d['xborder'])} acquire locally, the others process {cn.replace('Israel', 'Israeli')} cards cross-border ({len(live)})"
    secA = [{"header": live_h, "chips": [chip(x, d['key'].get(x)) for x in sorted(live, key=lambda x: (x in d['xborder'], x.lower()))]}] if live else []
    if hom: secA.append({"header": f"Homologating ({len(hom)})", "chips": [chip(x, d['key'].get(x)) for x in hom], "muted": True})
    if d['activate']: secA.append({"header": f"Integrated with Yuno, activation on request ({len(d['activate'])})", "chips": [chip(x, d['key'].get(x)) for x in sorted(d['activate'])], "style": "signed"})
    if code: secA.append({"header": f"Integrated in Yuno's code, not yet listed on y.uno/integrations ({len(code)})", "chips": [chip(x, d['key'].get(x)) for x in code], "style": "signed"})
    secB = [{"header": secB_h, "chips": [chip(x, d['key'].get(x)) for x in direct]}] if direct else []
    if signed: secB.append({"header": f"Signed with partners, not yet integrated ({len(signed)})", "chips": [chip(x, d['key'].get(x)) for x in signed], "style": "request"})
    if d['request']: secB.append({"header": f"New connections on request, built by Yuno ({len(d['request'])})", "chips": [chip(x, d['key'].get(x)) for x in sorted(d['request'])], "style": "request"})
    tbl = {"columns": tcols, "col_widths": [0.24, 0.70, 0.06], "font_size": 7.5}
    kick = "COUNTRY DETAIL › " + cn.upper()
    # 1) one combined slide
    for maxrows in (6, 4, 3, 2):
        rows = method_table(d, maxrows)
        s = {"id": "c-" + slug(c), "type": "logo_grid", "kicker": kick, "headline": headA, "sections": secA + secB}
        if rows: s["table"] = dict(tbl, rows=rows)
        if fits(s): return [s]
    # 2) providers slide + methods slide (table on the methods slide, shrinking)
    out = [{"id": "c-" + slug(c), "type": "logo_grid", "kicker": kick + " › PROVIDERS", "headline": headA, "sections": secA}]
    if not fits(out[0]): raise SystemExit(f"{c}: provider chips do not fit on one slide")
    for maxrows in (9, 7, 5, 4, 3):
        rows = method_table(d, maxrows)
        s = {"id": "c-" + slug(c) + "-methods", "type": "logo_grid", "kicker": kick + " › PAYMENT METHODS", "headline": headB, "sections": secB}
        if rows: s["table"] = dict(tbl, rows=rows)
        if fits(s): return out + [s]
    # 3) methods slide + separate table slide
    s = {"id": "c-" + slug(c) + "-methods", "type": "logo_grid", "kicker": kick + " › PAYMENT METHODS", "headline": headB, "sections": secB}
    out.append(s)
    for maxrows in (10, 8, 6):
        t = {"id": "c-" + slug(c) + "-local", "type": "table", "kicker": kick + " › LOCAL METHODS", "headline": f"{cn}: local methods through Yuno, and which providers carry each one.", **tbl, "rows": method_table(d, maxrows), "header_style": "dark", "bold_first_col": True, "zebra": True}
        if fits(t): return out + [t]
    raise SystemExit(f"{c}: table does not fit")
for rg in CFG['regions']:
    for c in rg['countries']: S.extend(country_slides(c))
nx = CFG['next']
S.append({"id": "next", "type": "next_steps", "kicker": "NEXT STEP", "headline": nx['headline'], "cards": nx['cards'], "contact": "german.tatis@y.uno"})
spec = {"presentation_id": CFG['presentation_id'], "merchant": CFG['merchant'], "footer": "", "logo_url": CFG['logo_url'], "logo_aspect": CFG['logo_aspect'], "slides": S}
json.dump(spec, open(os.path.join(GS, 'deck_spec.json'), 'w'), indent=1, ensure_ascii=False)
nchips = sum(len(sec['chips']) for s in S if s['type'] == 'logo_grid' for sec in s['sections']); nlogo = sum(1 for s in S if s['type'] == 'logo_grid' for sec in s['sections'] for ch in sec['chips'] if ch['logo'])
print(f"{CFG['merchant']}: {len(S)} slides; {sum(1 for s in S if s['type']=='logo_grid')} logo slides; {nchips} chips, {nlogo} with a logo; combined-country slides: {sum(1 for s in S if s['type']=='logo_grid' and '›' not in s['kicker'][16:])}")
