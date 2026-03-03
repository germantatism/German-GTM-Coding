"""Shared env loader. Import this at the top of every script."""
import os
from pathlib import Path
from dotenv import load_dotenv

# Walk up from this file to find .env
ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")


def get(key: str, required: bool = True) -> str:
    val = os.getenv(key)
    if required and not val:
        raise EnvironmentError(f"Missing required env var: {key}")
    return val or ""
