"""adidas · market research (processors + payment methods per country) crossed with Yuno coverage.
Inputs: market/*.json (research rows), prior gaps sheet export (optional), rows.json (connections sheet), Payments Concierge matrix CSV,
integrations directory. Output: gaps.json (one row per country x name) + a console summary.
python3 merge.py <market_dir> <prior_gaps.json|-> <integrations_full.json> <out gaps.json> [customer_sheet_export.json]
"""
import json, glob, csv, re, os, sys, collections
MD, PRIOR, DIRJ, OUT = sys.argv[1:5]
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
ROWS = sys.argv[5] if len(sys.argv) > 5 else os.path.join(HERE, 'customer_sheet_2026-10-14.json'); CSVP = os.path.join(REPO, 'Deals', 'Adidas', 'adidas_payment_connections_live.csv')
ORDER = ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Mexico', 'Peru', 'Uruguay', 'Bolivia', 'Costa Rica', 'Dominican Republic', 'Ecuador', 'El Salvador', 'Guatemala',
         'Honduras', 'Nicaragua', 'Panama', 'Paraguay', 'Indonesia', 'Malaysia', 'Philippines', 'Singapore', 'Thailand', 'Vietnam', 'Myanmar', 'Israel']
LATAM = ORDER[:17]; REGION = {**{c: 'LATAM' for c in LATAM}, **{c: 'Southeast Asia' for c in ORDER[17:24]}, 'Israel': 'Middle East'}
def nk(s): return re.sub(r'[^a-z0-9]', '', (s or '').lower())
def base(name): return re.sub(r'\s*\(.*?\)\s*', ' ', name).strip()
def cands(name, paren=False):
    out = []
    for part in re.split(r'\s*/\s*|\s+or\s+', base(name)): 
        if part.strip(): out.append(part.strip())
    out.append(base(name)); out.append(name)
    inside = re.findall(r'\((.*?)\)', name) if paren else []
    out += [i.strip() for i in inside if i and len(i.split()) <= 2 and not re.search(r'\b(formerly|incl|local|wallet|bank|cards?|online|cash|network|debit|acquiring|BNPL|regional|scheme|interoperable|ex|mobile|QR|transfer|voucher)\b', i, re.I)]
    seen = set(); res = []
    for x in out:
        k = nk(x)
        if k and k not in seen: seen.add(k); res.append(x)
    return res

