---
tags:
 - LLM
 - GPU
 - Howto Recipes
 - Engaging
---

# Running Your Own Retrieval-Augmented Generation (RAG) Model

RAG models harness the power of Large Language Models (LLMs) to query and
summarize a set of documents. Through RAG, one can combine the strengths of
retrieval-based and generative models to provide more accurate and contextually
relevant responses.

RAG also provides an interesting test case to make use of our resources on the
cluster. Here, we provide instructions on how to run a RAG model to query and
answer questions about [our ORCD documentation](https://orcd-docs.mit.edu/).

The code for developing this model can be found in this
[GitHub repository](https://github.com/mit-orcd/orcd-rag). Feel free to use
this repository as a guide to develop your own RAG model on separate
documents.

## Getting Started

### Working on a Compute Node

We require that you run this model on a compute node. You can request an
interactive session on a compute node with the following command:

```bash
salloc -N 1 -n 16 -p mit_normal --mem=48G
```

However, this works much more quickly with a GPU. If you have access to a
partition on Engaging with a GPU, then specify your partition as such:

```bash
salloc -N 1 -n 8 -p mit_normal_gpu --gres=gpu:l40s:1
```

I have specified an L40S GPU, which has 48GB of memory. You will need a GPU with
at least 40GB of memory for this model to work.

### Getting Access to HuggingFace

The LLMs used in this pipeline are from HuggingFace. By default, we use Llama
3.1, which is gated and requires users to request access. You can follow this
process for doing so:

1. [Create a HuggingFace account](https://huggingface.co/)
2. Request access to [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)
3. Create a [user access token](https://huggingface.co/settings/tokens)

    You will need to adjust the settings of your user access token so that you
    can download and run the model. To do so, navigate to your HuggingFace
    profile, then click "Edit Profile" > "Access Tokens" and edit the
    permissions for your access token:

    ![HF access token permissions](../images/RAG/hf_token_permissions.png)

    Edit your token permissions to match the following:

    ![HF token permission settings](../images/RAG/hf_token_permission_settings.png)

4. Export your access token as an environment variable on Engaging and add to
your `.bash_profile` so it can be saved for future uses:

    ```bash
    export HF_TOKEN="your_user_access_token"
    echo 'export HF_TOKEN="your_user_access_token"' >> ~/.bash_profile
    ```

    !!! note
        You will not be able to copy your HF token again from the HF website. If
        you do not save it somewhere, you will need to generate a new one every
        time you run this.

## Running the Model

### Running in a Container

You can run the RAG model on our documentation using the Apptainer image we have
saved to Engaging. We have the commands for doing so saved in a
[shell script](https://github.com/mit-orcd/orcd-rag/blob/main/container/run_container.sh).
To run the container, you can simply run the following:

```bash
sh /orcd/software/community/001/pkg/orcd-rag/container/run_container.sh
```

The first time you run this, the model will be downloaded from HuggingFace and
cached, so it may take a while to get running. Subsequent times will be much
quicker because the model has already been downloaded.

Llama 3.1 8B takes about 15GB of space. The default cache location for
HuggingFace models is `$HOME/.cache/huggingface`. If you do not have enough
space in your home directory to store the model, you can set the `HF_HOME`
environment variable to point to another directory. For example, to save models
to your scratch directory (depending on your storage setup), that would look
something like this:

```bash
export HF_HOME=/home/$USER/orcd/r8/scratch
```

or:

```bash
export HF_HOME=/nobackup1/$USER
```

### Running via a Python Environment

You can avoid the container route and run this using a Python environment. The
steps to do so can be found on the
[GitHub repository](https://github.com/mit-orcd/orcd-rag).

<!--
TODO:
- Include instructions for adding flags when that's ready
    - As part of this, include an option in the script to point to your own
    vector store
-->
