# -*- coding: utf-8 -*-
"""Build the "06 · Proposal" section for the deck "Business Case Yango + Yuno" through the Google Slides API.

Auth: service account key ~/.config/gsuite/sa.json (gtm-claude-editor@gtm-claude-tools-260922.iam.gserviceaccount.com).

Two modes:
  scratch (default)   creates a new presentation owned by the service account, builds divider + 2 content slides,
                      exports a PDF for QA and shares the deck with German as editor (File > Import slides).
      python3 yango_proposal_slides.py [--pdf out.pdf] [--share german.tatis@y.uno]

  --pid <deck id>     inserts the section into the real deck (must be shared with the service account as Editor):
                      agenda line on slide 2, divider duplicated from slide 29, two content slides after slide 34.
      python3 yango_proposal_slides.py --pid 1txk0atU1_2jUcEva6WYIQjvNlUp4yO_BPuWHzATOnQw --dry   # inventory only
      python3 yango_proposal_slides.py --pid 1txk0atU1_2jUcEva6WYIQjvNlUp4yO_BPuWHzATOnQw

Numbers come from build/yango_pricing_model.py (verified 2026-09-22). Copy is the same as
claude-design-prompt-proposal-section-2026-09-22.md.
"""
import argparse, os, sys, re
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SA_KEY = os.path.expanduser('~/.config/gsuite/sa.json')
SCOPES = ['https://www.googleapis.com/auth/presentations', 'https://www.googleapis.com/auth/drive']
EMU = 12700
FONT = 'Titillium Web'
LOGO = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'Design System', 'yuno-wordmark-cropped.png')  # cropped from 'yuno logo2.png' (1080x1080 with padding)

# palette taken from the deck's PDF export (slides 15, 16, 31, 32) and the FlightHub pricing slide
BLUE, DARKBLUE = '#3E4FE0', '#3143C2'
DARK, INK, GREY, GREY2, LIGHT, PGNUM, FOOT = '#1A1D2A', '#282A30', '#6E7284', '#5A5F78', '#92959B', '#C6CBE6', '#9A9DAB'
LAV, PALE, PANEL, BORDER, WHITE = '#EEF0FF', '#F7F8FC', '#F3F4F8', '#E3E5F0', '#FFFFFF'
DIVIDER_BG = '#141B63'

def hexrgb(h):
    h = h.lstrip('#'); return {'red': int(h[0:2], 16) / 255, 'green': int(h[2:4], 16) / 255, 'blue': int(h[4:6], 16) / 255}