# ---- Yuno: connections sheet (directory-backed, live per country)
rows = json.load(open(ROWS))
live = collections.defaultdict(lambda: {'Provider': {}, 'Payment method': {}})
for r in rows[1:]: live[r[0]][r[2]][nk(r[3])] = r
ROW_ALIAS = {'unlimint': 'unlimit', 'pagbank': 'pagbank', 'paycash': 'paycash', 'epayco': 'epayco', 'openpay': 'openpay', 'mercadopagowallet': 'mercadopago', 'transbank': 'webpay', 'webpaytransbank': 'webpay', 'rede': 'rede', 'pagbank': 'pagbank', 'placetopayevertec': 'placetopay',
             'facfirstatlanticcommerce': 'fac', 'firstatlanticcommerce': 'fac', 'cal': 'cal', 'machpay': 'mach', 'bcimach': 'mach', 'xendit': 'xendit', 'maya': 'maya', 'mayabusiness': 'maya',
             'nuvei': 'nuvei', 'dlocal': 'dlocal', 'ebanx': 'ebanx', 'payu': 'payu', 'adyen': 'adyen', 'stripe': 'stripe', 'checkoutcom': 'checkoutcom', 'checkout': 'checkoutcom',
             'antom': 'antom', 'antomalipay': 'antom', 'alipayplus': 'antom', 'midtrans': 'midtrans', 'doku': 'doku', '2c2p': '2c2p', 'kushki': 'kushki', 'getnet': 'getnet',
             'cielo': 'cielo', 'stone': 'stone', 'pagseguro': 'pagseguro', 'pagarme': 'pagarme', 'baccredomatic': 'baccredomatic', 'azul': 'azul', 'cardnet': 'cardnet',
             'bancard': 'bancard', 'datafast': 'datafast', 'medianet': 'medianet', 'niubiz': 'niubiz', 'izipay': 'izipay', 'wompi': 'wompi', 'epayco': 'epayco', 'redeban': 'redeban',
             'credibanco': 'credibanco', 'fiserv': 'fiserv', 'posnet': 'fiserv', 'fiservposnet': 'fiserv', 'openpay': 'openpay', 'openpaybbva': 'openpay', 'bbvabancomer': 'bbva',
             'globalpayments': 'globalpayments', 'evopayments': 'evopayments', 'evo': 'evopayments', 'prosa': 'prosa', 'paycash': 'paycash', 'oxxo': 'oxxopay',
             'rapipago': 'rapipago', 'pagofacil': 'pagofacil', 'pix': 'pix', 'khipu': 'khipu', 'yape': 'yape', 'yapebcp': 'yape', 'nequi': 'nequi', 'daviplata': 'daviplata',
             'efecty': 'efecty', 'sencillito': 'sencillito', 'mach': 'mach', 'deuna': 'deuna', 'yappy': 'yappy', 'puntopago': 'puntopago', 'puntoxpress': 'puntoxpress',
             'qris': 'qris', 'ovo': 'ovo', 'dana': 'dana', 'shopeepay': 'shopeepay', 'alfamart': 'alfamart', 'fpx': 'fpx', 'boost': 'boost', 'grabpay': 'grabpay', 'gcash': 'gcash',
             '7eleven': '7eleven', 'promptpay': 'thaiqrpromptpay', 'thaiqr': 'thaiqrpromptpay', 'thaiqrpromptpay': 'thaiqrpromptpay', 'truemoney': 'truemoney', 'bigc': 'bigc',
             'applepay': 'applepay', 'googlepay': 'googlepay', 'paypal': 'paypal', 'klarna': 'klarna', 'addi': 'addi', 'aplazo': 'aplazo', 'kueski': 'kueski', 'kueskipay': 'kueski',
             'acuotaz': 'acuotaz', 'cuotealo': 'cuotealobcp', 'cuotealobcp': 'cuotealobcp', 'nupay': 'nupay', 'picpay': 'picpay', 'boleto': 'boleto', 'spei': 'spei', 'codi': 'codi',
             'pagoalpaso': 'pagoalpaso', 'pagosnet': 'pagosnet', 'bancopopular': 'bancopopulardominicana', 'banconacional': 'banconacionaldecostarica', 'tigomoney': 'tigomoney',
             'clicktopay': 'clicktopay', 'unionpay': 'unionpay', 'wechatpay': 'wechatpay', 'samsungpay': 'samsungpay', 'walmart': 'walmart', 'transfiya': 'transfiya',
             'mercadopago': 'mercadopago', 'mercadopagocheckoutpro': 'mercadopago', 'cards': None, 'card': None, 'creditanddebitcards': None, 'cardswithinstallments': None}
def direct_hit(c, name):
    for x in cands(name):
        k = ROW_ALIAS.get(nk(x), nk(x))
        if k is None: continue
        for t in ('Provider', 'Payment method'):
            if k in live[c][t]: return t, live[c][t][k]
    return None
# ---- Yuno: integrations directory (any country)
D = json.load(open(DIRJ)); dirn = {}
for d in D: dirn.setdefault(nk(d['name']), d)
DIR_ALIAS = {'mercadopago': 'mercadopago', 'checkoutcom': 'checkoutcom', 'antom': 'antomalipay', 'fac': 'fac', 'mach': 'mach', 'oxxopay': 'oxxopay', 'thaiqrpromptpay': 'thaiqr',
             'ovo': 'ovowallet', 'payway': None, 'prisma': None, 'clip': None, 'oca': None, 'visanet': None, 'culqi': None, 'bit': None, 'max': None, 'cal': None, 'bancopopulardominicana': 'bancopopulardominicana', 'banconacionaldecostarica': 'banconacionaldecostarica', 'touchngo': None}
def dir_hit(name):
    for x in cands(name):
        k = ROW_ALIAS.get(nk(x), nk(x)); k = DIR_ALIAS.get(k, k)
        if k and k in dirn: return dirn[k]
    return None
# ---- Yuno: Payments Concierge matrix (production-proven methods per provider per payment country)
src = open(os.path.join(HERE, '..', 'csv', 'shape.py')).read().split('rows = list')[0]
g = {}; _a = sys.argv; sys.argv = ['x', CSVP, '/dev/null']; exec(src, g); sys.argv = _a
NATIVE, nm = g['NATIVE'], g['nm']
via = collections.defaultdict(lambda: collections.defaultdict(set))
for r in csv.DictReader(open(CSVP)):
    for m in r['Payment Methods (via Yuno)'].split('; '):
        if m: via[r['Country']][m].add(r['Provider'])
