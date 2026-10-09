# -*- coding: utf-8 -*-
"""Split the OnlyFans material into two decks, in the design of the current Yuno/OnlyFans deck
(Titillium Web, blue kicker, 19 pt title, white cards with fine border, blue panels).
  python3 split_decks.py vault   -> 1hrBLCF... becomes the token vault deck (15 slides)
  python3 split_decks.py bank    -> 1gUfjfG... becomes the banking connectivity deck (10 slides)
Everything stated in the decks is treated as confirmed (German, 9 Oct 2026)."""
import os, sys, re, json, warnings, time
warnings.filterwarnings('ignore')
from google.oauth2 import service_account
from googleapiclient.discovery import build

VAULT = '1hrBLCFxPXXAyNR73j46JH12ZtMZGPglRnFeaGBxjKk8'
BANK = '1gUfjfGbSmherHHMgJcPpBsauoNSSBpzEJipT4govY2g'
PT = 12700
INK = '#282A30'; BODY = '#535353'; GREY = '#757882'; BLUE = '#3E4FE0'; DEEP = '#1D2DB8'
PANEL = '#F4F5FD'; LAV = '#E8EAF5'; LINE = '#E2E3E6'; WHITE = '#FFFFFF'; GREEN = '#1F8A5B'; RED = '#C0392B'; DARK = '#282A30'
FONT = 'Titillium Web'; MONO = 'Roboto Mono'
INSET = 7.2

def svc():
    c = service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'), scopes=['https://www.googleapis.com/auth/presentations'])
    return build('slides', 'v1', credentials=c, cache_discovery=False)

def rgb(h):
    h = h.lstrip('#'); return {'red': int(h[0:2], 16) / 255, 'green': int(h[2:4], 16) / 255, 'blue': int(h[4:6], 16) / 255}

def run(s, pid, reqs, label=''):
    for i in range(0, len(reqs), 300):
        part = reqs[i:i + 300]
        for a in range(5):
            try:
                s.presentations().batchUpdate(presentationId=pid, body={'requests': part}).execute(); break
            except Exception as e:
                if '429' in str(e) and a < 4: time.sleep(20); continue
                raise
    print(f'  {label}: {len(reqs)} requests')

def txt(el):
    return ''.join(te.get('textRun', {}).get('content', '') for te in el.get('shape', {}).get('text', {}).get('textElements', []))

# ------------------------------------------------------------------ drawing primitives
class Page:
    def __init__(self, sid):
        self.sid = sid; self.R = []; self.n = 0
    def _id(self):
        self.n += 1; return f'{self.sid}_k{self.n:03d}'
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
def new_slide(s, pid, P, base_sid, new_sid, kicker, title):
    """Duplicate a content slide, keep only its chrome (background, kicker, title, accent bar, page number, logo)."""
    base = next(x for x in P['slides'] if x['objectId'] == base_sid)
    ids = {base_sid: new_sid}
    for el in base['pageElements']: ids[el['objectId']] = f"{new_sid}_{el['objectId'][-6:]}"
    run(s, pid, [{'duplicateObject': {'objectId': base_sid, 'objectIds': ids}}], f'dup {new_sid}')
    reqs = []; kk = tt = None
    for el in base['pageElements']:
        tr = el.get('transform', {}); x = tr.get('translateX', 0) / PT; y = tr.get('translateY', 0) / PT
        nid = ids[el['objectId']]; t = txt(el).strip()
        full_bg = 'image' in el and x < 1 and y < 1
        logo = 'image' in el and x > 640 and y < 30
        bar = el.get('shape', {}).get('shapeType') == 'ROUND_RECTANGLE' and x < 25 and y < 60
        pg = t.isdigit() and x < 12 and y > 360
        if t and abs(y - 25) < 3 and x < 40: kk = nid; continue
        if t and abs(y - 41) < 3 and x < 40: tt = nid; continue
        if logo or bar or pg: continue
        reqs.append({'deleteObject': {'objectId': nid}})
    for oid, t in ((kk, kicker), (tt, title)):
        reqs += [{'deleteText': {'objectId': oid, 'textRange': {'type': 'ALL'}}}, {'insertText': {'objectId': oid, 'insertionIndex': 0, 'text': t}}]
    run(s, pid, reqs, f'clear {new_sid}')
    return Page(new_sid)

def set_text(P, sid, find, markup, R):
    """Replace the whole text of the element on slide sid whose text contains `find`, keeping its regular and bold styles."""
    sl = next(x for x in P['slides'] if x['objectId'] == sid)
    def walk(els):
        for e in els:
            if 'elementGroup' in e: yield from walk(e['elementGroup']['children'])
            else: yield e
    el = next((e for e in walk(sl['pageElements']) if find in txt(e)), None)
    if el is None: print(f'  set_text skip (already applied?): {find!r} on {sid}'); return
    runs = [te['textRun'] for te in el['shape']['text']['textElements'] if 'textRun' in te and te['textRun']['content'].strip()]
    keep = ['fontFamily', 'weightedFontFamily', 'fontSize', 'foregroundColor', 'bold', 'italic']
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
        R.append({'updateTextStyle': {'objectId': oid, 'textRange': {'type': 'FIXED_RANGE', 'startIndex': i, 'endIndex': i + len(p)}, 'style': st, 'fields': ','.join(st.keys())}})
        i += len(p)