class Builder:
    """Collects batchUpdate requests. Coordinates in pt on a 720 x 405 page."""
    def __init__(self, prefix):
        self.reqs = []; self.n = 0; self.prefix = prefix
    def nid(self, tag='el'):
        self.n += 1; return f'{self.prefix}_{tag}_{self.n}'
    def _props(self, page, x, y, w, h):
        return {'pageObjectId': page,
                'size': {'width': {'magnitude': w * EMU, 'unit': 'EMU'}, 'height': {'magnitude': h * EMU, 'unit': 'EMU'}},
                'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': x * EMU, 'translateY': y * EMU, 'unit': 'EMU'}}
    def slide(self, insertion_index=None, background=None):
        sid = self.nid('slide')
        r = {'objectId': sid, 'slideLayoutReference': {'predefinedLayout': 'BLANK'}}
        if insertion_index is not None: r['insertionIndex'] = insertion_index
        self.reqs.append({'createSlide': r})
        if background:
            self.reqs.append({'updatePageProperties': {'objectId': sid, 'fields': 'pageBackgroundFill',
                              'pageProperties': {'pageBackgroundFill': {'solidFill': {'color': {'rgbColor': hexrgb(background)}}}}}})
        return sid
    def rect(self, page, x, y, w, h, fill=None, stroke=None, stroke_w=0.75, alpha=1.0):
        oid = self.nid('rect')
        self.reqs.append({'createShape': {'objectId': oid, 'shapeType': 'RECTANGLE', 'elementProperties': self._props(page, x, y, w, h)}})
        sp = {}
        if fill:
            sp['shapeBackgroundFill'] = {'solidFill': {'color': {'rgbColor': hexrgb(fill)}, 'alpha': alpha}}
        else:
            sp['shapeBackgroundFill'] = {'propertyState': 'NOT_RENDERED'}
        if stroke:
            sp['outline'] = {'outlineFill': {'solidFill': {'color': {'rgbColor': hexrgb(stroke)}}}, 'weight': {'magnitude': stroke_w * EMU, 'unit': 'EMU'}}
        else:
            sp['outline'] = {'propertyState': 'NOT_RENDERED'}
        self.reqs.append({'updateShapeProperties': {'objectId': oid, 'fields': 'shapeBackgroundFill,outline', 'shapeProperties': sp}})
        return oid
    def hline(self, page, x, y, w, color=BORDER, weight=0.6, alpha=1.0):
        oid = self.nid('line')
        self.reqs.append({'createLine': {'objectId': oid, 'lineCategory': 'STRAIGHT', 'elementProperties': self._props(page, x, y, w, 0.01)}})
        self.reqs.append({'updateLineProperties': {'objectId': oid, 'fields': 'lineFill,weight',
                          'lineProperties': {'lineFill': {'solidFill': {'color': {'rgbColor': hexrgb(color)}, 'alpha': alpha}},
                                             'weight': {'magnitude': weight * EMU, 'unit': 'EMU'}}}})
        return oid
    def vline(self, page, x, y, h, color=BORDER, weight=0.6, alpha=1.0):
        oid = self.nid('vline')
        self.reqs.append({'createLine': {'objectId': oid, 'lineCategory': 'STRAIGHT', 'elementProperties': self._props(page, x, y, 0.01, h)}})
        self.reqs.append({'updateLineProperties': {'objectId': oid, 'fields': 'lineFill,weight',
                          'lineProperties': {'lineFill': {'solidFill': {'color': {'rgbColor': hexrgb(color)}, 'alpha': alpha}},
                                             'weight': {'magnitude': weight * EMU, 'unit': 'EMU'}}}})
        return oid
    def text(self, page, x, y, w, h, runs, size=8, color=DARK, bold=False, italic=False, align='START', valign='TOP', line_spacing=100):
        """runs: a string, or a list of (text, {size,color,bold,italic}) tuples. Box coordinates are CONTENT coordinates;
        the API text box insets (7.2 pt left/right, 3.6 pt top/bottom) are compensated here."""
        oid = self.nid('txt')
        self.reqs.append({'createShape': {'objectId': oid, 'shapeType': 'TEXT_BOX',
                          'elementProperties': self._props(page, x - 7.2, y - 3.6, w + 14.4, h + 7.2)}})
        self.reqs.append({'updateShapeProperties': {'objectId': oid, 'fields': 'contentAlignment,autofit.autofitType',
                          'shapeProperties': {'contentAlignment': valign, 'autofit': {'autofitType': 'NONE'}}}})
        if isinstance(runs, str): runs = [(runs, {})]
        full = ''.join(t for t, _ in runs)
        if not full: return oid
        self.reqs.append({'insertText': {'objectId': oid, 'insertionIndex': 0, 'text': full}})
        base = {'fontFamily': FONT, 'fontSize': {'magnitude': size, 'unit': 'PT'}, 'bold': bold, 'italic': italic,
                'foregroundColor': {'opaqueColor': {'rgbColor': hexrgb(color)}}}
        self.reqs.append({'updateTextStyle': {'objectId': oid, 'textRange': {'type': 'ALL'}, 'style': base,
                          'fields': 'fontFamily,fontSize,bold,italic,foregroundColor'}})
        pos = 0
        for t, st in runs:
            if st and t:
                style = {}
                fields = []
                if 'size' in st: style['fontSize'] = {'magnitude': st['size'], 'unit': 'PT'}; fields.append('fontSize')
                if 'color' in st: style['foregroundColor'] = {'opaqueColor': {'rgbColor': hexrgb(st['color'])}}; fields.append('foregroundColor')
                if 'bold' in st: style['bold'] = st['bold']; fields.append('bold')
                if 'italic' in st: style['italic'] = st['italic']; fields.append('italic')
                self.reqs.append({'updateTextStyle': {'objectId': oid, 'textRange': {'type': 'FIXED_RANGE', 'startIndex': pos, 'endIndex': pos + len(t)},
                                  'style': style, 'fields': ','.join(fields)}})
            pos += len(t)
        self.reqs.append({'updateParagraphStyle': {'objectId': oid, 'textRange': {'type': 'ALL'},
                          'style': {'alignment': align, 'lineSpacing': line_spacing, 'spaceAbove': {'magnitude': 0, 'unit': 'PT'}, 'spaceBelow': {'magnitude': 0, 'unit': 'PT'}},
                          'fields': 'alignment,lineSpacing,spaceAbove,spaceBelow'}})
        return oid
    def image(self, page, url, x, y, w, h):
        oid = self.nid('img')
        self.reqs.append({'createImage': {'objectId': oid, 'url': url, 'elementProperties': self._props(page, x, y, w, h)}})
        return oid

