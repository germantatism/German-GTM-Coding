# -*- coding: utf-8 -*-
"""Third pass (German, 24-sep): the token vault is NOT part of what is included. Slide 16 only."""
import sys, os, json, urllib.request
sys.path.insert(0,'/Users/germantatis/Desktop/GTMCoding/Industry/AI/Higgsfield/build')
from engine import elements, text_of, replace_requests, run
from google.oauth2 import service_account
from googleapiclient.discovery import build
PID = '1VTuUxAAyVVrbEkpce2z2zih3YbfaEEsQ6eUSMZwubxk'
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
creds = service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'), scopes=['https://www.googleapis.com/auth/presentations'])
svc = build('slides', 'v1', credentials=creds, cache_discovery=False)
P = svc.presentations().get(presentationId=PID).execute()
idx = {el['objectId']: el for s in P['slides'] for el, tr in elements(s)}
FIX = {
 'g3fb7d86b358_4_658': 'Usuarios, roles y webhooks',            # "Qué cubre la tarifa": was "Bóveda de tokens PCI"
 'g3fb7d86b358_4_692': 'Monitores, reintentos y reportes',      # blue panel row: was "Monitores, reintentos y bóveda PCI"
}
for oid, new in FIX.items():
    print(oid, repr(text_of(idx[oid]).strip()), '->', repr(new))
reqs = []
for oid, new in FIX.items(): reqs += replace_requests(idx[oid], new)
run(svc, PID, reqs, label='vault out')
Q = svc.presentations().get(presentationId=PID).execute()
left = [(n, text_of(el).strip()[:80]) for n, s in enumerate(Q['slides'], 1) for el, tr in elements(s) if 'bóveda' in text_of(el).lower() or 'vault' in text_of(el).lower()]
print('remaining mentions of bóveda/vault:', left)
r = svc.presentations().pages().getThumbnail(presentationId=PID, pageObjectId=Q['slides'][15]['objectId'], thumbnailProperties_thumbnailSize='LARGE').execute()
urllib.request.urlretrieve(r['contentUrl'], f"{OUT}/fix3_16.png"); print('S16 re-rendered')
