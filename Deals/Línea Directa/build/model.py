# -*- coding: utf-8 -*-
"""Línea Directa: business case + pricing arithmetic. Every figure on slides 13, 14 and the pricing slide comes from here.
Client-reported inputs (Luis Paternina, email 24-sep-2026 and call 30-sep-2026); FX = official rates; ranges = Yuno modelling assumptions."""
TX_CO, TX_PE = 300_000, 25_000                 # transacciones digitales / mes (reportado)
TICKET_COP, TICKET_PEN = 180_000, 200          # ticket promedio (reportado)
TRM = 3341.23                                  # COP por USD, TRM vigente 30-sep-2026 (datos.gov.co / Superfinanciera)
SBS = 3.45                                     # PEN por USD, SBS venta 29-sep-2026 (BCRP serie PD04640PD)
t_co, t_pe = TICKET_COP / TRM, TICKET_PEN / SBS
tpv_co, tpv_pe = TX_CO * t_co * 12, TX_PE * t_pe * 12
tpv = tpv_co + tpv_pe
# L1 / L2: +1% / +2% de pagos digitales completados (supuesto Yuno)
L1 = (0.01 * tpv_co, 0.02 * tpv_co); L2 = (0.01 * tpv_pe, 0.02 * tpv_pe)
# L3: 5 a 10 bps sobre el TPV digital (supuesto Yuno)
L3 = (0.0005 * tpv, 0.0010 * tpv)
# L4: 2 integraciones nuevas (tarjeta CO, tarjeta PE) + 4 actuales (PSE, Bancolombia/Wompi, Nequi, Yape)
NEW, CUR, FTE = 2, 4, 50_000
weeks = (NEW * 8 + (NEW + CUR) * 8 * 0.20, NEW * 12 + (NEW + CUR) * 12 * 0.30)
L4 = tuple(w / 52 * FTE for w in weeks)
LEV = [L1, L2, L3, L4]
cons, opt = sum(l[0] for l in LEV), sum(l[1] for l in LEV)
avg = [(l[0] + l[1]) / 2 for l in LEV]
# Pricing (German, 30-sep-2026): platform $15,000 + $0.06 tramo 1 / $0.05 tramo 2; corte de tramo 150,000 (supuesto)
PLATFORM, P1, P2, CUT = 15_000, 0.06, 0.05, 150_000
def monthly(tx):
    var = min(tx, CUT) * P1 + max(tx - CUT, 0) * P2
    return var, var + PLATFORM
TX = TX_CO + TX_PE
var, total = monthly(TX)
def M(v):   # $1.94M / $174K
    return f"${v/1e6:.2f}M" if v >= 1e6 else f"${round(v/1e3):,.0f}K"
def M1(v):
    return f"${v/1e6:.1f}M" if v >= 1e6 else f"${round(v/1e3):,.0f}K"
if __name__ == '__main__':
    print(f"ticket CO ${t_co:.2f}  PE ${t_pe:.2f}")
    print(f"TPV digital: CO ${tpv_co/12:,.0f}/mes ${tpv_co:,.0f}/año | PE ${tpv_pe/12:,.0f}/mes ${tpv_pe:,.0f}/año | total ${tpv/12:,.0f}/mes ${tpv:,.0f}/año")
    for i, l in enumerate(LEV, 1): print(f"L{i}: {l[0]:,.0f} / {l[1]:,.0f} / avg {avg[i-1]:,.0f}  ->  {M(l[0])} / {M(l[1])} / {M(avg[i-1])}")
    print(f"weeks L4: {weeks}")
    print(f"total: {cons:,.0f} / {opt:,.0f} / {(cons+opt)/2:,.0f} -> {M(cons)} / {M(opt)} / {M((cons+opt)/2)}")
    print(f"L1+L2: {L1[0]+L2[0]:,.0f} / {L1[1]+L2[1]:,.0f} / {avg[0]+avg[1]:,.0f}")
    print(f"pricing @ {TX:,}: variable ${var:,.0f}  total ${total:,.0f}/mes  ${total*12:,.0f}/año  all-in ${total/TX:.4f}  var ${var/TX:.4f}  bps {total*12/tpv*1e4:.1f}")
    v2, t2 = monthly(400_000); print(f"pricing @ 400,000: variable ${v2:,.0f} total ${t2:,.0f} all-in ${t2/400_000:.4f}")
    print(f"físico CO (30% del total si 300k = 70%): {TX_CO/0.7*0.3:,.0f} pagos/mes")
