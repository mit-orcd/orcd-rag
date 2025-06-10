"""
Flags:
--temp: Model temperature (default: 0.5)
--vector_store_path: Path to vector store (default: public ORCD docs)
--llm: LLM model name (default: Meta Llama 3.1 8B)
--queries: Queries to run in a batch session
"""

import argparse
from huggingface_hub import login
from langchain.chains import RetrievalQA
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline
from langchain.prompts import PromptTemplate
import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
VECTOR_STORE_PATH = os.path.join(BASE_PATH, "orcd-docs-edit_vector_store")
EMBEDDING_MODEL_NAME = "BAAI/bge-base-en-v1.5"
LLM_MODEL_NAME = "mistralai/Ministral-8B-Instruct-2410"
MODEL_TEMPERATURE = 0.5


def initialize_components():
    """
    Initialize the components for the RAG system

    Returns:
        llm: HuggingFacePipeline
        retriever: Chroma retriever
    """

    # Set the embeddings model:
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

    # Set the vector_store:
    vector_store = Chroma(persist_directory=VECTOR_STORE_PATH,
                          embedding_function=embeddings)
    
    # Set up retriever:
    retriever = vector_store.as_retriever(search_type="similarity",
                                          search_kwargs={"k": 3})

    # Set up LLM:
    tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL_NAME)

    model = AutoModelForCausalLM.from_pretrained(LLM_MODEL_NAME)
    text_generation_pipeline = pipeline(
        model=model,
        tokenizer=tokenizer,
        task="text-generation",
        temperature=MODEL_TEMPERATURE,
        do_sample=True,
        repetition_penalty=1.1,
        return_full_text=False,
        max_new_tokens=300,
        eos_token_id=tokenizer.eos_token_id,
        device=0 if torch.cuda.is_available() else -1
    )
    llm = HuggingFacePipeline(pipeline=text_generation_pipeline)

    return llm, retriever, tokenizer


def get_prompt_template(tokenizer):
    """
    Get the prompt template for the RAG system

    Returns:
        prompt: PromptTemplate
    """

    # Determine headers based on LLM:
    if "llama" in LLM_MODEL_NAME.lower():
        headers = {"start": "<|start_header_id|>user<|end_header_id|>",
                   "end": "<|start_header_id|>assistant<|end_header_id|>"}
    elif "mistral" in LLM_MODEL_NAME.lower():
        headers = {"start": "[INST]",
                   "end": "[/INST]"}
    else:
        raise ValueError("Unsupported LLM model name. Please use a Llama or Mistral model.")
    
    prompt_background = """
    You are an assistant for answering questions using provided context. You are
    given the extracted parts of a long document and a question. Provide a
    conversational answer. If the context is not relevant to the question being
    asked, do not use it, and tell the user that there may not be information
    in the documentation relevant to their query. Keep your answers concise.
    """

    prompt_template = f"""
    {headers['start']}
    {prompt_background}
    Question: {{question}}
    Context: {{context}}
    {tokenizer.eos_token}{headers['end']}"""

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=prompt_template
    )

    return prompt


def get_qa_chain(llm, retriever, prompt):
    """
    Set up the RAG chain

    Args:
        llm: HuggingFacePipeline
        retriever: Chroma retriever
        prompt: PromptTemplate
    
    Returns:
        qa_chain: RetrievalQA
    """
    qa_chain = RetrievalQA.from_chain_type(llm,
                                           retriever=retriever,
                                           chain_type_kwargs={"prompt": prompt})
    return qa_chain


def run_batch(qa_chain, queries):
    """
    Run a batch of queries

    Inputs:
        qa_chain: RetrievalQA
        queries: list of queries
    """

    for question in queries:
        print(f"Prompt: {question}")
        print(qa_chain.invoke(question)["result"])

    return


def run_interactive(qa_chain):
    """
    Answer questions in a loop

    Inputs:
        qa_chain: RetrievalQA
    """
    
    print("\nHello! I am a conversational AI assistant. You can ask me questions",
          "about the provided documents. Type 'quit' or 'exit' to end the",
          "conversation.")
    
    while True:
        question = input("Prompt: ")
        if question.lower() == "quit" or question.lower() == "exit":
            print("Goodbye!")
            break
        print("\n", qa_chain.invoke(question)["result"])

    return


def main(queries):
    if "llama" in LLM_MODEL_NAME.lower():
        print("Built with Llama")

    # Login to Huggingface:
    login(token=os.getenv("HF_TOKEN"))
    # Initialize components:
    llm, retriever, tokenizer = initialize_components()
    # Set up prompt:
    prompt = get_prompt_template(tokenizer)
    # Set up RAG chain:
    qa_chain = get_qa_chain(llm, retriever, prompt)
    if queries:
        # Use pre-defined queries:
        run_batch(qa_chain, queries)
    else:
        # Run interactive chat session:
        run_interactive(qa_chain)

    return


if __name__ == "__main__":
    # Read system arguments:
    parser = argparse.ArgumentParser()
    parser.add_argument("--temp",
                        type=float,
                        default=MODEL_TEMPERATURE,
                        help="Model temperature " + \
                             f"(Default: {MODEL_TEMPERATURE})")
    parser.add_argument("--vector_store_path",
                        type=str,
                        default=VECTOR_STORE_PATH,
                        help="Path to vector store " + \
                             f"(Default: {VECTOR_STORE_PATH})")
    parser.add_argument("--llm",
                        type=str,
                        default=LLM_MODEL_NAME,
                        help="LLM model name " + \
                             f"(Default: {LLM_MODEL_NAME})")
    parser.add_argument("--queries",
                        type=str,
                        nargs="+",
                        default=None,
                        help="Enter queries to run in a batch session")
    args = parser.parse_args()
    MODEL_TEMPERATURE = args.temp
    VECTOR_STORE_PATH = args.vector_store_path
    LLM_MODEL_NAME = args.llm
    queries = args.queries

    # Copy vector store to user's home directory:
    new_vector_store_path = os.path.join(os.getenv("HOME"), ".cache",
                                         "orcd_rag", "vector_stores")
    os.system(f"mkdir -p {new_vector_store_path}")
    os.system(f"cp -r {VECTOR_STORE_PATH} {new_vector_store_path}")
    VECTOR_STORE_PATH = os.path.join(new_vector_store_path,
                                     os.path.basename(VECTOR_STORE_PATH))

    main(queries)
