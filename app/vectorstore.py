# store and search embeddings using FAISS
from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

from app.config import EMBED_MODEL, INDEX_PATH, get_api_key
from app.ingest import load_files, make_chunks


def _embeddings():
    return OpenAIEmbeddings(api_key=get_api_key(), model=EMBED_MODEL)


def index_ready():
    return (INDEX_PATH / "index.faiss").exists() and (INDEX_PATH / "index.pkl").exists()


def open_index():
    if not index_ready():
        raise FileNotFoundError("Index not found. Please add documents first.")

    # allow_dangerous_deserialization is needed for local faiss load
    return FAISS.load_local(
        str(INDEX_PATH),
        _embeddings(),
        allow_dangerous_deserialization=True,
    )


def add_docs(file_paths):
    docs = load_files(file_paths)
    if len(docs) == 0:
        return 0

    chunks = make_chunks(docs)
    emb = _embeddings()

    if index_ready():
        db = open_index()
        db.add_documents(chunks)
    else:
        db = FAISS.from_documents(chunks, emb)

    INDEX_PATH.mkdir(parents=True, exist_ok=True)
    db.save_local(str(INDEX_PATH))
    return len(chunks)


def search(query, k):
    db = open_index()
    return db.similarity_search(query, k=k)
