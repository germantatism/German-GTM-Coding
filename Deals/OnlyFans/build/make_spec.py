# -*- coding: utf-8 -*-
"""Assemble deck_spec.json for the OnlyFans token vault deck.
Order follows storyline_v1.md. Slide content comes from three modules:
  spec_samuel.py   Samuel's 25 slides (verbatim content)
  spec_research.py OnlyFans and industry slides (Agent A ledger)  -> dict SLIDES
  spec_yuno.py     Yuno vault extensions, gap questions, vs-model grid (Agent B) -> dict SLIDES
Cross-references written as {{slide:<id>}} are resolved to final slide numbers here.
Run: python3 make_spec.py  -> writes deck_spec.json and prints the final slide map."""
import json, re, importlib, sys

PRESENTATION_ID = "1JSaFLC6QEIoNDFq1RbmMglAyuf8bLx7HDk2qzeeEbbA"

def load(mod):
    try:
        return importlib.import_module(mod).SLIDES
    except ModuleNotFoundError:
        print(f"  (module {mod} not present yet)"); return {}

S = load("spec_samuel"); A = load("spec_research"); B = load("spec_yuno"); D = load("spec_direction")

def divider(id_, num, title, sub=None, notes=None):
    d = {"id": id_, "type": "divider", "num": num, "title": title}
    if sub: d["sub"] = sub
    if notes: d["notes"] = notes
    return d

def keep(id_, template_index, replacements=None, notes=None, delete_images_matching=None):
    d = {"id": id_, "type": "template_keep", "template_index": template_index, "replacements": replacements or []}
    if notes: d["notes"] = notes
    if delete_images_matching: d["delete_images_matching"] = delete_images_matching
    return d

DN = importlib.import_module("spec_samuel").DIVIDER_NOTES

ORDER = [
    S.get("cover"),
    {"id": "agenda", "type": "agenda", "items": [
        {"num": "01", "title": "WHY WE ARE HERE"}, {"num": "02", "title": "INDUSTRY CONTEXT"},
        {"num": "03", "title": "HOW ONLYFANS RUNS PAYMENTS TODAY"}, {"num": "04", "title": "WHAT THE VAULT HAS TO HOLD"},
        {"num": "05", "title": "WHY YUNO"}, {"num": "06", "title": "THE YUNO TOKEN VAULT"},
        {"num": "07", "title": "VERSUS A STANDALONE VAULT"}, {"num": "08", "title": "THE PATH FORWARD"},
    ]},
    divider("d01", "01", "Why we are here", "An RFP for a token vault, and a design that needs more than one."),
    S.get("understood"), S.get("howtoread"), S.get("answer"), A.get("exec"),
    divider("d02", "02", "Industry context", "Creator banking, multi-bank design, and what a vault is expected to do in 2026."),
    A.get("industry-glance"), A.get("no-single-bank"), A.get("vault-2026"), A.get("vault-market"),
    divider("d03", "03", "How OnlyFans runs payments today"),
    A.get("of-numbers"), A.get("traffic"), A.get("stack"), A.get("lesson-2021"), A.get("four-numbers"),
    divider("d04", "04", "How OnlyFans vaults today, and what the RFP has to cover"),
    A.get("cof-today"), A.get("five-data"), S.get("questions-1"), B.get("questions-2"), B.get("questions-3"), A.get("clocks"),
    divider("d05", "05", "Why Yuno"),
    keep("yuno-story", 23), keep("four-pillars", 24), B.get("compliance") or keep("compliance", 45),
    keep("offices", 25), keep("trusted", 26, delete_images_matching=["SPACEX_LOGO_OBJECT_ID"]), keep("team", 27),
    B.get("dedicated") or keep("dedicated", 29, replacements=[{"find": "Eventbrite", "replace": "OnlyFans"}]),
    divider("d06", "06", "The Yuno token vault", "Vault · Proxy · Decision layer · Product direction", DN["d06"]),
    S.get("vault-cards"), S.get("vault-data"), B.get("keep-current"), B.get("move"),
    S.get("proxy-how"), S.get("proxy-controls"), S.get("banking"), S.get("who-decides"),
    D.get("direction-architecture"), D.get("direction-rules"), D.get("direction-yield"),
    divider("d07", "07", "Versus a standalone vault", "Where VGS and Basis Theory lead, and where they stop.", DN["d07"]),
    S.get("versus-thesis"), B.get("versus-model"), S.get("versus-table"), S.get("versus-bt"), S.get("versus-vgs"),
    divider("d08", "08", "The path forward"),
    S.get("shape"), S.get("owe"), S.get("next"),
    {"id": "closing", "type": "closing", "line": "Let's grow together", "name": "Samuel Vieira", "title": "Business Development Manager", "phone": "", "email": "samuel@y.uno"},
    divider("d-appx", "", "Appendix"),
    S.get("app-limits"), S.get("app-who"), B.get("credentials") or keep("credentials", 40), S.get("app-sources"),
]

slides = [s for s in ORDER if s]
missing = [i for i, s in enumerate(ORDER) if not s]
if missing: print("WARNING: missing slides at positions", missing)

pos = {s["id"]: i + 1 for i, s in enumerate(slides)}
tok = re.compile(r"\{\{slide:([a-z0-9-]+)\}\}")
def resolve(obj):
    if isinstance(obj, str):
        def rep(m):
            if m.group(1) not in pos: raise KeyError(f"unresolved slide ref {m.group(1)}")
            return str(pos[m.group(1)])
        return tok.sub(rep, obj)
    if isinstance(obj, list): return [resolve(x) for x in obj]
    if isinstance(obj, dict): return {k: resolve(v) for k, v in obj.items()}
    return obj

spec = {"presentation_id": PRESENTATION_ID, "merchant": "OnlyFans", "footer": "For: OnlyFans", "slides": resolve(slides)}
# house checks
blob = json.dumps(spec, ensure_ascii=False)
for bad in ["—", " - ", "no small feat", "SpaceX", "Spike", "Ria ", "Chess.com", "+12%", "20-30%", "20–30%"]:
    if bad in blob: print("HOUSE RULE HIT:", repr(bad))
json.dump(spec, open("deck_spec.json", "w"), ensure_ascii=False, indent=1)
print(f"{len(slides)} slides written to deck_spec.json")
for s in slides: print(f"{pos[s['id']]:>2}  {s['type']:<16} {s['id']:<16} {s.get('headline', s.get('title', ''))[:80]}")
