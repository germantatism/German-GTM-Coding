# -*- coding: utf-8 -*-
"""UNICEF Colombia: pricing arithmetic. Every figure on the pricing slide comes from here.
Inputs dados por German el 2-oct-2026: 150,000 transacciones al mes, ticket promedio $15, todo en dólares;
fee de plataforma $10,000; tarifa variable como % del volumen aprobado "como en la propuesta de Yango";
motor de suscripciones $0.02 por transacción enviada.
Ajuste de German (2-oct, tarde): los tramos se definen por número de transacciones aprobadas, no por volumen aprobado.
SUPUESTO (por confirmar con German): los porcentajes son los de la propuesta final de Yango (0.25% y 0.20%) y el corte
de 100,000 transacciones es el corte de Yango ($1.5M) dividido por el ticket de $15."""
TX = 150_000                      # transacciones al mes (German)
TICKET = 15                       # ticket promedio en dólares (German)
VOL = TX * TICKET                 # volumen aprobado mensual
PLATFORM = 10_000                 # fee de plataforma mensual (German)
R1, R2, CUT_TX = 0.0025, 0.0020, 100_000  # % del valor de cada transacción aprobada; corte en transacciones aprobadas (supuesto)
CUT = CUT_TX * TICKET             # equivalente en volumen (v1 del slide, por volumen)
TX1, TX2 = min(TX, CUT_TX), max(TX - CUT_TX, 0)
SUBS = 0.02                       # por transacción enviada por el motor de suscripciones (German)
SUBS_TX = TX                      # supuesto: las 150,000 pasan por el motor, un envío por transacción
def variable(vol):
    return min(vol, CUT) * R1, max(vol - CUT, 0) * R2
t1, t2 = variable(VOL)
var = t1 + t2
subs = SUBS_TX * SUBS
total = var + subs + PLATFORM
def K(v):   # $2.25M / $750K
    return f"${v/1e6:.2f}M".replace('.00M', 'M').replace('0M', 'M') if v >= 1e6 else f"${v/1e3:,.0f}K"
if __name__ == '__main__':
    print(f"volumen aprobado: ${VOL:,.0f}/mes  ${VOL*12:,.0f}/año")
    print(f"tramo 1: {TX1:,} trx x ${TICKET} x {R1:.2%} = ${t1:,.0f} | tramo 2: {TX2:,} trx x ${TICKET} x {R2:.2%} = ${t2:,.0f}")
    assert abs(t1 - TX1 * TICKET * R1) < 1e-6 and abs(t2 - TX2 * TICKET * R2) < 1e-6
    print(f"variable: ${var:,.0f}/mes ${var*12:,.0f}/año  = ${var/TX:.4f}/trx  {var/VOL:.3%} efectivo")
    print(f"suscripciones: {SUBS_TX:,} x ${SUBS:.2f} = ${subs:,.0f}/mes ${subs*12:,.0f}/año")
    print(f"plataforma: ${PLATFORM:,}/mes ${PLATFORM*12:,}/año")
    print(f"TOTAL: ${total:,.0f}/mes ${total*12:,.0f}/año  all-in ${total/TX:.4f}/trx  {total/VOL:.3%} del volumen")
    print(f"por trx de cada tramo: ${TICKET*R1:.4f} / ${TICKET*R2:.4f}; suscripciones como % del ticket: {SUBS/TICKET:.3%}")
    for ap in (0.85,): print(f"sensibilidad: si 150,000 son las aprobadas a {ap:.0%}, envíos >= {TX/ap:,.0f} -> suscripciones ${TX/ap*SUBS:,.0f}/mes")
    print(K(VOL), K(CUT), K(VOL - CUT))
