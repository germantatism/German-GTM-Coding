# -*- coding: utf-8 -*-
"""Shared helpers for the Acebet proposal build (Slides API via service account). Deck id lives in pid.txt next to this file."""
import sys, os, json, warnings, re
warnings.filterwarnings('ignore')
sys.path.insert(0, '/Users/germantatis/Desktop/GTMCoding/Industry/AI/Higgsfield/build')
from engine import elements, text_of, replace_requests, run, TEXT_FIELDS
from google.oauth2 import service_account
from googleapiclient.discovery import build
HERE = os.path.dirname(os.path.abspath(__file__))
PID = os.environ.get('ACEBET_PID') or open(os.path.join(HERE, 'pid.txt')).read().strip()
WORK = os.environ.get('ACEBET_WORK', '/private/tmp/claude-501/-Users-germantatis-Desktop-GTMCoding/79b9e111-4187-4fd7-9475-2367c131665a/scratchpad/acebet')
os.makedirs(WORK, exist_ok=True)
SA = os.path.expanduser('~/.config/gsuite/sa.json')
def svc():
    creds = service_account.Credentials.from_service_account_file(SA, scopes=['https://www.googleapis.com/auth/presentations'])
    return build('slides', 'v1', credentials=creds, cache_discovery=False)
def drive():
    creds = service_account.Credentials.from_service_account_file(SA, scopes=['https://www.googleapis.com/auth/drive'])
    return build('drive', 'v3', credentials=creds, cache_discovery=False)
def thumbs(s, P, nums, prefix):
    import urllib.request
    for n in nums:
        r = s.presentations().pages().getThumbnail(presentationId=PID, pageObjectId=P['slides'][n - 1]['objectId'],
                thumbnailProperties_thumbnailSize='LARGE').execute()
        urllib.request.urlretrieve(r['contentUrl'], f"{WORK}/{prefix}_{n:02d}.png")
def runs(el):
    return [(te['textRun']['content'], {k: v for k, v in te['textRun'].get('style', {}).items() if k in TEXT_FIELDS})
            for te in el['shape']['text'].get('textElements', []) if 'textRun' in te and te['textRun'].get('content', '').strip()]
def fmt_requests(el, markup, styles=None, oid=None):
    """Replace all text of a shape. **x** segments take the style of the first bold run of the original element,
    the rest take the style of the first non-bold run (or the only style). oid overrides the target (for duplicated objects)."""
    oid = oid or el['objectId']; rr = styles or runs(el)
    reg = next((s for c, s in rr if not s.get('bold')), None); bold = next((s for c, s in rr if s.get('bold')), None)
    if reg is None and bold is None: reg = bold = {}
    if reg is None: reg = bold
    if bold is None: bold = dict(reg, bold=True)
    segs = []
    for i, part in enumerate(re.split(r'\*\*', markup)):
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
def two_run(el, head, tail, oid=None):
    """Replace text with head+tail: head takes the first run's style, tail the last run's style (big number + small suffix)."""
    oid = oid or el['objectId']; rr = runs(el)
    s0, s1 = rr[0][1], rr[-1][1]
    reqs = []
    if text_of(el).strip('\n'): reqs.append({'deleteText': {'objectId': oid, 'textRange': {'type': 'ALL'}}})
    reqs.append({'insertText': {'objectId': oid, 'insertionIndex': 0, 'text': head + tail}})
    for a, b, st in ((0, len(head), s0), (len(head), len(head) + len(tail), s1)):
        if st and b > a: reqs.append({'updateTextStyle': {'objectId': oid, 'textRange': {'type': 'FIXED_RANGE', 'startIndex': a, 'endIndex': b}, 'style': st, 'fields': ','.join(st.keys())}})
    return reqs, head + tail
def box_req(el, x, y, w, h, oid=None):
    size = el['size']
    return {'updatePageElementTransform': {'objectId': oid or el['objectId'], 'transform': {
        'scaleX': w * 12700 / size['width']['magnitude'], 'scaleY': h * 12700 / size['height']['magnitude'], 'shearX': 0, 'shearY': 0,
        'translateX': x * 12700, 'translateY': y * 12700, 'unit': 'EMU'}, 'applyMode': 'ABSOLUTE'}}
def geom(el, tr):
    return (tr.get('translateX', 0) / 12700, tr.get('translateY', 0) / 12700,
            el['size']['width']['magnitude'] * tr.get('scaleX', 1) / 12700, el['size']['height']['magnitude'] * tr.get('scaleY', 1) / 12700)
def image_req(new_id, page_id, url, x, y, w, h):
    return {'createImage': {'objectId': new_id, 'url': url, 'elementProperties': {'pageObjectId': page_id,
        'size': {'width': {'magnitude': w * 12700, 'unit': 'EMU'}, 'height': {'magnitude': h * 12700, 'unit': 'EMU'}},
        'transform': {'scaleX': 1, 'scaleY': 1, 'shearX': 0, 'shearY': 0, 'translateX': x * 12700, 'translateY': y * 12700, 'unit': 'EMU'}}}}
