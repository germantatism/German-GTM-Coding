"""Make the rebuilt Waymo deck's intro, dividers, vault wording and closing match the reviewed v6 deck."""
import os, sys, json, time, copy
from google.oauth2 import service_account
from googleapiclient.discovery import build
SRC = '1Qu3JvldczchxT9TrXmUkU1bSso9ltTGvOt5peT3hHjQ'; DST = '1r7g6kFtX8ZENovd3-51qyx9M0369yYLahpwXEGeEHRY'
creds = service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'), scopes=['https://www.googleapis.com/auth/presentations'])
svc = build('slides', 'v1', credentials=creds, cache_discovery=False)
def run(reqs, label):
    if not reqs: return
    for attempt in range(6):
        try:
            r = svc.presentations().batchUpdate(presentationId=DST, body={'requests': reqs}).execute(); print(f'  {label}: {len(reqs)} requests'); return r
        except Exception as e:
            if '429' in str(e) or 'RESOURCE_EXHAUSTED' in str(e): print('  429, waiting 65 s'); time.sleep(65)
            else: raise
src = svc.presentations().get(presentationId=SRC).execute()
dst = svc.presentations().get(presentationId=DST).execute()
S = src['slides']; D = dst['slides']
def sid(i): return D[i]['objectId']
def text_of(e):
    sh = e.get('shape', {}); return ''.join(te.get('textRun', {}).get('content', '') for te in sh.get('text', {}).get('textElements', []))
def find(slide, pred): return [e for e in slide['pageElements'] if pred(e)]
COUNTER = [0]
def nid(prefix='x'):
    COUNTER[0] += 1; return f'{prefix}_{int(time.time())%100000}_{COUNTER[0]}'
# ------------------------------------------------ element cloning
def clone_shape(e, page):
    oid = nid('sh'); sh = e['shape']; props = sh.get('shapeProperties', {})
    reqs = [{'createShape': {'objectId': oid, 'shapeType': sh.get('shapeType', 'TEXT_BOX'), 'elementProperties': {'pageObjectId': page, 'size': e['size'], 'transform': e['transform']}}}]
    sp = {}; fields = []
    bf = props.get('shapeBackgroundFill')
    if bf:
        if bf.get('propertyState') == 'NOT_RENDERED' or not bf.get('solidFill'): sp['shapeBackgroundFill'] = {'propertyState': 'NOT_RENDERED'}
        else: sp['shapeBackgroundFill'] = {'solidFill': bf['solidFill']}
        fields.append('shapeBackgroundFill')
    ol = props.get('outline')
    if ol:
        if ol.get('propertyState') == 'NOT_RENDERED' or not ol.get('outlineFill'): sp['outline'] = {'propertyState': 'NOT_RENDERED'}
        else: sp['outline'] = {k: v for k, v in ol.items() if k in ('outlineFill', 'weight', 'dashStyle')}
        fields.append('outline')
    if props.get('contentAlignment'): sp['contentAlignment'] = props['contentAlignment']; fields.append('contentAlignment')
    af = props.get('autofit', {}).get('autofitType')
    if af: sp['autofit'] = {'autofitType': af}; fields.append('autofit.autofitType')
    if fields: reqs.append({'updateShapeProperties': {'objectId': oid, 'shapeProperties': sp, 'fields': ','.join(fields)}})
    tes = sh.get('text', {}).get('textElements', [])
    full = ''.join(te.get('textRun', {}).get('content', '') for te in tes)
    if full.strip():
        reqs.append({'insertText': {'objectId': oid, 'insertionIndex': 0, 'text': full[:-1] if full.endswith('\n') else full}})
        for te in tes:
            if 'textRun' in te:
                st = {k: v for k, v in te['textRun'].get('style', {}).items() if k in ('fontFamily', 'fontSize', 'bold', 'italic', 'underline', 'strikethrough', 'smallCaps', 'baselineOffset', 'foregroundColor', 'backgroundColor', 'weightedFontFamily')}
                if st and te.get('endIndex', 0) > te.get('startIndex', 0):
                    reqs.append({'updateTextStyle': {'objectId': oid, 'textRange': {'type': 'FIXED_RANGE', 'startIndex': te.get('startIndex', 0), 'endIndex': te['endIndex']}, 'style': st, 'fields': ','.join(st.keys())}})
            elif 'paragraphMarker' in te:
                ps = {k: v for k, v in te['paragraphMarker'].get('style', {}).items() if k in ('alignment', 'lineSpacing', 'spaceAbove', 'spaceBelow', 'indentStart', 'indentEnd', 'indentFirstLine', 'direction', 'spacingMode')}
                if ps and te.get('endIndex', 0) > te.get('startIndex', 0):
                    reqs.append({'updateParagraphStyle': {'objectId': oid, 'textRange': {'type': 'FIXED_RANGE', 'startIndex': te.get('startIndex', 0), 'endIndex': te['endIndex']}, 'style': ps, 'fields': ','.join(ps.keys())}})
    return oid, reqs
