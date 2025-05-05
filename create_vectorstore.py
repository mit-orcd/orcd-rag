"""
Given .md or .pdf files, create a Chroma vectorstore.

Flags:
--docs_dir: Name of directory containing the documents to be added to the
vector store. This directory must be in the same directory as this script.
"""

import os
import argparse
from huggingface_hub import login
from langchain_chroma import Chroma
from langchain_community.document_loaders import UnstructuredMarkdownLoader, UnstructuredPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings

access_token = os.getenv("HF_TOKEN")
login(token=access_token)

WORKDIR = os.path.dirname(os.path.abspath(__file__))
EMBEDDING_MODEL_NAME = "BAAI/bge-base-en-v1.5"

def main(docs_dir, vector_store_dir):
    # Set the embeddings model:
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

    # Load the .md documents (not recursively):
    documents = []
    for filename in os.listdir(os.path.join(WORKDIR, docs_dir)):
        if filename.endswith('.md'):
            file_path = os.path.join(WORKDIR, docs_dir, filename)
            loader = UnstructuredMarkdownLoader(file_path)
            documents.extend(loader.load())
        elif filename.endswith('.pdf'):
            file_path = os.path.join(WORKDIR, docs_dir, filename)
            loader = UnstructuredPDFLoader(file_path)
            documents.extend(loader.load())

    Chroma.from_documents(documents=documents,
                          embedding=embeddings,
                          persist_directory=os.path.join(WORKDIR,
                                                         vector_store_dir))
    
    return

if __name__ == "__main__":
    # Read system arguments:
    parser = argparse.ArgumentParser()
    parser.add_argument("--docs_dir",
                        type=str,
                        required=True,
                        help="Name of directory containing the documents to" + \
                             "be added to the vector store. This directory" + \
                             "must be in the same directory as this script.")
    parser.add_argument("--embedding_model",
                        type=str,
                        default=EMBEDDING_MODEL_NAME,
                        help=f"Name of the embedding model to use" + \
                             "(Default: {EMBEDDING_MODEL_NAME}).")
    args = parser.parse_args()
    docs_dir = args.docs_dir
    EMBEDDING_MODEL_NAME = args.embedding_model
    vector_store_dir = f"{docs_dir}_vector_store"
    
    main(docs_dir, vector_store_dir)
