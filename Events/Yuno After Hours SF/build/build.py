"""Build the self-contained venue RFI HTML + PDF and run QA checks."""
import base64, re, sys
from pathlib import Path
import fitz
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
OUT = HERE.parent
DS = HERE.parents[2] / "Yuno Design System" / "yuno-design-system"

font = base64.b64encode((DS / "fonts/Geist-VariableFont_wght.ttf").read_bytes()).decode()
logo = (DS / "assets/yuno-wordmark-white.svg").read_text().strip()
logo = re.sub(r'<svg width="\d+" height="\d+"', '<svg role="img" aria-label="yuno"', logo, count=1)

html = (HERE / "venue-rfi.template.html").read_text()
html = html.replace("{{GEIST}}", font).replace("{{LOGO}}", logo)
html_path = OUT / "Yuno After Hours SF - Venue RFI.html"
pdf_path = OUT / "Yuno After Hours SF - Venue RFI.pdf"
html_path.write_text(html)

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto(html_path.as_uri())
    pg.evaluate("document.fonts.ready")
    qa = pg.evaluate("""() => {
      const page = document.querySelector('.page');
      const pr = page.getBoundingClientRect();
      const inner = {l: pr.left + 48, r: pr.right - 48, t: pr.top + 48, b: pr.bottom - 48};
      const els = [...page.querySelectorAll('h1,h2,p,li,dt,dd,svg,a,b,span')];
      const out = [];
      for (const e of els) {
        const r = e.getBoundingClientRect();
        if (r.left < inner.l - 0.5 || r.right > inner.r + 0.5 || r.top < inner.t - 0.5 || r.bottom > inner.b + 0.5)
          out.push('outside margins: ' + e.tagName + ' ' + e.textContent.slice(0, 40));
        const fs = parseFloat(getComputedStyle(e).fontSize);
        if (e.tagName !== 'svg' && fs < 12) out.push('small text ' + fs + ': ' + e.textContent.slice(0, 40));
      }
      // overlap among leaf text blocks
      const leaves = [...page.querySelectorAll('h1,h2,p,li,dt,dd')];
      for (let i = 0; i < leaves.length; i++) for (let j = i + 1; j < leaves.length; j++) {
        const a = leaves[i].getBoundingClientRect(), c = leaves[j].getBoundingClientRect();
        if (leaves[i].contains(leaves[j]) || leaves[j].contains(leaves[i])) continue;
        if (a.left < c.right - 1 && c.left < a.right - 1 && a.top < c.bottom - 1 && c.top < a.bottom - 1)
          out.push('overlap: ' + leaves[i].textContent.slice(0, 30) + ' | ' + leaves[j].textContent.slice(0, 30));
      }
      const foot = document.querySelector('.foot').getBoundingClientRect();
      const cols = document.querySelectorAll('.cols')[0].getBoundingClientRect();
      return {issues: out, font: document.fonts.check('12px Geist'),
              gapAboveFooter: Math.round(foot.top - cols.bottom),
              overflow: page.scrollHeight - page.clientHeight};
    }""")
    pg.emulate_media(media="print")
    pg.pdf(path=str(pdf_path), width="8.5in", height="11in", print_background=True,
           margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
    b.close()

doc = fitz.open(pdf_path)
text = "".join(pg.get_text() for pg in doc)
doc[0].get_pixmap(dpi=150).save(str(HERE / "preview.png"))
print("pages:", doc.page_count, "| size in:", doc[0].rect.width / 72, "x", doc[0].rect.height / 72)
print("geist loaded:", qa["font"], "| overflow px:", qa["overflow"], "| gap above footer px:", qa["gapAboveFooter"])
print("dash check:", "FAIL" if re.search("[—–]| - ", html.split("<body>")[1] + text) else "ok")
print("budget words:", re.findall(r"\bbudget\b", text, re.I) or "none")
print("issues:", qa["issues"] or "none")
print("fonts in pdf:", {f[3] for f in doc[0].get_fonts()})
