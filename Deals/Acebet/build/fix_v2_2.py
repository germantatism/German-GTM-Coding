# -*- coding: utf-8 -*-
"""v2 fix 2 (German, 27-oct-2026): 'As Acebet grows' column shows the usage rate only, platform fee out."""
import sys
sys.path.insert(0, '/Users/germantatis/Desktop/GTMCoding/Deals/Yuno General Deck/build')
from gsl import *
from v2 import PID, WORK
from model import var, GROWTH
svc = service(); P = svc.presentations().get(presentationId=PID).execute()
sid = next(sl['objectId'] for sl in P['slides'] for e in sl['pageElements'] if e['objectId'] == 't_e8fce7154a51')
s = Slide(sid)
s.set_text('t_e8fce7154a51', 'Average rate per transaction, before the platform fee')
cells = [('t_a365e5a49abc', 't_9955d4480f2e'), ('t_0e0be11016ed', 't_dd0c251db806'), ('t_4d186c661572', 't_0458e08effdd'), ('t_12a9f2670f25', 't_9b81ec99f2d9')]
for (big, small), t in zip(cells, GROWTH):
    s.set_text(big, f'${var(t)/t:.3f}'); s.set_text(small, f'${var(t):,.0f}/mo'); print(t, f'${var(t)/t:.3f}', f'${var(t):,.0f}/mo')
svc.presentations().batchUpdate(presentationId=PID, body={'requests': s.reqs}).execute()
import urllib.request
r = svc.presentations().pages().getThumbnail(presentationId=PID, pageObjectId=sid, thumbnailProperties_thumbnailSize='LARGE').execute()
urllib.request.urlretrieve(r['contentUrl'], f'{WORK}/f2_price.png'); print('ok')
