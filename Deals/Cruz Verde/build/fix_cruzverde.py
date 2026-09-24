# -*- coding: utf-8 -*-
"""Second pass on the Cruz Verde deck: restore the big-number + small-suffix style on the tranche prices (S16),
shorten the overlapping bullets on S11, one-line pillar header on S6, replace Payouts on S7, anchor S7 heading to top."""
import sys, os, json, urllib.request
sys.path.insert(0,'/Users/germantatis/Desktop/GTMCoding/Industry/AI/Higgsfield/build')
from engine import elements, text_of, replace_requests, run, TEXT_FIELDS
from google.oauth2 import service_account
from googleapiclient.discovery import build
PID = '1VTuUxAAyVVrbEkpce2z2zih3YbfaEEsQ6eUSMZwubxk'
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
creds = service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'), scopes=['https://www.googleapis.com/auth/presentations'])
svc = build('slides', 'v1', credentials=creds, cache_discovery=False)
P = svc.presentations().get(presentationId=PID).execute()
SRC = json.load(open(f'{OUT}/deck_before.json'))          # pristine Palco copy, for the original run styles
idx = {el['objectId']: el for s in P['slides'] for el, tr in elements(s)}
sidx = {el['objectId']: el for s in SRC['slides'] for el, tr in elements(s)}
def runs(el):
    return [(te['textRun']['content'], {k: v for k, v in te['textRun'].get('style', {}).items() if k in TEXT_FIELDS})
            for te in el['shape']['text'].get('textElements', []) if 'textRun' in te and te['textRun'].get('content', '').strip()]
reqs = []
# 1) S16 tranche prices: "$0.06" big + "/trx" small, styles copied from the original Palco runs
for oid in ('g3fb7d86b358_4_627', 'g3fb7d86b358_4_630', 'g3fb7d86b358_4_633'):
    rr = runs(sidx[oid]); txt = text_of(idx[oid]).rstrip('\n'); cut = txt.index('/')
    print(oid, 'text:', repr(txt), '| original runs:', [(c, s.get('fontSize')) for c, s in rr])
    reqs.append({'updateTextStyle': {'objectId': oid, 'textRange': {'type': 'FIXED_RANGE', 'startIndex': 0, 'endIndex': cut}, 'style': rr[0][1], 'fields': ','.join(rr[0][1].keys())}})
    reqs.append({'updateTextStyle': {'objectId': oid, 'textRange': {'type': 'FIXED_RANGE', 'startIndex': cut, 'endIndex': len(txt)}, 'style': rr[-1][1], 'fields': ','.join(rr[-1][1].keys())}})
# 2) text fixes
FIX = {
 'g3c99cf7678e_0_28735': 'Una integración para Mercado Pago y cada proveedor nuevo',
 'g3c99cf7678e_0_28726': 'Monitores con failover automático si un proveedor falla',
 'g3f8b4c413fe_1_2583': 'INSIGHTS Y DATOS',
 'g3f8b4c413fe_1_2624': 'Recupera rechazos técnicos en otra ruta.',
 'g3caca0138e4_0_2198': 'Reportes exportables',
 'g3caca0138e4_0_2199': 'para tener todas las transacciones en un solo archivo',
}
for oid, new in FIX.items(): reqs += replace_requests(idx[oid], new)
# 3) S7 heading box was two lines in the source; anchor to top so the one-line heading aligns with its siblings
reqs.append({'updateShapeProperties': {'objectId': 'g3caca0138e4_0_2204', 'shapeProperties': {'contentAlignment': 'TOP'}, 'fields': 'contentAlignment'}})
print('requests:', len(reqs))
run(svc, PID, reqs, label='cruz verde fixes')
Q = svc.presentations().get(presentationId=PID).execute(); json.dump(Q, open(f'{OUT}/deck_after_fix.json', 'w'))
for n in (6, 7, 11, 16):
    r = svc.presentations().pages().getThumbnail(presentationId=PID, pageObjectId=Q['slides'][n - 1]['objectId'], thumbnailProperties_thumbnailSize='LARGE').execute()
    urllib.request.urlretrieve(r['contentUrl'], f"{OUT}/fix_{n:02d}.png")
print('thumbs done')
