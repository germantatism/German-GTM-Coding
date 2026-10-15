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
SECTIONS = ['01 Executive summary', '02 Where Carry1st stands and what Black Friday needs', '03 Two ways to launch', '04 Why Yuno',
            '05 Business case', '06 Proposal', '07 Launch plan to Black Friday and Phase 2', '08 Next steps', 'Appendix: LatAm deep dive and sources']

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
    secs = [{'header': 'Merchant-of-record routes for the launch', 'style': 'signed', 'chips': [chip(m) for m in mor]}]
    secs += extra_sections or []
    secs += [{'header': hdr, 'chips': chips}, {'header': 'Wallets and payment methods (selected)', 'chips': method_chips(methods)}]
    s = {'id': id_, 'type': 'logo_grid', 'kicker': f'APPENDIX · {name.upper()} · CONNECTIONS THROUGH YUNO', 'headline': headline, 'sections': secs,
         'source': source or 'Yuno integrations directory (docs.y.uno Payment Type list and y.uno/integrations), pulled 14 Oct 2026. CONFIRMED. Logos are the providers\' own marks.', 'notes': notes}
    if table: s['table'] = table
    return s

# ---------------------------------------------------------------- the deck
S = []

S.append({'id': 'cover', 'type': 'cover', 'title': 'Carry1st Shop in Latin America by Black Friday',
          'subtitle': 'One integration, two merchant-of-record providers, and the economics that work at a $10 ticket',
          'presenter': 'German Tatis, Yuno · 16 October 2026',
          'notes': 'Cordel, Fatih: this deck answers the three things you asked for on the discovery call, the economics, pricing that works for small purchases, and how Yuno fits alongside EBANX, plus Fatih\'s two, checkout demos and merchant of record against local presence. Every number carries its label: confirmed in public documentation, read on a third party\'s public page, a Yuno estimate with the assumption stated, or open with an owner. The appendix holds the market detail for each of the five countries.'})

S.append({'id': 'agenda', 'type': 'agenda', 'items': [{'num': '01', 'title': 'Executive summary'}, {'num': '02', 'title': 'Where Carry1st stands and what Black Friday needs'},
          {'num': '03', 'title': 'Two ways to launch'}, {'num': '04', 'title': 'Why Yuno'}, {'num': '05', 'title': 'Business case'}, {'num': '06', 'title': 'Proposal'},
          {'num': '07', 'title': 'Launch plan to Black Friday and Phase 2'}, {'num': '08', 'title': 'Next steps'}, {'num': 'A', 'title': 'Appendix: LatAm deep dive and sources'}],
          'notes': 'Thirty minutes: the executive summary and the two ways to launch first, then the business case and the proposal, then the launch plan. The appendix is for Fatih\'s team to read afterwards.'})

S.append(divider('d01', '01', 'Executive summary', 'The decision, the recommended path, and what it returns at launch and at run rate',
                 'One slide: the decision in front of Carry1st, what Yuno proposes, and what it is worth at launch volume and at the end-2027 run rate.'))

S.append({'id': 'exec', 'type': 'exec_summary', 'kicker': 'EXECUTIVE SUMMARY', 'tag': ['ESTIMATE'],
          'headline': 'Through Yuno, EBANX and dLocal cost less than EBANX direct at run rate, add a second rail, and pay back in month two.',
          'left_header': 'WHERE CARRY1ST STANDS',
          'left_items': [
            {'title': 'The decision', 'body': 'Launch the Carry1st Shop in Brazil, Argentina, Mexico, Colombia and Bolivia by Black Friday, 27 November 2026, through a merchant of record: EBANX direct, or EBANX and dLocal through Yuno.'},
            {'title': 'The economics to beat', 'body': 'A $10 average and $5 median ticket, so every fixed fee per transaction is punished; $4 to 5M a month in LatAm by end 2027 (Carry1st, Cordel, Oct 2026, estimate).'},
            {'title': 'What EBANX direct gives', 'body': 'One agreement and one integration for all five countries once EBANX enables each; but one approval rate, one price, Bolivia cash only, no MODO.'},
            {'title': 'What is still open', 'body': 'Volumes by country, EBANX\'s proposed rates, Carry1st\'s take rate and the tax treatment under each MoR. Every modeled number in this deck carries its label and an owner.'}],
          'right_header': 'WHAT YUNO PROPOSES',
          'right_cards': [
            {'title': 'One integration, two merchants of record', 'body': 'EBANX primary, dLocal second, both as connections on the Yuno SDK: retries and failover between them, local methods per market, Phase 2 local acquirers without touching checkout.'},
            {'title': 'A fee that scales with sales, not with transactions', 'body': '$7,500 a month including the first $500K of monthly sales, then 30 / 25 / 20 bps on sales above it. At launch: $7,500 and nothing per transaction; at $4.5M: $18,750 a month, 0.42% of sales.'},
            {'title': 'A case that pays back in month two', 'body': 'Base case at run rate: $44.2 per $1,000 of sales through Yuno against $45.0 direct, +$29.1K a month net ($349K a year, 2.6x Yuno\'s cost); break-even about 65,000 transactions a month.'}],
          'bottom': 'Decide by 23 Oct, onboard EBANX and dLocal in parallel, launch Brazil by 27 Nov; the conservative case is cost-neutral at run rate.',
          'source': 'Yuno business-case model, 15 Oct 2026, base scenario: EBANX direct all-in 4.5% of sales and a 15% take rate are estimates, replaced by EBANX\'s quote and Shop margins. Volumes: Carry1st, Cordel, Oct 2026, estimate.',
          'notes': 'The whole deck on one slide. Left, where you stand: five markets, six weeks, a $5 median ticket and a run-rate estimate that is yours. Right, what we propose: one integration carrying EBANX and dLocal, a fee that is a share of what you sell with the first $500K of monthly sales inside the platform fee, and a business case that, in the base scenario, makes the Yuno route the cheaper cost line at run rate before counting approval or coverage gains. Two numbers to keep: break-even at about 65,000 transactions a month, and the conservative case cost-neutral at run rate. Everything modeled is labelled and will be re-cut on your volumes and EBANX\'s quote.'})

S.append(divider('d02', '02', 'Where Carry1st stands and what Black Friday needs', 'What we heard, the Shop and the plan, and what the five markets demand',
                 'Section 02 restates what we heard from Cordel and Fatih, sizes the plan as you described it, and shows what the five markets require of a checkout.'))

S.append({'id': 'heard', 'type': 'two_column', 'kicker': 'WHERE CARRY1ST STANDS · WHAT WE HEARD',
          'headline': 'Three asks from Cordel and two from Fatih set the bar for this deck; each one has a section that answers it.',
          'cols': [{'header': "CORDEL'S THREE ASKS", 'items': [
                      {'title': 'Demonstrate the economics', 'body': 'Show how processing savings, improved conversion and reduced engineering work justify Yuno\'s additional fee. Answered in section 05.'},
                      {'title': 'Make pricing work for small purchases', 'body': 'The average ticket is about $10 and the median closer to $5, so fixed transaction fees are especially sensitive. Answered in sections 05 and 06.'},
                      {'title': 'Clarify the EBANX arrangement', 'body': 'How working with Yuno fits alongside EBANX, including starting through a particular provider or integrating directly. Answered in section 03.'}]},
                   {'header': "FATIH'S TWO ASKS", 'items': [
                      {'title': 'Checkout demos', 'body': 'A working prototype of the Shop checkout on the Yuno SDK, checkout examples and test access to a live gaming checkout. Answered in section 04 and in the live demo.'},
                      {'title': 'Merchant of record versus local presence', 'body': 'Launch timelines and the longer-term customer experience under each model. Answered in section 07.'}]}],
          'bar': 'Everything else in this deck exists to answer these five questions; the appendix carries the market detail behind the answers.',
          'source': 'Discovery call between Carry1st and Yuno, October 2026, as summarized by Yuno.',
          'notes': 'We wrote down your five asks as close to verbatim as we could, so you can check that the deck answers what you actually asked rather than what we wanted to pitch. If we misheard any of them, this is the slide to correct.'})

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
          'bar': 'Six weeks to Black Friday: provider contracts and KYC are the critical path; the Yuno integration itself is measured in days (Yuno estimate, section 07).',
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
                          {'title': 'Taxes follow the rail', 'body': 'Argentina adds a 30% perception on foreign-currency card purchases; Brazil charges 3.5% IOF on international card payments. A local-currency charge through the MoR\'s local entity is domestic for the gamer. TO VALIDATE with EBANX and dLocal.'},
                          {'title': 'Bolivia and Argentina need a second provider', 'body': 'EBANX lists only PagosNet cash in Bolivia and no MODO or interoperable QR in Argentina; dLocal carries cards, QR and MODO there.'}],
          'bar': 'The Shop\'s African playbook, local methods in local currency, is exactly what LatAm requires; the open question is which rail carries it.',
          'source': 'Reuters on PCMI data, 10 Feb 2026; CCCE via Valora Analitik, 24 Aug 2025; PCMI 2024 data; AMVO Estudio 2024; approval ranges are vendor-reported (Worldline, Rapyd, Nuvei, Antom, EBANX, 2017 to 2026); ARCA RG 5617/2024; Decree 12.499/2025. PUBLIC DOCS.',
          'notes': 'Four numbers, one per market, and they point the same way: the winning method is local and it confirms instantly. Pix in Brazil, PSE in Colombia, wallets in Argentina and debit cards in Mexico are the rails the Shop needs on day one. The approval ranges on the right are vendor claims, not independent studies, so we show them as ranges and label them; the direction is not in dispute. The two tax lines explain why a local-currency charge through a merchant of record matters for the gamer, and both are items we will confirm in writing with EBANX and dLocal.'})