def rep(sid, a, b):
    return {'replaceAllText': {'containsText': {'text': a, 'matchCase': True}, 'replaceText': b, 'pageObjectIds': [sid]}}

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

# ------------------------------------------------------------------ shared slide bodies
def personal_data_body(p, right):
    p.card(36, 84, 384, 284)
    p.shape(50, 98, 22, 22, 'ELLIPSE', LAV, None)
    p.text(50, 102, 22, 12, 'AS', size=8, color=BLUE, weight=600, align='CENTER')
    p.text(80, 99, 120, 18, 'Ana Souza', size=13, color=INK, weight=600)
    p.text(160, 102, 60, 14, 'cr_8812', size=9, color=GREY, font=MONO)
    p.pill(316, 100, 92, 'PCI DSS LEVEL 1', size=7.5, h=16)
    for x, t in ((50, 'FIELD'), (176, 'STORED AS'), (340, 'PROTECTION')):
        p.label(x, 134, 110, t, size=7.5)
    rows = [('Legal name', 'A••• S••••', 'Encrypted'), ('Date of birth', '••/••/1991', 'Encrypted'), ('Passport', 'tok_71c0 ····', 'Tokenized'),
            ('Selfies × 2', '2 encrypted files', 'Encrypted'), ('TIN / W-9', '•••-••-6789', 'Tokenized'), ('Bank accounts × 3', '•••• 4421  +2 more', 'Tokenized')]
    y = 152
    for f, v, prot in rows:
        p.line(50, y - 3, 406, y - 3, LINE, 0.75)
        p.text(50, y + 3, 120, 14, f, size=9.5, color=INK)
        p.text(176, y + 3, 150, 14, v, size=9.5, color=INK, font=MONO)
        if prot == 'Tokenized': p.pill(340, y + 3, 62, prot, size=7.5, h=15)
        else: p.pill(340, y + 3, 62, prot, fill=LAV, color=BLUE, size=7.5, h=15)
        y += 27
    p.line(50, y - 3, 406, y - 3, LINE, 0.75)
    p.text(50, y + 8, 350, 14, 'Collected once at onboarding. Reused from the vault every time after.', size=8.5, color=GREY)
    ys = [104, 196, 288]
    for (t, sub), yy in zip(right, ys):
        p.line(420, yy + 26, 466, yy + 26, '#C9CDD6', 1, arrow=True)
        p.card(468, yy, 216, 54)
        p.text(482, yy + 10, 190, 16, t, size=11, color=INK, weight=600)
        p.text(482, yy + 29, 196, 14, sub, size=9, color=GREY)

