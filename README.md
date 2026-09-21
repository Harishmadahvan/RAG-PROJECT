# Simple RAG Document Q&A System

A **fresher / 1-year experience friendly** Retrieval-Augmented Generation (RAG) project.  
Upload company documents → store embeddings in FAISS → ask questions → get answers grounded in your docs (with sources).

> Not an over-engineered agent platform. Focused on clear RAG fundamentals you can explain in interviews.

---

## Project Overview

This app turns static documents (handbook, FAQ, PDFs) into a searchable knowledge base:

1. **Ingest** documents (PDF / TXT / MD)
2. **Chunk** text with overlap
3. **Embed** chunks using OpenAI embeddings
4. **Store** vectors in local **FAISS** index
5. **Retrieve** Top-K relevant chunks for a question
6. **Generate** an answer with an LLM using only retrieved context
7. **Show sources** in a Streamlit UI

---

## Features

- Document upload (PDF, TXT, MD)
- Sample company handbook + product FAQ included
- Chunking + embedding + vector search
- Grounded Q&A with “I don’t know” fallback
- Source chunk viewer in UI
- Simple modular Python code (easy to explain)

---

## Technology Stack

| Layer | Choice | Why |
|-------|--------|-----|
| Language | Python 3.12+ | Standard for LLM/RAG tooling |
| UI | Streamlit | Fast demo UI |
| Orchestration | LangChain | Loaders, splitters, prompts |
| Embeddings | OpenAI `text-embedding-3-small` | Quality semantic search |
| LLM | OpenAI `gpt-4o-mini` | Affordable grounded answers |
| Vector search | FAISS | Local, free, fast similarity search |
| Config | python-dotenv | Keep API keys out of code |

Details: [`docs/TECH-STACK-WHY.md`](docs/TECH-STACK-WHY.md)

---

## Architecture & Flow

- Architecture diagram & components: [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
- Step-by-step ingest + query flow: [`docs/FLOW.md`](docs/FLOW.md)
- What & why for each tool: [`docs/TECH-STACK-WHY.md`](docs/TECH-STACK-WHY.md)
- Interview Q&A (25 questions): [`docs/INTERVIEW-QA.md`](docs/INTERVIEW-QA.md)

```text
Documents → Chunk → Embed → FAISS index
                              ↑
User Question → Retrieve Top-K → Prompt + LLM → Answer + Sources
```

---

## Folder Structure

```text
RAG/
├── app.py                 # Streamlit entrypoint
├── app/
│   ├── config.py          # env + paths
│   ├── ingest.py          # load + chunk
│   ├── vectorstore.py     # FAISS + embeddings
│   └── rag_pipeline.py    # retrieve + generate
├── data/
│   └── sample_docs/       # sample handbook + FAQ
├── docs/
│   ├── ARCHITECTURE.md
│   ├── FLOW.md
│   ├── TECH-STACK-WHY.md
│   └── INTERVIEW-QA.md
├── requirements.txt
├── .env.example
└── README.md
```

---

## Setup & Run

### Prerequisites
- Python **3.12+** (recommended)
- OpenAI API key

### 1) Create virtual environment

```bash
cd C:\Docu\Documents-P\Ha\Cursor-Project\RAG
py -3.12 -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Configure API key

```bash
copy .env.example .env
```

Edit `.env` and set:

```env
OPENAI_API_KEY=sk-your-real-key
```

### 3) Run the app

```bash
streamlit run app.py
```

Open the local URL shown in the terminal (usually `http://localhost:8501`).

### 4) Try it
1. Keep **“Also ingest bundled sample docs”** checked  
2. Click **Ingest Documents**  
3. Ask: `How many WFH days can probation employees take?`  
4. Check the retrieved source chunks under the answer.  

---

## Git commands

```bash
cd C:\Docu\Documents-P\Ha\Cursor-Project\RAG
git init
git add .
git commit -m "Initial commit: Simple RAG Document Q&A system"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git push -u origin main
```

---

## Interview tip (30-second pitch)

“I built a simple RAG system where documents are chunked and embedded into a FAISS index. When a user asks a question, I retrieve the most relevant chunks and pass them to an LLM with a strict prompt so answers stay grounded in the documents. The Streamlit UI also shows source chunks for transparency.”
