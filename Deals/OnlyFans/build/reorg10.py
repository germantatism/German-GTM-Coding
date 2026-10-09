# -*- coding: utf-8 -*-
"""Reorganize the 28-slide 'OnlyFans + Yuno | Token Vault Revised' copy into a 10-slide deck
(Juan Pablo: max 10 slides, banking connectivity not BaaS; Justo: add banking connectivity from his skeleton).
Usage: python3 reorg10.py <presentation_id> [--dry]
Final order: cover, exec summary, integrated vs standalone, how it works, the vault you design,
banking connectivity (new, from slide 6), rules and resilience (new, from slide 7), issuers and yield (new, from slide 7),
clients, next steps. Kept on purpose (German): SpaceX logo, 'Agentic commerce' pill, PayPal."""
import sys, json, os, warnings, time
warnings.filterwarnings('ignore')

PID = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('--') else None
DRY = '--dry' in sys.argv

S = {  # source slide ids (identical in any Drive copy)
    1: 'n01_g3f77215683c_1_445', 4: 'of_exec_understanding_v2', 5: 'm5_mock', 6: 'of_vault_proxy_flow_v3',
    7: 'h7c266de662ba1cf0_35_0', 16: 'h7c266de662ba1cf0_9_241', 23: 'h7c266de662ba1cf0_9_611', 28: 'nv_time',
}
NEW = {'bc': S[6] + '_bc', 'rl': S[7] + '_rl', 'yd': S[7] + '_yd'}
ORDER = [S[1], S[4], S[5], S[6], S[16], NEW['bc'], NEW['rl'], NEW['yd'], S[23], S[28]]

def R(page, old, new):  # replace exact text on one page, keeps run styling
    return {'replaceAllText': {'containsText': {'text': old, 'matchCase': True}, 'replaceText': new, 'pageObjectIds': [page]}}

