# -*- coding: utf-8 -*-
"""Waymo token-vault section: four slides in the design of the OnlyFans vault deck (Titillium Web, blue kicker, accent bar),
drawn straight into the live Waymo deck with the primitives of Deals/OnlyFans/build/split_decks.py.
Replaces the engine-built slides 8..11 (section 02). Facts: data/research/waymo-2026-10-19.md (help center, terms, launches).
  python3 vault_slides.py <presentation_id>"""
import os, sys, json, time, warnings; warnings.filterwarnings('ignore')
sys.path.insert(0, '/Users/germantatis/Desktop/GTMCoding/Deals/OnlyFans/build'); import split_decks as SD
from split_decks import Page, run, rgb, INK, BODY, GREY, BLUE, DEEP, PANEL, LAV, LINE, WHITE, DARK, RED, MONO, FONT
PT = 12700
PID = sys.argv[1]
s = SD.svc()
def txt(el): return SD.txt(el)
P = s.presentations().get(presentationId=PID).execute()
json.dump(P, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backup_before_vault_slides_' + time.strftime('%H%M%S') + '.json'), 'w'))
slides = P['slides']; ids = [x['objectId'] for x in slides]
def kick(sl):
    for e in sl['pageElements']:
        t = txt(e).strip()
        if t: return t
    return ''
# the four engine-built vault slides sit between the dividers "02" and "03"
d02 = next(i for i, sl in enumerate(slides) if sl['objectId'].startswith('n07'))
old = [sl['objectId'] for sl in slides[d02 + 1:d02 + 5]]
print('replacing', [(o, kick(next(x for x in slides if x['objectId'] == o))[:40]) for o in old])
base = next(x for x in slides if x['objectId'].startswith('n13'))   # the markets table slide: white content chrome of this deck
NEW = ['wv_problem', 'wv_summary', 'wv_cards', 'wv_versus']
have = set(ids)

def chrome(new_sid, kicker, title, notes, title_size=19):
    """Duplicate the markets slide, keep only the yuno wordmark and the page number, draw the OnlyFans-style kicker, accent bar and title."""
    m = {base['objectId']: new_sid}
    for el in base['pageElements']: m[el['objectId']] = f"{new_sid}_{el['objectId'][-6:]}"
    run(s, PID, [{'duplicateObject': {'objectId': base['objectId'], 'objectIds': m}}], f'dup {new_sid}')
    reqs = []
    for el in base['pageElements']:
        tr = el.get('transform', {}); x = tr.get('translateX', 0) / PT; y = tr.get('translateY', 0) / PT; t = txt(el).strip()
        wordmark = 'image' in el and x > 600 and y < 40
        pageno = t.isdigit() and x > 600 and y > 360
        if not (wordmark or pageno): reqs.append({'deleteObject': {'objectId': m[el['objectId']]}})
    run(s, PID, reqs, f'clear {new_sid}')
    p = Page(new_sid)
    p.text(36, 24.9, 322, 13.5, kicker, size=7, color=BLUE, weight=600, pad=False, kind='RECTANGLE', valign='MIDDLE')
    p.shape(20.9, 47.2, 3.2, 15.1, 'ROUND_RECTANGLE', BLUE, None)
    p.text(36, 41.1, 648, 54, title, size=title_size, color=INK, weight=400, pad=False, kind='RECTANGLE', ls=100)
    p.notes = notes
    return p

def set_notes(sid, text):
    sl = s.presentations().pages().get(presentationId=PID, pageObjectId=sid).execute()
    nid = sl['slideProperties']['notesPage']['notesProperties']['speakerNotesObjectId']
    run(s, PID, [{'deleteText': {'objectId': nid, 'textRange': {'type': 'ALL'}}}, {'insertText': {'objectId': nid, 'insertionIndex': 0, 'text': text}}], f'notes {sid}')

SRC = ("Sources: Waymo Help Center, Approved payment methods (cards, Apple Pay, Google Pay, Waymo Cash and gift cards; a card on file is required even when paying with Waymo Cash); "
       "Waymo Terms of Service (card details may be updated as provided by our payment processor, your issuing bank or the applicable payment network; all charges in US dollars); "
       "Waymo Premier terms (secondary card fallback). Launch plans: London 2026, Tokyo 2027, Munich 2027, Singapore 2028, Toronto 2028 (public announcements). Read 19 to 22 October 2026. "
       "Yuno: docs.y.uno vault, network tokens, account updater, token migration and export pages, read 7 to 8 October 2026.")

# ---------------------------------------------------------------- 1. the problem
sid = NEW[0]
if sid not in have:
    p = chrome(sid, 'THE VAULT  ›  THE PROBLEM', 'A second PSP is the moment to put rider cards above both processors', SRC, title_size=18)
    p.card(36, 84, 300, 286)
    p.text(50, 96, 60, 14, 'BEFORE', size=8, color=GREY, weight=600)
    p.text(104, 93, 220, 18, 'Cards tied to one processor', size=13, color=INK, weight=600)
    p.card(50, 120, 130, 122, fill=PANEL, line=None)
    p.text(60, 128, 110, 16, 'Processor', size=11, color=INK, weight=600)
    p.text(60, 144, 116, 14, "holds the rider's card", size=9, color=GREY)
    for i, t in enumerate(('Rider cards', 'Business profile cards', 'Guardian cards (teens)')):
        p.card(60, 164 + i * 24, 112, 20, fill=WHITE, line=LINE); p.text(67, 168 + i * 24, 104, 12, t, size=8.5, color=INK)
    p.card(190, 120, 132, 122, fill=PANEL, line=None)
    p.text(200, 128, 120, 16, 'New markets', size=11, color=INK, weight=600)
    p.text(200, 144, 120, 14, 'each needs its own acquirer', size=9, color=GREY)
    for i, t in enumerate(('London 2026', 'Tokyo, Munich 2027', 'Singapore, Toronto 2028')):
        p.card(200, 164 + i * 24, 116, 20, fill=WHITE, line=LINE); p.text(207, 168 + i * 24, 108, 12, t, size=7.5, color=INK)
    for i, t in enumerate(('Rider cards are locked to the processor that stores them', 'Processor tokens do not travel to the second PSP', 'Card updates arrive only as the processor provides them')):
        p.text(52, 256 + i * 20, 12, 14, '×', size=10, color=GREY, weight=600)
        p.text(66, 257 + i * 20, 262, 14, t, size=9.5, color=INK)
    p.text(52, 322, 272, 40, 'Waymo Help Center: a card on file is required, even to pay with Waymo Cash. Waymo Terms: card details are updated as provided by our payment processor. Read 19 Oct 2026.', size=7.5, color=GREY, ls=110)
    p.shape(342, 214, 26, 26, 'ELLIPSE', BLUE, None)
    p.text(342, 218, 26, 16, '→', size=12, color=WHITE, weight=600, align='CENTER')
    p.card(374, 84, 310, 286, fill=PANEL, line=BLUE, lw=1)
    p.text(388, 96, 50, 14, 'AFTER', size=8, color=BLUE, weight=600)
    p.text(432, 93, 200, 18, 'One vault', size=13, color=INK, weight=600)
    for i, t in enumerate(('Processors', 'Local acquirers', 'Risk and 3DS')):
        x = 388 + i * 96
        p.card(x, 118, 88, 44, fill=WHITE, line=LINE)
        p.text(x + 8, 124, 76, 14, t, size=9.5, color=INK, weight=600)
        p.pill(x + 8, 142, 64, 'SWAPPABLE', fill=LAV, color=BLUE, size=7, h=13)
        p.line(x + 44, 162, x + 44, 176, '#C9CDD6', 1)
    p.card(388, 176, 282, 70, fill=BLUE, line=None)
    p.text(400, 186, 200, 16, 'Yuno Vault', size=12, color=WHITE, weight=600)
    for i, (t, w) in enumerate((('Cards', 58), ('Network tokens', 84), ('Wallet tokens', 84))):
        x = 398 + sum(ww + 4 for _, ww in (('Cards', 58), ('Network tokens', 84), ('Wallet tokens', 84))[:i])
        p.pill(x, 214, w, t, fill=BLUE, color=WHITE, size=7, h=16, line=WHITE)
    for i, t in enumerate(('Cards work on any processor you connect, in any market', 'One vault to secure and audit', 'Riders never re-enter a card when processors change')):
        p.shape(390, 262 + i * 22, 13, 13, 'ELLIPSE', BLUE, None)
        p.text(390, 263 + i * 22, 13, 10, '✓', size=7.5, color=WHITE, weight=600, align='CENTER', pad=False)
        p.text(410, 261 + i * 22, 262, 14, t, size=9.5, color=INK)
    run(s, PID, p.R, sid); set_notes(sid, p.notes)

# ---------------------------------------------------------------- 2. integrated versus standalone (redrawn from the OnlyFans summary slide)
sid = NEW[1]
if sid not in have:
    p = chrome(sid, 'EXECUTIVE SUMMARY  ›  INTEGRATED VERSUS STANDALONE', "Yuno's vault does everything a standalone vault does, plus the connections, with far less to build", SRC)
    p.text(36, 98, 137, 35, 'What Waymo needs', size=10.5, color=INK, weight=700, pad=False, valign='MIDDLE')
    p.text(180, 96, 216, 38, '**Standalone vault**\nStores the data. The rest is yours to build or buy.', size=8.5, color=BODY, weight=400, pad=False, kind='ROUND_RECTANGLE', fill='#F4F4FA', valign='MIDDLE', bold_color=INK)
    p.text(408, 96, 276, 38, '**Yuno integrated vault**\nStores the data, connects it to processors and runs payments on it.', size=8.5, color='#E8EAF5', weight=400, pad=False, kind='ROUND_RECTANGLE', fill=BLUE, valign='MIDDLE', bold_color=WHITE)
    p.pill(611, 101, 64, 'INCLUDED', fill='#2738CB', color=WHITE, size=6.5, h=12.5)
    p.text(36, 138, 137, 32, 'Basic vault function', size=9, color=INK, weight=700, pad=False, valign='MIDDLE')
    p.text(180, 142, 504, 25, 'PCI DSS Level 1 storage   ·   Tokenisation   ·   Proxy to providers   ·   Portable tokens and contractual exit', size=8.5, color=BODY, pad=False, kind='ROUND_RECTANGLE', fill='#F7F9FC', line=LINE, align='CENTER', valign='MIDDLE')
    p.text(36, 176, 220, 14, 'Other connections and capabilities', size=9, color=BLUE, weight=700, pad=False)
    p.shape(408, 188, 276, 164, 'RECTANGLE', '#F1F4FF', None)
    rows = [('Data in one vault', 'PARTIAL', 'Cards and tokens; wallet tokens vary by vendor', '**Cards, network tokens and Apple Pay and Google Pay tokens** in one vault'),
            ('Provider connections', 'Additional\nBuild', 'Each processor and local acquirer per market, built and run in-house', '**460+ processor integrations** already built and maintained'),
            ('Payment capabilities', 'Additional\nBuild', 'Routing, retries, failover and re-authorisation, built in-house', '**Routing, retries and failover** on rules you set'),
            ('Additional services', 'Additional\nPurchase', 'A new vendor and integration for each service', '**3DS, account updater and network tokens** on the same tokens')]
    for i, (lab, pill, left, right) in enumerate(rows):
        y = 192 + i * 40
        p.text(36, y, 137, 40, lab, size=9.5, color=INK, weight=700, pad=False, valign='MIDDLE')
        p.text(186, y + 8, 66, 24, pill, size=7, color='#B5473A', weight=700, pad=False, kind='ROUND_RECTANGLE', fill='#F7E4E1', align='CENTER', valign='MIDDLE', ls=100)
        p.text(258, y, 139, 40, left, size=8.5, color=BODY, pad=False, valign='MIDDLE')
        if i < 3: p.shape(36, y + 40, 360, 0.5, 'RECTANGLE', '#E7E7ED', None)
        p.line(420, y + 19, 423, y + 22, BLUE, 1.5); p.line(423, y + 22, 429, y + 15, BLUE, 1.5)
        p.text(433, y, 244, 40, right, size=10, color=INK, weight=400, pad=False, valign='MIDDLE', bold_color=BLUE)
        if i < 3: p.shape(418, y + 40, 256, 0.5, 'RECTANGLE', '#DEE4F7', None)
    p.text(36, 360, 648, 25, '**Same independence, far less to build.**   Waymo keeps portable tokens and exit terms, and decides how much of the stack Yuno runs.', size=9.5, color='#E8EAF5', pad=False, kind='ROUND_RECTANGLE', fill='#1C2DB8', align='CENTER', valign='MIDDLE', bold_color=WHITE)
    run(s, PID, p.R, sid); set_notes(sid, p.notes)

# ---------------------------------------------------------------- 3. cards: store, keep, move (OnlyFans vlt_cards, riders instead of fans)
sid = NEW[2]
if sid not in have:
    p = chrome(sid, 'THE VAULT  ›  CARDS', 'Rider cards are stored once and work on every processor you connect', SRC)
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
    p.pill(x + 134, 164, 36, 'Visa', fill=LAV, color=DEEP, size=7.5, h=14)
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
    for i, (nn, a, b) in enumerate((('01', 'Current processor exports', 'PGP file'), ('02', 'Drop over SFTP', 'to Yuno'), ('03', 'Yuno imports and issues tokens', 'riders untouched'))):
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
    p.text(50, 344, 620, 16, '**One vaulted token, every processor.** Add or swap a processor and the stored cards keep working.', size=10, color=WHITE, bold_color=WHITE)
    run(s, PID, p.R, sid); set_notes(sid, p.notes)

# ---------------------------------------------------------------- 4. versus VGS and Basis Theory (kept as in the OnlyFans deck)
sid = NEW[3]
if sid not in have:
    p = chrome(sid, 'WHY YUNO  ›  VERSUS A STANDALONE VAULT', 'Standalone vaults lead on vault depth. Yuno leads on everything around it',
               'VGS and Basis Theory: their public pages, read 7 October 2026 (verygoodsecurity.com, docs.verygoodsecurity.com, basistheory.com, developers.basistheory.com). Yuno: docs.y.uno and y.uno. Same table as the OnlyFans vault deck; only the owner of the token requestor ID changed.')
    cols = [('WHAT WAYMO NEEDS', 36, 150), ('YUNO', 186, 148), ('VGS', 334, 128), ('BASIS THEORY', 462, 128), ('WHO LEADS', 590, 94)]
    p.shape(36, 84, 648, 22, 'RECTANGLE', DARK, None)
    for t, x, w in cols: p.text(x + 8, 89, w - 12, 12, t, size=7.5, color=WHITE, weight=600)
    rows = [('PCI DSS Level 1 card vault', 'Yes, hosted fields and SDKs', 'Yes, Collect and Show', 'Yes, Elements', 'Level'),
            ('Personal data beyond cards', 'Tables you define, protection per column', 'Aliases for PII, bank, IBAN', 'Token types for bank, SSN, EIN', 'Level'),
            ('Network tokens', 'Visa, Mastercard, Amex; TRID under Waymo', 'All four networks', 'TRID created for you', 'Vaults lead'),
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
                p.text(x + 8, y + 5, w - 12, 18, v, size=8, color=INK, weight=600 if j == 0 else 400, ls=105)
        y += 26
    p.line(36, y, 684, y, LINE, 0.75)
    p.text(36, y + 8, 560, 12, 'Yuno leads on 4, level on 2, the standalone vaults lead on 3. VGS and Basis Theory: their public pages, read 7 October 2026.', size=8, color=GREY)
    run(s, PID, p.R, sid); set_notes(sid, p.notes)

# ---------------------------------------------------------------- order: new slides where the old four were, old four deleted, page numbers fixed
P = s.presentations().get(presentationId=PID).execute(); live = [x['objectId'] for x in P['slides']]
order = [o for o in live if o not in NEW and o not in old]
order = order[:d02 + 1] + NEW + order[d02 + 1:]
reqs = [{'updateSlidesPosition': {'slideObjectIds': [o], 'insertionIndex': i}} for i, o in enumerate(order)] + [{'deleteObject': {'objectId': o}} for o in old if o in live]
run(s, PID, reqs, 'order and delete')
P = s.presentations().get(presentationId=PID).execute(); pg = []
for n, sl in enumerate(P['slides'], 1):
    for el in sl['pageElements']:
        tr = el.get('transform', {}); t = txt(el).strip()
        if t.isdigit() and tr.get('translateX', 0) / PT > 600 and tr.get('translateY', 0) / PT > 360 and t != str(n):
            pg += [{'deleteText': {'objectId': el['objectId'], 'textRange': {'type': 'ALL'}}}, {'insertText': {'objectId': el['objectId'], 'insertionIndex': 0, 'text': str(n)}}]
if pg: run(s, PID, pg, 'page numbers')
print('final slides:', len(P['slides']), '| section 02 =', [x['objectId'] for x in P['slides'][d02:d02 + 6]])

# ---------------------------------------------------------------- deck font: Geist (German, 22 Oct 2026: "match the font")
import subprocess
subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'geist_restyle.py'), PID, ','.join(NEW)], check=True)
