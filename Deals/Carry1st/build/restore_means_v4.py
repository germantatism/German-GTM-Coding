# -*- coding: utf-8 -*-
"""One-off (26 Oct 2026): German asked to keep slide 12 of v4 uniform, so the 'What it means for Carry1st' card goes back to its full height
with the explanatory box and the cents line, copied from v2 (1D1HwXY1...) with the box text updated to the 6-month minimum. Usage: python3 restore_means_v4.py"""
import warnings; warnings.filterwarnings('ignore')
import gs_engine as E
SRC, PID, SLIDE = '1D1HwXY1TRczJxtqDKWi_JgJT-cKqSXhuH-6rRn1BIQ4', '17-dirMLGwFpXBgknXjkvt95rvDW1zNJ7QiaXDvWI8yA', 'n22r1_g3f77215683c_2_2968'
TEXT = {'simp_e022': 'A $2,500 minimum for six months, then $7,500 a month from month 7. No fixed fee per transaction, and the rate falls as Carry1st grows.'}
assert E.wrap_count(TEXT['simp_e022'], 8.5, 240.4, True) <= 3
src = {el['objectId']: el for s in E.Deck(SRC).fetch()['slides'] for el, _ in E.elements(s)}
deck = E.Deck(PID); P = deck.fetch()
cur = {el['objectId']: el for s in P['slides'] if s['objectId'] == SLIDE for el, _ in E.elements(s)}
reqs = [{'updatePageElementTransform': {'objectId': 'n22r1_e054', 'applyMode': 'ABSOLUTE', 'transform': {**src['n22r1_e054']['transform'], 'unit': 'EMU'}}}]
for oid in ('simp_e021', 'simp_e022', 'simp_e023'):
    assert oid not in cur, oid
    el = src[oid]; sp = el['shape']
    reqs.append({'createShape': {'objectId': oid, 'shapeType': sp['shapeType'], 'elementProperties': {'pageObjectId': SLIDE, 'size': el['size'], 'transform': el['transform']}}})
    props = {k: v for k, v in sp['shapeProperties'].items() if k in ('shapeBackgroundFill', 'outline', 'contentAlignment')}
    reqs.append({'updateShapeProperties': {'objectId': oid, 'shapeProperties': props, 'fields': ','.join(props)}})
    if 'text' in sp:
        run = next(te for te in sp['text']['textElements'] if 'textRun' in te)
        para = next(te for te in sp['text']['textElements'] if 'paragraphMarker' in te)['paragraphMarker']['style']
        t = TEXT.get(oid, run['textRun']['content'].rstrip('\n'))
        st = {k: v for k, v in run['textRun']['style'].items() if k in ('foregroundColor', 'bold', 'fontSize', 'weightedFontFamily')}
        reqs += [{'insertText': {'objectId': oid, 'text': t}},
                 {'updateTextStyle': {'objectId': oid, 'style': st, 'fields': ','.join(st), 'textRange': {'type': 'ALL'}}},
                 {'updateParagraphStyle': {'objectId': oid, 'style': {'lineSpacing': para['lineSpacing'], 'alignment': 'START'}, 'fields': 'lineSpacing,alignment', 'textRange': {'type': 'ALL'}}}]
deck.run(reqs, 'restore what-it-means card')
print('ok', len(reqs))
