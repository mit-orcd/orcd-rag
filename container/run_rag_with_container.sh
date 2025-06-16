#!/bin/bash

# Run a RAG session using a container.

# flags:
#   -h, --help            show this help message and exit
#   --temp TEMP           Model temperature (Default: 0.5)
#   --vector_store_path VECTOR_STORE_PATH
#                         Path to vector store (Default: /orcd-rag/orcd_docs_vector_store)
#   --llm LLM             LLM model name (Default: mistralai/Ministral-8B-Instruct-2410)
#   --queries QUERIES [QUERIES ...]
#                         Enter queries to run in a batch session

module load apptainer

# Read flags:
HELP=0
TEMP=""
VECTOR_STORE_PATH=""
LLM=""
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -h|--help) HELP=1; shift ;;
        --temp) TEMP="$2"; shift 2 ;;
        --vector_store_path) VECTOR_STORE_PATH="$2"; shift 2 ;;
        --llm) LLM="$2"; shift 2 ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
done
FLAGS=""
if [ $HELP -eq 1 ]; then
    FLAGS="$FLAGS -h"
fi
if [ -n "$TEMP" ]; then
    FLAGS="$FLAGS --temp $TEMP"
fi
if [ -n "$VECTOR_STORE_PATH" ]; then
    FLAGS="$FLAGS --vector_store_path $VECTOR_STORE_PATH"
fi
if [ -n "$LLM" ]; then
    FLAGS="$FLAGS --llm $LLM"
fi

# Get the path to the RAG directory:
WORKDIR=$(dirname "$(dirname "$(realpath "$0")")")

# Check for local image, use global otherwise:
if [ -f $WORKDIR/container/rag_container.sif ]; then
    SIF_PATH=$WORKDIR/container/rag_container.sif
else
    SIF_PATH="/orcd/software/community/001/container_images/orcd-rag/20250611/rag_container.sif"
fi
echo "Using image located at ${SIF_PATH}"

# Set HF_HOME if it is not set:
if [ -z "${HF_HOME}" ]; then
    export HF_HOME=$HOME/.cache/huggingface
fi
# Create HF_HOME directory if it does not exist:
mkdir -p $HF_HOME

# Warn if HF_TOKEN is not set
if [ -z "${HF_TOKEN}" ]; then
    echo "Warning: HF_TOKEN is not set. You may not be able to access private Hugging Face models." >&2
fi

export APPTAINER_BINDPATH="$HF_HOME:/tmp/.cache/huggingface,$WORKDIR:/orcd-rag,$VECTOR_STORE_PATH"

apptainer exec --nv \
               --env HF_TOKEN=$HF_TOKEN \
               --env HF_HOME=/tmp/.cache/huggingface \
               $SIF_PATH \
               /bin/bash -c "source activate /opt/conda/envs/orcd_rag && python /orcd-rag/rag.py $FLAGS"
