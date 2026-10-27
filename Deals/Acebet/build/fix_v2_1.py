# -*- coding: utf-8 -*-
"""v2 fix 1 (27-oct-2026): the house-slide page-number pass rewrote every digit-only text (smart routing steps 1/2/3 and
route circles, proven stats, results '21'). Restore those from before.json (only the bottom-left page number keeps the new
value), shorten the slide 2 headline, and say '1.5 cents' in the pricing headline."""
import sys, json
sys.path.insert(0, '/Users/germantatis/Desktop/GTMCoding/Deals/Yuno General Deck/build')
from gsl import *
from v2 import PID, WORK, HOUSE, txt
svc = service()
B = json.load(open(f'{WORK}/before.json')); Q = svc.presentations().get(presentationId=PID).execute()
now = {e['objectId']: e for sl in Q['slides'] for e in sl.get('pageElements', [])}
reqs = []
for key, sid in HOUSE.items():
    sl = next(x for x in B['slides'] if x['objectId'] == sid)
    for e in sl['pageElements']:
        t = txt(e); y = e.get('transform', {}).get('translateY', 0) / PT
        if t.isdigit() and y < 360 and e['objectId'] in now and txt(now[e['objectId']]) != t:
            s = Slide(sid); s.set_text(e['objectId'], t); reqs += s.reqs; print('restore', key, e['objectId'], txt(now[e['objectId']]), '->', t)
def head(old, new):
    for sl in Q['slides']:
        for e in sl.get('pageElements', []):
            if txt(e) == old: s = Slide(sl['objectId']); s.set_text(e['objectId'], new); reqs.extend(s.reqs); print('headline', new)
head('Acebet wants leverage and redundancy across acquirers, with room to grow', 'Acebet wants leverage, redundancy and room to grow')
head('Platform fee plus usage: about 2.5 cents a transaction today, 1.5 above 1M', 'Platform fee plus usage: about 2.5 cents today, 1.5 cents above 1M')
svc.presentations().batchUpdate(presentationId=PID, body={'requests': reqs}).execute()
import urllib.request
Q = svc.presentations().get(presentationId=PID).execute()
for n, sl in enumerate(Q['slides'], 1):
    r = svc.presentations().pages().getThumbnail(presentationId=PID, pageObjectId=sl['objectId'], thumbnailProperties_thumbnailSize='LARGE').execute()
    urllib.request.urlretrieve(r['contentUrl'], f'{WORK}/f1_{n:02d}.png')
print('done', len(reqs))
