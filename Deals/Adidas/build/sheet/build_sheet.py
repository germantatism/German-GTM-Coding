"""adidas · Yuno connections by country. Master source: y.uno/en/integrations (directory export, 14 Oct 2026).
Enrichment: Yuno integration matrix (Payments Concierge CSV) for which provider carries which method.
Exclusions: exclusions.json {key: {country: reason}} for directory entries contradicted by an official source.

python3 build_sheet.py <integrations_full.json> <connections_csv> <exclusions.json|-> [--write <spreadsheetId>]
"""
import json, csv, sys, re, os, collections
HERE = os.path.dirname(os.path.abspath(__file__))
DIRJ, CSVP, EXCL = sys.argv[1], sys.argv[2], sys.argv[3]
WRITE = sys.argv[sys.argv.index('--write') + 1] if '--write' in sys.argv else None

LATAM = ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Mexico', 'Peru', 'Uruguay', 'Bolivia', 'Costa Rica', 'Dominican Republic',
         'Ecuador', 'El Salvador', 'Guatemala', 'Honduras', 'Nicaragua', 'Panama', 'Paraguay']
SEA = ['Indonesia', 'Malaysia', 'Philippines', 'Singapore', 'Thailand', 'Vietnam', 'Myanmar']
ME = ['Israel']
T = LATAM + SEA + ME
REGION = {**{c: 'LATAM' for c in LATAM}, **{c: 'Southeast Asia' for c in SEA}, **{c: 'Middle East' for c in ME}}
NORM_C = {'Brasil': 'Brazil', 'Republica Dominicana': 'Dominican Republic', 'Netherlands 64bff': 'Netherlands', 'China C4bc9': 'China', 'Czechia': 'Czech Republic'}
def norm_key(s): return re.sub(r'[^a-z0-9]', '', (s or '').lower())

# ---- directory
D = json.load(open(DIRJ))
for d in D: d['countries'] = [NORM_C.get(c, c) for c in (d['countries'] or [])]
_cs = [d for d in D if norm_key(d['name']) in ('cybersource', 'cybersourcegtw')]
if len(_cs) == 2:
    keep, dup = sorted(_cs, key=lambda d: 0 if d['description'] else 1)
    keep['name'] = 'Cybersource'; keep['countries'] = sorted(set(keep['countries']) | set(dup['countries'])); keep['features'] = sorted(set(keep['features']) | set(dup['features']))
    D.remove(dup)
_ul = [d for d in D if norm_key(d['name']) in ('unlimit', 'unlimint')]
if len(_ul) == 2:
    keep = next(d for d in _ul if norm_key(d['name']) == 'unlimit'); dup = next(d for d in _ul if d is not keep)
    keep['countries'] = sorted(set(keep['countries']) | set(dup['countries'])); D.remove(dup)
PTYPE = {'clearsale': 'Fraud prevention', 'kount': 'Fraud prevention', 'striperadar': 'Fraud prevention', 'netcetera': '3DS authentication', 'cybersource3ds': '3DS authentication',
         'terrapay': 'Payouts and remittances', 'uniteller': 'Payouts and remittances', 'vtex': 'Commerce platform', 'skrill': 'Digital wallet', 'neteller': 'Digital wallet'}
def ptype(d):
    k = norm_key(d['name']); desc = (d['description'] or '').lower()
    if k in PTYPE: return PTYPE[k]
    if 'fraud' in desc and 'gateway' not in desc and 'payment' not in desc[:40]: return 'Fraud prevention'
    if 'remittance' in desc: return 'Payouts and remittances'
    return 'Payment processing'
excl = json.load(open(EXCL)) if EXCL != '-' else {}
def excluded(name, c): return excl.get(norm_key(name), {}).get(c)

prov_by_c = collections.defaultdict(list); meth_by_c = collections.defaultdict(list)
for d in D:
    for c in d['countries']:
        if c not in T or excluded(d['name'], c): continue
        if d['category'] == 'Provider' and ptype(d) != 'Payment processing': continue   # processors and payment methods only
        (prov_by_c if d['category'] == 'Provider' else meth_by_c)[c].append(d)