GLOBAL = {'APPLE_PAY', 'GOOGLE_PAY', 'PAYPAL', 'KLARNA', 'AFTERPAY', 'ZIP', 'ALIPAY', 'WECHAT_PAY', 'WECHAT', 'CRYPTO', 'ASTROPAY', 'NETELLER', 'SAFETYPAY', 'CARD'}
LATAM_ONLY_PROV = {'BAMBOO', 'DLOCAL', 'UNLIMINT', 'MONNET', 'PAYMENTEZ', 'EBANX', 'FINTOC', 'PAYRETAILERS', 'PAGSMILE', 'LOCAL_PAYMENT', 'KUSHKI', 'PAYU', 'NUVEI', 'RAPYD'}
CODE_ALIAS = {'pix': ['PIX', 'SMART_PIX'], 'pixautomatico': ['PIX_AUTOMATIC'], 'pixparcelado': ['PIX_PARCELADO'], 'boleto': ['BOLETO'], 'pse': ['PSE'], 'pseachcolombia': ['PSE'],
              'nequi': ['NEQUI', 'NEQUI_QR'], 'daviplata': ['DAVIPLATA'], 'efecty': ['EFECTY'], 'breb': ['BREB', 'BREB_LLAVES'], 'yape': ['YAPE', 'YAPE_ENROLLABLE', 'YAPE_ONESHOT'],
              'pagoefectivo': ['PAGO_EFECTIVO'], 'spei': ['SPEI'], 'codi': ['CODI'], 'oxxo': ['OXXO', 'OXXO_PAY'], 'oxxopay': ['OXXO', 'OXXO_PAY'], 'mercadopago': ['MERCADO_PAGO_WALLET', 'MERCADO_PAGO_CHECKOUT_PRO'],
              'mercadopagowallet': ['MERCADO_PAGO_WALLET', 'MERCADO_PAGO_CHECKOUT_PRO'], 'webpay': ['WEBPAY'], 'khipu': ['KHIPU'], 'mach': ['MACH_PAY', 'BCI_MACH_QR'], 'servipag': ['SERVIPAG'],
              'rapipago': ['RAPI_PAGO'], 'pagofacil': ['PAGO_FACIL'], 'modo': ['MODO'], 'transferencias30': ['TRANSFERENCIA_30'], 'qris': ['QRIS'], 'ovo': ['OVO_WALLET'], 'dana': ['DANA'],
              'shopeepay': ['SHOPEEPAY'], 'alfamart': ['ALFAMART'], 'indomaret': ['INDOMARET'], 'virtualaccount': ['VIRTUAL_ACCOUNT_IDN'], 'virtualaccounts': ['VIRTUAL_ACCOUNT_IDN'],
              'banktransfervirtualaccount': ['VIRTUAL_ACCOUNT_IDN'], 'fpx': ['FPX'], 'touchngo': ['TOUCH_AND_GO'], 'touchngoewallet': ['TOUCH_AND_GO'], 'tngewallet': ['TOUCH_AND_GO'],
              'boost': ['BOOST'], 'grabpay': ['GRABPAY'], 'gcash': ['GCASH'], 'maya': ['MAYA_WALLET'], '7eleven': ['7ELEVEN'], 'paynow': ['PAYNOW'], 'promptpay': ['THAI_QR'], 'thaiqr': ['THAI_QR'],
              'thaiqrpromptpay': ['THAI_QR'], 'truemoney': ['TRUEMONEY'], 'bigc': ['BIG_C'], 'yappy': ['YAPPY'], 'puntopago': ['PUNTO_PAGO'], 'puntoxpress': ['PUNTO_XPRESS'], 'deuna': ['DE_UNA'],
              'pagoalpaso': ['PAGO_AL_PASO'], 'pagosnet': ['PAGOSNET'], 'multipago': ['MULTIPAGO'], 'picpay': ['PICPAY'], 'nupay': ['NU_PAY'], 'addi': ['ADDI'], 'aplazo': ['APLAZO'],
              'acuotaz': ['ACUOTAZ'], 'cuotealo': ['CUOTEALO_BCP'], 'cuotealobcp': ['CUOTEALO_BCP'], 'paycash': ['PAYCASH'], 'paynet': ['PAYNET'], 'applepay': ['APPLE_PAY'], 'googlepay': ['GOOGLE_PAY'],
              'paypal': ['PAYPAL'], 'klarna': ['KLARNA'], 'bancolombia': ['BOTON_BANCOLOMBIA', 'BANCOLOMBIA_TRANSFER', 'BANCOLOMBIA_QR'], 'botonbancolombia': ['BOTON_BANCOLOMBIA'], 'bancolombiabutton': ['BOTON_BANCOLOMBIA'], 'botnbancolombia': ['BOTON_BANCOLOMBIA'],
              'banconacional': ['BANCO_NACIONAL_TRANSFER', 'BANCO_NACIONAL_CASH'], 'bancopopular': ['BANCO_POPULAR'], 'banreservas': ['BANRESERVAS'], 'pagatodo': ['PAGA_TODO'],
              'monnet': ['MONNET_QR', 'MONNET_WALLET'], 'powerpay': ['POWERPAY'], 'pluxee': ['PLUXEE_PA'], 'alipay': ['ALIPAY'], 'wechatpay': ['WECHAT_PAY', 'WECHAT'], 'cards': ['CARD'], 'card': ['CARD'],
              'creditanddebitcards': ['CARD'], 'cardswithinstallments': ['CARD'], 'cash': ['CASH'], 'cashvouchers': ['CASH'], 'banktransfer': ['BANK_TRANSFER', 'BANK_TRANSFER_AR'],
              'onlinebanktransfer': ['BANK_TRANSFER'], 'sepa': [], 'directdebit': ['DIRECT_DEBIT', 'DIRECT_DEBIT_ENROLLMENT'], 'tamara': ['TAMARA'], 'afterpay': ['AFTERPAY'], 'zip': ['ZIP']}
