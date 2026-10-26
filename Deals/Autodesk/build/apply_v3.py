# -*- coding: utf-8 -*-
"""26 Oct 2026 evening, after reading the deck as Autodesk's Head of Payments: coverage statement on slide 4, fit tiles and
published results on slide 6 (volume stats off), vault facts on slide 8, a closing 'ask' slide. Targeted, like restructure.py.
  python3 apply_v3.py"""
import sys, os, time, json, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); os.chdir(HERE)
import gs_lib as g
import build_deck as B
import content as C

s = g.svc(); pid = B.DECK
get = lambda: s.presentations().get(presentationId=pid).execute()


def main():
    P = get(); json.dump(P, open('backup_autodesk_prev3_' + time.strftime('%H%M%S') + '.json', 'w'))
    R = []
    for oid, t in C.PORT.items(): g.set_text_id(P, B.S['port'], oid, t, R)
    g.run(s, pid, R, 'port text')
    for key, draw, cc in (('orch', B.draw_orch, C.ORCH), ('subs', B.draw_subs, C.SUBS)):
        P = get(); p = g.clear_body(s, pid, P, B.S[key], kicker=cc['kicker'], title=cc['title']); draw(p); g.run(s, pid, p.R, key + ' body')
    P = get(); p = B.fresh(s, pid, P, 'ask', C.ASK['kicker'], C.ASK['title']); B.draw_ask(p); g.run(s, pid, p.R, 'ask body')
    P = get(); N = []
    for key in ('orch', 'subs', 'port', 'ask'): N += g.set_notes(s, pid, P, B.S[key], C.NOTES[key])
    g.run(s, pid, N, 'notes')
    g.finish(s, pid, [B.S[k] for k in B.ORDER])
    os.makedirs('thumbs_v10', exist_ok=True)
    P = get(); order = [x['objectId'] for x in P['slides']]
    for key in ('orch', 'subs', 'port', 'ask'):
        n = order.index(B.S[key]) + 1
        t = s.presentations().pages().getThumbnail(presentationId=pid, pageObjectId=B.S[key], thumbnailProperties_thumbnailSize='LARGE').execute()
        urllib.request.urlretrieve(t['contentUrl'], f'thumbs_v10/s{n:02d}.png'); print('thumb', key, n)


if __name__ == '__main__':
    main()
