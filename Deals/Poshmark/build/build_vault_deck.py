# -*- coding: utf-8 -*-
"""Turn the copy of the OnlyFans token vault deck into the Poshmark token vault deck.
  python3 build_vault_deck.py            -> apply everything to DECK
  python3 build_vault_deck.py dry        -> print the planned text edits only
Content lives in content.py so copy can be revised without touching the drawing code.
Pattern: Deals/Paramount/build/build_vault_deck.py (Skydance, 22 Oct 2026)."""
import sys, json, time
import gs_lib as g
from gs_lib import Page, PT, INK, BODY, GREY, BLUE, DEEP, PANEL, LAV, LINE, WHITE, GREEN, RED, DARK, FONT, MONO
import content as C

DECK = '1IzB5Cu6PGBEKGJzVGqc4mWpTNyNjLGmBHYyCTV-a7r8'
LOGO_URL = C.LOGO_URL          # white Poshmark wordmark PNG on Drive, anyone-reader
LOGO_ASPECT = 648 / 87          # padded PNG 648x87
S = {  # slide ids (preserved by the Drive copy of 1hrBLCF...)
    'cover': 'n01_g3f77215683c_1_445', 'exec': 'of_exec_understanding_v2', 'problem': 'vlt_problem', 'm5': 'm5_mock',
    'cards': 'vlt_cards', 'nt': 'h7c266de662ba1cf0_9_207', 'personal': 'vlt_personal', 'design': 'h7c266de662ba1cf0_9_241',
    'proxy': 'h7c266de662ba1cf0_9_391', 'controls': 'vlt_controls', 'versus': 'vlt_versus', 'port': 'h7c266de662ba1cf0_9_469',
    'proven': 'h6032acb876a0077a_1_0', 'team': 'h6032acb876a0077a_1_974', 'trusted': 'h7c266de662ba1cf0_9_611'}
ORDER = ('cover', 'exec', 'problem', 'm5', 'cards', 'nt', 'personal', 'design', 'proxy', 'controls', 'versus', 'port', 'proven', 'team', 'trusted')

def cover_logo(P, R):
    """Swap the OnlyFans wordmark (x=157 y=53 w=131 h=23) for the white Poshmark wordmark, same box, vertically centred."""
    cov = S['cover']
    sl = g.slide(P, cov)
    have = any(e['objectId'] == 'posh_cover_logo' for e in sl['pageElements'])
    old = [e for e in sl['pageElements'] if 'image' in e and e['objectId'] != 'posh_cover_logo'
           and 120 < e['transform']['translateX'] / PT < 200 and e['transform']['translateY'] / PT < 80]
    for e in old: R.append({'deleteObject': {'objectId': e['objectId']}})
    if have: return
    x, y, bw, bh = 157, 53, 131, 23
    w = min(bw, bh * LOGO_ASPECT); h = w / LOGO_ASPECT
    R.append({'createImage': {'objectId': 'posh_cover_logo', 'url': LOGO_URL, 'elementProperties': {'pageObjectId': cov,
              'size': {'width': {'magnitude': w * PT, 'unit': 'EMU'}, 'height': {'magnitude': h * PT, 'unit': 'EMU'}},
              'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': x * PT, 'translateY': (y + (bh - h) / 2) * PT, 'unit': 'EMU'}}}})

