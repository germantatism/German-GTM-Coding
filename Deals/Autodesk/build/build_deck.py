# -*- coding: utf-8 -*-
"""Turn the copy of the OnlyFans token vault deck into the Autodesk orchestration and vault deck (12 slides).
  python3 build_deck.py            -> apply everything to DECK
  python3 build_deck.py dry        -> print the planned text edits only
Copy lives in content.py. Pattern: Deals/Poshmark/build/build_vault_deck.py (23 Oct 2026)."""
import sys, json, time
import gs_lib as g
from gs_lib import Page, PT, INK, BODY, GREY, BLUE, DEEP, PANEL, LAV, LINE, WHITE, GREEN, RED, DARK, FONT, MONO
import content as C

DECK = '1H0NFvyWIPy6tGDQi7E_910v08y2Sokf_vkvvrF9o6-s'
LOGO_URL = C.LOGO_URL           # white Autodesk logo PNG on Drive, anyone-reader
LOGO_ASPECT = 640 / 112         # padded PNG, overwritten at runtime from LOGO_ASPECT.txt when present
S = {  # slide ids (preserved by the Drive copy of 1hrBLCF...)
    'cover': 'n01_g3f77215683c_1_445', 'exec': 'of_exec_understanding_v2', 'today': 'vlt_problem', 'm5': 'm5_mock',
    'cards': 'vlt_cards', 'nt': 'h7c266de662ba1cf0_9_207', 'personal': 'vlt_personal', 'design': 'h7c266de662ba1cf0_9_241',
    'proxy': 'h7c266de662ba1cf0_9_391', 'controls': 'vlt_controls', 'versus': 'vlt_versus', 'port': 'h7c266de662ba1cf0_9_469',
    'proven': 'h6032acb876a0077a_1_0', 'team': 'h6032acb876a0077a_1_974', 'trusted': 'h7c266de662ba1cf0_9_611',
    # new slides, drawn from the chrome of vlt_versus
    'orch': 'ad_orch', 'renew': 'ad_renew', 'subs': 'ad_subs', 'depth': 'ad_depth', 'beyond': 'ad_beyond', 'close': 'ad_close',
    'team2': 'h4674785995ee081b_0_1058', 'ask': 'ad_ask'}   # team slide German pasted in by hand on 26 Oct evening (not the OnlyFans 'team' id)
BASE = 'versus'   # chrome donor for the new slides (kicker 322x14, title 648x54, page number, wordmark)
ORDER = ('cover', 'exec', 'today', 'orch', 'renew', 'subs', 'cards', 'port', 'beyond', 'proven', 'team2', 'trusted')   # no closing slide: German deleted 'close' twice and 'ask' once by hand (26 Oct); the ask lives in the email   # 26 Oct evening: German removed 'close' by hand (twice, keep it out) and pasted a team slide before trusted; m5 and depth cut
WALL_URL = ''     # logo wall PNG (companies billing recurring payments through Yuno), anyone-reader on Drive
try:
    WALL_URL = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'SUBS_WALL_URL.txt')).read().strip()
except Exception:
    pass
CHIPS_URL = ''    # slide 3 methods column: one PNG of logo chips per market (methods_chips.py), anyone-reader on Drive
try:
    CHIPS_URL = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'TODAY_CHIPS_URL.txt')).read().strip()
except Exception:
    pass

try:
    import os
    LOGO_ASPECT = float(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'LOGO_ASPECT.txt')).read().strip())
except Exception:
    pass


def cover_logo(P, R):
    """Swap the OnlyFans wordmark (x=157 y=53 w=131 h=23) for the white Autodesk logo, same box, vertically centred."""
    cov = S['cover']
    sl = g.slide(P, cov)
    els = list(g.walk(sl['pageElements']))          # the lockup lives inside a group: walk into it
    have = any(e['objectId'] == 'adsk_cover_logo' for e in els)
    old = [e for e in els if 'image' in e and e['objectId'] != 'adsk_cover_logo'
           and 120 < e['transform']['translateX'] / PT < 240 and e['transform']['translateY'] / PT < 80]
    for e in old: R.append({'deleteObject': {'objectId': e['objectId']}})
    if have or not LOGO_URL: return
    # visual lockup on the rendered cover: yuno wordmark spans x 29..88 pt, y 36..53 pt; the "+" sits at x 101 pt
    x, y, bw, bh = 116, 37, 140, 15
    w = min(bw, bh * LOGO_ASPECT); h = w / LOGO_ASPECT
    R.append({'createImage': {'objectId': 'adsk_cover_logo', 'url': LOGO_URL, 'elementProperties': {'pageObjectId': cov,
              'size': {'width': {'magnitude': w * PT, 'unit': 'EMU'}, 'height': {'magnitude': h * PT, 'unit': 'EMU'}},
              'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': x * PT, 'translateY': (y + (bh - h) / 2) * PT, 'unit': 'EMU'}}}})


