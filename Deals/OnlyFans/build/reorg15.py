# -*- coding: utf-8 -*-
"""15-slide version, built on a fresh copy of German's 28-slide 'Token Vault Revised' deck.
Everything from reorg10.py plus the five slides a head of tokenization would ask for:
vault-only option (19), access per role (17), network tokens and PAR (15), proxy request (18), portability and exit (20).
Requestor-ID claims are softened to what our API reference supports.
Usage: python3 reorg15.py <presentation_id> [--dry]"""
import sys, os, json, warnings
warnings.filterwarnings('ignore')
sys.argv_backup = list(sys.argv)
import reorg10 as B

S = dict(B.S)
S.update({15: 'h7c266de662ba1cf0_9_207', 17: 'h7c266de662ba1cf0_9_316', 18: 'h7c266de662ba1cf0_9_391',
          19: 'h7c266de662ba1cf0_9_421', 20: 'h7c266de662ba1cf0_9_469'})
NEW = B.NEW
ORDER = [S[1], S[4], S[5], S[6], S[19], S[16], S[17], S[15], S[18], S[20],
         NEW['bc'], NEW['rl'], NEW['yd'], S[23], S[28]]
R = B.R
BASE_EDITS = B.edits

def edits():
    e = BASE_EDITS()
    e += [R(S[19], '2 · OUR PROPOSAL  ›  YOUR WAY  ›  OPTIONS', 'YOUR WAY  ›  VAULT ONLY OR WITH SERVICES'),
          R(S[17], '2 · OUR PROPOSAL  ›  VAULT  ›  ACCESS', 'THE VAULT  ›  ACCESS'),
          R(S[15], '2 · OUR PROPOSAL  ›  VAULT  ›  NETWORK TOKENS', 'THE VAULT  ›  NETWORK TOKENS'),
          R(S[15], 'Token requestor ID registered under OnlyFans where the scheme\x0ballows it. Yuno acts as TS-TRP.',
            'Token requestor model and scheme activation per network:\x0bconfirmed in writing with the RFP.'),
          R(S[18], '2 · OUR PROPOSAL  ›  PROXY  ›  HOW IT WORKS', 'THE PROXY  ›  HOW IT WORKS'),
          R(S[20], '2 · OUR PROPOSAL  ›  YOUR WAY  ›  PORTABILITY', 'YOUR WAY  ›  PORTABILITY'),
          R(S[20], "Registered under OnlyFans' token requestor ID\x0bwhere the scheme allows it, so they survive a\x0bchange of processor or of vault. No\x0bre-tokenization on exit.",
            'Card data exports in full, so tokens can be\x0bre-provisioned with any vault. Requestor\x0bmodel per network confirmed in writing\x0bwith the RFP.')]
    return e

POST = [  # fixes applied by hand on the 10-slide copy after its first review
    (NEW['bc'], 'One account per creator', 'Creator accounts'),
    (NEW['bc'], 'Sets the rules: which bank,', 'One per creator.'),
    (NEW['bc'], 'issuer and rail each creator uses.', 'You set bank, issuer and rail.'),
    (NEW['bc'], 'Plugged in or swapped by configuration', 'Swapped by configuration'),
    (NEW['bc'], 'Balances in one view', 'One balance view'),
    (NEW['rl'], 'Per-call bank choice live today', 'Per call: live'),
    (NEW['rl'], 'ACH, wire and RTP live', 'Rails live'),
    (NEW['rl'], 'Rules and failover proposed', 'Rules proposed'),
    (NEW['yd'], 'Partners confirmed in writing', 'To confirm'),
    (NEW['yd'], 'Proxy to issuer APIs (beta)', 'Proxy: beta'),
    (NEW['yd'], 'Issuer partners to confirm', 'To confirm'),
]

def main():
    pid = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('--') else None
    B.S, B.ORDER = S, ORDER
    B.edits = edits
    reqs = edits()
    if B.check_against_dump(reqs) or '--dry' in sys.argv or not pid: return
    sys.argv = [sys.argv[0], pid]
    B.PID = pid
    B.main()
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    creds = service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'), scopes=['https://www.googleapis.com/auth/presentations'])
    svc = build('slides', 'v1', credentials=creds, cache_discovery=False)
    rq = [R(p, a, b) for p, a, b in POST]
    P = svc.presentations().get(presentationId=pid).execute()
    yd = next(s for s in P['slides'] if s['objectId'] == NEW['yd'])
    svc.presentations().batchUpdate(presentationId=pid, body={'requests': rq}).execute()
    # left "To confirm" on the yield slide in the same blue as the right one
    P = svc.presentations().get(presentationId=pid).execute()
    yd = next(s for s in P['slides'] if s['objectId'] == NEW['yd'])
    t = lambda el: ''.join(te.get('textRun', {}).get('content', '') for te in el.get('shape', {}).get('text', {}).get('textElements', [])).strip()
    tc = [el for el in yd['pageElements'] if t(el) == 'To confirm']
    if len(tc) == 2:
        right = max(tc, key=lambda e: e['transform'].get('translateX', 0)); left = min(tc, key=lambda e: e['transform'].get('translateX', 0))
        col = next(te['textRun']['style'].get('foregroundColor') for te in right['shape']['text']['textElements'] if 'textRun' in te)
        svc.presentations().batchUpdate(presentationId=pid, body={'requests': [{'updateTextStyle': {'objectId': left['objectId'], 'textRange': {'type': 'ALL'}, 'style': {'foregroundColor': col}, 'fields': 'foregroundColor'}}]}).execute()
    print('post fixes applied')

if __name__ == '__main__':
    main()
