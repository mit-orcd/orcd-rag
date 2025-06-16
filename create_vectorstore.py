"""
Given .md or .pdf files, create a Chroma vectorstore.
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


def load_documents(docs_path):
    """
    Load documents from the specified directory recursively. Documents must be
    in .md or .pdf format.
    """
    # Load the documents recursively:
    documents = []
    for file_name in os.listdir(docs_path):
        file_path = os.path.join(docs_path, file_name)
        if file_name.endswith(".md"):
            loader = UnstructuredMarkdownLoader(file_path)
            documents.extend(loader.load())
        elif file_name.endswith('.pdf'):
            loader = UnstructuredPDFLoader(file_path)
            documents.extend(loader.load())
        elif os.path.isdir(file_path):
            documents.extend(load_documents(file_path))
    return documents


def main(docs_path):
    docs_dir = os.path.basename(docs_path)
    vector_store_dir = f"{docs_dir}_vector_store"
    # Set the embeddings model:
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    documents = load_documents(docs_path)
    Chroma.from_documents(documents=documents,
                          embedding=embeddings,
                          persist_directory=os.path.join(WORKDIR,
                                                         vector_store_dir))
    
    return


if __name__ == "__main__":
    # Read system arguments:
    parser = argparse.ArgumentParser()
    parser.add_argument("--docs_path",
                        type=str,
                        required=True,
                        help=("Path to directory containing the documents to "
                              "be added to the vector store"))
    parser.add_argument("--embedding_model",
                        type=str,
                        default=EMBEDDING_MODEL_NAME,
                        help=("Name of the embedding model to use "
                             f"(Default: {EMBEDDING_MODEL_NAME})"))
    args = parser.parse_args()
    EMBEDDING_MODEL_NAME = args.embedding_model
    docs_path = args.docs_path
    assert os.path.exists(docs_path), f"Path {docs_path} does not exist."
    
    main(docs_path)
