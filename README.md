# Implementing a RAG Model on the ORCD Documentation

## Authors

- **Riya Tyagi** - [GitHub Profile](https://github.com/Centrattic)
- **Sam Corey** - [GitHub Profile](https://github.com/secorey)

## Setting Up

**Connect to Engaging:**

```bash
ssh $USER@orcd-login001.mit.edu
```

**Get access to Llama 3.1:**

The LLMs used in this pipeline are from HuggingFace. By default, we use Llama
3.1, which is gated and requires users to request access. You can follow this
process for doing so:

1. [Create a HuggingFace account](https://huggingface.co/)
2. Request access to [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)
3. Create a [user access token](https://huggingface.co/settings/tokens)
4. Save your user access token as an environment variable on Engaging:

```bash
export HF_TOKEN="your_user_access_token"
```

**Get an interactive session with a GPU on Engaging (replacing the partition and GPU type as necessary):**

```bash
salloc -N 1 -n 4 -p mit_normal_gpu --gres=gpu:l40s:1
```

*Note: You will need a GPU with at least 40GB of memory. If you don't have a GPU, you can run this on a CPU, but it will be much slower.*

**Create a Python virtual environment:**

For [creating the vector store](process_docs.py) and
[running the RAG model](rag.py):

```bash
module load miniforge
python -m venv venv_dev
source venv_dev/bin/activate
pip install -r requirements_dev.txt
```

For just [running the RAG model](rag.py) (if you are using the pre-created vector store on Engaging):

```bash
module load miniforge
python -m venv venv_user
source venv_user/bin/activate
pip install -r requirements_user.txt
```

## Creating the Vector Store

You can skip this section if you are using the ORCD documentation vector store
that is publicly available on Engaging.

```bash
python process_docs.py
```

## Running the RAG Model

This script takes two arguments:
1. Model temperature (default: 0.5)
2. Path to vector store (default: public ORCD docs)
3. LLM name (default: Meta Llama 3.1 8B)
<!-- Check the best model temperature -->

For running with default settings:

```bash
python rag.py
```

To run with customized settings:

```bash
python rag.py <temperature> </path/to/vector/store> <LLM name>
```

