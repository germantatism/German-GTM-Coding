"""HBO Max v2: match the reviewed v1 deck (intro kickers, $100B, team slide, closing with Skydance lockup, cover lockup and presenter line, drop next steps)."""
import os, sys, json, time, copy
sys.argv=[sys.argv[0]]
src_code = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sync_intro.py')).read().split('# ------------------------------------------------ 1. story slide')[0]
src_code = src_code.replace("SRC = '1Qu3JvldczchxT9TrXmUkU1bSso9ltTGvOt5peT3hHjQ'; DST = '1r7g6kFtX8ZENovd3-51qyx9M0369yYLahpwXEGeEHRY'", "SRC = '1TyFXKt2OfoBLHGn8T1xX_Z1Uic_5ZYeeGUb8g_n0jrw'; DST = '1vULwizzS9eoNpyOYCOEfxGDkZegRp_9bmPgPhUAy2zo'")
exec(src_code)
print('src', len(S), 'dst', len(D))
# 1. story: drop kicker, 30 -> 100
k = find(D[2], lambda e: text_of(e).strip() == 'THE YUNO STORY')
run([{'deleteObject': {'objectId': k[0]['objectId']}}, {'replaceAllText': {'containsText': {'text': '30', 'matchCase': True}, 'replaceText': '100', 'pageObjectIds': [sid(2)]}}], 'story')
# 2. pillars kicker
k = find(D[3], lambda e: text_of(e).strip() == 'ABOUT YUNO · PLATFORM'); run([{'deleteObject': {'objectId': k[0]['objectId']}}], 'pillars')
# 3. trusted: kicker + page number 6 (logo swap done separately)
k = find(D[4], lambda e: text_of(e).strip() == 'WHY YUNO?'); pn = find(D[4], lambda e: text_of(e).strip() == '5')
run([{'deleteObject': {'objectId': k[0]['objectId']}}] + ([{'deleteText': {'objectId': pn[0]['objectId'], 'textRange': {'type': 'ALL'}}}, {'insertText': {'objectId': pn[0]['objectId'], 'insertionIndex': 0, 'text': '6'}}] if pn else []), 'trusted')
# 4. team: wipe v2 template team slide and clone v1 slide 5 (index 4)
n06 = sid(5)
run([{'deleteObject': {'objectId': e['objectId']}} for e in D[5]['pageElements']], 'team wipe')
bg = S[4].get('pageProperties', {}).get('pageBackgroundFill')
reqs = [{'updatePageProperties': {'objectId': n06, 'pageProperties': {'pageBackgroundFill': bg}, 'fields': 'pageBackgroundFill'}}] if bg else []
reqs += clone_elements(S[4]['pageElements'], n06)
for i in range(0, len(reqs), 120): run(reqs[i:i+120], f'team clone {i}')
run([{'updateSlidesPosition': {'slideObjectIds': [n06], 'insertionIndex': 4}}], 'team before logos')
# 5. closing from v1 slide 90 (index 89): layout graphics + texts + lockup
cs = S[89]; lay6 = {l['objectId']: l for l in src['layouts']}[cs['slideProperties']['layoutObjectId']]
mas6 = {m['objectId']: m for m in src['masters']}[lay6['layoutProperties']['masterObjectId']]
def ph_style(layout, ptype):
    for e in layout.get('pageElements', []):
        if e.get('shape', {}).get('placeholder', {}).get('type') == ptype:
            for te in e['shape'].get('text', {}).get('textElements', []):
                if 'textRun' in te: return te['textRun'].get('style', {})
    return {}
cl = 'closing_v2'
run([{'createSlide': {'objectId': cl, 'insertionIndex': len(D), 'slideLayoutReference': {'layoutId': 'g3f77215683c_2_1907'}}}], 'closing create')
dark = None
for c in mas6.get('masterProperties', {}).get('colorScheme', {}).get('colors', []):
    if c.get('type') == 'DARK1': dark = c.get('color')
reqs = [{'updatePageProperties': {'objectId': cl, 'pageProperties': {'pageBackgroundFill': {'solidFill': {'color': {'rgbColor': dark or {}}, 'alpha': 1}}}, 'fields': 'pageBackgroundFill'}}]
reqs += clone_elements([e for e in lay6.get('pageElements', []) if not e.get('shape', {}).get('placeholder')], cl)
for e in cs['pageElements']:
    ph = e.get('shape', {}).get('placeholder', {}).get('type')
    if ph in ('TITLE', 'BODY'):
        base = ph_style(lay6, ph); e2 = copy.deepcopy(e); e2['shape'].pop('placeholder', None)
        for te in e2['shape']['text']['textElements']:
            if 'textRun' in te:
                st = dict(base); st.update(te['textRun'].get('style', {})); st['foregroundColor'] = {'opaqueColor': {'rgbColor': {'red': 1, 'green': 1, 'blue': 1}}}; te['textRun']['style'] = st
            if 'paragraphMarker' in te and ph == 'BODY':
                st = te['paragraphMarker'].get('style', {}); st['indentStart'] = {'magnitude': 0, 'unit': 'PT'}; st['indentFirstLine'] = {'magnitude': 0, 'unit': 'PT'}
        e2['shape']['shapeProperties']['autofit'] = {'autofitType': 'NONE'}
        if ph == 'BODY': e2['transform']['scaleX'] = max(e2['transform'].get('scaleX', 1), 1.9)
        reqs += clone_shape(e2, cl)[1]
    elif e.get('image'): reqs += clone_image(e, cl, url=e['image'].get('sourceUrl') or None)[1]
    elif e.get('shape'): reqs += clone_shape(e, cl)[1]
run(reqs, 'closing content')
run([{'deleteObject': {'objectId': sid(len(D) - 1)}}], 'drop next steps')
# 6. cover: presenter line and Skydance lockup from v1
cov1, cov2 = S[0], D[0]
reqs = []
for e in cov2['pageElements']:
    if e.get('image') or e.get('elementGroup') or (e.get('shape') and text_of(e).strip() in ('+', '|')): reqs.append({'deleteObject': {'objectId': e['objectId']}})
pres = find(cov2, lambda e: 'October 2026' in text_of(e) and 'German' in text_of(e))
if pres: reqs.append({'replaceAllText': {'containsText': {'text': 'German Tatis, Yuno · October 2026', 'matchCase': True}, 'replaceText': 'Yuno · October 2026', 'pageObjectIds': [cov2['objectId']]}})
for e in cov1['pageElements']:
    if e.get('image') or e.get('elementGroup'): reqs += clone_elements([e], cov2['objectId'])
    elif e.get('shape') and text_of(e).strip() in ('+', '|'): reqs += clone_shape(e, cov2['objectId'])[1]
run(reqs, 'cover lockup')
dst2 = svc.presentations().get(presentationId=DST, fields='slides.objectId').execute()
print('final slides', len(dst2['slides']), [s['objectId'][:12] for s in dst2['slides'][:8]], dst2['slides'][-1]['objectId'])