def clone_image(e, page, url=None):
    oid = nid('im'); im = e['image']; ip = im.get('imageProperties', {})
    reqs = [{'createImage': {'objectId': oid, 'url': url or im['contentUrl'], 'elementProperties': {'pageObjectId': page, 'size': e['size'], 'transform': e['transform']}}}]
    up = {}; fields = []
    if ip.get('cropProperties'): up['cropProperties'] = ip['cropProperties']; fields.append('cropProperties')
    if ip.get('transparency'): up['transparency'] = ip['transparency']; fields.append('transparency')
    if ip.get('brightness') is not None: up['brightness'] = ip['brightness']; fields.append('brightness')
    if ip.get('contrast') is not None: up['contrast'] = ip['contrast']; fields.append('contrast')
    if fields: reqs.append({'updateImageProperties': {'objectId': oid, 'imageProperties': up, 'fields': ','.join(fields)}})
    return oid, reqs
def compose(g, c):
    """absolute transform of child c inside group g (preconcatenate)"""
    def m(t): return (t.get('scaleX', 1), t.get('shearX', 0), t.get('translateX', 0), t.get('shearY', 0), t.get('scaleY', 1), t.get('translateY', 0))
    a, b, tx, c_, d, ty = m(g); e, f, tx2, g_, h, ty2 = m(c)
    return {'scaleX': a*e + b*g_, 'shearX': a*f + b*h, 'translateX': a*tx2 + b*ty2 + tx, 'shearY': c_*e + d*g_, 'scaleY': c_*f + d*h, 'translateY': c_*tx2 + d*ty2 + ty, 'unit': 'EMU'}
def clone_elements(els, page, group_tf=None):
    reqs = []
    for e in els:
        if e.get('elementGroup'):
            tf = compose(group_tf, e['transform']) if group_tf else e['transform']
            reqs += clone_elements(e['elementGroup']['children'], page, tf); continue
        e2 = copy.deepcopy(e)
        if group_tf: e2['transform'] = compose(group_tf, e['transform'])
        if e2.get('shape'): reqs += clone_shape(e2, page)[1]
        elif e2.get('image'): reqs += clone_image(e2, page)[1]
        elif e2.get('line'): print('  skip line', e['objectId'])
    return reqs
# ------------------------------------------------ 1. story slide (3): drop kicker, $30B -> $100B
n03 = sid(2); k = find(D[2], lambda e: text_of(e).strip() == 'THE YUNO STORY')
run([{'deleteObject': {'objectId': k[0]['objectId']}}] + [{'replaceAllText': {'containsText': {'text': '30', 'matchCase': True}, 'replaceText': '100', 'pageObjectIds': [n03]}}], 'story')
# 2. pillars (4): drop kicker
k = find(D[3], lambda e: text_of(e).strip() == 'ABOUT YUNO · PLATFORM'); run([{'deleteObject': {'objectId': k[0]['objectId']}}], 'pillars')
# 3. trusted (5): drop kicker, Kraken -> Moonactive, page number 6
n05 = sid(4); k = find(D[4], lambda e: text_of(e).strip() == 'WHY YUNO?')
moon = [e for e in S[5]['pageElements'] if e.get('image') and 'moonactive' in e['image'].get('sourceUrl', '')][0]
kraken = [e for e in D[4]['pageElements'] if e['objectId'].endswith('g3f76accd9b2_0_0')][0]
pn = find(D[4], lambda e: text_of(e).strip() == '5')
run([{'deleteObject': {'objectId': k[0]['objectId']}},
     {'replaceImage': {'imageObjectId': kraken['objectId'], 'url': moon['image']['sourceUrl'], 'imageReplaceMethod': 'CENTER_INSIDE'}},
     {'updatePageElementTransform': {'objectId': kraken['objectId'], 'transform': moon['transform'], 'applyMode': 'ABSOLUTE'}}]
    + ([{'deleteText': {'objectId': pn[0]['objectId'], 'textRange': {'type': 'ALL'}}}, {'insertText': {'objectId': pn[0]['objectId'], 'insertionIndex': 0, 'text': '6'}}] if pn else []), 'trusted')