def edits():
    e = []
    # 1 · cover
    p = S[1]
    e += [R(p, 'The vault under creator banking', 'One vault, every bank behind it'),
          R(p, 'Your credentials, your connections, your rules.', 'Token vault and banking connectivity for OnlyFans'),
          R(p, '194+ COUNTRIES', '190+ COUNTRIES')]
    # 2 · executive summary (was 4)
    p = S[4]
    e += [R(p, 'EXECUTIVE SUMMARY  ›  OUR UNDERSTANDING OF THE CONTEXT', 'EXECUTIVE SUMMARY'),
          R(p, 'OnlyFans needs to manage creator payouts and expand into creator BaaS', 'OnlyFans needs a vault and connections to every bank behind each creator'),
          R(p, 'Reliable payments to creators', 'Reliable payouts to creators'),
          R(p, 'with a broader ambition to offer ', 'and '),
          R(p, 'one account', 'one account per creator'),
          R(p, ' for BaaS, cards and transfers.', ', with several banks, card issuers and transfer providers behind it.'),
          R(p, 'That choice should support how credentials will be used across providers, for both ', 'That choice decides how creator data reaches every bank, issuer and processor, for '),
          R(p, 'creator payouts and future financial services', 'creator payouts today and as partners change'),
          R(p, 'What the solution needs to cover', 'What we propose'),
          R(p, 'Secure storage, connections to providers and rules OnlyFans controls—so the data can be used to deliver services to creators.',
            'One Yuno vault for cards, bank, identity and tax data, plus banking connectivity to your banks, issuers, rails and stablecoin partners, on rules OnlyFans controls.'),
          R(p, '4', '2')]  # page number box
    # 3 · integrated vs standalone (was 5)
    p = S[5]
    e += [R(p, 'EXECUTIVE SUMMARY  ›  COMPREHENSIVE VERSUS STANDALONE', 'WHY AN INTEGRATED VAULT'),
          R(p, 'Yuno´s vault solution provides comprehensive functionality with far less build resources than standalone option',
            "Yuno's vault does everything a standalone vault does, plus the connections, with far less to build"),
          R(p, '460+ processors and banks', '460+ processor integrations'),
          R(p, ' already connected', ', plus banking connectivity to your banks'),
          R(p, 'payouts and BaaS', 'payouts and banking connectivity'),
          R(p, '5', '3')]
    # 4 · how it works (was 6)
    p = S[6]
    e += [R(p, 'EXECUTIVE SUMMARY  ›  VAULT AND PROXY', 'HOW IT WORKS'),
          R(p, 'BaaS', 'Bank connectivity'),
          R(p, '6', '4')]
    # 5 · the vault you design (was 16)
    p = S[16]
    e += [R(p, '2 · OUR PROPOSAL  ›  VAULT  ›  SCHEMA', 'THE VAULT  ›  YOUR DESIGN'), R(p, '16', '5')]
    # 6 · banking connectivity (new from 6)
    p = NEW['bc']
    e += [R(p, 'EXECUTIVE SUMMARY  ›  VAULT AND PROXY', 'BANKING CONNECTIVITY  ›  HOW IT WORKS'),
          R(p, 'Your systems use tokens. The proxy delivers the data providers need.', 'One creator account. Every bank, issuer and rail behind it, through one connection.'),
          R(p, 'YOUR SYSTEMS', 'ONLYFANS'), R(p, 'OnlyFans systems', 'One account per creator'),
          R(p, 'Store and send tokens only.', 'Sets the rules: which bank,'), R(p, 'No raw card or bank data.', 'issuer and rail each creator uses.'),
          R(p, 'SECURE STORAGE', 'SECURE DATA'),
          R(p, 'Cards and network tokens', 'KYC, tax IDs, bank details,'), R(p, 'Creator bank, identity', 'W-9s and cards, collected'), R(p, 'and tax data', 'once and reused'),
          R(p, 'SECURE FORWARDING', 'BANKING CONNECTIVITY'), R(p, 'Yuno Proxy', 'Yuno'),
          R(p, 'Swaps tokens for stored', 'Opens accounts, runs your'), R(p, 'values, then forwards.', 'rules, routes every transfer.'),
          R(p, 'APPROVED DESTINATION', 'YOUR PARTNERS'), R(p, 'Your chosen provider', 'Banks, issuers, rails'),
          R(p, 'Receives the data it needs', '2 to 5 banks per creator,'), R(p, 'to process the request.', 'issuers you add or swap.'),
          R(p, 'OPTIONAL', 'CONNECTED'), R(p, 'Yuno services', 'Your partners'), R(p, 'Same tokens, on per use case', 'Plugged in or swapped by configuration'),
          R(p, 'Authentication', 'Banks (2 to 5)'), R(p, 'Optimisation', 'Card issuers'), R(p, 'Payouts', 'ACH'), R(p, 'BaaS', 'Wire and RTP'),
          R(p, 'Orchestration', 'Stablecoin ramps'), R(p, 'Agentic commerce', 'Balances in one view'),
          R(p, "ONLYFANS' CONTROL", 'YUNO NEVER HOLDS THE MONEY'),
          R(p, 'You decide who accesses data and which destinations receive it', 'The banks hold the funds; Yuno connects, routes and reconciles'),
          R(p, 'Allowlisted destinations', 'Fan payments in'), R(p, 'Secure transport', 'Creator payouts out'), R(p, 'Audit trail', 'One platform'),
          R(p, 'Credential flow, not funds movement. Card proxy is in beta; broader data and destination coverage to confirm.',
            'Product direction, not a delivery commitment. Bank allocation by rule and the US banks and issuers behind the API are confirmed in writing with the RFP.'),
          R(p, 'tokens', 'rules'), R(p, 'data', 'transfers'),
          R(p, '6', '6')]
    # 7 · rules and resilience (new from 7)
    p = NEW['rl']
    e += [R(p, 'EXECUTIVE SUMMARY  ›  BEYOND THE VAULT', 'BANKING CONNECTIVITY  ›  CONTROL AND RESILIENCE'),
          R(p, "The same platform that holds your credentials can also route your fans' payments, when you want it to", 'You set the rules, Yuno runs them, and no single bank can cut a creator off'),
          R(p, 'FAN PAYMENTS IN · AN OPTION FOR LATER', 'YOU SET THE RULES'), R(p, 'Orchestration', 'OnlyFans decides. Yuno runs it.'),
          R(p, 'Routing across several processors by your rules', 'Spread each creator across 2 to 5 banks, with a cap per bank'),
          R(p, 'Automatic failover when a processor degrades', 'Send each payout on the cheapest or fastest rail'),
          R(p, 'Network tokens and authentication tuned per issuer', 'Every decision logged with the rule that triggered it'),
          R(p, 'No single processor can stop fans paying: the 2021 lesson on the pay-in side.', 'Who decides where each creator lands: OnlyFans, by rule.'),
          R(p, 'Live today', 'Per-call bank choice live today'),
          R(p, 'CREATOR PAYOUTS OUT · THE RFP DESIGN', 'NO SINGLE POINT OF FAILURE'), R(p, 'BaaS (Banking-as-a-Service) layer', 'Backup banks ready before you need them'),
          R(p, 'Bank and rail choice by your rules', 'Backup accounts opened when the creator signs up'),
          R(p, 'Payouts by ACH, same-day ACH, wire and RTP', 'If a bank freezes an account, funds and payouts move to the next'),
          R(p, 'Balances across banks in one view', 'Balances across every bank in one view, reconciled daily'),
          R(p, 'No single bank can stop creators being paid.', "The bank's ledger stays the record of truth."),
          R(p, 'API and rails live', 'ACH, wire and RTP live'), R(p, 'Bank rules proposed', 'Rules and failover proposed'),
          R(p, 'The vault sits under both. Start with the vault; adding orchestration later is configuration, not a new project.',
            'Losing a bank becomes a reallocation your rules already anticipated, not an outage.'),
          R(p, '7', '7')]
    # 8 · issuers and yield (new from 7)
    p = NEW['yd']
    e += [R(p, 'EXECUTIVE SUMMARY  ›  BEYOND THE VAULT', 'BANKING CONNECTIVITY  ›  BEYOND THE ACCOUNT'),
          R(p, "The same platform that holds your credentials can also route your fans' payments, when you want it to", 'Earn on idle balances and swap card issuers, on the same connections'),
          R(p, 'FAN PAYMENTS IN · AN OPTION FOR LATER', 'YIELD'), R(p, 'Orchestration', 'Two ways to earn on idle balances'),
          R(p, 'Routing across several processors by your rules', 'Treasury-backed balances in US T-bills, through Jiko'),
          R(p, 'Automatic failover when a processor degrades', 'Or convert to stablecoins, through Coinbase and Triple-A'),
          R(p, 'Network tokens and authentication tuned per issuer', 'Your rules decide how much moves and when'),
          R(p, 'No single processor can stop fans paying: the 2021 lesson on the pay-in side.', 'Yuno never holds funds or crypto.'),
          R(p, 'Live today', 'Partners confirmed in writing'),
          R(p, 'CREATOR PAYOUTS OUT · THE RFP DESIGN', 'PLUGGABLE ISSUERS'), R(p, 'BaaS (Banking-as-a-Service) layer', 'Add or swap issuers like any other connection'),
          R(p, 'Bank and rail choice by your rules', 'Issuers connect the same way processors and banks do'),
          R(p, 'Payouts by ACH, same-day ACH, wire and RTP', "The vault already holds the creator's verified data"),
          R(p, 'Balances across banks in one view', 'A new issuer needs no new KYC and no change to your integration'),
          R(p, 'No single bank can stop creators being paid.', 'Fan payments in, payouts and cards out.'),
          R(p, 'API and rails live', 'Proxy to issuer APIs (beta)'), R(p, 'Bank rules proposed', 'Issuer partners to confirm'),
          R(p, 'The vault sits under both. Start with the vault; adding orchestration later is configuration, not a new project.',
            'One platform for the full creator money flow. Product direction, not a delivery commitment.'),
          R(p, '7', '8')]
    # 9 · clients (was 23)
    p = S[23]
    e += [R(p, '3 · WHY YUNO  ›  CLIENTS', 'WHY YUNO'), R(p, '23', '9')]
    # 10 · next steps (was 28)
    p = S[28]
    e += [R(p, '4 · TIMELINE AND NEXT STEPS', 'NEXT STEPS'),
          R(p, '[RFP deadline]', 'Your RFP date'),
          R(p, 'Intro call', 'Your lead: Antoine Cathelin, Head of Trust & Vault'),
          R(p, 'Deck to the Payments Manager', 'Intro call with your payments and vault team'),
          R(p, 'Our ask this week: include Yuno in the RFP evaluation. After Phase 1: creator banking across banks, pluggable issuers, then yield, at OnlyFans\' pace.',
            "Our ask this week: include Yuno in the RFP and book a working session. After Phase 1: banking connectivity across your banks, pluggable issuers, then yield, at OnlyFans' pace."),
          R(p, '28', '10')]
    return e

