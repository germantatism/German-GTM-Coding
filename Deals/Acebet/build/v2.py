# -*- coding: utf-8 -*-
"""v2.py · 'Proposal - Acebet + Yuno (v2)' in the new look (OnlyFans / General deck: Titillium Web, blue bar headlines,
#F4F5FD panels, dark swirl cover). Base = Drive copy of 'Yuno · General deck (Oct 2026)', so the house slides
(cover, who we are, smart routing, proven, results, team, trusted by) keep their ids; Acebet slides are drawn with gsl.

  python3 v2.py dry        # build every request, execute nothing
  python3 v2.py build      # draw the Acebet slides, edit cover and house slides, set order, delete the rest
Pricing numbers come from model.py (German, 27-oct-2026). No business case."""
import sys, os, json
sys.path.insert(0, '/Users/germantatis/Desktop/GTMCoding/Deals/Yuno General Deck/build')
from gsl import *
from model import *

PID = os.environ.get('V2_PID', '18yGkpovjzJqul9EUTaHj82w5l5eucG26dIrGz1ALbx4')
WORK = '/private/tmp/claude-501/-Users-germantatis-Desktop-GTMCoding/79b9e111-4187-4fd7-9475-2367c131665a/scratchpad/acebet_v2'
os.makedirs(WORK, exist_ok=True)
X0, W0 = 36, 648
CHROME = 'pg_7669191a8125'             # 'The problem' slide: its c_* elements are the chrome (bg, kicker, headline, bar, page, wordmark)
COVER, S02, S06, PROVEN, S10, TEAM, TRUSTED = ('n01_g3f77215683c_1_445', 'pg_147d86386d35', 'pg_653ae9e65354',
                                               'h6032acb876a0077a_1_0', 'pg_313215eef259', 'h7dc675c3e48ab6fb_3_0', 'h7dc675c3e48ab6fb_3_58')
ORDER = ['cover', 'heard', 's02', 'setup', 's06', 'proven', 's10', 'team', 'trusted', 'price', 'terms', 'next']
HOUSE = {'cover': COVER, 's02': S02, 's06': S06, 'proven': PROVEN, 's10': S10, 'team': TEAM, 'trusted': TRUSTED}
b = bands(TX); V, TOT = var(TX), total(TX)
c3 = lambda r: f'${r:.3f}'


def band(s, y, h, txt, size=9.5):
    s.rect(X0, y, W0, h, fill=PANEL); s.rect(X0, y, 2, h, fill=BLUE)
    s.text(X0 + 14, y, W0 - 24, h, txt, size=size, color=INK, valign='MIDDLE', bold_color=DEEP)


def label(s, x, y, txt, color=BLUE, w=220):
    s.text(x, y, w, 9, txt.upper(), size=7, color=color, weight=600)


def dot(s, x, y, txt, size=9, w=250, h=14):
    """Deck bullet: a small blue square dot, no glyphs (✓ overflows in the editor)."""
    s.rect(x, y + size * 0.42, 4, 4, fill=BLUE, kind='ELLIPSE')
    s.text(x + 11, y, w, h, txt, size=size, color=INK, spacing=108)


def source(s, txt):
    s.text(X0, 372, 600, 9, txt, size=6.5, color=GREY)


SLIDES = {}
def slide(key, kicker, headline):
    def deco(fn): SLIDES[key] = (kicker, headline, fn); return fn
    return deco


