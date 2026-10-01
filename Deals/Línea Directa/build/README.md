# Propuesta - Línea Directa + Yuno (build, 2026-09-30)

Deck: https://docs.google.com/presentation/d/126rE0knbVczAsHtRVCtRWopV4lOh3yrKx5038hhjdew/edit
Auth: service account `~/.config/gsuite/sa.json` (el deck está compartido con gtm-claude-editor como editor).

Orden de ejecución (ya aplicado, no volver a correr sobre el mismo deck):
1. `dump.py [n ...]`: vuelca IDs, posición y texto de los slides.
2. `step0_dup_methods.py`: duplica el slide de pricing intacto como lienzo del slide de métodos (`ld_methods`, IDs `ldm_*`).
3. `build_ld.py dry` / `build_ld.py`: textos por element ID (`content_ld.py`), borrados, cajas y logos.
4. `build_methods.py`: slide de métodos de pago de Colombia y Perú.
5. `fix1.py`: segunda pasada tras la revisión visual.
6. `fix2_commitment.py`: pricing v2 (platform $7,500 + compromiso mínimo de $7,500 = facturación mínima de $15,000); solo el slide de pricing.
7. `fix3_orchestration_recon.py`: pricing v3 (orquestación y smart routing incluidos; conciliación $1,000 por 200,000 trx + $0.03 adicional en la franja inferior). Compara contra el estado anterior para no pisar ediciones manuales.
8. `qa.py`: tokens prohibidos, guiones, elementos fuera de página y hoja de contacto.

- `model.py`: toda la aritmética del business case y del pricing. Cambiar ahí el corte de tramo, las tarifas o los supuestos y volver a generar los textos.
- `common.py`: `fmt_requests` reemplaza texto con marcas `**negrita**` conservando los estilos regular y negrita del elemento original; `box_req` mueve y redimensiona en puntos.

Para un ajuste puntual de texto sobre el deck ya construido, usar el patrón de `fix1.py` (estilos tomados del JSON original).

Ojo: German quitó a mano la sección de Business Case el 30-sep; el deck tiene 20 slides. `build_ld.py` y `content_ld.py` quedan como registro de la v1 (referencian elementos que ya no existen).
