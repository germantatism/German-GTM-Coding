# -*- coding: utf-8 -*-
"""Shared Google Slides helpers for the Skydance / Paramount token vault deck.
Design tokens and primitives are the OnlyFans vault deck ones (Deals/OnlyFans/build/split_decks.py):
Titillium Web, blue kicker, white cards with fine border, #F4F5FD panels."""
import os, re, json, time, warnings
warnings.filterwarnings('ignore')
from google.oauth2 import service_account
from googleapiclient.discovery import build

PT = 12700
INK = '#282A30'; BODY = '#535353'; GREY = '#757882'; BLUE = '#3E4FE0'; DEEP = '#1D2DB8'
PANEL = '#F4F5FD'; LAV = '#E8EAF5'; LINE = '#E2E3E6'; WHITE = '#FFFFFF'; GREEN = '#1F8A5B'; RED = '#C0392B'; DARK = '#282A30'
FONT = 'Titillium Web'; MONO = 'Roboto Mono'
INSET = 7.2
SA_KEY = os.path.expanduser('~/.config/gsuite/sa.json')

def svc():
    c = service_account.Credentials.from_service_account_file(SA_KEY, scopes=['https://www.googleapis.com/auth/presentations', 'https://www.googleapis.com/auth/drive'])
    return build('slides', 'v1', credentials=c, cache_discovery=False)

def drive():
    c = service_account.Credentials.from_service_account_file(SA_KEY, scopes=['https://www.googleapis.com/auth/drive'])
    return build('drive', 'v3', credentials=c, cache_discovery=False)

def rgb(h):
    h = h.lstrip('#'); return {'red': int(h[0:2], 16) / 255, 'green': int(h[2:4], 16) / 255, 'blue': int(h[4:6], 16) / 255}

def run(s, pid, reqs, label=''):
    if not reqs: print(f'  {label}: 0 requests'); return
    for i in range(0, len(reqs), 300):
        part = reqs[i:i + 300]
        for a in range(6):
            try:
                s.presentations().batchUpdate(presentationId=pid, body={'requests': part}).execute(); break
            except Exception as e:
                if ('429' in str(e) or 'Quota' in str(e)) and a < 5: time.sleep(25); continue
                raise
    print(f'  {label}: {len(reqs)} requests')

def txt(el):
    return ''.join(te.get('textRun', {}).get('content', '') for te in el.get('shape', {}).get('text', {}).get('textElements', []))

def walk(els):
    for e in els:
        if 'elementGroup' in e: yield from walk(e['elementGroup']['children'])
        else: yield e

def slide(P, sid):
    return next(x for x in P['slides'] if x['objectId'] == sid)

