# -*- coding: utf-8 -*-
"""
gs_engine.py · Google Slides build engine for the OnlyFans token-vault deck.

Builds the deck natively inside the Google Slides copy of German's Eventbrite deck
(presentation 10A2GokDXPEPkeqqS29H7a460R6j5ux60nILIqUXmUKc) with the Slides API and the
service account ~/.config/gsuite/sa.json. Template slides are duplicated for their chrome
(background, kicker, headline, Yuno wordmark), everything else is drawn with primitives
in the template's own fonts and colours (see template_catalog.md). Spec format: SPEC_SCHEMA.md.

Usage
  python3 gs_engine.py build deck_spec.json            # append all slides (template kept)
  python3 gs_engine.py build deck_spec.json --final    # append all, then delete the 46 template slides
  python3 gs_engine.py build deck_spec.json --only s03,s07
  python3 gs_engine.py build deck_spec.json --only s03 --replace   # rebuild one slide in place (same position, old one deleted)
  python3 gs_engine.py check deck_spec.json                        # offline validation + fit check
  python3 gs_engine.py cleanup                          # delete every slide this engine appended (build_state.json)
  python3 gs_engine.py dump                             # presentations.get -> build/live_dump.json
"""
import json, os, re, sys, time, math, copy
from google.oauth2 import service_account
from googleapiclient.discovery import build as gbuild

HERE = os.path.dirname(os.path.abspath(__file__))
DEAD_PIDS = set()

def spec_pid(path=None):
    """presentation_id from deck_spec.json (the single switch point); --pid / OF_PID override it"""
    try: return json.load(open(path or os.path.join(HERE, 'deck_spec.json'))).get('presentation_id')
    except Exception: return None

PID = os.environ.get('OF_PID') or spec_pid()
SA = os.path.expanduser('~/.config/gsuite/sa.json')
TEMPLATE_DUMP = os.path.join(HERE, 'template_dump.json')
STATE = os.path.join(HERE, 'build_state.json')
LOGO_URL = 'https://drive.google.com/uc?export=download&id=1wVGCJ4_z9hEkR8aM59-S7KjlKH8EWnvI'  # Carry1st white wordmark, German's Drive, public
N_TEMPLATE = 46
LOGO_ASPECT = 640 / 162   # Carry1st white wordmark (w / h); the template box was cut for a 5.72 logo

PT = 12700
PAGE_W, PAGE_H = 720.0, 405.0
X0, W0 = 36.0, 648.0          # template side margin and full content width
ZONE_Y, ZONE_H = 95.0, 270.0  # content zone (y 95 .. 365); headline block ends at ~85
INSET_X, INSET_Y = 7.2, 7.2   # Google Slides default text insets on API-created shapes (compensated in text()); calibrated
CELL_PAD = 7.2                # native table cell padding (measured)
MIN_FONT = 6.5
FONT, MONO = 'Geist', 'Geist Mono'

# ---------------------------------------------------------------- palette (hex as the template stores them)
INK, BLACK, WHITE = '#121212', '#000000', '#FFFFFF'
GREY, MUTED, BODY2, BODY3 = '#767676', '#4A4A4A', '#2A2A2A', '#3C3C3C'
BLUE, DEEP, BRAND, LBLUE, LBLUE2, PALE = '#344FE0', '#1227AD', '#3E4FE0', '#7C89EF', '#5967E4', '#BDC3F6'
PANEL, PANEL2, PANEL3, BAND, TILE_OUT = '#E8EAF5', '#F6F7FB', '#F4F5FD', '#E5E7EF', '#B0B7F2'
DARK, DARK2, ONDARK, ONDARK2 = '#282A30', '#161616', '#D6DAF9', '#9A9CA3'
GREEN = '#1F8A5B'
PILLS = {  # label: (text colour, fill)
    'CONFIRMED': ('#1F8A5B', '#E2F3EB'),
    'BETA': ('#424449', '#EFF0F2'),
    'PUBLIC DOCS': ('#3E4FE0', '#E8EAF5'),
    'OPEN': ('#9A5B00', '#FBEFD9'),
    'NOT IN DOCS': ('#424449', '#EFF0F2'),
    'DIRECTION': ('#424449', '#D5D9F5'),
    'ESTIMATE': ('#5B3FA0', '#EEE9F8'),   # modeled figure, assumption stated (Carry1st deck, 15 Oct 2026)
}
STATE_GLYPH = {'open': ('✕', GREY), 'partial': ('◐', LBLUE), 'closed': ('✓', BLUE)}

# ---------------------------------------------------------------- template anatomy (object ids inside template_dump.json)
BASE = {
    'cover': 1, 'agenda': 2, 'divider': 3, 'white': 7, 'dark': 22, 'closing': 46,
}
KEEP = {  # template slide -> element ids kept after duplication (everything else on the slide is deleted)
    1: ['g3f77215683c_1_527', 'g3f77215683c_1_533'],                         # title, lockup group
    2: ['g3f769a0f446_0_19', 'g3f769a0f446_0_20', 'g3f769a0f446_0_21'],      # hairline, AGENDA kicker, wordmark
    3: None,                                                                 # divider: keep all
    7: ['g3f77215683c_2_3005', 'g3f77215683c_2_3006', 'g3f77215683c_2_2969'],  # kicker, headline, wordmark
    22: ['g3f769a0f446_0_14189', 'g3f769a0f446_0_14191', 'g3f769a0f446_0_14192',
         'g3f769a0f446_0_14193', 'g3f769a0f446_0_14194'],                     # bg image, hairline, kicker, wordmark, headline
    46: ['g3c99cf7678e_0_45', 'g3c99cf7678e_0_46'],                          # title + body placeholders
}
ROLE = {  # template element ids by role, per base
    1: {'title': 'g3f77215683c_1_527', 'logo': 'g3f77215683c_1_528', 'wordmark': 'g3f77215683c_1_529'},
    2: {'kicker': 'g3f769a0f446_0_20', 'wordmark': 'g3f769a0f446_0_21', 'hairline': 'g3f769a0f446_0_19'},
    3: {'num': 'g3f769a0f446_0_994', 'title': 'g3f769a0f446_0_993', 'wordmark': 'g3f769a0f446_0_990'},
    7: {'kicker': 'g3f77215683c_2_3005', 'headline': 'g3f77215683c_2_3006', 'wordmark': 'g3f77215683c_2_2969'},
    22: {'kicker': 'g3f769a0f446_0_14192', 'headline': 'g3f769a0f446_0_14194', 'wordmark': 'g3f769a0f446_0_14193'},
    46: {'title': 'g3c99cf7678e_0_45', 'body': 'g3c99cf7678e_0_46', 'icon': 'g3f7485aa48e_0_2'},
}
SPACEX_LOGO = 'g3f76accd9b2_0_4'  # template slide 25, trusted-by wall

# ================================================================= geometry + text metrics
def emu(pt): return int(round(pt * PT))
def rgb(hexstr):
    h = hexstr.lstrip('#'); return {'red': int(h[0:2], 16) / 255, 'green': int(h[2:4], 16) / 255, 'blue': int(h[4:6], 16) / 255}
def solid(hexstr, alpha=None):
    f = {'color': {'rgbColor': rgb(hexstr)}}
    if alpha is not None: f['alpha'] = alpha
    return {'solidFill': f}

_NARROW = set("iljtfr.,:;'|!I ()[]{}·-")
_WIDE = set("mwMW@%")
def text_width(s, size, bold=False):
    """Estimated rendered width in pt for Geist (calibrated against thumbnails)."""
    w = 0.0
    for ch in s:
        if ch in _NARROW: w += 0.30
        elif ch in _WIDE: w += 0.82
        elif ch.isupper(): w += 0.64
        elif ch.isdigit(): w += 0.56
        else: w += 0.53
    return w * size * (1.07 if bold else 1.0)

def wrap_count(text, size, width, bold=False):
    """Number of rendered lines for text (paragraphs split on \\n) in a box `width` pt wide (visual width, insets excluded)."""
    text = re.sub(r'\*\*', '', text or '')
    lines = 0
    for para in text.split('\n'):
        words = para.split(' ')
        cur = 0.0; n = 1
        for wd in words:
            ww = text_width(wd + ' ', size, bold)
            if cur + ww > width and cur > 0:
                n += 1; cur = ww
            else:
                cur += ww
        lines += n
    return lines

def text_h(text, size, width, ls=115, bold=False):
    return wrap_count(text, size, width, bold) * size * 1.21 * ls / 100.0 + 1.0

def mono_h(code, size, ls=130):
    return (code.count('\n') + 1) * size * 1.21 * ls / 100.0 + 2

class FitError(Exception): pass

# ================================================================= API plumbing
def service():
    creds = service_account.Credentials.from_service_account_file(SA, scopes=['https://www.googleapis.com/auth/presentations'])
    return gbuild('slides', 'v1', credentials=creds, cache_discovery=False)

def run(svc, pid, reqs, chunk=300, label=''):
    done = 0
    for i in range(0, len(reqs), chunk):
        part = reqs[i:i + chunk]
        for attempt in range(4):
            try:
                svc.presentations().batchUpdate(presentationId=pid, body={'requests': part}).execute(); break
            except Exception as e:
                msg = str(e)
                if attempt == 3 or ('400' in msg and 'rateLimit' not in msg and 'Internal' not in msg and 'createImage' not in msg and 'image' not in msg.lower()):
                    raise
                print(f"  retry {attempt + 1} on chunk {i} ({label}): {msg[:140]}"); time.sleep(3 + 3 * attempt)
        done += len(part)
    print(f"  applied {done:4d} requests {label}")

def compose(a, b):
    sx = a.get('scaleX', 1) * b.get('scaleX', 1) + a.get('shearX', 0) * b.get('shearY', 0)
    sy = a.get('shearY', 0) * b.get('shearX', 0) + a.get('scaleY', 1) * b.get('scaleY', 1)
    tx = a.get('scaleX', 1) * b.get('translateX', 0) + a.get('shearX', 0) * b.get('translateY', 0) + a.get('translateX', 0)
    ty = a.get('shearY', 0) * b.get('translateX', 0) + a.get('scaleY', 1) * b.get('translateY', 0) + a.get('translateY', 0)
    return {'scaleX': sx, 'scaleY': sy, 'translateX': tx, 'translateY': ty}

def elements(slide):
    """flat list of (element, absolute transform) including group children"""
    out = []
    def walk(el, par=None):
        tr = el.get('transform', {})
        if par: tr = compose(par, tr)
        if 'elementGroup' in el:
            for ch in el['elementGroup']['children']: walk(ch, tr)
        else: out.append((el, tr))
    for el in slide.get('pageElements', []): walk(el)
    return out

def all_ids(slide):
    ids = []
    def walk(el):
        ids.append(el['objectId'])
        if 'elementGroup' in el:
            for ch in el['elementGroup']['children']: walk(ch)
    for el in slide.get('pageElements', []): walk(el)
    return ids

def text_of(el):
    if 'shape' in el and 'text' in el['shape']:
        return ''.join(te.get('textRun', {}).get('content', '') for te in el['shape']['text'].get('textElements', []))
    return ''

def geom(el, tr):
    sz = el.get('size', {})
    return (tr.get('translateX', 0) / PT, tr.get('translateY', 0) / PT,
            sz.get('width', {}).get('magnitude', 0) * tr.get('scaleX', 1) / PT,
            sz.get('height', {}).get('magnitude', 0) * tr.get('scaleY', 1) / PT)

TEXT_FIELDS = ['bold', 'italic', 'underline', 'fontSize', 'foregroundColor', 'fontFamily', 'weightedFontFamily', 'baselineOffset', 'smallCaps', 'strikethrough']
PARA_FIELDS = ['alignment', 'lineSpacing', 'spaceAbove', 'spaceBelow', 'indentStart', 'indentEnd', 'indentFirstLine', 'direction', 'spacingMode']

def paragraphs(el):
    paras = []; cur = None
    for te in el['shape']['text'].get('textElements', []):
        if 'paragraphMarker' in te:
            cur = {'text': '', 'style': None, 'pstyle': te['paragraphMarker'].get('style', {}), 'bullet': te['paragraphMarker'].get('bullet')}
            paras.append(cur)
        elif 'textRun' in te and cur is not None:
            cur['text'] += te['textRun'].get('content', '')
            if cur['style'] is None and te['textRun'].get('content', '').strip():
                cur['style'] = te['textRun'].get('style', {})
    for p in paras:
        if p['style'] is None: p['style'] = {}
    return paras

def _runs(el):
    return [(te['textRun']['content'], {k: v for k, v in te['textRun'].get('style', {}).items() if k in TEXT_FIELDS})
            for te in el['shape']['text'].get('textElements', []) if 'textRun' in te and te['textRun'].get('content', '').strip()]

def _segments(markup):
    """'plain **bold** plain' -> [(text, is_bold)]"""
    segs = []
    for i, part in enumerate(re.split(r'\*\*', markup)):
        if part: segs.append((part, i % 2 == 1))
    return segs

def replace_text_requests(el, new_text, size=None, color=None):
    """Delete all text of an existing shape, insert new_text, re-apply the original per-paragraph styles.
    **bold** segments take the original bold run style (or the regular style + bold). Optional size/colour override."""
    oid = el['objectId']; new_text = new_text.rstrip('\n')
    paras = paragraphs(el); rr = _runs(el)
    reg = next((s for c, s in rr if not s.get('bold')), None); bold = next((s for c, s in rr if s.get('bold')), None)
    if reg is None and bold is None: reg = bold = {}
    if reg is None: reg = bold                     # all-bold original (headlines): plain text stays bold
    if bold is None: bold = dict(reg); bold['bold'] = True; bold['weightedFontFamily'] = {'fontFamily': reg.get('weightedFontFamily', {}).get('fontFamily', FONT), 'weight': 700}
    segs = _segments(new_text); plain = ''.join(t for t, b in segs)
    reqs = []
    if text_of(el).strip('\n'): reqs.append({'deleteText': {'objectId': oid, 'textRange': {'type': 'ALL'}}})
    reqs.append({'insertText': {'objectId': oid, 'insertionIndex': 0, 'text': plain}})
    i = 0
    for t, b in segs:
        st = dict(bold if b else reg)
        if size: st['fontSize'] = {'magnitude': size, 'unit': 'PT'}
        if color: st['foregroundColor'] = {'opaqueColor': {'rgbColor': rgb(color)}}
        st = {k: v for k, v in st.items() if k in TEXT_FIELDS}
        if st:
            reqs.append({'updateTextStyle': {'objectId': oid, 'textRange': {'type': 'FIXED_RANGE', 'startIndex': i, 'endIndex': i + len(t)}, 'style': st, 'fields': ','.join(st.keys())}})
        i += len(t)
    # paragraph styles: paragraph n of the new text takes paragraph n (or last) of the original
    nonempty = [p for p in paras if p['text'].strip()] or paras
    start = 0
    for n, line in enumerate(plain.split('\n')):
        end = start + len(line)
        src = nonempty[min(n, len(nonempty) - 1)] if nonempty else None
        if src and end > start:
            ps = {k: v for k, v in src['pstyle'].items() if k in PARA_FIELDS}
            if ps: reqs.append({'updateParagraphStyle': {'objectId': oid, 'textRange': {'type': 'FIXED_RANGE', 'startIndex': start, 'endIndex': end}, 'style': ps, 'fields': ','.join(ps.keys())}})
        start = end + 1
    return reqs

