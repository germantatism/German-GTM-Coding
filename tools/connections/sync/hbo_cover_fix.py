import os, sys, json, io, base64, urllib.request
sys.argv=[sys.argv[0]]
src_code = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sync_intro.py')).read().split('# ------------------------------------------------ 1. story slide')[0]
src_code = src_code.replace("SRC = '1Qu3JvldczchxT9TrXmUkU1bSso9ltTGvOt5peT3hHjQ'; DST = '1r7g6kFtX8ZENovd3-51qyx9M0369yYLahpwXEGeEHRY'", "SRC = '1TyFXKt2OfoBLHGn8T1xX_Z1Uic_5ZYeeGUb8g_n0jrw'; DST = '1vULwizzS9eoNpyOYCOEfxGDkZegRp_9bmPgPhUAy2zo'")
exec(src_code)
sky = [e for e in S[0]['pageElements'] if e['objectId'].endswith('_0_1255')][0]
print('skydance props:', json.dumps(sky['image'].get('imageProperties'))[:300])
raw = urllib.request.urlopen(sky['image']['contentUrl'], timeout=30).read()
from PIL import Image
im = Image.open(io.BytesIO(raw)).convert('RGBA'); print('skydance png', im.size, 'center px', im.getpixel((im.width//2, im.height//2)), 'corner', im.getpixel((0, 0)))
px = im.load(); dark = 0; light = 0
for y in range(im.height):
    for x in range(im.width):
        r, g, b, a = px[x, y]
        if a:
            if r + g + b < 384: dark += 1
            else: light += 1
            px[x, y] = (255, 255, 255, a)
print('opaque dark', dark, 'light', light)
out = io.BytesIO(); im.save(out, 'PNG'); data = out.getvalue()
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dl', 'skydance_white.png'), 'wb').write(data)
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dl', 'skydance_white.b64'), 'w').write(base64.b64encode(data).decode())
print('b64 chars', len(base64.b64encode(data)))
bar = [e for e in S[0]['pageElements'] if e['objectId'] == 'sky_cv_bar'][0]
run(clone_shape(bar, D[0]['objectId'])[1], 'cover bar')