# ------------------------------------------------------------------ drawing primitives
class Page:
    def __init__(self, sid, prefix=None):
        self.sid = sid; self.R = []; self.n = 0; self.prefix = prefix or sid
    def _id(self):
        self.n += 1; return f'{self.prefix}_k{self.n:03d}'
    def shape(self, x, y, w, h, kind='RECTANGLE', fill=None, line=None, lw=0.75, oid=None):
        oid = oid or self._id()
        self.R.append({'createShape': {'objectId': oid, 'shapeType': kind, 'elementProperties': {'pageObjectId': self.sid,
            'size': {'width': {'magnitude': w * PT, 'unit': 'EMU'}, 'height': {'magnitude': h * PT, 'unit': 'EMU'}},
            'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': x * PT, 'translateY': y * PT, 'unit': 'EMU'}}}})
        p = {}; f = []
        if fill: p['shapeBackgroundFill'] = {'solidFill': {'color': {'rgbColor': rgb(fill)}}}; f.append('shapeBackgroundFill.solidFill.color')
        else: p['shapeBackgroundFill'] = {'propertyState': 'NOT_RENDERED'}; f.append('shapeBackgroundFill.propertyState')
        if line: p['outline'] = {'outlineFill': {'solidFill': {'color': {'rgbColor': rgb(line)}}}, 'weight': {'magnitude': lw, 'unit': 'PT'}}; f += ['outline.outlineFill.solidFill.color', 'outline.weight']
        else: p['outline'] = {'propertyState': 'NOT_RENDERED'}; f.append('outline.propertyState')
        self.R.append({'updateShapeProperties': {'objectId': oid, 'shapeProperties': p, 'fields': ','.join(f)}})
        return oid
    def card(self, x, y, w, h, fill=WHITE, line=LINE, lw=0.75):
        return self.shape(x, y, w, h, 'ROUND_RECTANGLE' if h <= 60 else 'RECTANGLE', fill, line, lw)
    def line(self, x1, y1, x2, y2, color=LINE, w=1, arrow=False):
        oid = self._id()
        self.R.append({'createLine': {'objectId': oid, 'lineCategory': 'STRAIGHT', 'elementProperties': {'pageObjectId': self.sid,
            'size': {'width': {'magnitude': max(abs(x2 - x1), 0.01) * PT, 'unit': 'EMU'}, 'height': {'magnitude': max(abs(y2 - y1), 0.01) * PT, 'unit': 'EMU'}},
            'transform': {'scaleX': 1 if x2 >= x1 else -1, 'scaleY': 1 if y2 >= y1 else -1, 'translateX': x1 * PT, 'translateY': y1 * PT, 'unit': 'EMU'}}}})
        lp = {'lineFill': {'solidFill': {'color': {'rgbColor': rgb(color)}}}, 'weight': {'magnitude': w, 'unit': 'PT'}}
        fl = 'lineFill.solidFill.color,weight'
        if arrow: lp['endArrow'] = 'FILL_ARROW'; fl += ',endArrow'
        self.R.append({'updateLineProperties': {'objectId': oid, 'lineProperties': lp, 'fields': fl}})
    def text(self, x, y, w, h, markup, size=10, color=BODY, weight=400, align='START', valign='TOP', font=FONT, ls=115, fill=None, line=None, kind='TEXT_BOX', bold_color=None, pad=True):
        """markup: '**bold**' segments use weight 600 (and bold_color). '\n' = new paragraph."""
        if pad: oid = self.shape(x - INSET, y - INSET, w + 2 * INSET, h + 2 * INSET, kind, fill, line)
        else: oid = self.shape(x, y, w, h, kind, fill, line)
        segs = [(p, i % 2 == 1) for i, p in enumerate(re.split(r'\*\*', markup)) if p]
        plain = ''.join(p for p, _ in segs)
        if not plain: return oid
        self.R.append({'insertText': {'objectId': oid, 'insertionIndex': 0, 'text': plain}})
        self.R.append({'updateTextStyle': {'objectId': oid, 'textRange': {'type': 'ALL'}, 'style': {
            'weightedFontFamily': {'fontFamily': font, 'weight': weight}, 'fontSize': {'magnitude': size, 'unit': 'PT'},
            'foregroundColor': {'opaqueColor': {'rgbColor': rgb(color)}}}, 'fields': 'weightedFontFamily,fontSize,foregroundColor'}})
        i = 0
        for p, b in segs:
            if b:
                st = {'weightedFontFamily': {'fontFamily': font, 'weight': 600}}; fl = 'weightedFontFamily'
                if bold_color: st['foregroundColor'] = {'opaqueColor': {'rgbColor': rgb(bold_color)}}; fl += ',foregroundColor'
                self.R.append({'updateTextStyle': {'objectId': oid, 'textRange': {'type': 'FIXED_RANGE', 'startIndex': i, 'endIndex': i + len(p)}, 'style': st, 'fields': fl}})
            i += len(p)
        self.R.append({'updateParagraphStyle': {'objectId': oid, 'textRange': {'type': 'ALL'}, 'style': {'alignment': align, 'lineSpacing': ls, 'spaceAbove': {'magnitude': 0, 'unit': 'PT'}, 'spaceBelow': {'magnitude': 0, 'unit': 'PT'}}, 'fields': 'alignment,lineSpacing,spaceAbove,spaceBelow'}})
        self.R.append({'updateShapeProperties': {'objectId': oid, 'shapeProperties': {'contentAlignment': valign}, 'fields': 'contentAlignment'}})
        return oid
    def label(self, x, y, w, t, color=GREY, size=8):
        return self.text(x, y, w, 12, t.upper(), size=size, color=color, weight=600)
    def pill(self, x, y, w, t, fill=BLUE, color=WHITE, size=8, h=14, line=None):
        oid = self.shape(x, y, w, h, 'ROUND_RECTANGLE', fill, line)
        self.R.append({'insertText': {'objectId': oid, 'insertionIndex': 0, 'text': t}})
        self.R.append({'updateTextStyle': {'objectId': oid, 'textRange': {'type': 'ALL'}, 'style': {'weightedFontFamily': {'fontFamily': FONT, 'weight': 600}, 'fontSize': {'magnitude': size, 'unit': 'PT'}, 'foregroundColor': {'opaqueColor': {'rgbColor': rgb(color)}}}, 'fields': 'weightedFontFamily,fontSize,foregroundColor'}})
        self.R.append({'updateParagraphStyle': {'objectId': oid, 'textRange': {'type': 'ALL'}, 'style': {'alignment': 'CENTER'}, 'fields': 'alignment'}})
        self.R.append({'updateShapeProperties': {'objectId': oid, 'shapeProperties': {'contentAlignment': 'MIDDLE'}, 'fields': 'contentAlignment'}})
        return oid
    def circle_num(self, x, y, n, d=20, fill=WHITE, color=BLUE, line=BLUE):
        self.shape(x, y, d, d, 'ELLIPSE', fill, line, 1)
        self.text(x - 10, y + d / 2 - 6, d + 20, 12, n, size=8, color=color, weight=600, align='CENTER')