# ----------------------------------------------------------------------------------------------------------------
# Slide content
# ----------------------------------------------------------------------------------------------------------------
def chrome(b, page, eyebrow, title, page_no, footer=None, logo_url=None, title_size=22):
    b.vline(page, 28.5, 0, 405, color=BORDER, weight=0.5)
    b.text(page, 33.6, 9, 300, 12, eyebrow, size=9, color=LIGHT)
    b.rect(page, 26.8, 36.5, 3.2, 9, fill=BLUE)
    b.text(page, 44.8, 26, 620, 30, title, size=title_size, color=BLUE)
    b.text(page, 9.9, 386, 20, 10, page_no, size=7, color=PGNUM)
    if footer: b.text(page, 33, 386, 500, 10, footer, size=6, color=FOOT)
    if logo_url:
        w, h = 46, 14
        try:
            from PIL import Image
            im = Image.open(LOGO).convert('RGBA'); bb = im.getbbox()
            if bb: w = round(h * (bb[2] - bb[0]) / (bb[3] - bb[1]), 1)
        except Exception: pass
        b.image(page, logo_url, 690 - w, 11.5, w, h)

def slide_divider(b, page, number='06', label='Proposal'):
    b.hline(page, 55, 253, 590, color=WHITE, weight=0.6, alpha=0.35)
    b.rect(page, 55, 252.2, 14, 1.6, fill=WHITE)
    b.text(page, 55, 262, 100, 12, number, size=8, color=WHITE)
    b.text(page, 55, 280, 500, 40, label, size=30, color=WHITE)

