# -*- coding: utf-8 -*-
"""build.py · Yuno general deck (12 slides) in the OnlyFans deck look.

  python3 build.py build            # build every new slide (appended), record ids in state.json
  python3 build.py build s05 s06    # rebuild those slides in place
  python3 build.py finalize         # cover + house slides edited, final order set, OnlyFans slides deleted
"""
import sys, json, os, time
from gsl import *

PID = '16v9fmx94bVCvWEtSgM56Lz3s-9nsWZaf6kHWWKIdF54'
HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, 'state.json')

CHROME = 'h7c266de662ba1cf0_9_611'   # "trusted by" slide: bg, kicker, headline, bar, page number, wordmark
CH_KEEP = {'h7c266de662ba1cf0_9_612': 'bg', 'h7c266de662ba1cf0_9_613': 'kicker', 'h7c266de662ba1cf0_9_614': 'headline',
           'imbar_14': 'bar', 'impg_14': 'page', 'imlg_14': 'logo'}
COVER = 'n01_g3f77215683c_1_445'
PROVEN = 'h6032acb876a0077a_1_0'     # "Today, Yuno is proven global payment infrastructure"
TRUSTED = CHROME

ORDER = ['cover', 's02', 's03', 's04', 's05', 's06', 's07', 's08', 'proven', 's10', 'trusted', 's12']
X0, W0, R = 36, 648, 684


def load_state():
    return json.load(open(STATE)) if os.path.exists(STATE) else {}


def save_state(st):
    json.dump(st, open(STATE, 'w'), indent=1)


def band(s, y, h, txt, size=9.5):
    s.rect(X0, y, W0, h, fill=PANEL)
    s.rect(X0, y, 2, h, fill=BLUE)
    s.text(X0 + 14, y, W0 - 24, h, txt, size=size, color=INK, valign='MIDDLE', bold_color=DEEP)


def source(s, txt):
    s.text(X0, 372, 560, 9, txt, size=6.5, color=GREY)


def label(s, x, y, txt, color=BLUE, w=200):
    s.text(x, y, w, 9, txt.upper(), size=7, color=color, weight=600)


# ====================================================================== slides
SLIDES = {}


def slide(key, kicker, headline):
    def deco(fn):
        SLIDES[key] = (kicker, headline, fn); return fn
    return deco


