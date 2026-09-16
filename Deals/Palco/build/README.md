# Propuesta - Palco + Yuno (Google Slides build, 2026-09-16)

Deck: https://docs.google.com/presentation/d/1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY/edit
Origen: copia Drive de "Proposal - AppMaking + Yuno" (1oH2wwoz3EMYLKNMARaj23AVMf_C-hkPzdfLWnVZfNmc), carpeta Drive "Palco".
Motor: Industry/AI/Higgsfield/build/engine.py (token ~/.config/yuno-slides/token.json, solo scope presentations; la copia se hizo con el conector Drive de claude.ai).

- content_palco.py: texto en español por element ID (18 slides), filas del slide 13, movimientos, borrados y filas nuevas.
- build_palco.py: `python3 build_palco.py dry` simula y reporta IDs faltantes y tokens en inglés; sin `dry` aplica y baja thumbnails.
- fixes_palco.py: segunda pasada (estilo de las banderas emoji en S9, textos cortos S6/S7/S16, anclaje TOP en S7, logo Palco en portada).
- logo_url.txt: PNG público del wordmark blanco de Palco (SVG oficial de pal.co recortado vía images.weserv.nl).

Lección: el Slides API cuenta índices en UTF-16; cada bandera emoji son 4 unidades. El engine usa len() de Python, así que los rangos quedan cortos y las últimas letras heredan el estilo por defecto. Fix: updateTextStyle con range ALL.