def slide_pricing(b, page, page_no, logo_url=None):
    chrome(b, page, 'Proposal', 'Proposal · Platform fee plus a variable rate on approved recharges', page_no,
           footer='3 year term, rates locked, tranches reviewed annually as volume grows. All figures in USD.', logo_url=logo_url)
    # ---- left card
    b.rect(page, 31.5, 84.3, 198.6, 281.2, fill=WHITE, stroke=BORDER, stroke_w=0.75)
    x = 41.6
    b.text(page, x, 91.5, 180, 10, 'TRANSACTION FEE', size=8, bold=True)
    b.text(page, x, 104, 180, 24, "A percentage of the month's approved recharge volume, across Colombia, Peru, Bolivia and Venezuela", size=7.5, color=GREY)
    rows = [('TRANCHE 1', '$0 to $2.5M a month', '0.60%'), ('TRANCHE 2', '$2.5M to $5M', '0.50%'), ('TRANCHE 3', 'Above $5M', '0.45%')]
    y = 137
    for i, (lab, rng, rate) in enumerate(rows):
        b.text(page, x, y, 110, 9, lab, size=7, bold=True, color=GREY2)
        b.text(page, x, y + 9.6, 120, 11, rng, size=8)
        b.text(page, 150, y - 9, 70, 22, rate, size=14, bold=True, align='END', valign='MIDDLE')
        if i < 2: b.hline(page, x, y + 29, 178.6)
        y += 40
    b.rect(page, 40.9, 296, 179.8, 60, fill=PALE)
    b.text(page, 48, 300, 166, 52, "No setup fee. No fixed fee per transaction. Declines and card verification attempts cost nothing. Each tranche applies only to the volume inside it, so Yango's highest volume always pays the lowest rate.", size=7.5, color='#4A4E60')
    # ---- middle card
    b.rect(page, 239.1, 84.3, 215.9, 281.2, fill=LAV)
    x = 248.9
    b.text(page, x, 90.5, 150, 10, 'PLATFORM FEE', size=8, bold=True)
    b.text(page, x, 99, 190, 26, [('$10,000', {'size': 22, 'bold': True, 'color': BLUE}), ('  / month', {'size': 10, 'color': GREY2})], size=22, valign='BOTTOM')
    b.text(page, x, 130, 190, 10, '$120,000 / year. This is what covers the stack.', size=7.5, color='#4A4E60')
    b.text(page, x, 147, 150, 10, 'WHAT IT INCLUDES', size=8, bold=True, color=GREY2)
    inc = [('Dedicated KAM and TAM', 'Included'), ('Payment methods', '+1,000'), ('Payment providers', '+450'), ('Anti-fraud tools', '+50'),
           ('Orchestration & rules engine', 'Included'), ('Smart routing & retries', 'Included'), ('Monitors & auto-failover', 'Included'),
           ('PCI token vault', 'Included'), ('Reporting & dashboard', 'Included')]
    y = 160
    for lab, val in inc:
        b.text(page, x, y, 140, 10, lab, size=7.5)
        b.text(page, 370, y, 74.5, 10, val, size=7.5, bold=True, align='END')
        b.hline(page, x, y + 11.3, 195.6, color='#D9DCF0', weight=0.5)
        y += 13.2
    # add-ons box
    b.rect(page, 244.7, 283, 204.7, 58, fill=WHITE)
    b.text(page, 250.9, 286.5, 60, 9, 'ADD-ONS', size=6.5, bold=True, color=GREY2)
    b.text(page, 292, 286.8, 155, 9, 'Billed on usage, on top of the fees above.', size=6.2, color='#4A4E60')
    b.text(page, 250.9, 299, 194, 10, [('Network tokens · ', {}), ('$0.05', {'bold': True, 'color': BLUE}), (' per token created, ', {}), ('$0.01', {'bold': True, 'color': BLUE}), (' per update', {})], size=7, color='#4A4E60')
    b.text(page, 250.9, 311, 194, 10, [('Reconciliation · ', {}), ('Pending review', {'italic': True, 'color': GREY})], size=7, color='#4A4E60')
    b.text(page, 250.9, 323, 194, 10, [('Nova recovery for failed top-ups · ', {}), ('Pending review', {'italic': True, 'color': GREY})], size=7, color='#4A4E60')
    b.text(page, x, 345, 197, 18, 'Every integration maintained by Yuno. Adding a provider or a local rail later is a routing change, not a new fee.', size=6.5, color=GREY2)
    # ---- right card (blue)
    b.rect(page, 464, 84.3, 224.5, 281.2, fill=BLUE)
    x = 473.7
    b.text(page, x, 91.5, 206, 10, 'WHAT IT MEANS FOR YANGO', size=8, bold=True, color=WHITE)
    b.text(page, x, 103.5, 206, 22, "At $7.3M in approved recharges a month across the four markets (3.24M transactions, Yango's own August 2026 data)", size=7.5, color=WHITE)
    b.text(page, x, 128, 100, 9, 'LINE', size=7, bold=True, color=WHITE)
    b.text(page, 574, 128, 52, 9, 'MONTHLY', size=7, bold=True, color=WHITE, align='END')
    b.text(page, 632, 128, 47.5, 9, 'YEARLY', size=7, bold=True, color=WHITE, align='END')
    b.hline(page, x, 139, 205.8, color=WHITE, weight=0.5, alpha=0.5)
    lines = [('Tranche 1 · $2.5M at 0.60%', '$15,000', '$180,000'), ('Tranche 2 · $2.5M at 0.50%', '$12,500', '$150,000'),
             ('Tranche 3 · $2.3M at 0.45%', '$10,373', '$124,471'), ('Platform fee', '$10,000', '$120,000')]
    y = 143
    for lab, m, yr in lines:
        b.text(page, x, y, 110, 11, lab, size=7.5, color=WHITE)
        b.text(page, 569, y - 0.5, 57, 11, m, size=9, bold=True, color=WHITE, align='END')
        b.text(page, 630, y - 0.5, 49.5, 11, yr, size=9, bold=True, color=WHITE, align='END')
        b.hline(page, x, y + 14.5, 205.8, color=WHITE, weight=0.5, alpha=0.25)
        y += 18
    b.text(page, x, 217, 80, 13, 'Total', size=10, bold=True, color=WHITE)
    b.text(page, 554, 216, 72, 13, '$47,873', size=11, bold=True, color=WHITE, align='END')
    b.text(page, 628, 216, 51.5, 13, '$574,471', size=11, bold=True, color=WHITE, align='END')
    b.rect(page, 473, 240, 206.5, 33, fill=DARKBLUE)
    b.text(page, 480, 244, 193, 26, '$0.015 all-in per approved recharge, 0.66% of recharge volume, falling as volume grows.', size=9, bold=True, color=WHITE)
    b.text(page, x, 283, 206, 76, 'Colombia and Peru first: $31,128 a month on $3.7M in recharges. All four markets: $47,873. The card-rail case in this deck, $3.21M a year, is 5.6 times this cost, and the $0.88M estimated on processing cost alone exceeds it. Add-ons are billed on usage and are not in these totals.', size=7.5, color=WHITE)

