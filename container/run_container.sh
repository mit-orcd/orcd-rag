#!/bin/bash

module load apptainer

# Get the path to the RAG directory:
REPO_PATH=$(dirname "$(dirname "$(realpath "$0")")")

# Set HF_HOME if it is not set:
if [ -z "${HF_HOME}" ]; then
    export HF_HOME=$HOME/.cache/huggingface
fi

# Create HF_HOME directory if it does not exist:
mkdir -p $HF_HOME

apptainer exec --nv \
               --env HF_TOKEN=$HF_TOKEN \
               --env HF_HOME=/tmp/.cache/huggingface \
               --bind $HF_HOME:/tmp/.cache/huggingface \
               --bind $REPO_PATH:/tmp/orcd-rag \
               $REPO_PATH/container/rag_container.sif \
               python /tmp/orcd-rag/rag.py

