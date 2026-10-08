# -*- coding: utf-8 -*-
"""UNICEF Colombia: pricing arithmetic. Every figure on the pricing slide comes from here.
v7 (German, 8-oct-2026, tras presentar la propuesta): cuatro tramos por transacciones aprobadas al mes,
0 a 50,000 al 0.28%, 50,000 a 100,000 al 0.26%, 100,000 a 150,000 al 0.24% y más de 150,000 al 0.22%
(German eligió la escalera 0.28 / 0.26 / 0.24 / 0.22 entre las opciones propuestas). Lo demás no cambia:
150,000 trx al mes, ticket $15, plataforma $7,000, suscripciones $0.015 con 50,000 gratis al mes, mínimo $10,000."""
TX = 150_000                      # transacciones aprobadas al mes (German)
TICKET = 15                       # ticket promedio en dólares (German)
VOL = TX * TICKET                 # volumen aprobado mensual
PLATFORM = 7_000                  # fee de plataforma mensual (v6)
# tramos: (límite superior en trx aprobadas, tasa sobre el valor de cada trx aprobada); None = sin límite
TIERS = [(50_000, 0.0028), (100_000, 0.0026), (150_000, 0.0024), (None, 0.0022)]
R1 = TIERS[0][1]                  # compatibilidad con scripts anteriores
SUBS = 0.015                      # por transacción enviada por el motor de suscripciones (v6)
SUBS_S = ('$%.3f' % SUBS).rstrip('0').rstrip('.')  # '$0.015'
SUBS_TX = TX                      # supuesto: las 150,000 pasan por el motor, un envío por transacción
SUBS_FREE = 50_000                # primeras 50,000 transacciones del motor sin costo, por mes
MIN_BILL = 10_000                 # facturación mínima mensual (v6)
COMMIT = MIN_BILL - PLATFORM      # compromiso en transacciones que suma al fee de plataforma
def tier_rows(tx):
    """[(n, lo, hi, trx en el tramo, tasa, $)] para un volumen tx; hi=None es el último tramo."""
    rows, lo = [], 0
    for n, (hi, r) in enumerate(TIERS, 1):
        inside = max(min(tx, hi if hi is not None else tx) - lo, 0)
        rows.append((n, lo, hi, inside, r, inside * TICKET * r)); lo = hi if hi is not None else lo
    return rows
def variable(tx): return sum(row[5] for row in tier_rows(tx))
def commit_tx(commit):
    """transacciones aprobadas que cubren el compromiso, tramo a tramo."""
    left, lo = commit, 0
    for hi, r in TIERS:
        per = TICKET * r; span = (hi - lo) if hi is not None else float('inf')
        if left <= span * per: return lo + left / per
        left -= span * per; lo = hi
    raise ValueError
ROWS = tier_rows(TX)
var = variable(TX)
SUBS_BILL = max(SUBS_TX - SUBS_FREE, 0)
subs = SUBS_BILL * SUBS
total = var + subs + PLATFORM
COMMIT_TX = commit_tx(COMMIT)
def K(v):   # $2.25M / $750K
    return f"${v/1e6:.2f}M".replace('.00M', 'M').replace('0M', 'M') if v >= 1e6 else f"${v/1e3:,.0f}K"
def lbl(lo, hi):   # etiqueta del tramo en el panel izquierdo
    return f'{lo:,} a {hi:,} trx aprobadas' if hi is not None else f'Más de {lo:,} trx aprobadas'
if __name__ == '__main__':
    print(f"volumen aprobado: ${VOL:,.0f}/mes  ${VOL*12:,.0f}/año")
    for n, lo, hi, inside, r, amt in ROWS: print(f"  tramo {n}: {lbl(lo, hi):32} {inside:>7,} trx x ${TICKET} x {r:.2%} = ${amt:,.0f}")
    print(f"variable: ${var:,.0f}/mes ${var*12:,.0f}/año  = ${var/TX:.4f}/trx  {var/VOL:.3%} efectivo")
    print(f"suscripciones: ({SUBS_TX:,} - {SUBS_FREE:,} gratis) = {SUBS_BILL:,} x {SUBS_S} = ${subs:,.0f}/mes ${subs*12:,.0f}/año")
    print(f"plataforma: ${PLATFORM:,}/mes ${PLATFORM*12:,}/año")
    print(f"TOTAL: ${total:,.0f}/mes ${total*12:,.0f}/año  all-in ${total/TX:.4f}/trx -> ${total/TX:.2f}  {total/VOL:.3%} del volumen")
    print(f"facturación mínima ${MIN_BILL:,} = ${PLATFORM:,} plataforma + ${COMMIT:,} en transacciones = {COMMIT_TX:,.1f} trx aprobadas (slide: cerca de {round(COMMIT_TX, -3):,.0f})")
    for ap in (117_300,): print(f"sensibilidad {ap:,} aprobadas: variable ${variable(ap):,.0f}, total ${variable(ap)+max(138_000-SUBS_FREE,0)*SUBS+PLATFORM:,.0f}")