def slide_countries(b, page, page_no, logo_url=None):
    chrome(b, page, 'Proposal', 'Country by country: what each market adds as it goes live', page_no,
           footer='Source: Yango\'s own recharge data, August 2026, monthly. Declines and card verification attempts are not billed. Add-ons billed on usage and not included.',
           logo_url=logo_url, title_size=20)
    b.rect(page, 45, 60, 630, 24, fill=PANEL)
    b.text(page, 52, 62.5, 616, 20, 'The tranches pool the four markets, so each new market lands on a lower rate. Sequence shown as Yango proposed it: Colombia and Peru first, then Bolivia and Venezuela. Any order works, and the total at full volume does not change.', size=7.2, color=INK)
    cards = [
        ('🇨🇴 Colombia', 'STEP 1 · GOES LIVE FIRST', '$1.93M', '551K', '$3.50', '$21,578', '$11,578 transaction fee at 0.60% plus the $10,000 platform fee', '$21,578 / month', '$0.039 per recharge'),
        ('🇵🇪 Peru', 'STEP 2', '$1.80M', '561K', '$3.20', '+$9,551', 'Part at 0.60%, the rest at 0.50%', '$31,128 / month', '$0.028 per recharge'),
        ('🇧🇴 Bolivia', 'STEP 3', '$2.75M', '1.83M', '$1.50', '+$13,000', 'Part at 0.50%, the rest at 0.45%', '$44,129 / month', '$0.015 per recharge'),
        ('🇻🇪 Venezuela', 'STEP 4', '$0.83M', '297K', '$2.80', '+$3,744', 'All of it at 0.45%', '$47,873 / month', '$0.015 per recharge'),
    ]
    cw, gap, x0, y0, ch = 151.5, 8, 45, 92, 232
    for i, (name, step, vol, tx, ticket, added, note, run, per) in enumerate(cards):
        x = x0 + i * (cw + gap)
        b.rect(page, x, y0, cw, ch, fill=PANEL)
        cx = x + 8
        b.text(page, cx, y0 + 6, cw - 16, 13, name, size=10, bold=True)
        b.rect(page, cx, y0 + 22, cw - 16, 1.2, fill=BLUE)
        b.text(page, cx, y0 + 26, cw - 16, 9, step, size=6.5, bold=True, color=BLUE)
        stats = [('APPROVED RECHARGES / MONTH', vol), ('TRANSACTIONS / MONTH', tx), ('AVG RECHARGE TICKET', ticket)]
        y = y0 + 40
        for lab, val in stats:
            b.text(page, cx, y, cw - 16, 8, lab, size=5.5, bold=True, color='#8B909F')
            b.text(page, cx, y + 7.5, cw - 16, 14, val, size=12, bold=True)
            b.hline(page, cx, y + 25, cw - 16, color='#DDE0EA', weight=0.5)
            y += 29
        b.text(page, cx, y + 2, cw - 16, 8, 'ADDED MONTHLY COST', size=5.5, bold=True, color='#8B909F')
        b.text(page, cx, y + 9.5, cw - 16, 20, added, size=17, bold=True, color=BLUE)
        b.text(page, cx, y + 31, cw - 16, 20, note, size=6.5, color=GREY)
        b.hline(page, cx, y + 54, cw - 16, color='#DDE0EA', weight=0.5)
        b.text(page, cx, y + 58, cw - 16, 8, 'RUNNING TOTAL', size=5.5, bold=True, color='#8B909F')
        b.text(page, cx, y + 65.5, cw - 16, 12, run, size=9, bold=True)
        b.text(page, cx, y + 76.5, cw - 16, 10, per, size=7, color=GREY)
    # blue band
    b.rect(page, 45, 333, 630, 38, fill=BLUE)
    b.text(page, 55, 340, 100, 24, 'FOUR MARKETS,\nCOMBINED', size=7.5, bold=True, color=WHITE, valign='MIDDLE')
    stats = [('$47,873', 'a month'), ('$574,471', 'a year'), ('$0.015', 'per approved recharge'), ('0.66%', 'of recharge volume')]
    for i, (big, cap) in enumerate(stats):
        sx = 172 + i * 126
        b.vline(page, sx - 8, 339, 26, color=WHITE, weight=0.5, alpha=0.35)
        b.text(page, sx, 338, 118, 15, big, size=13, bold=True, color=WHITE)
        b.text(page, sx, 354, 118, 10, cap, size=6.5, color=WHITE)