@slide('heard', 'WHAT WE HEARD', 'Acebet wants leverage, redundancy and room to grow')
def heard(s):
    tiles = [('$25M', 'Monthly volume', 'as shared on our call'),
             ('~700K', 'Transactions a month', '$30 to $50 average ticket'),
             ('98%', 'US share of volume', 'Germany ramping; Canada, Australia, France and Spain next'),
             ('90s', 'Approval rate today', 'so the goal is allocation and resilience, not a rescue')]
    for i, (v, l, cap) in enumerate(tiles):
        x = X0 + (i % 2) * 160; y = 84 + (i // 2) * 106
        s.rect(x, y, 150, 96, fill=WHITE, outline=BORDER)
        s.text(x + 12, y + 10, 128, 30, v, size=24, color=BLUE)
        s.text(x + 12, y + 46, 128, 10, l.upper(), size=7, color=GREY, weight=600)
        s.text(x + 12, y + 60, 128, 26, cap, size=8.5, color=BODY, spacing=105)
    s.rect(364, 84, 320, 202, fill=PANEL)
    label(s, 378, 96, 'What the setup has to do')
    needs = ['Split volume across acquirers by set percentages',
             'Cascade and retry, with Apple Pay and Google Pay as most of the volume',
             'Add a new acquirer in weeks, not months',
             'Work for a non-US entity, starting with cross-border acquiring',
             'Hosted fields, so integration takes one to two weeks',
             'Reconciliation across providers without manual checks']
    for i, t in enumerate(needs):
        dot(s, 378, 114 + i * 27, t, size=9.5, w=290, h=24)
    band(s, 300, 46, '**Today:** Breeze live, Coinflow next, Whop for payouts, Checkout available.   '
                     '**Next:** more acquirers for leverage, including US high-risk acquiring, and local methods such as Interac in Canada.', size=9)


@slide('setup', 'HOW IT WORKS FOR ACEBET', 'One integration in front of every acquirer Acebet adds')
def setup(s):
    label(s, X0, 86, 'Acebet', color=GREY); label(s, 214, 86, 'Yuno', color=GREY); label(s, 534, 86, 'Acebet providers', color=GREY)
    left = [('Hosted fields', 'Cards, one PCI-light integration'), ('Apple Pay and Google Pay', 'Most of the volume today'),
            ('Redemptions and payouts', 'Same platform, same dashboard')]
    for i, (t, sub) in enumerate(left):
        y = 100 + i * 62
        s.rect(X0, y, 150, 50, fill=WHITE, outline=BORDER)
        s.text(X0 + 10, y + 9, 134, 12, t, size=9.5, color=INK, weight=600)
        s.text(X0 + 10, y + 26, 134, 10, sub, size=7.5, color=GREY)
        s.line(186, y + 25, 213, y + 25, color=BLUE, weight=1, arrow=True)
    s.rect(214, 100, 292, 174, fill=BLUE)
    s.text(228, 110, 260, 18, 'Yuno', size=14, color=WHITE, weight=600)
    s.text(228, 129, 260, 10, 'One API, one dashboard, every acquirer', size=8, color=LAV)
    mods = ['Volume split by percentage', 'Cascading and retries', 'Routing rules by BIN, method, amount', 'Monitors and auto-failover',
            'Reconciliation across providers', 'Approval and cost by provider']
    for i, m in enumerate(mods):
        x = 228 + (i % 2) * 134; y = 150 + (i // 2) * 38
        s.pill(x, y, 128, 30, m, fill=WHITE, color=DEEP, size=7.5)
    right = [('Breeze', 'Merchant of record'), ('Coinflow', 'Merchant of record'), ('Checkout.com', 'Acquirer'),
             ('Whop', 'Payouts'), ('US acquirers', 'Introductions underway'), ('EU cross-border', 'Germany, France, Spain')]
    for i, (t, sub) in enumerate(right):
        y = 100 + i * 29
        s.line(506, y + 12, 533, y + 12, color=BLUE, weight=1, arrow=True)
        s.rect(534, y, 150, 24, fill=PANEL)
        s.text(544, y, 70, 24, t, size=8.5, color=INK, weight=600, valign='MIDDLE')
        s.text(610, y, 68, 24, sub, size=6.5, color=GREY, valign='MIDDLE', align='END')
    band(s, 292, 40, '**Yuno never holds the money.** Funds settle from each provider straight to Acebet; Yuno routes, retries, monitors and reconciles.', size=9.5)
    source(s, 'Provider roles as described by Acebet on the call of 27 Oct 2026.')


@slide('price', 'PROPOSAL', f'Platform fee plus usage: about {V/TX*100:.1f} cents today, {RATES[-1]*100:g} cents above 1M')
def price(s):
    # left: tranches
    s.rect(X0, 84, 250, 276, fill=PANEL)
    label(s, 48, 96, 'Rate per successful transaction')
    s.text(48, 110, 226, 22, 'Each tranche is billed at its own rate within the month. Declines cost nothing; a retried or cascaded payment counts once.',
           size=7.5, color=BODY, spacing=108)
    for i in range(4):
        y = 142 + i * 44
        s.rect(48, y, 226, 0.5, fill=LINE)
        s.text(48, y + 8, 120, 9, f'TRANCHE {i+1}', size=6.5, color=GREY, weight=600)
        s.text(48, y + 19, 130, 14, rng(i), size=10.5, color=INK, weight=600)
        s.text(170, y + 6, 104, 30, f'**{c3(RATES[i])}** /trx', size=10, color=GREY, align='END', valign='MIDDLE', bold_color=BLUE)
    s.rect(48, 318, 226, 30, fill=WHITE)
    s.text(56, 318, 212, 30, f'Every transaction above {CUTS[2]:,} a month is billed at {c3(RATES[3])} as Acebet adds markets.', size=7.5, color=BODY, valign='MIDDLE')
    # middle: what it means today
    s.rect(298, 84, 214, 276, fill=WHITE, outline=BORDER)
    label(s, 310, 96, 'What it means today')
    s.text(310, 108, 190, 10, f'At about {TX:,} successful transactions a month', size=7.5, color=GREY)
    rows = [(f'Tranche {i+1}: {n:,} at {c3(r)}', f'${m:,.0f}') for i, (n, r, m) in enumerate(b) if n]
    y = 128
    for t, m in rows:
        s.text(310, y, 140, 12, t, size=8.5, color=INK); s.text(440, y, 60, 12, m, size=8.5, color=INK, align='END'); y += 17
    s.rect(310, y + 2, 190, 0.5, fill=LINE)
    s.text(310, y + 8, 140, 12, 'Transactions', size=8.5, color=INK, weight=600); s.text(440, y + 8, 60, 12, f'${V:,.0f}', size=8.5, color=INK, weight=600, align='END')
    s.text(310, y + 25, 140, 12, 'Platform fee', size=8.5, color=INK); s.text(440, y + 25, 60, 12, f'${PLATFORM:,}', size=8.5, color=INK, align='END')
    s.rect(306, y + 44, 198, 24, fill=PANEL)
    s.text(314, y + 44, 120, 24, 'Total a month', size=9, color=DEEP, weight=600, valign='MIDDLE')
    s.text(420, y + 44, 78, 24, f'${TOT:,.0f}', size=10, color=DEEP, weight=700, align='END', valign='MIDDLE')
    s.text(310, y + 76, 190, 10, f'${TOT*12:,.0f} a year', size=7.5, color=GREY)
    s.text(310, 282, 190, 30, c3(V / TX), size=26, color=BLUE)
    s.text(310, 316, 190, 30, f'average per successful transaction before the platform fee; {c3(TOT/TX)} all-in.', size=7.5, color=BODY, spacing=108)
    # right: growth
    s.rect(524, 84, 160, 276, fill=BLUE)
    s.text(536, 96, 140, 9, 'AS ACEBET GROWS', size=7, color=WHITE, weight=600)
    s.text(536, 108, 140, 20, 'Average rate per transaction, before the platform fee', size=7.5, color=LAV, spacing=105)
    for i, t in enumerate(GROWTH):
        y = 140 + i * 50
        s.rect(536, y - 4, 136, 0.5, fill=LAV)
        s.text(536, y + 2, 80, 12, f'{t:,}' + (' today' if i == 0 else ''), size=8, color=LAV)
        s.text(536, y + 16, 80, 20, c3(var(t) / t), size=15, color=WHITE, weight=600)
        s.text(600, y + 16, 72, 20, f'${var(t):,.0f}/mo', size=7.5, color=LAV, align='END', valign='MIDDLE')
    source(s, 'Illustrative volumes above today are not forecasts. Pricing valid for 30 days; subject to final agreement.')


@slide('terms', "WHAT'S INCLUDED", 'Every acquirer Acebet adds is a routing change, not a new fee')
def terms(s):
    s.rect(X0, 84, 312, 190, fill=WHITE, outline=BORDER)
    label(s, 48, 96, 'Included in the platform fee')
    inc = ['Orchestration and rules engine', 'Volume split, cascading and retries', 'Monitors and auto-failover',
           'Hosted fields, SDKs and sandbox', 'New provider connections, maintained by Yuno', 'Dashboard, approval and cost insights',
           'Dedicated team: account manager, technical account manager, solutions engineer']
    for i, t in enumerate(inc):
        dot(s, 48, 114 + i * 22, t, size=9, w=280, h=20)
    s.rect(360, 84, 324, 190, fill=PANEL)
    label(s, 372, 96, 'Commercial terms')
    terms_ = [('Platform fee', f'${PLATFORM:,} / month flat'), ('Usage', 'Four tranches per successful transaction'),
              ('Setup fee', 'None'), ('Retries and cascades', 'Billed once, only when approved'), ('Review', 'Rates locked, tranches reviewed annually')]
    for i, (k, v) in enumerate(terms_):
        y = 116 + i * 30
        s.rect(372, y - 4, 300, 0.5, fill=LINE)
        s.text(372, y + 2, 120, 14, k, size=9, color=GREY)
        s.text(482, y + 2, 190, 14, v, size=9, color=INK, weight=600, align='END')
    for i, (t, body) in enumerate([('PAYOUTS', 'Redemptions and payouts on the same platform, routed across providers from one integration.'),
                                   ('RECONCILIATION', 'One reconciliation view across Breeze, Coinflow, Whop and Checkout instead of one process per provider.')]):
        x = X0 + i * 330
        s.rect(x, 290, 318, 62, fill=WHITE, outline=BORDER); s.rect(x, 290, 2, 62, fill=BLUE)
        s.text(x + 14, 298, 150, 10, t, size=7.5, color=INK, weight=600)
        s.pill(x + 226, 296, 80, 14, 'PENDING REVIEW', fill=PILL, color=BLUE, size=6)
        s.text(x + 14, 314, 290, 32, body + ' **Not included** in the totals.', size=8, color=BODY, spacing=108)


@slide('next', 'NEXT STEPS', 'From proposal to live traffic, at the pace Acebet sets')
def nxt(s):
    steps = [('01', 'THIS WEEK', 'Proposal and API review', 'Sandbox access for the development team; API docs and hosted fields.'),
             ('02', 'AGREEMENT', 'Connect current providers', 'Breeze and Coinflow behind one integration; split and cascading rules set with our solutions team.'),
             ('03', 'GO LIVE', 'Integrate hosted fields', 'One to two weeks of work on Acebet\'s side, then traffic moves by rule.'),
             ('04', 'SCALE', 'Add acquirers', 'US acquiring introductions and cross-border acquiring for new markets.')]
    s.rect(X0, 86, W0, 170, fill=PANEL)
    cw = 148
    for i, (n, k, t, body) in enumerate(steps):
        x = 50 + i * (cw + 10)
        s.rect(x, 100, cw, 142, fill=WHITE, outline=BORDER)
        s.text(x + 12, 112, 124, 10, f'{n}  ·  {k}', size=7.5, color=BLUE, weight=600)
        s.text(x + 12, 130, 124, 30, t, size=11.5, color=INK, weight=600, spacing=105)
        s.text(x + 12, 168, 124, 66, body, size=8.5, color=BODY, spacing=112)
    s.rect(X0, 272, W0, 56, fill=BLUE)
    s.text(X0 + 16, 272, 300, 56, "**Let's grow together**", size=14, color=WHITE, valign='MIDDLE')
    s.text(330, 272, 340, 56, 'German Tatis  ·  Senior Account Executive\ngerman.tatis@y.uno  ·  +1 786 238 4554  ·  y.uno',
           size=9, color=WHITE, align='END', valign='MIDDLE', spacing=120)


# ---------------------------------------------------------------------------- plumbing
def els(pres, sid):
    return next(sl for sl in pres['slides'] if sl['objectId'] == sid)['pageElements']


def txt(e):
    return ''.join(x.get('textRun', {}).get('content', '') for x in e.get('shape', {}).get('text', {}).get('textElements', [])).strip()


def new_slide(pres, key, page_no):
    kicker, headline, fn = SLIDES[key]
    page = nid('pg'); ids = {CHROME: page}; reqs = []; keep = {}
    texts = []
    for e in els(pres, CHROME):
        n = nid('c'); ids[e['objectId']] = n
        if not e['objectId'].startswith('c_'): reqs.append(('del', n))
        elif txt(e): texts.append((e, n))
    # chrome texts: kicker (upper case), page number (digits), headline (the rest)
    for e, n in texts:
        t = txt(e)
        keep['page' if t.isdigit() else 'kicker' if t.isupper() else 'headline'] = n
    out = [{'duplicateObject': {'objectId': CHROME, 'objectIds': ids}}] + [{'deleteObject': {'objectId': n}} for _, n in reqs]
    s = Slide(page)
    s.set_text(keep['kicker'], kicker); s.set_text(keep['headline'], headline); s.set_text(keep['page'], str(page_no))
    fn(s)
    return page, out + s.reqs


def build(dry):
    svc = service(); pres = svc.presentations().get(presentationId=PID).execute()
    json.dump(pres, open(f'{WORK}/before.json', 'w'))
    have = [sl['objectId'] for sl in pres['slides']]
    print('deck:', pres['properties']['title'] if 'properties' in pres else pres.get('title'), '| slides:', len(have))
    print('missing house slides:', [k for k, v in HOUSE.items() if v not in have], '| chrome:', CHROME in have)
    pages, reqs = {}, []
    for key in SLIDES:
        p, r = new_slide(pres, key, ORDER.index(key) + 1); pages[key] = p; reqs += r
    # cover
    c = Slide(COVER)
    c.set_text('n01_g3f77215683c_1_527', 'Acebet + Yuno')
    c.set_text('n01_e001', 'One orchestration layer across every acquirer  ·  Proposal')
    c.set_text('n01_e002', 'Yuno  ·  October 2026')
    reqs += c.reqs
    # house slides: page numbers (any element whose whole text is a number)
    for key, sid in HOUSE.items():
        if key == 'cover': continue
        for e in els(pres, sid):
            if txt(e).isdigit() and e.get('transform', {}).get('translateY', 0) / PT > 360:   # page number only, not step labels
                x = Slide(sid); x.set_text(e['objectId'], str(ORDER.index(key) + 1)); reqs += x.reqs
    final = [HOUSE.get(k) or pages[k] for k in ORDER]
    reqs += [{'deleteObject': {'objectId': sid}} for sid in have if sid not in final]
    reqs += [{'updateSlidesPosition': {'slideObjectIds': [sid], 'insertionIndex': i}} for i, sid in enumerate(final)]
    print('requests:', len(reqs))
    if dry: print('dry run, nothing changed'); return
    svc.presentations().batchUpdate(presentationId=PID, body={'requests': reqs}).execute()
    json.dump({'pages': pages, 'final': final}, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'v2_state.json'), 'w'), indent=1)
    import urllib.request
    Q = svc.presentations().get(presentationId=PID).execute()
    for n, sl in enumerate(Q['slides'], 1):
        r = svc.presentations().pages().getThumbnail(presentationId=PID, pageObjectId=sl['objectId'], thumbnailProperties_thumbnailSize='LARGE').execute()
        urllib.request.urlretrieve(r['contentUrl'], f'{WORK}/v2_{n:02d}.png')
    print('built', len(Q['slides']), 'slides; thumbs in', WORK)


if __name__ == '__main__':
    build('dry' in sys.argv)