def via_hit(c, name):
    codes = set()
    for x in cands(name):
        k = nk(x)
        if k in CODE_ALIAS: codes |= set(CODE_ALIAS[k])
        for code, (label, homes) in NATIVE.items():
            if nk(label) == k and c in homes: codes.add(code)
    provs = set()
    for code in codes:
        if code in NATIVE and c not in NATIVE[code][1]: continue
        if code in ('CASH', 'BANK_TRANSFER', 'MULTIPAGO') and c not in LATAM: continue
        if code == 'MULTIPAGO' and c != 'Bolivia': continue
        if code in ('CASH', 'BANK_TRANSFER', 'BANK_TRANSFER_AR', 'CARD', 'DIRECT_DEBIT', 'DIRECT_DEBIT_ENROLLMENT'):
            livep = set(live[c]['Provider'].keys())
            provs |= {p for p in via[c].get(code, set()) if p in LATAM_ONLY_PROV and nk(pname(p)) in livep}
        else: provs |= via[c].get(code, set())
    return codes, provs
DISP = {'Unlimint': 'Unlimit', 'Paycash': 'PayCash', 'Epayco': 'ePayco', 'Openpay': 'Openpay', 'Dlocal': 'dLocal', 'Ebanx': 'EBANX', 'Payu': 'PayU', 'Mercado Pago': 'Mercado Pago', 'Pagseguro': 'PagSeguro', 'Pagbank': 'PagBank', 'Unlimint': 'Unlimit', 'Fac': 'FAC',
        'Cybersource Gtw': 'Cybersource', 'Checkout': 'Checkout.com', 'Bci Mach': 'BCI MACH', 'E Merchant Pay': 'emerchantpay', 'Pay Retailers': 'PayRetailers', 'Place To Pay': 'PlacetoPay',
        'Klap 2': 'Klap', 'Transbank 2': 'Transbank', 'Redeban Direct': 'Redeban', 'Qnb Mpgs': 'QNB MPGS', 'Evo': 'EVO Payments', 'Prosa Iso': 'Prosa', 'Bbva': 'BBVA', 'Btg': 'BTG Pactual',
        'Pagarme': 'Pagar.me', 'Paymentez': 'Paymentez (Kushki)', '2C2P': '2C2P', 'Ntt Data': 'NTT Data', 'Asiapay': 'AsiaPay', 'Astropay': 'AstroPay', 'Paypal': 'PayPal', 'Safetypay': 'SafetyPay'}
def pname(p): x = nm(p); return DISP.get(x, x)
def plist(ps): return ', '.join(sorted({pname(p) for p in ps}, key=str.lower))

