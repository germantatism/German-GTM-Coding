# -*- coding: utf-8 -*-
"""UNICEF Colombia: pricing arithmetic. Every figure on the pricing slide comes from here.
Inputs dados por German el 2-oct-2026: 150,000 transacciones al mes, ticket promedio $15, todo en dólares;
fee de plataforma $10,000; tarifa variable como % del volumen aprobado "como en la propuesta de Yango";
motor de suscripciones $0.02 por transacción enviada.
Ajuste de German (2-oct, tarde): los tramos se definen por número de transacciones aprobadas, no por volumen aprobado.
Porcentajes dados por German (2-oct): empieza en 0.28% y baja a 0.24%. SUPUESTO (por confirmar con German): el corte
de 100,000 transacciones es el corte de Yango ($1.5M) dividido por el ticket de $15."""
TX = 150_000                      # transacciones al mes (German)
TICKET = 15                       # ticket promedio en dólares (German)
VOL = TX * TICKET                 # volumen aprobado mensual
PLATFORM = 7_000                  # fee de plataforma mensual (German, 6-oct: baja de $10,000 a $7,000)
R1, R2, CUT_TX = 0.0028, 0.0024, 100_000  # % del valor de cada transacción aprobada (German, 2-oct: 0.28% y 0.24%); corte en transacciones aprobadas (supuesto)
CUT = CUT_TX * TICKET             # equivalente en volumen (v1 del slide, por volumen)
TX1, TX2 = min(TX, CUT_TX), max(TX - CUT_TX, 0)
SUBS = 0.015                      # por transacción enviada por el motor de suscripciones (German, 6-oct: baja de $0.02 a $0.015)
SUBS_S = ('$%.3f' % SUBS).rstrip('0').rstrip('.')  # '$0.015' en el slide (nunca '$0.02' con tres decimales)
SUBS_TX = TX                      # supuesto: las 150,000 pasan por el motor, un envío por transacción
SUBS_FREE = 50_000                # primeras 50,000 transacciones del motor sin costo (German, 2-oct); supuesto: por mes
MIN_BILL = 10_000                 # facturación mínima mensual (German, 6-oct: baja de $14,000 a $10,000)
COMMIT = MIN_BILL - PLATFORM      # compromiso en transacciones que suma al fee de plataforma
COMMIT_TX = COMMIT / (R1 * TICKET)  # transacciones aprobadas que cubren el compromiso, al ticket de $15 y la tarifa del tramo 1
assert COMMIT_TX <= CUT_TX
def variable(vol):
    return min(vol, CUT) * R1, max(vol - CUT, 0) * R2
t1, t2 = variable(VOL)
var = t1 + t2
SUBS_BILL = max(SUBS_TX - SUBS_FREE, 0)
subs = SUBS_BILL * SUBS
total = var + subs + PLATFORM
def K(v):   # $2.25M / $750K
    return f"${v/1e6:.2f}M".replace('.00M', 'M').replace('0M', 'M') if v >= 1e6 else f"${v/1e3:,.0f}K"
if __name__ == '__main__':
    print(f"volumen aprobado: ${VOL:,.0f}/mes  ${VOL*12:,.0f}/año")
    print(f"tramo 1: {TX1:,} trx x ${TICKET} x {R1:.2%} = ${t1:,.0f} | tramo 2: {TX2:,} trx x ${TICKET} x {R2:.2%} = ${t2:,.0f}")
    assert abs(t1 - TX1 * TICKET * R1) < 1e-6 and abs(t2 - TX2 * TICKET * R2) < 1e-6
    print(f"variable: ${var:,.0f}/mes ${var*12:,.0f}/año  = ${var/TX:.4f}/trx  {var/VOL:.3%} efectivo")
    print(f"suscripciones: ({SUBS_TX:,} - {SUBS_FREE:,} gratis) = {SUBS_BILL:,} x {SUBS_S} = ${subs:,.0f}/mes ${subs*12:,.0f}/año")
    print(f"plataforma: ${PLATFORM:,}/mes ${PLATFORM*12:,}/año")
    print(f"TOTAL: ${total:,.0f}/mes ${total*12:,.0f}/año  all-in ${total/TX:.4f}/trx  {total/VOL:.3%} del volumen")
    print(f"por trx de cada tramo: ${TICKET*R1:.4f} / ${TICKET*R2:.4f}; suscripciones como % del ticket: {SUBS/TICKET:.3%}")
    for ap in (0.85,): print(f"sensibilidad: si 150,000 son las aprobadas a {ap:.0%}, envíos >= {TX/ap:,.0f} -> suscripciones ${(TX/ap-SUBS_FREE)*SUBS:,.0f}/mes")
    print(f"facturación mínima ${MIN_BILL:,} = ${PLATFORM:,} plataforma + ${COMMIT:,} en transacciones = {COMMIT_TX:,.1f} trx aprobadas a ${R1*TICKET:.3f} (0.28% x $15); con suscripciones contando: {(COMMIT + SUBS_FREE*SUBS)/(R1*TICKET + SUBS):,.0f} trx")
    print(K(VOL), K(CUT), K(VOL - CUT))
