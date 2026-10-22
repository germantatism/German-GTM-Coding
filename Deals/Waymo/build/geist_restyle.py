# -*- coding: utf-8 -*-
"""Restyle slides drawn with the OnlyFans primitives (Titillium Web / Roboto Mono) to the deck's fonts (Geist / Geist Mono).
Weights: <600 -> 400, >=600 -> 700. Titles (19/18 pt regular) become Geist 700 at 17 pt so two lines fit above the content.
  python3 geist_restyle.py <presentation_id> <slide_id,slide_id,...>"""
import os, sys, warnings; warnings.filterwarnings('ignore')
from google.oauth2 import service_account
from googleapiclient.discovery import build
pid, sids = sys.argv[1], sys.argv[2].split(',')
cr = service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'), scopes=['https://www.googleapis.com/auth/presentations'])
s = build('slides', 'v1', credentials=cr, cache_discovery=False)
MAP = {'Titillium Web': 'Geist', 'Roboto Mono': 'Geist Mono'}
def walk(els):
    for e in els:
        if 'elementGroup' in e: yield from walk(e['elementGroup']['children'])
        else: yield e
for sid in sids:
    page = s.presentations().pages().get(presentationId=pid, pageObjectId=sid).execute(); reqs = []; n = 0
    for el in walk(page['pageElements']):
        tes = el.get('shape', {}).get('text', {}).get('textElements', [])
        for te in tes:
            tr = te.get('textRun')
            if not tr or not tr.get('content', '').strip(): continue
            st = tr.get('style', {}); wff = st.get('weightedFontFamily', {}); fam = wff.get('fontFamily', '')
            if fam not in MAP: continue
            w = wff.get('weight', 400); size = st.get('fontSize', {}).get('magnitude', 0)
            new = {'weightedFontFamily': {'fontFamily': MAP[fam], 'weight': 700 if w >= 600 else 400}}; fields = 'weightedFontFamily'
            if fam == 'Titillium Web' and size in (18, 19):   # slide titles
                new['weightedFontFamily']['weight'] = 700; new['fontSize'] = {'magnitude': 17, 'unit': 'PT'}; fields += ',fontSize'
            reqs.append({'updateTextStyle': {'objectId': el['objectId'], 'textRange': {'type': 'FIXED_RANGE', 'startIndex': te.get('startIndex', 0), 'endIndex': te['endIndex']}, 'style': new, 'fields': fields}}); n += 1
    for i in range(0, len(reqs), 300): s.presentations().batchUpdate(presentationId=pid, body={'requests': reqs[i:i + 300]}).execute()
    print(sid, n, 'runs restyled')
