"""exclusions.json for build_sheet.py: directory entries contradicted by an official source (research 14 Oct 2026)."""
import json, glob, re, sys, os
RD = sys.argv[1]; OUT = sys.argv[2]
def nk(s): return re.sub(r'[^a-z0-9]', '', s.lower())
# CSV provider code -> directory entry key(s)
CODE2DIR = {'CYBERSOURCE_GTW': ['cybersource'], 'MERCADO_PAGO': ['mercadopago'], 'CHECKOUT': ['checkoutcom', 'checkout'], 'QNB_MPGS': ['qnb'], 'REDEBAN_DIRECT': ['redeban'],
            'KLAP_2': ['klap'], 'TRANSBANK_2': ['transbank'], 'PROSA_ISO': ['prosa'], 'E_MERCHANT_PAY': ['emerchantpay'], 'PAY_RETAILERS': ['payretailers'], 'PLACE_TO_PAY': ['placetopay'],
            'BCI_MACH': ['machpay', 'bcimach'], 'DE_UNA': ['deuna'], 'ALL_IN_PAY': ['allinpay'], 'FAC': ['fac', 'firstatlanticcommerce'], 'BAC_CREDOMATIC': ['baccredomatic'], 'UNLIMINT': ['unlimit', 'unlimint'], 'DLOCAL': ['dlocal'], 'EBANX': ['ebanx'], 'NTT_DATA': ['nttdata', 'nttdatapaymentservices']}
ex = {}
def add(key, c, why): ex.setdefault(key, {})[c] = why
for f in sorted(glob.glob(os.path.join(RD, 'result_*.json'))):
    for r in json.load(open(f)):
        p = r['provider']; keys = CODE2DIR.get(p, [nk(p)])
        if os.path.basename(f) == 'result_E.json': keys = [nk(p)]
        src = r.get('evidence_url') or (r.get('evidence') or {}).get('all') or ''
        for c in r.get('drop', []):
            for k in keys: add(k, c, f"Not a supported market per the provider's own coverage list | {src}")
# result_F.json (truth-check on the sheet rows): display names, plus payment-method flags
fF = os.path.join(RD, 'result_F.json')
if os.path.exists(fF):
    F = json.load(open(fF))
    DISP2KEY = {'dlocal': 'dlocal', 'facfirstatlanticcommerce': 'fac', 'mercadopago': 'mercadopago', 'ppro': 'ppro', 'pagsmile': 'pagsmile', 'antom': 'antomalipay', 'morepayments': 'morepaymentsuniteller',
                'placetopay': 'placetopay', 'elavon': 'elavon', 'paynet': 'paynet', 'btgpactual': 'btgpactual', 'banbajo': 'banbajio', 'bcimach': 'bcimach', 'evopayments': 'evopayments', 'pagarme': 'pagarme', 'astropay': 'astropay', 'ebanx': 'ebanx', '2c2p': '2c2p', 'safetypay': 'safetypay'}
    for r in F.get('providers', []):
        k = nk(r['provider']); k = DISP2KEY.get(k, k)
        for c in r.get('drop', []): add(k, c, f"Not a supported market per the provider's own coverage list | {r.get('evidence_url', '')}")
    for m in F.get('method_flags', []):
        add(nk(m['method']), m['country'], f"{m.get('reason', 'Flagged in truth check')} | truth check 14 Oct 2026")
# not payment acceptance (research notes, batch E): Brinta is tax/e-invoicing; Nium coverage in these markets is payouts only; Pronto Paga Mexico is payouts only
for c in ['Brazil', 'Chile', 'Colombia', 'Uruguay']: add('brinta', c, 'Tax and e-invoicing provider, not a payment processor | https://brinta.com')
for c in ['Brazil', 'Malaysia']: add('nium', c, 'Payouts only in this market, no pay-in acquiring | https://www.nium.com')
add('prontopaga', 'Mexico', 'Payouts only in this market | https://prontopaga.com')
# wallets: official availability lists checked 14 Oct 2026
for c in ['Bolivia', 'Nicaragua', 'Indonesia', 'Thailand', 'Myanmar']: add('applepay', c, 'Not on Apple Pay official availability list | https://support.apple.com/en-us/102775')
add('googlepay', 'Indonesia', 'Not on Google Pay official online-payments country list | https://support.google.com/googlepay/answer/12429287')
add('paypal', 'Myanmar', 'Not on PayPal country list | https://developer.paypal.com/api/codes/country-region/')
json.dump(ex, open(OUT, 'w'), indent=1)
print(len(ex), 'entries,', sum(len(v) for v in ex.values()), 'country exclusions')
for k, v in sorted(ex.items()): print(' ', k, sorted(v))
