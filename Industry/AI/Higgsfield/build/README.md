# Higgsfield_Yuno_SEP 2026 build (Google Slides)

Deck: https://docs.google.com/presentation/d/17V3SJ4ErlM_8RMq46XG0nRkdau9NYAYz4rX3ilDxI8g/edit
Built 2026-09-16 by copying the Google Slides "OpenAI_Yuno_MAY 2026" (same element IDs) and replacing every text element via the Slides API with Higgsfield data, preserving per-paragraph styles.

- engine.py: Slides API auth (~/.config/yuno-slides/token.json), text replacement with style preservation, positional matching.
- content.py: per-slide text by element ID, three grids (top 20, wave 2, Lever 1 ranking).
- countries.py: 18 country slides (stats verified 2026-09-16 with primary sources; numbers from ../model).
- extras.py: bubble chart remap (S12) and the two new slides (industry context, what Higgsfield gets).
- apply.py: `python3 apply.py dry` simulates and scans for leftover tokens; `python3 apply.py` applies. extras_run.py / model_run.py create the new slides.
