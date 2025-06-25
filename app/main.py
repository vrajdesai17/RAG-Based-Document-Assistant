import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
import os
from backend.processor import process_pdf_to_chunks
from backend.vector_store import add_chunks_to_db, query_chunks
from backend.llm import get_answer_from_openai


st.set_page_config(page_title="📚 RAG Q&A Assistant", layout="wide")

st.title("📚 RAG-Based Document Assistant")

uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])
if uploaded_file:
    file_path = os.path.join("data", uploaded_file.name)
    # Creates a path like "data/contract.pdf" to save the uploaded file in a data/ folder.
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer()) 
        # This saves the uploaded PDF locally.

    with st.spinner("Processing document..."):
        chunks = process_pdf_to_chunks(file_path) # Pipeline: PDF → text → chunks.
        add_chunks_to_db(chunks, source_id=uploaded_file.name)
        st.success(f"✅ Processed and stored {len(chunks)} chunks.")

    # Ask a question
    query = st.text_input("Ask a question about the document:")
    if query:
        with st.spinner("Searching and generating answer..."):
            top_chunks = query_chunks(query, n_results=3)
            answer = get_answer_from_openai(top_chunks, query)
            
            st.markdown("### 🧠 Answer")
            st.success(answer)
            
            with st.expander("🔍 Context used"):
                for i, chunk in enumerate(top_chunks, 1):
                    st.markdown(f"**Chunk {i}:** {chunk}")