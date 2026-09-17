# Suno + Yuno | Technical Deep Dive, 17 sep 2026 (13:00 a 14:00 COT)

Invitados: Gurwinder Gulati, Madden Titus, Ben Rawstron (opcional) por Suno; German Tatis, Jarrett Falasco (demo), Caio Freitas Ferreira, Sean Calabro, Justo Benetti por Yuno. Asistencia real no registrada en estas notas.

## Notas a mano de German
- No interest on PCI (usan iframe; el scope PCI no es driver)
- Metadata routing, 120 fields
- Subscription
- Agnostic 3DS -> orchestration
- Smart Routing -> pick 2 processors to help ML choose the next best processor -> retries under smart routing
- Remove from Stripe Billing so they can control billing in house
- Leave billing
- Reconciliations
- Later: data visibility, insights + reporting, monitors, in-house subscriptions
- Debrief (interno, pendiente)

## Resumen estructurado

### Setup actual de Suno
- Stripe only, US entity only
- Stripe Billing para suscripciones (web y app, hoy al mismo precio)
- Dolor principal: el retry/recovery engine de Stripe no es confiable
- Web y app se manejan por separado; sin setup multi-país todavía

### Demo (Jarrett)
- Estructura multi-cuenta: recomendado separar por país (ej. Brasil vs México) para reglas de routing limpias; cuenta única posible pero suma complejidad; reglas compartidas vía API
- Marketplace de proveedores: cards, APMs, wallets (Apple Pay, Google Pay). Wallets nativas: Yuno desencripta el criptograma y lo envía como card, lo que habilita retries y fallbacks de wallets entre adquirentes
- Checkout: una sola capa de UI para todos los métodos; APMs nuevos (ej. NuPay) se activan desde el dashboard sin front-end; el SDK completa campos faltantes (nombre, email, documento) según el proveedor

### Routing y retries
- Routing dinámico por reglas sobre 100+ campos del request + metadata. Ejemplo: suscripción va a Stripe, en decline cae 50/50 a Adyen y wallets. Decline groups (soft vs hard) deciden si reintentar y con quién
- MIT vs CIT separados: MIT rutea conservador; la estrategia de dunning/retry puede quedarse en Suno si prefieren
- Smart routing: ML sobre auth rate y costo con los últimos 30 días; necesita al menos 2 procesadores; permite split de tráfico (ej. 20% smart / 80% reglas) para A/B
- Agnostic 3DS: autenticación desacoplada de autorización; la misma autenticación se reutiliza entre proveedores en un decline (pasa ECI, liability shift); 3DS condicional (ej. solo si el emisor lo exige)
- Provider health monitoring: redistribuye tráfico si un proveedor cae o hace timeout; evita pagar por intentos fallidos

### Migración y próximos pasos
- Migración de tokens de Stripe: herramienta de export al vault de Yuno; vault agnóstico, tokens sirven con cualquier adquirente conectado
- Suno puede conservar su propio retry/dunning y usar Yuno solo para routing y vault
- Primer paso recomendado: optimización de auth rate en un mercado, luego expandir
- Caio entrega credenciales de sandbox para que exploren y den feedback

## Next steps acordados
1. Enviar credenciales de sandbox a Suno (Caio)
2. Compartir documentación de SDK y reporting (Caio)
3. Agendar sesión de estrategia de routing con Suno

## Pendientes previos que NO se tocaron en esta llamada (seguir empujando)
- NDA (necesario para el data sprint)
- Reference call de migración desde Stripe (Justo la ofreció el 7-ago)
- Fecha del data sprint