# ----------------------------------------------------------------------------------------------------------------
class HtmlBuilder(Builder):
    """Same drawing API, emits absolutely positioned HTML (2 px per pt) so the layout can be previewed with Chrome
    without touching Google Slides. Used by --html."""
    def __init__(self, prefix):
        super().__init__(prefix); self.pages = []; self.cur = None
    def slide(self, insertion_index=None, background=WHITE):
        sid = self.nid('slide'); self.cur = {'id': sid, 'bg': background or WHITE, 'els': []}; self.pages.append(self.cur); return sid
    @staticmethod
    def _px(v): return f'{v * 2:.2f}px'
    def rect(self, page, x, y, w, h, fill=None, stroke=None, stroke_w=0.75, alpha=1.0):
        st = f'left:{self._px(x)};top:{self._px(y)};width:{self._px(w)};height:{self._px(h)};'
        if fill: st += f'background:{fill};opacity:{alpha};'
        if stroke: st += f'border:{stroke_w * 2:.2f}px solid {stroke};box-sizing:border-box;'
        self.cur['els'].append(f'<div class="el" style="{st}"></div>')
    def hline(self, page, x, y, w, color=BORDER, weight=0.6, alpha=1.0):
        self.cur['els'].append(f'<div class="el" style="left:{self._px(x)};top:{self._px(y - weight / 2)};width:{self._px(w)};height:{max(1, weight * 2):.2f}px;background:{color};opacity:{alpha};"></div>')
    def vline(self, page, x, y, h, color=BORDER, weight=0.6, alpha=1.0):
        self.cur['els'].append(f'<div class="el" style="left:{self._px(x - weight / 2)};top:{self._px(y)};width:{max(1, weight * 2):.2f}px;height:{self._px(h)};background:{color};opacity:{alpha};"></div>')
    def text(self, page, x, y, w, h, runs, size=8, color=DARK, bold=False, italic=False, align='START', valign='TOP', line_spacing=100):
        if isinstance(runs, str): runs = [(runs, {})]
        import html as H
        spans = []
        for t, st in runs:
            css = ''
            if 'size' in st: css += f'font-size:{st["size"] * 2:.2f}px;'
            if 'color' in st: css += f'color:{st["color"]};'
            if 'bold' in st: css += f'font-weight:{700 if st["bold"] else 400};'
            if 'italic' in st: css += f'font-style:{"italic" if st["italic"] else "normal"};'
            spans.append(f'<span style="{css}">{H.escape(t).replace(chr(10), "<br>")}</span>')
        ta = {'START': 'left', 'END': 'right', 'CENTER': 'center'}[align]
        jc = {'TOP': 'flex-start', 'MIDDLE': 'center', 'BOTTOM': 'flex-end'}[valign]
        st = (f'left:{self._px(x)};top:{self._px(y)};width:{self._px(w)};height:{self._px(h)};font-size:{size * 2:.2f}px;color:{color};'
              f'font-weight:{700 if bold else 400};font-style:{"italic" if italic else "normal"};text-align:{ta};justify-content:{jc};')
        self.cur['els'].append(f'<div class="el txt" style="{st}"><div>{"".join(spans)}</div></div>')
    def image(self, page, url, x, y, w, h):
        self.cur['els'].append(f'<img class="el" src="{url}" style="left:{self._px(x)};top:{self._px(y)};width:{self._px(w)};height:{self._px(h)};object-fit:contain;">')
    def html(self, page):
        return ('<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Titillium+Web:ital,wght@0,300;0,400;0,600;0,700;1,400&display=swap">'
                '<style>html,body{margin:0;padding:0}.page{position:relative;width:1440px;height:810px;overflow:hidden;font-family:"Titillium Web",sans-serif}'
                '.el{position:absolute}.txt{display:flex;flex-direction:column;line-height:1.2;white-space:pre-wrap;word-wrap:break-word}</style></head>'
                f'<body><div class="page" style="background:{page["bg"]}">{"".join(page["els"])}</div></body></html>')

