#!/usr/bin/env python3
"""
swap_shirt.py - Replace the top a person is wearing with the black Yuno t-shirt
(matte black crew neck, white lowercase "yuno" wordmark on the chest), keeping
everything else in the photo untouched.

Pipeline
  1. Downscale the target photo to a working size the model accepts and pad it to
     the provider's supported aspect ratio (3:4 Gemini, 2:3 OpenAI).
  2. Send the padded photo + a reference photo of the real Yuno t-shirt to an
     instruction-following image editor (Gemini image models or OpenAI gpt-image-1).
  3. Take the edited image back, undo the padding, and build a soft mask from the
     pixel difference between original and edit, restricted to below the chin
     (--protect-top) so the face, hair and background can never be altered.
  4. Composite ONLY the masked region (upscaled) onto the untouched full-resolution
     original. Save the final at --max-side (default 3800 px) plus debug files.

Usage
  GEMINI_API_KEY=... python3 tools/swap_shirt.py \
      --input "Headshots/60.jpg" --reference "Headshots/55 copy.jpg" \
      --output "Headshots/60 - yuno shirt.jpg" --provider gemini

  OPENAI_API_KEY=... python3 tools/swap_shirt.py ... --provider openai

  Dry run (no API call, composites a given edited image instead):
  python3 tools/swap_shirt.py --input ... --edited some_edit.png --output ...

Only the standard library + Pillow are required.
"""
import argparse
import base64
import io
import json
import os
import sys
import urllib.request
import uuid
from pathlib import Path

from PIL import Image, ImageChops, ImageFilter, ImageOps

PROMPT = (
    "Edit the FIRST image. Replace the top the person is wearing (the brown "
    "sleeveless button-up top) with a plain black crew-neck short-sleeve cotton "
    "t-shirt, exactly like the t-shirt worn by the man in the SECOND (reference) "
    "image: matte black fabric, white lowercase 'yuno' wordmark printed on the "
    "chest, centered, same font, size and position as in the reference. "
    "The t-shirt has short sleeves that cover the shoulders and upper arms. "
    "Keep everything else in the first image completely unchanged: face, "
    "expression, hair, skin tone, jewelry (necklace, earrings, bracelets, ring), "
    "the crossed arms and hands, body pose, lighting, shadows, the plain light "
    "gray background, framing and image proportions. The crossed arms should "
    "naturally cover part of the t-shirt and of the logo, just as they cover the "
    "current top, with realistic fabric folds where the arms press against it. "
    "Photorealistic, same camera, sharpness and color grading as the original. "
    "Do not add, remove, move or restyle anything else."
)

ASPECT = {"gemini": (3, 4), "openai": (2, 3)}
DEFAULT_MODEL = {"gemini": "gemini-2.5-flash-image", "openai": "gpt-image-1"}


def log(msg):
    print(f"[swap_shirt] {msg}", flush=True)


def pad_to_aspect(img, aspect):
    """Pad (never crop) img with its edge color so width/height == aspect."""
    aw, ah = aspect
    w, h = img.size
    target_w, target_h = w, h
    if w / h > aw / ah:          # too wide -> add height
        target_h = round(w * ah / aw)
    else:                        # too tall -> add width
        target_w = round(h * aw / ah)
    fill = img.resize((1, 1), Image.BOX).getpixel((0, 0))
    canvas = Image.new("RGB", (target_w, target_h), fill)
    off = ((target_w - w) // 2, (target_h - h) // 2)
    canvas.paste(img, off)
    return canvas, off


def to_bytes(img, fmt="PNG", quality=95):
    buf = io.BytesIO()
    if fmt == "JPEG":
        img.save(buf, fmt, quality=quality)
    else:
        img.save(buf, fmt)
    return buf.getvalue()


# --------------------------------------------------------------------------- providers
def call_gemini(target_png, reference_jpg, model, api_key, image_size=None):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    parts = [
        {"inline_data": {"mime_type": "image/png",
                         "data": base64.b64encode(target_png).decode()}},
        {"inline_data": {"mime_type": "image/jpeg",
                         "data": base64.b64encode(reference_jpg).decode()}},
        {"text": PROMPT},
    ]
    body = {"contents": [{"role": "user", "parts": parts}],
            "generationConfig": {"responseModalities": ["IMAGE"]}}
    if image_size:
        body["generationConfig"]["imageConfig"] = {"imageSize": image_size}
    req = urllib.request.Request(
        url, data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "x-goog-api-key": api_key})
    with urllib.request.urlopen(req, timeout=300) as r:
        data = json.loads(r.read())
    for cand in data.get("candidates", []):
        for part in cand.get("content", {}).get("parts", []):
            blob = part.get("inline_data") or part.get("inlineData")
            if blob:
                return base64.b64decode(blob["data"])
    raise RuntimeError(f"Gemini returned no image: {json.dumps(data)[:800]}")


