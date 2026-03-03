"""
save_research_to_gdrive.py

Saves the latest SDR Research Brief to a specific Google Drive folder
as a Google Doc, accessible to all Yuno users.

Usage:
    python scripts/save_research_to_gdrive.py --company "Ryanair"

Setup (one-time):
    1. Go to console.cloud.google.com
    2. Create a project → Enable "Google Drive API" + "Google Docs API"
    3. Create a Service Account → download credentials JSON
    4. Save credentials as config/gdrive_credentials.json
    5. Share your target Google Drive folder with the service account email
    6. Set GDRIVE_FOLDER_ID in your .env
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# ── path setup ────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from utils.env_loader import get

# ── config ────────────────────────────────────────────────────────────────────
SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/documents",
]
CREDENTIALS_FILE = ROOT / "config" / "gdrive_credentials.json"
RESEARCH_DIR = ROOT / "data" / "research"


def get_credentials():
    if not CREDENTIALS_FILE.exists():
        print(
            f"❌  Credentials not found at {CREDENTIALS_FILE}\n"
            "    Follow setup instructions at the top of this file."
        )
        sys.exit(1)
    creds = service_account.Credentials.from_service_account_file(
        str(CREDENTIALS_FILE), scopes=SCOPES
    )
    return creds


def find_latest_brief(company: str) -> Path:
    """Find the most recent markdown brief for this company in data/research/."""
    RESEARCH_DIR.mkdir(parents=True, exist_ok=True)
    slug = company.lower().replace(" ", "-")
    candidates = sorted(RESEARCH_DIR.glob(f"{slug}*.md"), reverse=True)
    if not candidates:
        # Fallback: look for any .md with the company name
        candidates = sorted(
            [f for f in RESEARCH_DIR.glob("*.md") if slug in f.stem.lower()],
            reverse=True,
        )
    if not candidates:
        print(
            f"❌  No research brief found for '{company}' in {RESEARCH_DIR}\n"
            "    Make sure the research output was saved as a .md file there first."
        )
        sys.exit(1)
    return candidates[0]


def markdown_to_gdoc_requests(markdown_text: str) -> list[dict]:
    """
    Convert markdown to a list of Google Docs API batchUpdate requests.
    Handles: headings (##, ###), bold (**text**), tables (basic),
    horizontal rules, and plain paragraphs.
    """
    requests = []
    index = 1  # Google Docs text insertion starts at index 1

    def insert_text(text: str, style: str = "NORMAL_TEXT") -> None:
        nonlocal index
        requests.append(
            {
                "insertText": {
                    "location": {"index": index},
                    "text": text,
                }
            }
        )
        end = index + len(text)

        heading_map = {
            "HEADING_1": 1,
            "HEADING_2": 2,
            "HEADING_3": 3,
            "HEADING_4": 4,
        }
        if style in heading_map:
            requests.append(
                {
                    "updateParagraphStyle": {
                        "range": {"startIndex": index, "endIndex": end},
                        "paragraphStyle": {"namedStyleType": style},
                        "fields": "namedStyleType",
                    }
                }
            )
        index = end

    lines = markdown_text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]

        # Skip empty lines (we'll insert a newline instead)
        if line.strip() == "":
            insert_text("\n")
            i += 1
            continue

        # Horizontal rule
        if line.strip() in ("---", "***", "___"):
            insert_text("\n")
            i += 1
            continue

        # Code blocks (skip formatting, insert as plain text)
        if line.strip().startswith("```"):
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                insert_text(lines[i] + "\n")
                i += 1
            i += 1  # skip closing ```
            continue

        # Headings
        if line.startswith("# "):
            insert_text(line[2:] + "\n", "HEADING_1")
        elif line.startswith("## "):
            insert_text(line[3:] + "\n", "HEADING_2")
        elif line.startswith("### "):
            insert_text(line[4:] + "\n", "HEADING_3")
        elif line.startswith("#### "):
            insert_text(line[5:] + "\n", "HEADING_4")

        # Table rows — convert to tab-separated plain text
        elif line.startswith("|"):
            cells = [c.strip() for c in line.split("|") if c.strip()]
            # Skip separator rows (e.g. |---|---|)
            if all(re.match(r"^[-:]+$", c) for c in cells):
                i += 1
                continue
            insert_text("\t".join(cells) + "\n")

        # Bullet points
        elif line.startswith("- ") or line.startswith("* "):
            insert_text("• " + line[2:] + "\n")

        # Bold markers — strip ** for now (full bold range requests are complex)
        else:
            clean = re.sub(r"\*\*(.*?)\*\*", r"\1", line)
            clean = re.sub(r"\*(.*?)\*", r"\1", clean)
            insert_text(clean + "\n")

        i += 1

    return requests


def create_gdoc(creds, company: str, markdown_text: str, folder_id: str) -> str:
    """Create a Google Doc from markdown and return its URL."""
    docs_service = build("docs", "v1", credentials=creds)
    drive_service = build("drive", "v3", credentials=creds)

    date_str = datetime.now().strftime("%Y-%m-%d")
    title = f"[Yuno Research] {company} — {date_str}"

    # 1. Create empty doc
    doc = docs_service.documents().create(body={"title": title}).execute()
    doc_id = doc["documentId"]

    # 2. Populate with content
    requests = markdown_to_gdoc_requests(markdown_text)
    if requests:
        docs_service.documents().batchUpdate(
            documentId=doc_id, body={"requests": requests}
        ).execute()

    # 3. Move to target folder
    file = drive_service.files().get(fileId=doc_id, fields="parents").execute()
    previous_parents = ",".join(file.get("parents", []))
    drive_service.files().update(
        fileId=doc_id,
        addParents=folder_id,
        removeParents=previous_parents,
        fields="id, parents",
    ).execute()

    # 4. Make accessible to anyone with the link (within Yuno domain ideally)
    drive_service.permissions().create(
        fileId=doc_id,
        body={
            "type": "anyone",   # Change to "domain" + "domain": "yuno.com" for domain-only
            "role": "reader",
        },
    ).execute()

    doc_url = f"https://docs.google.com/document/d/{doc_id}/edit"
    return doc_url


def save_brief_locally(company: str, content: str) -> Path:
    """Save the brief as a local .md file before uploading."""
    RESEARCH_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    slug = company.lower().replace(" ", "-")
    path = RESEARCH_DIR / f"{slug}-{date_str}.md"
    path.write_text(content, encoding="utf-8")
    return path


def main():
    parser = argparse.ArgumentParser(description="Save SDR research brief to Google Drive")
    parser.add_argument("--company", required=True, help="Company name researched")
    parser.add_argument(
        "--content",
        default=None,
        help="Markdown content to save. If omitted, reads latest file from data/research/",
    )
    args = parser.parse_args()

    folder_id = get("GDRIVE_RESEARCH_FOLDER_ID")

    # Get markdown content
    if args.content:
        md_path = save_brief_locally(args.company, args.content)
        markdown_text = args.content
        print(f"💾  Saved brief locally: {md_path}")
    else:
        md_path = find_latest_brief(args.company)
        markdown_text = md_path.read_text(encoding="utf-8")
        print(f"📄  Found brief: {md_path.name}")

    print(f"📤  Uploading to Google Drive folder...")
    creds = get_credentials()

    try:
        url = create_gdoc(creds, args.company, markdown_text, folder_id)
        print(f"\n✅  Research Brief created successfully!")
        print(f"🔗  {url}\n")
        print("    Share this link with the team — accessible to anyone with the URL.")
    except HttpError as e:
        print(f"❌  Google API error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
