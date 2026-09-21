# quick test without streamlit ui
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from app.config import SAMPLE_DOCS
from app.rag_pipeline import ask
from app.vectorstore import add_docs


def main():
    files = []
    for p in SAMPLE_DOCS.iterdir():
        if p.suffix.lower() in [".txt", ".md", ".pdf"]:
            files.append(p)

    print("adding", len(files), "files...")
    n = add_docs(files)
    print("chunks:", n)

    q = "How many WFH days can a probation employee take?"
    print("Q:", q)
    result = ask(q)
    print("A:", result["answer"])
    for i, d in enumerate(result["sources"], start=1):
        print(i, d.metadata.get("source"))


if __name__ == "__main__":
    main()
