# load files and break them into smaller chunks
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import CHUNK_OVERLAP, CHUNK_SIZE

ALLOWED = [".pdf", ".txt", ".md"]


def load_files(file_list):
    docs = []

    for f in file_list:
        ext = f.suffix.lower()
        if ext not in ALLOWED:
            continue

        # pdf needs different loader
        if ext == ".pdf":
            loader = PyPDFLoader(str(f))
        else:
            loader = TextLoader(str(f), encoding="utf-8")

        loaded = loader.load()
        for d in loaded:
            d.metadata["source"] = f.name
        docs.extend(loaded)

    return docs


def make_chunks(docs):
    # overlapping chunks so text at boundaries is not lost
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    return splitter.split_documents(docs)
