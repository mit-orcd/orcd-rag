#!/bin/bash

module load apptainer

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

apptainer exec --nv \
               --env HF_TOKEN=$HF_TOKEN \
               --env HF_HOME=/tmp/.cache/huggingface \
               --bind $HF_HOME:/tmp/.cache/huggingface \
               --bind $WORKDIR:/tmp/orcd-rag \
               $SIF_PATH \
               python /tmp/orcd-rag/rag.py $1 $2 $3 $4 $5 $6 $7 $8