S.append(divider('d03', '03', 'Two ways to launch', 'EBANX direct, or EBANX and dLocal through Yuno',
                 'The decision in one grid, then a picture of how Yuno sits alongside EBANX.'))

S.append({'id': 'options', 'type': 'comparison_grid', 'kicker': 'TWO WAYS TO LAUNCH · THE COMPARISON', 'tag': ['PUBLIC DOCS', 'CONFIRMED'],
          'headline': 'EBANX direct can switch on all five markets with one integration; what it cannot give Carry1st is a second rail.',
          'legend': ['Gap stays open', 'Partly closed', 'Closed'], 'row_header': 'WHAT THE LAUNCH NEEDS', 'row_header_sub': 'Six rows that decide the economics',
          'options': [{'header': 'EBANX direct', 'sub': 'TODAY\'S DEFAULT'}, {'header': 'EBANX plus a second direct build', 'sub': 'OPTION A'}, {'header': 'EBANX and dLocal through Yuno', 'sub': 'OPTION B · RECOMMENDED'}],
          'rows': [
            {'label': 'Integrations to build', 'sub': 'now, and when a second provider arrives', 'cells': [
                {'state': 'partial', 'text': 'One now. Each later provider is a new build.'},
                {'state': 'open', 'text': 'Two now; a third provider means a third build.'},
                {'state': 'closed', 'text': 'One now. EBANX, dLocal and later providers are connections.'}]},
            {'label': 'Countries on one integration', 'sub': 'Brazil, Argentina, Mexico, Colombia, Bolivia', 'cells': [
                {'state': 'partial', 'text': 'All five once EBANX enables each; Bolivia cash only.'},
                {'state': 'closed', 'text': 'All five; dLocal adds Bolivia cards, Argentina MODO.'},
                {'state': 'closed', 'text': 'All five, same coverage, one integration.'}]},
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
          'closing_line': 'One integration either way; through Yuno it carries EBANX, dLocal and the path to local acquiring.',
          'source': 'EBANX docs (api-operability, DEUNA partner page, pay-in guide, Bolivia and Argentina overviews) and status.ebanx.com, read 15 Oct 2026 (PUBLIC DOCS); docs.y.uno connections, routing, monitors, tokens (CONFIRMED). Yuno setup time is a Yuno estimate.',
          'notes': 'We start with the honest answer to your question. One EBANX integration and one agreement can switch on all five countries: the country is a field in the request, and EBANX enables each country on your account during onboarding, with sandbox tests per country and an integration review before production. So EBANX direct is a real option and we say so. What it cannot give you is a second rail: no retry on a decline, no failover in an outage, no cards or QR in Bolivia, no MODO in Argentina, and one counterparty on price. The middle column shows what it costs to fix that with a second direct build. The right column is the same fix as a routing rule.'})

S.append({'id': 'arrangement', 'type': 'diagram', 'kicker': 'TWO WAYS TO LAUNCH · HOW YUNO SITS ALONGSIDE EBANX',
          'headline': 'Yuno sits between the Shop and both merchants of record: EBANX for what it covers, dLocal for what it does not, one integration.',
          'boxes': [
            {'id': 'l1', 'x': 0, 'y': 0, 'w': 200, 'h': 12, 'style': 'label', 'title': 'CARRY1ST'},
            {'id': 'shop', 'x': 0, 'y': 13, 'w': 420, 'h': 36, 'style': 'outline', 'title': 'Carry1st Shop · web and app', 'body': 'Same checkout in every market; Spanish and Portuguese; instant delivery after confirmation'},
            {'id': 'yuno', 'x': 0, 'y': 66, 'w': 420, 'h': 62, 'style': 'blue', 'title': 'Yuno · one integration', 'pill': 'Rules set by Carry1st',
             'body': 'Checkout and SDK with local methods per market · routing and retries · Monitors and failover · vault with portable tokens · one dashboard and reconciliation'},
            {'id': 'l2', 'x': 0, 'y': 144, 'w': 300, 'h': 12, 'style': 'label', 'title': 'MERCHANTS OF RECORD · YOUR CONTRACTS, YUNO HOLDS THE CREDENTIALS'},
            {'id': 'ebanx', 'x': 0, 'y': 158, 'w': 135, 'h': 66, 'style': 'light', 'title': 'EBANX · primary MoR', 'body': 'Brazil, Mexico, Colombia, Argentina: cards, Pix, OXXO Pay, SPEI, PSE, Nequi, Checkout Pro', 'pill': 'CONFIRMED'},
            {'id': 'dlocal', 'x': 142, 'y': 158, 'w': 135, 'h': 66, 'style': 'light', 'title': 'dLocal · second MoR', 'body': 'Bolivia cards, QR and cash; Argentina MODO and QR; Mexico CoDi; failover in every market', 'pill': 'CONFIRMED'},
            {'id': 'local', 'x': 284, 'y': 158, 'w': 136, 'h': 66, 'style': 'panel', 'title': 'Phase 2 · local acquirers', 'body': 'Local entity or non-resident account per country, added as a connection and routed by country', 'pill': 'LATER'},
            {'id': 'note', 'x': 0, 'y': 231, 'w': 420, 'h': 36, 'style': 'panel', 'title': 'One agreement per provider, one integration for all of them', 'body': 'Carry1st signs and completes KYC with EBANX and with dLocal; both become connections on the same checkout.'}],
          'connectors': [{'from': 'shop', 'to': 'yuno'}, {'from': 'yuno', 'to': 'ebanx'}, {'from': 'yuno', 'to': 'dlocal'}, {'from': 'yuno', 'to': 'local', 'label': 'later'}],
          'side': {'header': 'WHAT THIS ARRANGEMENT GIVES CARRY1ST', 'items': [
              {'title': 'One integration unlocks every MoR', 'body': 'EBANX for what it covers, dLocal for what it does not. Both are connections on the same checkout, with the rest of Yuno\'s catalog behind them for Phase 2.'},
              {'title': 'One dashboard, one reconciliation', 'body': 'Approval by provider and country, retries, settlements and chargebacks in one console; Payment Concierge answers questions in Slack.'},
              {'title': 'MoR swap insurance', 'body': 'If EBANX pricing or service slips, Brazil moves to dLocal by routing rule, not by sprint. Card tokens stay in Yuno\'s vault; cash methods have nothing to tokenize.'}]},
          'source': 'docs.y.uno connections, routing, monitors, tokens (CONFIRMED); EBANX and dLocal country pages, read 15 Oct 2026 (PUBLIC DOCS). EBANX card coverage in Bolivia: OPEN, owner Yuno integrations.',
          'notes': 'This is the arrangement Cordel asked us to clarify. Carry1st keeps a direct agreement with EBANX and signs one with dLocal; Yuno never sits in the money flow. What changes is the integration: the Shop talks to one SDK, and EBANX and dLocal are credentials entered as connections, with routing rules deciding which one carries each payment. The Phase 2 box is the point for Fatih: when a country justifies a local entity, the local acquirer is one more connection and the checkout does not change.'})

S.append(divider('d04', '04', 'Why Yuno', 'Requirement, benefit, proof: what the Shop needs, what it gets, how we show it',
                 'Section 04 is the value proposition in the order you would check it: what the Shop needs, what each need gets through Yuno, and the proof behind it.'))

S.append({'id': 'why-rbp', 'type': 'table', 'kicker': 'WHY YUNO · REQUIREMENT, BENEFIT, PROOF', 'tag': ['CONFIRMED'],
          'headline': 'Seven things the Shop needs in Latin America, what each one gets through Yuno, and how we prove it.',
          'columns': ['Requirement', 'Benefit for the Shop', 'Proof', 'Label'], 'col_widths': [0.22, 0.36, 0.32, 0.10], 'header_style': 'dark', 'font_size': 7, 'bold_first_col': True, 'zebra': True,
          'rows': [
            ['One integration for five countries', 'EBANX and dLocal as connections on one SDK; later providers and local acquirers added without touching checkout', 'Connections are credentials entered in the dashboard or by API; Rappi: new-provider implementation time down to zero', {'text': '', 'pill': 'CONFIRMED'}],
            ['Local methods per market', 'Pix, PSE, Nequi, Bre-B, SPEI, OXXO Pay, CoDi, MODO, Rapipago, QR in Bolivia and wallets, returned per country by the checkout session', 'Yuno directory, Oct 2026: 46 providers live in Brazil, 36 in Mexico, 31 in Colombia, 23 in Argentina, 6 in Bolivia', {'text': '', 'pill': 'CONFIRMED'}],
            ['Higher approval, fewer lost sales', 'A decline on EBANX retries on dLocal; routing by BIN, brand, amount and country; Smart Routing as data builds', 'Published across Yuno merchants: up to 7% authorization uplift, 30% recovered revenue. Carry1st uplift modeled at +1.5 to +5 points', {'text': '', 'pill': 'CONFIRMED'}],
            ['No single point of failure', 'Monitors move traffic to the fallback provider when approval drops, and move it back on recovery', 'docs.y.uno monitors and automation; status.ebanx.com shows degradations and daily maintenance windows', {'text': '', 'pill': 'CONFIRMED'}],
            ['Cost that scales with a $5 median', 'Two MoRs on one checkout make the MDR negotiable; Yuno is billed as a share of what Carry1st sells, never a fixed fee per transaction', 'Business case in section 05 and the proposal in section 06', {'text': '', 'pill': 'ESTIMATE'}],
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

S.append(divider('d05', '05', 'Business case', 'EBANX direct against EBANX and dLocal through Yuno, at four volumes and three scenarios',
                 'Three slides: both options at four volumes, three scenarios with the levers, and why the shape of the fee matters at a $5 median ticket.'))

S.append({'id': 'bc-tiers', 'type': 'bar_chart', 'kicker': 'BUSINESS CASE · BOTH OPTIONS AT FOUR VOLUMES', 'tag': ['ESTIMATE'],
          'headline': 'The Yuno route costs $44.2 per $1,000 of sales at run rate against $45.0 direct, and covers its fee from about 65K transactions.',
          'unit': '$K',
          'series': [{'name': 'Option A · EBANX direct', 'color': '#B0B7F2'}, {'name': 'Option B · EBANX and dLocal through Yuno, provider plus fee', 'color': '#344FE0'}, {'name': 'Net benefit, base case', 'color': '#1F8A5B'}],
          'groups': [{'label': '50K tx a month', 'sub': '$0.5M of sales', 'values': [22.5, 27.5, 0], 'labels': ['$22.5K', '$27.5K', '($1.1K)']},
                     {'label': '100K', 'sub': '$1.0M', 'values': [45.0, 49.0, 2.6], 'labels': ['$45.0K', '$49.0K', '+$2.6K']},
                     {'label': '200K', 'sub': '$2.0M', 'values': [90.0, 92.0, 9.9], 'labels': ['$90.0K', '$92.0K', '+$9.9K']},
                     {'label': '450K', 'sub': '$4.5M', 'values': [202.5, 198.8, 29.1], 'labels': ['$202.5K', '$198.8K', '+$29.1K']}],
          'note': 'Monthly, USD thousands. Option A: all-in 4.5% of sales (Yuno estimate, range 3 to 6%, replaced by EBANX\'s quote). Option B: provider cost after a 50 bps routing saving, plus Yuno\'s fee. Net benefit: base case, contribution view at a 15% take rate (estimate), after Yuno\'s fee.',
          'side': {'header': 'COST PER $1,000 OF SALES', 'items': [
              {'title': 'EBANX direct', 'body': '$45.0 at every volume: one rate, one rail.'},
              {'title': 'Through Yuno, provider plus fee', 'body': '$55.0 at 50K · $49.0 at 100K · $46.0 at 200K · $44.2 at 450K. Yuno alone: $7.5K, $9.0K, $12.0K and $18.8K a month.'},
              {'title': 'Through Yuno, after all levers', 'body': '$47.3 · $42.5 · $40.1 · $38.5 per $1,000 of sales (base case).'},
              {'title': 'Break-even', 'body': 'About 65,000 transactions a month ($0.65M of sales) in the base case; about 29,000 optimistic; about 269,000 conservative.'}]},
          'bar': 'At launch (50K a month) the base case is ($1.1K) a month: Carry1st pays about $1.1K net for failover, a second provider in play and local-method coverage until volume passes about 65,000 transactions a month.',
          'source': 'Yuno business-case model (bc_model.xlsx), 15 Oct 2026. Volumes: Carry1st, Cordel, Oct 2026, estimate. Every assumption is on the risks slide in the appendix. ESTIMATE.',
          'notes': 'Both options at the four volumes you gave us. The light bars are EBANX direct at an all-in 4.5% of sales, which is our estimate until EBANX\'s quote replaces it. The blue bars are EBANX and dLocal through Yuno: the provider cost after a 50 basis-point routing saving, plus Yuno\'s fee. At launch the Yuno route costs about $5K more a month and the net, after the approval and coverage levers, is about $1.1K negative. From about 65,000 transactions a month the net turns positive, and at run rate the Yuno route is the cheaper cost line before any revenue lever is counted.'})
S.append({'id': 'bc-scenarios', 'type': 'table', 'kicker': 'BUSINESS CASE · THREE SCENARIOS AND THE LEVERS', 'tag': ['ESTIMATE', 'CONFIRMED'],
          'headline': 'Processing savings carry the case, then engineering avoided, then approval: the base case returns $29.1K a month net at run rate.',
          'columns': ['Monthly, contribution view', 'Conservative', 'Base', 'Optimistic'], 'col_widths': [0.37, 0.21, 0.21, 0.21], 'header_style': 'dark', 'font_size': 7.5, 'bold_first_col': True, 'zebra': True,
          'rows': [
            ['1 · Processing saving at 450K (second MoR, volume routed to the cheaper rail)', '$11.3K', '$22.5K', '$33.8K'],
            ['2 · Engineering avoided (direct integrations not built, 24-month equivalent)', '$0.5K', '$1.5K', '$3.2K'],
            ['3 · Approval, retries and failover at 450K (contribution on recovered sales)', '$9.3K ($90K of sales)', '$19.1K ($180K of sales)', '$32.5K ($300K of sales)'],
            ['4 · Local-method coverage at 450K (contribution on incremental sales)', '$2.3K ($22.5K)', '$4.8K ($45K)', '$9.8K ($90K)'],
            ['Gross benefit at 450K against Yuno\'s $18.8K', '$23.3K · 1.2x', '$47.8K · 2.6x', '$79.2K · 4.2x'],
            [{'text': 'Net at 450K, a month · a year', 'bold': True}, {'text': '+$4.6K · +$55K', 'bold': True}, {'text': '+$29.1K · +$349K', 'bold': True}, {'text': '+$60.5K · +$725K', 'bold': True}],
            ['Net at launch (50K), a month', '($4.6K)', '($1.1K)', '+$3.7K'],
            ['Break-even · cumulative payback on the ramp', 'about 269K tx · after Dec 2027', 'about 65K tx · Jan 2027', 'about 29K tx · Dec 2026'],
            ['Break-even by gross margin (41.7 bps all-in at run rate)', '+4.2% more approved sales at a 10% margin', '+2.8% at a 15% margin', '+2.1% at 20%; published Yuno uplift up to 7%']],
          'note': 'Levers: MDR 25 / 50 / 75 bps; 1 / 2 / 3 integrations avoided; +1.5 / +3.0 / +5.0 pts approval on a 75% baseline; +0.5 / 1.0 / 2.0% local-method sales; 15% take rate (estimate). Yuno model, 15 Oct 2026.',
          'source': 'Yuno business-case model, 15 Oct 2026 (ESTIMATE, assumptions on the risks slide). Published Yuno uplift: y.uno, read 15 Oct 2026 (CONFIRMED).',
          'notes': 'Resale margins are thin, so we did not build this case on conversion. The first lever is a processing saving: with two merchants of record live on the same checkout, volume moves to the cheaper rail by rule, and a saving on processing is worth one hundred cents on the dollar. The second is the engineering you do not build. Approval and coverage come third and are counted at your margin, not at face value. The last row is the test a CFO applies: at 41.7 basis points all-in, the fee pays for itself with about 4% more approved sales at a 10% margin, half that at 20%, against a published uplift of up to 7%.'})
S.append({'id': 'bc-ticket', 'type': 'table', 'kicker': 'BUSINESS CASE · SMALL-TICKET SENSITIVITY', 'tag': ['ESTIMATE'],
          'headline': 'A fixed fee doubles as a share of sales when the ticket halves; a share of sales does not: usage on a $5 purchase is one to two cents.',
          'columns': ['Yuno all-in at 450,000 transactions a month', '$5 median ticket', '$10 average ticket', '$15 ticket'], 'col_widths': [0.37, 0.21, 0.21, 0.21], 'header_style': 'dark', 'font_size': 7.5, 'bold_first_col': True, 'zebra': True,
          'rows': [
            ['Sales a month', '$2.25M', '$4.5M', '$6.75M'],
            ['Yuno a month (platform fee plus usage)', '$12.8K', '$18.8K', '$24.0K'],
            [{'text': 'Yuno as a share of sales', 'bold': True}, {'text': '0.57%', 'bold': True}, {'text': '0.42%', 'bold': True}, {'text': '0.36%', 'bold': True}],
            ['Yuno per successful transaction, all-in', '$0.028', '$0.042', '$0.053'],
            ['Marginal usage per transaction by band (30 / 25 / 20 bps)', '$0.015 / $0.0125 / $0.010', '$0.030 / $0.025 / $0.020', '$0.045 / $0.0375 / $0.030'],
            ['A fixed $0.05 per transaction, as a share of sales', '1.00%', '0.50%', '0.33%'],
            ['A fixed $0.10 per transaction, as a share of sales', '2.00%', '1.00%', '0.67%'],
            ['At launch, 50,000 transactions a month: Yuno all-in', '$7.5K · 3.00% of sales', '$7.5K · 1.50%', '$8.3K · 1.10%']],
          'note': 'The platform fee is the one fixed element, so at launch and a $5 ticket it is 3.00% of sales; the structure pays off as volume ramps. Yuno business-case model, 15 Oct 2026; tickets: Carry1st, Cordel, Oct 2026 (estimate).',
          'source': 'Yuno business-case model (bc_model.xlsx), Pricing and Sensitivity sheets, 15 Oct 2026. Ticket profile: Carry1st, Cordel, Oct 2026, estimate.',
          'notes': 'Cordel asked us to make pricing work for small purchases, so here is the same 450,000 transactions at three tickets. A fixed fee is blind to the ticket: five cents is 0.5% of a $10 sale and 1% of a $5 sale, ten cents twice that. Yuno\'s usage is a share of what you sell, so on a $5 purchase the marginal cost is one to one and a half cents, and all-in at run rate 0.57% of sales. We are upfront about the one fixed element: at launch volume and a $5 ticket the platform fee alone is 3% of sales, and the structure earns its keep as volume ramps rather than in month one.'})

S.append(divider('d06', '06', 'Proposal', 'A platform fee and a share of what Carry1st sells, never a fee per transaction',
                 'The commercial proposal on one slide, followed by what Yuno puts in before signing and what the platform fee already covers.'))

S.append({'id': 'proposal', 'type': 'pricing_cards', 'kicker': 'PROPOSAL',
          'headline': 'One platform fee covering the first $500K of monthly sales, then a share of sales that falls as Carry1st grows.',
          'subline': '$7,500 a month covering the first $500K of monthly sales, plus a share of the sales above it: $18,750 a month at 450,000 transactions, 0.42% of sales.',
          'left': {'title': 'TRANSACTION FEE', 'sub': 'A share of the month\'s sales above the included block, pooled across the five markets',
                   'rows': [{'label': 'INCLUDED', 'range': 'First $500K of monthly sales', 'rate': '$0'}, {'label': 'TRANCHE 1', 'range': '$500K to $3M', 'rate': '0.30%'}, {'label': 'TRANCHE 2', 'range': '$3M to $6M', 'rate': '0.25%'}, {'label': 'TRANCHE 3', 'range': 'Above $6M', 'rate': '0.20%'}],
                   'note': 'No setup fee, no fixed amount per transaction. Only successful transactions count: declines are not billed. Each tranche applies only to the volume inside it.'},
          'middle': {'title': 'PLATFORM FEE', 'value': '$7,500', 'unit': '/ month', 'sub': '$90,000 a year. Covers the first $500K of monthly sales. This is what covers the stack.',
                     'includes_label': 'WHAT IT INCLUDES',
                     'includes': [['Orchestration and rules engine', 'Included'], ['Smart routing and retries', 'Included'], ['Monitors and auto-failover', 'Included'], ['Methods, PSPs, fraud solutions', '1,000+'], ['Checkout, web and mobile SDKs', 'Included'], ['PCI token vault', 'Included'], ['Dashboard and insights', 'Included'], ['Dedicated KAM and TAM', 'Included']],
                     'addons': {'title': 'ADD-ONS', 'sub': 'Billed on usage, quoted separately, not in the totals on this slide.', 'rows': [['Network tokens', 'On usage'], ['3DS authentication', 'On usage']]},
                     'foot': 'Every integration maintained by Yuno. Adding dLocal, a local acquirer or a new local method later is a routing change, not a new project.'},
          'right': {'title': 'WHAT IT MEANS FOR CARRY1ST', 'sub': 'At a $10 average ticket, across the five markets', 'columns': ['Line', '50K', '200K', '450K'], 'col_widths': [2.0, 1, 1, 1], 'font_size': 7.5,
                    'rows': [['Sales a month', '$0.5M', '$2.0M', '$4.5M'], ['Platform fee', '$7,500', '$7,500', '$7,500'], ['Usage · tranche 1', '$0', '$4,500', '$7,500'], ['Usage · tranche 2', '$0', '$0', '$3,750'],
                             {'bold': True, 'cells': ['Total a month', '$7,500', '$12,000', '$18,750']}, ['Total a year', '$90,000', '$144,000', '$225,000'], ['Share of sales', '1.50%', '0.60%', '0.42%'], ['Per successful transaction', '$0.150', '$0.060', '$0.042']],
                    'callout': 'At launch Carry1st pays the platform fee and nothing per transaction. At the run rate the all-in cost is 0.42% of sales, falling as volume grows.',
                    'paragraph': 'Usage on a $5 purchase: $0.015 in tranche 1, $0.010 in tranche 3. A fixed fee stays the same whatever the ticket.'},
          'source': 'Platform fee billed annually. Usage billed monthly in arrears on successful transactions, net 30. Rates locked, tranches reviewed annually as volume grows. All figures in USD.',
          'notes': 'The proposal in one slide. A flat platform fee of $7,500 a month that already covers the first $500K of monthly sales, and above that a share of what you sell: 30 basis points to $3M, 25 to $6M, 20 above, each band on the volume inside it, only on approved payments, never a fee per transaction. At launch you pay the platform fee and nothing else; at the $4.5M run rate the all-in cost is $18,750 a month, 0.42% of sales, about four cents on a $10 purchase. Orchestration, smart routing, Monitors, the vault, the dashboard and a dedicated team are inside the platform fee; network tokens and 3DS are billed on usage and quoted separately.'})

S.append({'id': 'onus', 'type': 'two_column', 'kicker': 'INCLUDED, AT NO EXTRA COST',
          'headline': 'What Yuno puts in before signing, and what the platform fee already covers.',
          'cols': [{'header': 'BEFORE YOU SIGN', 'items': [
                      {'title': 'Shop prototype on the Yuno SDK', 'body': 'Already running in the sandbox for four markets; extended to Bolivia and the Shop\'s real SKUs before signature.'},
                      {'title': 'Localization support', 'body': 'Spanish and Portuguese checkout copy and market conventions, with Yuno\'s teams in São Paulo, Mexico City, Bogotá and Buenos Aires.'},
                      {'title': 'Local provider negotiation', 'body': 'Yuno brings EBANX and dLocal to the table on Carry1st\'s behalf, including how the EBANX arrangement sits alongside Yuno.'}]},
                   {'header': 'INSIDE THE PLATFORM FEE', 'items': [
                      {'title': 'No setup or implementation fee', 'body': 'Integration support, sandbox, go-live runbook and on-call during the launch weeks.'},
                      {'title': 'Adding a provider later is a routing change, not a fee', 'body': 'A local acquirer in Phase 2, a wallet or a new cash network is a new connection on the same checkout.'},
                      {'title': 'The stack', 'body': 'PCI token vault, risk conditions, Monitors and auto-failover, dashboard and insights with 20 seats.'},
                      {'title': 'Dedicated KAM and TAM', 'body': 'A named account manager and a technical account manager through the LatAm launch and after it.'}]}],
          'bar': 'The platform fee is the only fixed element in the proposal; everything on this slide sits inside it or comes before it.',
          'source': 'Yuno commitments to Carry1st, October 2026.',
          'notes': 'Everything on this slide is included. The prototype and the localization support were offered on the discovery call and we stand by them; the provider negotiation is part of how we work with EBANX and dLocal for every merchant on the platform. Inside the platform fee there is no setup charge, and adding a provider later is configuration, not a project or a fee.'})

S.append(divider('d07', '07', 'Launch plan to Black Friday and Phase 2', 'Six weeks to 27 November, then merchant of record against local presence',
                 'The week-by-week plan to Black Friday, and the comparison Fatih asked for: merchant of record, non-resident account, local entity.'))

S.append({'id': 'launch', 'type': 'table', 'kicker': 'LAUNCH PLAN · SIX WEEKS TO 27 NOVEMBER 2026', 'tag': ['PUBLIC DOCS', 'ESTIMATE'],
          'headline': 'Six weeks to 27 November: provider contracts and KYC are the critical path; the Yuno work is measured in days.',
          'columns': ['Week', 'Carry1st, EBANX and dLocal (critical path)', 'Yuno', 'Exit'], 'col_widths': [0.15, 0.37, 0.30, 0.18], 'header_style': 'dark', 'font_size': 7, 'bold_first_col': True, 'zebra': True,
          'rows': [
            ['Week 1 · 19 to 23 Oct', 'Scope confirmed (Brazil first or all five) and owners named; decision on the proposal; EBANX and dLocal agreements requested; volumes by country and EBANX\'s rates shared', 'Implementation lead named; sandbox keys and prototype access to Fatih\'s team; routing design agreed (EBANX primary, dLocal fallback)', 'Decision taken, agreements in motion'],
            ['Week 2 · 26 to 30 Oct', 'Agreements signed, KYC submitted to both providers; country enablement requested from EBANX for each market; Spanish and Portuguese copy started', 'Checkout build on the Yuno SDK starts from the prototype; payment-method list per market locked', 'KYC submitted; build under way'],
            ['Week 3 · 2 to 6 Nov', 'Provider sandbox credentials received; test transactions per country as EBANX requires', 'Connections created the day credentials arrive (1 to 2 days); routing rules and Monitors configured; webhooks and reconciliation set up', 'Both connections live in sandbox'],
            ['Week 4 · 9 to 13 Nov', 'EBANX Integration Review requested; dLocal go-live activation requested; support playbook and refund policy per market', 'End-to-end QA (3 to 5 days): decline retry EBANX to dLocal, refunds, Pix and PSE confirmation to delivery', 'Production credentials requested'],
            ['Week 5 · 16 to 20 Nov', 'Production credentials from both providers; soft launch in Brazil with internal buyers; local-currency pricing checked', 'Production connections, routing published, live monitoring; go-live runbook', 'Brazil live in production (soft)'],
            ['Week 6 · 23 to 27 Nov', 'Brazil open to all users; Argentina, Mexico and Colombia follow as each enablement lands; Bolivia through dLocal', 'On-call through launch; daily approval review by provider and country; Monitors active', 'Black Friday, 27 Nov: Shop live in LatAm']],
          'note': 'Provider onboarding and country enablement have no published SLA at EBANX or dLocal; Yuno durations are Yuno estimates. Dates assume the decision in week 1.',
          'source': 'EBANX pay-in guide and DEUNA partner page; docs.dlocal.com go-live prerequisites; docs.y.uno connections, read 15 Oct 2026 (PUBLIC DOCS and CONFIRMED). Yuno durations: Yuno estimate.',
          'notes': 'The honest version of the timeline. The critical path is not Yuno: it is the two provider onboardings, which neither EBANX nor dLocal puts a day count on, so we run them in parallel from week 1 and we start the Yuno build from the prototype while they progress. Once credentials exist, a connection takes a day or two and QA a few days. Brazil goes live softly in week 5 so that Black Friday is an opening, not a first test.'})

S.append({'id': 'phase2', 'type': 'table', 'kicker': 'PHASE 2 · MERCHANT OF RECORD AGAINST LOCAL PRESENCE', 'tag': ['PUBLIC DOCS', 'OPEN'],
          'headline': 'A merchant of record launches in weeks, local presence in months; through Yuno the move happens without a rebuild.',
          'columns': ['Dimension', 'Merchant of record (launch)', 'Non-resident account', 'Local entity and local acquirer', 'Yuno\'s role'], 'col_widths': [0.13, 0.25, 0.20, 0.25, 0.17], 'header_style': 'dark', 'font_size': 7, 'bold_first_col': True, 'zebra': True,
          'rows': [
            ['Time to launch', 'Weeks: agreement, KYC, sandbox, review (dLocal cites up to 8 weeks for market entry)', 'Weeks to months: local bank account and tax registration without a company; rules vary by country', 'Months: Brazil 6 to 12 weeks for registration plus the bank account; Mexico 4 to 12 weeks; Argentina SAS 7 to 15 business days plus bank; Colombia, Bolivia not published', 'Checkout unchanged across all three; the acquirer is a new connection'],
            ['Who carries tax and FX', 'The MoR: local-currency charge, FX and remittance; Carry1st is paid in USD. Tax treatment per country to be confirmed in writing (OPEN)', 'Carry1st registers for digital-services VAT: Mexico 16%, Colombia 19%, Argentina IVA withheld by issuers; Brazil CBS and IBS from 2026', 'Carry1st as a local taxpayer: VAT, income tax and FX remittance in each country', 'Routing by country keeps each model on its own rail'],
            ['Approval and customer experience', 'Domestic card presentation via the MoR\'s local entity; local methods; the gamer avoids FX and foreign-purchase taxes (AR 30% perception, BR 3.5% IOF)', 'Depends on whether the acquirer treats the merchant as domestic; often still cross-border', 'Local acquiring: vendor-reported 80 to 90% approval against 30 to 60% cross-border; installments and local brands (Elo, Naranja, Carnet)', 'Retries and failover apply whichever rail is live'],
            ['Cost', 'All-in rate with FX and tax pass-through inside it (Yuno estimate 3 to 6% of sales; EBANX\'s quote replaces it)', 'Lower processing, plus Carry1st\'s own tax and compliance overhead', 'Lowest processing cost at scale; highest fixed overhead (entity, accounting, treasury)', 'Two MoRs in play at launch keep the rate negotiable'],
            ['When it makes sense', 'Now: six weeks to Black Friday and volumes still unproven', 'When a country sustains volume and the MoR margin exceeds the compliance cost', 'At the $4 to 5M a month run rate, Brazil and Mexico first', 'Move country by country, no re-integration']],
          'note': 'Approval ranges are vendor-reported (2017 to 2026). Tax treatment under each MoR: OPEN, owner German, requested in writing from EBANX and dLocal.',
          'source': 'dLocal dMoRe release 26 Aug 2026; EBANX api-operability; Healy, Commenda, BizLatinHub, TMF 2025 to 2026 (incorporation); Kintsugi 2026, Estatuto Tributario, Ley 27.430, Decree 12.499/2025, RG 5617/2024 (tax); docs.y.uno connections and routing. PUBLIC DOCS unless marked.',
          'notes': 'Fatih asked for merchant of record against local presence with launch time and the long-term customer experience. The short version: the MoR launches in weeks and gives the gamer a domestic charge in local currency from day one; a local entity takes months and pays off at scale through lower processing and local acquiring. The Yuno column is the point: because the acquirer is a connection, Carry1st can make that move in Brazil first and Mexico second without touching the checkout, and keep the MoR live as fallback while it does.'})

S.append(divider('d08', '08', 'Next steps', 'Three weeks, owners on both sides, and a decision date',
                 'What happens in the next three weeks, who owns each step on each side, and the date by which the decision is needed so provider onboarding can start in time.'))

S.append({'id': 'next', 'type': 'next_steps', 'kicker': 'NEXT STEPS · THE NEXT THREE WEEKS',
          'headline': 'Three weeks, owners on both sides, and a decision by 23 October so provider onboarding can start in time for Black Friday.',
          'cards': [{'eyebrow': 'WEEK 1 · 19 TO 23 OCT', 'num': '01', 'title': 'Decide and sign', 'body': 'Carry1st (Cordel): confirm Brazil first or all five, send volumes by country and EBANX\'s proposed rates, decide on this proposal by Friday 23 October. Yuno (German, Justo): final terms and order form; JP confirms the localization support.'},
                    {'eyebrow': 'WEEK 2 · 26 TO 30 OCT', 'num': '02', 'title': 'Onboard the providers', 'body': 'Carry1st (Cordel, Fatih): EBANX and dLocal agreements and KYC in parallel, the critical path to 27 November. Yuno (solutions engineering): kickoff with Fatih\'s team, prototype extended to Bolivia and the Shop\'s real SKUs, routing design agreed.'},
                    {'eyebrow': 'WEEK 3 · 2 TO 6 NOV', 'num': '03', 'title': 'Connect and build', 'body': 'Carry1st (Fatih): checkout build on the Yuno SDK from the prototype; Spanish and Portuguese copy. Yuno (solutions engineering, German): connections live the day credentials arrive, Monitors and routing configured, QA plan for weeks 4 to 6.'}],
          'contact': 'Decision date: Friday 23 October 2026 · German Tatis · german.tatis@y.uno · +1 786 238 4554',
          'source': 'Owners and dates proposed by Yuno, 15 Oct 2026; to be confirmed on the call.',
          'notes': 'We propose a decision by Friday 23 October. Not because of us: the two provider onboardings are the critical path to 27 November, and they cannot start until the direction is set. Each step has an owner on both sides. If the decision is to go, the kickoff with Fatih\'s team happens the following week and the prototype becomes the starting point of the real build.'})

S.append({'id': 'closing', 'type': 'closing', 'line': "Let's grow together", 'name': 'German Tatis', 'title': 'Senior Account Executive, Yuno', 'phone': '+1 786 238 4554', 'email': 'german.tatis@y.uno',
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
    levers('Pix and domestic cards (Elo, Hipercard) through EBANX and dLocal from day one; Boleto in a second wave.',
           'Retry EBANX card declines on dLocal; present as a domestic charge so domestic-only cards (about 70%) can pay.',
           'Two MoRs live on Pix and cards; move share to the cheaper route by rule once both are live.'),
    [['Must-have', 'Pix', '42% of online purchases', 'Primary rail, instant confirmation', 'EBANX, dLocal and 25 more'],
     ['Must-have', 'Cards incl. Elo, Hipercard', '40 to 41% of value', 'Mainstream; installments later', 'EBANX, dLocal, Adyen, Cielo'],
     ['Optional', 'Boleto', 'Legacy cash voucher', 'Second wave; slow confirmation', 'EBANX, dLocal, Mercado Pago']],
    [{'title': 'Pix is the product fit', 'body': 'Confirms in seconds; 93% of adults use it.'},
     {'title': 'Domestic-only cards need a local rail', 'body': 'About 70% of Brazilian cards cannot pay cross-border.'},
     {'title': 'IOF makes the charge model matter', 'body': '3.5% IOF on international card payments; TO VALIDATE per MoR.'}],
    'Launch Brazil on Pix and local cards through the MoR; keep Boleto off at launch, and keep dLocal live behind EBANX from day one.',
    'Reuters 10 Feb 2026 (PCMI); Banco Central via press 2026; Newzoo and Allcorrect 2025; IQPC (undated); Decree 12.499/2025 (IOF); Yuno directory Oct 2026. TO VALIDATE: Boleto share 2025; IOF treatment of MoR charges (owner German).',
    'Brazil is where the Shop launches, and it is the market where the two rails that matter, Pix and domestic cards, both confirm instantly. The levers show one fifth of the base case at run rate as a placeholder until your volumes by country arrive. The one thing we would not do at launch is Boleto: it confirms late and the Shop promises instant delivery.'))

S.append(connections('cty-br-connections', 'Brazil',
    'Brazil: EBANX and dLocal are two of 46 providers live through Yuno; Pix is carried by 27 of them.',
    ['EBANX', 'dLocal'], ['Apple Pay', 'Google Pay', 'PayPal', 'PIX', 'Boleto', 'NuPay', 'Visa', 'Mastercard'],
    {'columns': ['Local method', 'Carried through Yuno by', '#'], 'col_widths': [0.2, 0.74, 0.06], 'font_size': 7,
     'rows': [['Pix', 'EBANX, dLocal, Adyen, Cielo, Getnet, Mercado Pago, PagSeguro, Pagar.me, PagBank, Nuvei, Stripe, PayRetailers, Fiserv, Santander and 13 more', '27'],
              ['Boleto', 'EBANX, dLocal, Mercado Pago, Pagar.me, PagBank, Banco do Brasil, Bradesco, Bamboo', '8']]},
    'Every provider live through Yuno in Brazil, from the Yuno integrations directory. The two merchant-of-record routes for the launch are highlighted; the rest is what Phase 2 can draw on without a new integration. Pix alone is carried by 27 providers, which is what makes the cost lever real.'))

# ---- Argentina
S.append(country('cty-ar', 'ar', 'Argentina',
    'Argentina is a wallet market where the 30% perception makes local-currency pricing the whole game; MODO arrives via dLocal.',
    [{'value': '46%', 'label': 'Wallets, share of e-commerce', 'caption': 'PCMI 2024 by value; above 55% in GPR 2026'},
     {'value': '22%', 'label': 'Domestic-only credit cards', 'caption': 'PCMI 2024: cannot be charged cross-border'},
     {'value': '17M+', 'label': 'MODO users; 100M+ QR a month', 'caption': 'Play Digital 2024; Descubre, Jul 2026'},
     {'value': '30%', 'label': 'Perception on foreign cards', 'caption': 'ARCA RG 5617/2024, in force Sep 2026'}],
    levers('Mercado Pago wallet and cards via EBANX and dLocal at launch; MODO and interoperable QR via dLocal as fast follow.',
           'A local-currency charge through the MoR avoids the 30% perception; retry declines across EBANX and dLocal.',
           'Both MoRs carry cards and Mercado Pago; move share by rule. Cash (Rapipago, Pago Fácil) stays optional.'),
    [['Must-have', 'Mercado Pago Wallet', '46 to 55% of e-commerce', 'Primary rail', 'EBANX, dLocal, Mercado Pago'],
     ['Must-have', 'Cards incl. Naranja, Cabal', '45% of value across card lines', 'Needs local presentation', 'EBANX, dLocal, Prisma, Fiserv'],
     ['Fast follow', 'MODO, interoperable QR', '17M+ users', 'Not available on EBANX', 'dLocal']],
    [{'title': 'Price in pesos through the MoR', 'body': 'A USD card charge costs the gamer 30% more; TO VALIDATE per MoR.'},
     {'title': 'Domestic-only cards are 22% of value', 'body': 'Cross-border rails cannot charge them at all.'},
     {'title': 'Refund timing differs by provider', 'body': 'EBANX card refunds can take 89 to 120 days (EBANX docs).'}],
    'Argentina rewards the second provider immediately: MODO and QR exist only on dLocal, and the perception rule makes local-currency pricing non-negotiable.',
    'PCMI 2024 via press; Global Payments Report 2026 via Forbes Argentina; Descubre 14 Jul 2026; ARCA RG 5617/2024 (Fortuna, 2026); Newzoo 2024 via iProUP; EBANX Argentina overview; Yuno directory Oct 2026. TO VALIDATE: perception treatment per MoR (owner German).',
    'Argentina is a wallet market, and it is the market where the rail decides the price the gamer sees: a foreign-currency card purchase carries a 30% perception that a local-currency charge through the merchant of record does not. MODO and interoperable QR are only reachable through dLocal, which is the second-provider argument in one line.'))

S.append(connections('cty-ar-connections', 'Argentina',
    'Argentina: 23 providers live through Yuno; MODO and interoperable QR reach the Shop only through dLocal.',
    ['EBANX', 'dLocal'], ['Apple Pay', 'Google Pay', 'PayPal', 'Pago Fácil', 'Rapipago', 'Visa', 'Mastercard', 'Click to Pay'],
    {'columns': ['Local method', 'Carried through Yuno by', '#'], 'col_widths': [0.22, 0.72, 0.06], 'font_size': 7,
     'rows': [['Cards', 'EBANX, dLocal, Prisma via Fiserv, Getnet, Mercado Pago, Nuvei, PayU, Worldline, Worldpay and others', '21'],
              ['Mercado Pago (Checkout Pro, Wallet)', 'EBANX (Checkout Pro), Mercado Pago (Wallet, QR, Checkout Pro), dLocal', '3'],
              ['MODO, interoperable QR', 'dLocal', '1'],
              ['Rapipago, Pago Fácil (cash)', 'dLocal; Bamboo (Pago Fácil); EBANX and PayU (cash)', '4']]},
    'The Argentina connections live through Yuno. Cards and Mercado Pago are on both merchant-of-record routes; MODO and interoperable QR are on dLocal only, which is why the second route matters here from day one.'))

# ---- Mexico
S.append(country('cty-mx', 'mx', 'Mexico',
    'Mexico is a debit market: three in four online buyers pay with debit cards foreign acquirers decline; the MoR must look domestic.',
    [{'value': '74%', 'label': 'Online buyers using debit cards', 'caption': 'AMVO Estudio de Venta Online 2024'},
     {'value': '77M', 'label': 'Digital buyers in 2025', 'caption': 'AMVO 2026; retail e-commerce +19% in 2025'},
     {'value': '76M+', 'label': 'Players; $2.3B games revenue', 'caption': 'Endeavor México and Santander, 2025'},
     {'value': '36', 'label': 'Providers live through Yuno', 'caption': 'Yuno integrations directory, Oct 2026'}],
    levers('Debit and credit cards incl. Carnet, SPEI and OXXO Pay through EBANX and dLocal; CoDi and 7-Eleven through dLocal later.',
           'Local presentation lifts debit approval (Nuvei cites 20 to 30 points); retry EBANX declines on dLocal.',
           'Both MoRs carry cards, SPEI and OXXO; the largest LatAm card base gives routing share real weight.'),
    [['Must-have', 'Debit and credit cards incl. Carnet', '74% and 54% usage', 'Domestic presentation, 3DS tuned', 'EBANX, dLocal and 31 more'],
     ['Must-have', 'SPEI', '8 of 10 buyers use cards or SPEI', 'Instant bank transfer', 'EBANX, dLocal, Kushki, STP'],
     ['Must-have', 'OXXO Pay and OXXO cash', 'Cash 17% of usage', 'OXXO Pay confirms faster', 'EBANX, dLocal, Bamboo']],
    [{'title': '16% IVA on digital services', 'body': 'Sits inside the MoR rate; TO VALIDATE per provider.'},
     {'title': 'Debit declines are structural', 'body': 'Many debit cards are blocked cross-border or fail 3DS abroad.'},
     {'title': 'The prototype already runs Mexico', 'body': 'OXXO and local prices run in the sandbox demo today.'}],
    'Mexico converts on debit and SPEI presented as domestic; the second MoR matters most for failover, and for CoDi and convenience-store cash later.',
    'AMVO Estudio 2024 and 2026; Endeavor México and Santander via Forbes México 2025; Nuvei, Unlimit and Antom vendor pages 2025 to 2026 (vendor claims); Kintsugi 2026 (IVA); Yuno directory Oct 2026. TO VALIDATE: AMVO 2026 method shares; OXXO share.',
    'Mexico is the largest card base in the region and a debit market: three in four online buyers use debit, and debit is the card type most often declined when the merchant looks foreign. That is why the merchant of record has to present the charge as domestic. SPEI and OXXO Pay complete the set; CoDi and the convenience-store networks can follow through dLocal.'))

S.append(connections('cty-mx-connections', 'Mexico',
    'Mexico: 36 providers live through Yuno; SPEI and OXXO reach the Shop through either MoR, CoDi and 7-Eleven through dLocal.',
    ['EBANX', 'dLocal'], ['Apple Pay', 'Google Pay', 'PayPal', 'OXXO Pay', 'SPEI', 'CoDi', '7-Eleven', 'Visa', 'Mastercard', 'Kueski'],
    {'columns': ['Local method', 'Carried through Yuno by', '#'], 'col_widths': [0.22, 0.72, 0.06], 'font_size': 7,
     'rows': [['SPEI', 'EBANX, dLocal, Kushki, Nuvei, PagSeguro, STP, Unlimit, Bamboo', '8'],
              ['OXXO Pay and OXXO cash', 'EBANX (OXXO Pay), dLocal (OXXO, 7-Eleven, Paynet), Bamboo, PagSeguro, Unlimit', '6'],
              ['CoDi, Mercado Pago wallet', 'dLocal (CoDi), Mercado Pago, EBANX (Checkout Pro), Unlimit', '4']]},
    'The Mexico connections live through Yuno. Cards, SPEI and OXXO are on both merchant-of-record routes; CoDi and the convenience-store cash networks are on dLocal. The 36 providers behind them are what Phase 2 local acquiring can draw on.'))

# ---- Colombia
S.append(country('cty-co', 'co', 'Colombia',
    'Colombia is an account-to-account market: PSE carries 64% of e-commerce transactions and Bre-B is the next rail; cards a third.',
    [{'value': '63.9%', 'label': 'PSE, share of online purchases', 'caption': 'CCCE via Valora Analitik, Q2 2025'},
     {'value': '36M+', 'label': 'Bre-B users in its first year', 'caption': 'Banco de la República, 6 Oct 2026; 1.7B tx'},
     {'value': '28M', 'label': 'Nequi active users', 'caption': 'Nequi via press, May 2026'},
     {'value': '31', 'label': 'Providers live through Yuno', 'caption': 'Yuno integrations directory, Oct 2026'}],
    levers('PSE and Nequi through dLocal and EBANX, Bre-B as fast follow through dLocal; cards through both MoRs.',
           'Account-to-account methods approve or fail instantly; retry card declines across both MoRs.',
           'PSE and cards sit on both MoRs: route by method and by cost; 19% IVA handled by the MoR (TO VALIDATE).'),
    [['Must-have', 'PSE', '63.9% of transactions', 'Primary rail, instant', 'dLocal, EBANX, PayU, Kushki, Wompi'],
     ['Must-have', 'Nequi, Bre-B', '28M and 36M users', 'Wallet and QR reach', 'dLocal, Wompi, Nuvei; Bre-B: dLocal'],
     ['Must-have', 'Cards', '33% of transactions, 43% of value', 'Local presentation', 'EBANX, dLocal, Credibanco, Redeban']],
    [{'title': 'EBANX rails in Colombia to confirm', 'body': 'PSE Avanza and Bre-B in EBANX docs; confirm on your account.'},
     {'title': 'Significant economic presence rules', 'body': 'Local pricing can trigger PES; a MoR keeps Carry1st offshore.'},
     {'title': 'The prototype already runs Colombia', 'body': 'PSE, Nequi and Daviplata run in the sandbox demo today.'}],
    'Colombia runs on PSE today and Bre-B tomorrow; both reach the Shop through dLocal on day one, with cards on either MoR.',
    'CCCE via Valora Analitik 24 Aug 2025; Banco de la República 6 Oct 2026; Nequi via press May 2026; Estatuto Tributario art. 20-3 and Decreto 2039/2023; EBANX Colombia overview; Yuno directory Oct 2026. TO VALIDATE: EBANX PSE Avanza and Bre-B on Carry1st\'s account; credit-card penetration 2025.',
    'Colombia moved from cards to account-to-account in three years: PSE is now two thirds of e-commerce transactions and Bre-B, the central bank\'s instant rail, passed 36 million users in its first year. Both are instant, which fits the Shop. Cards are a third of transactions and sit on both merchant-of-record routes.'))

S.append(connections('cty-co-connections', 'Colombia',
    'Colombia: 31 providers live through Yuno; PSE is carried by 12 of them and Bre-B by dLocal today.',
    ['EBANX', 'dLocal'], ['Apple Pay', 'Google Pay', 'PayPal', 'Nequi', 'Daviplata', 'Efecty', 'ADDI', 'Visa', 'Mastercard'],
    {'columns': ['Local method', 'Carried through Yuno by', '#'], 'col_widths': [0.22, 0.72, 0.06], 'font_size': 7,
     'rows': [['PSE', 'Bamboo, dLocal, EBANX, Ecommpay, Kushki, Mercado Pago, Nuvei, PagSeguro, PayU, SafetyPay, Unlimit, Wompi', '12'],
              ['Nequi, Daviplata', 'Nequi: Bamboo, dLocal, Nuvei, SafetyPay, Wompi · Daviplata: Nuvei, Wompi', '5'],
              ['Bre-B', 'dLocal', '1'],
              ['Efecty (cash)', 'dLocal, Nuvei, PagSeguro, Unlimit', '4']]},
    'The Colombia connections live through Yuno. PSE is carried by twelve providers including both merchant-of-record routes; Nequi by five; Bre-B by dLocal today, with more providers expected as the rail matures.'))

# ---- Bolivia
S.append(country('cty-bo', 'bo', 'Bolivia',
    'Bolivia is the clearest case for a second provider: EBANX direct means cash vouchers only; dLocal adds cards and QR on day one.',
    [{'value': '36%', 'label': 'QR share of payments, 2025', 'caption': 'BCB via Los Tiempos, Jun 2026; 15% in 2020'},
     {'value': '64%', 'label': 'Cash share of payments, 2025', 'caption': 'BCB via Los Tiempos, Jun 2026; 85% in 2020'},
     {'value': '$500', 'label': 'Foreign debit-card limit a month', 'caption': 'Asoban via Los Tiempos, 9 Apr 2026'},
     {'value': '6', 'label': 'Providers live through Yuno', 'caption': 'Yuno integrations directory, Oct 2026'}],
    levers('Cards and interoperable QR through dLocal; cash vouchers (Pago al Paso, Multipago) as the fallback.',
           'Local processing avoids the foreign-card limit and FX; QR confirms instantly.',
           'A single-route market today: leverage comes from the pooled five-country volume, not from Bolivia alone.'),
    [['Must-have', 'QR (BCB interoperable)', '36% of payments, rising', 'Instant; confirm on dLocal', 'dLocal'],
     ['Must-have', 'Visa, Mastercard (local)', 'Foreign cards capped at $500', 'Domestic charge, no FX', 'dLocal (EBANX: open)'],
     ['Optional', 'Cash: Pago al Paso, Multipago, PagosNet', '64% of payments', 'Slow confirmation; second wave', 'dLocal, EBANX']],
    [{'title': 'The second provider is the whole point', 'body': 'EBANX direct: PagosNet cash and bank only (EBANX docs).'},
     {'title': 'Cards need local processing', 'body': 'Foreign debit capped at $500 a month, FX at the daily reference rate.'},
     {'title': 'Phase the market', 'body': 'Smallest of the five; launch after Brazil, through dLocal only.'}],
    'Route Bolivia to dLocal from day one; EBANX\'s Bolivia card coverage stays an open item, not a dependency.',
    'BCB via Los Tiempos 14 Jun 2026 and 9 Apr 2026; EBANX Bolivia overview and status.ebanx.com; docs.dlocal.com/docs/bolivia; Yuno directory Oct 2026. TO VALIDATE: QR enabled on the dLocal connection; EBANX Bolivia cards (owner Yuno integrations).',
    'Bolivia is small and it is the clearest argument for a second provider: EBANX\'s own documentation lists only PagosNet cash and bank for Bolivia, while dLocal processes Visa and Mastercard locally and carries the interoperable QR that is now a third of all payments in the country. The Yuno directory lists EBANX under Bolivia cards, which conflicts with EBANX\'s docs, so we treat it as open and route Bolivia to dLocal.'))

S.append(connections('cty-bo-connections', 'Bolivia',
    'Bolivia: dLocal is the route for cards, QR and cash through Yuno; EBANX in Bolivia stays an open item.',
    ['dLocal'], ['PayPal', 'Visa', 'Mastercard', 'Pago al Paso'],
    {'columns': ['Method', 'Carried through Yuno by', 'Status'], 'col_widths': [0.24, 0.56, 0.20], 'font_size': 7,
     'rows': [['Cards (Visa, Mastercard)', 'dLocal; also AstroPay, Cybersource, Inswitch, Nuvei', {'text': '', 'pill': 'CONFIRMED'}],
              ['QR (BCB interoperable)', 'dLocal per its docs; to confirm on the Yuno dLocal connection', {'text': 'owner German', 'pill': 'OPEN'}],
              ['EBANX in Bolivia', 'Directory lists EBANX under cards; EBANX docs show PagosNet cash and bank only', {'text': 'owner Yuno integrations', 'pill': 'OPEN'}]]},
    'Bolivia has six providers live through Yuno and dLocal is the merchant-of-record route for the launch: cards, QR and cash. EBANX appears under Bolivia cards in the Yuno directory but EBANX\'s own documentation shows cash only, so we carry it as an open item and do not depend on it.',
    extra_sections=[{'header': 'Open: EBANX in Bolivia', 'style': 'request', 'chips': [chip('EBANX')]}],
    source='Yuno integrations directory, pulled 14 Oct 2026 (CONFIRMED); EBANX Bolivia overview and status.ebanx.com, docs.dlocal.com/docs/bolivia, read 15 Oct 2026 (PUBLIC DOCS). OPEN items carry an owner.'))

# ---- risks and sources
S.append({'id': 'risks', 'type': 'table', 'kicker': 'APPENDIX · RISKS AND ASSUMPTIONS', 'tag': ['ESTIMATE', 'OPEN'],
          'headline': 'Every modeled number in this deck rests on nine assumptions, each with an owner and a replacement path.',
          'columns': ['Assumption', 'Value in the deck', 'Basis and replacement', 'Owner', 'Status'], 'col_widths': [0.20, 0.24, 0.30, 0.13, 0.13], 'header_style': 'dark', 'font_size': 7, 'bold_first_col': True, 'zebra': True,
          'rows': [
            ['Run-rate volume and ticket', '450K tx, $4.5M a month; $10 / $5 ticket', 'Carry1st, Cordel, Oct 2026; not aligned internally', 'Cordel', {'text': '', 'pill': 'ESTIMATE'}],
            ['Launch volume and ramp', '50K a month, linear to 450K by Dec 2027', 'Yuno placeholder until volumes by country arrive', 'Cordel', {'text': '', 'pill': 'OPEN'}],
            ['EBANX direct all-in cost', '4.5% of sales (range 3 to 6%)', 'Yuno estimate; EBANX\'s quote to Carry1st replaces it', 'Cordel', {'text': '', 'pill': 'ESTIMATE'}],
            ['Carry1st take rate on GMV', '15%', 'Yuno estimate; to validate with Shop margins', 'Cordel', {'text': '', 'pill': 'ESTIMATE'}],
            ['Approval uplift, two providers', '+1.5 / +3.0 / +5.0 points', 'Yuno estimate under the published 7% ceiling', 'Cordel, Yuno', {'text': '', 'pill': 'ESTIMATE'}],
            ['MDR reduction, routing leverage', '25 / 50 / 75 bps of sales', 'Yuno estimate; provider rates through Yuno pending', 'Yuno', {'text': '', 'pill': 'OPEN'}],
            ['Provider onboarding time', 'Weeks; no published SLA', 'Provider docs; run both in parallel from week 1', 'Cordel, Yuno lead', {'text': '', 'pill': 'PUBLIC DOCS'}],
            ['EBANX cards in Bolivia', 'Not assumed; Bolivia on dLocal', 'Yuno directory says cards; EBANX docs say cash only', 'Yuno integrations', {'text': '', 'pill': 'OPEN'}],
            ['Tax treatment under each MoR', 'Domestic charge; taxes in the MoR rate', 'Not documented publicly; requested in writing', 'German', {'text': '', 'pill': 'OPEN'}]],
          'note': 'Every yellow input in the model swaps for Carry1st\'s data as it arrives; the deck is rebuilt from the same model.',
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
                      'dLocal · dlocal.com; docs.dlocal.com (Brazil, Argentina, Mexico, Colombia, Bolivia, go-live); dMoRe release 26 Aug 2026',
                      'Brazil · Reuters 10 Feb 2026 (PCMI); Banco Central via press 2026; Newzoo, Allcorrect 2025; Decree 12.499/2025 and ARQ Finance 29 Sep 2026 (IOF); VATCalc, Fonoa 2026',
                      'Argentina · PCMI 2024; Global Payments Report 2026 via Forbes Argentina; Descubre 14 Jul 2026; Fortuna 2026 and ARCA RG 5617/2024; Ley 27.430; Newzoo 2024 via iProUP',
                      'Mexico · AMVO Estudio 2024 and 2026; Endeavor México and Santander 2025 via Forbes México; Nuvei, Unlimit, Antom pages; Kintsugi 2026 (IVA); BizLatinHub, Commenda',
                      'Colombia · CCCE via Valora Analitik 24 Aug 2025; Banco de la República 6 Oct 2026; Nequi via press May 2026; Estatuto Tributario art. 20-3, Decreto 2039/2023',
                      'Bolivia · BCB via Los Tiempos 14 Jun 2026 and 9 Apr 2026 (Asoban); Ministerial Resolution 245/2026 (exchange rate); AGN 2026 tax card',
                      'Approval ranges · Worldline, Rapyd, Nuvei, Antom, EBANX 11 Sep 2017 (AMI); vendor-reported, 2017 to 2026']}],
          'footnote': 'Third-party lines are our reading of public pages on the dates shown; confirm each with the provider before relying on it. Carry1st call figures are estimates until confirmed.',
          'notes': 'Appendix. The pages behind every claim, so your team can open them. Yuno claims come from our public documentation, y.uno and the model in this deck; provider and market lines come from their own public pages or dated press, and we would rather you confirm them with each provider than take our reading.'})

SPEC = {'presentation_id': PID, 'merchant': 'Carry1st', 'footer': 'For: Carry1st', 'slides': S}
out = os.path.join(HERE, 'deck_spec.json')
json.dump(SPEC, open(out, 'w'), ensure_ascii=False, indent=1)
print(f'wrote {out}: {len(S)} slides')
