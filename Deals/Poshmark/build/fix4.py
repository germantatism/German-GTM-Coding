# -*- coding: utf-8 -*-
"""Fix pass 4 (23 Oct 2026, after the web research landed): speaker notes re-applied from content.NOTES on every slide,
and a Poshmark source line (offers_help wording) added under the table on slide 7."""
import json, time, os, urllib.request
import gs_lib as g
from gs_lib import Page, GREY
import content as C
from build_vault_deck import DECK, S
s = g.svc(); pid = DECK
P = s.presentations().get(presentationId=pid).execute()
json.dump(P, open('backup_poshmark_prefix4_' + time.strftime('%H%M%S') + '.json', 'w'))
R = []
for key, text in C.NOTES.items(): R += g.set_notes(s, pid, P, S[key], text)
sl = g.slide(P, S['personal']); ids = {e['objectId'] for e in g.walk(sl['pageElements'])}
if 'posh_offer_src_k001' in ids: R.append({'deleteObject': {'objectId': 'posh_offer_src_k001'}})
p = Page(S['personal'], prefix='posh_offer_src')
p.text(50, 342, 356, 22, C.OFFER['src'], size=7.5, color=GREY, ls=112)   # inside the left card, under the foot line
g.run(s, pid, R + p.R, 'fix4')
os.makedirs('thumbs_v3', exist_ok=True)
t = s.presentations().pages().getThumbnail(presentationId=pid, pageObjectId=S['personal'], thumbnailProperties_thumbnailSize='LARGE').execute()
urllib.request.urlretrieve(t['contentUrl'], 'thumbs_v3/s07.png'); print('fix4 done, thumb s07')
