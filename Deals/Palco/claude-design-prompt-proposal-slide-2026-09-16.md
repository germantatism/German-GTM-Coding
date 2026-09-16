# Prompt Claude Design: Palco + Yuno, rebuild the proposal slide in the Flair "Option B" layout (2026-09-16)

Attach two images: `palco-design-ref-flair-option-b.png` (the layout to copy) and `palco-proposal-slide-2026-09-16.png` (the current slide, content source). Deck: "Propuesta - Palco + Yuno", https://docs.google.com/presentation/d/1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY/edit

---

Target: the deck **"Propuesta - Palco + Yuno"** (18 slides, Spanish). Rebuild **slide 13, "Propuesta"**, so it matches the attached Flair Airlines reference slide ("Option B · Platform fee plus success-based rate") element for element: same grid, same card language, same typography scale, same color roles. Take the content from the attached current slide 13 and the copy below. Every word on the slide is in Spanish, exactly as written here. Do not touch any other slide.

## Layout to reproduce (from the Flair reference)

- 16:9, white background, thin light vertical rule at the far left as in the rest of the deck, Yuno wordmark top right, page number bottom left.
- Top left: small grey uppercase eyebrow, then the title in Yuno blue (#3B4BF9), bold, one line, then a two-line grey subtitle in regular weight.
- Three cards in one row, equal height, aligned tops, 16 to 20 px gutters, 12 px corner radius:
  1. Left card, light lilac fill (#EEF0FB), no border. Header in bold black small caps, grey sub-line, then three rows separated by 1 px lilac dividers. Each row: band label on the left in grey regular text, price on the right in Yuno blue, large (about 2.2x the body size), bold, with a small "/trx" suffix in regular weight. At the bottom of the card a white rounded note box with two lines of small grey text.
  2. Middle card, white fill, 1 px light grey border. Header in bold black, grey sub-line, then rows label left in black regular, value right: "Incluido" in Yuno blue bold, amounts in black bold. 1 px lilac dividers.
  3. Right card, solid Yuno blue fill, all text white. Header bold, sub-line in lighter white. A three-column mini table with a small uppercase header row (CONCEPTO, MENSUAL, ANUAL), thin white dividers at 25% opacity, subtotal and total rows in bold. Under the table one highlighted line and one small explanatory paragraph.
- Below the three cards, one row with two blocks: left, a light lilac callout with a 4 px Yuno blue left border and one sentence; right, a white strip with 1 px border holding a small uppercase label, a grey one-line note, and three inline prices in Yuno blue with grey unit suffixes.
- Footer: tiny grey text at the bottom left.
- Typeface: the same family already used in the deck. Number style: US format with commas and a dollar sign ($10,000, $0.08). No thousands with periods.

## Copy, in this order

**Eyebrow:** PROPUESTA · PRICING

**Title:** Fee de plataforma más tarifa por transacción exitosa

**Subtitle:** Una tarifa por transacción que empieza en 8 centavos y baja con el volumen, con orquestación, smart routing, monitores y subcuentas incluidos, sobre un fee de plataforma fijo de $10,000 al mes.

**Card 1, lilac. Header:** TARIFA POR TRANSACCIÓN EXITOSA. **Sub-line:** Por transacción exitosa, según el volumen del mes.

| Band label (left, grey) | Price (right, big blue) |
|---|---|
| 0 a 58,750 trx | $0.08/trx |
| 58,751 a 117,500 trx | $0.06/trx |
| Más de 117,500 trx | $0.05/trx |

**Note box inside card 1:** Sin fee de setup. Cada tramo se cobra a su tarifa dentro del mes. Las transacciones declinadas no se cobran.

**Card 2, white. Header:** QUÉ CUBRE LA TARIFA. **Sub-line:** El fee de plataforma se factura por separado.

| Label (left) | Value (right) |
|---|---|
| Orquestación y motor de reglas | Incluido |
| Smart routing y reintentos | Incluido |
| Monitores y alertas | Incluido |
| Subcuentas por cliente | Incluido |
| Reportes y dashboard | Incluido |
| Equipo dedicado (KAM y TAM) | Incluido |
| Fee de plataforma | $10,000 / mes |

**Card 3, blue. Header:** LO QUE SIGNIFICA PARA PALCO. **Sub-line:** A 235,000 transacciones exitosas / mes.

| CONCEPTO | MENSUAL | ANUAL |
|---|---|---|
| Transacciones exitosas (235k) | $14,100 | $169,200 |
| Fee de plataforma | $10,000 | $120,000 |
| **Subtotal pagos** | **$24,100** | **$289,200** |
| 3DS (100k autenticaciones) | $4,030 | $48,360 |
| Motor antifraude (20k evaluaciones) | $368 | $4,416 |
| **Total estimado** | **$28,498** | **$341,976** |

**Highlighted line under the table (bold amounts):** ≈ $0.103 all-in por transacción exitosa en pagos; ≈ $0.121 con 3DS y antifraude. Baja a medida que crece el volumen.

**Small paragraph under it:** Desglose a 235,000: 58,750 × $0.08 = $4,700, 58,750 × $0.06 = $3,525 y 117,500 × $0.05 = $5,875. A 300,000 trx/mes: $10,000 + $17,350 = $27,350 / mes ≈ $0.091 por trx. Los volúmenes de 3DS y antifraude son estimados y se ajustan al consumo real.

**Bottom left callout (blue left border):** Pendiente de revisión: conciliación, network tokens y token vault. Alcance y precio se revisan juntos en la siguiente fase.

**Bottom right strip. Label:** SEGURIDAD Y RIESGO. **Grey note:** Uso puro, sin mínimos, se factura según consumo. **Three inline prices (amount in blue, unit in grey):** 3DS $0.0403 / autenticación · Motor antifraude $0.0184 / evaluación · Risk conditions $0.0139 / trx evaluada

**Footer:** Contrato a 3 años.

## What NOT to do

- Do not keep the current four-column tier table, the "Ejemplo" breakdown rows, the "All-in al tope" column or the "$24,100/ mes" hero number. The three-card Flair layout replaces all of it; the same numbers now live in card 3.
- Do not change, round or reformat any number above. Do not convert to another currency. Do not add a minimum monthly billing line, a ramp, a first-month credit, a volume commitment or an "Opción A". None has been agreed.
- Do not invent prices for reconciliación, network tokens or token vault; they only appear in the bottom left callout as pending.
- Do not name any PSP, processor or client of Palco on this slide. Do not add approval-rate, savings or ROI claims.
- Do not translate "Smart routing", "3DS", "Risk conditions", "KAM", "TAM" or "trx".
- Do not use em-dashes or " - " as punctuation anywhere. Use commas, periods or the middle dot (·).
- Keep all text inside its card; if a line does not fit, reduce that line's size by one step, never overflow or overlap.
