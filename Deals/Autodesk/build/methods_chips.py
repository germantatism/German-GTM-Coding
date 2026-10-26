# -*- coding: utf-8 -*-
"""Slide 3 (how things stand today): the methods column as one transparent PNG of logo chips, one row per market,
aligned to the 22 pt row pitch of draw_today. v2 (German, 26 Oct evening): smaller marks, every listed method as a mark
(no text chips), card brands on the Germany row. Logos: Wikimedia Commons SVGs rasterized with headless Chrome, the
Pay-easy, CCAvenue and Direct Debit marks from the schemes' own sites (assets/methods); a bank front and a barcode are
drawn here for net banking / bank transfer and Boleto.
  python3 methods_chips.py   -> assets/today_chips.png + assets/today_chips.json (row widths in pt) + preview"""
import os, json
from PIL import Image, ImageDraw, ImageFont

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')
M = os.path.join(A, 'methods')
SCALE = 6              # px per pt
W_PT, ROW_PT = 304, 22  # column width and row pitch on the slide
GAP = 4
INK, GREY, LINE, PANEL = (40, 42, 48), (117, 120, 130), (226, 227, 230), (244, 245, 253)
H = {  # chip height in pt (v2, 26 Oct evening: smaller, every method as a mark)
     'visa': 7, 'mastercard': 9, 'amex': 9, 'discover': 6, 'jcb': 9, 'diners': 7, 'cb': 9, 'dankort': 8, 'nexi': 7.5,
     'applepay': 8, 'gpaymark': 8, 'paypal': 7, 'plaid': 7.5, 'nacha': 7.5, 'sepa': 8, 'ideal': 9, 'directdebit': 8,
     'pix': 7.5, 'upi': 7.5, 'paytm': 7.5, 'ccavenue': 6.5, 'seven': 9, 'lawson': 5.5, 'familymart': 5.5, 'payeasy': 9, 'zip': 7.5}
CARDS6 = [('l', 'visa'), ('l', 'mastercard'), ('l', 'amex'), ('l', 'discover'), ('l', 'jcb'), ('l', 'diners')]
CARDS3 = [('l', 'visa'), ('l', 'mastercard'), ('l', 'amex')]
WALLETS = [('l', 'applepay'), ('l', 'gpaymark'), ('l', 'paypal')]
ROWS = [  # (market, chips): ('l', logo) | ('i', drawn icon: bank | barcode) | ('n', grey note)
    ('United States', CARDS6 + WALLETS + [('l', 'plaid'), ('l', 'nacha')]),                       # Pay by Bank (Plaid), ACH (Nacha)
    ('EU', CARDS6 + [('l', 'cb'), ('l', 'dankort'), ('l', 'nexi'), ('l', 'paypal'), ('l', 'sepa'), ('l', 'ideal')]),   # CartaSi is Nexi today
    ('United Kingdom', CARDS6 + WALLETS + [('l', 'directdebit')]),                                 # Bacs Direct Debit
    ('Germany', CARDS3 + WALLETS + [('l', 'sepa'), ('n', 'direct debit')]),                        # page lists cards without brands
    ('Brazil', CARDS3 + [('l', 'paypal'), ('l', 'pix'), ('i', 'barcode'), ('n', 'priced in BRL')]),   # Boleto
    ('Mexico', CARDS3 + [('l', 'paypal'), ('n', 'priced in MXN')]),
    ('India', [('l', 'visa'), ('l', 'mastercard'), ('l', 'upi'), ('i', 'bank'), ('l', 'paytm'), ('l', 'ccavenue')]),   # net banking, wallets
    ('Japan', [('l', 'visa'), ('l', 'mastercard'), ('l', 'amex'), ('l', 'jcb')] + WALLETS + [('l', 'seven'), ('l', 'lawson'), ('l', 'familymart'), ('l', 'payeasy'), ('i', 'bank')]),   # konbini, Pay-easy, bank transfer
    ('Australia', CARDS6 + WALLETS + [('l', 'zip')]),
]
GAP = 3


def icon(dr, kind, x, cy):
    """Representative marks drawn in ink: a bank front (net banking, bank transfer) and a barcode (Boleto). Returns width in pt."""
    h = 9; y0 = cy - h / 2
    if kind == 'bank':
        w = 11; X, Y = px(x), px(y0)
        dr.polygon([(X + px(w / 2), Y), (X, Y + px(3)), (X + px(w), Y + px(3))], fill=INK + (255,))
        for cx in (1.5, 4.25, 7.0, 9.75):
            dr.rectangle([X + px(cx - 0.6), Y + px(3.6), X + px(cx + 0.6), Y + px(7.6)], fill=INK + (255,))
        dr.rectangle([X, Y + px(8), X + px(w), Y + px(h)], fill=INK + (255,))
        return w
    w = 13; X, Y = px(x), px(y0)
    dr.rounded_rectangle([X, Y, X + px(w), Y + px(h)], radius=px(1.2), outline=INK + (255,), width=px(0.6))
    for bx, bw in ((2, 0.6), (3.4, 1.1), (5.3, 0.6), (6.7, 0.6), (8.1, 1.1), (10, 0.6), (11.4, 0.6)):
        dr.rectangle([X + px(bx), Y + px(2), X + px(bx + bw), Y + px(7)], fill=INK + (255,))
    return w


def px(v): return int(round(v * SCALE))


def main():
    logos = {k: Image.open(os.path.join(M, k + '.png')).convert('RGBA') for k in H}
    reg = ImageFont.truetype(os.path.join(M, 'TitilliumWeb-Regular.ttf'), px(6.5))
    img = Image.new('RGBA', (px(W_PT), px(ROW_PT * len(ROWS))), (0, 0, 0, 0))
    dr = ImageDraw.Draw(img)
    widths = {}
    for i, (mk, chips) in enumerate(ROWS):
        cy = ROW_PT * i + ROW_PT / 2; x = 0.0
        for kind, v in chips:
            if kind == 'l':
                im = logos[v]; h = H[v]; w = im.width * h / im.height
                r = im.resize((px(w), px(h)), Image.LANCZOS)
                img.alpha_composite(r, (px(x), px(cy - h / 2)))
                x += w + GAP
            elif kind == 'i':
                x += icon(dr, v, x, cy) + GAP
            else:
                tw = reg.getlength(v) / SCALE
                dr.text((px(x), px(cy)), v, font=reg, fill=GREY + (255,), anchor='lm')
                x += tw + GAP
        widths[mk] = round(x - GAP, 1)
        flag = 'OVER' if x - GAP > W_PT else 'ok'
        print(f'{mk:15s} {x - GAP:6.1f} pt  {flag}')
    img.save(os.path.join(A, 'today_chips.png'))
    json.dump({'scale': SCALE, 'w_pt': W_PT, 'row_pt': ROW_PT, 'rows': [m for m, _ in ROWS], 'widths': widths}, open(os.path.join(A, 'today_chips.json'), 'w'), indent=1)
    prev = Image.new('RGBA', img.size, (255, 255, 255, 255)); prev.alpha_composite(img); prev.convert('RGB').save(os.path.join(A, 'today_chips_preview.png'))
    print('saved', img.size, os.path.getsize(os.path.join(A, 'today_chips.png')) // 1024, 'KB')


if __name__ == '__main__':
    main()
