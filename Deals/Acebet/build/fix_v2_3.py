# -*- coding: utf-8 -*-
"""v2 fix 3 (German, 27-oct-2026): 'What's included' redrawn: 1,000+ methods / 450+ providers / 50+ anti-fraud tiles,
payouts box removed, reconciliation box full width 'For further review'. Clears the drawn r_/t_/l_ elements and redraws terms()."""
import sys
sys.path.insert(0, '/Users/germantatis/Desktop/GTMCoding/Deals/Yuno General Deck/build')
from gsl import *
import v2
svc = service(); P = svc.presentations().get(presentationId=v2.PID).execute()
sl = next(x for x in P['slides'] if any(v2.txt(e) == 'INCLUDED IN THE PLATFORM FEE' for e in x['pageElements']))
reqs = [{'deleteObject': {'objectId': e['objectId']}} for e in sl['pageElements'] if e['objectId'][:2] in ('r_', 't_', 'l_')]
s = Slide(sl['objectId']); v2.terms(s); reqs += s.reqs
svc.presentations().batchUpdate(presentationId=v2.PID, body={'requests': reqs}).execute()
import urllib.request
r = svc.presentations().pages().getThumbnail(presentationId=v2.PID, pageObjectId=sl['objectId'], thumbnailProperties_thumbnailSize='LARGE').execute()
urllib.request.urlretrieve(r['contentUrl'], f'{v2.WORK}/f5_terms.png'); print('ok', len(reqs))