# ================================================================= the deck
class Deck:
    def __init__(self, pid=None, sa=SA):
        self.pid = os.environ.get('OF_PID') or pid or PID
        if not self.pid: raise SystemExit('no presentation id: set "presentation_id" in deck_spec.json or pass --pid')
        if self.pid in DEAD_PIDS: raise SystemExit(f'refusing to touch {self.pid}: that presentation was emptied; use the fresh copy id from deck_spec.json')
        self.svc = service()
        self.tpl = json.load(open(TEMPLATE_DUMP))
        self.tpl_slides = self.tpl['slides']
        self.pres = None
        self.state = json.load(open(STATE)) if os.path.exists(STATE) else {}
        if self.state.get('pid') != self.pid:          # state is per presentation; ids from another file are meaningless here
            self.state = {'pid': self.pid, 'built': []}

    # ---- fetch
    def fetch(self):
        self.pres = self.svc.presentations().get(presentationId=self.pid).execute(); return self.pres
    def slide_ids(self):
        p = self.svc.presentations().get(presentationId=self.pid, fields='slides(objectId)').execute()
        return [s['objectId'] for s in p.get('slides', [])]
    def page(self, page_id):
        return self.svc.presentations().pages().get(presentationId=self.pid, pageObjectId=page_id).execute()
    def notes_shape(self, slide_id):
        """(speaker notes shape id, has_text) for a slide, fetched fresh"""
        p = self.svc.presentations().get(presentationId=self.pid, fields='slides(objectId,slideProperties.notesPage(notesProperties,pageElements))').execute()
        for s in p['slides']:
            if s['objectId'] == slide_id:
                np_ = s['slideProperties']['notesPage']; sid = np_['notesProperties']['speakerNotesObjectId']
                has = any(e['objectId'] == sid and text_of(e).strip() for e in np_.get('pageElements', []))
                return sid, has
        raise KeyError(slide_id)
    def run(self, reqs, label=''):
        if reqs: run(self.svc, self.pid, reqs, label=label)
    def save_state(self):
        json.dump(self.state, open(STATE, 'w'), indent=1)

    # ---- duplication
    def duplicate(self, template_index, tag):
        """Duplicate template slide (1-based index in template_dump order) with deterministic ids `tag_<oldid>`,
        move it to the end of the deck. Returns (new_slide_id, idmap old->new)."""
        src = self.tpl_slides[template_index - 1]
        ids = [src['objectId']] + all_ids(src)
        idmap = {i: f"{tag}_{i}"[:50] for i in ids}
        new_id = idmap[src['objectId']]
        n = len(self.slide_ids())
        self.run([{'duplicateObject': {'objectId': src['objectId'], 'objectIds': idmap}},
                  {'updateSlidesPosition': {'slideObjectIds': [new_id], 'insertionIndex': n + 1}}], f'duplicate t{template_index} -> {new_id}')
        self.state['built'].append(new_id); self.save_state()
        return new_id, idmap

    def delete_slides(self, slide_ids):
        self.run([{'deleteObject': {'objectId': s}} for s in slide_ids], f'delete {len(slide_ids)} slides')

    def template_live_ids(self):
        """ids of the 46 original template slides still present"""
        live = set(self.slide_ids())
        return [s['objectId'] for s in self.tpl_slides if s['objectId'] in live]

    def set_notes(self, slide_id, text):
        sid, has = self.notes_shape(slide_id)
        reqs = []
        if has: reqs.append({'deleteText': {'objectId': sid, 'textRange': {'type': 'ALL'}}})
        if text and text.strip():
            reqs.append({'insertText': {'objectId': sid, 'insertionIndex': 0, 'text': text.strip()}})
            reqs.append({'updateTextStyle': {'objectId': sid, 'textRange': {'type': 'ALL'}, 'style': {'fontSize': {'magnitude': 11, 'unit': 'PT'}, 'weightedFontFamily': {'fontFamily': 'Arial', 'weight': 400}}, 'fields': 'fontSize,weightedFontFamily'}})
        self.run(reqs, f'notes {slide_id}')

    def wordmark_url(self):
        """fresh contentUrl of the white yuno wordmark on the template cover (lives ~30 min)"""
        return self.chrome_image_url('g3f77215683c_1_529')
    def chrome_image_url(self, suffix):
        """live contentUrl of any image whose id ends with a template id (works on duplicates too, e.g. the blue wordmark _2969)"""
        if not self.pres: self.fetch()
        for s in self.pres['slides']:
            for el, tr in elements(s):
                if el['objectId'].endswith(suffix) and 'image' in el:
                    return el['image']['contentUrl']
        if suffix.endswith('_2969'):   # template gone: use the wordmark drawn on any rebuilt white slide (x~645, y~24 pt)
            for s in self.pres['slides']:
                for el, tr in elements(s):
                    if 'image' in el and abs(tr.get('translateX', 0) / 12700 - 645) < 4 and abs(tr.get('translateY', 0) / 12700 - 24) < 4:
                        return el['image']['contentUrl']
        return None
    def has_template(self):
        if not hasattr(self, '_has_tpl'): self._has_tpl = len(self.template_live_ids()) == N_TEMPLATE
        return self._has_tpl
    def create_blank(self, tag, layout='g3f77215683c_2_1907'):
        """template-free white content slide: the content layout survives template deletion, so a blank slide on it
        plus the chrome drawn by SB.chrome_blank() is a faithful stand-in for a duplicate of template slide 7"""
        sid = f"{tag}_g3f77215683c_2_2968"
        # no insertionIndex: the API appends atomically, so concurrent workers cannot race on the slide count
        self.run([{'createSlide': {'objectId': sid, 'slideLayoutReference': {'layoutId': layout}}}], f'blank slide {sid}')
        self.state['built'].append(sid); self.save_state()
        return sid

