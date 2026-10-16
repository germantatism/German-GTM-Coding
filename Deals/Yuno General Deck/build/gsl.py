# -*- coding: utf-8 -*-
"""gsl.py · small Google Slides drawing library in the OnlyFans deck style (Titillium Web, blue bar headlines).

Base presentation: a Drive copy of the OnlyFans Token Vault deck (1hrBLCFx...), shared as writer with the
service account gtm-claude-editor@. New content slides duplicate the "trusted by" slide for its chrome
(background, kicker, headline, blue bar, page number, wordmark) and draw everything else with primitives.
"""
import os, re, json, uuid, time, warnings
warnings.filterwarnings('ignore')
from google.oauth2 import service_account
from googleapiclient.discovery import build as gbuild

SA = os.path.expanduser('~/.config/gsuite/sa.json')
PT = 12700
FONT = 'Titillium Web'

# palette (OnlyFans deck, as stored)
BLUE, DEEP, INK, GREY = '#3E4FE0', '#2638BF', '#282A30', '#75787F'
BODY = '#454C58'
PANEL, PILL, BORDER, LINE = '#F4F5FD', '#E8EAF5', '#E2E3E6', '#C9CDD6'
WHITE, DARK, GREEN, RED = '#FFFFFF', '#282A30', '#1F8A5B', '#B4483C'
LAV = '#BDC3F6'


def service():
    c = service_account.Credentials.from_service_account_file(
        SA, scopes=['https://www.googleapis.com/auth/presentations'])
    return gbuild('slides', 'v1', credentials=c, cache_discovery=False)


def emu(v): return int(round(v * PT))


def rgb(h):
    h = h.lstrip('#')
    return {'red': int(h[0:2], 16) / 255, 'green': int(h[2:4], 16) / 255, 'blue': int(h[4:6], 16) / 255}


def nid(prefix='g'):
    return f'{prefix}_{uuid.uuid4().hex[:12]}'


