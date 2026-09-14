# Appmaking: respuestas a las preguntas abiertas de Tatsiana

Hilo Gmail: "Appmaking + Yuno: Call Recap and Next Steps" (Tatsiana Gubarevich, Payment Manager; cc Dzmitry Katsiushchyk, Jarrett Falasco, Sean).
El 14-sep German prometió enviar "throughout the day" las muestras TC40/SAFE y las respuestas a las preguntas nuevas.
Call: **martes 15-sep, 9:00 AM COT / 5:00 PM hora de ellos** (Dzmitry ya aceptó).

## Tracker

| # | Pregunta | La hicieron | Estado |
|---|---|---|---|
| 1 | Muestra de reporte TC40 y SAFE (formato de entrega) | 8-sep | Info interna recibida, ver abajo. Falta el ejemplo del payload |
| 2 | ¿El TRID (Token Requestor ID) queda abierto bajo su propia entidad merchant? | 14-sep | Pendiente |
| 3 | ¿Quién es su proveedor de prevention alerts? | 14-sep | Pendiente |
| 4 | Lista completa de PSPs con los que trabajan | 14-sep | Pendiente |
| 5 | ¿Presentan merchants a bancos? | 8-sep | German lo difirió a la call |
| 6 | Pricing por escrito sobre su ramp-up | 8-sep | En curso: appmaking-pricing-proposal-2026-09-10.md |

## 1. TC40 y SAFE

**Info interna de German (14-sep):**
- dLocal deja los archivos en un SFTP.
- El equipo de Thiago baja la data.
- Leo la convierte en webhook y eso es lo que se le envía al merchant.
- Al merchant no le llega el archivo: no hay comunicación por archivos, solo por webhook.
- Hoy el único proveedor con TC40 y SAFE es dLocal.
- Si quieren cobertura con más proveedores, que nos cuenten y vemos cómo organizarlo.

**⚠️ Choca con lo que ya se dijo por escrito.** El recap del 4-sep dice: "TC40 and SAFE data, bank and fraud rates are delivered today as normalized reports across all your providers, with dashboard views on the roadmap." Lo que hay hoy es otra cosa:
- Entrega por **webhook**, no como reporte ni archivo.
- Solo **dLocal**, no todos sus proveedores.
- dLocal **no está** en su lista de fase 1 (Stripe, Ecompay, Unlimit, Airwallex, Shift4, Payabl, NMI).

La respuesta tiene que corregir esto con claridad, sin esconderlo.

**Implicaciones para el correo:**
- La "muestra de reporte" que pidieron sería un **ejemplo del payload del webhook**, no un archivo.
- Ofrecer abiertamente organizar TC40/SAFE con sus PSPs de fase 1 si es prioridad para ellos.

**Por confirmar internamente:**
- Ejemplo real o sanitizado del payload del webhook TC40/SAFE (¿Leo?).
- Campos que trae, frecuencia y latencia desde que dLocal deja el archivo.
- Qué haría falta para sumar otro proveedor y en cuánto tiempo.

## 2. TRID

Pendiente.

## 3. Proveedor de prevention alerts

Pendiente.

## 4. Lista completa de PSPs

Pendiente.

## 5. Presentación a bancos

Diferido a la call del 15-sep.