# ================================================================= per-slide builder (request factory)
class SB:
    """Collects requests for one slide. All coordinates are visual pt; text() compensates the API text insets."""
    def __init__(self, deck, page_id, tag, idmap=None, dark=False):
        self.deck, self.page, self.tag, self.idmap, self.dark = deck, page_id, tag, idmap or {}, dark
        self.R = []; self.n = 0; self.post = []   # post: callables run after a flush (need a fetch)
        self.min_font = 99
        self.zy, self.zh = ZONE_Y, ZONE_H          # content zone top / height (moved down when the headline takes 3 lines)
        self.table_h = 0
    def nid(self):
        self.n += 1; return f"{self.tag}_e{self.n:03d}"
    def flush(self, label=''):
        self.deck.run(self.R, label or self.tag); self.R = []
        for fn in self.post: fn()
        self.post = []
        if self.R: self.deck.run(self.R, (label or self.tag) + ' post'); self.R = []
    def mapped(self, old): return self.idmap.get(old, old)

    # ---- element ops
    def delete(self, ids):
        for i in ids: self.R.append({'deleteObject': {'objectId': i}})
    def delete_all_but(self, template_index, keep):
        src = self.deck.tpl_slides[template_index - 1]
        keep = set(keep or [])
        for el in src.get('pageElements', []):
            if el['objectId'] not in keep: self.R.append({'deleteObject': {'objectId': self.mapped(el['objectId'])}})
    def move(self, oid, x, y, w=None, h=None, size=None):
        """absolute reposition; w/h require the element's native size (pass size=(w_emu,h_emu))"""
        tr = {'scaleX': 1, 'scaleY': 1, 'shearX': 0, 'shearY': 0, 'translateX': emu(x), 'translateY': emu(y), 'unit': 'EMU'}
        if w is not None and size:
            tr['scaleX'] = w * PT / size[0]; tr['scaleY'] = h * PT / size[1]
        self.R.append({'updatePageElementTransform': {'objectId': oid, 'transform': tr, 'applyMode': 'ABSOLUTE'}})

    # ---- primitives
    def shape(self, kind, x, y, w, h, fill=None, outline=None, outline_w=0.375, valign='TOP', alpha=None):
        oid = self.nid()
        self.R.append({'createShape': {'objectId': oid, 'shapeType': kind, 'elementProperties': {'pageObjectId': self.page,
            'size': {'width': {'magnitude': emu(max(w, 0.1)), 'unit': 'EMU'}, 'height': {'magnitude': emu(max(h, 0.1)), 'unit': 'EMU'}},
            'transform': {'scaleX': 1, 'scaleY': 1, 'shearX': 0, 'shearY': 0, 'translateX': emu(x), 'translateY': emu(y), 'unit': 'EMU'}}}})
        props = {'contentAlignment': valign}; fields = ['contentAlignment']
        if fill: props['shapeBackgroundFill'] = solid(fill, alpha); fields.append('shapeBackgroundFill.solidFill')
        else: props['shapeBackgroundFill'] = {'propertyState': 'NOT_RENDERED'}; fields.append('shapeBackgroundFill.propertyState')
        if outline:
            props['outline'] = {'outlineFill': solid(outline), 'weight': {'magnitude': emu(outline_w), 'unit': 'EMU'}, 'dashStyle': 'SOLID'}
            fields += ['outline.outlineFill.solidFill', 'outline.weight', 'outline.dashStyle']
        else: props['outline'] = {'propertyState': 'NOT_RENDERED'}; fields.append('outline.propertyState')
        self.R.append({'updateShapeProperties': {'objectId': oid, 'shapeProperties': props, 'fields': ','.join(fields)}})
        return oid
    def rect(self, x, y, w, h, fill=None, outline=None, outline_w=0.375, alpha=None):
        return self.shape('RECTANGLE', x, y, w, h, fill, outline, outline_w, alpha=alpha)
    def round_rect(self, x, y, w, h, fill=None, outline=None, outline_w=0.375):
        return self.shape('ROUND_RECTANGLE', x, y, w, h, fill, outline, outline_w)
    def hairline(self, x, y, w, color=None, alpha=None):
        color = color or (WHITE if self.dark else DEEP); alpha = alpha if alpha is not None else (0.18 if self.dark else 0.1216)
        return self.rect(x, y, w, 0.4, fill=color, alpha=alpha)
    def vline(self, x, y, h, color=None, alpha=None):
        color = color or (WHITE if self.dark else DEEP); alpha = alpha if alpha is not None else (0.13 if self.dark else 0.1216)
        return self.rect(x, y, 0.4, h, fill=color, alpha=alpha)
    def line(self, x1, y1, x2, y2, color=LBLUE, weight=0.75, end_arrow=True, dash=None):
        oid = self.nid(); dx, dy = x2 - x1, y2 - y1
        self.R.append({'createLine': {'objectId': oid, 'lineCategory': 'STRAIGHT', 'elementProperties': {'pageObjectId': self.page,
            'size': {'width': {'magnitude': max(emu(abs(dx)), 1), 'unit': 'EMU'}, 'height': {'magnitude': max(emu(abs(dy)), 1), 'unit': 'EMU'}},
            'transform': {'scaleX': -1 if dx < 0 else 1, 'scaleY': -1 if dy < 0 else 1, 'shearX': 0, 'shearY': 0,
                          'translateX': emu(x1), 'translateY': emu(y1), 'unit': 'EMU'}}}})
        lp = {'lineFill': solid(color), 'weight': {'magnitude': emu(weight), 'unit': 'EMU'}, 'endArrow': 'FILL_ARROW' if end_arrow else 'NONE', 'startArrow': 'NONE'}
        fields = 'lineFill,weight,endArrow,startArrow'
        if dash: lp['dashStyle'] = dash; fields += ',dashStyle'
        self.R.append({'updateLineProperties': {'objectId': oid, 'lineProperties': lp, 'fields': fields}})
        return oid
    def image(self, url, x, y, w, h):
        oid = self.nid()
        self.R.append({'createImage': {'objectId': oid, 'url': url, 'elementProperties': {'pageObjectId': self.page,
            'size': {'width': {'magnitude': emu(w), 'unit': 'EMU'}, 'height': {'magnitude': emu(h), 'unit': 'EMU'}},
            'transform': {'scaleX': 1, 'scaleY': 1, 'shearX': 0, 'shearY': 0, 'translateX': emu(x), 'translateY': emu(y), 'unit': 'EMU'}}}})
        return oid
    def replace_image(self, image_id, url, method='CENTER_INSIDE'):
        self.R.append({'replaceImage': {'imageObjectId': image_id, 'url': url, 'imageReplaceMethod': method}})

    def text(self, x, y, w, h, content, size=9, bold=False, color=None, align='START', valign='TOP', ls=115,
             font=FONT, inset=True, space_below=0, space_above=0, italic=False, oid=None, caps=False):
        """content: str with \\n paragraphs and **bold** markup, or list of (text, size, bold, color[, font]) runs.
        (x,y,w,h) is the visual box; the shape is enlarged by the default insets so the text starts exactly at x,y."""
        color = color or (WHITE if self.dark else INK)
        if isinstance(content, str):
            if caps: content = content.upper()
            segs = [(t, size, b, color, font) for t, b in _segments(content)]
        else:
            segs = [(r[0], r[1], r[2], r[3], r[4] if len(r) > 4 else font) for r in content]
        plain = ''.join(s[0] for s in segs)
        if not plain: return None
        for s in segs: self.min_font = min(self.min_font, s[1])
        oid = oid or self.nid()
        sx, sy, sw, sh = (x - INSET_X, y - INSET_Y, w + 2 * INSET_X, h + 2 * INSET_Y) if inset else (x, y, w, h)
        self.R.append({'createShape': {'objectId': oid, 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': self.page,
            'size': {'width': {'magnitude': emu(sw), 'unit': 'EMU'}, 'height': {'magnitude': emu(max(sh, 1)), 'unit': 'EMU'}},
            'transform': {'scaleX': 1, 'scaleY': 1, 'shearX': 0, 'shearY': 0, 'translateX': emu(sx), 'translateY': emu(sy), 'unit': 'EMU'}}}})
        self.R.append({'updateShapeProperties': {'objectId': oid, 'shapeProperties': {'contentAlignment': valign, 'autofit': {'autofitType': 'NONE'}}, 'fields': 'contentAlignment,autofit.autofitType'}})
        self.R.append({'insertText': {'objectId': oid, 'insertionIndex': 0, 'text': plain}})
        i = 0
        for t, sz, b, c, f in segs:
            isb = bool(b) or bool(bold)   # markup **bold** segments, or the whole box when bold=True
            st = {'weightedFontFamily': {'fontFamily': f, 'weight': 700 if isb else 400}, 'bold': isb, 'italic': italic,
                  'fontSize': {'magnitude': sz, 'unit': 'PT'}, 'foregroundColor': {'opaqueColor': {'rgbColor': rgb(c)}}}
            self.R.append({'updateTextStyle': {'objectId': oid, 'textRange': {'type': 'FIXED_RANGE', 'startIndex': i, 'endIndex': i + len(t)},
                                               'style': st, 'fields': 'weightedFontFamily,bold,italic,fontSize,foregroundColor'}})
            i += len(t)
        ps = {'alignment': align, 'lineSpacing': ls, 'spaceAbove': {'magnitude': space_above, 'unit': 'PT'}, 'spaceBelow': {'magnitude': space_below, 'unit': 'PT'},
              'indentStart': {'magnitude': 0, 'unit': 'PT'}, 'indentFirstLine': {'magnitude': 0, 'unit': 'PT'}}
        self.R.append({'updateParagraphStyle': {'objectId': oid, 'textRange': {'type': 'ALL'}, 'style': ps, 'fields': 'alignment,lineSpacing,spaceAbove,spaceBelow,indentStart,indentFirstLine'}})
        return oid

    def pill(self, x, y, label, h=14.0, size=7.0, right=False):
        """Status pill (CONFIRMED / BETA / PUBLIC DOCS / OPEN / NOT IN DOCS). Returns (x_left, width)."""
        raw = (label or '').strip(); label = raw.upper()
        if label in PILLS: fg, bg = PILLS[label]
        else: fg, bg, label = DEEP, PANEL, raw          # free text chip (e.g. "Rules set by OnlyFans"): blue on light panel
        w = text_width(label, size, True) + 12
        if right: x = x - w
        self.round_rect(x, y, w, h, fill=bg)
        self.text(x, y + (h - size * 1.21) / 2 - 0.5, w, size * 1.3, label, size=size, bold=True, color=fg, align='CENTER', ls=100)
        return x, w
    def pills(self, labels, x_right, y, gap=4):
        """row of pills right-aligned to x_right"""
        x = x_right
        for lab in reversed(labels or []):
            x, w = self.pill(x, y, lab, right=True); x -= gap
        return x

    # ---- slide furniture
    def kicker(self, text, base):
        oid = self.mapped(ROLE[base]['kicker'])
        el = self._tpl_el(base, ROLE[base]['kicker'])
        self.R += replace_text_requests(el, (text or '').upper(), size=7, color=(WHITE if self.dark else GREY))
        self.min_font = min(self.min_font, 7)
    def headline(self, text, base, slide_id='?'):
        el = self._tpl_el(base, ROLE[base]['headline'])
        text = text or ''
        width = 602.6 if base == 7 else 600
        if wrap_count(text, 20, width, True) <= 2: size, lines = 20, wrap_count(text, 20, width, True)
        elif wrap_count(text, 18, width, True) <= 2: size, lines = 18, 2
        elif wrap_count(text, 18, width, True) == 3: size, lines = 18, 3
        else: raise FitError(f"slide {slide_id}: headline needs more than three lines at 18 pt: {text!r}")
        self.R += replace_text_requests(el, text, size=size, color=(WHITE if self.dark else BLACK))
        if lines == 3:
            self.move(self.mapped(ROLE[base]['headline']), 36, 41.1, 602.6, 64, size=(el['size']['width']['magnitude'], el['size']['height']['magnitude']))
            self.zy, self.zh = 112.0, 253.0
        if base == 22:  # dark base headline box is narrow (249 pt) and lower; widen and lift it to the white rhythm
            self.move(self.mapped(ROLE[base]['headline']), 36, 41.1, 602.6, 43.6, size=(el['size']['width']['magnitude'], el['size']['height']['magnitude']))
    def _tpl_el(self, base, oid):
        """copy of a template element with its objectId mapped to this slide's duplicate (never target the template itself)"""
        src = self.deck.tpl_slides[base - 1]
        for el, tr in elements(src):
            if el['objectId'] == oid:
                el = copy.deepcopy(el); el['objectId'] = self.mapped(oid); return el
        raise KeyError(oid)
    def headline_fit(self, text, slide_id='?', width=602.6):
        if wrap_count(text, 20, width, True) <= 2: return 20, wrap_count(text, 20, width, True)
        if wrap_count(text, 18, width, True) <= 2: return 18, 2
        if wrap_count(text, 18, width, True) == 3: return 18, 3
        raise FitError(f"slide {slide_id}: headline needs more than three lines at 18 pt: {text!r}")
    def chrome_blank(self, kicker, headline, slide_id, wm_url):
        """kicker, headline and wordmark at the template's measured positions (kicker glyph top 27.7, headline glyph top 45.7)"""
        self.text(X0, 26.2, 500, 10, (kicker or '').upper(), size=7, color=GREY, ls=125); self.min_font = min(self.min_font, 7)
        size, lines = self.headline_fit(headline or '', slide_id)
        self.text(X0, 41.5, 602.6, lines * size * 1.21 * 0.94 + 4, headline or '', size=size, bold=True, color=BLACK, ls=94)
        if lines == 3: self.zy, self.zh = 112.0, 253.0
        if wm_url: self.image(wm_url, 645.2, 24.0, 38.8, 10.5)
    def source_line(self, text):
        if not text: return
        lines = wrap_count(text, 6.5, W0 * 0.9)
        self.text(X0, 369.5 - (lines - 1) * 8.5, W0, 9 * lines, text, size=6.5, color=(ONDARK2 if self.dark else GREY), ls=100)
    def footer(self, text, n):
        col = ONDARK2 if self.dark else GREY
        if text: self.text(X0, 383, 400, 9, text, size=6.5, color=col, ls=100)
        self.text(640, 383, 44, 9, str(n), size=6.5, color=col, align='END', ls=100)
    def tags(self, labels):
        if labels: self.pills(labels, 636, 23.5)

    # ---- composites
    def stat_tile(self, x, y, w, h, value, label=None, caption=None, outline=TILE_OUT, value_size=24, value_color=None, fill=None, dark=False):
        self.round_rect(x, y, w, h, fill=fill, outline=outline, outline_w=1.0) if dark else self.rect(x, y, w, h, fill=fill, outline=outline, outline_w=1.0)
        cy = y + 9
        if label:
            self.text(x + 10, cy, w - 20, 10, label.upper(), size=7, bold=True, color=(ONDARK if dark else GREY), ls=100); cy += 13
        vs = value_size
        while vs > 14 and text_width(value, vs, True) > w - 20: vs -= 2
        self.text(x + 10, cy, w - 20, vs * 1.25, value, size=vs, bold=True, color=value_color or (WHITE if dark else BLUE), ls=90); cy += vs * 1.2 + 3
        if caption:
            self.text(x + 10, cy, w - 20, h - (cy - y) - 6, caption, size=7.5, color=(ONDARK if dark else BODY2), ls=112)
    def card(self, x, y, w, h, eyebrow=None, num=None, title=None, body=None, foot=None, pill=None, fill=WHITE, outline=DEEP,
             title_color=BLUE, title_size=10, body_size=8.5, body_color=BODY3, pad=11, blue=False, pill2=None):
        if blue: fill, outline, title_color, body_color = BLUE, None, WHITE, WHITE
        self.rect(x, y, w, h, fill=fill, outline=outline)
        cx, cw, cy = x + pad, w - 2 * pad, y + pad - 1
        row = False; pill_w = 0
        if pill or pill2:
            px = x + w - pad
            for lab in [p for p in (pill2, pill) if p]:
                px, pw = self.pill(px, y + pad - 3, lab, right=True); px -= 4
            pill_w = (x + w - pad) - (px + 4); row = True
        if num:
            self.text(cx, cy, 24, 11, str(num), size=8, color=(WHITE if blue else LBLUE), font=MONO, ls=100); row = True
        if eyebrow:
            ex = cx + (24 if num else 0); avail = cw - (24 if num else 0) - (pill_w + 8 if pill_w else 0)
            if text_width(eyebrow.upper(), 7, True) * 1.18 <= avail:
                self.text(ex, cy, avail, 11, eyebrow.upper(), size=7, bold=True, color=(PALE if blue else GREY), ls=100); row = True
            else:                                   # own line under the pill row
                if row: cy += 15
                self.text(ex, cy, cw - (24 if num else 0), 11, eyebrow.upper(), size=7, bold=True, color=(PALE if blue else GREY), ls=100); row = True
        if row: cy += 15
        if title:
            th = text_h(title, title_size, cw, 105, True)
            self.text(cx, cy, cw, th, title, size=title_size, bold=True, color=title_color, ls=105); cy += th + 3
        foot_h = (text_h(foot, 7.5, cw, 105, True) + 8) if foot else 0
        if body:
            bh = text_h(body, body_size, cw, 115)
            avail = y + h - pad - foot_h - cy
            if bh > avail + 2: raise FitError(f"card '{title or eyebrow}': body needs {bh:.0f} pt, has {avail:.0f} pt (size {body_size})")
            self.text(cx, cy, cw, bh, body, size=body_size, color=body_color, ls=115)
        if foot:
            fy = y + h - pad - foot_h + 4
            self.rect(cx, fy - 4, 10.5, 1.0, fill=(WHITE if blue else BLUE))
            self.text(cx, fy, cw, foot_h - 4, foot, size=7.5, bold=True, color=(WHITE if blue else DEEP), ls=105)
    def code_block(self, x, y, w, h, code, size=7.5, title=None):
        cy = y
        if title:
            self.text(x, cy, w, 11, title.upper(), size=7, bold=True, color=BLUE, ls=100); cy += 14
        self.rect(x, cy, w, h - (cy - y), fill=BLACK, outline=PANEL, outline_w=0.56)
        self.text(x + 12, cy + 10, w - 24, h - (cy - y) - 20, code.replace('\t', '    '), size=size, color=WHITE, font=MONO, ls=130, valign='TOP')
        self.min_font = min(self.min_font, size)
    def diagram_box(self, x, y, w, h, title=None, body=None, pill=None, style='light', title_size=9, body_size=7.5):
        if style == 'label':   # lane header: no fill, no outline, 7 pt bold blue caps
            self.text(x, y, w, h, (title or body or '').upper(), size=7, bold=True, color=BLUE, ls=105, valign='MIDDLE'); return
        st = {'light': (PANEL3, None, INK, BODY3), 'blue': (BRAND, None, WHITE, WHITE), 'dark': (DARK, None, WHITE, ONDARK),
              'outline': (WHITE, DEEP, INK, BODY3), 'panel': (PANEL, None, INK, BODY3)}[style]
        self.rect(x, y, w, h, fill=st[0], outline=st[1])
        cx, cw, cy = x + 8, w - 16, y + 7
        reserve = 0
        if pill:
            px, pw = self.pill(x + w - 6, y + 5, pill, h=12, size=6.5, right=True)
            if pw > cw * 0.45: cy += 13          # chip takes the first line; title goes under it
            else: reserve = pw + 10
        if title:
            th = text_h(title, title_size, cw - reserve, 100, True)
            self.text(cx, cy, cw - reserve, th, title, size=title_size, bold=True, color=st[2], ls=100); cy += th + 1
        if body:
            avail = y + h - cy - 3
            bs = body_size; bh = text_h(body, bs, cw, 108)
            if bh > avail + 2: bs = 7.0; bh = text_h(body, bs, cw, 108)
            if bh > avail + 6: raise FitError(f"diagram box '{title or body[:20]}': body needs {bh:.0f} pt at 7 pt, box has {avail:.0f} pt")
            self.text(cx, cy, cw, max(bh, avail), body, size=bs, color=st[3], ls=108)
    def connector(self, a, b, label=None, color=LBLUE, obstacles=()):
        """a, b: (x,y,w,h) boxes; straight line between facing edge midpoints with an end arrow.
        A label sits at the midpoint unless that covers a box; then above / below (horizontal) or beside (vertical)."""
        ax, ay, aw, ah = a; bx, by, bw, bh = b
        if bx >= ax + aw: p1, p2 = (ax + aw, ay + ah / 2), (bx, by + bh / 2)
        elif bx + bw <= ax: p1, p2 = (ax, ay + ah / 2), (bx + bw, by + bh / 2)
        elif by >= ay + ah: p1, p2 = (ax + aw / 2, ay + ah), (bx + bw / 2, by)
        else: p1, p2 = (ax + aw / 2, ay), (bx + bw / 2, by + bh)
        self.line(p1[0], p1[1], p2[0], p2[1], color=color, weight=0.75, end_arrow=True)
        if label:
            mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
            lw = text_width(label, 6.5) + 6; lh = 11
            horizontal = abs(p2[0] - p1[0]) >= abs(p2[1] - p1[1])
            cands = [(mx - lw / 2, my - 6)]
            if horizontal: cands += [(mx - lw / 2, min(ay, by) - lh - 2), (mx - lw / 2, max(ay + ah, by + bh) + 2)]
            else: cands += [(mx + 5, my - 6), (mx - lw - 5, my - 6)]
            def clear(r):
                rx, ry = r
                for (ox, oy, ow, oh) in obstacles:
                    if rx < ox + ow - 1 and rx + lw > ox + 1 and ry < oy + oh - 1 and ry + lh > oy + 1: return False
                return 0 <= rx and rx + lw <= PAGE_W and 0 <= ry
            rx, ry = next((c for c in cands if clear(c)), cands[0])
            self.rect(rx, ry, lw, lh, fill=WHITE)
            self.text(rx, ry + 0.5, lw, 10, label, size=6.5, color=GREY, align='CENTER', ls=100)

    def table(self, x, y, col_widths, rows, header=None, header_style='dark', font_size=8, bold_first_col=True, zebra=True,
              min_row=18, header_min=22, max_h=None, native=False, pad_x=6, pad_y=5):
        """Table. Default: a rectangle grid in the template's own idiom (slides 15, 32, 43 to 45), 5 pt vertical padding,
        deterministic row heights. native=True uses createTable (7.2 pt fixed cell padding, see table_native).
        rows: list of lists of cells; a cell is a string or {'text','pill','pill2','bold','align'}. Returns the table height."""
        if native:
            self.table_native(x, y, col_widths, rows, header, header_style, font_size, bold_first_col, zebra, max(min_row, 22), max(header_min, 24), max_h); return self.table_h
        ncols = len(col_widths); allrows = ([list(header)] if header else []) + [list(r) for r in rows]
        hfill = DARK if header_style == 'dark' else BRAND
        cells = []; row_h = []
        for i, r in enumerate(allrows):
            is_h = bool(header) and i == 0; fs = max(font_size - 0.5, 6.5) if is_h else font_size   # header never under the 6.5 pt floor (15 Oct 2026)
            need = 0; crow = []
            for j in range(ncols):
                c = r[j] if j < len(r) else ''
                d = c if isinstance(c, dict) else {'text': c}
                txt = (d.get('text') or '').strip()
                if is_h: txt = txt.upper()
                plist = [p for p in (d.get('pill'), d.get('pill2')) if p]
                base_bold = bool(is_h or d.get('bold') or (bold_first_col and j == 0))
                tfs = 7 if plist else fs
                lines = wrap_count(txt, tfs, col_widths[j] - 2 * pad_x, base_bold) if txt else 0
                hgt = lines * tfs * 1.21 * 1.08 + (14.4 if plist else 0) + (2 if (plist and txt) else 0)
                need = max(need, hgt); crow.append((d, txt, plist, base_bold, tfs))
            row_h.append(max(header_min if is_h else min_row, need + 2 * pad_y)); cells.append(crow)
        self.table_h = sum(row_h)
        if max_h and self.table_h > max_h + 2:
            raise FitError(f"table needs {self.table_h:.0f} pt, zone has {max_h:.0f} pt (font {font_size}, {len(rows)} rows)")
        cy = y
        for i, crow in enumerate(cells):
            is_h = bool(header) and i == 0; bi = i - (1 if header else 0)
            for j, (d, txt, plist, base_bold, tfs) in enumerate(crow):
                cx = x + sum(col_widths[:j]); cw = col_widths[j]
                if is_h: fill = hfill
                elif bold_first_col and j == 0: fill = PANEL
                else: fill = PANEL2 if (zebra and bi % 2 == 1) else WHITE
                self.rect(cx, cy, cw, row_h[i], fill=fill)
                color = WHITE if is_h else (d.get('color') or (DEEP if (bold_first_col and j == 0) else INK))
                if plist:
                    px = cx + pad_x; py = cy + pad_y if txt else cy + (row_h[i] - 14) / 2
                    for lab in plist:
                        px, pw = self.pill(px, py, lab); px += pw + 4
                    if txt: self.text(cx + pad_x, cy + pad_y + 15.4, cw - 2 * pad_x, row_h[i] - pad_y - 15.4, txt, size=7, color=GREY, ls=108)
                elif txt:
                    self.text(cx + pad_x, cy + pad_y, cw - 2 * pad_x, row_h[i] - 2 * pad_y, txt, size=tfs, bold=base_bold, color=color, align=d.get('align', 'START'), ls=108, valign='MIDDLE')
            if is_h: self.hairline(x, cy + row_h[i] - 0.4, sum(col_widths), alpha=0.24)
            cy += row_h[i]
        self.min_font = min(self.min_font, max(font_size - 0.5, 6.5))
        return self.table_h

    def table_native(self, x, y, col_widths, rows, header=None, header_style='dark', font_size=8, bold_first_col=True, zebra=True,
              min_row=22, header_min=24, max_h=None, cell_valign='MIDDLE'):
        """Native Slides table (createTable + per-cell styling). Limits hit on 8 Oct 2026: cell padding is fixed at 0.1 in and not
        exposed by the API, and tableRows[].rowHeight reports the minimum, not the rendered height, so rows are pinned from a text model."""
        tid = self.nid(); ncols = len(col_widths); body = [list(r) for r in rows]
        allrows = ([list(header)] if header else []) + body
        nrows = len(allrows)
        est = (header_min if header else 0) + sum(max(min_row, max(text_h(_cell_text(c), font_size, col_widths[j] - 14, 110) + 12 for j, c in enumerate(r))) for r in body)
        if max_h and est > max_h + 4:
            raise FitError(f"table needs about {est:.0f} pt, zone has {max_h:.0f} pt (font {font_size})")
        self.R.append({'createTable': {'objectId': tid, 'elementProperties': {'pageObjectId': self.page,
            'size': {'width': {'magnitude': emu(sum(col_widths)), 'unit': 'EMU'}, 'height': {'magnitude': emu(nrows * min_row), 'unit': 'EMU'}},
            'transform': {'scaleX': 1, 'scaleY': 1, 'shearX': 0, 'shearY': 0, 'translateX': emu(x), 'translateY': emu(y), 'unit': 'EMU'}},
            'rows': nrows, 'columns': ncols}})
        for j, cw in enumerate(col_widths):
            self.R.append({'updateTableColumnProperties': {'objectId': tid, 'columnIndices': [j], 'tableColumnProperties': {'columnWidth': {'magnitude': emu(cw), 'unit': 'EMU'}}, 'fields': 'columnWidth'}})
        row_h = []
        for i, r in enumerate(allrows):
            is_h = header and i == 0
            fs = (font_size - 0.5) if is_h else font_size
            need = 0
            for j in range(ncols):
                c = r[j] if j < len(r) else ''
                d = c if isinstance(c, dict) else {'text': c}
                txt = d.get('text') or ''
                has_p = bool(d.get('pill') or d.get('pill2'))
                tfs = 7 if has_p else fs
                lines = wrap_count(txt, tfs, col_widths[j] - 2 * CELL_PAD, is_h or bool(d.get('bold')) or (bold_first_col and j == 0)) if txt else 0
                hgt = lines * tfs * 1.21 * 1.08 + (14.4 if has_p else 0) + (1 if (has_p and txt) else 0)
                need = max(need, hgt)
            row_h.append(max(header_min if is_h else min_row, need + 2 * CELL_PAD + 1))
        for i, h in enumerate(row_h):
            self.R.append({'updateTableRowProperties': {'objectId': tid, 'rowIndices': [i], 'tableRowProperties': {'minRowHeight': {'magnitude': emu(h), 'unit': 'EMU'}}, 'fields': 'minRowHeight'}})
        self.table_h = sum(row_h)
        if max_h and self.table_h > max_h + 4:
            raise FitError(f"table renders about {self.table_h:.0f} pt, zone has {max_h:.0f} pt (font {font_size})")
        hfill = DARK if header_style == 'dark' else BRAND
        pill_cells = []
        for i, r in enumerate(allrows):
            is_h = header and i == 0
            for j in range(ncols):
                c = r[j] if j < len(r) else ''
                d = c if isinstance(c, dict) else {'text': c}
                txt = (d.get('text') or '')
                pill = d.get('pill'); pill2 = d.get('pill2')
                if pill or pill2: pill_cells.append((i, j, [p for p in (pill, pill2) if p], bool(txt)))
                has_pill = bool(pill or pill2)
                if has_pill and not txt: txt = ' '
                elif has_pill and txt: txt = ' \n' + txt
                if not txt: txt = ' '
                segs = _segments(txt); plain = ''.join(t for t, b in segs)
                self.R.append({'insertText': {'objectId': tid, 'cellLocation': {'rowIndex': i, 'columnIndex': j}, 'text': plain, 'insertionIndex': 0}})
                base_bold = bool(is_h or d.get('bold') or (bold_first_col and j == 0))
                color = WHITE if is_h else (INK if not d.get('color') else d['color'])
                size = (font_size - 0.5) if is_h else font_size
                k = 0
                for t, b in segs:
                    isb = base_bold or b
                    st = {'weightedFontFamily': {'fontFamily': FONT, 'weight': 700 if isb else 400}, 'bold': isb, 'fontSize': {'magnitude': size, 'unit': 'PT'}, 'foregroundColor': {'opaqueColor': {'rgbColor': rgb(color)}}}
                    self.R.append({'updateTextStyle': {'objectId': tid, 'cellLocation': {'rowIndex': i, 'columnIndex': j}, 'textRange': {'type': 'FIXED_RANGE', 'startIndex': k, 'endIndex': k + len(t)}, 'style': st, 'fields': 'weightedFontFamily,bold,fontSize,foregroundColor'}})
                    k += len(t)
                if has_pill:  # first (blank) line reserves the pill height; any text under the pills is small grey (owners)
                    self.R.append({'updateTextStyle': {'objectId': tid, 'cellLocation': {'rowIndex': i, 'columnIndex': j}, 'textRange': {'type': 'FIXED_RANGE', 'startIndex': 0, 'endIndex': 1}, 'style': {'fontSize': {'magnitude': 11, 'unit': 'PT'}}, 'fields': 'fontSize'}})
                    if len(plain) > 2:
                        self.R.append({'updateTextStyle': {'objectId': tid, 'cellLocation': {'rowIndex': i, 'columnIndex': j}, 'textRange': {'type': 'FIXED_RANGE', 'startIndex': 2, 'endIndex': len(plain)}, 'style': {'fontSize': {'magnitude': 7, 'unit': 'PT'}, 'foregroundColor': {'opaqueColor': {'rgbColor': rgb(GREY)}}, 'bold': False, 'weightedFontFamily': {'fontFamily': FONT, 'weight': 400}}, 'fields': 'fontSize,foregroundColor,bold,weightedFontFamily'}})
                self.R.append({'updateParagraphStyle': {'objectId': tid, 'cellLocation': {'rowIndex': i, 'columnIndex': j}, 'textRange': {'type': 'ALL'},
                    'style': {'alignment': d.get('align', 'START'), 'lineSpacing': 108, 'spaceAbove': {'magnitude': 0, 'unit': 'PT'}, 'spaceBelow': {'magnitude': 0, 'unit': 'PT'}}, 'fields': 'alignment,lineSpacing,spaceAbove,spaceBelow'}})
                if is_h: fill = hfill
                elif zebra and ((i - (1 if header else 0)) % 2 == 1): fill = PANEL2
                else: fill = WHITE
                if not is_h and bold_first_col and j == 0 and header_style != 'plain': fill = PANEL if fill == WHITE else PANEL
                self.R.append({'updateTableCellProperties': {'objectId': tid, 'tableRange': {'location': {'rowIndex': i, 'columnIndex': j}, 'rowSpan': 1, 'columnSpan': 1},
                    'tableCellProperties': {'tableCellBackgroundFill': solid(fill), 'contentAlignment': cell_valign}, 'fields': 'tableCellBackgroundFill.solidFill,contentAlignment'}})
        self.R.append({'updateTableBorderProperties': {'objectId': tid, 'tableRange': {'location': {'rowIndex': 0, 'columnIndex': 0}, 'rowSpan': nrows, 'columnSpan': ncols}, 'borderPosition': 'ALL',
            'tableBorderProperties': {'tableBorderFill': solid(WHITE), 'weight': {'magnitude': emu(1.0), 'unit': 'EMU'}, 'dashStyle': 'SOLID'}, 'fields': 'tableBorderFill,weight,dashStyle'}})
        self.min_font = min(self.min_font, font_size - 0.5)
        for (i, j, plist, has_text) in pill_cells:   # overlay from the pinned row model (the API does not expose rendered heights)
            cx = x + sum(col_widths[:j]) + CELL_PAD; cy = y + sum(row_h[:i])
            py = cy + (row_h[i] - 14) / 2 if not has_text else cy + CELL_PAD + 0.5
            for lab in plist:
                px, pw = self.pill(cx, py, lab); cx += pw + 4
        return tid