def main(dry=False):
    s = g.svc(); pid = DECK
    P = s.presentations().get(presentationId=pid).execute()
    json.dump(P, open('backup_poshmark_prebuild_' + time.strftime('%H%M%S') + '.json', 'w'))
    R = []
    # ---------------------------------------------------------------- 1. cover
    cov = S['cover']
    g.set_text(P, cov, 'The OnlyFans Yuno Vault', C.COVER['title'], R)
    g.set_text(P, cov, 'Your schema, your connections, your vault.', C.COVER['sub'], R)
    g.set_text(P, cov, 'Prepared for OnlyFans', C.COVER['prep'], R)
    cover_logo(P, R)
    # ---------------------------------------------------------------- 2. executive summary
    for oid, t in C.EXEC.items(): g.set_text_id(P, S['exec'], oid, t, R)
    # ---------------------------------------------------------------- 4. integrated vs standalone
    for oid, t in C.M5.items(): g.set_text_id(P, S['m5'], oid, t, R)
    # ---------------------------------------------------------------- 5. cards
    for oid, t in C.CARDS.items(): g.set_text_id(P, S['cards'], oid, t, R)
    # ---------------------------------------------------------------- 6. network tokens
    for oid, t in C.NT.items(): g.set_text_id(P, S['nt'], oid, t, R)
    # ---------------------------------------------------------------- 8. your design
    for oid, t in C.DESIGN.items(): g.set_text_id(P, S['design'], oid, t, R)
    # ---------------------------------------------------------------- 9. proxy how it works
    for oid, t in C.PROXY.items(): g.set_text_id(P, S['proxy'], oid, t, R)
    R.append(g.rep(S['proxy'], '"amount": 1499', '"amount": %s' % C.PROXY_AMOUNT))
    # ---------------------------------------------------------------- 10. controls
    for oid, t in C.CONTROLS.items(): g.set_text_id(P, S['controls'], oid, t, R)
    # ---------------------------------------------------------------- 11. versus
    for oid, t in C.VERSUS.items(): g.set_text_id(P, S['versus'], oid, t, R)
    for oid, col in C.VERSUS_COLORS.items():
        R.append({'updateTextStyle': {'objectId': oid, 'textRange': {'type': 'ALL'}, 'style': {'foregroundColor': {'opaqueColor': {'rgbColor': g.rgb(col)}}}, 'fields': 'foregroundColor'}})
    # ---------------------------------------------------------------- 12. portability
    for oid, t in C.PORT.items(): g.set_text_id(P, S['port'], oid, t, R)
    if dry:
        print(json.dumps([r for r in R if 'insertText' in r], indent=1, ensure_ascii=False)[:30000]); return
    g.run(s, pid, R, 'text edits')

    # ---------------------------------------------------------------- 3. problem (rebuilt body)
    P = s.presentations().get(presentationId=pid).execute()
    p = g.clear_body(s, pid, P, S['problem'], kicker=C.PROBLEM['kicker'], title=C.PROBLEM['title'])
    draw_problem(p); g.run(s, pid, p.R, 'problem body')
    # ---------------------------------------------------------------- 7. offers and shows (replaces personal data)
    P = s.presentations().get(presentationId=pid).execute()
    p = g.clear_body(s, pid, P, S['personal'], kicker=C.OFFER['kicker'], title=C.OFFER['title'])
    draw_offer(p); g.run(s, pid, p.R, 'offer body')
    # ---------------------------------------------------------------- speaker notes
    P = s.presentations().get(presentationId=pid).execute()
    N = []
    for key, text in C.NOTES.items(): N += g.set_notes(s, pid, P, S[key], text)
    g.run(s, pid, N, 'speaker notes')
    g.finish(s, pid, [S[k] for k in ORDER])

