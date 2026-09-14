# Appmaking: respuestas a las preguntas abiertas de Tatsiana

Hilo Gmail: "Appmaking + Yuno: Call Recap and Next Steps" (Tatsiana Gubarevich, Payment Manager; cc Dzmitry Katsiushchyk, Jarrett Falasco, Sean).
El 14-sep German prometió enviar "throughout the day" las muestras TC40/SAFE y las respuestas a las preguntas nuevas.
Call: **martes 15-sep, 9:00 AM COT / 5:00 PM hora de ellos** (Dzmitry ya aceptó).

## Tracker

| # | Pregunta | La hicieron | Estado |
|---|---|---|---|
| 1 | Muestra de reporte TC40 y SAFE (formato de entrega) | 8-sep | Explicación y payload de Leo recibidos. Faltan 2 confirmaciones (ver abajo) |
| 2 | ¿El TRID (Token Requestor ID) queda abierto bajo su propia entidad merchant? | 14-sep | Pendiente |
| 3 | ¿Quién es su proveedor de prevention alerts? | 14-sep | Pendiente |
| 4 | Lista completa de PSPs con los que trabajan | 14-sep | Pendiente |
| 5 | ¿Presentan merchants a bancos? | 8-sep | German lo difirió a la call |
| 6 | Pricing por escrito sobre su ramp-up | 8-sep | En curso: appmaking-pricing-proposal-2026-09-10.md |

## 1. TC40 y SAFE

**Fuente: Leo, quien lidera este tema internamente (14-sep, vía German).**

### Cómo funciona (explicación de Leo)
- **Yuno no le manda el archivo al merchant, lo lee por él.**
- Cuando el banco del tarjetahabiente le reporta a Visa (**TC40**) o a Mastercard (**SAFE**) que un pago fue fraude, el proveedor le pasa esa alerta a Yuno.
- Yuno le manda al merchant un aviso de ese pago puntual, llamado **pre-chargeback** (webhook `payment.pre_chargeback`).
- Es **solo un aviso**: todavía no es un contracargo y no se ha movido plata. Así el merchant alcanza a devolver el pago o bloquear al cliente antes de que se vuelva un contracargo de verdad.

### Operación interna (German, 14-sep)
- dLocal deja los archivos en un SFTP; el equipo de Thiago baja la data; Leo la convierte en webhook al merchant.
- Al merchant no le llega ningún archivo: la comunicación es solo por webhook.
- "The only provider right now with TC40 and SAFE is dLocal."
- Si quieren más proveedores, nos cuentan y vemos cómo organizarlo.

### Ejemplo real enviado a un merchant (datos tapados, compartido por Leo)

```json
{
  "type": "payment",
  "type_event": "payment.pre_chargeback",
  "account_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "retry": 0,
  "version": 2,
  "data": {
    "payment": {
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "account_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "description": "Ecommerce Order",
      "country": "BR",
      "status": "SUCCEEDED",
      "sub_status": "APPROVED",
      "order_id": "ORDER-123456",
      "created_at": "2026-04-29T04:44:49.904820Z",
      "updated_at": "2026-06-03T12:41:17.236899Z",
      "amount": {
        "currency": "BRL",
        "value": 35.9,
        "refunded": 0.0,
        "captured": 0.0
      },
      "transactions": {
        "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "type": "PRE_CHARGEBACK",
        "status": "CREATED",
        "category": "WALLET",
        "amount": 35.9,
        "provider_id": "ADYEN",
        "response_code": "ACTION_REQUIRED",
        "response_message": "Chargeback or Inquiry received. Decision or documentation must be provided",
        "reason": "FRAUDULENT",
        "description": "webhook transaction",
        "created_at": "2026-06-03T12:41:17.184528Z",
        "updated_at": "2026-06-03T12:41:17.212602Z",
        "payment_method": {
          "type": "GOOGLE_PAY"
        },
        "provider": {
          "provider_transaction_id": "XXXXXXXXXXXXXXXX"
        },
        "provider_data": {
          "id": "ADYEN",
          "transaction_id": "XXXXXXXXXXXXXXXX",
          "status": "NOTIFICATION_OF_FRAUD"
        }
      }
    }
  }
}
```

**Cómo leerlo (Leo):** el pago sigue aprobado (`status: SUCCEEDED`, `sub_status: APPROVED`); el aviso es `type: PRE_CHARGEBACK` con `reason: FRAUDULENT`; `provider_data.status: NOTIFICATION_OF_FRAUD` es la alerta de fraude que mandó el proveedor.

### ⚠️ Antes de escribir el correo

1. **El ejemplo es de Adyen, no de dLocal.** Choca con "el único proveedor con TC40 y SAFE es dLocal". Posible lectura: dLocal es el único vía archivo SFTP y Adyen lo manda por su propia notificación. Confirmar con Leo qué proveedores lo soportan hoy. Ojo: ninguno de los dos está en su fase 1, y Adyen además está bloqueado por su exclusividad con Solidgate.
2. **Sanitizar más antes de compartirlo.** Los IDs están tapados, pero el ejemplo sigue mostrando datos de otro merchant (Brasil, BRL 35.90, Adyen, Google Pay, fechas). Mandar una versión con valores genéricos y decir que es ilustrativa. Regla Riot: nada de un cliente a terceros sin permiso.
3. **No es exactamente lo que pidieron.** Pidieron una "muestra de reporte TC40 y SAFE" y, en la call del 4-sep, tasas de banco y de fraude por PSP. Lo que existe es un aviso por pago, no un reporte agregado ni tasas por PSP.

### Corrección pendiente frente al recap del 4-sep
El recap dice: "TC40 and SAFE data, bank and fraud rates are delivered today as normalized reports across all your providers, with dashboard views on the roadmap." Lo real hoy:
- Entrega por **webhook por pago** (pre-chargeback), no como reporte ni archivo.
- Solo con **algunos proveedores** (dLocal confirmado; Adyen por confirmar), no con todos.
- Ninguno de los dos está en su fase 1 (Stripe, Ecompay, Unlimit, Airwallex, Shift4, Payabl, NMI).

**Implicaciones para el correo:**
- Explicar el flujo en simple (lo leemos por ustedes y les avisamos por pago) y adjuntar el payload ilustrativo.
- Corregir el recap con claridad, sin esconderlo.
- Ofrecer organizar TC40/SAFE con sus PSPs de fase 1 si es prioridad para ellos.

## 2. TRID

Pendiente.

## 3. Proveedor de prevention alerts

Pendiente.

## 4. Lista completa de PSPs

Pendiente.

## 5. Presentación a bancos

Diferido a la call del 15-sep.
