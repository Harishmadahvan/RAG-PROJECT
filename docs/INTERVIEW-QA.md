# Interview Questions & Answers — Simple RAG Project

Use these to prepare for fresher / 1-year experience interviews.

---

### 1. What is RAG?
**A:** Retrieval-Augmented Generation. Before the LLM answers, we retrieve relevant document chunks from a knowledge base and pass them as context. This grounds answers in your data and reduces hallucination.

### 2. Why not just put the whole PDF in the prompt?
**A:** Token limits, cost, and noise. Large docs don’t fit well; retrieval sends only the most relevant parts.

### 3. What is an embedding?
**A:** A numeric vector representation of text. Texts with similar meaning have vectors that are close in distance (cosine similarity / L2).

### 4. What is FAISS / a vector index?
**A:** FAISS stores embedding vectors and finds nearest neighbors quickly. In this project, the index is saved locally under `faiss_index/`.

### 5. Explain your project architecture in 30 seconds.
**A:** Users upload docs → we chunk and embed them into FAISS → for each question we retrieve Top-K chunks → we build a prompt with that context → OpenAI generates an answer → UI shows answer and sources.

### 6. What is chunking and why overlap?
**A:** Splitting long text into smaller pieces. Overlap keeps context continuity so important sentences aren’t cut awkwardly between chunks.

### 7. How did you choose chunk size?
**A:** Started with 800 characters and 150 overlap — small enough for precise retrieval, large enough to keep useful context. Tunable via `.env`.

### 8. What is Top-K?
**A:** Number of most similar chunks retrieved for a question. Higher K = more context but more noise/cost. We default to 3.

### 9. Difference between keyword search and semantic search?
**A:** Keyword search matches exact words. Semantic search matches meaning (e.g., “vacation” can match “annual leave”) using embeddings.

### 10. How do you reduce hallucination in RAG?
**A:** Provide retrieved context, instruct the model to answer only from context, and say “I don’t know” when context is insufficient. Also show sources.

### 11. What happens if retrieval returns irrelevant chunks?
**A:** Answer quality drops. Fixes: better chunking, clearer docs, higher-quality embeddings, metadata filters, or re-ranking (future improvement).

### 12. Why LangChain?
**A:** It provides ready building blocks for loaders, splitters, vector stores, and prompts so we focus on the RAG flow instead of low-level plumbing.

### 13. Why FAISS instead of Pinecone?
**A:** FAISS is local/free and simple for demos. Pinecone is a managed cloud vector database better for multi-user production scale.

### 14. Why temperature = 0?
**A:** For factual Q&A we want deterministic, less creative answers grounded in documents.

### 15. What is the difference between embedding model and chat model?
**A:** Embedding model converts text to vectors for search. Chat/completion model generates natural language answers.

### 16. How is this different from fine-tuning?
**A:** Fine-tuning changes model weights with training data. RAG keeps the model as-is and supplies fresh external knowledge at query time. RAG is cheaper/faster to update (just re-ingest docs).

### 17. How would you evaluate your RAG system?
**A:** Manual checks on sample Q&A, faithfulness to sources, retrieval hit-rate, and later metrics like context precision/recall or RAGAS.

### 18. How would you scale this for production?
**A:** Swap Streamlit for FastAPI + proper frontend, use a managed vector DB, add auth, logging, caching, async ingestion, monitoring, and CI/CD.

### 19. Security concerns?
**A:** Keep API keys in `.env` (not Git), validate uploads, restrict document access by user/role, and avoid sending sensitive data to external APIs without policy approval.

### 20. What was the hardest part?
**A:** Good sample answer: “Getting chunking and Top-K right so answers were grounded. Too-large chunks retrieved noise; too-small chunks lost context.”

### 21. Walk me through one call in your code.
**A:** `similarity_search(query, k)` embeds the query and returns nearest document chunks from FAISS. Those chunks become `{context}` in the chat prompt.

### 22. What if two documents contradict each other?
**A:** Model may mix answers. Production systems add document versioning, effective dates, or source priority rules.

### 23. Can RAG work without OpenAI?
**A:** Yes — use local embeddings (e.g., sentence-transformers) and local LLMs (e.g., Ollama). We used OpenAI for quality and interview familiarity.

### 24. What is prompt engineering in this project?
**A:** Designing the system message and context template so the model follows rules: use context only, admit unknowns, cite sources.

### 25. Future improvements you would add?
**A:** Hybrid search (BM25 + vectors), re-ranking, conversation memory, citations with page numbers, evaluation dashboard, and deployment with Docker.

---

## Quick definitions cheat-sheet

| Term | One-line meaning |
|------|------------------|
| RAG | Retrieve docs, then generate answer |
| Embedding | Text → vector |
| Vector index / DB | Fast similarity search store |
| Chunk | Small piece of a document |
| Top-K | How many chunks to retrieve |
| Hallucination | Model invents facts not in data |
| Grounding | Forcing answers to use sources |
