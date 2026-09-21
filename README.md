# Document Q&A using RAG

This project is a simple Document Question-Answering system built with **Retrieval-Augmented Generation (RAG)**.

Users can upload documents (PDF / TXT / MD). The text is split into chunks, converted into embeddings, and stored in a FAISS index. When a question is asked, the system finds the most relevant chunks and sends them to an LLM, so the answer is based on the uploaded documents instead of random model knowledge. The Streamlit UI also shows the source chunks used for the answer.

---

## Flow Diagram

### 1) Document ingest flow

```text
Upload PDF / TXT / MD
        |
        v
   Load document text
        |
        v
 Split into chunks (with overlap)
        |
        v
 Create embeddings (OpenAI)
        |
        v
 Store in FAISS index (local)
```

### 2) Question answering flow

```text
User question
     |
     v
Embed the question
     |
     v
Search similar chunks in FAISS (Top-K)
     |
     v
Build prompt = context + question
     |
     v
LLM generates answer
     |
     v
Show answer + source chunks in UI
```

### End-to-end view

```text
Documents --> Chunk --> Embed --> FAISS Index
                                       ^
                                       |
User Question --> Retrieve Top-K ------+
                                       |
                                       v
                         Prompt + LLM --> Answer + Sources
```

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python |
| UI | Streamlit |
| Framework | LangChain |
| Embeddings | OpenAI (`text-embedding-3-small`) |
| LLM | OpenAI (`gpt-4o-mini`) |
| Vector search | FAISS |
| Config | python-dotenv |
