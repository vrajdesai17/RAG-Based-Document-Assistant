# 🧠 RAG-based Domain-Specific Q&A System

This is a lightweight Retrieval-Augmented Generation (RAG) app that lets users upload a PDF document and ask questions about its content. It's designed for **domain-specific question answering** using OpenAI's LLMs and ChromaDB for local vector search.

---

## 🚀 Features

- Upload any PDF (e.g. academic papers, contracts, manuals)
- Ask natural language questions about the document
- Uses `SentenceTransformer` embeddings and OpenAI's `gpt-3.5-turbo` for answers
- Built with `Streamlit` for quick and interactive UI
- Chunking with overlap to preserve semantic context
- Stores and queries vector representations locally via ChromaDB

---

## 📦 Dependencies

pip install -r requirements.txt

## Project Structure

rag_qa_product/
│
├── app/
│   └── main.py                 # Streamlit app entry point
│
├── backend/
│   ├── processor.py            # Extracts and chunks PDF text
│   ├── vector_store.py         # Handles vector DB logic
│   └── llm.py                  # Interacts with OpenAI's LLM
│
├── data/                       # Local sample PDFs
├── vector_db/                 # Local ChromaDB storage
├── requirements.txt           # Python dependencies
├── .env                       # Your OpenAI key (not committed)
└── .gitignore

## Running Locally

1. Clone and enter the repo
git clone https://github.com/your-username/RAG-Based-Domain-Specific-Q-A-System.git
cd RAG-Based-Domain-Specific-Q-A-System

2. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4.Set up .env file
OPENAI_API_KEY=your-openai-api-key-here

5.Run the app
streamlit run app/main.py

## 🧾 Example Questions for a research paper

Once you upload a PDF, try asking:
- "What is the main contribution of this paper?"
- "Which algorithm is used?"
- "What are the limitations discussed?"
- "Explain the methodology"
- "List the datasets used"

## 💡 Notes
- Chunk size and overlap can be tweaked in processor.py
- Embedding model can be changed in vector_store.py
- Local vector DB (ChromaDB) is reset on reruns unless persisted in vector_db/

## 📬 Contact
Feel free to reach out if you want to deploy or scale this further.
Name: Vraj Desai
Email: vrajdhar@usc.edu
Contact: +1 2136915656
