# PeYa + Yuno | Resumen del call del 29-sep-2026

**Fecha:** martes 29-sep-2026, 1:30 p.m. COT (11:30 a.m. PT), Google Meet, 32 min
**Yuno:** German Tatis, Alejandro Albarracín (organizador)
**PedidosYa:** Belén Casaret (lidera Collections)

**Fuente:** notas del call que pasó German. El transcript de Google Meet quedó inservible (transcribió el español como inglés), así que nada de esto está contrastado contra grabación.

## Contexto de Belén

- Lidera Collections en PedidosYa, lleva 3 meses en el cargo y opera en 15 países.
- Alcance de Collections: solo B2B. Cubre la deuda de los partners por comisiones, servicios de marketing y créditos.
  - La deuda nace cuando la liquidación semanal no cubre lo que el partner debe.
  - Los servicios de marketing se facturan aparte, a 30/60/90 días, y se pagan offline.
- Dos segmentos de partners:
  - Multi (McDonald's, Carrefour, Coto): pagan por portal, email o transferencia bancaria; ordenados.
  - Non-multi (restaurantes chicos): más difíciles de contactar y con más deuda sin resolver.
- Más de 20.000 cuentas en cobranza; unas se gestionan in-house y otras en agencias externas (etapa de write-off).

## Dolores

- **Conciliación:** un banco por país, 15 bancos en total, cada uno devuelve un formato de datos distinto.
  - Muchos bancos no identifican quién pagó; en varios mercados no llega CUIT ni información del ordenante.
  - Los pagos llegan sin matchear y dejan un volumen grande de partidas abiertas en el ledger de deudores.
  - Hoy es manual; quiere automatizarlo.
- **Métodos de pago:** los partners solo pueden pagar por transferencia bancaria, efectivo en Western Union o dLocal (3 a 4 países).
  - Los links de dLocal no son permanentes y se generan a mano, por transacción y por monto.
  - No hay checkout ni opción de autoservicio para los partners.
- **Portal de vendors:** existe, pero Collections no está integrado; el partner no puede ver ni pagar su deuda ahí.
- **Dos objetivos claros:** saber quién está pagando y lograr que más partners paguen.

## Fit

- Tres frentes conversados:
  - Métodos de pago nuevos con un checkout embebido en el portal de vendors.
  - Agregación bancaria: vista unificada de los 15 países bajo una API.
  - Motor de conciliación: matchear pagos con partners sin comprobante manual.
- Las conversaciones anteriores de Yuno con PedidosYa fueron B2C (pay-ins); esta es la primera exploración B2B.
- Belén pidió un recorrido concreto de cómo funcionaría de punta a punta la identificación del partner y el matching.

⚠️ Por confirmar con producto antes del deep dive: qué está disponible hoy (GA) en conciliación y en agregación bancaria. En los decks la conciliación de settlement, payouts y fees va marcada como roadmap, y el brief del 29-sep ya advertía no prometerla sin confirmación. El research previo encontró que PeYa usa Simetrik y SAP para conciliación (job listing).

## Próximos pasos

1. **German:** enviar a Belén opciones de agenda para el deep dive demo. Belén suma a Fanny (líder de Cash Application, dueña operativa). Prefieren jueves o viernes; están en cierre de mitad de mes, así que puede pasar a la semana siguiente. Borrador en Gmail con jueves 8 o viernes 9-oct.
2. **Belén:** compartir la lista de bancos de los 15 países. **Yuno:** revisar cobertura.
3. **German:** confirmar con producto el alcance real de conciliación y agregación bancaria antes de la demo.