class Slide:
    """Collects requests for one slide."""
    def __init__(self, page_id):
        self.page = page_id
        self.reqs = []

    def _create(self, oid, kind, x, y, w, h):
        self.reqs.append({'createShape': {'objectId': oid, 'shapeType': kind, 'elementProperties': {
            'pageObjectId': self.page,
            'size': {'width': {'magnitude': emu(w), 'unit': 'EMU'}, 'height': {'magnitude': emu(h), 'unit': 'EMU'}},
            'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': emu(x), 'translateY': emu(y), 'unit': 'EMU'}}}})

    def rect(self, x, y, w, h, fill=None, outline=None, weight=0.75, kind='RECTANGLE', dash=None):
        oid = nid('r')
        self._create(oid, kind, x, y, w, h)
        props, fields = {}, []
        if fill:
            props['shapeBackgroundFill'] = {'solidFill': {'color': {'rgbColor': rgb(fill)}}}
        else:
            props['shapeBackgroundFill'] = {'propertyState': 'NOT_RENDERED'}
        fields.append('shapeBackgroundFill')
        if outline:
            props['outline'] = {'outlineFill': {'solidFill': {'color': {'rgbColor': rgb(outline)}}},
                                'weight': {'magnitude': weight, 'unit': 'PT'}}
            if dash: props['outline']['dashStyle'] = dash
        else:
            props['outline'] = {'propertyState': 'NOT_RENDERED'}
        fields.append('outline')
        self.reqs.append({'updateShapeProperties': {'objectId': oid, 'shapeProperties': props, 'fields': ','.join(fields)}})
        return oid

    def text(self, x, y, w, h, txt, size=9, color=INK, weight=400, align='START', valign='TOP',
             spacing=100, fill=None, outline=None, kind='TEXT_BOX', bold_color=None, space_below=0, inset=True):
        """Text box; x/y/w/h are the VISUAL text area (Slides' 7.2 pt insets are compensated when inset=True).
        `**bold**` markup renders weight 700 (or bold_color)."""
        ix = 7.2 if inset else 0
        oid = nid('t')
        self._create(oid, kind, x - ix, y - ix, w + 2 * ix, h + 2 * ix)
        plain, bolds = '', []
        for i, part in enumerate(re.split(r'\*\*', txt)):
            if i % 2 == 1:
                bolds.append((len(plain), len(plain) + len(part)))
            plain += part
        if not plain:
            return oid
        self.reqs.append({'insertText': {'objectId': oid, 'text': plain}})
        self.reqs.append({'updateTextStyle': {'objectId': oid, 'textRange': {'type': 'ALL'}, 'style': {
            'weightedFontFamily': {'fontFamily': FONT, 'weight': weight}, 'fontSize': {'magnitude': size, 'unit': 'PT'},
            'foregroundColor': {'opaqueColor': {'rgbColor': rgb(color)}}},
            'fields': 'weightedFontFamily,fontSize,foregroundColor'}})
        for a, b in bolds:
            st = {'weightedFontFamily': {'fontFamily': FONT, 'weight': 700}}
            f = 'weightedFontFamily'
            if bold_color:
                st['foregroundColor'] = {'opaqueColor': {'rgbColor': rgb(bold_color)}}; f += ',foregroundColor'
            self.reqs.append({'updateTextStyle': {'objectId': oid, 'textRange': {'type': 'FIXED_RANGE', 'startIndex': a, 'endIndex': b}, 'style': st, 'fields': f}})
        self.reqs.append({'updateParagraphStyle': {'objectId': oid, 'textRange': {'type': 'ALL'}, 'style': {
            'alignment': align, 'lineSpacing': spacing, 'spaceAbove': {'magnitude': 0, 'unit': 'PT'},
            'spaceBelow': {'magnitude': space_below, 'unit': 'PT'}}, 'fields': 'alignment,lineSpacing,spaceAbove,spaceBelow'}})
        props = {'contentAlignment': valign}
        fields = ['contentAlignment']
        if fill:
            props['shapeBackgroundFill'] = {'solidFill': {'color': {'rgbColor': rgb(fill)}}}; fields.append('shapeBackgroundFill')
        if outline:
            props['outline'] = {'outlineFill': {'solidFill': {'color': {'rgbColor': rgb(outline)}}}, 'weight': {'magnitude': 0.75, 'unit': 'PT'}}
            fields.append('outline')
        elif kind != 'TEXT_BOX':
            props['outline'] = {'propertyState': 'NOT_RENDERED'}; fields.append('outline')
        self.reqs.append({'updateShapeProperties': {'objectId': oid, 'shapeProperties': props, 'fields': ','.join(fields)}})
        return oid

    def pill(self, x, y, w, h, txt, fill=PILL, color=BLUE, size=7, weight=600, outline=None):
        """Rounded label with centred text (no insets)."""
        oid = self.rect(x, y, w, h, fill=fill, outline=outline, kind='ROUND_RECTANGLE')
        self.reqs.append({'insertText': {'objectId': oid, 'text': txt}})
        self.reqs.append({'updateTextStyle': {'objectId': oid, 'textRange': {'type': 'ALL'}, 'style': {
            'weightedFontFamily': {'fontFamily': FONT, 'weight': weight}, 'fontSize': {'magnitude': size, 'unit': 'PT'},
            'foregroundColor': {'opaqueColor': {'rgbColor': rgb(color)}}}, 'fields': 'weightedFontFamily,fontSize,foregroundColor'}})
        self.reqs.append({'updateParagraphStyle': {'objectId': oid, 'textRange': {'type': 'ALL'}, 'style': {'alignment': 'CENTER'}, 'fields': 'alignment'}})
        self.reqs.append({'updateShapeProperties': {'objectId': oid, 'shapeProperties': {'contentAlignment': 'MIDDLE'}, 'fields': 'contentAlignment'}})
        return oid

    def line(self, x1, y1, x2, y2, color=LINE, weight=1, arrow=False, dash=None):
        oid = nid('l')
        x, y = min(x1, x2), min(y1, y2)
        w, h = max(abs(x2 - x1), 0.01), max(abs(y2 - y1), 0.01)
        cat = 'STRAIGHT'
        self.reqs.append({'createLine': {'objectId': oid, 'lineCategory': cat, 'elementProperties': {
            'pageObjectId': self.page,
            'size': {'width': {'magnitude': emu(w), 'unit': 'EMU'}, 'height': {'magnitude': emu(h), 'unit': 'EMU'}},
            'transform': {'scaleX': -1 if x2 < x1 else 1, 'scaleY': -1 if y2 < y1 else 1,
                          'translateX': emu(x if x2 >= x1 else x1), 'translateY': emu(y if y2 >= y1 else y1), 'unit': 'EMU'}}}})
        lp = {'lineFill': {'solidFill': {'color': {'rgbColor': rgb(color)}}}, 'weight': {'magnitude': weight, 'unit': 'PT'}}
        f = 'lineFill,weight'
        if arrow:
            lp['endArrow'] = 'FILL_ARROW'; f += ',endArrow'
        if dash:
            lp['dashStyle'] = dash; f += ',dashStyle'
        self.reqs.append({'updateLineProperties': {'objectId': oid, 'lineProperties': lp, 'fields': f}})
        return oid

    def image(self, url, x, y, w, h):
        oid = nid('i')
        self.reqs.append({'createImage': {'objectId': oid, 'url': url, 'elementProperties': {
            'pageObjectId': self.page,
            'size': {'width': {'magnitude': emu(w), 'unit': 'EMU'}, 'height': {'magnitude': emu(h), 'unit': 'EMU'}},
            'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': emu(x), 'translateY': emu(y), 'unit': 'EMU'}}}})
        return oid

    def set_text(self, oid, txt):
        """Replace the text of an existing element, keeping the style of its first run."""
        self.reqs.append({'deleteText': {'objectId': oid, 'textRange': {'type': 'ALL'}}})
        self.reqs.append({'insertText': {'objectId': oid, 'text': txt, 'insertionIndex': 0}})

    def style_all(self, oid, size, color, weight=400):
        self.reqs.append({'updateTextStyle': {'objectId': oid, 'textRange': {'type': 'ALL'}, 'style': {
            'weightedFontFamily': {'fontFamily': FONT, 'weight': weight}, 'fontSize': {'magnitude': size, 'unit': 'PT'},
            'foregroundColor': {'opaqueColor': {'rgbColor': rgb(color)}}}, 'fields': 'weightedFontFamily,fontSize,foregroundColor'}})

    # ---------------------------------------------------------------- composite helpers
    def check(self, x, y, txt, size=9, w=260, ok=True, color=INK):
        """Round blue tick (or grey cross) plus one line of text."""
        if ok:
            self.rect(x, y + 1.5, 11, 11, fill=BLUE, kind='ELLIPSE')
            self.text(x, y + 1.5, 11, 11, '✓', size=6.5, color=WHITE, weight=700, align='CENTER', valign='MIDDLE')
        else:
            self.text(x, y + 1, 11, 12, '×', size=10, color=GREY, weight=600, align='CENTER', valign='MIDDLE')
        self.text(x + 17, y, w, 14, txt, size=size, color=color)
