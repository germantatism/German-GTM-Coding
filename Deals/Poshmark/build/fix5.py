# -*- coding: utf-8 -*-
"""Fix pass 5 (23 Oct 2026): slide 7 footer shortened to one line and the Poshmark source line re-placed below it with an exact (elided) quote."""
import json, time, os, urllib.request
import gs_lib as g
from gs_lib import Page, GREY
import content as C
from build_vault_deck import DECK, S
s = g.svc(); pid = DECK
P = s.presentations().get(presentationId=pid).execute()
json.dump(P, open('backup_poshmark_prefix5_' + time.strftime('%H%M%S') + '.json', 'w'))
sl = g.slide(P, S['personal']); R = []
foot = next(e for e in g.walk(sl['pageElements']) if g.txt(e).startswith('Captured when'))
g.set_text_el(foot, C.OFFER['foot'], R)
for e in g.walk(sl['pageElements']):
    if e['objectId'].startswith('posh_offer_src'): R.append({'deleteObject': {'objectId': e['objectId']}})
p = Page(S['personal'], prefix='posh_offer_src2')
p.text(50, 342, 356, 22, C.OFFER['src'], size=7.5, color=GREY, ls=112)
g.run(s, pid, R + p.R, 'fix5')
t = s.presentations().pages().getThumbnail(presentationId=pid, pageObjectId=S['personal'], thumbnailProperties_thumbnailSize='LARGE').execute()
urllib.request.urlretrieve(t['contentUrl'], 'thumbs_v3/s07.png'); print('fix5 done, thumb s07')
