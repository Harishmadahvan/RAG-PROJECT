# settings / paths for the project
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

ROOT = Path(__file__).resolve().parent.parent

SAMPLE_DOCS = ROOT / "data" / "sample_docs"
UPLOADS = ROOT / "data" / "uploads"
INDEX_PATH = ROOT / "faiss_index"

# models - can change in .env if needed
API_KEY = os.getenv("OPENAI_API_KEY", "")
CHAT_MODEL = os.getenv("OPENAI_CHAT_MODEL", "gpt-4o-mini")
EMBED_MODEL = os.getenv("OPENAI_EMBED_MODEL", "text-embedding-3-small")

# these values worked okay for my sample docs
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "800"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "150"))
TOP_K = int(os.getenv("TOP_K", "3"))

UPLOADS.mkdir(parents=True, exist_ok=True)
INDEX_PATH.mkdir(parents=True, exist_ok=True)


def get_api_key():
    if not API_KEY or API_KEY.startswith("sk-your-"):
        raise ValueError("Add OPENAI_API_KEY in .env file first")
    return API_KEY
