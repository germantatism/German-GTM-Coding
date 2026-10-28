# -*- coding: utf-8 -*-
"""make_spec.py · builds deck_spec.json for the Carry1st LatAm Shop deck (content agent, 15 Oct 2026).

Logo chips come from research/connections_latam_from_adidas.json (y.uno vendor URLs, pulled 14 Oct 2026).
Numbers come from model/bc_numbers.md and model/model_numbers.json; market facts from research/latam_markets.md.
Run:  python3 make_spec.py  &&  python3 gs_engine.py check deck_spec.json
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
PID = '1-IdPVaPu5FE4P36ByuiQ2vupRFocujdFcmmQeuPI9kk'
CONN = json.load(open(os.path.join(HERE, 'research', 'connections_latam_from_adidas.json')))

# ---------------------------------------------------------------- logo lookup
PROV, METH = {}, {}
for _c, _v in CONN.items():
    for _s in _v['providers_slide']['sections']:
        for _ch in _s['chips']:
            (METH if 'method' in _s['header'].lower() else PROV).setdefault(_ch['name'], _ch)
    _ms = _v.get('methods_slide')
    if _ms:
        for _s in _ms['sections']:
            for _ch in _s['chips']: METH.setdefault(_ch['name'], _ch)

def chip(name, table=PROV):
    c = table.get(name) or PROV.get(name) or METH.get(name)
    if not c: raise SystemExit(f'no logo for {name}')
    return {'name': name, 'logo': c['logo'], 'aspect': c.get('aspect', 1.0)}

def live_chips(country):
    sec = CONN[country]['providers_slide']['sections'][0]
    assert sec['header'].startswith('Live through Yuno'), sec['header']
    return sec['header'], [chip(c['name']) for c in sec['chips']]

def method_chips(names): return [chip(n, METH) for n in names]

FLAG = lambda cc: f'https://flagcdn.com/w80/{cc}.png'
SECTIONS = ['01 Executive summary', '02 Where Carry1st stands', '03 Two ways to launch', '04 Why Yuno',
            '05 Business case', '06 Proposal', '07 Phase 2', 'Appendix: LatAm deep dive and sources']

def divider(id_, num, title, sub, notes):
    return {'id': id_, 'type': 'divider', 'num': num, 'title': title, 'sub': sub, 'section_list': SECTIONS, 'notes': notes}

def pending(id_, kicker, headline):
    """visible placeholder, replaced in place with --only <id> --replace once pricing v3 is confirmed"""
    return {'id': id_, 'type': 'cards_row', 'kicker': kicker, 'headline': headline,
            'cards': [{'eyebrow': 'PENDING', 'title': 'This slide is being refreshed', 'body': 'The figures on this slide follow the final pricing structure and will be in place before the review. Nothing on this placeholder is a quote.'}],
            'source': 'Placeholder, 15 Oct 2026.', 'notes': 'Placeholder slide; the final version replaces it before the review.'}

# ---------------------------------------------------------------- per-country appendix content
LEVER_MONEY = {'local': '$9K incremental GMV a month, one fifth', 'appr': '$36K incremental GMV a month, one fifth', 'mdr': '$4.5K saved a month, one fifth of base'}

def levers(t1, t2, t3):
    return [{'num': '1', 'label': 'LOCAL METHODS', 'value': '+1.0% of TPV', 'money': LEVER_MONEY['local'], 'tactic': t1},
            {'num': '2', 'label': 'APPROVAL AND RETRIES', 'value': '+3.0 pts approval', 'money': LEVER_MONEY['appr'], 'tactic': t2},
            {'num': '3', 'label': 'COST AND LEVERAGE', 'value': '50 bps of TPV', 'money': LEVER_MONEY['mdr'], 'tactic': t3}]

TABLE_COLS = ['Priority', 'Method', 'Scale', 'Role for the Shop', 'Carried by']
TABLE_W = [0.13, 0.22, 0.21, 0.22, 0.22]

def country(id_, cc, name, headline, stats, levs, rows, box_items, sowhat, source, notes):
    return {'id': id_, 'type': 'country_deepdive', 'kicker': f'APPENDIX · {name.upper()}', 'flag': FLAG(cc), 'headline': headline,
            'stats': stats, 'levers': levs,
            'table': {'label': 'PAYMENT METHOD PRIORITY', 'columns': TABLE_COLS, 'col_widths': TABLE_W, 'font_size': 6.5, 'header_style': 'blue', 'rows': rows},
            'box': {'header': 'WHAT IT MEANS FOR THE SHOP', 'items': box_items}, 'sowhat': sowhat, 'source': source, 'notes': notes}

def connections(id_, name, headline, mor, methods, table, notes, extra_sections=None, source=None):
    hdr, chips = live_chips(name)
    hdr = hdr.replace('Live through Yuno', 'Local rails and acquirers live through Yuno')
    secs = [{'header': 'Merchant of record at launch', 'style': 'signed', 'chips': [chip(m) for m in mor]}] if mor else []
    secs += extra_sections or []
    secs += [{'header': hdr, 'chips': chips}, {'header': 'Wallets and payment methods (selected)', 'chips': method_chips(methods)}]
    s = {'id': id_, 'type': 'logo_grid', 'kicker': f'APPENDIX · {name.upper()} · CONNECTIONS THROUGH YUNO', 'headline': headline, 'sections': secs,
         'source': source or 'Yuno integrations directory (docs.y.uno Payment Type list and y.uno/integrations), pulled 14 Oct 2026. CONFIRMED. Logos are the providers\' own marks.', 'notes': notes}
    if table: s['table'] = table
    return s

# ---------------------------------------------------------------- the deck
S = []

S.append({'id': 'cover', 'type': 'cover', 'title': 'Carry1st Shop in Latin America by Black Friday',
          'subtitle': 'One integration for five markets, EBANX plus any rail each market needs, priced on what Carry1st sells',
          'presenter': 'German Tatis, Yuno · 16 October 2026',
          'notes': 'Cordel, Fatih: this deck sets out how the Carry1st Shop can launch in Latin America with EBANX plus any other rail, acquirer or merchant of record each market needs, through one integration; what that is worth at a $5 to $10 ticket; how the fee is shaped; and how the move from merchant of record to local presence works later. Every number carries its label: confirmed in public documentation, read on a third party\'s public page, a Yuno estimate with the assumption stated, or open with an owner. The appendix holds the market detail for each of the five countries.'})

S.append({'id': 'agenda', 'type': 'agenda', 'items': [{'num': '01', 'title': 'Executive summary'}, {'num': '02', 'title': 'Where Carry1st stands'},
          {'num': '03', 'title': 'Two ways to launch'}, {'num': '04', 'title': 'Why Yuno'}, {'num': '05', 'title': 'Business case'}, {'num': '06', 'title': 'Proposal'},
          {'num': '07', 'title': 'Phase 2'}, {'num': 'A', 'title': 'Appendix: LatAm deep dive and sources'}],
          'notes': 'Thirty minutes: the executive summary and the two ways to launch first, then the business case and the proposal, then Phase 2. The appendix holds the market detail for each country, to read afterwards.'})

S.append(divider('d01', '01', 'Executive summary', 'The decision, the recommended path, and what it returns at launch and at run rate',
                 'One slide: the decision in front of Carry1st, what Yuno proposes, and what it is worth at launch volume and at the end-2027 run rate.'))

S.append({'id': 'exec', 'type': 'exec_summary', 'kicker': 'EXECUTIVE SUMMARY', 'tag': ['ESTIMATE'],
          'headline': 'Through Yuno, EBANX plus local rails per market costs less than EBANX direct at run rate, and pays back in month one.',
          'left_header': 'WHERE CARRY1ST STANDS',
          'left_items': [
            {'title': 'The decision', 'body': 'Launch the Carry1st Shop in Brazil, Argentina, Mexico, Colombia and Bolivia by Black Friday, 27 November 2026, through a merchant of record: EBANX direct, or EBANX plus the rails each market needs, through Yuno.'},
            {'title': 'The economics to beat', 'body': 'A $10 average and $5 median ticket, so every fixed fee per transaction is punished; $4 to 5M a month in LatAm by end 2027 (Carry1st, Cordel, Oct 2026, estimate).'},
            {'title': 'What EBANX direct gives', 'body': 'One agreement and one integration for all five countries once EBANX enables each; but one approval rate, one price, Bolivia cash only, no MODO.'},
            {'title': 'What is still open', 'body': 'Volumes by country, EBANX\'s proposed rates, Carry1st\'s take rate and the tax treatment under each MoR. Every modeled number in this deck carries its label and an owner.'}],
          'right_header': 'WHAT YUNO PROPOSES',
          'right_cards': [
            {'title': 'One integration, every rail Carry1st needs', 'body': 'EBANX plus any other MoR, acquirer or local method each market needs, all connections on the Yuno SDK: retries and failover across them, Phase 2 without touching checkout.'},
            {'title': 'A fee that scales with sales, not with transactions', 'body': '$7,500 a month including the first $500K of monthly sales, then 40 / 30 / 20 / 10 bps on sales above it. At launch: $7,500 and nothing per transaction; at $4.5M: $21,000 a month, 0.47% of sales.'},
            {'title': 'A case that pays back in month one', 'body': 'Base case at run rate: $44.7 per $1,000 of sales through Yuno against $45.0 direct, +$31.8K a month net ($381K a year, 2.5x Yuno\'s cost); break-even about 12,000 transactions a month.'}],
          'bottom': 'EBANX stays at the center and Yuno adds every rail around it; even the conservative case is positive at run rate.',
          'source': 'Yuno business-case model, 15 Oct 2026, base scenario: EBANX direct all-in 4.5% of sales and a 15% take rate are estimates, replaced by EBANX\'s quote and Shop margins. Volumes: Carry1st, Cordel, Oct 2026, estimate.',
          'notes': 'The whole deck on one slide. Left, where you stand: five markets, six weeks, a $5 median ticket and a run-rate estimate that is yours. Right, what we propose: one integration carrying EBANX plus any other merchant of record, acquirer or local method each market needs, a fee that is a share of what you sell with the first $500K of monthly sales inside the platform fee, and a business case that, in the base scenario, makes the Yuno route the cheaper cost line at run rate before counting approval or coverage gains. Two numbers to keep: break-even at about 12,000 transactions a month, and the conservative case still positive at run rate. Everything modeled is labelled and will be re-cut on your volumes and EBANX\'s quote.'})

S.append(divider('d02', '02', 'Where Carry1st stands and what Black Friday needs', 'What the launch has to get right, the Shop and the plan, and what the five markets demand',
                 'Section 02 sets out what the Latin America launch has to get right, sizes the plan, and shows what the five markets require of a checkout.'))

S.append({'id': 'heard', 'type': 'two_column', 'kicker': 'WHERE CARRY1ST STANDS · WHAT THE LAUNCH HAS TO GET RIGHT',
          'headline': 'The Latin America launch has to get five things right, from economics at a $5 ticket to a path to local presence.',
          'cols': [{'header': 'THE COMMERCIAL TEST', 'items': [
                      {'title': 'Economics that hold at a $5 to $10 ticket', 'body': 'Processing savings, higher approval and engineering avoided have to cover the cost of orchestration at small tickets, not only at scale.'},
                      {'title': 'Pricing that scales with sales, not transactions', 'body': 'With a median ticket near $5, a fixed fee per transaction taxes the core basket; cost should be a share of what the Shop sells.'},
                      {'title': 'One integration for EBANX and any rail added later', 'body': 'EBANX stays where it is strong; other merchants of record, local acquirers and methods arrive as connections, not new builds.'}]},
                   {'header': 'THE GAMER AND THE ROADMAP', 'items': [
                      {'title': 'A checkout that converts with local methods', 'body': 'Pix, PSE, SPEI, wallets and QR in local currency, confirming in seconds to match instant top-up delivery.'},
                      {'title': 'A path from merchant of record to local presence', 'body': 'Launch on a merchant of record now; move country by country to non-resident accounts or local entities later, without a rebuild.'}]}],
          'bar': 'This is our read of what the launch needs; the rest of the deck tests EBANX direct and the Yuno route against these five points.',
          'source': 'Yuno analysis of the Carry1st Latin America launch, October 2026.',
          'notes': 'Our read of what the Latin America launch has to get right, in five points. Two are commercial: economics that hold at a small ticket, and a fee that follows sales rather than transactions. One is architectural: EBANX plus whatever else each market needs, without a new build each time. Two are about the gamer and the roadmap: local methods that confirm instantly, and a path to local presence that does not mean rebuilding the checkout. The rest of the deck is built against these five points.'})

S.append({'id': 'stands', 'type': 'scale', 'kicker': 'WHERE CARRY1ST STANDS · THE SHOP AND THE PLAN',
          'headline': 'Five markets, a $10 average ticket and six weeks to Black Friday: the launch has to be fast, local and cheap per transaction.',
          'left_header': 'THE SHOP TODAY',
          'tiles': [{'value': '21', 'label': 'storefronts across Africa, the Middle East and the US: game top-ups and gift cards, instant delivery'},
                    {'value': '$10', 'label': 'average ticket; median about $5 (Carry1st, Cordel, Oct 2026, estimate)'}],
          'left_note': 'Founded 2018 in Cape Town; backed by a16z, BITKRAFT, Google, Konvoy and Sony. Publishing partners include Activision, Supercell and EA. The US storefront already lists Free Fire Diamonds (LATAM) and Brazil SKUs.',
          'mid_header': 'THE LATAM PLAN AS YOU DESCRIBED IT',
          'mid_items': ['Brazil first, then Argentina, Mexico, Bolivia and Colombia; all five together if payments, localization and support fit in two to three weeks.',
                        'Launch through a merchant of record (no LatAm entities today); non-resident accounts and local entities are a Phase 2 decision.',
                        '$4 to 5M a month by end 2027 (Carry1st, Cordel, Oct 2026, estimate): about 450,000 transactions a month at a $10 ticket. Volumes by country to come.'],
          'right_header': 'WHAT BLACK FRIDAY NEEDS',
          'right_body': '**Live by 27 November 2026.** Local methods that confirm in seconds (Pix, PSE, SPEI, wallets), because the Shop promises instant delivery. **A domestic charge in local currency,** so cards are not declined as cross-border and gamers do not pay FX or foreign-purchase taxes. **One approval rate to beat, not to accept:** a second provider in play from day one. **Spanish and Portuguese** checkout and support. **Costs that scale with a $5 median,** never a fixed fee per transaction.',
          'bar': 'Six weeks to Black Friday: provider contracts and KYC are the critical path; the Yuno integration itself is measured in days (Yuno estimate).',
          'source': 'Discovery call, Oct 2026 (Cordel\'s figures are estimates, not yet aligned internally); shop.carry1st.com sitemap and Carry1st press releases 2021 to 2026, read 15 Oct 2026.',
          'notes': 'This is the plan as you described it, in your numbers. We label the run rate as your estimate because you told us it is not yet aligned internally, and the model in this deck runs at four volumes so it holds whichever way the alignment lands. The right-hand column is the checklist we built the launch against: speed, local methods that confirm instantly, domestic presentation of the charge, a second provider from day one, and costs that behave at a $5 median.'})

S.append({'id': 'needs', 'type': 'four_numbers', 'kicker': 'WHERE CARRY1ST STANDS · WHAT THE FIVE MARKETS DEMAND',
          'headline': 'In every launch market the method that wins is local and instant, and most of it sits outside international card rails.',
          'tiles': [{'value': '42%', 'label': "of Brazil's online purchases are Pix (2025); cards 41%"},
                    {'value': '63.9%', 'label': "of Colombia's e-commerce transactions run on PSE (Q2 2025)"},
                    {'value': '46%', 'label': "of Argentina's e-commerce value is in digital wallets (2024)"},
                    {'value': '74%', 'label': 'of Mexican online buyers pay with debit cards (AMVO 2024)'}],
          'right_header': 'WHAT THIS MEANS FOR THE SHOP',
          'right_items': [{'title': 'Instant confirmation is the product', 'body': 'Pix, PSE, SPEI and wallets confirm in seconds, which matches instant top-up delivery. Cash vouchers (Boleto, OXXO, Rapipago) confirm hours or days later and belong in a second wave.'},
                          {'title': 'Domestic presentation decides approval', 'body': 'Vendor-reported ranges put cross-border card approval at 30 to 60% against 80 to 90% for local processing (2017 to 2026). A merchant of record charging in local currency is what lets a Brazilian or Mexican debit card approve.'},
                          {'title': 'Taxes follow the rail', 'body': 'Argentina adds a 30% perception on foreign-currency card purchases; Brazil charges 3.5% IOF on international card payments. A local-currency charge through the MoR\'s local entity is domestic for the gamer. TO VALIDATE with each MoR.'},
                          {'title': 'Bolivia and Argentina need more than EBANX', 'body': 'EBANX lists only PagosNet cash in Bolivia and no MODO or interoperable QR in Argentina; other providers live on Yuno carry them.'}],
          'bar': 'The Shop\'s African playbook, local methods in local currency, is exactly what LatAm requires; the open question is which rail carries it.',
          'source': 'Reuters on PCMI data, 10 Feb 2026; CCCE via Valora Analitik, 24 Aug 2025; PCMI 2024 data; AMVO Estudio 2024; approval ranges are vendor-reported (Worldline, Rapyd, Nuvei, Antom, EBANX, 2017 to 2026); ARCA RG 5617/2024; Decree 12.499/2025. PUBLIC DOCS.',
          'notes': 'Four numbers, one per market, and they point the same way: the winning method is local and it confirms instantly. Pix in Brazil, PSE in Colombia, wallets in Argentina and debit cards in Mexico are the rails the Shop needs on day one. The approval ranges on the right are vendor claims, not independent studies, so we show them as ranges and label them; the direction is not in dispute. The two tax lines explain why a local-currency charge through a merchant of record matters for the gamer, and both are items we will confirm in writing with each merchant of record.'})

S.append(divider('d03', '03', 'Two ways to launch', 'EBANX direct, or EBANX plus any local rail through Yuno',
                 'The decision in one grid, then a picture of how Yuno sits alongside EBANX.'))

S.append({'id': 'options', 'type': 'comparison_grid', 'kicker': 'TWO WAYS TO LAUNCH · THE COMPARISON', 'tag': ['PUBLIC DOCS', 'CONFIRMED'],
          'headline': 'EBANX direct can switch on all five markets with one integration; what it cannot give Carry1st is a second rail.',
          'legend': ['Gap stays open', 'Partly closed', 'Closed'], 'row_header': 'WHAT THE LAUNCH NEEDS', 'row_header_sub': 'Six rows that decide the economics',
          'options': [{'header': 'EBANX direct', 'sub': 'TODAY\'S DEFAULT'}, {'header': 'EBANX plus a second direct build', 'sub': 'OPTION A'}, {'header': 'EBANX plus local rails through Yuno', 'sub': 'OPTION B · RECOMMENDED'}],
          'rows': [
            {'label': 'Integrations to build', 'sub': 'now, and when a second provider arrives', 'cells': [
                {'state': 'partial', 'text': 'One now. Each later provider is a new build.'},
                {'state': 'open', 'text': 'Two now; a third provider means a third build.'},
                {'state': 'closed', 'text': 'One now. EBANX and every later provider is a connection.'}]},
            {'label': 'Countries on one integration', 'sub': 'Brazil, Argentina, Mexico, Colombia, Bolivia', 'cells': [
                {'state': 'partial', 'text': 'All five once EBANX enables each; Bolivia cash only.'},
                {'state': 'closed', 'text': 'All five; a second provider adds Bolivia cards, MODO.'},
                {'state': 'closed', 'text': 'All five, plus any rail live on Yuno, one integration.'}]},
            {'label': 'Approval levers', 'sub': 'retries, routing, failover', 'cells': [
                {'state': 'open', 'text': 'One rail, one approval rate; outages wait for EBANX.'},
                {'state': 'partial', 'text': 'Second rail exists; retry and failover are yours to build.'},
                {'state': 'closed', 'text': 'Retry on the second rail; Monitors reroute on a drop.'}]},
            {'label': 'Cost leverage', 'sub': 'MDR negotiation', 'cells': [
                {'state': 'open', 'text': 'One counterparty, no alternative route.'},
                {'state': 'partial', 'text': 'Two counterparties; moving volume is a code change.'},
                {'state': 'closed', 'text': 'Volume moves by rule: a real negotiating position.'}]},
            {'label': 'Tokens, dashboard, reconciliation', 'sub': '', 'cells': [
                {'state': 'partial', 'text': 'Tokens held at EBANX; one portal.'},
                {'state': 'open', 'text': 'Two vaults, two portals, two reconciliations.'},
                {'state': 'closed', 'text': 'One vault, portable tokens; one dashboard for all.'}]},
            {'label': 'Time to 27 Nov, and Phase 2', 'sub': 'local entities later', 'cells': [
                {'state': 'partial', 'text': 'EBANX onboarding sets the pace; Phase 2 is a new build.'},
                {'state': 'open', 'text': 'Two onboardings and two builds in six weeks.'},
                {'state': 'closed', 'text': 'Same onboarding in parallel; Yuno setup in days; Phase 2 is a connection.'}]}],
          'footer': [{'label': 'Rows closed'}, {'value': '0 of 6'}, {'value': '1 of 6'}, {'value': '6 of 6'}],
          'closing_line': 'One integration either way; through Yuno it carries EBANX, any other rail and the path to local acquiring.',
          'source': 'EBANX docs (api-operability, DEUNA partner page, pay-in guide, Bolivia and Argentina overviews) and status.ebanx.com, read 15 Oct 2026 (PUBLIC DOCS); docs.y.uno connections, routing, monitors, tokens (CONFIRMED). Yuno setup time is a Yuno estimate.',
          'notes': 'We start with the honest answer on EBANX direct. One EBANX integration and one agreement can switch on all five countries: the country is a field in the request, and EBANX enables each country on your account during onboarding, with sandbox tests per country and an integration review before production. So EBANX direct is a real option and we say so. What it cannot give you is a second rail: no retry on a decline, no failover in an outage, no cards or QR in Bolivia, no MODO in Argentina, and one counterparty on price. The middle column shows what it costs to fix that with a second direct build. The right column is the same fix as a routing rule.'})

S.append({'id': 'arrangement', 'type': 'diagram', 'kicker': 'TWO WAYS TO LAUNCH · HOW YUNO SITS ALONGSIDE EBANX',
          'headline': 'Yuno sits between the Shop and every provider: EBANX as merchant of record, plus whatever rail each market needs.',
          'boxes': [
            {'id': 'l1', 'x': 0, 'y': 0, 'w': 200, 'h': 12, 'style': 'label', 'title': 'CARRY1ST'},
            {'id': 'shop', 'x': 0, 'y': 13, 'w': 420, 'h': 36, 'style': 'outline', 'title': 'Carry1st Shop · web and app', 'body': 'Same checkout in every market; Spanish and Portuguese; instant delivery after confirmation'},
            {'id': 'yuno', 'x': 0, 'y': 66, 'w': 420, 'h': 62, 'style': 'blue', 'title': 'Yuno · one integration', 'pill': 'Rules set by Carry1st',
             'body': 'Checkout and SDK with local methods per market · routing and retries · Monitors and failover · vault with portable tokens · one dashboard and reconciliation'},
            {'id': 'ebanx', 'x': 0, 'y': 158, 'w': 101, 'h': 66, 'style': 'light', 'title': 'EBANX · MoR', 'body': 'Brazil, Mexico, Colombia, Argentina: cards and the main local methods', 'pill': 'CONFIRMED'},
            {'id': 'mor2', 'x': 106, 'y': 158, 'w': 101, 'h': 66, 'style': 'light', 'title': 'More MoRs as needed', 'body': 'A second MoR where a market needs one, chosen with Carry1st (OPEN)'},
            {'id': 'apms', 'x': 212, 'y': 158, 'w': 102, 'h': 66, 'style': 'light', 'title': 'Local rails', 'body': 'Acquirers and APMs: Pix, PSE, Bre-B, SPEI, OXXO, MODO, QR', 'pill': 'CONFIRMED'},
            {'id': 'local', 'x': 319, 'y': 158, 'w': 101, 'h': 66, 'style': 'panel', 'title': 'Phase 2', 'body': 'Local acquiring on a local entity or account, one more connection', 'pill': 'LATER'},
            {'id': 'note', 'x': 0, 'y': 231, 'w': 420, 'h': 36, 'style': 'panel', 'title': 'One agreement per provider, one integration for all of them', 'body': 'Your contracts, Yuno holds the credentials: Carry1st signs with EBANX and each provider it adds, each one a connection.'}],
          'connectors': [{'from': 'shop', 'to': 'yuno'}, {'from': 'yuno', 'to': 'ebanx'}, {'from': 'yuno', 'to': 'mor2'}, {'from': 'yuno', 'to': 'apms'}, {'from': 'yuno', 'to': 'local', 'label': 'later'}],
          'side': {'header': 'WHAT THIS ARRANGEMENT GIVES CARRY1ST', 'items': [
              {'title': 'One integration unlocks every rail', 'body': 'EBANX for what it covers; other MoRs, acquirers and local methods for what it does not. All are connections on the same checkout.'},
              {'title': 'One dashboard, one reconciliation', 'body': 'Approval by provider and country, retries, settlements and chargebacks in one console; Payment Concierge answers questions in Slack.'},
              {'title': 'MoR swap insurance', 'body': 'If EBANX pricing or service slips, a market moves to another provider live on Yuno by routing rule, not by sprint. Card tokens stay in Yuno\'s vault.'}]},
          'source': 'docs.y.uno connections, routing, monitors, tokens; Yuno integrations directory (CONFIRMED); EBANX country pages, read 15 Oct 2026 (PUBLIC DOCS). Second MoR per market: OPEN, owner Justo.',
          'notes': 'This is how Yuno fits alongside EBANX. Carry1st keeps a direct agreement with EBANX and signs with whichever other providers each market needs: a second merchant of record, local acquirers, local methods. Yuno never sits in the money flow. What changes is the integration: the Shop talks to one SDK, every provider is a set of credentials entered as a connection, and routing rules decide which one carries each payment. Which second merchant of record to add is a choice we make with you market by market, on coverage and price. The Phase 2 box is about local presence: when a country justifies a local entity, the local acquirer is one more connection and the checkout does not change.'})

S.append(divider('d04', '04', 'Why Yuno', 'Requirement, benefit, proof: what the Shop needs, what it gets, how we show it',
                 'Section 04 is the value proposition in the order you would check it: what the Shop needs, what each need gets through Yuno, and the proof behind it.'))

S.append({'id': 'why-rbp', 'type': 'table', 'kicker': 'WHY YUNO · REQUIREMENT, BENEFIT, PROOF', 'tag': ['CONFIRMED'],
          'headline': 'Seven things the Shop needs in Latin America, what each one gets through Yuno, and how we prove it.',
          'columns': ['Requirement', 'Benefit for the Shop', 'Proof', 'Label'], 'col_widths': [0.22, 0.36, 0.32, 0.10], 'header_style': 'dark', 'font_size': 7, 'bold_first_col': True, 'zebra': True,
          'rows': [
            ['One integration for five countries', 'EBANX and every other provider as connections on one SDK; later MoRs, acquirers and local methods added without touching checkout', 'Connections are credentials entered in the dashboard or by API; Rappi: new-provider implementation time down to zero', {'text': '', 'pill': 'CONFIRMED'}],
            ['Local methods per market', 'Pix, PSE, Nequi, Bre-B, SPEI, OXXO Pay, CoDi, MODO, Rapipago, QR in Bolivia and wallets, returned per country by the checkout session', 'Yuno directory, Oct 2026: 46 providers live in Brazil, 36 in Mexico, 31 in Colombia, 23 in Argentina, 6 in Bolivia', {'text': '', 'pill': 'CONFIRMED'}],
            ['Higher approval, fewer lost sales', 'A decline on EBANX retries on a second provider; routing by BIN, brand, amount and country; Smart Routing as data builds', 'Published across Yuno merchants: up to 7% authorization uplift, 30% recovered revenue. Carry1st uplift modeled at +1.5 to +5 points', {'text': '', 'pill': 'CONFIRMED'}],
            ['No single point of failure', 'Monitors move traffic to the fallback provider when approval drops, and move it back on recovery', 'docs.y.uno monitors and automation; status.ebanx.com shows degradations and daily maintenance windows', {'text': '', 'pill': 'CONFIRMED'}],
            ['Cost that scales with a $5 median', 'More than one provider per rail makes the MDR negotiable; Yuno is billed as a share of what Carry1st sells, never a fixed fee per transaction', 'Business case in section 05 and the proposal in section 06', {'text': '', 'pill': 'ESTIMATE'}],
            ['A checkout that converts, shipped in days', 'Web and mobile SDKs; local prices and methods per market; tokens portable across providers; PCI DSS, SOC 2 Type 2, ISO 27001 and 27701', 'Working prototype of the Shop checkout on the Yuno SDK, sandbox, four LatAm markets, 15 Oct 2026', {'text': '', 'pill': 'CONFIRMED'}],
            ['One view of the business, and a team that has done this', 'Approval, retries, chargebacks and reconciliation by provider and country; Payment Concierge; dedicated KAM and TAM; teams in São Paulo, Mexico City, Bogotá, Buenos Aires', 'y.uno/about; inDrive: around 90% approval and 11 new countries in under eight months', {'text': '', 'pill': 'CONFIRMED'}]],
          'note': 'Labels: CONFIRMED in docs.y.uno or y.uno, read 15 Oct 2026; ESTIMATE is modeled with the assumption stated in section 05.',
          'source': 'docs.y.uno (connections, routing, monitors, tokens, insights), y.uno homepage, about and success stories, Yuno integrations directory, read 14 and 15 Oct 2026.',
          'notes': 'We read this table top-down: the left column is what the Shop needs, the middle is what it gets, the right is how you can check it. Five of the seven rows are confirmed in our public documentation or on y.uno; the cost row is modeled and we label it so. The one number we lean on for approval is the published ceiling of up to 7%, and the Carry1st model stays well under it.'})

S.append({'id': 'platform', 'type': 'template_keep', 'template_index': 23, 'template_ref': 'four-pillars',
          'replacements': [{'find': '460+', 'replace': '16'}, {'find': 'INTEGRATIONS', 'replace': 'OFFICES'}],
          'notes': 'The Yuno platform in one view: orchestration, checkout and SDKs, security and risk, and the intelligence layer. The four figures are the ones published on y.uno: 16 offices, 190+ countries, 1,000+ payment methods and providers, 180+ currencies. For the Shop the modules that matter first are smart routing, Monitors and auto-failover, the customizable checkout and the PCI vault; the rest is there when you need it.'})

S.append({'id': 'proof', 'type': 'stats', 'kicker': 'WHY YUNO · PROOF',
          'headline': 'The checkout already exists: a working prototype of the Shop on the Yuno SDK runs in four LatAm markets today.',
          'tiles': [{'label': 'PROTOTYPE', 'value': '4', 'caption': 'LatAm markets in the sandbox replica of the Shop checkout (Brazil, Colombia, Argentina, Mexico): local prices, with Pix, OXXO, PSE, Nequi, Daviplata and Mercado Pago returned by the checkout session. Bolivia next.'},
                    {'label': 'PUBLISHED', 'value': 'up to 7%', 'caption': 'authorization uplift across Yuno merchants, with 30% recovered revenue (y.uno, read 15 Oct 2026).'},
                    {'label': 'REFERENCES', 'value': '11', 'caption': 'new countries in under eight months for inDrive, at around 90% approval; Rappi cut new-provider implementation time to zero (y.uno success stories).'}],
          'chips': ['NetEase Games', 'Garena', 'inDrive', 'Rappi', "McDonald's (Arcos Dorados)", 'PCI DSS', 'SOC 2 Type 2', 'ISO 27001', 'ISO 27701'],
          'paragraph': 'The prototype replicates the Shop\'s Call of Duty: Mobile top-up flow with a market switcher: the South Africa flow as it runs today, and the same page on the Yuno Web SDK against the sandbox for Brazil, Colombia, Argentina and Mexico, with an under-the-hood panel showing what changed, the methods wired per market and the request timeline. It is a sandbox prototype, not production. NetEase Games and Garena are gaming publishers live on Yuno; one more mobile-games reference is to be confirmed.',
          'bar': 'The prototype is live in the sandbox today; access details go to Fatih\'s team after the call, and we extend it to Bolivia and to the Shop\'s real SKUs before signing.',
          'source': 'Carry1st Shop prototype on the Yuno SDK, Yuno sandbox, 15 Oct 2026; y.uno homepage and success stories (inDrive, Rappi), read 15 Oct 2026. CONFIRMED.',
          'notes': 'Proof you can click. The prototype is a replica of your Call of Duty: Mobile top-up page running on the Yuno Web SDK against our sandbox for four of the five markets, and we will walk through it live. The published figures are the only Yuno-wide numbers we use anywhere in this deck: up to 7% authorization uplift and 30% recovered revenue. The gaming publishers named are live on Yuno and shown on y.uno; one further mobile-games reference will be confirmed with you after the call.'})

S.append({'id': 'trusted', 'type': 'template_keep', 'template_index': 25, 'template_ref': 'trusted', 'delete_images_matching': ['g3f76accd9b2_0_4'],
          'notes': 'A selection of the companies that run payments on Yuno, including gaming publishers NetEase and Garena and marketplaces and mobility companies that operate across Latin America. Logos as shown on y.uno.'})

S.append(divider('d05', '05', 'Business case', 'EBANX direct against EBANX plus local rails through Yuno: four levers, three scenarios, one ticket test',
                 'Three slides: the four levers and what each is worth at run rate, the total impact across three scenarios, and why the shape of the fee matters at a $5 median ticket.'))

# Business case in the Luni format (German, 15 Oct 2026): annual $ per lever at the 450K run rate, contribution view,
# from model/model_numbers.json (l1 MDR, l4 integrations avoided: per-market EBANX work, later integrations, maintenance; l2c approval, l3c local methods; x12). Checked against bc_numbers.md Section B.
_MN = json.load(open(os.path.join(HERE, 'model', 'model_numbers.json')))['model']
def _k(v): return f'${v / 1e6:,.2f}M' if v >= 1e6 else (f'${v / 1e3:,.0f}K' if v >= 9500 else f'${v / 1e3:,.1f}K')
_LV = {sc: [_MN[sc]['450000'][k] * 12 for k in ('l1', 'l4', 'l2c', 'l3c')] for sc in ('Conservative', 'Base', 'Optimistic')}
_TOT = {sc: sum(v) for sc, v in _LV.items()}
_YUNO_YR = _MN['Base']['450000']['yuno'] * 12
assert round(_TOT['Base']) == round(_MN['Base']['450000']['gross_c'] * 12) and _YUNO_YR == 252000
_NET = {sc: _TOT[sc] - _YUNO_YR for sc in _TOT}

S.append({'id': 'bc-levers', 'type': 'lever_grid', 'kicker': 'BUSINESS CASE · FOUR LEVERS AT RUN RATE', 'tag': ['ESTIMATE'],
          'headline': f'At $4.5M a month of sales, the four levers are worth about {_k(_TOT["Base"])} a year to Carry1st in the base case.',
          'groups': [{'label': 'Cost levers', 'span': 2}, {'label': 'Operational levers', 'span': 2}],
          'row_labels': ['Lever', 'How it works', 'Conservative', 'Optimistic'],
          'levers': [
            {'num': 1, 'name': 'Processing cost', 'range': '25 to 75 bps',
             'body': 'With EBANX and other providers live on the same rails (Pix runs on 27 in Brazil, PSE on 12 in Colombia), volume moves by rule to the cheaper route, and every rate is negotiated against a real alternative. A processing saving is 100% contribution.',
             'conservative': f'+{_k(_LV["Conservative"][0])}/yr', 'optimistic': f'+{_k(_LV["Optimistic"][0])}/yr'},
            {'num': 2, 'name': 'Integrations avoided', 'range': '5 markets + 1 to 3',
             'body': 'Direct, EBANX is enabled, tested and certified market by market, each later provider is a new build, and Carry1st maintains every integration. Through Yuno: one integration, ready for every market, and Yuno maintains the connections.',
             'conservative': f'+{_k(_LV["Conservative"][1])}/yr', 'optimistic': f'+{_k(_LV["Optimistic"][1])}/yr'},
            {'num': 3, 'name': 'Approval uplift', 'range': '+1.5 to +5 pts',
             'body': 'Direct, every payment goes to one provider. Through Yuno a decline on EBANX retries on a second provider, Monitors reroute on a drop, and routing by BIN and country lifts approval from a 75% baseline. Counted at the take rate, not at face value.',
             'conservative': f'+{_k(_LV["Conservative"][2])}/yr', 'optimistic': f'+{_k(_LV["Optimistic"][2])}/yr'},
            {'num': 4, 'name': 'Local methods, checkout', 'range': '+0.5 to +2% of sales',
             'body': 'One checkout returns Pix, PSE, Nequi, SPEI, OXXO, MODO and QR per market, in local currency, so gamers without an international card can pay. Incremental sales are counted at the take rate, net of processing.',
             'conservative': f'+{_k(_LV["Conservative"][3])}/yr', 'optimistic': f'+{_k(_LV["Optimistic"][3])}/yr'}],
          'assumptions': '**Assumptions** All figures in USD, a year, at run rate: 450,000 transactions a month at a $10 average ticket, $4.5M of monthly sales (Carry1st, Cordel, Oct 2026, estimate). Baseline approval 75%; EBANX direct all-in 4.5% of sales (ESTIMATE, replaced by EBANX\'s quote); 15% take rate on sales (ESTIMATE). Contribution view: L1 and L2 count in full, L3 and L4 at the take rate net of processing. L2: 5 markets x 2 to 4 weeks on EBANX plus 1 to 3 later integrations x 4 to 8 weeks over 24 months, plus 0.25 to 1 FTE upkeep a year, at $2,000 a week. Ranges are Yuno modelling assumptions, recalibrated on Carry1st\'s data.',
          'closing': 'The value can be monetized from launch: Yuno\'s connections to EBANX and the local rails already exist, so each lever is switched on, not built.',
          'source': 'Yuno business-case model (bc_model.xlsx), 15 Oct 2026. ESTIMATE; every assumption is on the risks slide in the appendix.',
          'notes': f'Four levers, two that cut cost and two that add sales. Processing cost comes first because resale margins are thin: with EBANX and other providers live on the same rails, volume moves to the cheaper route by rule, and a saving on processing is worth one hundred cents on the dollar. Integrations avoided is the engineering Carry1st does not spend: enabling, testing and certifying EBANX market by market, building each later provider, and maintaining all of it. Through Yuno, one integration is ready for every market and Yuno maintains the connections. Approval and local methods add sales, and we count them at your take rate, not at face value. The two rows show the conservative and optimistic value of each lever a year at the $4.5M run rate; the base case totals about {_k(_TOT["Base"])} a year.'})

S.append({'id': 'bc-impact', 'type': 'impact_table', 'kicker': 'BUSINESS CASE · TOTAL IMPACT', 'tag': ['ESTIMATE'],
          'headline': 'Total impact',
          'subline': 'At run rate: 450,000 transactions a month at a $10 average ticket, $4.5M of monthly sales, contribution view, a year.',
          'columns': ['Scenario', 'L1 Processing cost', 'L2 Integrations', 'L3 Approval', 'L4 Local methods', 'Total annual'],
          'rows': [{'label': sc if sc != 'Base' else 'Base', 'cells': [_k(v) for v in _LV[sc]], 'total': _k(_TOT[sc]), 'highlight': sc == 'Base'}
                   for sc in ('Conservative', 'Base', 'Optimistic')],
          'hero': {'value': _k(_TOT['Base']),
                   'text': f'of base-case **annual value** across the four levers, within a {_k(_TOT["Conservative"])} to {_k(_TOT["Optimistic"])} range, against $252,000 a year on the proposal that follows: **+{_k(_NET["Base"])} a year net** in the base case, +{_k(_NET["Conservative"])} in the conservative case.'},
          'takeaways': [
            {'title': 'Processing cost carries it', 'body': f'L1 is {_LV["Base"][0] / _TOT["Base"] * 100:.0f}% of the base case: a saving on processing counts in full, while extra sales count only at the take rate.'},
            {'title': 'Nothing here needs a rebuild', 'body': 'EBANX stays. Other merchants of record, local acquirers and methods are connections already live on Yuno, switched on per market.'},
            {'title': 'The baseline is yours to set', 'body': '75% approval, a 4.5% all-in rate and a 15% take rate are our estimates; your data and EBANX\'s quote replace them before anything is committed.'}],
          'source': 'Yuno business-case model (bc_model.xlsx), 15 Oct 2026. ESTIMATE. Yuno cost: the proposal in section 06, $21,000 a month at $4.5M.',
          'notes': f'The same four levers added up. In the base case they are worth about {_k(_TOT["Base"])} a year at the $4.5M run rate, against $252,000 a year for Yuno, so about {_k(_NET["Base"])} a year net. We show the conservative case honestly: about {_k(_TOT["Conservative"])} of value against the same $252,000, about {_k(_NET["Conservative"])} a year net, which is why the case leans on processing cost first. Every input is a placeholder for your data: approval baseline, EBANX\'s quote and your take rate.'})
S.append({'id': 'bc-ticket', 'type': 'table', 'kicker': 'BUSINESS CASE · SMALL-TICKET SENSITIVITY', 'tag': ['ESTIMATE'],
          'headline': 'A fixed fee doubles as a share of sales when the ticket halves; a share of sales does not: usage on a $5 purchase is two cents or less.',
          'columns': ['Yuno all-in at 450,000 transactions a month', '$5 median ticket', '$10 average ticket', '$15 ticket'], 'col_widths': [0.37, 0.21, 0.21, 0.21], 'header_style': 'dark', 'font_size': 7.5, 'bold_first_col': True, 'zebra': True,
          'rows': [
            ['Sales a month', '$2.25M', '$4.5M', '$6.75M'],
            ['Yuno a month (platform fee plus usage)', '$14.3K', '$21.0K', '$26.0K'],
            [{'text': 'Yuno as a share of sales', 'bold': True}, {'text': '0.63%', 'bold': True}, {'text': '0.47%', 'bold': True}, {'text': '0.39%', 'bold': True}],
            ['Yuno per successful transaction, all-in', '$0.032', '$0.047', '$0.058'],
            ['Marginal usage per transaction by band (40 / 30 / 20 / 10 bps)', '$0.020 / $0.015 / $0.010 / $0.005', '$0.040 / $0.030 / $0.020 / $0.010', '$0.060 / $0.045 / $0.030 / $0.015'],
            ['A fixed $0.05 per transaction, as a share of sales', '1.00%', '0.50%', '0.33%'],
            ['A fixed $0.10 per transaction, as a share of sales', '2.00%', '1.00%', '0.67%'],
            ['At launch, 50,000 transactions a month: Yuno all-in', '$7.5K · 3.00% of sales', '$7.5K · 1.50%', '$8.5K · 1.13%']],
          'note': 'The platform fee is the one fixed element, so at launch and a $5 ticket it is 3.00% of sales; the structure pays off as volume ramps. Yuno business-case model, 15 Oct 2026; tickets: Carry1st, Cordel, Oct 2026 (estimate).',
          'source': 'Yuno business-case model (bc_model.xlsx), Pricing and Sensitivity sheets, 15 Oct 2026. Ticket profile: Carry1st, Cordel, Oct 2026, estimate.',
          'notes': 'Pricing has to work for small purchases, so here is the same 450,000 transactions at three tickets. A fixed fee is blind to the ticket: five cents is 0.5% of a $10 sale and 1% of a $5 sale, ten cents twice that. Yuno\'s usage is a share of what you sell, so on a $5 purchase the marginal cost is one and a half to two cents, and all-in at run rate 0.63% of sales. We are upfront about the one fixed element: at launch volume and a $5 ticket the platform fee alone is 3% of sales, and the structure earns its keep as volume ramps rather than in month one.'})

S.append(divider('d06', '06', 'Proposal', 'A platform fee and a share of what Carry1st sells, never a fee per transaction',
                 'The commercial proposal on one slide, followed by what Yuno puts in before signing and what the platform fee already covers.'))

S.append({'id': 'proposal', 'type': 'pricing_cards', 'kicker': 'PROPOSAL',
          'headline': 'One platform fee covering the first $500K of monthly sales, then a share of sales that falls as Carry1st grows.',
          'subline': '$7,500 a month covering the first $500K of monthly sales, plus a share of the sales above it: $21,000 a month at 450,000 transactions, 0.47% of sales.',
          'left': {'title': 'TRANSACTION FEE', 'sub': 'A share of the month\'s sales above the included block, pooled across the five markets',
                   'rows': [{'label': 'INCLUDED', 'range': 'First $500K of monthly sales', 'rate': '$0'}, {'label': 'TRANCHE 1', 'range': '$500K to $2M', 'rate': '0.40%'}, {'label': 'TRANCHE 2', 'range': '$2M to $5M', 'rate': '0.30%'}, {'label': 'TRANCHE 3', 'range': '$5M to $10M', 'rate': '0.20%'}, {'label': 'TRANCHE 4', 'range': 'Above $10M', 'rate': '0.10%'}],
                   'note': 'No setup fee, no fixed amount per transaction. Only successful transactions count: declines are not billed. Each tranche applies only to the volume inside it.'},
          'middle': {'title': 'PLATFORM FEE', 'value': '$7,500', 'unit': '/ month', 'sub': '$90,000 a year. Covers the first $500K of monthly sales. This is what covers the stack.',
                     'includes_label': 'WHAT IT INCLUDES',
                     'includes': [['Orchestration and rules engine', 'Included'], ['Smart routing and retries', 'Included'], ['Monitors and auto-failover', 'Included'], ['Methods, PSPs, fraud solutions', '1,000+'], ['Checkout, web and mobile SDKs', 'Included'], ['PCI token vault', 'Included'], ['Dashboard and insights', 'Included'], ['Dedicated KAM and TAM', 'Included']],
                     'addons': {'title': 'ADD-ONS', 'sub': 'Billed on usage, quoted separately, not in the totals on this slide.', 'rows': [['Network tokens', 'On usage'], ['3DS authentication', 'On usage']]},
                     'foot': 'Every integration maintained by Yuno. Adding another MoR, a local acquirer or a new local method later is a routing change, not a new project.'},
          'right': {'title': 'WHAT IT MEANS FOR CARRY1ST', 'sub': 'At a $10 average ticket, across the five markets', 'columns': ['Line', '50K', '200K', '450K'], 'col_widths': [2.0, 1, 1, 1], 'font_size': 7.5,
                    'rows': [['Sales a month', '$0.5M', '$2.0M', '$4.5M'], ['Platform fee', '$7,500', '$7,500', '$7,500'], ['Usage · tranche 1', '$0', '$6,000', '$6,000'], ['Usage · tranche 2', '$0', '$0', '$7,500'],
                             {'bold': True, 'cells': ['Total a month', '$7,500', '$13,500', '$21,000']}, ['Total a year', '$90,000', '$162,000', '$252,000'], ['Share of sales', '1.50%', '0.68%', '0.47%'], ['Per successful transaction', '$0.150', '$0.068', '$0.047']],
                    'callout': 'At launch Carry1st pays the platform fee and nothing per transaction. At the run rate the all-in cost is 0.47% of sales, falling as volume grows.',
                    'paragraph': 'Usage on a $5 purchase: $0.020 in tranche 1, $0.005 in tranche 4. A fixed fee stays the same whatever the ticket. The base case returns 2.5x this cost at run rate.'},
          'source': 'Platform fee billed annually. Usage billed monthly in arrears on successful transactions, net 30. Rates locked, tranches reviewed annually as volume grows. All figures in USD.',
          'notes': 'The proposal in one slide. A flat platform fee of $7,500 a month that already covers the first $500K of monthly sales, and above that a share of what you sell: 40 basis points to $2M, 30 to $5M, 20 to $10M, 10 above, each band on the volume inside it, only on approved payments, never a fee per transaction. At launch you pay the platform fee and nothing else; at the $4.5M run rate the all-in cost is $21,000 a month, 0.47% of sales, under five cents on a $10 purchase. Orchestration, smart routing, Monitors, the vault, the dashboard and a dedicated team are inside the platform fee; network tokens and 3DS are billed on usage and quoted separately.'})

S.append({'id': 'onus', 'type': 'two_column', 'kicker': 'INCLUDED, AT NO EXTRA COST',
          'headline': 'What Yuno puts in before signing, and what the platform fee already covers.',
          'cols': [{'header': 'BEFORE YOU SIGN', 'items': [
                      {'title': 'Shop prototype on the Yuno SDK', 'body': 'Already running in the sandbox for four markets; extended to Bolivia and the Shop\'s real SKUs before signature.'},
                      {'title': 'Localization support', 'body': 'Spanish and Portuguese checkout copy and market conventions, with Yuno\'s teams in São Paulo, Mexico City, Bogotá and Buenos Aires.'},
                      {'title': 'Local provider negotiation', 'body': 'Yuno brings EBANX and the other providers each market needs to the table on Carry1st\'s behalf, alongside the EBANX arrangement.'}]},
                   {'header': 'INSIDE THE PLATFORM FEE', 'items': [
                      {'title': 'No setup or implementation fee', 'body': 'Integration support, sandbox, go-live runbook and on-call during the launch weeks.'},
                      {'title': 'Adding a provider later is a routing change, not a fee', 'body': 'A local acquirer in Phase 2, a wallet or a new cash network is a new connection on the same checkout.'},
                      {'title': 'The stack', 'body': 'PCI token vault, risk conditions, Monitors and auto-failover, dashboard and insights with 20 seats.'},
                      {'title': 'Dedicated KAM and TAM', 'body': 'A named account manager and a technical account manager through the LatAm launch and after it.'}]}],
          'bar': 'The platform fee is the only fixed element in the proposal; everything on this slide sits inside it or comes before it.',
          'source': 'Yuno commitments to Carry1st, October 2026.',
          'notes': 'Everything on this slide is included. The prototype and the localization support were offered on the discovery call and we stand by them; the provider negotiation is part of how we work with EBANX and the local providers on the platform for every merchant. Inside the platform fee there is no setup charge, and adding a provider later is configuration, not a project or a fee.'})

S.append(divider('d07', '07', 'Phase 2: merchant of record or local presence', 'Launch on a merchant of record now, then move country by country to local presence',
                 'Merchant of record, non-resident account and local entity compared on launch time, tax, approval and cost, and where Yuno fits as Carry1st moves between them.'))

S.append({'id': 'phase2', 'type': 'table', 'kicker': 'PHASE 2 · MERCHANT OF RECORD AGAINST LOCAL PRESENCE', 'tag': ['PUBLIC DOCS', 'OPEN'],
          'headline': 'A merchant of record launches in weeks, local presence in months; through Yuno the move happens without a rebuild.',
          'columns': ['Dimension', 'Merchant of record (launch)', 'Non-resident account', 'Local entity and local acquirer', 'Yuno\'s role'], 'col_widths': [0.13, 0.25, 0.20, 0.25, 0.17], 'header_style': 'dark', 'font_size': 7, 'bold_first_col': True, 'zebra': True,
          'rows': [
            ['Time to launch', 'Weeks: agreement, KYC, sandbox tests per country and an integration review', 'Weeks to months: local bank account and tax registration without a company; rules vary by country', 'Months: Brazil 6 to 12 weeks for registration plus the bank account; Mexico 4 to 12 weeks; Argentina SAS 7 to 15 business days plus bank; Colombia, Bolivia not published', 'Checkout unchanged across all three; the acquirer is a new connection'],
            ['Who carries tax and FX', 'The MoR: local-currency charge, FX and remittance; Carry1st is paid in USD. Tax treatment per country to be confirmed in writing (OPEN)', 'Carry1st registers for digital-services VAT: Mexico 16%, Colombia 19%, Argentina IVA withheld by issuers; Brazil CBS and IBS from 2026', 'Carry1st as a local taxpayer: VAT, income tax and FX remittance in each country', 'Routing by country keeps each model on its own rail'],
            ['Approval and customer experience', 'Domestic card presentation via the MoR\'s local entity; local methods; the gamer avoids FX and foreign-purchase taxes (AR 30% perception, BR 3.5% IOF)', 'Depends on whether the acquirer treats the merchant as domestic; often still cross-border', 'Local acquiring: vendor-reported 80 to 90% approval against 30 to 60% cross-border; installments and local brands (Elo, Naranja, Carnet)', 'Retries and failover apply whichever rail is live'],
            ['Cost', 'All-in rate with FX and tax pass-through inside it (Yuno estimate 3 to 6% of sales; EBANX\'s quote replaces it)', 'Lower processing, plus Carry1st\'s own tax and compliance overhead', 'Lowest processing cost at scale; highest fixed overhead (entity, accounting, treasury)', 'More than one provider per rail keeps the rate negotiable'],
            ['When it makes sense', 'Now: six weeks to Black Friday and volumes still unproven', 'When a country sustains volume and the MoR margin exceeds the compliance cost', 'At the $4 to 5M a month run rate, Brazil and Mexico first', 'Move country by country, no re-integration']],
          'note': 'Approval ranges are vendor-reported (2017 to 2026). Tax treatment under each MoR: OPEN, owner German, requested in writing from each MoR.',
          'source': 'EBANX api-operability and pay-in guide; Healy, Commenda, BizLatinHub, TMF 2025 to 2026 (incorporation); Kintsugi 2026, Estatuto Tributario, Ley 27.430, Decree 12.499/2025, RG 5617/2024 (tax); docs.y.uno connections and routing. PUBLIC DOCS unless marked.',
          'notes': 'Merchant of record against local presence, on launch time and the long-term customer experience. The short version: the MoR launches in weeks and gives the gamer a domestic charge in local currency from day one; a local entity takes months and pays off at scale through lower processing and local acquiring. The Yuno column is the point: because the acquirer is a connection, Carry1st can make that move in Brazil first and Mexico second without touching the checkout, and keep the MoR live as fallback while it does.'})

S.append({'id': 'closing', 'type': 'closing', 'line': "Let's grow together", 'name': 'German Tatis', 'title': 'Business Development Manager, Yuno', 'phone': '+1 786 238 4554', 'email': 'german.tatis@y.uno',
          'notes': 'Thank you. German Tatis, Yuno.'})

S.append(divider('dA', 'A', 'Appendix: LatAm deep dive and sources', 'Country levers show one fifth of the base case at run rate, an equal split until volumes by country arrive.',
                 'One market slide and one connections slide per country, then the assumptions behind every modeled number and the sources. The lever cards split the base-case run-rate figures in equal fifths as a placeholder; they will be re-cut on Carry1st\'s volume projections by country.'))

# ---- Brazil
S.append(country('cty-br', 'br', 'Brazil',
    'Brazil is the launch market: Pix and domestic cards carry more than 80% of online purchases and confirm in seconds.',
    [{'value': '42%', 'label': 'Pix, share of online purchases', 'caption': 'Reuters on PCMI, Feb 2026; cards 41%'},
     {'value': '$2.5B', 'label': 'Games revenue, 100M+ players', 'caption': 'Newzoo and Allcorrect via press, 2025'},
     {'value': '93%', 'label': 'Of adults used Pix in Apr 2026', 'caption': 'Banco Central via press, May 2026'},
     {'value': '46', 'label': 'Providers live through Yuno', 'caption': 'Yuno integrations directory, Oct 2026'}],
    levers('Pix and domestic cards (Elo, Hipercard) through EBANX from day one, with more providers live on both; Boleto later.',
           'Retry EBANX card declines on a second provider; present as a domestic charge so domestic-only cards (about 70%) can pay.',
           'Pix runs on 27 providers live on Yuno; move share to the cheaper route by rule once a second one is live.'),
    [['Must-have', 'Pix', '42% of online purchases', 'Primary rail, instant confirmation', 'EBANX and 26 more on Yuno'],
     ['Must-have', 'Cards incl. Elo, Hipercard', '40 to 41% of value', 'Mainstream; installments later', 'EBANX, Adyen, Cielo, Getnet'],
     ['Optional', 'Boleto', 'Legacy cash voucher', 'Second wave; slow confirmation', 'EBANX, Mercado Pago, Pagar.me']],
    [{'title': 'Pix is the product fit', 'body': 'Confirms in seconds; 93% of adults use it.'},
     {'title': 'Domestic-only cards need a local rail', 'body': 'About 70% of Brazilian cards cannot pay cross-border.'},
     {'title': 'IOF makes the charge model matter', 'body': '3.5% IOF on international card payments; TO VALIDATE per MoR.'}],
    'Launch Brazil on Pix and local cards through the MoR; keep Boleto off at launch, and keep a second provider live behind EBANX from day one.',
    'Reuters 10 Feb 2026 (PCMI); Banco Central via press 2026; Newzoo and Allcorrect 2025; IQPC (undated); Decree 12.499/2025 (IOF); Yuno directory Oct 2026. TO VALIDATE: Boleto share 2025; IOF treatment of MoR charges (owner German).',
    'Brazil is where the Shop launches, and it is the market where the two rails that matter, Pix and domestic cards, both confirm instantly. The levers show one fifth of the base case at run rate as a placeholder until your volumes by country arrive. The one thing we would not do at launch is Boleto: it confirms late and the Shop promises instant delivery.'))

S.append(connections('cty-br-connections', 'Brazil',
    'Brazil: 46 providers live through Yuno, EBANX among them; 27 of them carry Pix and eight carry Boleto.',
    ['EBANX'], ['Apple Pay', 'Google Pay', 'PayPal', 'PIX', 'Boleto', 'NuPay', 'Visa', 'Mastercard'],
    {'columns': ['Local method', 'Carried through Yuno by', '#'], 'col_widths': [0.2, 0.74, 0.06], 'font_size': 7,
     'rows': [['Pix', 'EBANX, dLocal, Adyen, Cielo, Getnet, Mercado Pago, PagSeguro, Pagar.me, PagBank, Nuvei, Stripe, PayRetailers, Fiserv, Santander and 13 more', '27'],
              ['Boleto', 'EBANX, dLocal, Mercado Pago, Pagar.me, PagBank, Banco do Brasil, Bradesco, Bamboo', '8']]},
    'Every provider live through Yuno in Brazil, from the Yuno integrations directory. EBANX, the merchant of record at launch, is highlighted; the 46 below are the local rails and acquirers the Shop can add by routing rule, at launch or in Phase 2, without a new integration. Pix alone is carried by 27 providers, which is what makes the cost lever real.'))

# ---- Argentina
S.append(country('cty-ar', 'ar', 'Argentina',
    'Argentina is a wallet market where the 30% perception makes local pricing decisive; MODO and QR need rails beyond EBANX.',
    [{'value': '46%', 'label': 'Wallets, share of e-commerce', 'caption': 'PCMI 2024 by value; above 55% in GPR 2026'},
     {'value': '22%', 'label': 'Domestic-only credit cards', 'caption': 'PCMI 2024: cannot be charged cross-border'},
     {'value': '17M+', 'label': 'MODO users; 100M+ QR a month', 'caption': 'Play Digital 2024; Descubre, Jul 2026'},
     {'value': '30%', 'label': 'Perception on foreign cards', 'caption': 'ARCA RG 5617/2024, in force Sep 2026'}],
    levers('Mercado Pago and cards via EBANX at launch; MODO and interoperable QR through local rails on Yuno as fast follow.',
           'A local-currency charge through the MoR avoids the 30% perception; retry declines on a second provider.',
           'Cards run on 21 providers live on Yuno; move share by rule. Cash (Rapipago, Pago Fácil) stays optional.'),
    [['Must-have', 'Mercado Pago Wallet', '46 to 55% of e-commerce', 'Primary rail', 'EBANX, Mercado Pago and more'],
     ['Must-have', 'Cards incl. Naranja, Cabal', '45% of value across card lines', 'Needs local presentation', 'EBANX, Prisma, Fiserv and more'],
     ['Fast follow', 'MODO, interoperable QR', '17M+ users', 'Not available on EBANX', 'dLocal, MODO, Mercado Pago']],
    [{'title': 'Price in pesos through the MoR', 'body': 'A USD card charge costs the gamer 30% more; TO VALIDATE per MoR.'},
     {'title': 'Domestic-only cards are 22% of value', 'body': 'Cross-border rails cannot charge them at all.'},
     {'title': 'Refund timing differs by provider', 'body': 'EBANX card refunds can take 89 to 120 days (EBANX docs).'}],
    'Argentina rewards a second rail immediately: MODO and QR sit outside EBANX, and the perception rule makes local-currency pricing non-negotiable.',
    'PCMI 2024 via press; Global Payments Report 2026 via Forbes Argentina; Descubre 14 Jul 2026; ARCA RG 5617/2024 (Fortuna, 2026); Newzoo 2024 via iProUP; EBANX Argentina overview; Yuno directory Oct 2026. TO VALIDATE: perception treatment per MoR (owner German).',
    'Argentina is a wallet market, and it is the market where the rail decides the price the gamer sees: a foreign-currency card purchase carries a 30% perception that a local-currency charge through the merchant of record does not. MODO and interoperable QR are not on EBANX; through Yuno they come from local rails such as dLocal, MODO itself and Mercado Pago QR, which is the second-provider argument in one line.'))

S.append(connections('cty-ar-connections', 'Argentina',
    'Argentina: 23 providers live through Yuno; 21 carry cards, and MODO and QR come through rails beyond EBANX.',
    ['EBANX'], ['Apple Pay', 'Google Pay', 'PayPal', 'Pago Fácil', 'Rapipago', 'Visa', 'Mastercard', 'Click to Pay'],
    {'columns': ['Local method', 'Carried through Yuno by', '#'], 'col_widths': [0.22, 0.72, 0.06], 'font_size': 7,
     'rows': [['Cards', 'EBANX, dLocal, Prisma via Fiserv, Getnet, Mercado Pago, Nuvei, PayU, Worldline, Worldpay and others', '21'],
              ['Mercado Pago (Checkout Pro, Wallet)', 'EBANX (Checkout Pro), Mercado Pago (Wallet, QR, Checkout Pro), dLocal', '3'],
              ['MODO, interoperable QR', 'MODO: dLocal, MODO direct · QR: Mercado Pago', '3'],
              ['Rapipago, Pago Fácil (cash)', 'dLocal; Bamboo (Pago Fácil); EBANX and PayU (cash)', '4']]},
    'The Argentina connections live through Yuno. EBANX carries cards and Mercado Pago Checkout Pro; MODO and interoperable QR come from other rails live on Yuno (dLocal and MODO direct for MODO, Mercado Pago for QR), which is why more than one rail matters here from day one.'))

# ---- Mexico
S.append(country('cty-mx', 'mx', 'Mexico',
    'Mexico is a debit market: three in four online buyers pay with debit cards foreign acquirers decline; the MoR must look domestic.',
    [{'value': '74%', 'label': 'Online buyers using debit cards', 'caption': 'AMVO Estudio de Venta Online 2024'},
     {'value': '77M', 'label': 'Digital buyers in 2025', 'caption': 'AMVO 2026; retail e-commerce +19% in 2025'},
     {'value': '76M+', 'label': 'Players; $2.3B games revenue', 'caption': 'Endeavor México and Santander, 2025'},
     {'value': '36', 'label': 'Providers live through Yuno', 'caption': 'Yuno integrations directory, Oct 2026'}],
    levers('Debit and credit cards incl. Carnet, SPEI and OXXO Pay through EBANX; CoDi and store cash through local rails later.',
           'Local presentation lifts debit approval (Nuvei cites 20 to 30 points); retry EBANX declines on a second provider.',
           'Cards, SPEI and OXXO each run on several providers; the largest LatAm card base gives routing share real weight.'),
    [['Must-have', 'Debit and credit cards incl. Carnet', '74% and 54% usage', 'Domestic presentation, 3DS tuned', 'EBANX and 32 more on Yuno'],
     ['Must-have', 'SPEI', '8 of 10 buyers use cards or SPEI', 'Instant bank transfer', 'EBANX, Kushki, STP and 5 more'],
     ['Must-have', 'OXXO Pay and OXXO cash', 'Cash 17% of usage', 'OXXO Pay confirms faster', 'EBANX, Bamboo, PagSeguro']],
    [{'title': '16% IVA on digital services', 'body': 'Sits inside the MoR rate; TO VALIDATE per provider.'},
     {'title': 'Debit declines are structural', 'body': 'Many debit cards are blocked cross-border or fail 3DS abroad.'},
     {'title': 'The prototype already runs Mexico', 'body': 'OXXO and local prices run in the sandbox demo today.'}],
    'Mexico converts on debit and SPEI presented as domestic; a second rail matters most for failover, and for CoDi and convenience-store cash later.',
    'AMVO Estudio 2024 and 2026; Endeavor México and Santander via Forbes México 2025; Nuvei, Unlimit and Antom vendor pages 2025 to 2026 (vendor claims); Kintsugi 2026 (IVA); Yuno directory Oct 2026. TO VALIDATE: AMVO 2026 method shares; OXXO share.',
    'Mexico is the largest card base in the region and a debit market: three in four online buyers use debit, and debit is the card type most often declined when the merchant looks foreign. That is why the merchant of record has to present the charge as domestic. SPEI and OXXO Pay complete the set; CoDi and the convenience-store networks can follow through other rails live on Yuno, for example dLocal or Unlimit.'))

S.append(connections('cty-mx-connections', 'Mexico',
    'Mexico: 36 providers live through Yuno; SPEI runs on eight of them, OXXO on six and CoDi on two.',
    ['EBANX'], ['Apple Pay', 'Google Pay', 'PayPal', 'OXXO Pay', 'SPEI', 'CoDi', '7-Eleven', 'Visa', 'Mastercard', 'Kueski'],
    {'columns': ['Local method', 'Carried through Yuno by', '#'], 'col_widths': [0.22, 0.72, 0.06], 'font_size': 7,
     'rows': [['SPEI', 'EBANX, dLocal, Kushki, Nuvei, PagSeguro, STP, Unlimit, Bamboo', '8'],
              ['OXXO Pay and OXXO cash', 'EBANX (OXXO Pay), dLocal (OXXO, 7-Eleven, Paynet), Bamboo, PagSeguro, Unlimit', '6'],
              ['CoDi, Mercado Pago wallet', 'dLocal (CoDi), Mercado Pago, EBANX (Checkout Pro), Unlimit', '4']]},
    'The Mexico connections live through Yuno. EBANX carries cards, SPEI and OXXO Pay, and each of them also runs on several other providers; CoDi and the convenience-store cash networks come from local rails such as dLocal and Unlimit. The 36 providers behind them are what Phase 2 local acquiring can draw on.'))

# ---- Colombia
S.append(country('cty-co', 'co', 'Colombia',
    'Colombia is an account-to-account market: PSE carries 64% of e-commerce transactions and Bre-B is the next rail; cards a third.',
    [{'value': '63.9%', 'label': 'PSE, share of online purchases', 'caption': 'CCCE via Valora Analitik, Q2 2025'},
     {'value': '36M+', 'label': 'Bre-B users in its first year', 'caption': 'Banco de la República, 6 Oct 2026; 1.7B tx'},
     {'value': '28M', 'label': 'Nequi active users', 'caption': 'Nequi via press, May 2026'},
     {'value': '31', 'label': 'Providers live through Yuno', 'caption': 'Yuno integrations directory, Oct 2026'}],
    levers('PSE and Nequi from day one; Bre-B as fast follow through local rails on Yuno; cards on several providers.',
           'Account-to-account methods approve or fail instantly; retry card declines on a second provider.',
           'PSE runs on 12 providers live on Yuno: route by method and cost; 19% IVA handled by the MoR (TO VALIDATE).'),
    [['Must-have', 'PSE', '63.9% of transactions', 'Primary rail, instant', 'EBANX, PayU, Kushki, Wompi and more'],
     ['Must-have', 'Nequi, Bre-B', '28M and 36M users', 'Wallet and QR reach', 'Wompi, Nuvei; Bre-B: dLocal, Refacil'],
     ['Must-have', 'Cards', '33% of transactions, 43% of value', 'Local presentation', 'EBANX, Credibanco, Redeban and more']],
    [{'title': 'EBANX rails in Colombia to confirm', 'body': 'PSE Avanza and Bre-B in EBANX docs; confirm on your account.'},
     {'title': 'Significant economic presence rules', 'body': 'Local pricing can trigger PES; a MoR keeps Carry1st offshore.'},
     {'title': 'The prototype already runs Colombia', 'body': 'PSE, Nequi and Daviplata run in the sandbox demo today.'}],
    'Colombia runs on PSE today and Bre-B tomorrow; both reach the Shop through local rails live on Yuno, with cards on several providers.',
    'CCCE via Valora Analitik 24 Aug 2025; Banco de la República 6 Oct 2026; Nequi via press May 2026; Estatuto Tributario art. 20-3 and Decreto 2039/2023; EBANX Colombia overview; Yuno directory Oct 2026. TO VALIDATE: EBANX PSE Avanza and Bre-B on Carry1st\'s account; credit-card penetration 2025.',
    'Colombia moved from cards to account-to-account in three years: PSE is now two thirds of e-commerce transactions and Bre-B, the central bank\'s instant rail, passed 36 million users in its first year. Both are instant, which fits the Shop. Cards are a third of transactions and run on several providers live through Yuno.'))

S.append(connections('cty-co-connections', 'Colombia',
    'Colombia: 31 providers live through Yuno; 12 carry PSE, five carry Nequi, and Bre-B is live through local rails.',
    ['EBANX'], ['Apple Pay', 'Google Pay', 'PayPal', 'Nequi', 'Daviplata', 'Efecty', 'ADDI', 'Visa', 'Mastercard'],
    {'columns': ['Local method', 'Carried through Yuno by', '#'], 'col_widths': [0.22, 0.72, 0.06], 'font_size': 7,
     'rows': [['PSE', 'Bamboo, dLocal, EBANX, Ecommpay, Kushki, Mercado Pago, Nuvei, PagSeguro, PayU, SafetyPay, Unlimit, Wompi', '12'],
              ['Nequi, Daviplata', 'Nequi: Bamboo, dLocal, Nuvei, SafetyPay, Wompi · Daviplata: Nuvei, Wompi', '5'],
              ['Bre-B', 'dLocal, Refacil', '2'],
              ['Efecty (cash)', 'dLocal, Nuvei, PagSeguro, Unlimit', '4']]},
    'The Colombia connections live through Yuno. PSE is carried by twelve providers including EBANX; Nequi by five; Bre-B through local rails such as dLocal and Refacil today, with more providers expected as the rail matures.'))

# ---- Bolivia
S.append(country('cty-bo', 'bo', 'Bolivia',
    'Bolivia is the clearest case for a second provider: EBANX direct means cash vouchers only; local rails on Yuno add cards and QR.',
    [{'value': '36%', 'label': 'QR share of payments, 2025', 'caption': 'BCB via Los Tiempos, Jun 2026; 15% in 2020'},
     {'value': '64%', 'label': 'Cash share of payments, 2025', 'caption': 'BCB via Los Tiempos, Jun 2026; 85% in 2020'},
     {'value': '$500', 'label': 'Foreign debit-card limit a month', 'caption': 'Asoban via Los Tiempos, 9 Apr 2026'},
     {'value': '6', 'label': 'Providers live through Yuno', 'caption': 'Yuno integrations directory, Oct 2026'}],
    levers('Cards on local rails live on Yuno (for example dLocal, Nuvei, Cybersource); QR via dLocal; cash as fallback.',
           'Local processing avoids the foreign-card limit and FX; QR confirms instantly.',
           'A single-route market today: leverage comes from the pooled five-country volume, not from Bolivia alone.'),
    [['Must-have', 'QR (BCB interoperable)', '36% of payments, rising', 'Instant; confirm on dLocal', 'dLocal'],
     ['Must-have', 'Visa, Mastercard (local)', 'Foreign cards capped at $500', 'Domestic charge, no FX', 'dLocal, Nuvei, Cybersource'],
     ['Optional', 'Cash: Pago al Paso, Multipago, PagosNet', '64% of payments', 'Slow confirmation; second wave', 'dLocal, EBANX (PagosNet)']],
    [{'title': 'The second provider is the whole point', 'body': 'EBANX direct: PagosNet cash and bank only (EBANX docs).'},
     {'title': 'Cards need local processing', 'body': 'Foreign debit capped at $500 a month, FX at the daily reference rate.'},
     {'title': 'Phase the market', 'body': 'Smallest of the five; launch after Brazil, on local rails only.'}],
    'Route Bolivia to the local rails live on Yuno from day one; EBANX\'s Bolivia card coverage stays an open item, not a dependency.',
    'BCB via Los Tiempos 14 Jun 2026 and 9 Apr 2026; EBANX Bolivia overview and status.ebanx.com; docs.dlocal.com/docs/bolivia; Yuno directory Oct 2026. TO VALIDATE: QR enabled on the dLocal connection; EBANX Bolivia cards (owner Yuno integrations).',
    'Bolivia is small and it is the clearest argument for a second provider: EBANX\'s own documentation lists only PagosNet cash and bank for Bolivia, while five providers live on Yuno process Visa and Mastercard locally (dLocal, Nuvei, Cybersource, AstroPay, Inswitch), and dLocal\'s documentation lists the interoperable QR that is now a third of all payments in the country. The Yuno directory lists EBANX under Bolivia cards, which conflicts with EBANX\'s docs, so we treat it as open and route Bolivia to the local rails.'))

S.append(connections('cty-bo-connections', 'Bolivia',
    'Bolivia: six providers live through Yuno, five of them carrying cards locally; EBANX in Bolivia stays an open item.',
    [], ['PayPal', 'Visa', 'Mastercard', 'Pago al Paso'],
    {'columns': ['Method', 'Carried through Yuno by', 'Status'], 'col_widths': [0.24, 0.56, 0.20], 'font_size': 7,
     'rows': [['Cards (Visa, Mastercard)', 'AstroPay, Cybersource, dLocal, Inswitch, Nuvei', {'text': '', 'pill': 'CONFIRMED'}],
              ['QR (BCB interoperable)', 'dLocal per its docs; to confirm on the Yuno dLocal connection', {'text': 'owner German', 'pill': 'OPEN'}],
              ['EBANX in Bolivia', 'Directory lists EBANX under cards; EBANX docs show PagosNet cash and bank only', {'text': 'owner Yuno integrations', 'pill': 'OPEN'}]]},
    'Bolivia has six providers live through Yuno, and five of them process cards locally; dLocal also lists QR and cash, with QR to confirm on the Yuno connection. EBANX appears under Bolivia cards in the Yuno directory but EBANX\'s own documentation shows cash only, so we carry it as an open item and do not depend on it.',
    extra_sections=[{'header': 'Open: EBANX in Bolivia', 'style': 'request', 'chips': [chip('EBANX')]}],
    source='Yuno integrations directory, pulled 14 Oct 2026 (CONFIRMED); EBANX Bolivia overview and status.ebanx.com, docs.dlocal.com/docs/bolivia, read 15 Oct 2026 (PUBLIC DOCS). OPEN items carry an owner.'))

# ---- risks and sources
S.append({'id': 'risks', 'type': 'table', 'kicker': 'APPENDIX · RISKS AND ASSUMPTIONS', 'tag': ['ESTIMATE', 'OPEN'],
          'headline': 'Every modeled number in this deck rests on ten assumptions, each with an owner and a replacement path.',
          'columns': ['Assumption', 'Value in the deck', 'Basis and replacement', 'Owner', 'Status'], 'col_widths': [0.20, 0.24, 0.30, 0.13, 0.13], 'header_style': 'dark', 'font_size': 7, 'bold_first_col': True, 'zebra': True,
          'rows': [
            ['Run-rate volume and ticket', '450K tx, $4.5M a month; $10 / $5 ticket', 'Carry1st, Cordel, Oct 2026; not aligned internally', 'Cordel', {'text': '', 'pill': 'ESTIMATE'}],
            ['Launch volume and ramp', '50K a month, linear to 450K by Dec 2027', 'Yuno placeholder until volumes by country arrive', 'Cordel', {'text': '', 'pill': 'OPEN'}],
            ['EBANX direct all-in cost', '4.5% of sales (range 3 to 6%)', 'Yuno estimate; EBANX\'s quote to Carry1st replaces it', 'Cordel', {'text': '', 'pill': 'ESTIMATE'}],
            ['Carry1st take rate on GMV', '15%', 'Yuno estimate; to validate with Shop margins', 'Cordel', {'text': '', 'pill': 'ESTIMATE'}],
            ['Approval uplift, second provider', '+1.5 / +3.0 / +5.0 points', 'Yuno estimate under the published 7% ceiling', 'Cordel, Yuno', {'text': '', 'pill': 'ESTIMATE'}],
            ['MDR reduction, routing leverage', '25 / 50 / 75 bps of sales', 'Yuno estimate; provider rates through Yuno pending', 'Yuno', {'text': '', 'pill': 'OPEN'}],
            ['Provider onboarding time', 'Weeks; no published SLA', 'Provider docs; run onboardings in parallel', 'Cordel, Yuno lead', {'text': '', 'pill': 'PUBLIC DOCS'}],
            ['EBANX cards in Bolivia', 'Not assumed; Bolivia on local rails', 'Yuno directory says cards; EBANX docs say cash only', 'Yuno integrations', {'text': '', 'pill': 'OPEN'}],
            ['Second MoR per market', 'Chosen per market', 'Coverage and price per market, with Carry1st', 'Justo', {'text': '', 'pill': 'OPEN'}],
            ['Tax treatment under each MoR', 'Domestic charge; taxes in the MoR rate', 'Not documented publicly; requested in writing', 'German', {'text': '', 'pill': 'OPEN'}]],
          'source': 'model/bc_numbers.md, Section D (Yuno, 15 Oct 2026); research files of the same date.',
          'notes': 'This is the list of everything we assumed, with the value we used, where it came from, who owns the replacement and its status. Nothing on it is hidden inside a chart. The two that move the business case most are the EBANX all-in rate and your take rate; both are yours to replace, and the model is built so that swapping them re-cuts every slide in section 05.'})

S.append({'id': 'sources', 'type': 'sources', 'kicker': 'APPENDIX · SOURCES',
          'headline': 'Every page behind this deck, read on 15 October 2026 unless dated otherwise.',
          'cols': [{'header': 'YUNO AND THE MODEL', 'pill': 'CONFIRMED', 'items': [
                      'docs.y.uno · Connections; Routing and routing resource shape; Monitors; Automation (retries); Tokens, network tokens, PCI compliance, stored credentials; Provider installments; Insights; Reconciliations; AI capabilities; SDK overview',
                      'y.uno · Homepage (up to 7% uplift, 30% recovered revenue, 1,000+ methods, PSPs and fraud solutions); About (16 offices, 190+ countries, 180+ currencies, certifications); success stories: inDrive (10 Sep 2024), Rappi (21 Nov 2024), McDonald\'s (18 Feb 2025)',
                      'Yuno integrations directory · docs.y.uno Payment Type list and y.uno/integrations, pulled 14 Oct 2026 (providers and methods per country, logos)',
                      'Carry1st Shop prototype on the Yuno SDK · Yuno sandbox, 15 Oct 2026 (four LatAm markets)',
                      'Yuno business-case model · bc_model.xlsx, 15 Oct 2026: four volumes, three scenarios, small-ticket sensitivity; every assumption on the risks slide']},
                   {'header': 'CARRY1ST, PROVIDERS AND MARKETS', 'pill': 'PUBLIC DOCS', 'items': [
                      'Carry1st · carry1st.com, shop.carry1st.com and sitemap, press releases 2021 to 2026, App Store listing, BITKRAFT job post 28 Jul 2026, TechCabal, TechCrunch, GlobeNewswire 29 Jan 2024',
                      'EBANX · docs.ebanx.com (api-operability, pay-in guide, payment methods, country overviews BR, MX, CO, AR, BO, DEUNA page, FAQ); ebanx.com; business.ebanx.com press room; status.ebanx.com',
                      'Local rails · provider country pages for Argentina, Mexico, Colombia and Bolivia methods (docs.dlocal.com and others), read 15 Oct 2026',
                      'Brazil · Reuters 10 Feb 2026 (PCMI); Banco Central via press 2026; Newzoo, Allcorrect 2025; Decree 12.499/2025 and ARQ Finance 29 Sep 2026 (IOF); VATCalc, Fonoa 2026',
                      'Argentina · PCMI 2024; Global Payments Report 2026 via Forbes Argentina; Descubre 14 Jul 2026; Fortuna 2026 and ARCA RG 5617/2024; Ley 27.430; Newzoo 2024 via iProUP',
                      'Mexico · AMVO Estudio 2024 and 2026; Endeavor México and Santander 2025 via Forbes México; Nuvei, Unlimit, Antom pages; Kintsugi 2026 (IVA); BizLatinHub, Commenda',
                      'Colombia · CCCE via Valora Analitik 24 Aug 2025; Banco de la República 6 Oct 2026; Nequi via press May 2026; Estatuto Tributario art. 20-3, Decreto 2039/2023',
                      'Bolivia · BCB via Los Tiempos 14 Jun 2026 and 9 Apr 2026 (Asoban); Ministerial Resolution 245/2026 (exchange rate); AGN 2026 tax card',
                      'Approval ranges · Worldline, Rapyd, Nuvei, Antom, EBANX 11 Sep 2017 (AMI); vendor-reported, 2017 to 2026']}],
          'footnote': 'Third-party lines are our reading of public pages on the dates shown; confirm each with the provider before relying on it. Carry1st call figures are estimates until confirmed.',
          'notes': 'Appendix. The pages behind every claim, so your team can open them. Yuno claims come from our public documentation, y.uno and the model in this deck; provider and market lines come from their own public pages or dated press, and we would rather you confirm them with each provider than take our reading.'})

SPEC = {'presentation_id': PID, 'merchant': 'Carry1st', 'footer': '', 'slides': S}
out = os.path.join(HERE, 'deck_spec.json')
json.dump(SPEC, open(out, 'w'), ensure_ascii=False, indent=1)
print(f'wrote {out}: {len(S)} slides')
