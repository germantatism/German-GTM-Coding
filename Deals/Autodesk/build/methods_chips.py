# -*- coding: utf-8 -*-
"""Slide 3 (how things stand today): the methods column as one transparent PNG of logo chips, one row per market,
aligned to the 22 pt row pitch of draw_today (German, 26 Oct 2026: logos for Apple Pay, Google Pay, PayPal and every
method; Visa, Mastercard, Amex, Discover for 'cards', as listed per market). Logos: Wikimedia Commons SVGs rasterized
with headless Chrome (assets/methods). Methods with no usable logo are text chips in the deck font (Titillium Web).
  python3 methods_chips.py   -> assets/today_chips.png + assets/today_chips.json (row widths in pt) + preview"""
import os, json
from PIL import Image, ImageDraw, ImageFont

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')
M = os.path.join(A, 'methods')
SCALE = 6              # px per pt
W_PT, ROW_PT = 304, 22  # column width and row pitch on the slide
GAP = 4
INK, GREY, LINE, PANEL = (40, 42, 48), (117, 120, 130), (226, 227, 230), (244, 245, 253)
H = {'visa': 9, 'mastercard': 11, 'amex': 11, 'discover': 7.5, 'jcb': 11, 'cb': 11, 'dankort': 10, 'applepay': 10,
     'gpaymark': 10, 'paypal': 8.5, 'sepa': 10, 'ideal': 11, 'pix': 9, 'upi': 9, 'zip': 9}
ROWS = [  # (market, chips): ('l', logo) | ('p', pill text) | ('n', grey note)
    ('United States', [('l', 'visa'), ('l', 'mastercard'), ('l', 'amex'), ('l', 'discover'), ('l', 'jcb'), ('l', 'applepay'), ('l', 'gpaymark'), ('l', 'paypal'), ('p', 'Pay by Bank'), ('p', 'ACH')]),
    ('EU', [('l', 'visa'), ('l', 'mastercard'), ('l', 'amex'), ('l', 'discover'), ('l', 'jcb'), ('l', 'cb'), ('l', 'dankort'), ('p', 'CartaSi'), ('l', 'paypal'), ('l', 'sepa'), ('l', 'ideal')]),
    ('United Kingdom', [('l', 'visa'), ('l', 'mastercard'), ('l', 'amex'), ('l', 'discover'), ('l', 'jcb'), ('l', 'applepay'), ('l', 'gpaymark'), ('l', 'paypal'), ('p', 'Bacs Direct Debit')]),
    ('Germany', [('p', 'Cards'), ('l', 'applepay'), ('l', 'gpaymark'), ('l', 'paypal'), ('l', 'sepa'), ('n', 'direct debit')]),
    ('Brazil', [('l', 'visa'), ('l', 'mastercard'), ('l', 'amex'), ('l', 'paypal'), ('l', 'pix'), ('p', 'Boleto'), ('n', 'priced in BRL')]),
    ('Mexico', [('l', 'visa'), ('l', 'mastercard'), ('l', 'amex'), ('l', 'paypal'), ('n', 'priced in MXN')]),
    ('India', [('l', 'visa'), ('l', 'mastercard'), ('l', 'upi'), ('p', 'net banking'), ('p', 'wallets via CCAvenue')]),
    ('Japan', [('l', 'visa'), ('l', 'mastercard'), ('l', 'amex'), ('l', 'jcb'), ('l', 'applepay'), ('l', 'gpaymark'), ('l', 'paypal'), ('p', 'konbini'), ('p', 'Pay-easy')]),
    ('Australia', [('l', 'visa'), ('l', 'mastercard'), ('l', 'amex'), ('l', 'discover'), ('l', 'jcb'), ('l', 'applepay'), ('l', 'gpaymark'), ('l', 'paypal'), ('l', 'zip')]),
]


def px(v): return int(round(v * SCALE))


def main():
    logos = {k: Image.open(os.path.join(M, k + '.png')).convert('RGBA') for k in H}
    semi = ImageFont.truetype(os.path.join(M, 'TitilliumWeb-SemiBold.ttf'), px(6.5))
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
            elif kind == 'p':
                tw = semi.getlength(v) / SCALE; w = tw + 9; h = 13
                x0, y0 = px(x), px(cy - h / 2)
                dr.rounded_rectangle([x0, y0, x0 + px(w), y0 + px(h)], radius=px(2.5), fill=(255, 255, 255, 255), outline=LINE + (255,), width=px(0.75))
                dr.text((x0 + px(4.5), y0 + px(h) / 2), v, font=semi, fill=INK + (255,), anchor='lm')
                x += w + GAP
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
