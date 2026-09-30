# -*- coding: utf-8 -*-
"""Step 0 (run once, before build_ld.py): duplicate the pristine pricing slide to use as canvas for the payment-methods slide.
New element ids: 'ldm_' + last two id segments. The copy is placed right before the pricing slide."""
import json
from common import *
s = svc(); P = s.presentations().get(presentationId=PID).execute()
if any(sl['objectId'] == 'ld_methods' for sl in P['slides']): raise SystemExit('ld_methods already exists')
src = next(sl for sl in P['slides'] if sl['objectId'] == 'g3fb7d86b358_4_331')
idmap = {src['objectId']: 'ld_methods'}
for el, tr in elements(src): idmap[el['objectId']] = 'ldm_' + '_'.join(el['objectId'].split('_')[-2:])
assert len(set(idmap.values())) == len(idmap)
pos0 = [sl['objectId'] for sl in P['slides']].index(src['objectId'])
run(s, PID, [{'duplicateObject': {'objectId': src['objectId'], 'objectIds': idmap}},
             {'updateSlidesPosition': {'slideObjectIds': ['ld_methods'], 'insertionIndex': pos0}}], label='dup methods slide')
Q = s.presentations().get(presentationId=PID).execute()
print([(i + 1, sl['objectId']) for i, sl in enumerate(Q['slides'])][13:19])
json.dump(Q, open(f'{WORK}/deck_after_dup.json', 'w'))
