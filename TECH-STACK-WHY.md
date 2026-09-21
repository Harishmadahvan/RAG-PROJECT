# Technology Stack — What & Why

This document explains every major choice in the project in plain interview language.

---

## 1. Python
**What:** Main programming language.  
**Why:** Most RAG/LLM tooling (LangChain, FAISS, OpenAI SDK) is Python-first. Easy for fresher demos and notebooks.

---

## 2. Streamlit
**What:** Simple web UI framework for Python.  
**Why:** Fastest way to build a demo UI (upload + chat) without React/Angular complexity. Great for portfolio demos.

---

## 3. LangChain
**What:** Framework for LLM apps (loaders, splitters, prompts, model wrappers).  
**Why:** Industry-standard keyword in interviews. Reduces boilerplate for document loading, chunking, and prompt templates.

---

## 4. OpenAI Embeddings (`text-embedding-3-small`)
**What:** Converts text chunks into numeric vectors.  
**Why:** High-quality semantic search; similar meaning texts end up close in vector space (e.g., “leave policy” ≈ “annual vacation days”).

---

## 5. OpenAI Chat Model (`gpt-4o-mini`)
**What:** Large Language Model that writes the final answer.  
**Why:** Affordable, strong instruction-following. Good for answering from retrieved context. Temperature is set to `0` for more factual answers.

---

## 6. FAISS (Facebook AI Similarity Search)
**What:** Local vector similarity search library (index saved under `faiss_index/`).  
**Why:** Free, fast nearest-neighbor search, works well for demos on a laptop. No separate DB server. Easy to explain: “I store embedding vectors and find the closest ones to the question vector.”

> Interview note: FAISS is a **vector index/library**. Managed products like Pinecone/Weaviate are full vector **databases** with APIs, multi-tenancy, and cloud hosting. You can say you started with FAISS and could migrate later.

---

## 7. RecursiveCharacterTextSplitter
**What:** Splits long documents into overlapping chunks.  
**Why:** Better retrieval than sending whole files. Recursive splitter tries paragraph/sentence boundaries before cutting mid-word.

---

## 8. PyPDF / Text loaders
**What:** Read PDF and TXT/MD content into Document objects.  
**Why:** Real enterprise knowledge often lives in PDFs and text FAQs.

---

## 9. python-dotenv
**What:** Loads secrets from `.env`.  
**Why:** Keeps API keys out of source code / GitHub.

---

## What we intentionally did NOT use (and why)

| Skipped | Reason |
|---------|--------|
| Auth / login | Keep project simple |
| Agents / tools | Extra complexity for fresher scope |
| Pinecone / Weaviate | Cloud setup overhead |
| Fine-tuning | Costly and unnecessary for FAQ Q&A |
| FastAPI + Angular | Overkill for a focused RAG demo |

You can say in interviews:  
“I kept the first version simple and productionizable later by swapping FAISS for Pinecone and Streamlit for a full web stack.”

---

## Mapping to resume skills

- Retrieval-Augmented Generation (RAG)
- LangChain
- Vector Search (FAISS)
- OpenAI Embeddings & LLMs
- Prompt Engineering
- Document Chunking & Semantic Search
- Streamlit
- Python
