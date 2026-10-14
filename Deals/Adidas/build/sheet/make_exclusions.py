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
        src = r.get('evidence_url') or (r.get('evidence') or {}).get('all') or ''
        for c in r.get('drop', []):
            for k in keys: add(k, c, f"Not a supported market per the provider's own coverage list | {src}")
# wallets: official availability lists checked 14 Oct 2026
for c in ['Bolivia', 'Nicaragua', 'Indonesia', 'Thailand', 'Myanmar']: add('applepay', c, 'Not on Apple Pay official availability list | https://support.apple.com/en-us/102775')
add('googlepay', 'Indonesia', 'Not on Google Pay official online-payments country list | https://support.google.com/googlepay/answer/12429287')
add('paypal', 'Myanmar', 'Not on PayPal country list | https://developer.paypal.com/api/codes/country-region/')
json.dump(ex, open(OUT, 'w'), indent=1)
print(len(ex), 'entries,', sum(len(v) for v in ex.values()), 'country exclusions')
for k, v in sorted(ex.items()): print(' ', k, sorted(v))