def run_html(args):
    """Writes one HTML file per slide and, if Google Chrome is installed, a 1440x810 PNG of each."""
    import subprocess, pathlib
    out = pathlib.Path(args.html); out.mkdir(parents=True, exist_ok=True)
    logo = pathlib.Path(LOGO).resolve().as_uri() if os.path.exists(LOGO) else None
    b = HtmlBuilder('yp')
    d = b.slide(background=DIVIDER_BG); slide_divider(b, d)
    p1 = b.slide(); slide_pricing(b, p1, '36', logo)
    p2 = b.slide(); slide_countries(b, p2, '37', logo)
    chrome = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    for i, page in enumerate(b.pages, 35):
        f = out / f'yango_proposal_slide{i}.html'; f.write_text(b.html(page), encoding='utf-8')
        if os.path.exists(chrome):
            png = out / f'yango_proposal_slide{i}.png'
            subprocess.run([chrome, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--window-size=1440,810',
                            f'--screenshot={png}', '--virtual-time-budget=4000', f.resolve().as_uri()], capture_output=True, timeout=90)
            print('rendered', png)
        else:
            print('html only (Chrome not found):', f)

def creds():
    return service_account.Credentials.from_service_account_file(SA_KEY, scopes=SCOPES)

def upload_public_logo(drive):
    """Uploads the Yuno wordmark to the service account's Drive (anyone-with-link, reader) so createImage can fetch it."""
    if not os.path.exists(LOGO): return None
    q = "name = 'yuno-wordmark-for-slides.png' and trashed = false"
    hits = drive.files().list(q=q, fields='files(id)').execute().get('files', [])
    if hits: fid = hits[0]['id']
    else:
        media = MediaFileUpload(LOGO, mimetype='image/png')
        fid = drive.files().create(body={'name': 'yuno-wordmark-for-slides.png'}, media_body=media, fields='id').execute()['id']
        drive.permissions().create(fileId=fid, body={'type': 'anyone', 'role': 'reader'}).execute()
    return f'https://drive.google.com/uc?export=download&id={fid}'

def run_scratch(args):
    c = creds(); slides = build('slides', 'v1', credentials=c, cache_discovery=False); drive = build('drive', 'v3', credentials=c, cache_discovery=False)
    logo_url = None if args.no_logo else upload_public_logo(drive)
    pres = slides.presentations().create(body={'title': args.title}).execute()
    pid = pres['presentationId']; first = pres['slides'][0]['objectId']
    b = Builder('yp')
    d = b.slide(background=DIVIDER_BG); slide_divider(b, d)
    p1 = b.slide(); slide_pricing(b, p1, '36', logo_url)
    p2 = b.slide(); slide_countries(b, p2, '37', logo_url)
    b.reqs.append({'deleteObject': {'objectId': first}})
    slides.presentations().batchUpdate(presentationId=pid, body={'requests': b.reqs}).execute()
    print('scratch deck:', f'https://docs.google.com/presentation/d/{pid}/edit')
    if args.share:
        drive.permissions().create(fileId=pid, body={'type': 'user', 'role': 'writer', 'emailAddress': args.share}, sendNotificationEmail=False).execute()
        print('shared with', args.share)
    if args.pdf:
        data = drive.files().export(fileId=pid, mimeType='application/pdf').execute()
        open(args.pdf, 'wb').write(data); print('pdf:', args.pdf, len(data), 'bytes')
    return pid