def fresh(s, pid, P, key, kicker, title):
    """A Page for a new slide: duplicate the chrome donor the first time, clear the body on later runs."""
    sid = S[key]
    if any(sl['objectId'] == sid for sl in P['slides']):
        return g.clear_body(s, pid, P, sid, kicker=kicker, title=title)
    live = {sl['objectId'] for sl in P['slides']}
    donor = next(S[k] for k in (BASE, 'orch', 'renew', 'beyond', 'close') if S[k] in live)   # the OnlyFans donor is gone after the first finish()
    return g.new_slide(s, pid, P, donor, sid, kicker, title)


def main(dry=False):
    s = g.svc(); pid = DECK
    P = s.presentations().get(presentationId=pid).execute()
    json.dump(P, open('backup_autodesk_prebuild_' + time.strftime('%H%M%S') + '.json', 'w'))
    R = []
    # ---------------------------------------------------------------- 1. cover
    cov = S['cover']
    g.set_text(P, cov, 'The OnlyFans Yuno Vault', C.COVER['title'], R) or g.set_text(P, cov, C.COVER['title'], C.COVER['title'], R)
    g.set_text(P, cov, 'Your schema, your connections, your vault.', C.COVER['sub'], R) or g.set_text(P, cov, C.COVER['sub'], C.COVER['sub'], R)
    g.set_text(P, cov, 'Prepared for', C.COVER['prep'], R)
    cover_logo(P, R)
    # ---------------------------------------------------------------- 2. executive summary
    for oid, t in C.EXEC.items(): g.set_text_id(P, S['exec'], oid, t, R)
    # ---------------------------------------------------------------- 4. one vendor for both halves
    if 'm5' in ORDER:
        for oid, t in C.M5.items(): g.set_text_id(P, S['m5'], oid, t, R)
    # ---------------------------------------------------------------- 7. cards
    for oid, t in C.CARDS.items(): g.set_text_id(P, S['cards'], oid, t, R)
    # ---------------------------------------------------------------- 8. portability
    for oid, t in C.PORT.items(): g.set_text_id(P, S['port'], oid, t, R)
    if dry:
        print(json.dumps([r for r in R if 'insertText' in r], indent=1, ensure_ascii=False)[:30000]); return
    g.run(s, pid, R, 'text edits')

    # ---------------------------------------------------------------- 3. how things stand today (rebuilt body)
    P = s.presentations().get(presentationId=pid).execute()
    p = g.clear_body(s, pid, P, S['today'], kicker=C.TODAY['kicker'], title=C.TODAY['title'])
    draw_today(p); g.run(s, pid, p.R, 'today body')
    # ---------------------------------------------------------------- 5. orchestration architecture (new)
    P = s.presentations().get(presentationId=pid).execute()
    p = fresh(s, pid, P, 'orch', C.ORCH['kicker'], C.ORCH['title']); draw_orch(p); g.run(s, pid, p.R, 'orch body')
    # ---------------------------------------------------------------- 6. renewals (new)
    P = s.presentations().get(presentationId=pid).execute()
    p = fresh(s, pid, P, 'renew', C.RENEW['kicker'], C.RENEW['title']); draw_renew(p); g.run(s, pid, p.R, 'renew body')
    # ---------------------------------------------------------------- 7. subscription engine (new)
    P = s.presentations().get(presentationId=pid).execute()
    p = fresh(s, pid, P, 'subs', C.SUBS['kicker'], C.SUBS['title']); draw_subs(p)
    try:
        g.run(s, pid, p.R, 'subs body')
    except Exception as e:   # the logo wall URL may not be fetchable yet: draw everything else, add the image later
        print('  subs body: wall image rejected, retrying without it:', str(e)[-90:])
        g.run(s, pid, [r for r in p.R if 'createImage' not in r], 'subs body (no wall)')
    # ---------------------------------------------------------------- 8. billing depth (new)
    if 'depth' in ORDER:
        P = s.presentations().get(presentationId=pid).execute()
        p = fresh(s, pid, P, 'depth', C.DEPTH['kicker'], C.DEPTH['title']); draw_depth(p); g.run(s, pid, p.R, 'depth body')
    # ---------------------------------------------------------------- 9. beyond (new)
    P = s.presentations().get(presentationId=pid).execute()
    p = fresh(s, pid, P, 'beyond', C.BEYOND['kicker'], C.BEYOND['title']); draw_beyond(p); g.run(s, pid, p.R, 'beyond body')
    # ---------------------------------------------------------------- 12. next steps (new)
    P = s.presentations().get(presentationId=pid).execute()
    p = fresh(s, pid, P, 'close', C.CLOSE['kicker'], C.CLOSE['title']); draw_close(p); g.run(s, pid, p.R, 'close body')
    # ---------------------------------------------------------------- speaker notes
    P = s.presentations().get(presentationId=pid).execute()
    N = []
    for key, text in C.NOTES.items():
        if key in ORDER: N += g.set_notes(s, pid, P, S[key], text)
    g.run(s, pid, N, 'speaker notes')
    g.finish(s, pid, [S[k] for k in ORDER])