# ------------------------------------------------------------------ VAULT DECK
def build_vault():
    s = svc(); pid = VAULT
    P = s.presentations().get(presentationId=pid).execute()
    json.dump(P, open('backup_vaultdeck_prebuild_' + time.strftime('%H%M%S') + '.json', 'w'))
    base = 'h7c266de662ba1cf0_9_241'
    have = {x['objectId'] for x in P['slides']}

    # --- edits to existing slides
    R = []
    cov = 'n01_g3f77215683c_1_445'
    set_text(P, cov, 'every bank behind it', 'The OnlyFans Yuno Vault', R)
    set_text(P, cov, 'Token vault and banking', 'Your schema, your connections, your vault.', R)
    set_text(P, cov, 'Strictly confidential', 'Prepared for OnlyFans · October 2026 · Strictly confidential', R)
    ex = 'of_exec_understanding_v2'
    set_text(P, ex, 'OnlyFans needs a vault and', 'OnlyFans needs one vault that every provider can use, under its own rules', R)
    set_text(P, ex, 'Reliable payments to creators', '**Reliable payments and payouts**, with one place for every sensitive record: fan cards, network tokens and creator identity, tax and bank data.', R)
    set_text(P, ex, 'Delivering this through', 'Today fan cards sit with the processor and creator data sits in OnlyFans systems. **Every new processor or issuer** means moving sensitive data again, and **every system that holds it** has to be secured and audited.', R)
    set_text(P, ex, 'selecting a token-vault provider', 'OnlyFans is selecting a token vault provider through the **current RFP**. That choice decides **who holds every credential** and how freely OnlyFans can add, swap or leave providers.', R)
    R.append(rep(ex, 'One Yuno vault for cards, bank, identity and tax data, plus banking connectivity to your banks, issuers, rails and stablecoin partners, on rules OnlyFans controls.',
                 'One PCI DSS Level 1 Yuno Vault for cards, network tokens and creator data, a proxy that delivers each value only to the provider that needs it, and portable tokens with the exit written into the contract.'))
    m5 = 'm5_mock'
    R.append(rep(m5, 'WHY AN INTEGRATED VAULT', 'EXECUTIVE SUMMARY  ›  INTEGRATED VERSUS STANDALONE'))
    set_text(P, m5, '460+ processor integrations, plus', '**460+ processor integrations** already built and maintained', R)
    set_text(P, m5, '3DS, account updater, payouts and banking', '**3DS, account updater, network tokens and payouts** on the same tokens', R)
    nt = 'h7c266de662ba1cf0_9_207'
    set_text(P, nt, 'Token requestor model', 'Token requestor ID registered under OnlyFans where the scheme allows it. Yuno acts as TS-TRP.', R)
    po = 'h7c266de662ba1cf0_9_469'
    set_text(P, po, 'Card data exports in full', "Registered under OnlyFans' token requestor ID where the scheme allows it, so they survive a change of processor or of vault. No re-tokenization on exit.", R)
    run(s, pid, R, 'text edits')

    # --- new slides
    n = {}
    # 1. the problem
    sid = 'vlt_problem'
    if sid not in have:
        p = new_slide(s, pid, P, base, sid, 'THE VAULT  ›  THE PROBLEM', 'Fan cards live with your processor and creator data lives in your systems')
        p.card(36, 84, 300, 286)
        p.text(50, 96, 60, 14, 'BEFORE', size=8, color=GREY, weight=600)
        p.text(104, 93, 200, 18, 'Data in two places', size=13, color=INK, weight=600)
        p.card(50, 120, 130, 122, fill=PANEL, line=None)
        p.text(60, 128, 110, 16, 'Processor', size=11, color=INK, weight=600)
        p.text(60, 144, 110, 14, "holds the fan's card", size=9, color=GREY)
        p.card(60, 208, 110, 22, fill=WHITE, line=LINE); p.text(68, 213, 96, 14, 'Fan cards', size=9, color=INK)
        p.card(190, 120, 132, 122, fill=PANEL, line=None)
        p.text(200, 128, 116, 16, 'OnlyFans systems', size=11, color=INK, weight=600)
        p.text(200, 144, 116, 14, "hold the creator's data", size=9, color=GREY)
        for i, t in enumerate(('Bank accounts', 'ID documents', 'Tax records')):
            p.card(200, 164 + i * 24, 112, 20, fill=WHITE, line=LINE); p.text(207, 168 + i * 24, 100, 12, t, size=8.5, color=INK)
        for i, t in enumerate(('Fan cards are locked to the processor that stores them', 'Two systems to secure and audit', 'A new provider means collecting creator details again')):
            p.text(52, 256 + i * 20, 12, 14, '×', size=10, color=GREY, weight=600)
            p.text(66, 257 + i * 20, 260, 14, t, size=9.5, color=INK)
        p.text(52, 322, 270, 36, 'OnlyFans Privacy Policy: "We do not receive your full payment card number." Read 8 Oct 2026.', size=8, color=GREY)
        p.shape(342, 214, 26, 26, 'ELLIPSE', BLUE, None)
        p.text(342, 218, 26, 16, '→', size=12, color=WHITE, weight=600, align='CENTER')
        p.card(374, 84, 310, 286, fill=PANEL, line=BLUE, lw=1)
        p.text(388, 96, 50, 14, 'AFTER', size=8, color=BLUE, weight=600)
        p.text(432, 93, 200, 18, 'One vault', size=13, color=INK, weight=600)
        for i, t in enumerate(('Processors', 'Card issuers', 'KYC and tax')):
            x = 388 + i * 96
            p.card(x, 118, 88, 44, fill=WHITE, line=LINE)
            p.text(x + 8, 124, 76, 14, t, size=9.5, color=INK, weight=600)
            p.pill(x + 8, 142, 64, 'SWAPPABLE', fill=LAV, color=BLUE, size=7, h=13)
            p.line(x + 44, 162, x + 44, 176, '#C9CDD6', 1)
        p.card(388, 176, 282, 70, fill=BLUE, line=None)
        p.text(400, 186, 200, 16, 'Yuno Vault', size=12, color=WHITE, weight=600)
        for i, t in enumerate(('Cards', 'Bank details', 'ID documents', 'Tax records')):
            p.pill(398 + i * 68, 214, 64, t, fill=BLUE, color=WHITE, size=7, h=16, line=WHITE)
        for i, t in enumerate(('Cards work on any processor you connect', 'One vault to secure and audit', 'Creator details collected once and reused')):
            p.shape(390, 262 + i * 22, 13, 13, 'ELLIPSE', BLUE, None)
            p.text(390, 263 + i * 22, 13, 10, '✓', size=7.5, color=WHITE, weight=600, align='CENTER', pad=False)
            p.text(410, 261 + i * 22, 260, 14, t, size=9.5, color=INK)
        run(s, pid, p.R, sid)
    # 2. cards: store, keep, move
    sid = 'vlt_cards'
    if sid not in have:
        p = new_slide(s, pid, P, base, sid, 'THE VAULT  ›  CARDS', 'Fan cards are stored once and work on every processor you connect')
        cols = [('STEP 1', 'Hosted fields', 'Store'), ('STEP 2', 'Account updater', 'Keep'), ('STEP 3', 'Import and export', 'Move')]
        for i, (st, tag, ttl) in enumerate(cols):
            x = 36 + i * 220
            p.card(x, 84, 208, 238)
            p.text(x + 12, 96, 60, 12, st, size=8, color=GREY, weight=600)
            p.text(x + 96, 96, 100, 12, tag, size=8.5, color=GREY, align='END')
            p.text(x + 12, 112, 180, 18, ttl, size=14, color=INK, weight=600)
            p.card(x + 12, 138, 184, 116, fill=PANEL, line=None)
        x = 48
        p.text(x + 8, 146, 100, 12, 'Card number', size=8, color=GREY)
        p.card(x + 8, 160, 168, 22, line=LINE); p.text(x + 14, 165, 120, 12, '4895 •••• •••• 0193', size=8.5, color=INK, font=MONO)
        p.pill(x + 140, 164, 30, 'Visa', fill=LAV, color=DEEP, size=7.5, h=14)
        p.text(x + 8, 190, 60, 12, 'Expiry', size=8, color=GREY); p.text(x + 94, 190, 30, 12, 'CVV', size=8, color=GREY)
        p.text(x + 120, 190, 60, 12, 'never stored', size=8, color=RED, weight=600)
        p.card(x + 8, 204, 78, 22, line=LINE); p.text(x + 14, 209, 64, 12, '09 / 29', size=8.5, color=INK, font=MONO)
        p.card(x + 94, 204, 82, 22, line=LINE); p.text(x + 100, 209, 64, 12, '•••', size=8.5, color=INK, font=MONO)
        x = 268
        p.text(x + 8, 146, 100, 12, 'Before reissue', size=8, color=GREY)
        p.card(x + 8, 160, 168, 22, line=LINE); p.text(x + 14, 165, 70, 12, '•••• 0193', size=8.5, color=INK, font=MONO); p.text(x + 110, 165, 60, 12, 'tok_9f2a', size=8.5, color=BLUE, weight=600, font=MONO, align='END')
        p.text(x + 8, 190, 160, 12, '↻  Account updater', size=8.5, color=BLUE)
        p.text(x + 8, 206, 100, 12, 'After reissue', size=8, color=GREY)
        p.card(x + 8, 220, 168, 22, line=LINE); p.text(x + 14, 225, 70, 12, '•••• 5521', size=8.5, color=INK, font=MONO); p.text(x + 110, 225, 60, 12, 'tok_9f2a', size=8.5, color=BLUE, weight=600, font=MONO, align='END')
        x = 488
        for i, (nn, a, b) in enumerate((('01', 'Current processor exports', 'PGP file'), ('02', 'Drop over SFTP', 'to Yuno'), ('03', 'Yuno imports and issues tokens', 'fans untouched'))):
            yy = 146 + i * 34
            p.card(x + 8, yy, 168, 30, line=LINE)
            p.text(x + 14, yy + 9, 16, 12, nn, size=8.5, color=BLUE, weight=600, font=MONO)
            p.text(x + 34, yy + 4, 92, 24, a, size=8, color=INK, weight=600)
            p.text(x + 120, yy + 9, 52, 12, b, size=7.5, color=GREY, align='END')
        for i, t in enumerate(('Hosted fields on web, iOS and Android. No charge needed. The CVV is never stored.',
                               'The account updater refreshes cards. The vaulted token stays the same. PAR identifies the unique card behind every credential.',
                               'Import from your current processor as a PGP-encrypted file over SFTP. Export is documented.')):
            p.text(48 + i * 220, 266, 184, 50, t, size=9.5, color=INK, ls=125)
        p.card(36, 334, 648, 36, fill=BLUE, line=None)
        p.text(50, 344, 620, 16, '**One vaulted token, every processor.** Add or swap a processor and the stored cards keep working, with nothing collected again from fans.', size=10, color=WHITE, bold_color=WHITE)
        run(s, pid, p.R, sid)
    # 3. personal data
    sid = 'vlt_personal'
    if sid not in have:
        p = new_slide(s, pid, P, base, sid, 'THE VAULT  ›  PERSONAL DATA', 'Creator identity, tax and bank data get the same Level 1 protection as a card')
        personal_data_body(p, [('KYC and verification', 'legal name · date of birth · passport · selfies'), ('Card issuer onboarding', 'legal name · TIN · bank account'), ('Tax reporting', 'legal name · TIN')])
        run(s, pid, p.R, sid)
    # 4. proxy controls
    sid = 'vlt_controls'
    if sid not in have:
        p = new_slide(s, pid, P, base, sid, 'THE PROXY  ›  CONTROLS', 'The controls you would build around card data come with the proxy')
        p.pill(132, 23, 34, 'BETA', fill=LAV, color=BLUE, size=7, h=13)
        p.card(36, 150, 104, 56); p.text(46, 158, 90, 16, 'OnlyFans system', size=10.5, color=INK, weight=600); p.text(46, 176, 90, 24, 'request with tokens', size=8.5, color=GREY)
        p.line(140, 178, 158, 178, '#C9CDD6', 1)
        p.card(158, 100, 404, 140, fill=PANEL, line=BLUE, lw=1)
        p.text(172, 106, 120, 16, 'Yuno Proxy', size=12, color=INK, weight=600)
        p.text(430, 108, 120, 14, 'every call, in this order', size=8.5, color=GREY, align='END')
        steps = [('01', 'Allowlist', 'Exact HTTPS hosts you register. Every change lands in an append-only log.'),
                 ('02', 'Mutual TLS', 'Your client certificate per destination. The private key is write-only in KMS.'),
                 ('03', 'Detokenize', 'Tokens are swapped for vault values inside the request body.'),
                 ('04', 'Audit', 'One record for every call, with the destination and the result.')]
        p.line(182, 144, 520, 144, '#C9CDD6', 1)
        for i, (nn, t, b) in enumerate(steps):
            x = 172 + i * 96
            p.circle_num(x, 134, nn)
            p.text(x, 162, 88, 16, t, size=10.5, color=INK, weight=600)
            p.text(x, 180, 88, 70, b, size=8.5, color=BODY, ls=120)
        p.line(562, 178, 580, 178, '#C9CDD6', 1)
        p.card(580, 150, 104, 56); p.text(590, 158, 90, 16, 'Destination', size=10.5, color=INK, weight=600); p.text(590, 176, 90, 24, 'receives the real values', size=8.5, color=GREY)
        p.card(36, 258, 648, 54, fill=DARK, line=None)
        p.text(52, 277, 90, 16, 'Nothing kept', size=11, color=WHITE, weight=600)
        p.pill(132, 278, 56, 'OPTIONAL', fill=DARK, color=WHITE, size=7, h=14, line=WHITE)
        p.text(206, 270, 466, 30, 'Request bodies are not stored or logged unless you switch it on, per destination. Card numbers echoed back are cut to the last four.', size=9, color='#E8EAF5', ls=125)
        p.text(36, 334, 70, 12, 'DESTINATIONS', size=7.5, color=GREY, weight=600)
        for i, t in enumerate(('PSPs and acquirers', 'Your own acquiring', 'Card issuers', 'KYC and tax providers', 'Fraud services')):
            p.pill(112 + i * 114, 332, 106, t, fill=WHITE, color=INK, size=7.5, h=16, line=LINE)
        run(s, pid, p.R, sid)
    # 5. versus VGS and Basis Theory
    sid = 'vlt_versus'
    if sid not in have:
        p = new_slide(s, pid, P, base, sid, 'WHY YUNO  ›  VERSUS A STANDALONE VAULT', 'Standalone vaults lead on vault depth. Yuno leads on everything around it')
        cols = [('YOUR DESIGN NEEDS', 36, 150), ('YUNO', 186, 148), ('VGS', 334, 128), ('BASIS THEORY', 462, 128), ('WHO LEADS', 590, 94)]
        p.shape(36, 84, 648, 22, 'RECTANGLE', DARK, None)
        for t, x, w in cols: p.text(x + 8, 89, w - 12, 12, t, size=7.5, color=WHITE, weight=600)
        rows = [('PCI DSS Level 1 card vault', 'Yes, hosted fields and SDKs', 'Yes, Collect and Show', 'Yes, Elements', 'Level'),
                ('Personal data beyond cards', 'Tables you define, protection per column', 'Aliases for PII, bank, IBAN', 'Token types for bank, SSN, EIN', 'Level'),
                ('Network tokens', 'Visa, Mastercard, Amex; TRID under OnlyFans', 'All four networks', 'TRID created for you', 'Vaults lead'),
                ('Proxy and custom code', 'Outbound proxy, allowlist, mTLS, audit', 'Inbound and outbound routes, custom code', 'Proxy and serverless Reactors', 'Vaults lead'),
                ('Show an issued card, set its PIN', 'Not offered today', 'Card display with VGS Show', 'Display; PIN with Lithic, Marqeta', 'Vaults lead'),
                ('Rules for where each request goes', 'Rules, splits, fallbacks and monitors', '"Does not make routing decisions for you"', 'No rules product found', 'Yuno leads'),
                ('Provider connections built for you', '460+ processor integrations', 'Your own logic, or a partner', 'Proxy requests you write', 'Yuno leads'),
                ('Payments on the same token', '3DS, account updater, routing, retries', 'A second vendor', 'A second vendor', 'Yuno leads'),
                ('Payouts and split payments', 'Payouts API, split payments', 'Via partners like TabaPay, Astra', 'No payouts product found', 'Yuno leads')]
        y = 106
        for i, r in enumerate(rows):
            if i % 2: p.shape(36, y, 648, 26, 'RECTANGLE', PANEL, None)
            for j, (t, x, w) in enumerate(cols):
                v = r[j]
                if j == 4:
                    c = BLUE if v == 'Yuno leads' else (GREY if v == 'Level' else INK)
                    p.text(x + 8, y + 7, w - 12, 12, v, size=8.5, color=c, weight=600)
                else:
                    p.text(x + 8, y + 5, w - 12, 18, v, size=8, color=INK if j else INK, weight=600 if j == 0 else 400, ls=105)
            y += 26
        p.line(36, y, 684, y, LINE, 0.75)
        p.text(36, y + 8, 520, 12, 'Yuno leads on 4, level on 2, the standalone vaults lead on 3. VGS and Basis Theory: their public pages, read 7 October 2026.', size=8, color=GREY)
        run(s, pid, p.R, sid)

    order = ['n01_g3f77215683c_1_445', 'of_exec_understanding_v2', 'vlt_problem', 'm5_mock', 'vlt_cards', 'h7c266de662ba1cf0_9_207', 'vlt_personal',
             'h7c266de662ba1cf0_9_241', 'h7c266de662ba1cf0_9_391', 'vlt_controls', 'vlt_versus', 'h7c266de662ba1cf0_9_469',
             'h6032acb876a0077a_1_0', 'h6032acb876a0077a_1_974', 'h7c266de662ba1cf0_9_611']
    finish(s, pid, order)

