# End-to-End Flow — Simple RAG System

## 1) Ingestion flow (build knowledge base)

```text
Upload PDF/TXT/MD
        │
        ▼
   Load document text
        │
        ▼
 Split into chunks
 (size=800, overlap=150)
        │
        ▼
 Create embedding vector
 for each chunk (OpenAI)
        │
        ▼
 Store vectors + text
 in FAISS index (local)
```

### Why chunking?
LLMs and embedding models have token limits. Small overlapping chunks improve retrieval precision and keep related sentences together.

### Why overlap?
Overlap (e.g., 150 chars) reduces the chance that an important sentence is cut between two chunks.

---

## 2) Query flow (answer a question)

```text
User question
     │
     ▼
Embed the question
     │
     ▼
Similarity search in FAISS
(Top-K nearest chunks)
     │
     ▼
Build prompt =
  system rules
  + retrieved context
  + user question
     │
     ▼
LLM generates answer
     │
     ▼
Show answer + source chunks in UI
```

### Why retrieve before generate?
Pure LLMs may invent facts. RAG first finds relevant company text, then asks the model to answer from that text only.

### Why show sources?
Interviewers like transparency. Sources prove the answer is grounded in documents.

---

## 3) Prompt policy used in this project

The system prompt tells the model to:

1. Use **only** provided context  
2. Say **“I don’t know…”** if context is insufficient  
3. Keep answers concise  
4. Mention source file names when useful  

This is a simple anti-hallucination pattern suitable for fresher projects.

---

## 4) Example walkthrough

**Question:** “How many WFH days can a probation employee take?”

1. Question is embedded.  
2. FAISS returns chunks from `employee_handbook.txt` about WFH.  
3. Prompt includes those chunks.  
4. LLM answers: probation employees get **1 WFH day per week**.  
5. UI shows the handbook chunk as source.

---

## 5) Failure cases to mention in interviews

| Case | What happens | What it teaches |
|------|----------------|-----------------|
| Empty vector index | App asks user to ingest docs | RAG needs a knowledge base |
| Irrelevant docs | Model says it doesn’t know | Retrieval quality matters |
| Too small Top-K | Missing context | Tune Top-K |
| Too large chunks | Noisy retrieval | Tune chunk size |
| Missing API key | Clear config error | Secrets via `.env` |
