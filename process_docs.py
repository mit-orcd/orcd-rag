"""
Given the ORCD .md files, create a Chroma vectorstore.
"""

import os
from huggingface_hub import login
from langchain_chroma import Chroma
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_huggingface import HuggingFaceEmbeddings

access_token = os.getenv("HF_TOKEN")
login(token=access_token)

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
DOCS_PATH = os.path.join(BASE_PATH, "orcd_docs")
VECTOR_STORE_PATH = os.path.join(BASE_PATH, "orcd_docs_vector_store")
EMBEDDING_MODEL_NAME = "BAAI/bge-base-en-v1.5"

# Set the embeddings model:
embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

# Load the .md documents (not recursively):
documents = []
for filename in os.listdir(DOCS_PATH):
    if filename.endswith('.md'):
        file_path = os.path.join(DOCS_PATH, filename)
        loader = UnstructuredMarkdownLoader(file_path)
        documents.extend(loader.load())

vectorstore = Chroma.from_documents(collection_name="ORCD_docs",
                                    documents=documents,
                                    embedding=embeddings,
                                    persist_directory=VECTOR_STORE_PATH)