# ------------------------------------------------------------------ BANK DECK
def build_bank():
    s = svc(); pid = BANK
    P = s.presentations().get(presentationId=pid).execute()
    json.dump(P, open('backup_bankdeck_prebuild_' + time.strftime('%H%M%S') + '.json', 'w'))
    base = 'h7c266de662ba1cf0_9_241'
    have = {x['objectId'] for x in P['slides']}
    R = []
    cov = 'n01_g3f77215683c_1_445'
    set_text(P, cov, 'every bank behind it', 'One account, every bank behind it', R)
    set_text(P, cov, 'Token vault and banking', 'Banking connectivity for OnlyFans creators', R)
    set_text(P, cov, 'Strictly confidential', 'Prepared for OnlyFans · October 2026 · Strictly confidential', R)
    ex = 'of_exec_understanding_v2'
    set_text(P, ex, 'OnlyFans needs a vault and', 'OnlyFans wants to work with banks directly. Yuno connects every bank behind each creator account', R)
    set_text(P, ex, 'Reliable payments to creators', '**One OnlyFans account per creator**, held at two to five banks behind it, with card issuers and transfer providers that can be added or swapped.', R)
    set_text(P, ex, 'Delivering this through', '**No single bank should be able to cut a creator off.** That means opening and running accounts at several banks per creator, and still showing the creator **one balance**.', R)
    set_text(P, ex, 'selecting a token-vault provider', '**Who decides where each creator\'s money lives**, and how it moves between banks, rails and issuers. OnlyFans sets the rules. **US balances first.**', R)
    R.append(rep(ex, 'One Yuno vault for cards, bank, identity and tax data, plus banking connectivity to your banks, issuers, rails and stablecoin partners, on rules OnlyFans controls.',
                 'One API to your banks, issuers and rails, an aggregation layer that shows each creator one balance and one history, and rules OnlyFans controls. The banks hold the money.'))
    bc = 'of_vault_proxy_flow_v3_bc'
    R.append(rep(bc, 'BANKING CONNECTIVITY  ›  HOW IT WORKS', 'BANKING CONNECTIVITY  ›  YOUR DESIGN'))
    bc_el = next(x for x in P['slides'] if x['objectId'] == bc)
    for el in bc_el['pageElements']:
        if 'Product direction' in txt(el): R.append({'deleteObject': {'objectId': el['objectId']}})
    rl = 'h7c266de662ba1cf0_35_0_rl'
    R += [rep(rl, 'Per call: live', 'Bank choice by rule'), rep(rl, 'Rails live', 'ACH, wire, RTP'), rep(rl, 'Rules proposed', 'Failover across banks')]
    yd = 'h7c266de662ba1cf0_35_0_yd'
    ydsl = next(x for x in P['slides'] if x['objectId'] == yd)
    tc = sorted([e for e in ydsl['pageElements'] if txt(e).strip() == 'To confirm'], key=lambda e: e['transform'].get('translateX', 0))
    if len(tc) == 2:
        R += [{'deleteText': {'objectId': tc[0]['objectId'], 'textRange': {'type': 'ALL'}}}, {'insertText': {'objectId': tc[0]['objectId'], 'insertionIndex': 0, 'text': 'Jiko · Coinbase · Triple-A'}},
              {'deleteText': {'objectId': tc[1]['objectId'], 'textRange': {'type': 'ALL'}}}, {'insertText': {'objectId': tc[1]['objectId'], 'insertionIndex': 0, 'text': 'Any issuer API'}}]
    R.append(rep(yd, 'One platform for the full creator money flow. Product direction, not a delivery commitment.', 'One platform for the full creator money flow: fan payments in, balances across banks, payouts and cards out.'))
    # status dots and labels on rl and yd: all live (green, filled)
    for sid in (rl, yd):
        sl = next(x for x in P['slides'] if x['objectId'] == sid)
        for el in sl['pageElements']:
            if el.get('shape', {}).get('shapeType') == 'ELLIPSE':
                R.append({'updateShapeProperties': {'objectId': el['objectId'], 'shapeProperties': {'shapeBackgroundFill': {'solidFill': {'color': {'rgbColor': rgb(GREEN)}}}, 'outline': {'outlineFill': {'solidFill': {'color': {'rgbColor': rgb(GREEN)}}}, 'weight': {'magnitude': 1, 'unit': 'PT'}}}, 'fields': 'shapeBackgroundFill.solidFill.color,outline.outlineFill.solidFill.color,outline.weight'}})
            t = txt(el).strip(); tr = el.get('transform', {})
            if t and 250 < tr.get('translateY', 0) / PT < 270:
                R.append({'updateTextStyle': {'objectId': el['objectId'], 'textRange': {'type': 'ALL'}, 'style': {'foregroundColor': {'opaqueColor': {'rgbColor': rgb(GREEN)}}}, 'fields': 'foregroundColor'}})
    run(s, pid, R, 'text edits')

    # aggregation
    sid = 'bnk_aggregation'
    if sid not in have:
        p = new_slide(s, pid, P, base, sid, 'BANKING CONNECTIVITY  ›  AGGREGATION', "The account lives at each bank. Yuno aggregates them into one balance and one history for the creator")
        banks = [('Bank A', '•••• 4421', '$12,480.00'), ('Bank B', '•••• 7310', '$8,210.50'), ('Bank C', '•••• 1188', '$3,905.25')]
        for i, (b, acc, bal) in enumerate(banks):
            y = 86 + i * 82
            p.card(36, y, 196, 70)
            p.text(48, y + 9, 90, 16, b, size=11, color=INK, weight=600)
            p.text(128, y + 11, 92, 12, acc, size=8.5, color=GREY, font=MONO, align='END')
            p.text(48, y + 30, 80, 12, 'Balance', size=8, color=GREY)
            p.text(48, y + 43, 170, 18, bal, size=13, color=INK, weight=600)
            p.line(232, y + 35, 262, 176, '#C9CDD6', 1, arrow=True)
        p.card(264, 120, 150, 112, fill=BLUE, line=None)
        p.text(276, 130, 130, 16, 'Yuno aggregation layer', size=11.5, color=WHITE, weight=600)
        p.text(276, 152, 128, 74, 'Reads the activity of every bank account, normalises it and reconciles it daily. One balance, one history.', size=8.5, color='#E8EAF5', ls=125)
        p.line(414, 176, 446, 176, '#C9CDD6', 1, arrow=True)
        p.card(448, 86, 236, 234)
        p.text(462, 96, 160, 14, 'CREATOR VIEW · ANA SOUZA', size=7.5, color=GREY, weight=600)
        p.text(462, 114, 120, 12, 'Total balance', size=8.5, color=GREY)
        p.text(462, 128, 200, 26, '$24,595.75', size=22, color=BLUE, weight=600)
        p.text(462, 158, 200, 12, 'across 3 banks', size=8.5, color=GREY)
        p.line(462, 178, 670, 178, LINE, 0.75)
        p.text(462, 184, 80, 12, 'ACTIVITY', size=7.5, color=GREY, weight=600)
        acts = [('Subscription earnings', '+$1,240.00', 'Today'), ('Transfer to debit card', '−$300.00', 'Today'), ('Tips', '+$86.50', 'Yesterday'), ('Payout to bank', '−$2,000.00', 'Mon')]
        for i, (a, amt, d) in enumerate(acts):
            yy = 202 + i * 27
            p.text(462, yy, 120, 12, a, size=9, color=INK)
            p.text(462, yy + 12, 80, 10, d, size=7.5, color=GREY)
            p.text(590, yy + 3, 82, 12, amt, size=9.5, color=GREEN if amt.startswith('+') else INK, weight=600, align='END')
        p.card(36, 336, 648, 34, fill=PANEL, line=None)
        p.text(50, 345, 620, 16, "**One balance, one history.** The account lives at each bank and the bank's ledger stays the record of truth. Yuno never holds the money.", size=9.5, color=INK)
        p.text(560, 324, 124, 10, 'Illustrative figures', size=7, color=GREY, align='END')
        run(s, pid, p.R, sid)
    # account opening
    sid = 'bnk_opening'
    if sid not in have:
        p = new_slide(s, pid, P, base, sid, 'BANKING CONNECTIVITY  ›  ACCOUNT OPENING', 'A creator signs up once. Yuno opens and keeps an account at every bank your rules choose')
        steps = [('01', 'Creator signs up', 'One OnlyFans account. KYC collected once and kept in the vault.'),
                 ('02', 'Your rules pick the banks', "Two to five banks per creator, chosen by OnlyFans' allocation rules."),
                 ('03', 'Yuno onboards at each bank', 'One onboarding per bank connection, using the same verified data.'),
                 ('04', 'Accounts are live', 'Each account returns its own account and routing numbers. Status by webhook.')]
        p.line(60, 104, 660, 104, '#C9CDD6', 1)
        for i, (nn, t, b) in enumerate(steps):
            x = 36 + i * 164
            p.circle_num(x + 12, 94, nn)
            p.card(x, 122, 156, 104)
            p.text(x + 12, 132, 134, 16, t, size=11, color=INK, weight=600)
            p.text(x + 12, 154, 134, 66, b, size=9, color=BODY, ls=125)
        p.card(36, 242, 380, 128, fill=PANEL, line=None)
        p.text(50, 252, 200, 12, 'WHAT THE API HANDLES', size=7.5, color=BLUE, weight=600)
        items = [('Entities', 'individual or business, one record per creator'), ('Onboarding', 'KYC or KYB on a named bank connection'),
                 ('Accounts', 'account and routing numbers at each bank'), ('Events', 'a webhook for every status change')]
        for i, (a, b) in enumerate(items):
            p.text(50, 272 + i * 23, 360, 14, f'**{a}**  {b}', size=9.5, color=INK, bold_color=INK)
        p.card(430, 242, 254, 128, fill=DARK, line=None)
        p.text(444, 254, 230, 12, 'ONBOARDING REQUEST', size=7.5, color='#B7BEF2', weight=600)
        p.text(444, 274, 230, 60, '{\n  "entity_id": "cr_8812",\n  "yuno_connection_id": "bank_b",\n  "type": "INDIVIDUAL"\n}', size=8.5, color=WHITE, font=MONO, ls=130)
        p.text(444, 340, 230, 24, 'Every onboarding names the bank it runs on. Your rules set it.', size=8.5, color='#E8EAF5')
        run(s, pid, p.R, sid)
    # money movement
    sid = 'bnk_money'
    if sid not in have:
        p = new_slide(s, pid, P, base, sid, 'BANKING CONNECTIVITY  ›  MONEY MOVEMENT', 'Every transfer leaves from the bank and on the rail your rules choose')
        rails = [('ACH', 'Standard', 'Low cost, for scheduled payouts'), ('Same-day ACH', 'Same business day', 'For payouts that cannot wait'),
                 ('Wire', 'Immediate', 'For large or urgent transfers'), ('RTP', 'Real time, 24/7', 'Instant payouts to the creator')]
        for i, (r, a, b) in enumerate(rails):
            x = 36 + i * 164
            p.card(x, 86, 156, 104)
            p.text(x + 12, 96, 134, 18, r, size=14, color=INK, weight=600)
            p.pill(x + 12, 120, 100, a, fill=LAV, color=BLUE, size=7.5, h=15)
            p.text(x + 12, 144, 134, 40, b, size=9.5, color=BODY, ls=125)
        p.card(36, 206, 648, 116, fill=PANEL, line=None)
        p.text(50, 216, 300, 12, 'HOW A PAYOUT IS ROUTED', size=7.5, color=BLUE, weight=600)
        flow = [('Payout request', 'from the creator or on schedule'), ('Rule picks the rail', 'cheapest or fastest'), ('Rule picks the bank', 'by balance and cap per bank'), ('Status and reconciliation', 'webhook now, ledger match daily')]
        for i, (a, b) in enumerate(flow):
            x = 50 + i * 158
            p.card(x, 238, 140, 66, fill=WHITE, line=LINE)
            p.text(x + 10, 248, 122, 16, a, size=10, color=INK, weight=600)
            p.text(x + 10, 268, 122, 30, b, size=8.5, color=GREY)
            if i < 3: p.line(x + 140, 271, x + 158, 271, '#C9CDD6', 1, arrow=True)
        p.text(36, 338, 648, 28, '**Book transfers** move funds between a creator\'s own accounts at different banks, so balances can be rebalanced when a cap is reached or a bank is lost.', size=9.5, color=INK, bold_color=INK)
        run(s, pid, p.R, sid)
    # vault underneath
    sid = 'bnk_vault'
    if sid not in have:
        p = new_slide(s, pid, P, base, sid, 'BANKING CONNECTIVITY  ›  THE VAULT UNDERNEATH', 'Creator data is collected once, held in the vault and reused for every bank and issuer')
        personal_data_body(p, [('New bank onboarding', 'legal name · TIN · bank account'), ('Card issuer onboarding', 'legal name · date of birth · passport · selfies'), ('Tax reporting', 'legal name · TIN')])
        run(s, pid, p.R, sid)

    order = ['n01_g3f77215683c_1_445', 'of_exec_understanding_v2', 'of_vault_proxy_flow_v3_bc', 'bnk_aggregation', 'bnk_opening',
             'h7c266de662ba1cf0_35_0_rl', 'bnk_money', 'h7c266de662ba1cf0_35_0_yd', 'bnk_vault', 'h7c266de662ba1cf0_9_611']
    finish(s, pid, order)

if __name__ == '__main__':
    {'vault': build_vault, 'bank': build_bank}[sys.argv[1]]()
