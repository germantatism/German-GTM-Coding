# FlightHub · two questions for Jarrett (Sep 22 in-person, Will's notes)

1. Can we schedule retries with a delay on a route (wait X seconds or minutes before retrying, instead of retrying instantly)? If not, is it on the roadmap?
2. Can we orchestrate chargebacks and disputes across their providers, in the dashboard and via API? How does it work? They already have a chargeback provider.

## Jarrett's answers (Slack, Sep 22, 2026, 12:39 PM)

**Q1, scheduled / delayed retries.** "Right now there is no configurable delay in the failover logic. A full retry (create payment call) is controlled by them already today, so they could put in whatever retry logic they want. Latency and user experience is the only thing they have to keep in mind. I would need to know more about what they are trying to accomplish to give them a better response."

Lectura: el failover (cascada al siguiente proveedor) es instantáneo y sin delay configurable. Un retry con espera lo implementa FlightHub desde su lado con una nueva llamada de create payment; Yuno no lo programa hoy. Antes de responderles, aclarar qué quieren lograr con el delay (soft declines, timeouts, límites de issuer).

**Q2, orchestrate chargebacks and disputes.** "The answer to 2 is yes. I could give you the real answer but I'd get in trouble, so yes to 2. I'd check with Martin to see who owns dispute from product to align with our current capabilities and roadmap."

Lectura: sí con matices. La capacidad real de gestión de disputas (portal, API, orquestación entre proveedores) no está cerrada; confirmar alcance actual vs roadmap con Martin Mexia (SVP Product) antes de prometer detalles a FlightHub. Ellos ya tienen proveedor de chargebacks, así que el mensaje seguro es: visibilidad y alertas hoy, gestión completa a validar con Producto.

**Pendiente:** hablar con Martin para saber quién es el owner de disputes en Producto y qué hay live vs roadmap.
