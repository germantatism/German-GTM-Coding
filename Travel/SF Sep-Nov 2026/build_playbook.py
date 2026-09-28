#!/usr/bin/env python3
"""Arma sf-playbook.html a partir de src/ y events.json.

events.json es la fuente única de los eventos: de ahí salen la lista del
Playbook y los bloques base del Interactive Calendar. calls.json son las
llamadas del calendario de German. Lo que el equipo agrega desde la página
vive en la base compartida del artifact, no aquí.

Uso: python3 build_playbook.py
"""
import html
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "src"

CHIP = {
    "must": ("must", "No faltar"),
    "go": ("go", "Ir"),
    "opt": ("opt", "Si cabe"),
    "planb": ("opt", "Plan B"),
    "skip": ("skip", "Saltar"),
}
FILTER = {"must": "must", "go": "go", "opt": "opt", "planb": "opt", "skip": "skip"}


def esc(text):
    return html.escape(text or "", quote=True)


def event_row(ev):
    chip_class, chip_label = CHIP[ev["verdict"]]
    date = esc(ev["dateLabel"])
    if ev.get("subLabel"):
        date += "<span>%s</span>" % esc(ev["subLabel"])
    title = esc(ev["title"])
    if ev.get("host"):
        title += " <small>%s</small>" % esc(ev["host"])
    body = ["        <h4>%s</h4>" % title, "        <p>%s</p>" % esc(ev["desc"])]
    if ev.get("desc2"):
        body.append("        <p>%s</p>" % esc(ev["desc2"]))
    cost = '<span class="price %s">%s</span>' % (ev["priceKind"], esc(ev["priceShort"]))
    if ev["price"] != ev["priceShort"]:
        cost += " <span>%s</span>" % esc(ev["price"])
    body.append('        <p class="cost">%s</p>' % cost)
    meta = [esc(x) for x in (ev.get("reg"), ev.get("place")) if x]
    meta += ['<a href="%s">%s</a>' % (esc(url), esc(label)) for label, url in ev.get("links", [])]
    if meta:
        body.append('        <p class="meta">%s</p>' % " · ".join(meta))
    tags = ['<span class="chip %s">%s</span>' % (chip_class, chip_label)]
    if ev.get("alert"):
        tags.append('<span class="chip crit">%s</span>' % esc(ev["alert"]))
    if ev.get("tag"):
        tags.append('<span class="who">%s</span>' % esc(ev["tag"]))
    return "\n".join([
        '    <li class="ev" data-v="%s">' % FILTER[ev["verdict"]],
        '      <div class="ev-date">%s</div>' % date,
        '      <div class="ev-body">',
        "\n".join(body),
        "      </div>",
        '      <div class="ev-tag">%s</div>' % "".join(tags),
        "    </li>",
    ])


def base_items(data, calls):
    items = []
    for ev in data["events"]:
        for c in ev.get("cal", []):
            if c.get("url"):
                links = [["abrir página", c["url"]]]
            else:
                links = ev.get("links", [])
            items.append({
                "id": c["id"],
                "title": c.get("title") or ev["title"],
                "host": "" if c.get("title") else ev.get("host", ""),
                "cat": c.get("cat") or ev["verdict"],
                "date": c["date"],
                "endDate": c.get("endDate", ""),
                "allDay": bool(c.get("allDay")),
                "start": c.get("start", ""),
                "end": c.get("end", ""),
                "endAssumed": bool(c.get("endAssumed")),
                "place": c.get("place") or ev.get("place", ""),
                "price": c.get("price") or ev["price"],
                "priceShort": c.get("priceShort") or ev["priceShort"],
                "priceKind": c.get("priceKind") or ev["priceKind"],
                "reg": c.get("reg") or ev.get("reg", ""),
                "links": links,
                "url": "",
                "note": ev.get("desc", ""),
                "by": "",
            })
    for o in data.get("own", []):
        items.append({
            "id": o["id"], "title": o["title"], "host": "", "cat": o["cat"], "date": o["date"], "endDate": "",
            "allDay": False, "start": o["start"], "end": o["end"], "endAssumed": False, "place": o.get("place", ""),
            "price": o["price"], "priceShort": o["priceShort"], "priceKind": o["priceKind"], "reg": "",
            "links": [], "url": "", "note": o.get("note", ""), "by": "",
        })
    for c in calls:
        items.append({
            "id": c["id"], "title": c["title"], "host": "", "cat": "call", "date": c["date"], "endDate": "",
            "allDay": False, "start": c["start"], "end": c["end"], "endAssumed": False, "place": "",
            "price": "", "priceShort": "", "priceKind": "na", "reg": "",
            "links": [], "url": "",
            "note": "Llamada con cliente, del calendario de German." if c.get("kind") == "client" else "Llamada interna, del calendario de German.",
            "by": "",
        })
    ids = [i["id"] for i in items]
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    if dupes:
        raise SystemExit("ids repetidos: %s" % dupes)
    missing = [i["id"] for i in items if i["cat"] != "call" and not i["price"]]
    if missing:
        raise SystemExit("eventos sin precio: %s" % missing)
    return items


def main():
    data = json.loads((HERE / "events.json").read_text(encoding="utf-8"))
    calls = json.loads((HERE / "calls.json").read_text(encoding="utf-8"))
    page = (SRC / "page.html").read_text(encoding="utf-8")
    bay = "\n".join(event_row(e) for e in data["events"] if e["group"] == "bay")
    trip = "\n".join(event_row(e) for e in data["events"] if e["group"] == "trip")
    items = base_items(data, calls)
    blob = json.dumps(items, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    out = (page
           .replace("{{CALENDAR_CSS}}", (SRC / "calendar.css").read_text(encoding="utf-8"))
           .replace("{{EVENTS_BAY}}", bay)
           .replace("{{EVENTS_TRIP}}", trip)
           .replace("{{CALENDAR_HTML}}", (SRC / "calendar.html").read_text(encoding="utf-8"))
           .replace("{{BASE_ITEMS}}", blob)
           .replace("{{CALENDAR_JS}}", (SRC / "calendar.js").read_text(encoding="utf-8")))
    if "{{" in out:
        raise SystemExit("quedó un marcador sin reemplazar")
    (HERE / "sf-playbook.html").write_text(out, encoding="utf-8")
    print("sf-playbook.html: %d bytes, %d eventos en la lista, %d bloques en el calendario"
          % (len(out.encode("utf-8")), len(data["events"]), len(items)))


if __name__ == "__main__":
    main()