def slide_text(s):
    out = []
    for el in s.get('pageElements', []):
        for te in el.get('shape', {}).get('text', {}).get('textElements', []):
            out.append(te.get('textRun', {}).get('content', ''))
    return ''.join(out)

def run_real(args):
    c = creds(); slides = build('slides', 'v1', credentials=c, cache_discovery=False)
    pres = slides.presentations().get(presentationId=args.pid).execute()
    S = pres['slides']; print('deck:', pres['title'], '| slides:', len(S))
    if len(S) != 36: print('expected 36 slides, found', len(S), ': check the deck before applying'); sys.exit(1)
    agenda, divider, data_slide, last_body = S[1], S[28], S[30], S[33]
    # inventory: agenda shapes, divider text, wordmark on the data slide
    ag = {}
    for el in agenda.get('pageElements', []):
        t = ''.join(te.get('textRun', {}).get('content', '') for te in el.get('shape', {}).get('text', {}).get('textElements', []))
        if '05.' in t: ag['num'] = el['objectId']
        if 'BUSINESS CASE' in t: ag['lab'] = el['objectId']
    print('agenda shapes:', ag, '| divider text:', slide_text(divider).strip().replace('\n', ' / '))
    logo_url = None
    for el in data_slide.get('pageElements', []):
        if 'image' in el and el['image'].get('contentUrl'):
            logo_url = el['image']['contentUrl']; print('  wordmark image on slide 31:', el['objectId'], '(contentUrl reused for the new slides)')
    if args.dry: print('dry run, nothing changed'); return
    if 'num' not in ag or 'lab' not in ag: print('agenda shapes not found, aborting'); sys.exit(1)
    b = Builder('yp')
    # 1. agenda
    for key, add in (('num', '\n06.'), ('lab', '\nPROPOSAL')):
        b.reqs.append({'insertText': {'objectId': ag[key], 'text': add, 'insertionIndex': len(''.join(
            te.get('textRun', {}).get('content', '') for el in agenda['pageElements'] if el['objectId'] == ag[key]
            for te in el['shape']['text']['textElements'])) - 1}})
    # 2. divider duplicated from slide 29, placed after slide 34 (index 34)
    div_id = 'yp_divider'
    b.reqs.append({'duplicateObject': {'objectId': divider['objectId'], 'objectIds': {divider['objectId']: div_id}}})
    b.reqs.append({'updateSlidesPosition': {'slideObjectIds': [div_id], 'insertionIndex': 34}})
    b.reqs.append({'replaceAllText': {'containsText': {'text': 'Business Case', 'matchCase': True}, 'replaceText': 'Proposal', 'pageObjectIds': [div_id]}})
    b.reqs.append({'replaceAllText': {'containsText': {'text': '05', 'matchCase': True}, 'replaceText': '06', 'pageObjectIds': [div_id]}})
    # 3. content slides (blank layout, the deck's wordmark is copied from slide 31 if the image can be re-inserted by URL later)
    p1 = b.slide(insertion_index=35); slide_pricing(b, p1, '36', logo_url)
    p2 = b.slide(insertion_index=36); slide_countries(b, p2, '37', logo_url)
    res = slides.presentations().batchUpdate(presentationId=args.pid, body={'requests': b.reqs}).execute()
    print('applied', len(b.reqs), 'requests. New slides at positions 35 (divider), 36, 37. Closing slides now 38 and 39: update their page numbers by hand if they show one.')

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--pid', help='real deck id (shared with the service account as Editor)')
    ap.add_argument('--dry', action='store_true')
    ap.add_argument('--pdf', help='scratch mode: export a PDF here for QA')
    ap.add_argument('--share', default='german.tatis@y.uno', help='scratch mode: share the deck with this user (empty to skip)')
    ap.add_argument('--title', default='Yango + Yuno · Proposal section (2026-09-22)')
    ap.add_argument('--no-logo', action='store_true')
    ap.add_argument('--html', help='write HTML (+PNG via Chrome headless) previews into this directory, no API calls')
    args = ap.parse_args()
    if args.html: run_html(args)
    elif args.pid: run_real(args)
    else: run_scratch(args)
