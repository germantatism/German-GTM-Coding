# -*- coding: utf-8 -*-
"""Shared helpers for the UNICEF Colombia proposal build (Slides API via service account)."""
import sys, os, json, warnings
warnings.filterwarnings('ignore')
sys.path.insert(0, '/Users/germantatis/Desktop/GTMCoding/Industry/AI/Higgsfield/build')
from engine import elements, text_of, replace_requests, run, pos, TEXT_FIELDS
from google.oauth2 import service_account
from googleapiclient.discovery import build
PID = '111EW1tmbSYPYtxLYRa5Mf_yx0Cn-BxA4wT2FAZeGpe0'
WORK = '/private/tmp/claude-501/-Users-germantatis-Desktop-GTMCoding/9370c6dc-908f-4e40-b6bc-431ca9d296b0/scratchpad/unicef'
os.makedirs(WORK, exist_ok=True)
def svc():
    creds = service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'),
            scopes=['https://www.googleapis.com/auth/presentations'])
    return build('slides', 'v1', credentials=creds, cache_discovery=False)
def thumbs(s, P, nums, prefix):
    import urllib.request
    for n in nums:
        r = s.presentations().pages().getThumbnail(presentationId=PID, pageObjectId=P['slides'][n - 1]['objectId'],
                thumbnailProperties_thumbnailSize='LARGE').execute()
        urllib.request.urlretrieve(r['contentUrl'], f"{WORK}/{prefix}_{n:02d}.png")

# ---------- rich text replace: "plain **bold** plain" keeps the original regular / bold run styles ----------
import re as _re
def _runs(el):
    return [(te['textRun']['content'], {k: v for k, v in te['textRun'].get('style', {}).items() if k in TEXT_FIELDS})
            for te in el['shape']['text'].get('textElements', []) if 'textRun' in te and te['textRun'].get('content', '').strip()]
def fmt_requests(el, markup, styles=None):
    """Replace all text of a shape. **x** segments take the style of the first bold run of the original element,
    the rest take the style of the first non-bold run (or the first run when there is only one style)."""
    oid = el['objectId']; rr = styles or _runs(el)
    reg = next((s for c, s in rr if not s.get('bold')), None); bold = next((s for c, s in rr if s.get('bold')), None)
    if reg is None and bold is None: reg = bold = {}
    if reg is None: reg = bold
    if bold is None: bold = dict(reg, bold=True)
    segs = []
    for i, part in enumerate(_re.split(r'\*\*', markup)):
        if part: segs.append((part, i % 2 == 1))
    text = ''.join(p for p, b in segs)
    reqs = []
    if text_of(el).strip('\n'): reqs.append({'deleteText': {'objectId': oid, 'textRange': {'type': 'ALL'}}})
    reqs.append({'insertText': {'objectId': oid, 'insertionIndex': 0, 'text': text}})
    i = 0
    for part, b in segs:
        st = dict(bold if b else reg); st.setdefault('bold', bool(b))
        reqs.append({'updateTextStyle': {'objectId': oid, 'textRange': {'type': 'FIXED_RANGE', 'startIndex': i, 'endIndex': i + len(part)},
                                         'style': st, 'fields': ','.join(st.keys())}})
        i += len(part)
    return reqs, text
def box_req(el, x, y, w, h):
    size = el['size']
    return {'updatePageElementTransform': {'objectId': el['objectId'], 'transform': {
        'scaleX': w * 12700 / size['width']['magnitude'], 'scaleY': h * 12700 / size['height']['magnitude'], 'shearX': 0, 'shearY': 0,
        'translateX': x * 12700, 'translateY': y * 12700, 'unit': 'EMU'}, 'applyMode': 'ABSOLUTE'}}
def geom(el, tr):
    return (tr.get('translateX', 0) / 12700, tr.get('translateY', 0) / 12700,
            el['size']['width']['magnitude'] * tr.get('scaleX', 1) / 12700, el['size']['height']['magnitude'] * tr.get('scaleY', 1) / 12700)