def _cell_text(c):
    return (c.get('text') or '') if isinstance(c, dict) else (c or '')

# ================================================================= slide renderers
def _item_text(it):
    """string or {'text','pill','bold'} -> (text, pill)"""
    if isinstance(it, dict): return (('**%s**' % it['text']) if it.get('bold') else it.get('text', '')), it.get('pill')
    return it, None

def bar_h(text):
    """height of a bottom band (#E8EAF5, 8.5 pt) for this text; 0 when empty"""
    return (max(24.0, text_h(text, 8.5, W0 - 24, 110) + 11)) if text else 0.0

def _bar(sb, y, text, h=None):
    """bottom band like template slide 4, top edge at y, height from the text"""
    if not text: return 0
    h = h or bar_h(text); th = text_h(text, 8.5, W0 - 24, 110)
    sb.rect(X0, y, W0, h, fill=PANEL)
    sb.text(X0 + 12, y + (h - th) / 2, W0 - 24, th, text, size=8.5, color=INK, valign='MIDDLE', ls=110)
    return h

def card_need(w, eyebrow=None, num=None, title=None, body=None, foot=None, pill=None, pill2=None, title_size=10, body_size=8.5, pad=11):
    """height card() needs for this content"""
    cw = w - 2 * pad; h = pad - 1
    if eyebrow or num or pill or pill2: h += 15
    if eyebrow and (pill or pill2):
        pill_w = sum(text_width((p or '').upper(), 7, True) + 12 for p in (pill, pill2) if p) + (4 if (pill and pill2) else 0)
        if text_width(eyebrow.upper(), 7, True) > cw - (24 if num else 0) - pill_w - 8: h += 15
    if title: h += text_h(title, title_size, cw, 105, True) + 3
    if body: h += text_h(body, body_size, cw, 115)
    if foot: h += text_h(foot, 7.5, cw, 105, True) + 8
    return h + pad

def _side_column(sb, x, y, w, h, side):
    """right column: header + items (title/body)"""
    if not side: return
    cy = y
    if side.get('header'):
        sb.text(x, cy, w, 11, side['header'].upper(), size=7.5, bold=True, color=BLUE, ls=100); cy += 14
        sb.hairline(x, cy, w); cy += 8
    items = side.get('items', [])
    for it in items:
        t = it.get('title'); b = it.get('body')
        if t:
            th = text_h(t, 8.5, w, 105, True); sb.text(x, cy, w, th, t, size=8.5, bold=True, color=INK, ls=105); cy += th + 1
        if b:
            bh = text_h(b, 8, w, 112); sb.text(x, cy, w, bh, b, size=8, color=BODY3, ls=112); cy += bh + 7
    if cy > y + h + 4: raise FitError(f"side column overflows by {cy - (y + h):.0f} pt")

def r_cover(deck, s, tag, n):
    sid, m = deck.duplicate(BASE['cover'], tag); sb = SB(deck, sid, tag, m, dark=True)
    el = sb._tpl_el(1, ROLE[1]['title'])
    title = s.get('title') or ''
    size = 30 if wrap_count(title, 30, 480, True) <= 2 else 26
    lines = wrap_count(title, size, 480, True)
    sb.R += replace_text_requests(el, title, size=size)
    # merchant wordmark: drop the template's logo box (cut for a 5.72-aspect logo) and place ours at x 115, centred on the yuno wordmark (y 38.8..54.8)
    lh = float(s.get('logo_h') or 22.0); lw = float(s.get('logo_w') or lh * LOGO_ASPECT)
    sb.delete([m[ROLE[1]['logo']]])
    sb.image(s.get('logo_url') or LOGO_URL, 115.0, 46.8 - lh / 2, lw, lh)
    # title box (valign MIDDLE) sized to its lines and bottom-anchored at y 330; subtitle and presenter underneath
    th = lines * size * 1.21 + 6
    sb.move(m[ROLE[1]['title']], 29, 330 - th, 492.8, th, size=(el['size']['width']['magnitude'], el['size']['height']['magnitude']))
    if s.get('subtitle'): sb.text(36, 338, 560, 16, s['subtitle'], size=12, color=WHITE, ls=110)
    if s.get('presenter'): sb.text(36, 358, 560, 12, s['presenter'], size=8.5, color=PALE, ls=100)
    sb.flush(); deck.set_notes(sid, s.get('notes')); return sid

def r_agenda(deck, s, tag, n):
    sid, m = deck.duplicate(BASE['agenda'], tag); sb = SB(deck, sid, tag, m)
    sb.delete_all_but(2, KEEP[2])
    items = s.get('items', [])
    N = max(len(items), 1); y0 = 118; pitch = min(47.6, (362 - y0) / N); size = 15 if pitch >= 36 else (13 if pitch >= 28 else 11)
    for i, it in enumerate(items):
        y = y0 + i * pitch
        sb.text(X0, y + 4, 40, 14, str(it.get('num', f"{i + 1:02d}")), size=10, color=LBLUE, font=MONO, ls=100)
        sb.text(73.8, y, 549, size * 1.5, (it.get('title') or '').upper(), size=size, color=INK, ls=110)
        if i < N - 1: sb.hairline(X0, y + pitch - 13, W0)
    sb.flush(); deck.set_notes(sid, s.get('notes')); return sid

def r_divider(deck, s, tag, n):
    sid, m = deck.duplicate(BASE['divider'], tag); sb = SB(deck, sid, tag, m, dark=True)
    sb.R += replace_text_requests(sb._tpl_el(3, ROLE[3]['num']), str(s.get('num', '')))
    title = s.get('title') or ''
    sb.R += replace_text_requests(sb._tpl_el(3, ROLE[3]['title']), title, size=29 if wrap_count(title, 29, 579, True) <= 2 else 24)
    if s.get('sub'): sb.text(X0, 352, 579, 14, s['sub'], size=10, color=ONDARK, ls=110)
    sl = s.get('section_list') or []
    if sl:
        y = 78
        for item in sl:
            cur = (str(s.get('num', '')).strip() and item.strip().startswith(str(s.get('num')).strip())) or (title and title.lower() in item.lower())
            sb.text(X0, y, 400, 10, item.upper(), size=7, bold=bool(cur), color=WHITE if cur else '#B9BFE8', ls=100)
            y += 13
    sb.flush(); deck.set_notes(sid, s.get('notes')); return sid

def _content_base(deck, s, tag, dark=False):
    base = BASE['dark'] if dark else BASE['white']
    if not dark and not deck.has_template():
        wm = deck.chrome_image_url('g3f77215683c_2_2969') or deck.chrome_image_url('_2969')
        if not wm: raise SystemExit('no live Yuno wordmark image to copy; the deck has no built content slide')
        sid = deck.create_blank(tag); sb = SB(deck, sid, tag, {}, dark=False)
        sb.chrome_blank(s.get('kicker', ''), s.get('headline', ''), s.get('id'), wm)
        sb.tags(s.get('tag'))
        return sid, sb
    sid, m = deck.duplicate(base, tag); sb = SB(deck, sid, tag, m, dark=dark)
    sb.delete_all_but(base, KEEP[base])
    sb.kicker(s.get('kicker', ''), base); sb.headline(s.get('headline', ''), base, s.get('id'))
    sb.tags(s.get('tag'))
    return sid, sb

def _finish(deck, sb, sid, s, n, footer):
    sb.source_line(s.get('source')); sb.footer(footer, n)
    sb.flush(); deck.set_notes(sid, s.get('notes')); return sid

def r_exec_summary(deck, s, tag, n, footer):
    sid, sb = _content_base(deck, s, tag)
    bottom = s.get('bottom'); bh = bar_h(bottom); y_end = (363 - bh - 12) if bottom else 365
    # right panel
    px, pw = 393.4, 684 - 393.4
    sb.rect(px, sb.zy, pw, y_end - sb.zy, fill=BLUE)
    cy = sb.zy + 16
    if s.get('right_header'): sb.text(px + 20, cy, pw - 40, 12, s['right_header'].upper(), size=8.5, bold=True, color=WHITE, ls=100); cy += 22
    cards = s.get('right_cards', [])[:3]
    avail = y_end - 12 - cy; per = avail / max(len(cards), 1)
    for c in cards:
        th = text_h(c.get('title', ''), 8, pw - 40, 105, True); cb = text_h(c.get('body', ''), 8, pw - 40, 115)   # cb, not bh: bh is the band height (fixed 15 Oct 2026)
        if th + cb + 6 > per + 1: raise FitError(f"slide {s.get('id')}: exec_summary right card '{c.get('title')}' overflows")
        sb.text(px + 20, cy, pw - 40, th, c.get('title', '').upper(), size=8, bold=True, color=WHITE, ls=105)
        sb.text(px + 20, cy + th + 2, pw - 40, cb, c.get('body', ''), size=8, color=WHITE, ls=115)
        cy += per
    # left column
    lx, lw = X0, px - 20 - X0
    cy = sb.zy
    if s.get('left_header'): sb.text(lx, cy, lw, 12, s['left_header'].upper(), size=8, bold=True, color=BLUE, ls=100); cy += 16
    items = s.get('left_items', [])
    sizes = [(9, 8.5), (9, 8), (8.5, 7.5)]
    for ts, bs in sizes:
        hs = [(text_h(it.get('title', ''), ts, lw, 105, True), text_h(it.get('body', ''), bs, lw, 112)) for it in items]
        total = sum(a + b + 9 for a, b in hs)
        if cy + total <= y_end - 4: break
    else:
        raise FitError(f"slide {s.get('id')}: exec_summary left column overflows ({cy + total:.0f} > {y_end})")
    for it, (th, bh) in zip(items, hs):
        sb.text(lx, cy, lw, th, it.get('title', ''), size=ts, bold=True, color=INK, ls=105); cy += th + 1
        sb.text(lx, cy, lw, bh, it.get('body', ''), size=bs, color=BODY3, ls=112); cy += bh + 8
    _bar(sb, 363 - bh, bottom)
    return _finish(deck, sb, sid, s, n, footer)

def r_stats(deck, s, tag, n, footer):
    sid, sb = _content_base(deck, s, tag)
    tiles = s.get('tiles', [])[:4]; N = max(len(tiles), 1)
    gap = 12; tw = (W0 - gap * (N - 1)) / N
    below = (30 if s.get('chips') else 0) + ((text_h(s['paragraph'], 9.5, W0, 125) + 10) if s.get('paragraph') else 0)
    bh = bar_h(s.get('bar')); bar_top = 363 - bh
    th = max(100, min(170, (bar_top - 12 if s.get('bar') else 362) - sb.zy - below))
    for i, t in enumerate(tiles):
        sb.stat_tile(X0 + i * (tw + gap), sb.zy, tw, th, t.get('value', ''), t.get('label'), t.get('caption'))
    cy = sb.zy + th + 14
    chips = s.get('chips') or []
    if chips:
        cx = X0
        for ch in chips:
            w = text_width(ch, 7.5) + 16
            if cx + w > 684: cx = X0; cy += 22
            sb.rect(cx, cy, w, 17, outline=DEEP, outline_w=0.5)
            sb.text(cx, cy + 3.5, w, 10, ch, size=7.5, color=DEEP, align='CENTER', ls=100)
            cx += w + 6
        cy += 30
    if s.get('paragraph'):
        ph = text_h(s['paragraph'], 9.5, W0, 125)
        sb.text(X0, cy, W0, ph, s['paragraph'], size=9.5, color=INK, ls=125); cy += ph
    if s.get('bar'): _bar(sb, bar_top, s['bar'])
    if cy > (bar_top - 8 if s.get('bar') else 365) + 2: raise FitError(f"slide {s.get('id')}: stats paragraph overflows")
    return _finish(deck, sb, sid, s, n, footer)

def r_scale(deck, s, tag, n, footer):
    """three outlined cards like template slide 4: numbers | bullets | body"""
    sid, sb = _content_base(deck, s, tag)
    bh = bar_h(s.get('bar'))
    cw, gap, y = 207, 13.5, sb.zy; h = (363 - bh - 10 - y) if s.get('bar') else (365 - y)
    xs = [X0, X0 + cw + gap, X0 + 2 * (cw + gap)]
    for x in xs: sb.rect(x, y, cw, h, fill=WHITE, outline=DEEP)
    # left: header + 2 tiles + note
    cy = y + 12
    sb.text(xs[0] + 11.6, cy, cw - 23, 10, (s.get('left_header') or '').upper(), size=7, bold=True, color=INK, ls=100); cy += 22
    for t in s.get('tiles', [])[:2]:
        sb.text(xs[0] + 11.6, cy, cw - 23, 26, t.get('value', ''), size=22, bold=True, color=BLUE, ls=87); cy += 26
        lh = text_h(t.get('label', ''), 8, cw - 23, 125)
        sb.text(xs[0] + 11.6, cy, cw - 23, lh, t.get('label', ''), size=8, color=INK, ls=125); cy += lh + 8
    if s.get('left_note'):
        sb.hairline(xs[0] + 11.6, cy, cw - 23); cy += 8
        nh = text_h(s['left_note'], 8, cw - 23, 125)
        if cy + nh > y + h - 8: raise FitError(f"slide {s.get('id')}: scale left card overflows")
        sb.text(xs[0] + 11.6, cy, cw - 23, nh, s['left_note'], size=8, color=INK, ls=125)
    # middle: header + 3 items with arrow glyph
    cy = y + 12
    sb.text(xs[1] + 11.6, cy, cw - 23, 10, (s.get('mid_header') or '').upper(), size=7, bold=True, color=INK, ls=100); cy += 22
    for it in s.get('mid_items', [])[:4]:
        t, _ = _item_text(it)
        ih = text_h(t, 8, cw - 44, 125)
        sb.text(xs[1] + 11.6, cy - 1, 14, 12, '↗', size=10, color=LBLUE, ls=100)
        sb.text(xs[1] + 27.4, cy, cw - 39, ih, t, size=8, color=INK, ls=125); cy += ih + 10
    if cy > y + h - 4: raise FitError(f"slide {s.get('id')}: scale middle card overflows")
    # right: header + body
    cy = y + 12
    sb.text(xs[2] + 11.6, cy, cw - 23, 10, (s.get('right_header') or '').upper(), size=7, bold=True, color=INK, ls=100); cy += 22
    rb = s.get('right_body', ''); rh = text_h(rb, 8, cw - 23, 125)
    if cy + rh > y + h - 8: raise FitError(f"slide {s.get('id')}: scale right card overflows")
    sb.text(xs[2] + 11.6, cy, cw - 23, rh, rb, size=8, color=INK, ls=125)
    _bar(sb, 363 - bh, s.get('bar'))
    return _finish(deck, sb, sid, s, n, footer)