# -------------------------------------------------------------------- drawings (OnlyFans vault design tokens)
def dot(p, x, y, color=BLUE, d=5):
    p.shape(x, y, d, d, 'ELLIPSE', color, None)


def tick(p, x, y, text, w=260, size=9.5, color=INK):
    """Unused since 26 Oct evening: the check glyph and the 13 pt text box did not survive the editor. Use dot()."""
    dot(p, x + 4, y + 5)
    p.text(x + 20, y, w, 14, text, size=size, color=color)


TOP = 96   # body start on slides with a two-line title (title box ends at 95)
SRC_Y = 368   # source line baseline shared by the drawn slides (page number sits at 376)


def draw_today(p):
    """Left: the business (246 wide). Right: stores and methods (390 wide), market names as text and the methods as one
    image of logo chips (assets/today_chips.png, 304 x 198 pt, rows on the same 22 pt pitch as the lines drawn here)."""
    c = C.TODAY
    # ---- left: the business
    p.card(36, TOP, 246, 274)
    p.text(50, TOP + 10, 200, 12, c['left_h'], size=7.5, color=GREY, weight=600)
    for i, (v, l, sub) in enumerate(c['tiles']):
        x = 50 + (i % 2) * 112; y = TOP + 26 + (i // 2) * 66
        p.card(x, y, 106, 60, fill=PANEL, line=None)
        p.text(x + 9, y + 5, 92, 22, v, size=18, color=BLUE, weight=600)
        p.text(x + 9, y + 29, 92, 10, l, size=6.5, color=GREY, weight=600)
        p.text(x + 9, y + 40, 92, 18, sub, size=7, color=BODY, ls=105)
    for i, t in enumerate(c['bullets']):
        y = TOP + 164 + i * 19
        dot(p, 52, y + 5)
        p.text(64, y, 212, 14, t, size=8, color=INK)
    p.text(50, TOP + 226, 220, 40, c['left_src'], size=6.5, color=GREY, ls=110)
    # ---- right: stores and methods
    p.card(294, TOP, 390, 274)
    p.text(308, TOP + 10, 360, 12, c['right_h'], size=7.5, color=GREY, weight=600)
    p.text(308, TOP + 26, 56, 10, c['col1'], size=6, color=GREY, weight=600)
    p.text(366, TOP + 26, 300, 10, c['col2'], size=6, color=GREY, weight=600)
    y = TOP + 40
    for mk, _methods in c['rows']:
        p.line(308, y - 2, 670, y - 2, LINE, 0.5)
        p.text(308, y + 2, 58, 14, mk, size=7.5, color=INK, weight=600)
        y += 22
    p.line(308, y - 2, 670, y - 2, LINE, 0.5)
    p.text(308, y + 3, 362, 26, c['right_note'], size=6.5, color=GREY, ls=110)
    if CHIPS_URL:
        p.R.append({'createImage': {'objectId': 'ad_today_chips', 'url': CHIPS_URL, 'elementProperties': {'pageObjectId': p.sid,
                    'size': {'width': {'magnitude': 304 * PT, 'unit': 'EMU'}, 'height': {'magnitude': 198 * PT, 'unit': 'EMU'}},
                    'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': 366 * PT, 'translateY': (TOP + 38) * PT, 'unit': 'EMU'}}}})

