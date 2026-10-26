# -*- coding: utf-8 -*-
"""26 Oct 2026 evening (German): slide 3 chips v2 (smaller, every method as a mark, card brands on Germany) and the
subscriptions slide redrawn as a process flow instead of the logo wall. Targeted, like restructure.py.
  python3 apply_v2.py"""
import sys, os, time, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); os.chdir(HERE)
import gs_lib as g
import build_deck as B
import content as C
import restructure as R0      # host(), run_with_image(), s, d, pid

CHIPS_FID_V2 = '1RN9hYHdRXAjwEKzDkPpyAD3byPNz89sp'   # new placeholder (new id, so the lh3 CDN never serves the v1 bytes)
s, pid, get = R0.s, R0.pid, R0.get


def main():
    print('host chips v2:', R0.host(CHIPS_FID_V2, os.path.join('assets', 'today_chips.png')))
    P = get(); json.dump(P, open('backup_autodesk_prev2_' + time.strftime('%H%M%S') + '.json', 'w'))
    p = g.clear_body(s, pid, P, B.S['today'], kicker=C.TODAY['kicker'], title=C.TODAY['title']); B.draw_today(p)
    ok = R0.run_with_image(p.R, 'today body')
    P = get(); p = g.clear_body(s, pid, P, B.S['subs'], kicker=C.SUBS['kicker'], title=C.SUBS['title']); B.draw_subs(p)
    g.run(s, pid, p.R, 'subs body (flow)')
    P = get(); N = []
    for key in ('today', 'subs'): N += g.set_notes(s, pid, P, B.S[key], C.NOTES[key])
    g.run(s, pid, N, 'notes')
    os.makedirs('thumbs_v7', exist_ok=True)
    import urllib.request
    for key, name in (('today', 's03'), ('subs', 's06')):
        t = s.presentations().pages().getThumbnail(presentationId=pid, pageObjectId=B.S[key], thumbnailProperties_thumbnailSize='LARGE').execute()
        urllib.request.urlretrieve(t['contentUrl'], f'thumbs_v7/{name}.png')
    print('chips placed:', ok, '| thumbs in thumbs_v7')


if __name__ == '__main__':
    main()