# -------------------------------------------------------------------- drawings (OnlyFans vault design tokens)
def draw_problem(p):
    c = C.PROBLEM
    # TODAY
    p.card(36, 84, 300, 286)
    p.text(50, 96, 60, 14, 'TODAY', size=8, color=GREY, weight=600)
    p.text(96, 93, 220, 18, c['before_h'], size=13, color=INK, weight=600)
    for i, (name, sub, chips) in enumerate(c['stacks']):
        x = 50 + i * 140
        p.card(x, 120, 130, 122, fill=PANEL, line=None)
        p.text(x + 10, 128, 112, 16, name, size=11, color=INK, weight=600)
        p.text(x + 10, 144, 112, 26, sub, size=8.5, color=GREY, ls=112)
        for j, t in enumerate(chips):
            p.card(x + 10, 170 + j * 23, 110, 19, fill=WHITE, line=LINE); p.text(x + 16, 173 + j * 23, 100, 12, t, size=8.5, color=INK)
    for i, t in enumerate(c['before_x']):
        p.text(52, 256 + i * 20, 12, 14, '×', size=10, color=GREY, weight=600)
        p.text(66, 257 + i * 20, 262, 14, t, size=9.5, color=INK)
    p.text(52, 320, 272, 40, c['before_src'], size=7.5, color=GREY, ls=112)
    # arrow
    p.shape(342, 214, 26, 26, 'ELLIPSE', BLUE, None)
    p.text(342, 218, 26, 16, '→', size=12, color=WHITE, weight=600, align='CENTER')
    # WITH YUNO
    p.card(374, 84, 310, 286, fill=PANEL, line=BLUE, lw=1)
    p.text(388, 96, 50, 14, 'WITH YUNO', size=8, color=BLUE, weight=600)
    p.text(448, 93, 200, 18, c['after_h'], size=13, color=INK, weight=600)
    for i, t in enumerate(c['swappable']):
        x = 388 + i * 96
        p.card(x, 118, 88, 44, fill=WHITE, line=LINE)
        p.text(x + 8, 124, 76, 14, t, size=9.5, color=INK, weight=600)
        p.pill(x + 8, 142, 64, 'SWAPPABLE', fill=LAV, color=BLUE, size=7, h=13)
        p.line(x + 44, 162, x + 44, 176, '#C9CDD6', 1)
    p.card(388, 176, 282, 70, fill=BLUE, line=None)
    p.text(400, 186, 200, 16, 'Yuno Vault', size=12, color=WHITE, weight=600)
    for i, t in enumerate(c['vault_pills']):
        p.pill(398 + i * 68, 214, 64, t, fill=BLUE, color=WHITE, size=7, h=16, line=WHITE)
    for i, t in enumerate(c['after_ok']):
        p.shape(390, 262 + i * 22, 13, 13, 'ELLIPSE', BLUE, None)
        p.text(390, 263 + i * 22, 13, 10, '✓', size=7.5, color=WHITE, weight=600, align='CENTER', pad=False)
        p.text(410, 261 + i * 22, 260, 14, t, size=9.5, color=INK)

def draw_offer(p):
    c = C.OFFER
    p.card(36, 84, 384, 284)
    p.shape(50, 98, 22, 22, 'ELLIPSE', LAV, None)
    p.text(50, 102, 22, 12, c['initials'], size=8, color=BLUE, weight=600, align='CENTER')
    p.text(80, 99, 140, 18, c['name'], size=13, color=INK, weight=600)
    p.text(176, 102, 80, 14, c['ref'], size=9, color=GREY, font=MONO)
    p.pill(316, 100, 92, 'PCI DSS LEVEL 1', size=7.5, h=16)
    for x, t in ((50, 'FIELD'), (176, 'STORED AS'), (320, c['col3'])):
        p.label(x, 134, 110, t, size=7.5)
    y = 152
    for f, v, use, kind in c['rows']:
        p.line(50, y - 3, 406, y - 3, LINE, 0.75)
        p.text(50, y + 3, 124, 14, f, size=9.5, color=INK)
        p.text(176, y + 3, 140, 14, v, size=9, color=INK, font=MONO)
        if kind == 'blue': p.pill(320, y + 3, 86, use, size=7, h=15)
        else: p.pill(320, y + 3, 86, use, fill=LAV, color=BLUE, size=7, h=15)
        y += 27
    p.line(50, y - 3, 406, y - 3, LINE, 0.75)
    p.text(50, y + 8, 356, 26, c['foot'], size=8.5, color=GREY, ls=112)
    ys = [100, 188, 276]
    for (t, sub), yy in zip(c['right'], ys):
        p.line(420, yy + 27, 466, yy + 27, '#C9CDD6', 1, arrow=True)
        p.card(468, yy, 216, 58)
        p.text(480, yy + 8, 196, 16, t, size=10.5, color=INK, weight=600)
        p.text(480, yy + 27, 198, 26, sub, size=8.5, color=GREY, ls=112)
    p.text(468, 344, 216, 24, c['quote'], size=7.5, color=GREY, ls=112)

if __name__ == '__main__':
    main(dry=(len(sys.argv) > 1 and sys.argv[1] == 'dry'))
