#!/usr/bin/env python3
"""
slides_thumbs.py: visual QA for a deck without LibreOffice.

This Mac has no soffice/pdftoppm, so the render step of the QA is done through Google Slides:
  1. Upload the .pptx to Google Drive and open it as Google Slides (File > Save as Google Slides,
     or upload with "Convert uploads" on). Copy the presentation id from the URL.
  2. python3 slides_thumbs.py <presentationId> <outdir> [start-end]
     Downloads LARGE thumbnails of every slide (or the range) to <outdir>/S##.png.
  3. Look at every image: overflow, overlap, clipped text, orphan words in titles, empty space.

Uses German's existing Slides API token (~/.config/yuno-slides/token.json, scope: presentations),
the same one the Higgsfield build used (Industry/AI/Higgsfield/build/engine.py).
"""
import os, sys, pathlib, urllib.request

TOKEN = os.path.expanduser("~/.config/yuno-slides/token.json")


def service():
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
    creds = Credentials.from_authorized_user_file(TOKEN)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        open(TOKEN, "w").write(creds.to_json())
    return build("slides", "v1", credentials=creds, cache_discovery=False)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    pres_id, outdir = sys.argv[1], pathlib.Path(sys.argv[2])
    outdir.mkdir(parents=True, exist_ok=True)
    svc = service()
    pres = svc.presentations().get(presentationId=pres_id).execute()
    slides = pres.get("slides", [])
    start, end = 1, len(slides)
    if len(sys.argv) > 3 and "-" in sys.argv[3]:
        a, b = sys.argv[3].split("-", 1)
        start, end = int(a), int(b)
    print(f"{pres.get('title')} · {len(slides)} slides · saving {start}-{end} to {outdir}")
    for n in range(start, end + 1):
        page_id = slides[n - 1]["objectId"]
        th = svc.presentations().pages().getThumbnail(
            presentationId=pres_id, pageObjectId=page_id,
            thumbnailProperties_thumbnailSize="LARGE").execute()
        target = outdir / f"S{n:02d}.png"
        urllib.request.urlretrieve(th["contentUrl"], target)
        print(f"  S{n:02d} -> {target}")
    print("Done. Open the PNGs and walk references/qa-checklist.md section 5.")


if __name__ == "__main__":
    main()