# ---- matrix enrichment (reuse the native-method map from the csv shaping script)
shape_src = open(os.path.join(HERE, '..', 'csv', 'shape.py')).read().split('rows = list')[0]
g = {}; sys_argv = sys.argv; sys.argv = ['x', CSVP, '/dev/null']; exec(shape_src, g); sys.argv = sys_argv
NATIVE, nm, WALLET_PROV = g['NATIVE'], g['nm'], g['WALLET_PROV']
CODE_ALIAS = {'2c2p': '2c2p', 'checkoutcom': 'checkout', 'cybersource': 'cybersourcegtw', 'mercadopago': 'mercadopago', 'qnb': 'qnbmpgs', 'redeban': 'redebandirect',
              'klap': 'klap', 'transbank': 'transbank', 'prosa': 'prosaiso', 'emerchantpay': 'emerchantpay', 'payretailers': 'payretailers', 'placetopay': 'placetopay',
              'machpay': 'bcimach', 'deuna': 'deuna', 'allinpay': 'allinpay', 'dlocal': 'dlocal', 'firstatlanticcommerce': 'fac', 'baccredomatic': 'baccredomatic', 'unlimit': 'unlimint', 'antomalipay': 'antom', 'pagsmile': 'pagsmile', 'paynet': 'paynet', 'evopayments': 'evo', 'bbvabancomer': 'bbva', 'webpay': 'transbank'}
M = list(csv.DictReader(open(CSVP)))
matrix = collections.defaultdict(lambda: collections.defaultdict(set))   # country -> provider_code -> labels
for r in M:
    c, p = r['Country'], r['Provider']
    if c not in T or p in WALLET_PROV: continue
    for m in r['Payment Methods (via Yuno)'].split('; '):
        if m == 'CARD': matrix[c][p].add('Cards')
        elif m in NATIVE and c in NATIVE[m][1]: matrix[c][p].add(NATIVE[m][0])
        elif m.startswith('PAYPAL'): matrix[c][p].add('PayPal')
        elif m.startswith('ASTROPAY'): matrix[c][p].add('AstroPay')
        elif m == 'SAFETYPAY' and c != 'Israel': matrix[c][p].add('SafetyPay')
        elif m == 'DOLARAPP' and c in ('Argentina', 'Brazil', 'Colombia', 'Mexico'): matrix[c][p].add('DolarApp')
        elif m == 'PAYVALIDA' and c in ('Colombia', 'Peru'): matrix[c][p].add('Payvalida')
        elif m == 'MULTIPAGO' and c == 'Bolivia': matrix[c][p].add('Multipago')
        elif m in ('BANK_TRANSFER', 'CASH') and c in LATAM and p in ('BAMBOO', 'DLOCAL', 'UNLIMINT', 'MONNET', 'PAYMENTEZ', 'EBANX', 'FINTOC'): matrix[c][p].add('Bank transfer' if m == 'BANK_TRANSFER' else 'Cash')
        elif m == 'PAGA_TODO' and c == 'Dominican Republic': matrix[c][p].add('Pagatodo')
        elif m in g['DR_BANKS'] and c == 'Dominican Republic': matrix[c][p].add('Local bank transfers and cash')
def code_for(name):
    k = norm_key(name); k = CODE_ALIAS.get(k, k)
    return k
matrix_norm = {c: {norm_key(p): v for p, v in pv.items()} for c, pv in matrix.items()}
def methods_via_yuno(c, name):
    v = matrix_norm.get(c, {}).get(code_for(name)); return ', '.join(sorted(v, key=lambda x: (x != 'Cards', x))) if v else ''
METHOD_ALIAS = {'thaiqr': 'thaiqrpromptpay', 'ovowallet': 'ovo', 'bancopopulardominicana': 'bancopopular', '7eleven': '7eleven', 'pagoalpaso': 'pagoalpaso',
                'rapipago': 'rapipago', 'nupay': 'nupay', 'codi': 'codi', 'oxxopay': 'oxxopay', 'mach': 'mach', 'deuna': 'deuna', 'clicktopay': 'clicktopay'}
def providers_for_method(c, name):
    k = METHOD_ALIAS.get(norm_key(name), norm_key(name)); out = []
    for p, labels in matrix.get(c, {}).items():
        if any(norm_key(l) == k for l in labels): out.append(disp(nm(p)))
    return ', '.join(sorted(set(out), key=str.lower))

