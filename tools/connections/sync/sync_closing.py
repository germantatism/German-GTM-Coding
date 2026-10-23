"""Second half of the sync: closing slide cloned from v6 (layout graphics + texts + lockup), drop next steps, divider and vault wording."""
import os, sys, json, time, copy
sys.argv = [sys.argv[0]]
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sync_intro.py')).read().split('# ------------------------------------------------ 1. story slide')[0])
S6 = S; D7 = D
lay6 = {l['objectId']: l for l in src['layouts']}['h2d2d16976c09ce2e_6_1396']
mas6 = {m['objectId']: m for m in src['masters']}[lay6['layoutProperties']['masterObjectId']]
def ph_style(layout, ptype):
    for e in layout.get('pageElements', []):
        if e.get('shape', {}).get('placeholder', {}).get('type') == ptype:
            for te in e['shape'].get('text', {}).get('textElements', []):
                if 'textRun' in te: return te['textRun'].get('style', {})
    return {}
cl = 'closing_v7'
default_layout = [l['objectId'] for l in dst['layouts'] if l['objectId'] == 'g3f77215683c_2_1907'][0]
run([{'createSlide': {'objectId': cl, 'insertionIndex': len(D7), 'slideLayoutReference': {'layoutId': default_layout}}}], 'closing create')
# background: DARK1 of the v6 master -> resolve to rgb if possible, else black
dark = None
for c in mas6.get('masterProperties', {}).get('colorScheme', {}).get('colors', []):
    if c.get('type') == 'DARK1': dark = c.get('color')
reqs = [{'updatePageProperties': {'objectId': cl, 'pageProperties': {'pageBackgroundFill': {'solidFill': {'color': {'rgbColor': dark or {}}, 'alpha': 1}}}, 'fields': 'pageBackgroundFill'}}]
# layout graphics (non-placeholder elements), then slide elements
lay_els = [e for e in lay6.get('pageElements', []) if not e.get('shape', {}).get('placeholder')]
reqs += clone_elements(lay_els, cl)
for e in S6[79]['pageElements']:
    ph = e.get('shape', {}).get('placeholder', {}).get('type')
    if ph in ('TITLE', 'BODY'):
        base = ph_style(lay6, ph); e2 = copy.deepcopy(e); e2['shape'].pop('placeholder', None)
        for te in e2['shape']['text']['textElements']:
            if 'textRun' in te:
                st = dict(base); st.update(te['textRun'].get('style', {})); te['textRun']['style'] = st
        e2['shape']['shapeProperties']['autofit'] = {'autofitType': 'NONE'}
        reqs += clone_shape(e2, cl)[1]
    elif e.get('image'): reqs += clone_image(e, cl, url=e['image'].get('sourceUrl') or None)[1]
run(reqs, 'closing content')
nxt = sid(len(D7) - 1); run([{'deleteObject': {'objectId': nxt}}], 'drop next steps')
# dividers and vault wording
d01, d02, d03 = sid(1), sid(6), sid(11)
reqs = [{'replaceAllText': {'containsText': {'text': '03 CONNECTIONS AND PAYMENT METHODS', 'matchCase': True}, 'replaceText': '03 CONNECTIONS AND PAYMENT METHODS IN TARGET MARKETS', 'pageObjectIds': [d01, d02, d03]}},
        {'replaceAllText': {'containsText': {'text': 'The token vault', 'matchCase': True}, 'replaceText': 'The Token Vault', 'pageObjectIds': [d02]}},
        {'replaceAllText': {'containsText': {'text': 'Connections and payment methods', 'matchCase': True}, 'replaceText': 'Connections and payment methods in target markets', 'pageObjectIds': [d03]}}]
for i, start in [(1, 'What we do, the platform'), (6, 'A PCI DSS Level 1 vault you can use'), (11, 'Who is live through Yuno')]:
    for e in find(D7[i], lambda e: text_of(e).strip().startswith(start)): reqs.append({'deleteObject': {'objectId': e['objectId']}})
run(reqs, 'dividers')
wv = {s['objectId']: s for s in D7}
reqs = [{'replaceAllText': {'containsText': {'text': 'London 2026', 'matchCase': True}, 'replaceText': 'London', 'pageObjectIds': ['wv_problem']}},
        {'replaceAllText': {'containsText': {'text': 'Tokyo, Munich 2027', 'matchCase': True}, 'replaceText': 'Tokyo, Munich', 'pageObjectIds': ['wv_problem']}},
        {'replaceAllText': {'containsText': {'text': 'Singapore, Toronto 2028', 'matchCase': True}, 'replaceText': 'Singapore, Toronto', 'pageObjectIds': ['wv_problem']}},
        {'replaceAllText': {'containsText': {'text': 'Tokenisation', 'matchCase': True}, 'replaceText': 'Tokenization', 'pageObjectIds': ['wv_summary']}},
        {'replaceAllText': {'containsText': {'text': 'One token on both PSPs, with routing', 'matchCase': True}, 'replaceText': 'One token on both PSPs (and future), with routing', 'pageObjectIds': ['wv_summary']}}]
for e in find(wv['wv_summary'], lambda e: text_of(e).strip() == 'INCLUDED'): reqs.append({'deleteObject': {'objectId': e['objectId']}})
for e in find(wv['wv_versus'], lambda e: text_of(e).strip().startswith('Yuno leads on 4')): reqs.append({'deleteObject': {'objectId': e['objectId']}})
run(reqs, 'vault wording')
dst2 = svc.presentations().get(presentationId=DST, fields='slides.objectId').execute()
print('final slides', len(dst2['slides']), [s['objectId'][:12] for s in dst2['slides'][:13]], dst2['slides'][-1]['objectId'])