RANK = {'Yes (connection built; not listed on y.uno/integrations)': 4, 'Yes': 4, 'Yes (via provider)': 3, 'Partial': 2, 'In catalog, other countries': 1, 'Not connected (possible via live provider)': 1, 'No': 0}
def status(c, name, kind, typical_access=''):
    """-> (on_yuno, entry)"""
    hit = direct_hit(c, name)
    codes, provs = via_hit(c, name)
    if codes == {'CARD'} or nk(base(name)) in ('cards', 'card', 'creditanddebitcards', 'cardswithinstallmentstashlumim', 'cardswithinstallments', 'internationalcards'):
        cp = sorted({r[3] for r in live[c]['Provider'].values()}, key=str.lower)
        return 'Yes', f"Cards through {len(cp)} live providers here: {', '.join(cp[:12])}{'…' if len(cp) > 12 else ''}"
    if hit:
        t, r = hit
        if t == 'Provider': return 'Yes', f"{r[3]} (Provider){'; methods processed: ' + r[4] if r[4] else ''}"
        carriers = r[5] or plist(provs)
        return 'Yes', f"{r[3]} (Payment method){'; via ' + carriers if carriers else ''}"
    if provs: return 'Yes (via provider)', f"Processed through {plist(provs)} (Payments Concierge matrix)"
    d = dir_hit(name)
    if d:
        cs = [x for x in d['countries'] if x != c][:8]
        return 'In catalog, other countries', f"{d['name']} ({d['category']}) listed for {', '.join(cs)}{'…' if len(d['countries']) > 8 else ''}"
    # aggregators named in research that are live Yuno providers in this country
    aggs = [a.strip() for a in re.split(r',|;|\bor\b|\band\b', typical_access.replace('via', ' ')) if a.strip() and nk(a) not in ('direct', '')]
    hits = []
    for a in aggs:
        h = direct_hit(c, a)
        if h and h[0] == 'Provider': hits.append(h[1][3])
    if hits: return 'Not connected (possible via live provider)', f"{', '.join(sorted(set(hits)))} is live on Yuno here and lists this method publicly; not verified in the Yuno matrix"
    return 'No', ''
def action(rel, on):
    if on == 'n/a': return 'Not applicable (merchant-side COD, not a payment connection)'
    if on.startswith('Yes (connection built'): return 'Covered (connection built; not on public directory)'
    if on == 'Yes': return 'Covered'
    if on == 'Yes (via provider)': return 'Covered via provider (confirm routing)'
    if on in ('Partial', 'In catalog, other countries', 'Not connected (possible via live provider)'): return 'Confirm with Integrations'
    return 'Gap: High' if rel == 'High' else 'Gap: Medium'
CAT_FROM_TYPE = lambda t: 'Acquirer / PSP' if t.startswith('Acq') else ''
def guess_cat(name, why):
    s = (name + ' ' + why).lower()
    for kw, cat in [('scheme', 'Local card scheme'), ('amex', 'Cards'), ('american express', 'Cards'), ('bnpl', 'BNPL / installments'), ('wallet', 'Wallet'), ('transfer', 'Instant / bank transfer'),
                    ('qr', 'Instant / bank transfer'), ('cash', 'Cash voucher'), ('voucher', 'Cash voucher'), ('app', 'Wallet')]:
        if kw in s: return cat
    return 'Other'

# ---- research rows
R = []
for f in sorted(glob.glob(os.path.join(MD, '*.json'))):
    for x in json.load(open(f)):
        x['_src'] = os.path.basename(f); R.append(x)
print(len(R), 'research rows from', len(glob.glob(os.path.join(MD, '*.json'))), 'files')
# ---- prior sheet rows
P = []
if PRIOR != '-':
    pv = json.load(open(PRIOR))
    for r in pv[1:]:
        r += [''] * (9 - len(r)); P.append(dict(zip(['country', 'region', 'type', 'name', 'why', 'on', 'entry', 'priority', 'source'], r)))
print(len(P), 'prior rows')

