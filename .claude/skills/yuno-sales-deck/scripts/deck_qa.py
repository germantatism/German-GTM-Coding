#!/usr/bin/env python3
"""
deck_qa.py — pre-send QA for Yuno sales decks (.pptx).

Catches the defects that actually shipped in past decks:
  - other merchants'/prospects' names left in from a template
  - placeholders, internal notes (incl. Spanish working notes) left on slides
  - "$" on a people count, numbers with no unit before "/year"
  - inconsistent counts ("18 markets" vs "20 markets")
  - content slides without a Source line; over-long titles; overloaded slides
  - German's house rules: em-dashes or " - " as punctuation, "no small feat", local-currency amounts,
    the fabricated Yuno tiles (+12% / 20-30%), PayPal counted as a PSP, reconciliation without a roadmap note
and prints an inventory of every money figure per slide so headline numbers can be reconciled by hand.

Usage:
  python deck_qa.py deck.pptx --merchant "Roblox" [--allow "Stripe,Adyen,Xsolla"] [--lang en]
Exit code 1 if any ERROR is found.
"""
import argparse, re, sys
from collections import defaultdict
from pptx import Presentation
from pptx.util import Emu

# Prospects / accounts whose names have leaked between decks. Reference customers
# (Uber, Rappi, inDrive, etc.) are intentionally NOT listed: they legitimately appear on proof slides.
LEAK_NAMES = [
    "OpenAI", "ChatGPT", "Anthropic", "Claude", "xAI", "Grok", "Higgsfield", "Discord", "Scopely", "Turo",
    "Roblox", "Robux", "Skool", "Nutrameg", "Adobe", "Flair", "Allegiant", "Groupon", "Whop", "Kraken",
    "Agent Pay", "Aerolineas", "Zuora", "Poshmark", "Peek", "AXS", "Showpass", "EpicVIN", "Automatiq",
    "Plusgrade", "Zeely", "Cencosud", "Getnet", "High Wire", "Lepta",
    # German's accounts (Sep 2026)
    "Palco", "Suno", "Hostinger", "Eventbrite", "Appmaking", "AstroSoul", "Yango", "FlightHub", "HBO Max",
    "Warner Bros", "Gamma", "Airalo", "Riot Games", "TripAdvisor", "ViX", "TelevisaUnivision", "Fareportal",
    "Curology", "Gopuff", "Cambly", "Babbel", "Voodoo", "Hertz", "ThriveCart", "Tango", "FanDuel", "StubHub",
    "Lululemon", "Polymarket", "Bending Spoons", "Replika", "Lightricks", "Chai", "Perplexity", "Praktika",
    "McAfee", "Warby Parker", "Localiza", "Thinkific", "CellPoint", "Patreon", "Super.com", "Magnific", "Freepik",
    "T-Mobile", "Best Buy", "FC Barcelona", "doTERRA", "Universal Destinations",
]
PLACEHOLDERS = [r"\[[^\]]{0,60}\]", r"\bTBD\b", r"\bTBC\b", r"\bXX+\b", r"lorem ipsum", r"⚠", r"PLACEHOLDER",
                r"COMPANY NAME", r"to confirm\b", r"\bTODO\b", r"<[^>]{1,40}>"]
SPANISH_NOTE = re.compile(r"\b(cambiar|dividir|arriba|abajo|revisar|pendiente|ojo|falta|corregir|ajustar|igualar|ac[aá]|aqu[ií])\b", re.I)
MONEY = re.compile(r"[~≈]?\s?\$\s?\d[\d,\.]*\s?(?:[KMB]|bn|mn|million|billion)?\b(?:\s?(?:/|per)\s?(?:mo|month|yr|year))?", re.I)
DOLLAR_PEOPLE = re.compile(r"\$\s?\d[\d,\.]*\s?[KMB]?\s+(?:MAU|WAU|DAU|users?|consumers?|subscribers?|people|population)\b", re.I)
NO_UNIT = re.compile(r"(?<![\$\d\.,])[~≈]\s?\d+(?:\.\d+)?\s?/\s?(?:year|yr|month|mo)\b", re.I)
COUNT_NOUNS = ["markets", "countries", "levers", "data points", "slides"]
ALLOWED_BRACKETS = re.compile(r"^\[(F|E|Y|A)\]$")
# German's house rules
EM_DASH = re.compile(r"\u2014|(?<=\w)\s-\s(?=\w)")
EN_DASH = re.compile(r"\u2013")
NO_SMALL_FEAT = re.compile(r"no small feat", re.I)
LOCAL_CURRENCY = re.compile(
    r"(?<![A-Za-z$])(?:\u20a9|\u20ac|\u00a3|\u00a5|\u20b9|\u20ba|\u20b1|\u20ab|\u20a6|\u20aa|\u0e3f|R\$|C\$|A\$|S\$|MX\$|HK\$|NT\$|NZ\$)\s?\d"
    r"|\b(?:BRL|MXN|COP|ARS|CLP|PEN|EUR|GBP|JPY|KRW|INR|IDR|TRY|VND|PHP|PKR|NGN|ZAR|AED|SAR|CAD|AUD|SGD|HKD|TWD|THB|MYR|PLN|CZK|SEK|NOK|DKK|CHF|EGP|KES|BDT|UAH|RUB|CNY|RMB)\s?\d")