# ---- 2C2P: live (German, 14 Oct 2026); it is in the directory for the 7 SEA markets, make sure the matrix enrichment shows cards
for c in SEA:
    if any(d['name'].lower() == '2c2p' for d in prov_by_c[c]): matrix[c].setdefault('2C2P', set()).add('Cards'); matrix_norm[c]['2c2p'] = matrix[c]['2C2P']

DISPLAY = {'Dlocal': 'dLocal', 'Astropay': 'AstroPay', 'Ebanx': 'EBANX', 'Fac': 'FAC (First Atlantic Commerce)', 'Ppro': 'PPRO', 'Paypal': 'PayPal', 'Pag Smile': 'Pagsmile',
           'MercadoPago': 'Mercado Pago', '2c2p': '2C2P', 'Safetypay': 'SafetyPay', 'PlaceToPay': 'PlacetoPay', 'Antom/Alipay': 'Antom', 'More Payments/uniteller': 'More Payments',
           'ELAVON': 'Elavon', 'PAYNET': 'Paynet', 'Btg Pactual': 'BTG Pactual', 'Banbajio': 'BanBajío', 'Bci Mach': 'BCI MACH', 'Evo Payments': 'EVO Payments', 'Pagarme': 'Pagar.me',
           'Openpay': 'Openpay', 'Stripe': 'Stripe', 'Xendit': 'Xendit', 'Nuvei': 'Nuvei', 'Kushki': 'Kushki', 'ALFAMART': 'Alfamart', 'BOOST': 'Boost', 'THAI QR': 'Thai QR (PromptPay)',
           'TRUEMONEY': 'TrueMoney', 'BIG C': 'Big C', 'SHOPEEPAY': 'ShopeePay', '7ELEVEN': '7-Eleven', 'OVO WALLET': 'OVO', 'CODI': 'CoDi', 'PAGO AL PASO': 'Pago al Paso',
           'PUNTO PAGO': 'Punto Pago', 'YAPE': 'Yape', 'PIX': 'PIX', 'Nupay': 'NuPay', 'RapiPago': 'Rapipago', 'Pago Facil': 'Pago Fácil', 'SAMSclub': "Sam's Club", 'Mach': 'MACH',
           'SPEI': 'SPEI', 'QRIS': 'QRIS', 'FPX': 'FPX', 'Click-to-Pay': 'Click to Pay', 'De Una': 'Deuna', 'PuntosHey': 'Puntos Hey', 'T1Pagos': 'T1 Pagos'}
def disp(name): return DISPLAY.get(name, name)
# ---- single tab: one row per country x entry (providers first, then payment methods)
rows = [['Country', 'Region', 'Type', 'Name', 'Payment methods processed through Yuno to date', 'Providers carrying it through Yuno', 'Status on Yuno', 'Website']]
for c in T:
    for d in sorted(prov_by_c[c], key=lambda d: d['name'].lower()):
        rows.append([c, REGION[c], 'Provider', disp(d['name']), methods_via_yuno(c, d['name']), '', 'Live', d['website'] or ''])
    for d in sorted(meth_by_c[c], key=lambda d: d['name'].lower()):
        rows.append([c, REGION[c], 'Payment method', disp(d['name']), '', providers_for_method(c, d['name']), 'Live', d['website'] or ''])
TABS = [('Connections by country', rows)]
cnt = collections.Counter((r[0], r[2]) for r in rows[1:])
for c in T: print(f"{c:20s} providers={cnt[(c, 'Provider')]:3d} methods={cnt[(c, 'Payment method')]:3d}")
print(len(rows) - 1, 'rows')
json.dump(rows, open(os.path.join(HERE, 'rows.json'), 'w'), ensure_ascii=False)
if not WRITE: sys.exit(0)

# ---- write + house format (header navy #10284A Roboto 10 white, thin borders, freeze B2, no gridlines)
from google.oauth2 import service_account
from googleapiclient.discovery import build
cr = service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'), scopes=['https://www.googleapis.com/auth/spreadsheets'])
api = build('sheets', 'v4', credentials=cr, cache_discovery=False).spreadsheets()
meta = api.get(spreadsheetId=WRITE, fields='sheets.properties').execute()
existing = {s['properties']['title']: s['properties']['sheetId'] for s in meta['sheets']}
reqs = []
for i, (t, v) in enumerate(TABS):
    if t not in existing: reqs.append({'addSheet': {'properties': {'title': t, 'index': i, 'gridProperties': {'rowCount': len(v) + 5, 'columnCount': len(v[0])}}}})
