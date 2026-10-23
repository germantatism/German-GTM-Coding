import os, sys
sys.argv=[sys.argv[0]]
src_code = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sync_intro.py')).read().split('# ------------------------------------------------ 1. story slide')[0]
src_code = src_code.replace("SRC = '1Qu3JvldczchxT9TrXmUkU1bSso9ltTGvOt5peT3hHjQ'; DST = '1r7g6kFtX8ZENovd3-51qyx9M0369yYLahpwXEGeEHRY'", "SRC = '1TyFXKt2OfoBLHGn8T1xX_Z1Uic_5ZYeeGUb8g_n0jrw'; DST = '1vULwizzS9eoNpyOYCOEfxGDkZegRp_9bmPgPhUAy2zo'")
exec(src_code)
def slide_with(needle):
    for s in D:
        for e in s['pageElements']:
            if e.get('table'):
                for r in e['table']['tableRows']:
                    for c in r['tableCells']:
                        t = ''.join(te.get('textRun', {}).get('content', '') for te in c.get('text', {}).get('textElements', []))
                        if needle in t: return s['objectId']
            elif needle in text_of(e): return s['objectId']
EDITS = [('PIX Automático · Smart PIX · Mercado Pago Wallet · Apple Pay · Google Pay · PayPal', 'PIX Automático · NuPay · Smart PIX · Mercado Pago Wallet · Apple Pay · Google Pay · PayPal'),
         ('Nequi · Mercado Pago Wallet · Bancolombia Tokenbox · Apple Pay · Google Pay · PayPal', 'Nequi · Daviplata · Mercado Pago Wallet · Bancolombia Tokenbox · Apple Pay · Google Pay · PayPal'),
         ('Netherlands: 6 recurring-capable payment methods available and 4 recurring local methods', 'Netherlands: 6 recurring-capable payment methods and 4 recurring local methods')]
reqs = []
for old, new in EDITS:
    sid_ = slide_with(old); print('  ', 'found' if sid_ else 'MISSING', old[:50], '->', sid_)
    if sid_: reqs.append({'replaceAllText': {'containsText': {'text': old, 'matchCase': True}, 'replaceText': new, 'pageObjectIds': [sid_]}})
run(reqs, 'hbo manual edits re-applied')
