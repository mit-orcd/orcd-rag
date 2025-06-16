#!/bin/bash

# Create a vector store from documents in a specified directory using a container.

# flags:
#   -h, --help            show this help message and exit
#   --docs_path DOCS_PATH
#                         Path to directory containing the documents to be added to the vector store
#   --embedding_model EMBEDDING_MODEL
#                         Name of the embedding model to use (Default: BAAI/bge-base-en-v1.5)

module load apptainer

# Read flags:
HELP=0
DOCS_PATH=""
EMBEDDING_MODEL=""
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -h|--help) HELP=1; shift ;;
        --docs_path) DOCS_PATH="$2"; shift 2 ;;
        --embedding_model) EMBEDDING_MODEL="$2"; shift 2 ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
done
FLAGS=""
if [ $HELP -eq 1 ]; then
    FLAGS="$FLAGS -h"
fi
if [ -n "$DOCS_PATH" ]; then
    FLAGS="$FLAGS --docs_path $DOCS_PATH"
fi
if [ -n "$EMBEDDING_MODEL" ]; then
    FLAGS="$FLAGS --embedding_model $EMBEDDING_MODEL"
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

# Warn if HF_TOKEN is not set:
if [ -z "${HF_TOKEN}" ]; then
    echo "Warning: HF_TOKEN is not set. You may not be able to access private Hugging Face models." >&2
fi

# Set Apptainer bind mounts:
export APPTAINER_BINDPATH="$HF_HOME:/tmp/.cache/huggingface,$WORKDIR:/orcd-rag,$DOCS_PATH"

apptainer exec --nv \
               --env HF_TOKEN=$HF_TOKEN \
               --env HF_HOME=/tmp/.cache/huggingface \
               $SIF_PATH \
               /bin/bash -c "source activate /opt/conda/envs/orcd_rag && python /orcd-rag/create_vectorstore.py $FLAGS"