FABRICATED_STATS = re.compile(r"\+\s?12\s?%|\b20\s?(?:-|\u2013|to)\s?30\s?%", re.I)
PAYPAL_PSP = re.compile(r"PayPal[^.\n]{0,50}\b(?:PSPs?|processors?|acquirers?)\b|\b(?:PSPs?|processors?|acquirers?)\b[^.\n]{0,50}PayPal", re.I)
RECON_GA = re.compile(r"one ledger across|unified reconciliation|reconciliation across (?:all |every )?(?:PSPs|providers|processors)", re.I)


def shape_text(shape):
    out = []
    if shape.shape_type == 6:  # group
        for sh in shape.shapes:
            out += shape_text(sh)
    if getattr(shape, "has_text_frame", False) and shape.has_text_frame:
        t = "\n".join(p.text for p in shape.text_frame.paragraphs).strip()
        if t:
            out.append((shape, t))
    if getattr(shape, "has_table", False) and shape.has_table:
        for row in shape.table.rows:
            for cell in row.cells:
                if cell.text.strip():
                    out.append((shape, cell.text.strip()))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("deck")
    ap.add_argument("--merchant", required=True, help="Target merchant name (and aliases, comma-separated)")
    ap.add_argument("--allow", default="", help="Comma-separated names that may legitimately appear (their PSPs, named competitors)")
    ap.add_argument("--lang", default="en")
    ap.add_argument("--max-words", type=int, default=170)
    a = ap.parse_args()

    target = [t.strip().lower() for t in a.merchant.split(",") if t.strip()]
    allow = [t.strip().lower() for t in a.allow.split(",") if t.strip()]
    leak = [n for n in LEAK_NAMES if not any(t in n.lower() or n.lower() in t for t in target) and n.lower() not in allow]

    prs = Presentation(a.deck)
    issues = []  # (level, slide, msg)
    money = defaultdict(list)
    counts = defaultdict(lambda: defaultdict(list))
    n_slides = len(prs.slides)

    for i, sl in enumerate(prs.slides, 1):
        items = []
        for sh in sl.shapes:
            items += shape_text(sh)
        texts = [t for _, t in items]
        full = "\n".join(texts)
        words = len(full.split())
        notes = sl.notes_slide.notes_text_frame.text if sl.has_notes_slide else ""

        # 1. leaked names (whole word)
        for n in leak:
            if re.search(r"(?<![A-Za-z])" + re.escape(n) + r"(?![A-Za-z])", full):
                issues.append(("ERROR", i, f"Other account name on slide: '{n}'. If intentional (competitor/reference), pass it in --allow."))
        # 2. placeholders
        if re.search(r"_{4,}", re.sub(r"(?i)proposed dates?:\s*_+", "", full)):
            issues.append(("ERROR", i, "Blank line placeholder '____' left on slide."))
        for pat in PLACEHOLDERS:
            for m in re.finditer(pat, full, re.I):
                if ALLOWED_BRACKETS.match(m.group(0)):
                    continue
                issues.append(("ERROR", i, f"Placeholder or unresolved marker: '{m.group(0)[:50]}'"))
        # 3. internal notes in Spanish on an English deck
        if a.lang == "en":
            for t in texts:
                if len(SPANISH_NOTE.findall(t)) >= 2:
                    issues.append(("ERROR", i, f"Looks like an internal working note left on the slide: '{t[:70]}'"))
        # 4. units
        for m in DOLLAR_PEOPLE.finditer(full):
            issues.append(("ERROR", i, f"'$' on a people count: '{m.group(0)}'"))
        for m in NO_UNIT.finditer(full):
            issues.append(("ERROR", i, f"Number with no currency/unit: '{m.group(0)}'"))
        # 4b. German's house rules
        for m in EM_DASH.finditer(full):
            issues.append(("ERROR", i, f"Em-dash or ' - ' used as punctuation: '{full[max(0, m.start()-25):m.end()+25].strip()}'"))
        if EN_DASH.search(full):
            issues.append(("WARN", i, "En-dash found; write ranges with a plain hyphen (2-3 markets) and never use dashes as punctuation."))
        if NO_SMALL_FEAT.search(full):
            issues.append(("ERROR", i, "Phrase 'no small feat' is banned."))
        for m in LOCAL_CURRENCY.finditer(full):
            issues.append(("ERROR", i, f"Local-currency amount (decks are USD only; use a currency-free metric instead): '{m.group(0)}'"))
        for m in FABRICATED_STATS.finditer(full):
            issues.append(("WARN", i, f"'{m.group(0)}' looks like the fabricated Yuno tile (+12% / 20-30%). Yuno-wide figures must be the published 7% uplift / 30% recovered revenue, or a verified client result."))
        if PAYPAL_PSP.search(full):
            issues.append(("WARN", i, "PayPal appears next to PSP/processor/acquirer wording. PayPal is a wallet/APM, never a PSP; do not count it in processor totals."))
        if RECON_GA.search(full) and not re.search(r"roadmap", full, re.I):
            issues.append(("WARN", i, "Cross-PSP reconciliation claimed without a roadmap footnote; it is not GA."))
        # 5. count consistency
        for noun in COUNT_NOUNS:
            for m in re.finditer(r"(?<![\d\-–])\b(\d{1,3})\s+(?:priority |addressable |additional |emerging |strategic )?" + noun + r"\b", full, re.I):
                counts[noun][m.group(1)].append(i)
        # 6. money inventory
        for m in MONEY.finditer(full):
            money[i].append(re.sub(r"\s+", " ", m.group(0).strip()))
        # 7. source line + density + title length (skip cover/dividers = very little text)
        if words > 25:
            if not re.search(r"\bSources?\b\s*:?", full):
                issues.append(("WARN", i, "No Source line on a content slide."))
            if words > a.max_words:
                issues.append(("WARN", i, f"Dense slide: {words} words (> {a.max_words}). One idea per slide; move detail to appendix/notes."))
        # title = largest-font text near top; approximate with the longest text box in the top 25% of the slide
        top = [(sh, t) for sh, t in items if getattr(sh, "top", None) is not None and sh.top < Emu(int(prs.slide_height * 0.2))]
        if top:
            title = max(top, key=lambda st: len(st[1]))[1]
            if len(title) > 140:
                issues.append(("WARN", i, f"Title is {len(title)} chars; keep to two lines (~120)."))
        # 8. off-slide shapes
        for sh in sl.shapes:
            try:
                if sh.left is not None and (sh.left + sh.width > prs.slide_width * 1.01 or sh.top + sh.height > prs.slide_height * 1.01 or sh.left < 0 or sh.top < 0):
                    issues.append(("WARN", i, f"Shape extends beyond the slide: '{(sh.name or '')[:30]}'"))
            except Exception:
                pass
        if re.search(r"\b(thank you|thanks!?|gracias)\b", full, re.I) and i == n_slides and words < 12:
            issues.append(("WARN", i, "Deck ends on 'Thank you'. End on The Ask / next step instead."))
        if notes and a.lang == "en" and len(SPANISH_NOTE.findall(notes)) >= 2:
            issues.append(("INFO", i, "Speaker notes contain Spanish working notes (fine internally; remove before sending)."))

    for noun, vals in counts.items():
        if len(vals) > 1:
            detail = "; ".join(f"{v} {noun} on slides {sorted(set(s))}" for v, s in vals.items())
            issues.append(("WARN", 0, f"Inconsistent count of {noun}: {detail}. Confirm each is a different thing, or fix."))

    print(f"\n=== deck_qa: {a.deck} · {n_slides} slides · merchant={a.merchant} ===\n")
    order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    for lvl, sl, msg in sorted(issues, key=lambda x: (order[x[0]], x[1])):
        print(f"[{lvl}] slide {sl if sl else '-'}: {msg}")
    if not issues:
        print("No automated issues found.")

    print("\n--- Money figures by slide (reconcile by hand: hero number, lever subtotals, totals, /mo x 12 = /yr) ---")
    for i in sorted(money):
        print(f"slide {i:>2}: " + " | ".join(dict.fromkeys(money[i])))

    errs = sum(1 for x in issues if x[0] == "ERROR")
    warns = sum(1 for x in issues if x[0] == "WARN")
    print(f"\nSummary: {errs} error(s), {warns} warning(s). Now run the manual checklist in references/qa-checklist.md and render the slides to images.")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
