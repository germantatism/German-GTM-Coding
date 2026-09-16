# Propuesta - Palco + Yuno (Google Slides build, 2026-09-16)

Deck: https://docs.google.com/presentation/d/1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY/edit
Origen: copia Drive de "Proposal - AppMaking + Yuno" (1oH2wwoz3EMYLKNMARaj23AVMf_C-hkPzdfLWnVZfNmc), carpeta Drive "Palco".
Motor: Industry/AI/Higgsfield/build/engine.py (token ~/.config/yuno-slides/token.json, solo scope presentations; la copia se hizo con el conector Drive de claude.ai).

- content_palco.py: texto en español por element ID (18 slides), filas del slide 13, movimientos, borrados y filas nuevas.
- build_palco.py: `python3 build_palco.py dry` simula y reporta IDs faltantes y tokens en inglés; sin `dry` aplica y baja thumbnails.
- fixes_palco.py: segunda pasada (estilo de las banderas emoji en S9, textos cortos S6/S7/S16, anclaje TOP en S7, logo Palco en portada).
- logo_url.txt: PNG público del wordmark blanco de Palco (SVG oficial de pal.co recortado vía images.weserv.nl).

Lección: el Slides API cuenta índices en UTF-16; cada bandera emoji son 4 unidades. El engine usa len() de Python, así que los rangos quedan cortos y las últimas letras heredan el estilo por defecto. Fix: updateTextStyle con range ALL.

## Sección de contexto (16-sep, noche)
- readjust_3709.py: business case a ticket $37.09 vía replaceAllText (conserva negritas) + fixes de texto + notas de S11 borradas.
- build_context.py + fix_context.py: agenda de 4 puntos, divisor "Nuestro entendimiento del contexto" (dup de S3), slides "Resumen ejecutivo" (ctx_a2) y "La capa de pagos de Palco hoy" (ctx_b2) construidos sobre duplicados de S13 conservando sus tarjetas redondeadas, divisor "Propuesta" (dup de S12) antes del pricing. Deck final: 24 slides.
Lecciones API: los IDs de objeto deben tener 5+ caracteres y ser únicos en todo el deck; createShape normaliza el tamaño base a 3,000,000 EMU y pasa el tamaño real a la escala del transform; ROUND_RECTANGLE creado por API usa radio = 16.7% del lado corto y no se puede ajustar (duplicar una tarjeta existente hereda su radio); las tablas nativas tienen 7.2pt de relleno por celda (una fila de 7pt mide ~22pt), mejor tablas con formas; updateSlidesPosition usa el índice del orden previo sin sumar uno; createImage desde el contentUrl de otro icono del deck no renderizó (usar glifo ↗).
