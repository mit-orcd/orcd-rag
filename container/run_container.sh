#!/bin/bash

module load apptainer

REPO_PATH=/orcd/datasets/001/orcd-rag

# Set HF_HOME if it is not set:
if [ -z "${HF_HOME}" ]; then
    export HF_HOME=$HOME/.cache/huggingface

apptainer exec --nv \
               --env HF_TOKEN=$HF_TOKEN \
               --env HF_HOME=/tmp/.cache/huggingface \
               --bind $HF_HOME:/tmp/.cache/huggingface \
               --bind $REPO_PATH:/tmp/orcd-rag \
               $REPO_PATH/container/rag_container.sif \
               python /tmp/orcd-rag/rag.py

# To do: Add option for flags