def call_openai(target_png, reference_jpg, model, api_key, size="1024x1536"):
    boundary = f"----swapshirt{uuid.uuid4().hex}"
    fields = [("model", model), ("prompt", PROMPT), ("size", size),
              ("quality", "high"), ("input_fidelity", "high"), ("n", "1")]
    files = [("image[]", "target.png", "image/png", target_png),
             ("image[]", "reference.jpg", "image/jpeg", reference_jpg)]
    body = io.BytesIO()
    for name, value in fields:
        body.write(f"--{boundary}\r\nContent-Disposition: form-data; "
                   f"name=\"{name}\"\r\n\r\n{value}\r\n".encode())
    for name, fname, mime, blob in files:
        body.write(f"--{boundary}\r\nContent-Disposition: form-data; name=\"{name}\"; "
                   f"filename=\"{fname}\"\r\nContent-Type: {mime}\r\n\r\n".encode())
        body.write(blob)
        body.write(b"\r\n")
    body.write(f"--{boundary}--\r\n".encode())
    req = urllib.request.Request(
        "https://api.openai.com/v1/images/edits", data=body.getvalue(),
        headers={"Authorization": f"Bearer {api_key}",
                 "Content-Type": f"multipart/form-data; boundary={boundary}"})
    with urllib.request.urlopen(req, timeout=600) as r:
        data = json.loads(r.read())
    return base64.b64decode(data["data"][0]["b64_json"])


# --------------------------------------------------------------------------- mask + composite
def build_mask(orig_small, edit_small, protect_top, ramp, threshold):
    """Soft mask (L) = where the edit differs from the original, below the chin."""
    w, h = orig_small.size
    a = orig_small.filter(ImageFilter.GaussianBlur(2))
    b = edit_small.filter(ImageFilter.GaussianBlur(2))
    diff = ImageChops.difference(a, b).convert("RGB")
    r, g, bl = diff.split()
    mx = ImageChops.lighter(ImageChops.lighter(r, g), bl)
    mask = mx.point(lambda v: 255 if v >= threshold else 0)
    mask = mask.filter(ImageFilter.MinFilter(5))     # drop speckles
    mask = mask.filter(ImageFilter.MaxFilter(21))    # grow to cover edges/folds
    mask = mask.filter(ImageFilter.GaussianBlur(6))  # feather
    # protect everything above the chin line, with a short vertical ramp
    y0, y1 = int(h * protect_top), int(h * (protect_top + ramp))
    grad = Image.new("L", (w, h), 255)
    px = grad.load()
    for y in range(0, y1):
        v = 0 if y < y0 else int(255 * (y - y0) / max(1, y1 - y0))
        for x in range(w):
            px[x, y] = v
    return ImageChops.multiply(mask, grad)


def composite(orig_full, edit_small, mask_small):
    edit_full = edit_small.resize(orig_full.size, Image.LANCZOS)
    mask_full = mask_small.resize(orig_full.size, Image.LANCZOS)
    return Image.composite(edit_full, orig_full, mask_full), mask_full