# ------------------------------------------------------------------ slide scaffolding
def chrome_ids(P, sid):
    """Return element ids on slide sid that are chrome (bg, kicker, title, accent bar, page number, small logo)."""
    sl = slide(P, sid); keep = {}
    for el in sl['pageElements']:
        tr = el.get('transform', {}); x = tr.get('translateX', 0) / PT; y = tr.get('translateY', 0) / PT; t = txt(el).strip()
        if 'image' in el and x < 1 and y < 1: keep[el['objectId']] = 'bg'
        elif 'image' in el and x > 640 and y < 30: keep[el['objectId']] = 'logo'
        elif el.get('shape', {}).get('shapeType') == 'ROUND_RECTANGLE' and x < 25 and y < 60 and not t: keep[el['objectId']] = 'bar'
        elif t.isdigit() and x < 12 and y > 360: keep[el['objectId']] = 'pg'
        elif t and abs(y - 25) < 3 and x < 40: keep[el['objectId']] = 'kicker'
        elif t and abs(y - 41) < 3 and x < 40: keep[el['objectId']] = 'title'
        elif t and 26 < y < 80 and x < 40 and (el.get('size', {}).get('width', {}).get('magnitude', 0) / PT) * tr.get('scaleX', 1) > 400: keep[el['objectId']] = 'title'   # nudged by hand
    return keep

def new_slide(s, pid, P, base_sid, new_sid, kicker, title, pg=None):
    """Duplicate a content slide, keep only its chrome (background, kicker, title, accent bar, page number, logo)."""
    base = slide(P, base_sid)
    ids = {base_sid: new_sid}
    for el in base['pageElements']: ids[el['objectId']] = f"{new_sid}_{el['objectId'][-6:]}"
    run(s, pid, [{'duplicateObject': {'objectId': base_sid, 'objectIds': ids}}], f'dup {new_sid}')
    roles = chrome_ids(P, base_sid)
    reqs = []; kk = tt = None
    for el in base['pageElements']:
        nid = ids[el['objectId']]; role = roles.get(el['objectId'])
        if role == 'kicker': kk = nid; continue
        if role == 'title': tt = nid; continue
        if role in ('bg', 'logo', 'bar', 'pg'): continue
        reqs.append({'deleteObject': {'objectId': nid}})
    for oid, t in ((kk, kicker), (tt, title)):
        if oid: reqs += [{'deleteText': {'objectId': oid, 'textRange': {'type': 'ALL'}}}, {'insertText': {'objectId': oid, 'insertionIndex': 0, 'text': t}}]
    run(s, pid, reqs, f'clear {new_sid}')
    return Page(new_sid)

def clear_body(s, pid, P, sid, kicker=None, title=None):
    """Remove everything except chrome on an existing slide; optionally rewrite kicker/title. Returns a Page for new content."""
    roles = chrome_ids(P, sid); sl = slide(P, sid); reqs = []
    for el in sl['pageElements']:
        role = roles.get(el['objectId'])
        if role is None: reqs.append({'deleteObject': {'objectId': el['objectId']}})
    for role, t in (('kicker', kicker), ('title', title)):
        if t is None: continue
        oid = next((k for k, v in roles.items() if v == role), None)
        if oid: reqs += [{'deleteText': {'objectId': oid, 'textRange': {'type': 'ALL'}}}, {'insertText': {'objectId': oid, 'insertionIndex': 0, 'text': t}}]
    run(s, pid, reqs, f'clear body {sid}')
    return Page(sid, prefix=sid[:12] + '_n')

