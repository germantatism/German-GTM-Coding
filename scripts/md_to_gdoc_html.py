#!/usr/bin/env python3
"""Convert a brief in markdown to compact HTML that imports cleanly as a Google Doc.
Usage: python3 scripts/md_to_gdoc_html.py input.md output.html
Rules: no <hr> (Docs merges it into headings), 4-byte emoji replaced by BMP-safe marks,
bold table headers, single-line output."""
import re, html, sys
src = open(sys.argv[1], encoding="utf-8").read().replace("🔍", "❓")
def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2">\1</a>', s)
    return s
out, lines, i, inlist = [], src.split("\n"), 0, None
def close_list():
    global inlist
    if inlist: out.append(f"</{inlist}>"); inlist = None
while i < len(lines):
    l = lines[i]
    if l.startswith("|") and i + 1 < len(lines) and re.match(r'^\|[\s\-|:]+\|$', lines[i+1]):
        close_list()
        hdr = [c.strip() for c in l.strip().strip("|").split("|")]
        rows = []; i += 2
        while i < len(lines) and lines[i].startswith("|"):
            rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
        t = "<table><tr>" + "".join(f"<th><b>{inline(c)}</b></th>" for c in hdr) + "</tr>"
        for r in rows: t += "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>"
        out.append(t + "</table>"); continue
    m = re.match(r'^(#{1,3})\s+(.*)', l)
    if m:
        close_list(); n = len(m.group(1)); out.append(f"<h{n}>{inline(m.group(2))}</h{n}>"); i += 1; continue
    if l.strip() == "---":
        close_list(); i += 1; continue
    m = re.match(r'^- (.*)', l)
    if m:
        if inlist != "ul": close_list(); out.append("<ul>"); inlist = "ul"
        out.append(f"<li>{inline(m.group(1))}</li>"); i += 1; continue
    m = re.match(r'^\d+\. (.*)', l)
    if m:
        if inlist != "ol": close_list(); out.append("<ol>"); inlist = "ol"
        out.append(f"<li>{inline(m.group(1))}</li>"); i += 1; continue
    if l.strip() == "":
        close_list(); i += 1; continue
    close_list()
    para = [l]; i += 1
    while i < len(lines) and lines[i].strip() and not re.match(r'^(#{1,3}\s|- |\d+\. |\||---)', lines[i]):
        para.append(lines[i]); i += 1
    out.append("<p>" + "<br>".join(inline(x) for x in para) + "</p>")
close_list()
css = "<style>body{font-family:Arial,sans-serif;font-size:10.5pt;line-height:1.35}h1{font-size:18pt}h2{font-size:14pt;margin-top:20pt}h3{font-size:11.5pt}table{border-collapse:collapse;width:100%;margin:6pt 0}th,td{border:1px solid #bbb;padding:4pt 6pt;vertical-align:top;font-size:9.5pt;text-align:left}th{background:#efefef}</style>"
doc = "<html><head><meta charset='utf-8'>" + css + "</head><body>" + "".join(out) + "</body></html>"
open(sys.argv[2], "w", encoding="utf-8").write(doc)
print("html bytes:", len(doc.encode()))
