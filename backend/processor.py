import fitz  # Imports the fitz module from the PyMuPDF library — used to open and read PDFs easily in Python.

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text
    # It combines all the text from both pages into one string.

def chunk_text(text, chunk_size=300, overlap=50): #each chunk will overlap by 50 words with the previous one (to preserve context).
    """Split text into overlapping chunks."""
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def process_pdf_to_chunks(pdf_path):
    """Pipeline: PDF → text → chunks."""
    text = extract_text_from_pdf(pdf_path)
    chunks = chunk_text(text)
    return chunks
