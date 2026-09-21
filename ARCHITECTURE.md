# Architecture — Simple RAG Document Q&A

## High-level architecture

```text
┌──────────────────┐     ┌────────────────────┐     ┌────────────────────┐
│  Documents       │     │  Ingestion Layer   │     │  Vector Index       │
│  (PDF / TXT/MD)  │────►│  Load → Chunk →    │────►│  FAISS (local)      │
│                  │     │  Embed             │     │  saved on disk      │
└──────────────────┘     └────────────────────┘     └─────────┬──────────┘
                                                              │
                                                              │ similarity search
                                                              ▼
┌──────────────────┐     ┌────────────────────┐     ┌────────────────────┐
│  Streamlit UI    │────►│  RAG Orchestrator  │◄────│  Retrieved Chunks  │
│  (ask question)  │     │  Prompt + Context  │     │  (Top-K)           │
└──────────────────┘     └─────────┬──────────┘     └────────────────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │  LLM (OpenAI)      │
                         │  Final Answer      │
                         └────────────────────┘
```

## Components

| Component | Responsibility |
|-----------|----------------|
| **Streamlit UI (`app.py`)** | Upload docs, trigger ingest, ask questions, show sources |
| **Ingest (`app/ingest.py`)** | Load files and split into overlapping chunks |
| **Vector store (`app/vectorstore.py`)** | Create embeddings and store/search with FAISS |
| **RAG pipeline (`app/rag_pipeline.py`)** | Retrieve Top-K chunks, build prompt, call LLM |
| **Config (`app/config.py`)** | Paths, models, chunk size, Top-K from `.env` |

## Why this architecture (fresher-friendly)

- **Separation of concerns:** ingest, retrieve, and generate are separate modules — easy to explain in interviews.
- **Local vector index:** FAISS runs on your machine; no cloud vector-DB account needed for demos.
- **Grounded answers:** LLM only sees retrieved context, reducing hallucination for handbook/FAQ questions.
- **Visible sources:** UI shows which chunks were used — strong interview talking point.

## Data flow summary

1. **Offline / Ingest path:** Document → chunks → embeddings → FAISS index on disk  
2. **Online / Query path:** Question → embed question → Top-K similar chunks → LLM prompt → answer + sources  

## Design choices kept simple on purpose

- No authentication
- No multi-user session store
- No agent/tool calling
- No re-ranking model
- No production orchestration (Kafka, Airflow, etc.)

These can be listed as “future improvements” in interviews.