out = []; used_prior = set()
EQUIV = {'7elevenotccash': 'overthecountercash', 'fiuuformerlyrazermerchantservices': 'razermerchantservices', 'opnpaymentsformerlyomise': 'omise', 'kbankscbacquiring': 'kasikornbank', 'qrph': 'qrphinstapayonlinebanking', 'clavetelereddebitnetwork': 'tarjetaclave', 'qrpaymentssipaptransfers': 'spiinstanttransferssipap', 'localcardschemesisracardbrandedcards': 'localcardschemesisracardbrandedcards'}
def match_prior(c, name):
    """all prior rows for this country that name the same thing (first = best match)"""
    ks = {ROW_ALIAS.get(nk(x), nk(x)) for x in cands(name, True)} | {nk(x) for x in cands(name, True)}; ks -= {None, ''}
    tn = set(re.findall(r'[a-z0-9]+', base(name).lower())) - STOP; nb = nk(base(name))
    found = []
    for i, p in enumerate(P):
        if p['country'] != c or i in used_prior: continue
        pk = {ROW_ALIAS.get(nk(x), nk(x)) for x in cands(p['name'], True)} | {nk(x) for x in cands(p['name'], True)} | {EQUIV.get(nk(p['name']), '')}; pk -= {None, ''}
        tp = set(re.findall(r'[a-z0-9]+', base(p['name']).lower())) - STOP; pb = nk(base(p['name']))
        ok = bool(ks & pk) or (len(tn) >= 2 and len(tp) >= 2 and (tn <= tp or tp <= tn)) or (len(pb) >= 5 and pb in nk(name)) or (len(nb) >= 5 and nb in nk(p['name']))
        if ok: used_prior.add(i); found.append(p)
    found.sort(key=lambda p: -RANK.get(p['on'], 0))
    return found[0] if found else None
STOP = {'the', 'and', 'of', 'online', 'local', 'instant', 'transfers', 'transfer', 'wallet', 'cards', 'card', 'bank', 'banking', 'scheme', 'schemes', 'domestic', 'network', 'qr', 'cash', 'otc', 'payments', 'mobile'}
for x in R:
    c = x['country']; kind = 'Acquirer/PSP' if x['kind'] == 'Processor' else 'Payment method'
    on, entry = status(c, x['name'], kind, x.get('typical_access', ''))
    if 'cash on delivery' in x['name'].lower(): on, entry = 'n/a', 'Cash on delivery is collected by the carrier; not a Yuno connection'
    p = match_prior(c, x['name'])
    if p and on != 'n/a' and RANK.get(p['on'], 0) > RANK.get(on, 0):
        on, entry = p['on'], p['entry']
    rel = x.get('relevance', 'Medium')
    if p and p.get('priority') == 'High': rel = 'High'
    out.append({'country': c, 'region': REGION.get(c, ''), 'type': kind, 'category': x.get('category', ''), 'name': x['name'], 'why': x.get('why_it_matters', ''), 'relevance': rel,
                'on': on, 'entry': entry, 'action': action(rel, on), 'source': x.get('source_url', ''), 'origin': 'research 14-Oct (deep)' + (' + prior' if p else '')})
for i, p in enumerate(P):
    if i in used_prior: continue
    c = p['country']; on, entry = status(c, p['name'], p['type'])
    if 'cash on delivery' in p['name'].lower(): on, entry = 'n/a', 'Cash on delivery is collected by the carrier; not a Yuno connection'
    pon = p['on']
    if on != 'n/a' and RANK.get(pon, 0) > RANK.get(on, 0): on, entry = pon, p['entry']
    rel = p['priority'] or 'Medium'
    out.append({'country': c, 'region': REGION.get(c, ''), 'type': p['type'], 'category': CAT_FROM_TYPE(p['type']) or guess_cat(p['name'], p['why']), 'name': p['name'], 'why': p['why'],
                'relevance': rel, 'on': on, 'entry': entry, 'action': action(rel, on), 'source': p['source'], 'origin': 'prior pass 14-Oct'})
TYPE_ORD = {'Acquirer/PSP': 0, 'Payment method': 1}; REL_ORD = {'High': 0, 'Medium': 1}
out.sort(key=lambda r: (ORDER.index(r['country']) if r['country'] in ORDER else 99, TYPE_ORD.get(r['type'], 2), REL_ORD.get(r['relevance'], 2), r['name'].lower()))
json.dump(out, open(OUT, 'w'), ensure_ascii=False, indent=1)
cnt = collections.Counter((r['country'], r['action'].split(' (')[0]) for r in out)
print(f"{'country':20s} rows  covered  via  confirm  gapH  gapM")
for c in ORDER:
    n = sum(1 for r in out if r['country'] == c)
    print(f"{c:20s} {n:4d}  {cnt[(c,'Covered')]:7d}  {cnt[(c,'Covered via provider')]:3d}  {cnt[(c,'Confirm with Integrations')]:7d}  {cnt[(c,'Gap: High')]:4d}  {cnt[(c,'Gap: Medium')]:4d}")
print(len(out), 'rows total')
