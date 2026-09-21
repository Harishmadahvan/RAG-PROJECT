# main RAG logic - search relevant text then ask llm
from langchain_openai import ChatOpenAI

from app.config import CHAT_MODEL, TOP_K, get_api_key
from app.vectorstore import search

SYSTEM_MSG = """Answer using only the context given below.
If context is not enough, say you don't know.
Keep the answer short. Mention file name if possible."""


def build_context(chunks):
    text = ""
    for i, c in enumerate(chunks, start=1):
        src = c.metadata.get("source", "unknown")
        text += f"[{i}] {src}\n{c.page_content}\n\n"
    return text.strip()


def ask(question, k=TOP_K):
    chunks = search(question, k)

    if not chunks:
        return {
            "answer": "No data in index yet. Please upload/ingest documents.",
            "sources": [],
        }

    context = build_context(chunks)
    prompt = f"{SYSTEM_MSG}\n\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"

    llm = ChatOpenAI(api_key=get_api_key(), model=CHAT_MODEL, temperature=0)
    out = llm.invoke(prompt)

    return {"answer": out.content, "sources": chunks}