def draw_orch(p):
    """v2 (26 Oct night): the Yuno box with its modules on the left, six outcome tiles on the right, the Autodesk-scale band."""
    c = C.ORCH
    p.label(36, TOP + 2, 300, c['left_h'], color=GREY, size=7)
    p.label(436, TOP + 2, 248, c['right_h'], color=GREY, size=7)
    B = TOP + 16   # 112
    p.card(36, B, 380, 172, fill=BLUE, line=None)
    p.text(50, B + 8, 352, 18, c['box_title'], size=14, color=WHITE, weight=600)
    p.text(50, B + 27, 352, 10, c['box_sub'], size=7.5, color=LAV)
    for i, m in enumerate(c['mods']):
        x = 50 + (i % 2) * 180; y = B + 44 + (i // 2) * 29
        p.pill(x, y, 172, m, fill=WHITE, color=DEEP, size=7.5, h=23)
    p.text(50, B + 157, 352, 12, c['box_foot'], size=7, color=LAV)
    for i, (v, l, src) in enumerate(c['tiles']):
        x = 436 + (i % 2) * 128; y = B + (i // 2) * 59
        p.card(x, y, 120, 52, fill=PANEL, line=None)
        p.text(x + 10, y + 3, 104, 22, v, size=17, color=BLUE, weight=600)
        p.text(x + 10, y + 25, 104, 17, l, size=7, color=INK, ls=105)
        p.text(x + 10, y + 42, 104, 9, src, size=6, color=GREY)
    p.card(36, 300, 648, 40, fill=PANEL, line=None)
    p.shape(36, 300, 2, 40, 'RECTANGLE', BLUE, None)
    p.text(50, 300, 620, 40, c['band'], size=9.5, color=INK, valign='MIDDLE', bold_color=DEEP)
    p.text(36, SRC_Y - 4, 640, 22, c['src'], size=6.5, color=GREY, ls=110)

def draw_renew(p):
    c = C.RENEW
    top = TOP + 8   # 104
    p.pill(36, top, 62, 'ILLUSTRATIVE', fill=LAV, color=GREY, size=6.5, h=13)
    k, amt, sub = c['pay']
    p.card(36, top + 44, 104, 60)
    p.text(46, top + 51, 88, 9, k, size=6.5, color=GREY, weight=600)
    p.text(46, top + 63, 92, 13, amt, size=9, color=INK, weight=600)
    p.text(46, top + 78, 92, 20, sub, size=7, color=GREY, ls=105)
    p.line(140, top + 74, 152, top + 74, BLUE, 1, arrow=True)
    e1, e2, e3 = c['engine']
    p.card(154, top + 32, 114, 84, fill=BLUE, line=None)
    p.text(164, top + 40, 96, 14, e1, size=11, color=WHITE, weight=600)
    p.text(164, top + 57, 96, 10, e2, size=7.5, color=LAV)
    p.text(164, top + 72, 96, 36, e3, size=7, color=WHITE, ls=108)
    styles = {'DECLINED': ('#FBE9E7', RED, '1'), 'APPROVED': ('#E2F3EB', GREEN, '2'), 'STANDBY': (LAV, GREY, '')}
    for i, (name, st) in enumerate(c['providers']):
        f, col, n = styles[st]
        y = top + 4 + i * 50
        p.line(268, top + 74, 318, y + 20, BLUE if n else '#C9CDD6', 1 if n else 0.75, arrow=True)
        p.card(318, y, 132, 40)
        p.text(328, y + 13, 70, 14, name, size=9, color=INK, weight=600)
        p.pill(388, y + 12, 54, st, fill=f, color=col, size=6.5, h=16)
        if n:
            mx, my = 293, (top + 74 + y + 20) / 2
            p.shape(mx - 7, my - 7, 14, 14, 'ELLIPSE', WHITE, BLUE, 1)
            p.text(mx - 20, my - 8, 40, 16, n, size=7, color=BLUE, weight=600, align='CENTER', pad=False)   # wide box, text centred on the circle
    for i, (n, t) in enumerate(c['steps']):
        x = 36 + i * 140
        p.card(x, 272, 132, 54, fill=PANEL, line=None)
        p.text(x + 10, 278, 20, 14, n, size=11, color=BLUE, weight=600)
        p.text(x + 10, 294, 114, 30, t, size=7.5, color=INK, ls=105)
    # right column
    p.card(470, TOP, 214, 230, fill=PANEL, line=None)   # ends at 326 like the step cards on the left
    p.text(482, TOP + 10, 190, 9, c['right_h'], size=7, color=BLUE, weight=600)
    (v1, l1), (v2, l2) = c['stats']
    p.text(482, TOP + 22, 90, 28, v1, size=22, color=BLUE)
    p.text(482, TOP + 50, 90, 10, l1, size=8, color=BODY)
    p.text(584, TOP + 22, 90, 28, v2, size=22, color=BLUE)
    p.text(584, TOP + 50, 90, 10, l2, size=8, color=BODY)
    p.line(482, TOP + 68, 672, TOP + 68, '#C9CDD6', 0.5)
    for i, t in enumerate(c['checks']):
        y = TOP + 78 + i * 42
        dot(p, 484, y + 4)
        p.text(498, y - 1, 174, 34, t, size=8.5, color=INK, ls=108)
    p.text(36, SRC_Y - 4, 640, 22, c['src'], size=6.5, color=GREY, ls=110)   # two lines, same baseline as the other slides


def draw_subs(p):
    """Stats row, then the subscription engine as a five-step flow on the orchestration band (no logo wall, 26 Oct evening)."""
    c = C.SUBS
    T0 = TOP - 8   # one-line title
    for i, (tt, body) in enumerate(c['fit']):
        x = 36 + i * 328
        p.card(x, T0, 320, 44, fill=PANEL, line=None)
        p.text(x + 12, T0 + 5, 296, 12, tt, size=8, color=DEEP, weight=600)
        p.text(x + 12, T0 + 18, 296, 24, body, size=6.5, color=INK, ls=106)
    p.label(36, T0 + 54, 420, c['flow_h'], color=GREY, size=7)
    B = T0 + 68
    for i, (n, tt, d, tag) in enumerate(c['steps']):
        x = 36 + i * 132; w = 120
        p.card(x, B, w, 96)
        p.pill(x + 8, B + 9, 28, n, fill=BLUE, color=WHITE, size=6.5, h=13)   # shape insets eat 14 pt, keep it wide
        p.text(x + 38, B + 5, w - 42, 22, tt, size=7.5, color=INK, weight=600, valign='MIDDLE')
        p.text(x + 8, B + 30, w - 16, 48, d, size=7, color=BODY, ls=108)
        p.text(x + 8, B + 80, w - 16, 10, tag, size=6.5, color=BLUE, weight=600)
        if i < 4: p.line(x + w, B + 48, x + 132, B + 48, BLUE, 1, arrow=True)
    y = B + 106
    p.card(36, y, 648, 28, fill=BLUE, line=None)
    p.text(48, y, 624, 28, c['band'], size=8.5, color=WHITE, valign='MIDDLE', bold_color=WHITE)
    y2 = y + 36
    for (x, w, hh, body) in ((36, 320, c['box1_h'], c['box1']), (364, 320, c['box2_h'], c['box2'])):
        p.card(x, y2, w, 60, fill=PANEL, line=None)
        p.text(x + 12, y2 + 6, w - 24, 10, hh, size=7, color=BLUE, weight=600)
        p.text(x + 12, y2 + 18, w - 24, 40, body, size=7.5, color=INK, ls=108)
    p.text(36, SRC_Y, 640, 10, c['src'], size=6.5, color=GREY)

def draw_depth(p):
    c = C.DEPTH
    p.text(36, 84, 470, 32, c['intro'], size=9.5, color=INK, ls=115)
    p.card(520, 80, 164, 56, fill=BLUE, line=None)
    p.text(530, 86, 144, 10, c['diff_h'], size=7, color=WHITE, weight=600)
    p.text(530, 97, 144, 38, c['diff'], size=7.5, color=WHITE, ls=108, bold_color=WHITE)
    cw, ch = 154, 96
    for i, (t, body, tag) in enumerate(c['cards']):
        x = 36 + (i % 4) * 164.67; y = 144 + (i // 4) * 104
        p.card(x, y, cw, ch)
        p.text(x + 10, y + 8, cw - 20, 12, t, size=9.5, color=INK, weight=600)
        p.text(x + 10, y + 23, cw - 20, 44, body, size=7.5, color=BODY, ls=110)
        p.pill(x + 10, y + 72, cw - 20, tag, fill=LAV, color=BLUE, size=7, h=15)
    p.card(36, 352, 648, 24, fill=BLUE, line=None)
    p.text(48, 352, 72, 24, 'ENABLED BY', size=7.5, color=WHITE, weight=600, valign='MIDDLE')
    p.line(126, 356, 126, 372, '#7C89EF', 0.75)
    for j, (t, sub) in enumerate(c['enabled']):
        p.text(140 + j * 185, 352, 180, 24, f'**{t}**  ' + sub, size=7.5, color=LAV, valign='MIDDLE', bold_color=WHITE)


def draw_ask(p):
    """Closing slide, 26 Oct evening: three asks on cards, then the contact band."""
    c = C.ASK
    T0 = TOP - 8
    for i, (k, tt, d) in enumerate(c['cards']):
        x = 36 + i * 220; w = 208
        p.card(x, T0, w, 148)
        p.shape(x, T0, w, 3, 'RECTANGLE', BLUE, None)
        p.text(x + 14, T0 + 16, w - 28, 10, k, size=7, color=BLUE, weight=600)
        p.text(x + 14, T0 + 32, w - 28, 18, tt, size=12, color=INK, weight=600)
        p.text(x + 14, T0 + 58, w - 28, 80, d, size=8.5, color=BODY, ls=115)
    y = 300   # sign-off band at the foot of the slide, like the house closing slides
    p.card(36, y, 648, 56, fill=BLUE, line=None)
    p.text(52, y, 300, 56, c['band'], size=14, color=WHITE, weight=600, valign='MIDDLE', bold_color=WHITE)
    p.text(380, y, 292, 56, c['contact'], size=8, color=WHITE, align='END', valign='MIDDLE', ls=120)


def draw_beyond(p):
    c = C.BEYOND
    cw, gap = 153, 12
    for i, (t, body, who) in enumerate(c['cards']):
        x = 36 + i * (cw + gap)
        p.card(x, TOP, cw, 182)
        p.shape(x, TOP, cw, 3, 'RECTANGLE', BLUE, None)
        p.text(x + 12, TOP + 14, cw - 24, 16, t, size=12, color=INK, weight=600)
        p.text(x + 12, TOP + 36, cw - 24, 98, body, size=8.5, color=BODY, ls=115)
        p.line(x + 12, TOP + 140, x + cw - 12, TOP + 140, LINE, 0.5)
        p.text(x + 12, TOP + 147, cw - 24, 9, 'BUILT FOR', size=6.5, color=GREY, weight=600)
        p.text(x + 12, TOP + 159, cw - 24, 20, who, size=8, color=BLUE, weight=600, ls=105)
    p.card(36, 292, 648, 36, fill=WHITE, line=BLUE)
    p.pill(48, 303, 40, c['also_pill'], fill=LAV, color=BLUE, size=7, h=15)
    p.text(98, 292, 570, 36, c['also'], size=9.5, color=INK, valign='MIDDLE', bold_color=DEEP)
    p.text(36, SRC_Y, 600, 12, c['src'], size=6.5, color=GREY)


def draw_close(p):
    c = C.CLOSE
    p.card(36, 90, 648, 150, fill=PANEL, line=None)
    cw = 190
    for i, (k, t, b) in enumerate(c['steps']):
        x = 54 + i * (cw + 23)
        p.card(x, 104, cw, 122)
        p.text(x + 14, 116, 150, 10, k, size=8, color=BLUE, weight=600)
        p.text(x + 14, 132, cw - 28, 16, t, size=13, color=INK, weight=600)
        p.text(x + 14, 154, cw - 28, 64, b, size=9, color=BODY, ls=115)
        if i < 2: p.line(x + cw + 3, 165, x + cw + 20, 165, BLUE, 1.25, arrow=True)
    p.text(36, 250, 648, 12, c['security'], size=8, color=GREY)
    p.card(36, 272, 648, 56, fill=BLUE, line=None)
    p.text(52, 272, 300, 56, c['band'], size=14, color=WHITE, valign='MIDDLE', bold_color=WHITE)
    p.text(330, 272, 340, 56, c['contact'], size=9, color=WHITE, align='END', valign='MIDDLE', ls=120)


if __name__ == '__main__':
    main(dry=(len(sys.argv) > 1 and sys.argv[1] == 'dry'))
