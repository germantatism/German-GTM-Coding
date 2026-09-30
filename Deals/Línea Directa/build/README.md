# Propuesta - Línea Directa + Yuno (build, 2026-09-30)

Deck: https://docs.google.com/presentation/d/126rE0knbVczAsHtRVCtRWopV4lOh3yrKx5038hhjdew/edit
Auth: service account `~/.config/gsuite/sa.json` (el deck está compartido con gtm-claude-editor como editor).

Orden de ejecución (ya aplicado, no volver a correr sobre el mismo deck):
1. `dump.py [n ...]`: vuelca IDs, posición y texto de los slides.
2. `step0_dup_methods.py`: duplica el slide de pricing intacto como lienzo del slide de métodos (`ld_methods`, IDs `ldm_*`).
3. `build_ld.py dry` / `build_ld.py`: textos por element ID (`content_ld.py`), borrados, cajas y logos.
4. `build_methods.py`: slide de métodos de pago de Colombia y Perú.
5. `fix1.py`: segunda pasada tras la revisión visual.
6. `qa.py`: tokens prohibidos, guiones, elementos fuera de página y hoja de contacto.

- `model.py`: toda la aritmética del business case y del pricing. Cambiar ahí el corte de tramo, las tarifas o los supuestos y volver a generar los textos.
- `common.py`: `fmt_requests` reemplaza texto con marcas `**negrita**` conservando los estilos regular y negrita del elemento original; `box_req` mueve y redimensiona en puntos.

Para un ajuste puntual de texto sobre el deck ya construido, usar el patrón de `fix1.py` (estilos tomados del JSON original).
