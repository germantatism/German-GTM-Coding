# -*- coding: utf-8 -*-
"""Slide 10 investors panel, two rows (German, 26 Oct night: logos bigger, first four on top, other five below).
The panel on the house slide is one image (648 x 129 pt) with the logos baked in; this rebuilds it: lavender rounded
panel, every logo in the deck ink, first row of four, second row of five. Sources: repo high-res PNGs (a16z, Tiger Global,
Kaszek, Monashees), the funds' own sites (Rasmal, GrowthX), and crops from the previous panel for the rest.
  python3 investors_panel.py  -> assets/investors_two_rows.png (+ preview)"""
import os
from PIL import Image, ImageDraw

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')
I = os.path.join(A, 'investors')
S = 4                      # px per pt
W, H = 648, 129
BG = (243, 245, 254, 255); INK = (40, 42, 48)
ORDER = ['globalpaytech', 'a16z', 'tiger', 'quantumlight', 'monashees', 'kaszek', 'rasmal', 'growthx', 'further']
SRC = {'a16z': 'a16z_src.png', 'tiger': 'tiger_src.png', 'kaszek': 'kaszek_src.png', 'monashees': 'monashees_src.png',
       'rasmal': 'rasmal_src.png', 'growthx': 'growthx_src.png'}


def ink(name):
    """Logo as INK on transparent, from the source alpha (or from darkness when there is no alpha), trimmed."""
    f = os.path.join(I, SRC.get(name, name + '_crop.png'))
    im = Image.open(f).convert('RGBA'); a = im.getchannel('A')
    if a.getextrema() == (255, 255):   # opaque: build alpha from darkness
        g = im.convert('L'); a = g.point(lambda v: max(0, min(255, int((255 - v) * 1.2))))
    out = Image.new('RGBA', im.size, INK + (0,)); out.putalpha(a)
    return out.crop(out.getbbox())


def px(v): return int(round(v * S))


def main():
    img = Image.new('RGBA', (px(W), px(H)), (0, 0, 0, 0)); dr = ImageDraw.Draw(img)
    dr.rounded_rectangle([0, 0, px(W) - 1, px(H) - 1], radius=px(6), fill=BG)
    rows = [(ORDER[:4], 52, 118, 26), (ORDER[4:], 98, 94, 22)]   # names, centre y (pt), max w, max h
    x0, x1 = 15, 633
    for names, cy, mw, mh in rows:
        cell = (x1 - x0) / len(names)
        for i, n in enumerate(names):
            lg = ink(n); sc = min(mw * S / lg.width, mh * S / lg.height)
            w, h = max(1, int(lg.width * sc)), max(1, int(lg.height * sc))
            r = lg.resize((w, h), Image.LANCZOS)
            cx = x0 + cell * (i + 0.5)
            img.alpha_composite(r, (px(cx) - w // 2, px(cy) - h // 2))
            print(f'{n:14s} {w / S:6.1f} x {h / S:5.1f} pt')
    img.save(os.path.join(A, 'investors_two_rows.png'))
    prev = Image.new('RGBA', img.size, (255, 255, 255, 255)); prev.alpha_composite(img); prev.convert('RGB').save(os.path.join(A, 'investors_two_rows_preview.png'))
    print('saved', img.size)


if __name__ == '__main__':
    main()
