"""fix_story_width.py <pid> [<ref_pid>] : widen the $100B+ number box on the story slide to the reference width (one-off for decks already post-built)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
NEW = sys.argv[1]; REF = sys.argv[2] if len(sys.argv) > 2 else '1Qu3JvldczchxT9TrXmUkU1bSso9ltTGvOt5peT3hHjQ'
prelude = open(os.path.join(HERE, 'sync_intro.py')).read().split('# ------------------------------------------------ 1. story slide')[0]
prelude = prelude.replace("SRC = '1Qu3JvldczchxT9TrXmUkU1bSso9ltTGvOt5peT3hHjQ'; DST = '1r7g6kFtX8ZENovd3-51qyx9M0369yYLahpwXEGeEHRY'", f"SRC = '{REF}'; DST = '{NEW}'")
sys.argv = [sys.argv[0]]; exec(prelude)
k = find(D[2], lambda e: text_of(e).strip() in ('$30B+', '$100B+')); r = find(S[2], lambda e: text_of(e).strip() == '$100B+')
e = k[0]; tf = dict(e['transform']); cur_w = e['size']['width']['magnitude'] * tf.get('scaleX', 1)
ref_w = r[0]['size']['width']['magnitude'] * r[0]['transform'].get('scaleX', 1)
print('current width', cur_w, 'reference', ref_w)
if abs(ref_w - cur_w) > 1000:
    tf['scaleX'] = tf.get('scaleX', 1) * ref_w / cur_w
    run([{'updatePageElementTransform': {'objectId': e['objectId'], 'applyMode': 'ABSOLUTE', 'transform': {'scaleX': tf['scaleX'], 'scaleY': tf.get('scaleY', 1), 'shearX': tf.get('shearX', 0), 'shearY': tf.get('shearY', 0), 'translateX': tf.get('translateX', 0), 'translateY': tf.get('translateY', 0), 'unit': 'EMU'}}}], 'story width')
