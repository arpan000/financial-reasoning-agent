from langchain_community.document_loaders import PyPDFLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

import os

DOCUMENTS_PATH = "rag/documents"

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents = []

for file in os.listdir(DOCUMENTS_PATH):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(DOCUMENTS_PATH, file)

        print(f"Loading: {file}")

        loader = PyPDFLoader(pdf_path)

        documents.extend(loader.load())

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

print(f"Total Chunks Created: {len(docs)}")

vector_db = Chroma.from_documents(
    docs,
    embedding_model,
    persist_directory="rag/vector_store"
)

vector_db.persist()

print("Embeddings created successfully!")