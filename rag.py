"""
System arguments:
1. Model temperature (default: 0.5)
2. Path to vector store (default: public ORCD docs)
3. LLM name (default: Meta Llama 3.1 8B)
"""

from huggingface_hub import login
from langchain.chains import RetrievalQA
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline
from langchain.prompts import PromptTemplate
import os
import sys
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
VECTOR_STORE_PATH = os.path.join(BASE_PATH, "orcd_docs_vector_store")
# VECTOR_STORE_PATH = "/orcd/datasets/orcd_rag/orcd_docs_vector_store" # Will uncomment when we know the vector store path
VECTOR_STORE_COLLECTION_NAME = "ORCD_docs"
EMBEDDING_MODEL_NAME = "BAAI/bge-base-en-v1.5"
LLM_MODEL_NAME = "meta-llama/Llama-3.1-8B-Instruct"
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
    vector_store = Chroma(collection_name=VECTOR_STORE_COLLECTION_NAME,
                          persist_directory=VECTOR_STORE_PATH,
                          embedding_function=embeddings)
    
    # Set up retriever:
    retriever = vector_store.as_retriever(search_type="similarity",
                                          search_kwargs={"k": 3})

    # Set up LLM:
    tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL_NAME)
    terminators = [tokenizer.eos_token_id,
                tokenizer.convert_tokens_to_ids("<|eot_id|>")]
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
        eos_token_id=terminators,
        device=0 if torch.cuda.is_available() else -1
    )
    llm = HuggingFacePipeline(pipeline=text_generation_pipeline)

    return llm, retriever


def get_prompt_template():
    """
    Get the prompt template for the RAG system

    Returns:
        prompt: PromptTemplate
    """

    prompt_template = """
    <|start_header_id|>user<|end_header_id|>
    You are an assistant for answering questions using provided context. You are
    given the extracted parts of a long document and a question. Provide a
    conversational answer. If you don't know the answer, just say "I do not
    know." Don't make up an answer.
    Question: {question}
    Context: {context}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
    """
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


def run_conversation(qa_chain):
    while True:
        question = input("Prompt: ")
        if question.lower() == "quit" or question.lower() == "exit":
            break
        print(qa_chain.invoke(question)["result"])


def main():
    if "llama" in LLM_MODEL_NAME.lower():
        print("Built with Llama")

    # Read system arguments:
    try:
        MODEL_TEMPERATURE = float(sys.argv[1])
    except IndexError:
        MODEL_TEMPERATURE = MODEL_TEMPERATURE
    try:
        VECTOR_STORE_PATH = sys.argv[2]
    except IndexError:
        VECTOR_STORE_PATH = VECTOR_STORE_PATH
    try:
        LLM_MODEL_NAME = sys.argv[3]
    except IndexError:
        LLM_MODEL_NAME = LLM_MODEL_NAME

    # Login to Huggingface:
    access_token = os.getenv("HF_TOKEN")
    login(token=access_token)
    
    # Initialize components:
    llm, retriever = initialize_components()

    # Set up prompt:
    prompt = get_prompt_template()

    # Set up RAG chain:
    qa_chain = get_qa_chain(llm, retriever, prompt)

    # Run interactive chat session:
    run_conversation(qa_chain)

    return


if __name__ == "__main__":
    main()