def check_against_dump(reqs):
    """dry run: every 'old' string must exist on its source page in copy_dump.json"""
    P = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'copy_dump.json')))
    def texts(sl):
        out = []
        def walk(els):
            for el in els:
                if 'elementGroup' in el: walk(el['elementGroup']['children'])
                elif 'shape' in el:
                    out.append(''.join(te.get('textRun', {}).get('content', '') for te in el['shape'].get('text', {}).get('textElements', [])))
        walk(sl.get('pageElements', [])); return out
    by = {sl['objectId']: texts(sl) for sl in P['slides']}
    src = {NEW['bc']: S[6], NEW['rl']: S[7], NEW['yd']: S[7]}
    bad = 0
    for r in reqs:
        page = r['replaceAllText']['pageObjectIds'][0]; old = r['replaceAllText']['containsText']['text']
        if not any(old in t for t in by[src.get(page, page)]): print('MISSING', page, repr(old)); bad += 1
    print(f'{len(reqs)} replacements, {bad} missing'); return bad

def main():
    reqs = edits()
    if check_against_dump(reqs) or DRY or not PID: return
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    creds = service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'), scopes=['https://www.googleapis.com/auth/presentations'])
    svc = build('slides', 'v1', credentials=creds, cache_discovery=False)
    P = svc.presentations().get(presentationId=PID).execute()
    ids = [s['objectId'] for s in P['slides']]
    assert all(v in ids for v in S.values()), 'source slides missing: not a copy of the 28-slide deck?'
    def idmap(sl, suf):
        m = {sl['objectId']: sl['objectId'] + suf}
        def walk(els):
            for el in els:
                m[el['objectId']] = el['objectId'] + suf
                if 'elementGroup' in el: walk(el['elementGroup']['children'])
        walk(sl.get('pageElements', [])); return m
    bys = {s['objectId']: s for s in P['slides']}
    dup = []
    if NEW['bc'] not in ids: dup.append({'duplicateObject': {'objectId': S[6], 'objectIds': idmap(bys[S[6]], '_bc')}})
    if NEW['rl'] not in ids: dup.append({'duplicateObject': {'objectId': S[7], 'objectIds': idmap(bys[S[7]], '_rl')}})
    if NEW['yd'] not in ids: dup.append({'duplicateObject': {'objectId': S[7], 'objectIds': idmap(bys[S[7]], '_yd')}})
    if dup: svc.presentations().batchUpdate(presentationId=PID, body={'requests': dup}).execute(); print('duplicated', len(dup))
    # text edits (page numbers last-matched per page are single-digit strings; run them after text)
    num = [r for r in reqs if r['replaceAllText']['containsText']['text'].isdigit()]
    txt = [r for r in reqs if r not in num]
    svc.presentations().batchUpdate(presentationId=PID, body={'requests': txt}).execute(); print('text edits', len(txt))
    # page numbers: set the page-number box text directly (digits appear elsewhere on slides)
    P = svc.presentations().get(presentationId=PID).execute(); bys = {s['objectId']: s for s in P['slides']}
    pg = []
    for pos, sid in enumerate(ORDER, 1):
        for el in bys[sid].get('pageElements', []):
            t = ''.join(te.get('textRun', {}).get('content', '') for te in el.get('shape', {}).get('text', {}).get('textElements', [])).strip()
            tr = el.get('transform', {})
            if t.isdigit() and tr.get('translateX', 0) / 12700 < 12 and tr.get('translateY', 0) / 12700 > 360:
                pg += [{'deleteText': {'objectId': el['objectId'], 'textRange': {'type': 'ALL'}}}, {'insertText': {'objectId': el['objectId'], 'insertionIndex': 0, 'text': str(pos)}}]
    if pg: svc.presentations().batchUpdate(presentationId=PID, body={'requests': pg}).execute(); print('page numbers', len(pg) // 2)
    # hollow status dot on the yield slide (left status is not live): copy style from the hollow dot on the right
    yd = bys[NEW['yd']]; dots = [el for el in yd.get('pageElements', []) if 'shape' in el and el['shape'].get('shapeType') == 'ELLIPSE']
    if len(dots) >= 2:
        left = min(dots, key=lambda el: el['transform'].get('translateX', 0))
        svc.presentations().batchUpdate(presentationId=PID, body={'requests': [{'updateShapeProperties': {'objectId': left['objectId'], 'shapeProperties': {
            'shapeBackgroundFill': {'solidFill': {'color': {'rgbColor': {'red': 1, 'green': 1, 'blue': 1}}}},
            'outline': {'outlineFill': {'solidFill': {'color': {'rgbColor': {'red': 0.243, 'green': 0.31, 'blue': 0.878}}}}, 'weight': {'magnitude': 1, 'unit': 'PT'}}},
            'fields': 'shapeBackgroundFill.solidFill.color,outline.outlineFill.solidFill.color,outline.weight'}}]}).execute(); print('yield status dot set to hollow')
    # order, then delete everything else
    reqs2 = [{'updateSlidesPosition': {'slideObjectIds': [sid], 'insertionIndex': i}} for i, sid in enumerate(ORDER)]
    keep = set(ORDER); live = [s['objectId'] for s in P['slides']]
    reqs2 += [{'deleteObject': {'objectId': s}} for s in live if s not in keep]
    svc.presentations().batchUpdate(presentationId=PID, body={'requests': reqs2}).execute()
    P = svc.presentations().get(presentationId=PID, fields='slides.objectId').execute()
    print('final slides:', len(P['slides']), 'order ok:', [s['objectId'] for s in P['slides']] == ORDER)

if __name__ == '__main__':
    main()