def set_text_el(el, markup, R):
    """Replace the whole text of element el, keeping its regular and bold run styles."""
    runs = [te['textRun'] for te in el['shape']['text']['textElements'] if 'textRun' in te and te['textRun']['content'].strip()]
    keep = ['fontFamily', 'weightedFontFamily', 'fontSize', 'foregroundColor', 'bold', 'italic']
    if not runs: runs = [{'style': {'weightedFontFamily': {'fontFamily': FONT, 'weight': 400}}}]
    reg = next((r['style'] for r in runs if (r['style'].get('weightedFontFamily', {}).get('weight', 400) < 600 and not r['style'].get('bold'))), runs[0]['style'])
    bld = next((r['style'] for r in runs if (r['style'].get('weightedFontFamily', {}).get('weight', 400) >= 600 or r['style'].get('bold'))), None)
    reg = {k: v for k, v in reg.items() if k in keep}
    bld = {k: v for k, v in (bld or dict(reg, weightedFontFamily={'fontFamily': FONT, 'weight': 600})).items() if k in keep}
    segs = [(p, i % 2 == 1) for i, p in enumerate(re.split(r'\*\*', markup)) if p]
    plain = ''.join(p for p, _ in segs); oid = el['objectId']
    R += [{'deleteText': {'objectId': oid, 'textRange': {'type': 'ALL'}}}, {'insertText': {'objectId': oid, 'insertionIndex': 0, 'text': plain}}]
    i = 0
    for p, b in segs:
        st = bld if b else reg
        if st: R.append({'updateTextStyle': {'objectId': oid, 'textRange': {'type': 'FIXED_RANGE', 'startIndex': i, 'endIndex': i + len(p)}, 'style': st, 'fields': ','.join(st.keys())}})
        i += len(p)
    return True

def set_text(P, sid, find, markup, R, exact=False):
    """Replace the whole text of the element on slide sid whose text contains `find` (first match)."""
    sl = slide(P, sid)
    cands = [e for e in walk(sl['pageElements']) if (txt(e).strip() == find if exact else find in txt(e))]
    if not cands: print(f'  set_text MISS: {find!r} on {sid}'); return False
    return set_text_el(cands[0], markup, R)

def set_text_id(P, sid, oid, markup, R):
    """Same as set_text but addressing the element by id."""
    sl = slide(P, sid)
    el = next((e for e in walk(sl['pageElements']) if e['objectId'] == oid), None)
    if el is None: print(f'  set_text_id MISS: {oid} on {sid}'); return False
    return set_text_el(el, markup, R)

def rep(sid, a, b):
    return {'replaceAllText': {'containsText': {'text': a, 'matchCase': True}, 'replaceText': b, 'pageObjectIds': [sid]}}

def set_notes(s, pid, P, sid, text):
    sl = slide(P, sid)
    np_ = sl.get('slideProperties', {}).get('notesPage', {})
    oid = np_.get('notesProperties', {}).get('speakerNotesObjectId')
    if not oid: print(f'  notes MISS on {sid}'); return []
    existing = ''
    for el in np_.get('pageElements', []):
        if el['objectId'] == oid: existing = txt(el)
    R = []
    if existing.strip(): R.append({'deleteText': {'objectId': oid, 'textRange': {'type': 'ALL'}}})
    R.append({'insertText': {'objectId': oid, 'insertionIndex': 0, 'text': text}})
    return R

def finish(s, pid, order):
    P = s.presentations().get(presentationId=pid).execute()
    live = [x['objectId'] for x in P['slides']]
    missing = [o for o in order if o not in live]
    if missing: raise SystemExit(f'missing slides {missing}')
    reqs = [{'updateSlidesPosition': {'slideObjectIds': [o], 'insertionIndex': i}} for i, o in enumerate(order)]
    reqs += [{'deleteObject': {'objectId': o}} for o in live if o not in order]
    run(s, pid, reqs, 'order and delete')
    P = s.presentations().get(presentationId=pid).execute(); pg = []
    for n, sl in enumerate(P['slides'], 1):
        for el in sl['pageElements']:
            tr = el.get('transform', {}); t = txt(el).strip()
            if t.isdigit() and tr.get('translateX', 0) / PT < 12 and tr.get('translateY', 0) / PT > 360 and t != str(n):
                pg += [{'deleteText': {'objectId': el['objectId'], 'textRange': {'type': 'ALL'}}}, {'insertText': {'objectId': el['objectId'], 'insertionIndex': 0, 'text': str(n)}}]
    if pg: run(s, pid, pg, 'page numbers')
    print('  final slides:', len(P['slides']))
    return P