def r_four_numbers(deck, s, tag, n, footer):
    sid, sb = _content_base(deck, s, tag)
    tiles = s.get('tiles', [])[:4]
    tw, th, g = 138, 76, 8
    for i, t in enumerate(tiles):
        x = X0 + (i % 2) * (tw + g); y = sb.zy + 4 + (i // 2) * (th + g)
        sb.round_rect(x, y, tw, th, outline=TILE_OUT, outline_w=1.4)
        sb.text(x + 11, y + 12, tw - 22, 28, t.get('value', ''), size=24, bold=True, color=BLACK, ls=80)
        sb.text(x + 11, y + 44, tw - 22, 24, t.get('label', ''), size=7.6, color=INK, ls=112)
    rx = X0 + 2 * tw + g + 24; rw = 684 - rx; cy = sb.zy + 4
    if s.get('right_header'): sb.text(rx, cy, rw, 11, s['right_header'].upper(), size=7.5, bold=True, color=BLUE, ls=100); cy += 16
    items = s.get('right_items', [])[:4]
    bh = bar_h(s.get('bar')); y_end = (363 - bh - 10) if s.get('bar') else 365
    for bs in (8.5, 8, 7.5):
        hs = [(text_h(it.get('title', ''), 8.2, rw, 105, True), text_h(it.get('body', ''), bs, rw, 112)) for it in items]
        if cy + sum(a + b + 9 for a, b in hs) <= y_end: break
    else: raise FitError(f"slide {s.get('id')}: four_numbers right column overflows")
    for it, (a, b) in zip(items, hs):
        sb.text(rx, cy, rw, a, it.get('title', '').upper(), size=8.2, bold=True, color=BLUE, ls=105); cy += a + 1
        sb.text(rx, cy, rw, b, it.get('body', ''), size=bs, color=INK, ls=112); cy += b + 8
    _bar(sb, 363 - bh, s.get('bar'))
    return _finish(deck, sb, sid, s, n, footer)

def r_traffic_list(deck, s, tag, n, footer):
    sid, sb = _content_base(deck, s, tag)
    rows = s.get('rows', [])[:12]; N = max(len(rows), 1)
    pitch = min(22, (sb.zh - 10) / N); y = sb.zy
    try: mx = max(float(str(r.get('pct', '0')).replace('%', '').replace(',', '.')) for r in rows) or 1
    except ValueError: mx = 100
    side = s.get('side')
    right = (X0 + W0 * 0.55) if side else 684
    bx = X0 + 110; bw = right - 56 - bx
    for r in rows:
        sb.text(X0, y, 104, 12, r.get('country', ''), size=9, color=INK, ls=100)
        try: v = float(str(r.get('pct', '0')).replace('%', '').replace(',', '.'))
        except ValueError: v = 0
        sb.rect(bx, y + 3, bw, 7, fill=PANEL); sb.rect(bx, y + 3, max(bw * v / mx, 1), 7, fill=BLUE)
        sb.text(bx + bw + 8, y, right - (bx + bw + 8), 12, str(r.get('pct', '')), size=9, color=DEEP, align='END', ls=100)
        sb.hairline(X0, y + pitch - 4, right - X0, alpha=0.10)
        y += pitch
    if side: _side_column(sb, right + 24, sb.zy, 684 - (right + 24), sb.zh, side)
    return _finish(deck, sb, sid, s, n, footer)

def r_cards_row(deck, s, tag, n, footer, numbered_default=False):
    sid, sb = _content_base(deck, s, tag)
    cards = s.get('cards', [])[:5]; N = max(len(cards), 1)
    side = s.get('side'); bar = s.get('bar')
    width = W0 * 0.65 if side else W0
    gap = 12 if N < 5 else 9; cw = (width - gap * (N - 1)) / N
    ts, bs = (10, 8.5) if N < 5 else (9.5, 8)   # five cards: narrower, a step smaller
    limits = s.get('limits'); bh = bar_h(bar)
    y = sb.zy; y_end = (363 - bh - 12) if bar else 365
    max_h = (y_end - y - 86) if limits else (y_end - y)
    need = max([card_need(cw, c.get('eyebrow'), c.get('num'), c.get('title'), c.get('body'), c.get('foot'), c.get('pill'), c.get('pill2'), title_size=ts, body_size=bs)
                + (15 if (c.get('eyebrow') and text_width(c['eyebrow'].upper(), 7, True) * 1.18 > cw - 22 - (24 if c.get('num') else 0)) else 0) for c in cards] + [0])
    if need > max_h + 1: raise FitError(f"slide {s.get('id')}: cards need {need:.0f} pt, have {max_h:.0f} pt")
    h = max_h if (not bar and not limits) else max(110.0, min(need, max_h))   # no band: cards use the zone like the template
    hc = max(150.0, min(need + 16, max_h)) if side else h
    for i, c in enumerate(cards):
        sb.card(X0 + i * (cw + gap), y, cw, hc, eyebrow=c.get('eyebrow'), num=c.get('num'), title=c.get('title'), body=c.get('body'), foot=c.get('foot'), pill=c.get('pill'), pill2=c.get('pill2'),
                title_size=ts, body_size=bs)
    if side: _side_column(sb, X0 + width + 20, y, 684 - (X0 + width + 20), h, side)
    if limits:   # four-tile strip under the cards
        ly = y + h + 12
        if limits.get('header'): sb.text(X0, ly, W0, 10, limits['header'].upper(), size=7, bold=True, color=BLUE, ls=100); ly += 14
        tiles = limits.get('tiles', [])[:4]; N2 = max(len(tiles), 1); tw = (W0 - 10 * (N2 - 1)) / N2; th = min(74, y_end - ly)
        for i, t in enumerate(tiles):
            tx = X0 + i * (tw + 10)
            sb.rect(tx, ly, tw, th, fill=PANEL3)
            sb.text(tx + 10, ly + 7, tw - 20, 20, str(t.get('value', '')), size=15, bold=True, color=BLUE, ls=95)
            sb.text(tx + 10, ly + 28, tw - 20, th - 32, t.get('label', ''), size=7.5, color=BODY3, ls=110)
        y_cards_end = ly + th
    else: y_cards_end = y + h
    _bar(sb, y_cards_end + 12, bar)
    return _finish(deck, sb, sid, s, n, footer)

def r_two_column(deck, s, tag, n, footer):
    sid, sb = _content_base(deck, s, tag)
    cols = s.get('cols', [])[:2]; bar = s.get('bar'); bh = bar_h(bar); y_end = (363 - bh - 12) if bar else 365
    gap = 24; cw = (W0 - gap) / 2
    for i, col in enumerate(cols):
        x = X0 + i * (cw + gap); cy = sb.zy
        if col.get('header'):
            hs_ = 9 if wrap_count(col['header'].upper(), 9, cw, True) <= 2 else 8
            hh = text_h(col['header'].upper(), hs_, cw, 100, True)
            sb.text(x, cy, cw, hh, col['header'].upper(), size=hs_, bold=True, color=BLUE, ls=100); cy += hh + 6
        items = col.get('items', [])
        for bs in (8.5, 8, 7.5):
            hs = [(text_h(it.get('title', ''), 9, cw - 22, 105, True), text_h(it.get('body', ''), bs, cw - 22, 112)) for it in items]
            if cy + sum(a + b + 9 for a, b in hs) <= y_end: break
        else: raise FitError(f"slide {s.get('id')}: two_column column {i + 1} overflows")
        for k, (it, (a, b)) in enumerate(zip(items, hs)):
            sb.text(x, cy + 1, 20, 10, f"{k + 1:02d}", size=7, color=LBLUE, font=MONO, ls=100)
            sb.text(x + 22, cy, cw - 22, a, it.get('title', ''), size=9, bold=True, color=INK, ls=105); cy += a + 1
            sb.text(x + 22, cy, cw - 22, b, it.get('body', ''), size=bs, color=BODY3, ls=112); cy += b + 8
    _bar(sb, 363 - bh, bar)
    return _finish(deck, sb, sid, s, n, footer)

def r_table(deck, s, tag, n, footer):
    sid, sb = _content_base(deck, s, tag)
    cols = s.get('columns', []); fr = s.get('col_widths') or [1.0 / max(len(cols), 1)] * len(cols)
    tot = sum(fr); widths = [W0 * f / tot for f in fr]
    note = s.get('note'); bar = s.get('bar'); bh = bar_h(bar)
    max_h = ((363 - bh - 10) if bar else 366) - sb.zy - (14 if note else 0)
    sb.table(X0, sb.zy, widths, s.get('rows', []), header=cols, header_style=s.get('header_style', 'dark'), font_size=s.get('font_size', 8),
             bold_first_col=s.get('bold_first_col', True), zebra=s.get('zebra', True), max_h=max_h, native=bool(s.get('native')))
    if note: sb.text(X0, sb.zy + sb.table_h + 5, W0, 9, note, size=6.5, color=GREY, ls=100)
    if bar: _bar(sb, 363 - bh, bar)
    return _finish(deck, sb, sid, s, n, footer)

def r_comparison_grid(deck, s, tag, n, footer):
    sid, sb = _content_base(deck, s, tag)
    y = sb.zy; qh = 0
    if s.get('quote'):
        qh = text_h(s['quote'], 8, 330, 115)
        sb.text(X0, y, 330, qh, s['quote'], size=8, color=MUTED, ls=115, italic=True)
    legend = s.get('legend') or ['Gap stays open', 'Partly closed', 'Closed']
    lx = 684
    for key, lab in reversed(list(zip(['open', 'partial', 'closed'], legend))):
        g, c = STATE_GLYPH[key]; w = text_width(lab, 6.5) + 14
        lx -= w
        sb.text(lx, y - 1, 10, 10, g, size=8, color=c, ls=100); sb.text(lx + 11, y, w - 11, 10, lab, size=6.5, color=MUTED, ls=100)
        lx -= 8
    y += max(qh, 12) + 6
    opts = s.get('options', [])[:3]; rows = s.get('rows', [])[:6]
    foot = s.get('footer') or []; closing = s.get('closing_line')
    hh = 26; pad = 9
    avail = 365 - (y + hh) - (18 if foot else 0) - ((text_h(closing, 7.5, W0 - 200, 112) + 6) if closing else 0) - 2
    def heights(c0, fs):
        cwid = (W0 - c0) / 3; out = []
        for r in rows:
            lh = text_h(r.get('label', ''), 7.5, (c0 - 15) * 0.9, 105, True) + (text_h(r.get('sub', ''), 6.5, (c0 - 15) * 0.9, 110) if r.get('sub') else 0)
            ch = max([text_h(c.get('text', ''), fs, (cwid - 29) * 0.95, 112) for c in r.get('cells', [])] + [0])
            out.append(max(lh, ch) + pad)
        return out
    choice = None
    for fs in (7.5, 7):
        for c0 in (157.5, 170, 180):
            hs = heights(c0, fs)
            if sum(hs) <= avail + 1: choice = (c0, fs, hs); break
        if choice: break
    if not choice:
        hs = heights(157.5, 7)
        raise FitError(f"slide {s.get('id')}: comparison_grid rows need {sum(hs):.0f} pt, have {avail:.0f} (7 pt, {len(rows)} rows)")
    c0, fs, hs = choice; cwid = (W0 - c0) / 3
    heads = [(X0, c0, BLUE, WHITE, WHITE)] + [(X0 + c0 + i * cwid, cwid, (DEEP if i == 2 else PANEL), (PALE if i == 2 else GREY), (WHITE if i == 2 else INK)) for i in range(3)]
    for i, (hx, hw, fill, c_sub, c_main) in enumerate(heads):
        sb.rect(hx, y, hw, hh, fill=fill)
        if i == 0:
            sb.text(hx + 7.5, y + 3.5, hw - 15, 9, (s.get('row_header') or 'THE GAP').upper(), size=6.5, color=WHITE, ls=100)
            sb.text(hx + 7.5, y + 13, hw - 15, 11, s.get('row_header_sub') or 'Where the current setup breaks', size=7.5, bold=True, color=WHITE, ls=100)
        else:
            o = opts[i - 1] if i - 1 < len(opts) else {}
            sb.text(hx + 7.5, y + 3.5, hw - 15, 9, (o.get('sub') or '').upper(), size=6.5, color=c_sub, ls=100)
            sb.text(hx + 7.5, y + 13, hw - 15, 11, o.get('header') or '', size=7.5, bold=True, color=c_main, ls=100)
    y += hh; sb.hairline(X0, y, W0, alpha=0.24)
    for ri, (r, rh) in enumerate(zip(rows, hs)):
        sb.rect(X0, y, c0, rh, fill=PANEL)
        lh = text_h(r.get('label', ''), 7.5, (c0 - 15) * 0.9, 105, True)
        sb.text(X0 + 7.5, y + pad / 2, c0 - 15, lh, r.get('label', ''), size=7.5, bold=True, color=BLUE, ls=105)
        if r.get('sub'): sb.text(X0 + 7.5, y + pad / 2 + lh, c0 - 15, rh - pad - lh, r['sub'], size=6.5, color=GREY, ls=110)
        for ci in range(3):
            cx = X0 + c0 + ci * cwid; cell = r.get('cells', [])[ci] if ci < len(r.get('cells', [])) else {}
            fill = PANEL if ci == 2 else (WHITE if ri % 2 == 0 else PANEL2)
            sb.rect(cx, y, cwid, rh, fill=fill)
            g, gc = STATE_GLYPH.get(cell.get('state', 'open'), STATE_GLYPH['open'])
            sb.text(cx + 7.5, y + pad / 2 - 1, 12, 12, g, size=9, color=gc, ls=100)
            sb.text(cx + 21.5, y + pad / 2, cwid - 29, rh - pad, cell.get('text', ''), size=fs, bold=(ci == 2), color=INK, ls=112)
        y += rh
    if foot:
        sb.hairline(X0, y, W0, alpha=0.24)
        first = foot[0] if foot and isinstance(foot[0], dict) else {}
        sb.rect(X0, y, c0, 18, fill=PANEL); sb.text(X0 + 7.5, y + 4.5, c0 - 15, 10, first.get('label') or 'Gaps closed', size=6.5, bold=True, color=INK, ls=100)
        vals = []
        for f in foot:
            if isinstance(f, dict):
                if 'value' in f: vals.append(f['value'])
            else: vals.append(str(f))
        if len(vals) < 3 and all(isinstance(f, dict) and 'label' in f for f in foot) and len(foot) >= 4: vals = [f.get('value') or f.get('label') for f in foot[1:4]]
        for ci in range(3):
            cx = X0 + c0 + ci * cwid
            sb.rect(cx, y, cwid, 18, fill=(PANEL if ci == 2 else PANEL2))
            sb.text(cx + 7.5, y + 4.5, cwid - 15, 10, str(vals[ci]) if ci < len(vals) else '', size=6.5, bold=True, color=DEEP, ls=100)
        y += 18
    if closing:
        ch = text_h(closing, 7.5, W0 - 200, 112)
        sb.text(X0 + 200, y + 5, W0 - 200, ch, closing, size=7.5, color=INK, align='END', ls=112)
    return _finish(deck, sb, sid, s, n, footer)

def r_diagram(deck, s, tag, n, footer):
    sid, sb = _content_base(deck, s, tag)
    side = s.get('side'); ox, oy = X0, sb.zy
    boxes = {}
    for b in s.get('boxes', []):
        x, y, w, h = ox + float(b['x']), oy + float(b['y']), float(b['w']), float(b['h'])
        if x + w > 684.5 or y + h > 366: raise FitError(f"slide {s.get('id')}: diagram box '{b.get('id')}' leaves the content zone")
        boxes[b['id']] = (x, y, w, h)
    obstacles = [v for k, v in boxes.items() if next((b for b in s.get('boxes', []) if b['id'] == k), {}).get('style') != 'label']
    for c in s.get('connectors', []):
        if c['from'] in boxes and c['to'] in boxes: sb.connector(boxes[c['from']], boxes[c['to']], c.get('label'), obstacles=obstacles)
    for b in s.get('boxes', []):
        x, y, w, h = boxes[b['id']]
        sb.diagram_box(x, y, w, h, b.get('title'), b.get('body'), b.get('pill'), b.get('style', 'light'))
    if side: _side_column(sb, X0 + 440, sb.zy, 684 - (X0 + 440), sb.zh, side)
    return _finish(deck, sb, sid, s, n, footer)

def r_code_before_after(deck, s, tag, n, footer):
    sid, sb = _content_base(deck, s, tag)
    side = s.get('side'); L, M, Rr = s.get('left', {}), s.get('middle', {}), s.get('right', {})
    if side: lw, mw, rw, sw = 196, 52, 196, 164; xs = [X0, X0 + lw + 10, X0 + lw + 10 + mw + 10]; sx = xs[2] + rw + 20
    else: lw, mw, rw = 276, 72, 276; xs = [X0, X0 + lw + 12, X0 + lw + 12 + mw + 12]; sx = None
    cap_h = text_h(Rr.get('caption', ''), 6.5, rw, 100) if Rr.get('caption') else 0
    code_h = min(230, 365 - sb.zy - 14 - (cap_h + 8 if cap_h else 0)); size = 7.5
    for code, wdt in ((L.get('code', ''), lw), (Rr.get('code', ''), rw)):
        lines = code.split('\n')
        if max((text_width(l, size, False) * 1.15 for l in lines), default=0) > wdt - 24: size = 7
        if mono_h(code, size) + 20 > code_h: raise FitError(f"slide {s.get('id')}: code block needs {mono_h(code, size) + 20:.0f} pt, has {code_h}")
    sb.code_block(xs[0], sb.zy, lw, code_h + 14, L.get('code', ''), size=size, title=L.get('title'))
    sb.code_block(xs[2], sb.zy, rw, code_h + 14, Rr.get('code', ''), size=size, title=Rr.get('title'))
    my = sb.zy + 14 + code_h / 2 - 30
    if M.get('title'): sb.text(xs[1], my, mw, 24, M['title'], size=8, bold=True, color=INK, align='CENTER', ls=105)
    sb.text(xs[1], my + 26, mw, 20, '→', size=16, color=LBLUE, align='CENTER', ls=100)
    if M.get('sub'): sb.text(xs[1], my + 48, mw, 30, M['sub'], size=6.5, color=GREY, align='CENTER', ls=110)
    if Rr.get('caption'): sb.text(xs[2], sb.zy + code_h + 19, rw, cap_h, Rr['caption'], size=6.5, color=GREY, ls=100)
    if side: _side_column(sb, sx, sb.zy, 684 - sx, sb.zh, side)
    return _finish(deck, sb, sid, s, n, footer)

def r_phases(deck, s, tag, n, footer):
    sid, sb = _content_base(deck, s, tag)
    cards = s.get('cards', [])[:3]; bar = s.get('bar'); N = max(len(cards), 1)
    gap = 26; cw = (W0 - gap * (N - 1)) / N; y = sb.zy; bh = bar_h(bar); max_h = (363 - bh - 12 - y) if bar else (362 - y)
    need = 0
    for i, c in enumerate(cards):
        cwi = cw - 28
        nh = 12 + 18 + text_h(c.get('title', ''), 10, cwi, 105, True) + 4 + text_h(c.get('body', ''), 8.5, cwi, 115) + ((text_h(c.get('exit', ''), 8, cwi, 112) + 16 + 6) if c.get('exit') else 0) + 12
        need = max(need, nh)
    if need > max_h + 1: raise FitError(f"slide {s.get('id')}: phase cards need {need:.0f} pt, have {max_h:.0f} pt")
    h = max(110.0, min(need, max_h)) if bar else max_h
    sb.rect(X0, y, W0, h, fill=PANEL3)
    for i, c in enumerate(cards):
        x = X0 + i * (cw + gap); cy = y + 12; cx, cwi = x + 14, cw - 28
        sb.text(cx, cy, cwi, 12, c.get('eyebrow') or f"{i + 1:02d}", size=9, color=LBLUE, font=MONO, ls=100); cy += 18
        th = text_h(c.get('title', ''), 10, cwi, 105, True); sb.text(cx, cy, cwi, th, c.get('title', ''), size=10, bold=True, color=DEEP, ls=105); cy += th + 4
        eh = (text_h(c.get('exit', ''), 8, cwi, 112) + 16) if c.get('exit') else 0
        bh = text_h(c.get('body', ''), 8.5, cwi, 115)
        if cy + bh + eh > y + h - 10: raise FitError(f"slide {s.get('id')}: phase card {i + 1} overflows")
        sb.text(cx, cy, cwi, bh, c.get('body', ''), size=8.5, color=BODY3, ls=115)
        if c.get('exit'):
            ey = y + h - 12 - eh + 4
            sb.hairline(cx, ey - 6, cwi)
            sb.text(cx, ey, cwi, 10, (c.get('exit_label') or 'EXIT CRITERIA').upper(), size=6.5, bold=True, color=BLUE, ls=100)
            sb.text(cx, ey + 11, cwi, eh - 14, c['exit'], size=8, color=INK, ls=112)
        if i < N - 1: sb.text(x + cw + 2, y + h / 2 - 10, gap - 4, 20, '→', size=14, color=LBLUE, align='CENTER', ls=100)
    _bar(sb, y + h + 12, bar)
    return _finish(deck, sb, sid, s, n, footer)

def r_next_steps(deck, s, tag, n, footer):
    sid, sb = _content_base(deck, s, tag)
    cards = s.get('cards', [])[:3]; N = max(len(cards), 1)
    gap = 12; cw = (W0 - gap * (N - 1)) / N; y = sb.zy
    max_h = (365 - y - 46) if s.get('contact') else (365 - y)
    need = max([card_need(cw, c.get('eyebrow'), c.get('num'), c.get('title'), c.get('body')) for c in cards] + [0])
    if need > max_h + 1: raise FitError(f"slide {s.get('id')}: next_steps cards need {need:.0f} pt, have {max_h:.0f} pt")
    h = max(110.0, min(need, max_h)) if s.get('contact') else max_h
    for i, c in enumerate(cards):
        sb.card(X0 + i * (cw + gap), y, cw, h, eyebrow=c.get('eyebrow'), num=c.get('num'), title=c.get('title'), body=c.get('body'))
    if s.get('contact'):
        sb.rect(X0, y + h + 16, W0, 30, fill=BLUE)
        sb.text(X0 + 14, y + h + 16 + 9, W0 - 28, 12, s['contact'], size=9, color=WHITE, ls=100)
    return _finish(deck, sb, sid, s, n, footer)

def r_sources(deck, s, tag, n, footer):
    sid, sb = _content_base(deck, s, tag)
    cols = s.get('cols', [])[:2]; gap = 24; cw = (W0 - gap) / 2
    for i, col in enumerate(cols):
        x = X0 + i * (cw + gap); cy = sb.zy
        if col.get('header'):
            hw = text_width(col['header'].upper(), 7.5, True) + 6
            sb.text(x, cy, hw, 11, col['header'].upper(), size=7.5, bold=True, color=BLUE, ls=100)
            if col.get('pill'): sb.pill(x + hw + 4, cy - 3, col['pill'])
            cy += 14; sb.hairline(x, cy, cw); cy += 8
        items = col.get('items', [])
        fs = 7.5
        hs = [text_h(_item_text(it)[0], fs, cw - 18, 112) for it in items]
        if cy + sum(h + 4 for h in hs) > 352:
            fs = 7; hs = [text_h(_item_text(it)[0], fs, cw - 18, 110) for it in items]
            if cy + sum(h + 3 for h in hs) > 352: raise FitError(f"slide {s.get('id')}: sources column {i + 1} overflows")
        for k, (it, h) in enumerate(zip(items, hs)):
            t, pl = _item_text(it)
            sb.text(x, cy + 0.5, 16, 9, f"{k + 1:02d}", size=6.5, color=LBLUE, font=MONO, ls=100)
            sb.text(x + 18, cy, cw - 18, h, t, size=fs, color=BODY2, ls=112); cy += h + 4
    if s.get('footnote'): sb.text(X0, 357, W0, 9, s['footnote'], size=6.5, color=GREY, ls=100)
    return _finish(deck, sb, sid, s, n, footer)

def r_closing(deck, s, tag, n):
    sid, m = deck.duplicate(BASE['closing'], tag); sb = SB(deck, sid, tag, m, dark=True)
    sb.delete([m[ROLE[46]['icon']]])
    sb.R += replace_text_requests(sb._tpl_el(46, ROLE[46]['title']), s.get('line') or "Let's grow together")
    lines = []
    if s.get('name') or s.get('title'): lines.append(('**%s**' % s.get('name', '')) + (' | ' + s['title'] if s.get('title') else ''))
    if s.get('phone'): lines.append('**%s**' % s['phone'])
    if s.get('email'): lines.append('**%s**' % s['email'])
    sb.R += replace_text_requests(sb._tpl_el(46, ROLE[46]['body']), '\n'.join(lines), size=11, color=WHITE)
    sb.flush('closing text')
    # lockup: cover the layout's "yuno |" (x 540..615, y 195..220) and redraw `yuno | OnlyFans` right-aligned to x 684
    url = deck.wordmark_url(); lh = 14.0; lw = lh * LOGO_ASPECT; ww = lh / 16.0 * 59.2   # cover wordmark is 59.2 x 16.0 pt
    logo_x = 684 - lw; bar_x = logo_x - 13; wm_x = bar_x - 13 - ww; y = 199.4 + (16.4 - lh) / 2
    try:
        if not url: raise RuntimeError('no wordmark url')
        sb.rect(528, 186, 192, 44, fill=BLACK)
        sb.image(url, wm_x, y, ww, lh)
        sb.rect(bar_x, y - 1.5, 1.3, lh + 3, fill=WHITE)
        sb.image(s.get('logo_url') or LOGO_URL, logo_x, y, lw, lh)
        sb.flush('closing lockup')
    except Exception as e:
        print('  closing lockup fallback (layout wordmark kept):', str(e)[:140])
        sb.R = []; sb.post = []
        lh2 = 12.0; lw2 = lh2 * LOGO_ASPECT
        sb.image(s.get('logo_url') or LOGO_URL, 632.5, 199.4 + (16.4 - lh2) / 2, lw2, lh2)
        sb.flush('closing lockup fallback')
    deck.set_notes(sid, s.get('notes')); return sid

TEMPLATE_BY_REF = {'yuno-story': 22, 'yuno_story': 22, 'four-pillars': 23, 'four_pillars': 23, 'pillars': 23, 'offices': 24, 'global-presence': 24,
                   'trusted': 25, 'trusted-by': 25, 'trusted_by': 25, 'logos': 25, 'team': 26, 'leadership': 26, 'dedicated': 27, 'dedicated-team': 27,
                   'awards': 38, 'coverage': 40, 'credentials': 41, 'quotes': 42, 'compliance': 45}
HIDDEN_JUNK = {22: ['g3f76accd9b2_0_1750']}   # invisible "Happy Easter" text box on the Yuno story slide

def resolve_template_index(s):
    ti = int(s.get('template_index') or 0)
    ref = (s.get('template_ref') or s.get('id') or '').lower()
    want = TEMPLATE_BY_REF.get(ref)
    if 'SPACEX_LOGO_OBJECT_ID' in (s.get('delete_images_matching') or []) or SPACEX_LOGO in (s.get('delete_images_matching') or []): want = 25
    if want and want != ti:
        print(f"  WARNING slide {s.get('id')}: template_index {ti} is '{_kind(ti)}' in template_dump order; using {want} ('{_kind(want)}') from the slide id")
        return want
    return ti

def _kind(i):
    return {22: 'Yuno story stats', 23: 'four pillars', 24: 'offices map', 25: 'trusted-by logos', 26: 'team', 27: 'dedicated team', 28: 'divider 05',
            29: 'marketplace hero', 38: 'awards', 40: 'coverage', 41: 'credentials', 42: 'quotes', 45: 'compliance'}.get(i, f'slide {i}')

def r_template_keep(deck, s, tag, n, footer):
    ti = resolve_template_index(s); sid, m = deck.duplicate(ti, tag)
    src = deck.tpl_slides[ti - 1]
    dark = (src.get('pageProperties', {}).get('pageBackgroundFill', {}).get('solidFill', {}).get('color', {}).get('rgbColor', {'red': 1}) == {} or
            src.get('pageProperties', {}).get('pageBackgroundFill', {}).get('solidFill', {}).get('color', {}).get('themeColor') == 'DARK1')
    sb = SB(deck, sid, tag, m, dark=dark)
    for rep in s.get('replacements', []):
        find, repl = rep.get('find', ''), rep.get('replace', '')
        if not find: continue
        hit = False
        for el, tr in elements(src):
            t = text_of(el)
            if find in t:
                new_el = copy.deepcopy(el); new_el['objectId'] = m[el['objectId']]
                sb.R += replace_text_requests(new_el, t.rstrip('\n').replace(find, repl)); hit = True
        if not hit: print(f"  warning: template_keep find text not found on slide {ti}: {find!r}")
    for oid in list(s.get('delete_images_matching', []) or []) + HIDDEN_JUNK.get(ti, []):
        if oid == 'SPACEX_LOGO_OBJECT_ID': oid = SPACEX_LOGO
        if oid in m: sb.delete([m[oid]])
        else: print(f"  warning: element {oid} not on template slide {ti}")
    if s.get('kicker') and ti in ROLE and 'kicker' in ROLE[ti]: sb.kicker(s['kicker'], ti)
    sb.footer(footer, n)
    sb.flush(); deck.set_notes(sid, s.get('notes')); return sid

def r_logo_grid(deck, s, tag, n, footer):
    """Chips with a small logo and the name, flowing in rows; sections stack; an optional table sits under the chips.
    spec: sections=[{header, chips=[{name, logo, aspect}], muted}], table={columns, col_widths, rows, font_size}"""
    sid, sb = _content_base(deck, s, tag)
    y = sb.zy; CH, LH, PITCH, GAP, FS = 16.0, 10.0, 19.5, 4.0, 7.0
    for sec in s.get('sections', []):
        chips = sec.get('chips', [])
        if not chips: continue
        if sec.get('header'):
            sb.text(X0, y, W0, 9, sec['header'].upper(), size=6.5, bold=True, color=GREY, ls=100); y += 12
        muted = sec.get('muted'); fill = '#F3F3F3' if muted else '#F4F5FD'; tcol = GREY if muted else INK
        if sec.get('style') == 'signed': fill, tcol = '#E8EAF5', DEEP
        outline = '#BDC3F6' if sec.get('style') == 'request' else None
        if sec.get('style') == 'request': fill, tcol = WHITE, GREY
        x = X0
        for c in chips:
            lw = min(LH * float(c.get('aspect') or 1.0), 30.0) if c.get('logo') else 0.0
            tw = text_width(c['name'], FS); w = 6 + (lw + 5 if lw else 0) + tw + 7
            if x + w > X0 + W0 + 0.5: x = X0; y += PITCH
            if y + CH > 366: raise FitError(f"slide {s.get('id')}: chips overflow the zone")
            sb.round_rect(x, y, w, CH, fill=fill, outline=outline, outline_w=0.5)
            if lw: sb.image(c['logo'], x + 6, y + (CH - LH) / 2, lw, LH)
            sb.text(x + 6 + (lw + 5 if lw else 0), y + 1.5, tw + 8, CH - 3, c['name'], size=FS, color=tcol, ls=100, valign='MIDDLE')
            x += w + GAP
        y += PITCH + 4
    t = s.get('table')
    if t:
        y += 2
        cols = t.get('columns', []); fr = t.get('col_widths') or [1.0 / max(len(cols), 1)] * len(cols); tot = sum(fr)
        max_h = 366 - y
        if max_h < 40: raise FitError(f"slide {s.get('id')}: no room left for the table ({max_h:.0f} pt)")
        sb.table(X0, y, [W0 * f / tot for f in fr], t.get('rows', []), header=cols, header_style=t.get('header_style', 'dark'),
                 font_size=t.get('font_size', 7.5), bold_first_col=True, zebra=True, max_h=max_h, native=bool(t.get('native')))
    return _finish(deck, sb, sid, s, n, footer)

# ---------------------------------------------------------------- Carry1st renderers (15 Oct 2026): pricing_cards, country_deepdive, bar_chart
def _kv_rows(sb, x, y, w, rows, size=7.5, label_color=INK, value_color=INK, bold_value=True, pitch=None, value_w=None):
    """label left, value right-aligned (bold). rows: [[label, value], ...]. Returns height used."""
    cy = y; pitch = pitch or (size * 1.21 + 4)
    vw = value_w or max(text_width(str(r[1]), size, True) for r in rows) + 6
    for lab, val in rows:
        sb.text(x, cy, w - vw - 4, pitch, str(lab), size=size, color=label_color, ls=100)
        sb.text(x + w - vw, cy, vw, pitch, str(val), size=size, bold=bold_value, color=value_color, align='END', ls=100)
        cy += pitch
    return cy - y

def r_pricing_cards(deck, s, tag, n, footer):
    """Three-card proposal slide (Yango format): left TRANSACTION FEE (tranches), middle PLATFORM FEE (big figure + includes + add-ons),
    right blue WHAT IT MEANS FOR <merchant> (mini table + callout + paragraph). spec keys: subline, left, middle, right, source, notes."""
    sid, sb = _content_base(deck, s, tag)
    y = sb.zy
    if s.get('subline'):
        sh = text_h(s['subline'], 8, W0, 110); sb.text(X0, y, W0, sh, s['subline'], size=8, color=MUTED, ls=110); y += sh + 4
    y0 = y; H = 363 - y0; gap = 10
    wl, wm = round((W0 - 2 * gap) * 0.28), round((W0 - 2 * gap) * 0.30); wr = W0 - 2 * gap - wl - wm
    xl, xm, xr = X0, X0 + wl + gap, X0 + wl + gap + wm + gap
    pad = 11
    # ---- left card
    L = s.get('left', {}); sb.rect(xl, y0, wl, H, fill=WHITE, outline=DEEP)
    cx, cw, cy = xl + pad, wl - 2 * pad, y0 + pad - 1
    sb.text(cx, cy, cw, 11, (L.get('title') or 'TRANSACTION FEE').upper(), size=8, bold=True, color=DEEP, ls=100); cy += 14
    if L.get('sub'):
        sh = text_h(L['sub'], 7, cw, 110); sb.text(cx, cy, cw, sh, L['sub'], size=7, color=GREY, ls=110); cy += sh + 6
    for r in L.get('rows', []):
        sb.hairline(cx, cy, cw); cy += 4
        sb.text(cx, cy, cw * 0.62, 9, (r.get('label') or '').upper(), size=6.5, bold=True, color=GREY, ls=100)
        rate = r.get('rate') or ''; rs = 12
        while rs > 9 and text_width(rate, rs, True) > cw * 0.38: rs -= 1
        sb.text(cx + cw * 0.6, cy - 1, cw * 0.4, rs * 1.3, rate, size=rs, bold=True, color=BLUE, align='END', ls=100)
        rh = text_h(r.get('range') or '', 7.5, cw * 0.62, 108); sb.text(cx, cy + 9, cw * 0.62, rh, r.get('range') or '', size=7.5, color=INK, ls=108)
        cy += max(9 + rh, rs * 1.25) + (3 if len(L.get('rows', [])) <= 4 else 1)   # tighter pitch for a fifth row (pricing v4)
    if L.get('note'):
        nh = text_h(L['note'], 7, cw - 14, 112) + 12
        ny = y0 + H - pad - nh
        if ny < cy + 4: raise FitError(f"slide {s.get('id')}: left card note does not fit ({ny - cy:.0f} pt)")
        sb.rect(cx, ny, cw, nh, fill=PANEL2); sb.text(cx + 7, ny + 6, cw - 14, nh - 12, L['note'], size=7, color=BODY3, ls=112)
    elif cy > y0 + H - pad + 2: raise FitError(f"slide {s.get('id')}: left card overflows by {cy - (y0 + H - pad):.0f} pt")
    # ---- middle card
    M = s.get('middle', {}); sb.rect(xm, y0, wm, H, fill=PANEL)
    cx, cw, cy = xm + pad, wm - 2 * pad, y0 + pad - 1
    sb.text(cx, cy, cw, 11, (M.get('title') or 'PLATFORM FEE').upper(), size=8, bold=True, color=DEEP, ls=100); cy += 14
    val = M.get('value') or ''; vw = text_width(val, 22, True) + 2
    sb.text(cx, cy, vw + 4, 28, val, size=22, bold=True, color=BLUE, ls=90)
    if M.get('unit'): sb.text(cx + vw + 4, cy + 11, cw - vw - 4, 12, M['unit'], size=8, color=GREY, ls=100)
    cy += 28
    if M.get('sub'):
        sh = text_h(M['sub'], 7, cw, 110); sb.text(cx, cy, cw, sh, M['sub'], size=7, color=GREY, ls=110); cy += sh + 5
    foot_h = (text_h(M['foot'], 6.5, cw, 110) + 4) if M.get('foot') else 0
    add = dict(M.get('addons') or {}); add_rows = add.get('rows', [])
    inc = M.get('includes', []); fitted = False
    def _add_h(a):
        return (8 + 11 + ((text_h(a.get('sub'), 6.5, cw - 14, 110) + 2) if a.get('sub') else 0) + len(a.get('rows', [])) * (7 * 1.21 + 2.5) + 8) if a else 0
    for step in range(3):                      # 1 shrink the rows, 2 drop the add-ons sub-line, 3 drop the foot
        fs = 7.5
        while fs >= 6.5:
            pitch = fs * 1.21 + 2.5; inc_h = (11 if inc else 0) + len(inc) * pitch
            if cy + inc_h + 6 + _add_h(add) + foot_h <= y0 + H - pad: fitted = True; break
            fs -= 0.5
        if fitted: break
        if step == 0 and add.get('sub'): add.pop('sub')
        elif step == 1 and foot_h: foot_h = 0; M = dict(M); M.pop('foot', None)
    if not fitted: raise FitError(f"slide {s.get('id')}: middle card overflows (includes {len(inc)} rows, add-ons {len(add_rows)}); merge rows")
    add_h = _add_h(add)
    if inc:
        sb.text(cx, cy, cw, 9, (M.get('includes_label') or 'WHAT IT INCLUDES').upper(), size=6.5, bold=True, color=GREY, ls=100); cy += 11
        cy += _kv_rows(sb, cx, cy, cw, inc, size=fs, pitch=pitch)
    if add:
        cy += 6; ay = cy
        sb.rect(cx, ay, cw, add_h, fill=WHITE)
        iy = ay + 7; sb.text(cx + 7, iy, cw - 14, 9, (add.get('title') or 'ADD-ONS').upper(), size=6.5, bold=True, color=DEEP, ls=100); iy += 11
        if add.get('sub'):
            sh = text_h(add['sub'], 6.5, cw - 14, 110); sb.text(cx + 7, iy, cw - 14, sh, add['sub'], size=6.5, color=GREY, ls=110); iy += sh + 2
        _kv_rows(sb, cx + 7, iy, cw - 14, add_rows, size=7, pitch=7 * 1.21 + 2.5)
        cy = ay + add_h
    if M.get('foot'):
        sb.text(cx, y0 + H - pad - foot_h + 4, cw, foot_h - 4, M['foot'], size=6.5, color=GREY, ls=110)
    # ---- right card (blue)
    Rc = s.get('right', {}); sb.rect(xr, y0, wr, H, fill=BLUE)
    cx, cw, cy = xr + pad, wr - 2 * pad, y0 + pad - 1
    sb.text(cx, cy, cw, 11, (Rc.get('title') or 'WHAT IT MEANS').upper(), size=8, bold=True, color=WHITE, ls=100); cy += 14
    if Rc.get('sub'):
        sh = text_h(Rc['sub'], 7, cw, 110); sb.text(cx, cy, cw, sh, Rc['sub'], size=7, color=PALE, ls=110); cy += sh + 6
    cols = Rc.get('columns') or []; rows = Rc.get('rows') or []
    if cols:
        fr = Rc.get('col_widths') or ([2.2] + [1.0] * (len(cols) - 1)); tot = sum(fr); ws = [cw * f / tot for f in fr]
        tfs = Rc.get('font_size', 7.5); pitch = tfs * 1.21 + 4
        xx = cx
        for j, c in enumerate(cols):
            sb.text(xx, cy, ws[j], 9, str(c).upper(), size=6.5, bold=True, color=PALE, align=('START' if j == 0 else 'END'), ls=100); xx += ws[j]
        cy += 11; sb.hairline(cx, cy - 2, cw, color=WHITE, alpha=0.35)
        for r in rows:
            bold = isinstance(r, dict) and r.get('bold'); cells = r['cells'] if isinstance(r, dict) else r
            if bold: sb.hairline(cx, cy - 1, cw, color=WHITE, alpha=0.35)
            xx = cx
            for j, c in enumerate(cells):
                sb.text(xx, cy + 1, ws[j], pitch, str(c), size=tfs, bold=bool(bold), color=WHITE, align=('START' if j == 0 else 'END'), ls=100); xx += ws[j]
            cy += pitch
        cy += 4
    if Rc.get('callout'):
        ch = text_h(Rc['callout'], 8, cw - 16, 112, True) + 12
        sb.rect(cx, cy, cw, ch, fill=DEEP); sb.text(cx + 8, cy + 6, cw - 16, ch - 12, Rc['callout'], size=8, bold=True, color=WHITE, ls=112); cy += ch + 6
    if Rc.get('paragraph'):
        ph = text_h(Rc['paragraph'], 7, cw, 112); sb.text(cx, cy, cw, ph, Rc['paragraph'], size=7, color=WHITE, ls=112); cy += ph
    if cy > y0 + H - pad + 2: raise FitError(f"slide {s.get('id')}: right card overflows by {cy - (y0 + H - pad):.0f} pt")
    return _finish(deck, sb, sid, s, n, footer)

def r_country_deepdive(deck, s, tag, n, footer):
    """Suno/Higgsfield country slide: flag next to the kicker, 4-cell stat bar (deep blue), three numbered lever cards,
    bottom row = method priority table (left) + 'what it means' box (right), SO WHAT band. spec keys: flag, stats[4], levers[3],
    table{columns,col_widths,rows,font_size}, box{header,items[{title,body}]}, sowhat, source, notes."""
    sid, sb = _content_base(deck, s, tag)
    if s.get('flag'):
        kw = text_width((s.get('kicker') or '').upper(), 7) + 6
        sb.image(s['flag'], X0 + kw + 2, 24.6, 13.5, 9.5)
    y = sb.zy + 2
    # stat bar
    stats = s.get('stats', [])[:4]; N = max(len(stats), 1); bh = 46; cwid = W0 / N
    sb.rect(X0, y, W0, bh, fill=DEEP)
    for i, st in enumerate(stats):
        x = X0 + i * cwid
        if i: sb.vline(x, y + 6, bh - 12, color=WHITE, alpha=0.25)
        vs = 16
        while vs > 10 and text_width(st.get('value', ''), vs, True) > cwid - 20: vs -= 1
        sb.text(x + 10, y + 5, cwid - 20, 20, st.get('value', ''), size=vs, bold=True, color=WHITE, ls=95)
        sb.text(x + 10, y + 25, cwid - 20, 9, (st.get('label') or '').upper(), size=6.5, bold=True, color=PALE, ls=100)
        if st.get('caption'):
            if wrap_count(st['caption'], 6.5, cwid - 20) > 1: raise FitError(f"slide {s.get('id')}: stat caption {i + 1} wraps; shorten it")
            sb.text(x + 10, y + 34, cwid - 20, 9, st['caption'], size=6.5, color=ONDARK, ls=100)
    y += bh + 8
    # levers
    levers = s.get('levers', [])[:3]; N = max(len(levers), 1); g = 10; lw = (W0 - g * (N - 1)) / N; lh = 70
    for i, lv in enumerate(levers):
        x = X0 + i * (lw + g); sb.rect(x, y, lw, lh, fill=WHITE, outline=DEEP)
        sb.shape('ELLIPSE', x + 10, y + 8, 14, 14, fill=BLUE)
        sb.text(x + 10, y + 9.5, 14, 12, str(lv.get('num') or i + 1), size=7, bold=True, color=WHITE, align='CENTER', ls=100)
        sb.text(x + 29, y + 11, lw - 39, 9, (lv.get('label') or '').upper(), size=6.5, bold=True, color=GREY, ls=100)
        vs = 13
        while vs > 9 and text_width(lv.get('value', ''), vs, True) > lw - 20: vs -= 1
        sb.text(x + 10, y + 25, lw - 20, 16, lv.get('value', ''), size=vs, bold=True, color=INK, ls=100)
        sb.text(x + 10, y + 40, lw - 20, 10, lv.get('money', ''), size=8, bold=True, color=BLUE, ls=100)
        if lv.get('tactic'):
            th = text_h(lv['tactic'], 6.5, lw - 20, 108)
            if th > lh - 48: raise FitError(f"slide {s.get('id')}: lever {i + 1} tactic too long")
            sb.text(x + 10, y + 50, lw - 20, th, lv['tactic'], size=6.5, color=GREY, italic=True, ls=108)
    y += lh + 8
    # bottom row
    so = s.get('sowhat'); so_h = (max(20.0, text_h(so, 7.5, W0 - 80, 110) + 9)) if so else 0
    bottom = 363 - so_h - (8 if so else 0)
    avail = bottom - y
    if avail < 50: raise FitError(f"slide {s.get('id')}: no room for the bottom row ({avail:.0f} pt)")
    t = s.get('table'); box = s.get('box')
    tw = (W0 * 0.58) if box else W0; bx = X0 + tw + 12; bw = W0 - tw - 12
    if t:
        cols = t.get('columns', []); fr = t.get('col_widths') or [1.0 / max(len(cols), 1)] * len(cols); tot = sum(fr)
        if t.get('label'): sb.text(X0, y, tw, 9, t['label'].upper(), size=6.5, bold=True, color=GREY, ls=100)
        ty = y + (11 if t.get('label') else 0)
        sb.table(X0, ty, [tw * f / tot for f in fr], t.get('rows', []), header=cols, header_style=t.get('header_style', 'blue'),
                 font_size=t.get('font_size', 6.5), bold_first_col=True, zebra=True, max_h=bottom - ty, min_row=14, header_min=16, pad_y=3)
    if box:
        sb.rect(bx, y, bw, avail, fill=PANEL3)
        cy = y + 8; ix, iw = bx + 10, bw - 20
        if box.get('header'): sb.text(ix, cy, iw, 9, box['header'].upper(), size=6.5, bold=True, color=BLUE, ls=100); cy += 12
        for it in box.get('items', []):
            tt, bb = it.get('title'), it.get('body')
            if tt:
                th = text_h(tt, 7.5, iw, 105, True); sb.text(ix, cy, iw, th, tt, size=7.5, bold=True, color=INK, ls=105); cy += th
            if bb:
                bh2 = text_h(bb, 7, iw, 110); sb.text(ix, cy, iw, bh2, bb, size=7, color=BODY3, ls=110); cy += bh2 + 4
        if box.get('body'):
            bh2 = text_h(box['body'], 7, iw, 110); sb.text(ix, cy, iw, bh2, box['body'], size=7, color=BODY3, ls=110); cy += bh2
        if cy > y + avail - 4: raise FitError(f"slide {s.get('id')}: side box overflows by {cy - (y + avail - 4):.0f} pt")
    if so:
        sy = 363 - so_h; sb.rect(X0, sy, W0, so_h, fill=PANEL)
        sb.text(X0 + 10, sy + (so_h - 9) / 2, 44, 9, 'SO WHAT', size=7, bold=True, color=DEEP, ls=100)
        th = text_h(so, 7.5, W0 - 80, 110); sb.text(X0 + 56, sy + (so_h - th) / 2, W0 - 66, th, so, size=7.5, color=INK, italic=True, ls=110)
    return _finish(deck, sb, sid, s, n, footer)

def _fmt_num(v, unit):
    if unit == '$K': return f"${v:,.1f}K" if abs(v) < 100 else f"${v:,.0f}K"
    if unit == '%': return f"{v:.2f}%"
    return f"{v:,.0f}"

def r_bar_chart(deck, s, tag, n, footer):
    """Grouped bars drawn with rectangles. spec: series[{name,color}], groups[{label, values[], labels[]?}], unit ('$K' | '%' | ''),
    side{header,items}, bar (band), note (small line under the x axis), source, notes. Negative values hang below the baseline."""
    sid, sb = _content_base(deck, s, tag)
    series = s.get('series', []); groups = s.get('groups', []); unit = s.get('unit', '')
    if not series or not groups: raise FitError(f"slide {s.get('id')}: bar_chart needs series and groups")
    side = s.get('side'); band = s.get('bar'); bh = bar_h(band)
    cx0 = X0; cw = (W0 * 0.64) if side else W0; top = sb.zy + 4; bottom = (363 - bh - 12) if band else 362
    # legend
    lx = cx0; ly = top
    for sr in series:
        sb.rect(lx, ly + 2, 7, 7, fill=sr.get('color') or BLUE); tw = text_width(sr['name'], 6.5) + 6
        sb.text(lx + 10, ly, tw + 4, 10, sr['name'], size=6.5, color=MUTED, ls=100); lx += 10 + tw + 10
    chart_top = top + 18; axis_y_space = 22; note_h = (text_h(s['note'], 6.5, cw, 108) + 4) if s.get('note') else 0
    chart_bottom = bottom - axis_y_space - note_h
    vals = [v for g in groups for v in g.get('values', [])]
    vmax = max(max(vals), 0); vmin = min(min(vals), 0); span = (vmax - vmin) or 1.0
    H = chart_bottom - chart_top - 12   # room for value labels above the tallest bar
    base_y = chart_top + 12 + (vmax / span) * H
    G = len(groups); S = len(series); gw = cw / G; bw = min(26.0, (gw * 0.72) / S); inner = bw * S + 3 * (S - 1); gx0 = (gw - inner) / 2
    sb.hairline(cx0, base_y, cw, alpha=0.4)
    for gi, g in enumerate(groups):
        for si, v in enumerate(g.get('values', [])[:S]):
            x = cx0 + gi * gw + gx0 + si * (bw + 3); h = abs(v) / span * H
            y = base_y - h if v >= 0 else base_y
            if h > 0.5: sb.rect(x, y, bw, h, fill=series[si].get('color') or BLUE)
            lab = (g.get('labels') or [None] * S)[si] if g.get('labels') else _fmt_num(v, unit)
            if lab:
                ly2 = (y - 10) if v >= 0 else (y + h + 1)
                sb.text(x - 8, ly2, bw + 16, 9, str(lab), size=6.5, bold=True, color=INK, align='CENTER', ls=100)
        sb.text(cx0 + gi * gw, chart_bottom + 4, gw, 9, g.get('label', ''), size=7, bold=True, color=MUTED, align='CENTER', ls=100)
        if g.get('sub'): sb.text(cx0 + gi * gw, chart_bottom + 13, gw, 9, g['sub'], size=6.5, color=GREY, align='CENTER', ls=100)
    if s.get('note'): sb.text(cx0, bottom - note_h + 2, cw, note_h, s['note'], size=6.5, color=GREY, ls=108)
    if side:
        sx = X0 + cw + 18; _side_column(sb, sx, top, 684 - sx, bottom - top, side)
    _bar(sb, 363 - bh, band)
    return _finish(deck, sb, sid, s, n, footer)


def r_lever_grid(deck, s, tag, n, footer):
    """Luni-format value levers (15 Oct 2026). spec: groups[{label, span}], row_labels[4], levers[{num, name, range, body,
    conservative, optimistic}], assumptions (markup, '**Assumptions**' lead), closing (blue line), source, notes."""
    sid, sb = _content_base(deck, s, tag)
    levers = s.get('levers', [])[:5]; L = max(len(levers), 1)
    lab_w = 60.0; gx = X0 + lab_w + 6; gap = 6.0; gw = 684 - gx; cw = (gw - gap * (L - 1)) / L
    y = sb.zy
    # group headers: pale band with a blue rule underneath, spanning their columns
    ci = 0
    for g in s.get('groups', []):
        span = int(g.get('span', 1)); x = gx + ci * (cw + gap); w = span * cw + (span - 1) * gap
        sb.rect(x, y, w, 16, fill=PANEL); sb.rect(x, y + 15.4, w, 0.8, fill=LBLUE)
        sb.text(x, y + 4.2, w, 9, g.get('label', ''), size=7, bold=True, color=INK, align='CENTER', ls=100)
        ci += span
    y += 21
    body_w = cw - 16
    bh = max(text_h(l.get('body', ''), 6.8, body_w, 118) for l in levers) if levers else 0
    card_h = 40 + bh + 8
    # bottom-up budget
    closing = s.get('closing'); ch = text_h(closing, 8, W0, 110) if closing else 0
    assum = s.get('assumptions'); ah = (text_h(assum, 6.5, W0 - 20, 118) + 10) if assum else 0
    src_top = 369.5 - (wrap_count(s.get('source'), 6.5, W0 * 0.9) - 1) * 8.5 if s.get('source') else 372
    row_h = 23.0
    need = card_h + 3 + row_h + 3 + row_h + 8 + ah + (6 + ch if closing else 0)
    if y + need > src_top - 4:
        raise FitError(f"slide {s.get('id')}: lever_grid needs {need:.0f} pt, zone has {src_top - 4 - y:.0f} pt")
    labels = s.get('row_labels') or ['Lever', 'How it works', 'Conservative', 'Optimistic']
    sb.text(X0, y + 8, lab_w, 9, labels[0], size=7, bold=True, color=INK, align='END', ls=100)
    sb.text(X0, y + 24, lab_w, 9, labels[1], size=7, bold=True, color=INK, align='END', ls=100)
    r1 = y + card_h + 3; r2 = r1 + row_h + 3
    sb.text(X0, r1 + 7.5, lab_w, 9, labels[2], size=7, bold=True, color=INK, align='END', ls=100)
    sb.text(X0, r2 + 7.5, lab_w, 9, labels[3], size=7, bold=True, color=INK, align='END', ls=100)
    name_sz = next((z for z in (8.5, 8, 7.5, 7) if all(text_width(l.get('name', ''), z, True) <= cw - 32 for l in levers)), None)
    rng_sz = next((z for z in (14, 13, 12, 11, 10) if all(text_width(l.get('range', ''), z, True) <= cw - 18 for l in levers)), None)
    if not name_sz or not rng_sz: raise FitError(f"slide {s.get('id')}: lever_grid lever name or range too long for one line")
    for i, l in enumerate(levers):
        x = gx + i * (cw + gap)
        sb.rect(x, y, cw, card_h, fill=PANEL2)
        sb.text(x + 8, y + 7, cw - 30, 10, l.get('name', ''), size=name_sz, bold=True, color=INK, ls=100)
        cx = x + cw - 19; oid = sb.shape('ELLIPSE', cx, y + 6, 12, 12, fill=BLUE)
        sb.text(cx, y + 8.3, 12, 8, str(l.get('num', i + 1)), size=7, bold=True, color=WHITE, align='CENTER', ls=100)
        sb.text(x + 8, y + 20 + (14 - rng_sz) / 2, cw - 16, 17, l.get('range', ''), size=rng_sz, bold=True, color=INK, ls=100)
        sb.text(x + 8, y + 40, body_w, bh, l.get('body', ''), size=6.8, color=MUTED, ls=118)
        sb.rect(x, r1, cw, row_h, fill=PANEL2)
        sb.text(x, r1 + 6.5, cw, 11, l.get('conservative', ''), size=10, bold=True, color=INK, align='CENTER', ls=100)
        sb.rect(x, r2, cw, row_h, fill=PANEL)
        sb.text(x, r2 + 6.5, cw, 11, l.get('optimistic', ''), size=10, bold=True, color=BLUE, align='CENTER', ls=100)
    y = r2 + row_h + 8
    if assum:
        sb.rect(X0, y, W0, ah, fill='#EFF0F2')
        sb.text(X0 + 10, y + 5, W0 - 20, ah - 10, assum, size=6.5, color=MUTED, ls=118)
        y += ah + 6
    if closing:
        sb.text(X0, y, W0, ch, closing, size=8, bold=True, color=BLUE, align='CENTER', ls=110)
    return _finish(deck, sb, sid, s, n, footer)

def r_impact_table(deck, s, tag, n, footer):
    """Luni-format total impact (15 Oct 2026). The headline is drawn as a large blue title ('Total impact').
    spec: subline, columns[] (first = scenario, last = total), rows[{label, cells[], total, highlight}], hero{value, text (markup)},
    takeaways[{title, body}] (three), source, notes."""
    sid, sb = _content_base(deck, dict(s, headline=''), tag)
    sb.text(X0, 40, 602, 26, s.get('headline', ''), size=22, bold=True, color=INK, ls=100)   # black, as German set it on the live deck
    y = 70
    if s.get('subline'):
        sb.text(X0, y, W0, 10, s['subline'], size=8, color=MUTED, ls=110); y += 18
    cols = s.get('columns', []); rows = s.get('rows', []); C = len(cols)
    NT = int(s.get('n_totals', 1))          # trailing total columns (e.g. recurring a year, and 2027 with a one-off lever)
    fr = s.get('col_widths') or ([0.22] + [0.13] * (C - 1 - NT) + [0.26 / NT] * NT)
    tot = sum(fr); ws = [W0 * f / tot for f in fr]; xs = [X0 + sum(ws[:i]) for i in range(C)]
    hh, rh = 24.0, 30.0
    pad_h = 10 if NT == 1 else 6
    for j, c in enumerate(cols):
        last = j >= C - NT
        lab = c.upper() if (j == 0 or last) else c
        if text_width(lab, 6.8, (j == 0 or last)) > ws[j] - 2 * pad_h + 1:
            raise FitError(f"slide {s.get('id')}: impact_table header '{c}' too wide for its column")
        sb.rect(xs[j], y, ws[j], hh, fill=BLUE if last else DARK)
        if 0 < j: sb.vline(xs[j], y, hh, color=WHITE, alpha=0.18)
        sb.text(xs[j] + pad_h, y + 8, ws[j] - 2 * pad_h, 9, lab, size=6.8, bold=(j == 0 or last), color=WHITE,
                align='START' if j == 0 else 'END', ls=100)
    y += hh
    tw0 = sum(ws[C - NT:])
    for r in rows:
        hi = r.get('highlight')
        totals = r.get('totals') or [r.get('total', '')]
        if hi: sb.rect(X0, y, W0, rh, fill=BLUE)
        else:
            sb.rect(xs[C - NT], y, tw0, rh, fill=PANEL3); sb.hairline(X0, y + rh, W0 - tw0)
        tc = WHITE if hi else INK
        sb.text(xs[0] + 10, y + 10, ws[0] - 20, 10, r.get('label', ''), size=8.5, bold=True, color=tc, ls=100)
        for j, v in enumerate(r.get('cells', [])[:C - 1 - NT], 1):
            if hi and j > 0: sb.vline(xs[j], y, rh, color=WHITE, alpha=0.18)
            sb.text(xs[j] + 6, y + 10, ws[j] - 6 - pad_h, 10, v, size=8.5, color=tc, align='END', ls=100)
        for k, tv in enumerate(totals[:NT]):
            j = C - NT + k
            if k > 0: sb.vline(xs[j], y, rh, color=WHITE if hi else GREY, alpha=0.18 if hi else 0.35)
            sb.text(xs[j] + 6, y + 7.5, ws[j] - 6 - pad_h, 15, tv, size=13, bold=True, color=WHITE if hi else BLUE, align='END', ls=100)
        y += rh
    if s.get('table_note'):
        sb.text(X0, y + 4, W0, 9, s['table_note'], size=6.8, color=MUTED, ls=100); y += 12
    y += 12
    hero = s.get('hero')
    if hero:
        tw = W0 - 150 - 24; th = text_h(hero.get('text', ''), 8.5, tw, 125); hh2 = max(44.0, th + 18)
        sb.rect(X0, y, W0, hh2, fill=PANEL3)
        sb.text(X0 + 14, y + (hh2 - 26) / 2, 124, 26, hero.get('value', ''), size=24, bold=True, color=BLUE, ls=100)
        sb.vline(X0 + 146, y + 10, hh2 - 20, color=GREY, alpha=0.5)
        sb.text(X0 + 160, y + (hh2 - th) / 2, tw, th, hero.get('text', ''), size=8.5, color=INK, ls=125)
        y += hh2 + 16
    tk = s.get('takeaways', [])[:3]
    if tk:
        K = len(tk); g = 24.0; w = (W0 - g * (K - 1)) / K
        src_top = 369.5 - (wrap_count(s.get('source'), 6.5, W0 * 0.9) - 1) * 8.5 if s.get('source') else 372
        need = max(12 + text_h(t.get('body', ''), 7.2, w, 120) for t in tk)
        if y + need > src_top - 4: raise FitError(f"slide {s.get('id')}: impact_table takeaways need {need:.0f} pt, zone has {src_top - 4 - y:.0f} pt")
        for i, t in enumerate(tk):
            x = X0 + i * (w + g)
            sb.text(x, y, w, 10, t.get('title', ''), size=8, bold=True, color=INK, ls=100)
            sb.text(x, y + 13, w, need - 12, t.get('body', ''), size=7.2, color=MUTED, ls=120)
    return _finish(deck, sb, sid, s, n, footer)


RENDERERS = {
    'exec_summary': r_exec_summary, 'stats': r_stats, 'scale': r_scale, 'four_numbers': r_four_numbers, 'traffic_list': r_traffic_list,
    'cards_row': r_cards_row, 'two_column': r_two_column, 'table': r_table, 'checklist_table': r_table, 'open_items_table': r_table,
    'comparison_grid': r_comparison_grid, 'diagram': r_diagram, 'code_before_after': r_code_before_after, 'phases': r_phases,
    'next_steps': r_next_steps, 'logo_grid': r_logo_grid, 'sources': r_sources, 'template_keep': r_template_keep,
    'pricing_cards': r_pricing_cards, 'country_deepdive': r_country_deepdive, 'bar_chart': r_bar_chart,
    'lever_grid': r_lever_grid, 'impact_table': r_impact_table,
}

def validate(spec):
    errs = []
    ids = [s.get('id') for s in spec.get('slides', [])]
    if len(set(ids)) != len(ids): errs.append('duplicate slide ids')
    for s in spec.get('slides', []):
        t = s.get('type')
        if t not in RENDERERS and t not in ('cover', 'agenda', 'divider', 'closing'): errs.append(f"slide {s.get('id')}: unknown type {t}")
        if t in RENDERERS and t != 'template_keep':
            if not s.get('headline'): errs.append(f"slide {s.get('id')}: missing headline")
            if not s.get('kicker'): errs.append(f"slide {s.get('id')}: missing kicker")
        for p in s.get('tag') or []:
            if p.upper() not in PILLS: errs.append(f"slide {s.get('id')}: unknown pill {p}")
        blob = json.dumps(s, ensure_ascii=False)
        if '—' in blob or ' - ' in blob or 'no small feat' in blob.lower(): errs.append(f"slide {s.get('id')}: em dash, ' - ' or forbidden phrase in text")
    return errs

class DryDeck(Deck):
    """No API calls: duplicate/run/notes are simulated so renderers can be fit-checked offline."""
    def __init__(self):
        self.pid = PID; self.svc = None; self.tpl = json.load(open(TEMPLATE_DUMP)); self.tpl_slides = self.tpl['slides']
        self.pres = self.tpl; self.state = {'built': []}; self._n = N_TEMPLATE; self.log = []
    def fetch(self): return self.tpl
    def slide_ids(self): return ['x'] * self._n
    def run(self, reqs, label=''): self.log.append((label, len(reqs)))
    def duplicate(self, template_index, tag):
        src = self.tpl_slides[template_index - 1]; ids = [src['objectId']] + all_ids(src)
        idmap = {i: f"{tag}_{i}"[:50] for i in ids}; self._n += 1
        return idmap[src['objectId']], idmap
    def set_notes(self, slide_id, text): pass
    def save_state(self): pass
    def wordmark_url(self): return 'dry://wordmark'
    def chrome_image_url(self, suffix): return 'dry://' + suffix
    def has_template(self): return True
    def page(self, page_id): return {'pageElements': []}

def check_spec(spec_path):
    """Offline: validate + run every renderer against a DryDeck; print per-slide fit problems."""
    spec = json.load(open(spec_path)); errs = validate(spec)
    for e in errs: print('SPEC ', e)
    deck = DryDeck(); footer = spec.get('footer', ''); bad = 0
    for n, s in enumerate(spec['slides'], 1):
        tag = 'c%02d' % n; t = s['type']
        try:
            if t == 'cover': r_cover(deck, s, tag, n)
            elif t == 'agenda': r_agenda(deck, s, tag, n)
            elif t == 'divider': r_divider(deck, s, tag, n)
            elif t == 'closing': r_closing(deck, s, tag, n)
            else: RENDERERS[t](deck, s, tag, n, footer)
            print(f"ok    [{n:02d}] {t:18s} {s.get('id')}")
        except FitError as e:
            bad += 1; print(f"FIT   [{n:02d}] {t:18s} {s.get('id')}: {e}")
        except Exception as e:
            bad += 1; print(f"ERROR [{n:02d}] {t:18s} {s.get('id')}: {type(e).__name__}: {e}")
    print(f"{len(spec['slides']) - bad} ok, {bad} with problems"); return bad

NEEDS_TEMPLATE = {'cover', 'agenda', 'divider', 'closing', 'template_keep'}

def render_one(deck, s, tag, n, footer):
    t = s['type']
    if t in NEEDS_TEMPLATE and hasattr(deck, 'has_template') and not deck.has_template():
        raise FitError(f"slide {s.get('id')}: type {t} needs the template slides, which are gone after --final; rebuild it from a fresh template copy")
    if t == 'cover': return r_cover(deck, s, tag, n)
    if t == 'agenda': return r_agenda(deck, s, tag, n)
    if t == 'divider': return r_divider(deck, s, tag, n)
    if t == 'closing': return r_closing(deck, s, tag, n)
    return RENDERERS[t](deck, s, tag, n, footer)

def r_placeholder(deck, s, tag, n, footer, reason):
    """a slide that could not be laid out: chrome + a visible notice, so order and numbering hold until the copy is shortened"""
    sid, sb = _content_base(deck, s, tag)
    sb.rect(X0, sb.zy, W0, 60, fill='#FBEFD9')
    sb.text(X0 + 12, sb.zy + 8, W0 - 24, 12, 'CONTENT DOES NOT FIT · REBUILD AFTER SHORTENING THE COPY', size=8, bold=True, color='#9A5B00', ls=100)
    sb.text(X0 + 12, sb.zy + 24, W0 - 24, 30, reason, size=8, color=INK, ls=115)
    return _finish(deck, sb, sid, s, n, footer)

def build_from_spec(spec_path, final=False, only=None, replace=False):
    spec = json.load(open(spec_path))
    errs = validate(spec)
    if errs: raise SystemExit('spec errors:\n  ' + '\n  '.join(errs))
    deck = Deck(spec.get('presentation_id') or PID); deck.fetch()
    print(f"target presentation: {deck.pid} ({deck.pres.get('title')})")
    if len(deck.template_live_ids()) != N_TEMPLATE and not only:
        raise SystemExit(f'template incomplete in {deck.pid}: {len(deck.template_live_ids())} of {N_TEMPLATE} slides; point --pid at a fresh copy of the Eventbrite deck')
    footer = spec.get('footer', '')
    slides = spec['slides']
    built = []; problems = []
    for n, s in enumerate(slides, 1):
        if only and s.get('id') not in only: continue
        tag = 'n%02d' % n
        if replace:  # a fresh tag so ids never collide with any live slide (the state file is per process, the deck is the truth)
            live_now = deck.slide_ids(); k = 1
            while any(i.startswith(f"{tag}r{k}_") for i in live_now): k += 1
            tag = f"{tag}r{k}"
        t = s['type']; print(f"[{n:02d}] {t:18s} {s.get('id')}")
        try:
            render_one(DryDeck(), s, tag, n, footer)          # offline rehearsal, no API calls
            sid = render_one(deck, s, tag, n, footer)
        except FitError as e:
            print(f"  FIT PROBLEM: {e}"); problems.append((n, s.get('id'), str(e)))
            sid = r_placeholder(deck, s, tag + 'p', n, footer, str(e))
        built.append(sid)
        if replace:
            live = deck.slide_ids()
            rest = [i for i in live if i != sid]
            if not deck.has_template() and len(rest) == len(slides):
                old = [rest[n - 1]]   # finalized deck: the live position IS the spec index (ids keep the tag of an earlier index after slides were removed, 15 Oct 2026)
            else:
                old = [i for i in live if i != sid and re.match(rf"^n{n:02d}(r\d+)?p?_", i)]   # placeholders are tagged <tag>p
            if old:
                idx = live.index(old[0])
                deck.run([{'updateSlidesPosition': {'slideObjectIds': [sid], 'insertionIndex': idx}}] + [{'deleteObject': {'objectId': o}} for o in old], f'replace slide {n}')
                deck.state['built'] = [i for i in deck.state['built'] if i not in old]; deck.save_state()
    if final:
        tpl = deck.template_live_ids()
        if len(built) != len(slides): raise SystemExit('refusing --final on a partial build')
        if len(tpl) != N_TEMPLATE: raise SystemExit(f'refusing --final: {len(tpl)} of {N_TEMPLATE} template slides present')
        deck.delete_slides(tpl)
        deck.state['built'] = []; deck.state['finalized'] = time.strftime('%Y-%m-%d %H:%M'); deck.save_state()   # the build IS the deck now; cleanup must never touch it
        print(f"deleted {len(tpl)} template slides in one call; deck now has {len(deck.slide_ids())} slides")
    if problems:
        print('\nSLIDES THAT NEED SHORTER COPY (placeholder inserted):')
        for n, i, e in problems: print(f"  [{n:02d}] {i}: {e}")
    return built

def cleanup():
    deck = Deck()
    if len(deck.template_live_ids()) != N_TEMPLATE:
        raise SystemExit('refusing cleanup: the 46 template slides are not all present, so the built slides are the deck itself')
    live = set(deck.slide_ids()); ids = [s for s in deck.state.get('built', []) if s in live]
    if ids: deck.delete_slides(ids)
    deck.state['built'] = []; deck.save_state()
    print(f"removed {len(ids)} built slides; {len(deck.slide_ids())} remain")

if __name__ == '__main__':
    a = sys.argv[1:]
    if '--pid' in a:
        PID = a[a.index('--pid') + 1]; os.environ['OF_PID'] = PID
        del a[a.index('--pid'):a.index('--pid') + 2]
    if not a: print(__doc__); sys.exit(0)
    if a[0] == 'check': sys.exit(1 if check_spec(a[1]) else 0)
    if a[0] == 'build':
        only = None
        if '--only' in a: only = set(a[a.index('--only') + 1].split(','))
        build_from_spec(a[1], final='--final' in a, only=only, replace='--replace' in a)
    elif a[0] == 'cleanup': cleanup()
    elif a[0] == 'dump':
        d = Deck().fetch(); json.dump(d, open(os.path.join(HERE, 'live_dump.json'), 'w')); print('live_dump.json', len(d['slides']), 'slides')
    else: print(__doc__)
