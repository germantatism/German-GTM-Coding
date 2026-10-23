import os, sys, json, time, copy
sys.argv=[sys.argv[0]]
src_code = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sync_intro.py')).read().split('# ------------------------------------------------ 1. story slide')[0]
src_code = src_code.replace("SRC = '1Qu3JvldczchxT9TrXmUkU1bSso9ltTGvOt5peT3hHjQ'; DST = '1r7g6kFtX8ZENovd3-51qyx9M0369yYLahpwXEGeEHRY'", "SRC = '1TyFXKt2OfoBLHGn8T1xX_Z1Uic_5ZYeeGUb8g_n0jrw'; DST = '1vULwizzS9eoNpyOYCOEfxGDkZegRp_9bmPgPhUAy2zo'")
exec(src_code)
print('src', len(S), 'dst', len(D))
cs = S[89]; lay6 = {l['objectId']: l for l in src['layouts']}[cs['slideProperties']['layoutObjectId']]
mas6 = {m['objectId']: m for m in src['masters']}[lay6['layoutProperties']['masterObjectId']]
def ph_style(layout, ptype):
    for e in layout.get('pageElements', []):
        if e.get('shape', {}).get('placeholder', {}).get('type') == ptype:
            for te in e['shape'].get('text', {}).get('textElements', []):
                if 'textRun' in te: return te['textRun'].get('style', {})
    return {}
cl = 'closing_v2'
closing = [s for s in D if s['objectId'] == cl][0]
run([{'deleteObject': {'objectId': e['objectId']}} for e in closing.get('pageElements', [])], 'closing reset')
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
    elif e.get('image'): reqs += clone_image(e, cl)[1]      # contentUrl, fresh
    elif e.get('shape'): reqs += clone_shape(e, cl)[1]
    elif e.get('elementGroup'): reqs += clone_elements([e], cl)
run(reqs, 'closing content')
nxt = [s for s in D if s['objectId'].startswith('n91_')]
if nxt: run([{'deleteObject': {'objectId': nxt[0]['objectId']}}], 'drop next steps')
cov1, cov2 = S[0], D[0]
reqs = []
for e in cov2['pageElements']:
    if e.get('image') or e.get('elementGroup') or (e.get('shape') and text_of(e).strip() in ('+', '|')): reqs.append({'deleteObject': {'objectId': e['objectId']}})
reqs.append({'replaceAllText': {'containsText': {'text': 'German Tatis, Yuno · October 2026', 'matchCase': True}, 'replaceText': 'Yuno · October 2026', 'pageObjectIds': [cov2['objectId']]}})
for e in cov1['pageElements']:
    if e.get('image') or e.get('elementGroup'): reqs += clone_elements([e], cov2['objectId'])
    elif e.get('shape') and text_of(e).strip() in ('+', '|'): reqs += clone_shape(e, cov2['objectId'])[1]
run(reqs, 'cover lockup')
dst2 = svc.presentations().get(presentationId=DST, fields='slides.objectId').execute()
print('final slides', len(dst2['slides']), [s['objectId'][:12] for s in dst2['slides'][:8]], dst2['slides'][-1]['objectId'])
