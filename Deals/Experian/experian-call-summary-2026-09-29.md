# Experian + Yuno | Suscripciones: resumen del call del 29-sep-2026

**Fecha:** martes 29-sep-2026, 2:00 a 2:45 p.m. COT (12:00 p.m. PT), Google Meet, 41 min
**Yuno:** German Tatis, Daniel Lozano (PM Subscriptions), Joaquín Mann
**Experian:** Carlos Falla (PM), Cristian Vargas (dueño de Midatacrédito)

**Fuente:** notas del call que pasó German. El transcript de Google Meet quedó inservible (transcribió el español como inglés) y la llamada aún no estaba en Gong al redactar, así que nada de esto está contrastado contra grabación.

## Correcciones a las notas

- "Breve" en las notas es **Bre-B** (el sistema de pagos inmediatos del Banco de la República). Misma confusión que en el transcript del 23-sep.
- Las notas dicen "retoma tras pausa de ~2 meses por falta de urgencia". La llamada anterior fue el 23-sep (seis días antes); la pausa larga fue de abril a septiembre. Dato sin verificar, no usar en correos.
- "Milena disponible; probable fin de semana": se interpreta como fin de esta semana (jueves 1 o viernes 2 de octubre), no sábado o domingo. Por confirmar con Cristian.
- "OnePay" aparece como ejemplo de conexión en el marketplace. Sin verificar el nombre.

## Contexto y agenda

- Sesión de hoy: deep dive en el motor de suscripciones.
- Sesión pendiente: motor de reconciliaciones, con Milena (Experian, operaciones). La sesión que se había propuesto para el 30-sep nunca se agendó.

## Demo: conexiones y ruteo

- Marketplace de conexiones: integrar procesadores con pocos clics (ejemplos mostrados: Wompi, PayU).
- Checkout Builder: los métodos de pago se prenden y apagan sin desarrollo adicional.
- Tokenización PCI: cada método queda guardado en bóveda; los reintentos pueden ir entre procesadores.
- Ruteo configurable por porcentaje (50/50, 70/30) con hasta 2 fallbacks. Si PayU declina, Wompi rescata la transacción.
- Condiciones por BIN, país emisor, banco emisor o metadata personalizada.
- Smart Routing usa ML para optimizar conversión y costo a la vez.

## Demo: motor de suscripciones

- Planes configurables: ciclos (semanal, quincenal, mensual, trimestral, etc.), prepago o pospago, precio por país.
  - Ejemplo mostrado: precio introductorio de $39.900 por 6 meses, luego $44.900.
- Reintentos de cobro: estándar (5 min, 5 h, 17 h, 41 h, 3 d, 5 d, 9 d), Smart Recharge (ML) o custom.
  - A/B testing de estrategias desde la plataforma.
  - El ML considera comportamiento del usuario, procesador, país, monto y moneda.
- Gestión desde el dashboard: cancelar, pausar (indefinido o por plazo), upgrade y downgrade. Se puede mantener o reiniciar la fecha de cobro al cambiar de plan.
- Métricas: suscripciones activas, en prueba, canceladas (con motivo), distribución por plan, tasa de aprobación por intento.
- Meters (uso variable): cobro adicional por consumo sobre el límite del plan.

## Prioridades de Experian (Cristian)

1. **Débitos automáticos a cuentas de ahorro y corriente**, principalmente Davivienda y Grupo Aval.
2. **Tarjetas:** explorar procesadores alternativos a PayU. Cristian dijo que la efectividad viene bajando tras la adquisición. Cambio frente al 23-sep, cuando Carlos dijo que no querían tocar PayU ni Wompi.
3. **Bre-B** como medio de pago tokenizable (Yuno en proceso de habilitarlo).

## Lo que dijo Yuno

- Bancos: integración directa con Nubank y BBVA; explorando un tercero para acceder al pool de bancos colombianos.
- Banking as a service: en desarrollo, cierre esperado en las próximas semanas.

## Timeline

- Experian apunta a iniciar implementación en **abril de 2027**, inicio de su año fiscal. (El 23-sep Carlos había hablado de arrancar entre enero y marzo y terminar en abril o mayo.)
- Antes de eso necesitan adelantar el proceso interno de vinculación de proveedores y el caso de negocio.

## Próximos pasos

| Qué | Quién |
|---|---|
| Agendar la llamada de reconciliaciones con Milena | Cristian (Experian) |
| Compartir proveedores recomendados para tarjetas y débitos automáticos | German (Yuno) |
| Confirmar el estado de tokenización de Bre-B | Daniel (Yuno) |
| Tarifarios para el caso de negocio (pendiente desde el 23-sep) | German, consultando la Pricing Policy |

## Pendientes abiertos de llamadas anteriores

- Migración de cuentas de ahorro: el 23-sep se dijo "validando internamente, creemos que sí". Las notas de hoy no dicen si se cerró.
- Diagrama del flujo de integración que pidió Carlos: las notas de hoy no dicen si se presentó.