@slide('s02', 'WHO WE ARE', 'One operating system for every provider, rail and market you sell in')
def s02(s):
    label(s, X0, 88, 'What Yuno is')
    s.text(X0, 103, 290, 120, 'Yuno is an **AI native operating system** for global financial infrastructure. Companies connect once and '
           'orchestrate payment methods, processors, antifraud tools, KYC and KYB providers, reconciliation and stablecoins from one platform.',
           size=12.5, color=INK, spacing=112, bold_color=BLUE)
    label(s, X0, 218, 'What it changes')
    for i, t in enumerate(['Lower processing costs and higher approval rates',
                           'New markets and methods without new integrations',
                           'One view of every payment, provider and payout']):
        s.check(X0, 234 + i * 20, t, size=9.5, w=270)
    tiles = [('Up to 7%', 'Approval uplift', 'more payments approved through smart routing and retries'),
             ('30%', 'Recovered revenue', 'won back from payments that failed the first time'),
             ('27%', 'Lower payment costs', 'saved on payment processing costs'),
             ('90%', 'Less development time', 'to add a provider, a method or a market')]
    for i, (v, l, c) in enumerate(tiles):
        x = 352 + (i % 2) * 171; y = 88 + (i // 2) * 106
        s.rect(x, y, 161, 96, fill=WHITE, outline=BORDER)
        s.text(x + 12, y + 10, 140, 30, v, size=24, color=BLUE, weight=400)
        s.text(x + 12, y + 46, 140, 10, l.upper(), size=7, color=GREY, weight=600)
        s.text(x + 12, y + 60, 140, 26, c, size=8.5, color=BODY, spacing=105)
    band(s, 310, 34, '**1,000+** payment methods, PSPs and fraud solutions      **190+** countries      **180+** currencies      **One** API and one dashboard', size=10)
    source(s, 'Published figures, y.uno, read 16 Oct 2026. Results vary by merchant, market and payment mix.')


@slide('s03', 'THE PROBLEM', 'Payments are fragmented: every provider is a new integration')
def s03(s):
    # left card: without a neutral layer
    s.rect(X0, 84, 300, 272, fill=WHITE, outline=BORDER)
    s.text(48, 94, 200, 9, 'WITHOUT A NEUTRAL LAYER', size=7, color=GREY, weight=600)
    s.text(48, 106, 270, 16, 'One integration per provider', size=13, color=INK, weight=600)
    s.rect(50, 168, 76, 44, fill=PANEL)
    s.text(50, 168, 76, 44, 'Your business', size=9, color=INK, weight=600, align='CENTER', valign='MIDDLE')
    provs = ['Acquirer A', 'Acquirer B', 'Local methods', 'Fraud tool', 'Payout provider', 'Bank']
    for i, p in enumerate(provs):
        y = 134 + i * 19
        s.line(126, 190, 214, y + 7.5, color=LINE, weight=0.75)
        s.rect(214, y, 108, 15, fill=WHITE, outline=BORDER, kind='ROUND_RECTANGLE')
        s.text(214, y, 108, 15, p, size=7.5, color=INK, align='CENTER', valign='MIDDLE')
    for i, t in enumerate(['A new contract, API and report for each provider',
                           'A decline at one provider is a lost sale',
                           'Every new market is an engineering project']):
        s.check(48, 260 + i * 20, t, size=9, w=260, ok=False)
    s.text(48, 326, 276, 22, 'Every provider brings its own API, dashboard and settlement file.', size=7.5, color=GREY)
    # arrow
    s.rect(343, 207, 24, 24, fill=BLUE, kind='ELLIPSE')
    s.text(343, 207, 24, 24, '→', size=12, color=WHITE, weight=600, align='CENTER', valign='MIDDLE')
    # right card: with Yuno
    s.rect(374, 84, 310, 272, fill=PANEL, outline=BLUE, weight=1)
    s.text(386, 94, 200, 9, 'WITH YUNO', size=7, color=BLUE, weight=600)
    s.text(386, 106, 280, 16, 'One integration, every provider', size=13, color=INK, weight=600)
    s.rect(388, 134, 282, 22, fill=WHITE, outline=BORDER)
    s.text(388, 134, 282, 22, 'Your business  ·  one API', size=8.5, color=INK, weight=600, align='CENTER', valign='MIDDLE')
    s.line(529, 156, 529, 168, color=BLUE, weight=1, arrow=True)
    s.rect(388, 168, 282, 34, fill=BLUE)
    s.text(398, 168, 80, 34, 'Yuno', size=12, color=WHITE, weight=600, valign='MIDDLE')
    s.text(470, 168, 192, 34, 'routing · vault · risk · reconciliation', size=8, color=WHITE, align='END', valign='MIDDLE')
    chips = ['Acquirers', 'Local methods', 'Fraud and KYC', 'Banks']
    for i, c in enumerate(chips):
        x = 388 + i * 72
        s.line(x + 33, 202, x + 33, 220, color=BLUE, weight=0.75)
        s.pill(x, 220, 66, 18, c, fill=WHITE, color=BLUE, size=7, outline=BORDER)
    for i, t in enumerate(['One API opens 1,000+ methods, PSPs and fraud tools',
                           'A declined payment is retried on another route',
                           'New providers and markets switch on as configuration']):
        s.check(388, 260 + i * 20, t, size=9, w=262)
    s.text(388, 326, 280, 22, 'Same providers, one layer on top: nothing to rebuild when you add the next one.', size=7.5, color=GREY)


@slide('s04', 'HOW IT WORKS', 'One API between your business and the whole payments ecosystem')
def s04(s):
    label(s, X0, 86, 'Your business', color=GREY)
    label(s, 214, 86, 'Yuno', color=GREY)
    label(s, 534, 86, 'Your providers', color=GREY)
    left = [('Web and app checkout', 'SDKs for web, iOS and Android'), ('Subscriptions', 'Recurring billing and renewals'),
            ('Marketplaces and payouts', 'Sellers, drivers, creators'), ('AI agents', 'Agentic commerce on your rules')]
    for i, (t, sub) in enumerate(left):
        y = 100 + i * 48
        s.rect(X0, y, 150, 40, fill=WHITE, outline=BORDER)
        s.text(X0 + 10, y + 6, 134, 12, t, size=9, color=INK, weight=600)
        s.text(X0 + 10, y + 21, 134, 10, sub, size=7.5, color=GREY)
        s.line(186, y + 20, 213, y + 20, color=BLUE, weight=1, arrow=True)
    s.rect(214, 100, 292, 184, fill=BLUE)
    s.text(228, 110, 260, 18, 'Yuno', size=14, color=WHITE, weight=600)
    s.text(228, 129, 260, 10, 'One API, one dashboard, every provider', size=8, color=LAV)
    mods = ['Checkout and SDKs', 'Smart routing and retries', 'Vault and network tokens', '3DS and risk conditions',
            'Payouts', 'Subscriptions', 'Reconciliation and insights', 'Payments Concierge (AI)']
    for i, m in enumerate(mods):
        x = 228 + (i % 2) * 134; y = 150 + (i // 2) * 32
        s.pill(x, y, 128, 26, m, fill=WHITE, color=DEEP, size=7.5)
    right = ['Acquirers and PSPs', 'Local methods and wallets', 'Fraud and 3DS providers', 'KYC and KYB', 'Banks and payout rails', 'Stablecoin providers']
    for i, t in enumerate(right):
        y = 100 + i * 31
        s.line(506, y + 13, 533, y + 13, color=BLUE, weight=1, arrow=True)
        s.rect(534, y, 150, 26, fill=PANEL)
        s.text(544, y, 136, 26, t, size=8.5, color=INK, weight=600, valign='MIDDLE')
    band(s, 302, 40, '**Yuno never holds the money.** Funds settle from your providers straight to your accounts; Yuno connects, decides, secures and reconciles.', size=9.5)


@slide('s05', 'THE PLATFORM', 'A complete suite in four pillars, switched on as configuration')
def s05(s):
    pillars = [
        ('01', 'Orchestration', 'Route and recover', [
            ('Smart routing', 'Each payment to the provider most likely to approve it'),
            ('Failover and retries', 'A decline or outage takes a second route on its own'),
            ('Payins and payouts', 'Collect and pay out from the same integration'),
            ('Stablecoins', 'Accept and pay out in stablecoins on the same API')]),
        ('02', 'Checkout and SDKs', 'Convert everywhere', [
            ('Customizable checkout', 'Local methods shown natively in each country'),
            ('Web and mobile SDKs', 'One interface for web, iOS and Android'),
            ('Subscriptions', 'Plans, trials and smart retries on renewals'),
            ('Agentic commerce', 'AI agents pay within the limits you set')]),
        ('03', 'Security and risk', 'Protect every payment', [
            ('Vault and tokenization', 'PCI DSS Level 1, tokens portable across processors'),
            ('3DS', 'Native or external, applied where it helps'),
            ('Network tokens', 'Plus Account Updater, so stored cards stay current'),
            ('Risk and chargebacks', 'Risk conditions, fraud tools, chargeback management')]),
        ('04', 'AI and intelligence', 'The brain', [
            ('Analytics and insights', 'Approval, cost and fees by provider and market'),
            ('Reconciliation', 'Transactions matched to settlements across providers'),
            ('Payments Concierge', 'An AI agent for your payments operations'),
            ('Monitors', 'Provider health watched live, traffic moved on drops')]),
    ]
    cw, gap = 153, 12
    for i, (num, name, tag, items) in enumerate(pillars):
        x = X0 + i * (cw + gap)
        hl = i == 0
        s.rect(x, 84, cw, 218, fill=WHITE, outline=BORDER)
        s.text(x + 12, 94, 40, 10, num, size=8.5, color='#7C89EF')
        s.text(x + 12, 106, cw - 24, 14, name, size=11, color=INK, weight=600)
        s.text(x + 12, 122, cw - 24, 10, tag, size=8, color=BLUE)
        s.rect(x + 12, 139, cw - 24, 0.5, fill=BORDER)
        for j, (t, d) in enumerate(items):
            y = 147 + j * 38
            s.text(x + 12, y, cw - 24, 11, t, size=8.5, color=INK, weight=600)
            s.text(x + 12, y + 12, cw - 24, 22, d, size=7.5, color=GREY, spacing=105)
    # certifications
    s.text(X0, 318, 80, 16, 'CERTIFIED', size=7, color=GREY, weight=600, valign='MIDDLE')
    certs = [('PCI DSS Level 1', 78), ('SOC 2 Type 2', 66), ('ISO 27001', 56), ('ISO 27701', 56), ('GDPR', 40), ('Visa Service Provider', 98)]
    x = 96
    for c, w in certs:
        s.pill(x, 318, w, 16, c, fill=WHITE, color=BLUE, size=7, outline=BORDER)
        x += w + 6
    source(s, 'Product list and certifications as published on y.uno, read 16 Oct 2026.')


@slide('s06', 'SMART ROUTING', 'Every payment takes its best path, and a failure takes a second one')
def s06(s):
    top = 100
    s.pill(X0, top, 62, 13, 'ILLUSTRATIVE', fill=PILL, color=GREY, size=6.5)
    # payment
    s.rect(X0, top + 46, 92, 60, fill=WHITE, outline=BORDER)
    s.text(X0 + 10, top + 53, 76, 9, 'PAYMENT', size=6.5, color=GREY, weight=600)
    s.text(X0 + 10, top + 65, 76, 13, '$49.00 · card', size=10, color=INK, weight=600)
    s.text(X0 + 10, top + 81, 76, 18, 'Brazil · debit · first try', size=7.5, color=GREY)
    s.line(128, top + 76, 147, top + 76, color=BLUE, weight=1, arrow=True)
    # engine
    s.rect(148, top + 34, 118, 84, fill=BLUE)
    s.text(158, top + 42, 100, 14, 'Routing engine', size=11, color=WHITE, weight=600)
    s.text(158, top + 59, 100, 10, 'Rules you set, or AI', size=7.5, color=LAV)
    s.text(158, top + 78, 100, 30, 'BIN, country, amount, method, cost, provider health', size=7.5, color=WHITE, spacing=110)
    provs = [('Provider A', 'DECLINED', '#FBE9E7', RED, '1'), ('Provider B', 'APPROVED', '#E2F3EB', GREEN, '2'), ('Provider C', 'STANDBY', PILL, GREY, '')]
    for i, (p, st, f, col, n) in enumerate(provs):
        y = top + 6 + i * 50
        s.line(266, top + 76, 318, y + 20, color=BLUE if n else LINE, weight=1 if n else 0.75, arrow=True, dash=None if n else 'DASH')
        s.rect(318, y, 132, 40, fill=WHITE, outline=BORDER)
        s.text(328, y, 70, 40, p, size=9, color=INK, weight=600, valign='MIDDLE')
        s.pill(388, y + 12, 54, 16, st, fill=f, color=col, size=6.5)
        if n:
            mx, my = 292, (top + 76 + y + 20) / 2
            s.rect(mx - 7, my - 7, 14, 14, fill=WHITE, outline=BLUE, kind='ELLIPSE')
            s.text(mx - 7, my - 7, 14, 14, n, size=7, color=BLUE, weight=600, align='CENTER', valign='MIDDLE')
    steps = [('1', 'The first route declines, or the provider is down'),
             ('2', 'Yuno sends the payment to the next best route'),
             ('3', 'The customer sees one approved payment')]
    for i, (n, t) in enumerate(steps):
        x = X0 + i * 140
        s.rect(x, 268, 132, 52, fill=PANEL)
        s.text(x + 10, 274, 20, 14, n, size=11, color=BLUE, weight=600)
        s.text(x + 10, 290, 114, 26, t, size=8, color=INK, spacing=105)
    # right column
    s.rect(470, 84, 214, 236, fill=PANEL)
    s.text(482, 94, 190, 9, 'WHAT IT DELIVERS', size=7, color=BLUE, weight=600)
    s.text(482, 108, 190, 28, 'Up to 7%', size=24, color=BLUE)
    s.text(482, 140, 190, 10, 'approval uplift', size=8.5, color=BODY)
    s.text(482, 158, 190, 28, '30%', size=24, color=BLUE)
    s.text(482, 190, 190, 10, 'recovered revenue', size=8.5, color=BODY)
    s.rect(482, 210, 190, 0.5, fill=BORDER)
    for i, t in enumerate(['Rules by BIN, country, amount, method', 'Volume splits to test providers', 'Cascades through retryable declines', 'Monitors move traffic when a provider drops']):
        s.check(482, 220 + i * 22, t, size=8.5, w=170)
    source(s, 'Illustrative flow. Uplift and recovery are Yuno published figures (y.uno, read 16 Oct 2026); results vary by merchant.')


@slide('s07', 'START ANYWHERE', 'Start with one product, add the rest as a switch')
def s07(s):
    cards = [
        ('01', 'Subscriptions', True, 'Plans, trials and pricing by country, with smart retries on every renewal. A declined renewal is retried on another route.'),
        ('02', 'Vault and tokenization', True, 'A PCI DSS Level 1 vault for cards and sensitive data. Tokens work on every processor you connect, with network tokens and Account Updater.'),
        ('03', '3DS', True, 'Native 3DS or your current provider, applied by rule where it protects the payment and skipped where it only adds friction.'),
        ('04', 'Reconciliation', True, 'Settlement reports from every provider matched to your transactions, so finance sees what actually arrived.'),
        ('05', 'Payouts', False, 'Pay sellers, drivers, creators and suppliers across countries from the same integration you collect with.'),
        ('06', 'Fraud and risk', False, 'Risk conditions inside the routing, the fraud tools you choose, and chargeback management in one place.'),
    ]
    cw, ch, gap = 208, 104, 12
    for i, (n, t, alone, body) in enumerate(cards):
        x = X0 + (i % 3) * (cw + gap); y = 84 + (i // 3) * (ch + 10)
        s.rect(x, y, cw, ch, fill=WHITE, outline=BORDER)
        s.text(x + 12, y + 11, 30, 10, n, size=8.5, color='#7C89EF')
        if alone:
            s.pill(x + cw - 84, y + 9, 72, 14, 'RUNS STANDALONE', fill=PILL, color=BLUE, size=6)
        s.text(x + 12, y + 28, cw - 24, 15, t, size=12, color=INK, weight=600)
        s.text(x + 12, y + 50, cw - 24, 60, body, size=8.5, color=BODY, spacing=112)
    band(s, 316, 34, '**Standalone** modules run on top of the providers you already have. Every module also runs inside the full platform, on one API and one dashboard.', size=9)


@slide('s08', "WHAT'S NEW", 'AI, agentic commerce, stablecoins and banking on one connection')
def s08(s):
    cards = [
        ('Payments Concierge', 'An AI agent for payments teams. It watches approvals and providers, explains what changed in plain language and helps route, retry and recover transactions.', 'Payments and operations teams'),
        ('Agentic commerce', 'When AI agents buy on behalf of your customers, you set spend limits and approvals. The platform enforces and records each one.', 'Merchants selling to AI agents'),
        ('Stablecoins', 'Accept and pay out in stablecoins alongside cards and local methods, through the same API and the same dashboard.', 'Cross-border pay-ins and payouts'),
        ('Banking connectivity', 'Direct connections to the banks you work with for accounts, balances and transfers, on the same layer as payments.', 'Treasury and finance teams'),
    ]
    cw, gap = 153, 12
    for i, (t, body, who) in enumerate(cards):
        x = X0 + i * (cw + gap)
        s.rect(x, 84, cw, 196, fill=WHITE, outline=BORDER)
        s.rect(x, 84, cw, 3, fill=BLUE)
        s.pill(x + 12, 98, 34, 14, 'NEW', fill=BLUE, color=WHITE, size=6.5)
        s.text(x + 12, 120, cw - 24, 16, t, size=12, color=INK, weight=600)
        s.text(x + 12, 144, cw - 24, 90, body, size=8.5, color=BODY, spacing=115)
        s.rect(x + 12, 244, cw - 24, 0.5, fill=BORDER)
        s.text(x + 12, 250, cw - 24, 9, 'BUILT FOR', size=6.5, color=GREY, weight=600)
        s.text(x + 12, 261, cw - 24, 11, who, size=8, color=BLUE, weight=600)
    s.rect(X0, 296, W0, 36, fill=WHITE, outline=BLUE, dash='DASH')
    s.pill(X0 + 12, 306, 40, 16, 'NEXT', fill=PILL, color=BLUE, size=7)
    s.text(X0 + 62, 296, 560, 36, '**Identity:** KYC and KYB on the same connection, next to payments, risk and banking.', size=9.5, color=INK, valign='MIDDLE', bold_color=DEEP)


@slide('s10', 'PROVEN IN PRODUCTION', 'Higher approvals and faster launches, measured in production')
def s10(s):
    cases = [('inDrive', '~90%', 'payment approval rate, with new countries live in under eight months'),
             ('Livelo', '50%', 'of failed transactions recovered, and approval rates up 5%'),
             ('Vibra', '80%', 'approval rate for new users, up more than 30 points'),
             ('Reserva', '+4%', 'improvement in payment approval rates with Smart Routing'),
             ('Rappi', 'Zero', 'implementation time for new providers; issue response from minutes to seconds'),
             ("McDonald's", '21', 'countries unified on one payments layer')]
    cw, ch, gap = 208, 128, 12
    for i, (name, v, cap) in enumerate(cases):
        x = X0 + (i % 3) * (cw + gap); y = 84 + (i // 3) * (ch + 10)
        s.rect(x, y, cw, ch, fill=WHITE, outline=BORDER)
        s.text(x + 12, y + 12, cw - 24, 13, name, size=10.5, color=INK, weight=600)
        s.rect(x + 12, y + 32, cw - 24, 0.5, fill=BORDER)
        s.text(x + 12, y + 42, cw - 24, 34, v, size=28, color=BLUE)
        s.text(x + 12, y + 84, cw - 24, 32, cap, size=8.5, color=BODY, spacing=110)
    source(s, 'Yuno success stories as published on y.uno/success-stories, read 16 Oct 2026.')


@slide('s12', 'HOW WE START', 'Tell us where your stack hurts most; we prove it on one flow')
def s12(s):
    steps = [('01', 'MAP', 'Your current stack', 'Providers, markets and methods, and where approvals or costs slip today.'),
             ('02', 'PICK', 'One pain to solve first', 'Approval rate, processing cost, reconciliation or a new market.'),
             ('03', 'PROVE', 'A focused pilot', 'One flow and clear metrics. Nothing migrates until the numbers say so.')]
    s.rect(X0, 90, W0, 158, fill=PANEL)
    cw = 190
    for i, (n, k, t, b) in enumerate(steps):
        x = 54 + i * (cw + 23)
        s.rect(x, 106, cw, 126, fill=WHITE, outline=BORDER)
        s.text(x + 14, 120, 120, 10, f'{n}  ·  {k}', size=8, color=BLUE, weight=600)
        s.text(x + 14, 138, cw - 28, 16, t, size=13, color=INK, weight=600)
        s.text(x + 14, 164, cw - 28, 60, b, size=9, color=BODY, spacing=115)
        if i < 2:
            s.line(x + cw + 3, 169, x + cw + 20, 169, color=BLUE, weight=1.25, arrow=True)
    s.rect(X0, 266, W0, 56, fill=BLUE)
    s.text(X0 + 16, 266, 300, 56, "**Let's grow together**", size=14, color=WHITE, valign='MIDDLE')
    s.text(330, 266, 340, 56, 'German Tatis  ·  Business Development Manager\ngerman.tatis@y.uno  ·  +1 786 238 4554  ·  y.uno', size=9, color=WHITE, align='END', valign='MIDDLE', spacing=120)


# ====================================================================== build plumbing
def chrome_ids(pres):
    for sl in pres['slides']:
        if sl['objectId'] == CHROME:
            return [e['objectId'] for e in sl['pageElements']]
    raise SystemExit('chrome slide missing')


def build_one(svc, pres, key, st, page_no):
    kicker, headline, fn = SLIDES[key]
    old = st.get(key)
    new_page = nid('pg')
    ids = {CHROME: new_page}
    keep = {}
    for eid in chrome_ids(pres):
        n = nid('c'); ids[eid] = n
        if eid in CH_KEEP: keep[CH_KEEP[eid]] = n
    reqs = [{'duplicateObject': {'objectId': CHROME, 'objectIds': ids}}]
    for eid, n in ids.items():
        if eid != CHROME and eid not in CH_KEEP:
            reqs.append({'deleteObject': {'objectId': n}})
    s = Slide(new_page)
    s.set_text(keep['kicker'], kicker); s.style_all(keep['kicker'], 7, BLUE)
    s.set_text(keep['headline'], headline); s.style_all(keep['headline'], 19, INK)
    s.set_text(keep['page'], str(page_no))
    hl = next(e for sl in pres['slides'] if sl['objectId'] == CHROME for e in sl['pageElements'] if e['objectId'] == 'h7c266de662ba1cf0_9_614')
    t = dict(hl['transform']); t['scaleX'] = emu(600) / hl['size']['width']['magnitude']; t.setdefault('unit', 'EMU')
    s.reqs.append({'updatePageElementTransform': {'objectId': keep['headline'], 'applyMode': 'ABSOLUTE', 'transform': t}})
    fn(s)
    reqs += s.reqs
    svc.presentations().batchUpdate(presentationId=PID, body={'requests': reqs}).execute()
    if old:
        try:
            pres2 = svc.presentations().get(presentationId=PID, fields='slides.objectId').execute()
            pos = [x['objectId'] for x in pres2['slides']].index(old)
            svc.presentations().batchUpdate(presentationId=PID, body={'requests': [
                {'updateSlidesPosition': {'slideObjectIds': [new_page], 'insertionIndex': pos}},
                {'deleteObject': {'objectId': old}}]}).execute()
        except ValueError:
            pass
    else:
        n = len(svc.presentations().get(presentationId=PID, fields='slides.objectId').execute()['slides'])
        svc.presentations().batchUpdate(presentationId=PID, body={'requests': [
            {'updateSlidesPosition': {'slideObjectIds': [new_page], 'insertionIndex': n}}]}).execute()
    st[key] = new_page
    save_state(st)
    print('built', key, new_page, len(reqs), 'requests')


def finalize(svc):
    st = load_state()
    pres = svc.presentations().get(presentationId=PID).execute()
    by = {sl['objectId']: sl for sl in pres['slides']}
    reqs = []
    # cover
    cov = by[COVER]
    els = {e['objectId']: e for e in cov['pageElements']}
    for gid in ['n01_g3f77215683c_1_528', 'n01_g3f77215683c_1_530', 'n01_g3f77215683c_1_531']:
        reqs.append({'deleteObject': {'objectId': gid}})
    c = Slide(COVER)
    c.set_text('n01_g3f77215683c_1_527', 'Global payments, one platform')
    c.set_text('n01_e001', 'The AI native operating system for global financial infrastructure')
    c.set_text('n01_e002', 'Yuno  ·  October 2026')
    reqs += c.reqs
    # house slides: page numbers and kicker
    pg = {PROVEN: ('h6032acb876a0077a_1_19', 9), TRUSTED: ('impg_14', 11)}
    for sid, (eid, n) in pg.items():
        x = Slide(sid); x.set_text(eid, str(n)); reqs += x.reqs
    if not st.get('cover_done'):
        svc.presentations().batchUpdate(presentationId=PID, body={'requests': reqs}).execute()
        st['cover_done'] = True; save_state(st)
    # order and delete
    final = [COVER if k == 'cover' else PROVEN if k == 'proven' else TRUSTED if k == 'trusted' else st[k] for k in ORDER]
    reqs = [{'deleteObject': {'objectId': sl['objectId']}} for sl in pres['slides'] if sl['objectId'] not in final]
    reqs += [{'updateSlidesPosition': {'slideObjectIds': [sid], 'insertionIndex': i}} for i, sid in enumerate(final)]
    svc.presentations().batchUpdate(presentationId=PID, body={'requests': reqs}).execute()
    st['finalized'] = True; save_state(st)
    print('finalized', len(final), 'slides')


if __name__ == '__main__':
    svc = service()
    cmd = sys.argv[1]
    if cmd == 'build':
        st = load_state()
        keys = sys.argv[2:] or list(SLIDES)
        pres = svc.presentations().get(presentationId=PID).execute()
        for k in keys:
            build_one(svc, pres, k, st, ORDER.index(k) + 1)
            time.sleep(1)
    elif cmd == 'finalize':
        finalize(svc)
