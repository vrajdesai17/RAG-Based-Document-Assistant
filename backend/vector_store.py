import os
from sentence_transformers import SentenceTransformer
from chromadb import PersistentClient
from chromadb.config import Settings
from chromadb.utils import embedding_functions

CHROMA_DIR = os.path.abspath("vector_db")
COLLECTION_NAME = "rag_chunks"

embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
client = PersistentClient(path="/mount/tmp/chroma_db", settings=Settings(anonymized_telemetry=False))
## Use a safe path for Streamlit Cloud
# Tells Chroma to use DuckDB (a lightweight SQL engine) + Parquet (a fast file format) to store vector data.
collection = client.get_or_create_collection(name=COLLECTION_NAME, embedding_function=embedding_fn)

def add_chunks_to_db(chunks, source_id="doc1"):
    ids = [f"{source_id}_{i}" for i in range(len(chunks))]
    # Creates a unique ID for each chunk like: "doc1_0", "doc1_1", "doc1_2"
    metadatas = [{"source": source_id}] * len(chunks)
    collection.add(documents=chunks, ids=ids, metadatas=metadatas)
    print(f"✅ Stored {len(chunks)} chunks in ChromaDB")
    
def query_chunks(query, n_results=3):
    results = collection.query(query_texts=[query], n_results=n_results)
    # Converts the query to a vector using your embedding function, results contains matched documents, metadata, IDs, and similarity scores.
    documents = results['documents'][0]  
    return documents