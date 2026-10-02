# Propuesta - UNICEF Colombia + Yuno (build, 2026-10-02)

Deck: https://docs.google.com/presentation/d/111EW1tmbSYPYtxLYRa5Mf_yx0Cn-BxA4wT2FAZeGpe0/edit
Auth: service account `~/.config/gsuite/sa.json` (el deck está compartido con gtm-claude-editor como editor).

Orden de ejecución (ya aplicado, no volver a correr sobre el mismo deck):
1. `dump.py [n ...]`: vuelca IDs, posición y texto de los slides.
2. `build_unicef.py dry` / `build_unicef.py`: textos por element ID, borrados (slide de Perú, franja de conciliación de Línea Directa), cajas y logos.
3. `fix1.py`: segunda pasada tras la revisión visual (ventajas clave del S11, alineación del fee de plataforma).
4. `fix2_tx_tiers.py`: pricing v2, tramos por número de transacciones aprobadas (0 a 100,000 y más de 100,000) en vez de volumen aprobado; solo el slide de pricing. Compara contra el estado anterior para no pisar ediciones manuales.
5. `fix3_rates.py`: pricing v3, 0.28% y 0.24% (antes 0.25% y 0.20%); solo el slide de pricing.
6. `qa.py`: tokens prohibidos, guiones, elementos fuera de página y hoja de contacto.

- `model.py`: toda la aritmética del pricing. Cambiar ahí los porcentajes, el corte de tramo, el volumen o el precio de suscripciones.
- `common.py`: helpers de Línea Directa (`fmt_requests`, `box_req`, `geom`, `thumbs`).

Para cambiar el pricing sobre el deck ya construido: editar `model.py` y escribir un `fix4_*.py` con el patrón de `fix3_rates.py` (IDs `g3fb7d86b358_4_*` y `ld_commit_*`). Antes de pisar, comparar contra el estado guardado para no borrar ediciones manuales de German.
