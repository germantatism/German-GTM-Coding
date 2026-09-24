# -*- coding: utf-8 -*-
"""Build 'Propuesta - Cruz Verde + Yuno' on the Drive copy of the Palco deck via the Slides API (service account).
Usage: python3 build_cruzverde.py dry   -> simulate, report missing IDs / untouched text / forbidden tokens
       python3 build_cruzverde.py       -> apply and download thumbnails of the changed slides"""
import sys, os, json, re, urllib.request
sys.path.insert(0,'/Users/germantatis/Desktop/GTMCoding/Industry/AI/Higgsfield/build')
from engine import elements, text_of, replace_requests, run, TEXT_FIELDS
from google.oauth2 import service_account
from googleapiclient.discovery import build
from content_cruzverde import T, DELETE, MOVE, RESTYLE_FROM, FORBID, LOGO, COVER_LOGO_OLD, COVER_LOGO_BOX
PID = '1VTuUxAAyVVrbEkpce2z2zih3YbfaEEsQ6eUSMZwubxk'
OUT = sys.argv[2] if len(sys.argv) > 2 else '.'
DRY = 'dry' in sys.argv
creds = service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'),
        scopes=['https://www.googleapis.com/auth/presentations'])
svc = build('slides', 'v1', credentials=creds, cache_discovery=False)
P = svc.presentations().get(presentationId=PID).execute()
json.dump(P, open(f'{OUT}/deck_before_build.json', 'w'))
idx = {}; slide_of = {}
for n, s in enumerate(P['slides'], 1):
    for el, tr in elements(s):
        idx[el['objectId']] = (el, tr); slide_of[el['objectId']] = n
missing = [k for k in T if k not in idx] + [k for k in list(MOVE) + list(RESTYLE_FROM) + list(RESTYLE_FROM.values()) + [COVER_LOGO_OLD] if k not in idx]
print("MISSING ids:", missing)
reqs = []; sim = {}
for oid, new in T.items():
    if oid in idx:
        reqs += replace_requests(idx[oid][0], new); sim[oid] = new
for oid in DELETE:
    if oid in idx: reqs.append({'deleteObject': {'objectId': oid}}); sim[oid] = ''
def box_req(oid, x, y, w, h):
    size = idx[oid][0]['size']
    sx = w * 12700 / size['width']['magnitude']; sy = h * 12700 / size['height']['magnitude']
    return {'updatePageElementTransform': {'objectId': oid, 'transform': {'scaleX': sx, 'scaleY': sy, 'shearX': 0, 'shearY': 0,
            'translateX': x * 12700, 'translateY': y * 12700, 'unit': 'EMU'}, 'applyMode': 'ABSOLUTE'}}
for oid, box in MOVE.items(): reqs.append(box_req(oid, *box))
def first_run_style(el):
    for te in el['shape']['text'].get('textElements', []):
        if 'textRun' in te and te['textRun'].get('content', '').strip():
            return {k: v for k, v in te['textRun'].get('style', {}).items() if k in TEXT_FIELDS}
    return {}
for oid, src in RESTYLE_FROM.items():
    st = first_run_style(idx[src][0])
    if st: reqs.append({'updateTextStyle': {'objectId': oid, 'textRange': {'type': 'ALL'}, 'style': st, 'fields': ','.join(st.keys())}})
# cover logo: Palco wordmark -> Cruz Verde wordmark
s1 = P['slides'][0]['objectId']
if COVER_LOGO_OLD in idx: reqs.append({'deleteObject': {'objectId': COVER_LOGO_OLD}})
x, y, w, h = COVER_LOGO_BOX
reqs.append({'createImage': {'objectId': 'cv_cover_logo', 'url': LOGO, 'elementProperties': {'pageObjectId': s1,
    'size': {'width': {'magnitude': w * 12700, 'unit': 'EMU'}, 'height': {'magnitude': h * 12700, 'unit': 'EMU'}},
    'transform': {'scaleX': 1, 'scaleY': 1, 'shearX': 0, 'shearY': 0, 'translateX': x * 12700, 'translateY': y * 12700, 'unit': 'EMU'}}}})
# scan: untouched text elements that still look merchant-specific, and forbidden tokens in the simulated final text
bad = []
for n, s in enumerate(P['slides'], 1):
    for el, tr in elements(s):
        t = text_of(el).strip()
        if not t: continue
        chk = sim.get(el['objectId'], t)
        for f in FORBID:
            if f in chk: bad.append((n, el['objectId'], f, chk[:70]))
print("FORBIDDEN tokens in final text:"); [print("  S%d %s [%s] %s" % b) for b in bad]
print("requests:", len(reqs), "| text elements replaced:", len(sim))
if DRY: print("dry run, nothing changed"); sys.exit(0)
run(svc, PID, reqs, label='cruz verde build')
Q = svc.presentations().get(presentationId=PID).execute(); json.dump(Q, open(f'{OUT}/deck_after_build.json', 'w'))
changed = sorted({slide_of[o] for o in list(sim) + list(MOVE)} | {1})
for n in changed:
    r = svc.presentations().pages().getThumbnail(presentationId=PID, pageObjectId=Q['slides'][n - 1]['objectId'], thumbnailProperties_thumbnailSize='LARGE').execute()
    urllib.request.urlretrieve(r['contentUrl'], f"{OUT}/after_{n:02d}.png")
print("thumbs:", changed)
