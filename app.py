# streamlit ui for my rag demo
from pathlib import Path
import sys

# streamlit begins 
import streamlit as st

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.config import SAMPLE_DOCS, TOP_K, UPLOADS
from app.rag_pipeline import ask
from app.vectorstore import add_docs


st.set_page_config(page_title="Doc Q&A (RAG)", layout="wide")
st.title("Document Q&A using RAG")
st.write("Upload some docs, build the index, then ask questions based on those docs.")

with st.sidebar:
    st.subheader("Documents")
    files = st.file_uploader("Upload pdf/txt/md", type=["pdf", "txt", "md"], accept_multiple_files=True)
    include_samples = st.checkbox("Include sample docs from data folder", value=True)
    k = st.slider("How many chunks to retrieve", 1, 8, TOP_K)

    if st.button("Build / Update Index"):
        paths = []

        if files:
            for f in files:
                save_to = UPLOADS / f.name
                save_to.write_bytes(f.getbuffer())
                paths.append(save_to)

        if include_samples and SAMPLE_DOCS.exists():
            for p in SAMPLE_DOCS.iterdir():
                if p.suffix.lower() in [".pdf", ".txt", ".md"]:
                    paths.append(p)

        if not paths:
            st.warning("No files found. Upload something or keep sample docs checked.")
        else:
            try:
                with st.spinner("Creating embeddings, please wait..."):
                    n = add_docs(paths)
                st.success(f"Done. Saved {n} chunks from {len(paths)} files.")
            except Exception as e:
                st.error(str(e))

    st.markdown("---")
    st.write("Steps: split docs -> embeddings -> FAISS search -> LLM answer")

st.subheader("Ask something")
q = st.text_input("Question", placeholder="ex: leave policy for probation employees")

col1, col2 = st.columns([1, 4])
with col1:
    go = st.button("Ask")

if go:
    if not q.strip():
        st.warning("Type a question first")
    else:
        try:
            with st.spinner("Searching and generating answer..."):
                result = ask(q.strip(), k=k)

            st.markdown("### Answer")
            st.write(result["answer"])

            st.markdown("### Sources used")
            if not result["sources"]:
                st.write("No sources")
            else:
                for i, doc in enumerate(result["sources"], start=1):
                    name = doc.metadata.get("source", "unknown")
                    with st.expander(f"{i}. {name}"):
                        st.write(doc.page_content)
        except Exception as e:
            st.error(str(e))