if reqs:
    res = api.batchUpdate(spreadsheetId=WRITE, body={'requests': reqs}).execute()
    for r in res['replies']:
        if 'addSheet' in r: existing[r['addSheet']['properties']['title']] = r['addSheet']['properties']['sheetId']
for t0, sid0 in list(existing.items()):
    if t0 not in dict(TABS): api.batchUpdate(spreadsheetId=WRITE, body={'requests': [{'deleteSheet': {'sheetId': sid0}}]}).execute(); existing.pop(t0)
api.values().batchClear(spreadsheetId=WRITE, body={'ranges': [f"'{t}'" for t, _ in TABS]}).execute()
api.values().batchUpdate(spreadsheetId=WRITE, body={'valueInputOption': 'RAW', 'data': [{'range': f"'{t}'!A1", 'values': v} for t, v in TABS]}).execute()
NAVY = {'red': 0x10 / 255, 'green': 0x28 / 255, 'blue': 0x4A / 255}; WHITE = {'red': 1, 'green': 1, 'blue': 1}
thin = {'style': 'SOLID', 'width': 1, 'color': {'red': 0.8, 'green': 0.8, 'blue': 0.8}}
WIDTHS = {'Connections by country': [150, 110, 120, 200, 320, 320, 110, 220], 'Summary': [150, 110, 90, 120, 520, 520], 'Named providers': [130, 120, 100, 420, 320, 380], 'Providers by country': [140, 110, 170, 220, 260, 160, 220, 220],
          'Payment methods by country': [140, 110, 190, 300, 420, 220], 'Integrations directory': [190, 120, 160, 420, 220, 420, 220, 220],
          'Internal review (delete before sharing)': [190, 140, 420, 320]}
fmt = []
for t, v in TABS:
    sid = existing[t]; ncol = len(v[0]); nrow = len(v)
    rng = {'sheetId': sid, 'startRowIndex': 0, 'endRowIndex': nrow, 'startColumnIndex': 0, 'endColumnIndex': ncol}
    fmt += [
        {'repeatCell': {'range': rng, 'cell': {'userEnteredFormat': {'textFormat': {'fontFamily': 'Roboto', 'fontSize': 10}, 'verticalAlignment': 'TOP', 'wrapStrategy': 'WRAP'}}, 'fields': 'userEnteredFormat(textFormat,verticalAlignment,wrapStrategy)'}},
        {'repeatCell': {'range': {**rng, 'endRowIndex': 1}, 'cell': {'userEnteredFormat': {'backgroundColor': NAVY, 'textFormat': {'fontFamily': 'Roboto', 'fontSize': 10, 'bold': True, 'foregroundColor': WHITE}, 'verticalAlignment': 'MIDDLE', 'wrapStrategy': 'WRAP'}}, 'fields': 'userEnteredFormat(backgroundColor,textFormat,verticalAlignment,wrapStrategy)'}},
        {'updateBorders': {'range': rng, 'top': thin, 'bottom': thin, 'left': thin, 'right': thin, 'innerHorizontal': thin, 'innerVertical': thin}},
        {'updateSheetProperties': {'properties': {'sheetId': sid, 'gridProperties': {'frozenRowCount': 1, 'frozenColumnCount': 1, 'hideGridlines': True}}, 'fields': 'gridProperties(frozenRowCount,frozenColumnCount,hideGridlines)'}},
    ]
    for ci, w in enumerate(WIDTHS.get(t, [])[:ncol]):
        fmt.append({'updateDimensionProperties': {'range': {'sheetId': sid, 'dimension': 'COLUMNS', 'startIndex': ci, 'endIndex': ci + 1}, 'properties': {'pixelSize': w}, 'fields': 'pixelSize'}})
api.batchUpdate(spreadsheetId=WRITE, body={'requests': fmt}).execute()
print('written + formatted:', WRITE)