# 4. team (6): wipe and clone v6 slide 5
n06 = sid(5)
run([{'deleteObject': {'objectId': e['objectId']}} for e in D[5]['pageElements']], 'team wipe')
bg = S[4].get('pageProperties', {}).get('pageBackgroundFill')
reqs = [{'updatePageProperties': {'objectId': n06, 'pageProperties': {'pageBackgroundFill': bg}, 'fields': 'pageBackgroundFill'}}] if bg else []
reqs += clone_elements(S[4]['pageElements'], n06)
for i in range(0, len(reqs), 120): run(reqs[i:i+120], f'team clone {i}')
run([{'updateSlidesPosition': {'slideObjectIds': [n06], 'insertionIndex': 4}}], 'team before logos')
# 5. closing: new slide from the End layout, texts and lockup from v6 slide 80; drop next steps
end_layout = [l['objectId'] for l in dst['layouts'] if l['layoutProperties'].get('displayName') == 'End' and l['layoutProperties'].get('masterObjectId') == 'p50'][0]
cl = 'closing_v7'
run([{'createSlide': {'objectId': cl, 'insertionIndex': len(D), 'slideLayoutReference': {'layoutId': end_layout}, 'placeholderIdMappings': [{'layoutPlaceholder': {'type': 'TITLE', 'index': 0}, 'objectId': cl + '_t'}, {'layoutPlaceholder': {'type': 'BODY', 'index': 0}, 'objectId': cl + '_b'}]}}], 'closing create')
reqs = []
for e in S[79]['pageElements']:
    ph = e.get('shape', {}).get('placeholder', {}).get('type')
    if ph in ('TITLE', 'BODY'):
        oid = cl + ('_t' if ph == 'TITLE' else '_b'); tes = e['shape']['text']['textElements']; full = ''.join(te.get('textRun', {}).get('content', '') for te in tes)
        reqs.append({'insertText': {'objectId': oid, 'insertionIndex': 0, 'text': full[:-1] if full.endswith('\n') else full}})
        for te in tes:
            if 'textRun' in te:
                st = {k: v for k, v in te['textRun'].get('style', {}).items() if k in ('fontFamily', 'fontSize', 'bold', 'italic', 'foregroundColor', 'weightedFontFamily')}
                if st and te.get('endIndex', 0) > te.get('startIndex', 0): reqs.append({'updateTextStyle': {'objectId': oid, 'textRange': {'type': 'FIXED_RANGE', 'startIndex': te.get('startIndex', 0), 'endIndex': te['endIndex']}, 'style': st, 'fields': ','.join(st.keys())}})
        reqs.append({'updatePageElementTransform': {'objectId': oid, 'transform': e['transform'], 'applyMode': 'ABSOLUTE'}})
    elif e.get('image'): reqs += clone_image(e, cl, url=e['image'].get('sourceUrl') or None)[1]
run(reqs, 'closing content')
nxt = sid(len(D) - 1); run([{'deleteObject': {'objectId': nxt}}], 'drop next steps')
# 6. dividers and vault wording
d01, d02, d03 = sid(1), sid(6), sid(11)
reqs = [{'replaceAllText': {'containsText': {'text': '03 CONNECTIONS AND PAYMENT METHODS', 'matchCase': True}, 'replaceText': '03 CONNECTIONS AND PAYMENT METHODS IN TARGET MARKETS', 'pageObjectIds': [d01, d02, d03]}},
        {'replaceAllText': {'containsText': {'text': 'The token vault', 'matchCase': True}, 'replaceText': 'The Token Vault', 'pageObjectIds': [d02]}},
        {'replaceAllText': {'containsText': {'text': 'Connections and payment methods', 'matchCase': True}, 'replaceText': 'Connections and payment methods in target markets', 'pageObjectIds': [d03]}}]
for i, start in [(1, 'What we do, the platform'), (6, 'A PCI DSS Level 1 vault you can use'), (11, 'Who is live through Yuno')]:
    for e in find(D[i], lambda e: text_of(e).strip().startswith(start)): reqs.append({'deleteObject': {'objectId': e['objectId']}})
run(reqs, 'dividers')
wv = {s['objectId']: s for s in D}
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