# --------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--input", required=True, help="photo of the person to edit")
    ap.add_argument("--reference", default=None, help="photo of the real Yuno t-shirt (German)")
    ap.add_argument("--output", required=True)
    ap.add_argument("--provider", choices=["gemini", "openai"], default="gemini")
    ap.add_argument("--model", default=None)
    ap.add_argument("--gemini-image-size", default=None, help="e.g. 2K or 4K for models that support it")
    ap.add_argument("--edited", default=None, help="skip the API and composite this edited image (dry run)")
    ap.add_argument("--work-side", type=int, default=1536, help="long side sent to the model")
    ap.add_argument("--max-side", type=int, default=3800, help="long side of the final JPEG")
    ap.add_argument("--protect-top", type=float, default=0.49, help="fraction of height that is never edited")
    ap.add_argument("--ramp", type=float, default=0.03)
    ap.add_argument("--threshold", type=int, default=28)
    ap.add_argument("--quality", type=int, default=92)
    ap.add_argument("--workdir", default=None, help="where to save debug files (default: next to output)")
    args = ap.parse_args()

    out = Path(args.output)
    workdir = Path(args.workdir) if args.workdir else out.parent / f"{out.stem}_work"
    workdir.mkdir(parents=True, exist_ok=True)

    orig_full = ImageOps.exif_transpose(Image.open(args.input)).convert("RGB")
    log(f"input {args.input}: {orig_full.size[0]}x{orig_full.size[1]}")

    small = orig_full.copy()
    small.thumbnail((args.work_side, args.work_side), Image.LANCZOS)
    padded, off = pad_to_aspect(small, ASPECT[args.provider])
    log(f"working size {small.size}, padded to {padded.size} (offset {off})")

    if args.edited:
        edited = Image.open(args.edited).convert("RGB")
        log(f"dry run: using {args.edited} {edited.size}")
    else:
        if not args.reference:
            sys.exit("--reference is required when calling the API")
        ref = ImageOps.exif_transpose(Image.open(args.reference)).convert("RGB")
        ref.thumbnail((1024, 1024), Image.LANCZOS)
        model = args.model or DEFAULT_MODEL[args.provider]
        key_name = "GEMINI_API_KEY" if args.provider == "gemini" else "OPENAI_API_KEY"
        api_key = os.environ.get(key_name)
        if not api_key:
            sys.exit(f"missing {key_name} in the environment")
        log(f"calling {args.provider} / {model} ...")
        if args.provider == "gemini":
            raw = call_gemini(to_bytes(padded), to_bytes(ref, "JPEG"), model, api_key,
                              args.gemini_image_size)
        else:
            raw = call_openai(to_bytes(padded), to_bytes(ref, "JPEG"), model, api_key)
        (workdir / "model_raw.png").write_bytes(raw)
        edited = Image.open(io.BytesIO(raw)).convert("RGB")
        log(f"model returned {edited.size}, saved {workdir / 'model_raw.png'}")

    # undo padding: map the model output onto the padded frame, then crop
    pw, ph = padded.size
    ratio_in, ratio_out = pw / ph, edited.size[0] / edited.size[1]
    if abs(ratio_in - ratio_out) / ratio_in > 0.01:
        log(f"WARNING: model changed the aspect ratio ({ratio_out:.3f} vs {ratio_in:.3f}); "
            "the composite may be misaligned")
    edited = edited.resize((pw, ph), Image.LANCZOS)
    edited_small = edited.crop((off[0], off[1], off[0] + small.size[0], off[1] + small.size[1]))

    mask_small = build_mask(small, edited_small, args.protect_top, args.ramp, args.threshold)
    final, mask_full = composite(orig_full, edited_small, mask_small)

    final_out = final.copy()
    final_out.thumbnail((args.max_side, args.max_side), Image.LANCZOS)
    final_out.save(out, "JPEG", quality=args.quality, subsampling=0)
    mask_small.save(workdir / "mask.png")
    edited_small.save(workdir / "edited_small.png")
    preview = final.copy(); preview.thumbnail((900, 900)); preview.save(workdir / "preview.jpg", quality=85)
    log(f"saved {out} ({final_out.size[0]}x{final_out.size[1]}); debug files in {workdir}")


if __name__ == "__main__":
    main()
