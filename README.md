# Implementing a RAG Model on the ORCD Documentation

<!-- TODO:
- Change to DeepSeek
- Python script:
    - Deal with the "Setting `pad_token_id` to `eos_token_id`:128009 for open-end generation." message-->

## Authors

- **Riya Tyagi** - [GitHub Profile](https://github.com/Centrattic)
- **Sam Corey** - [GitHub Profile](https://github.com/secorey)

## Setting Up

**Connect to Engaging:**

```bash
ssh $USER@orcd-login001.mit.edu
```

**Get access to the LLM on HuggingFace:**

The LLMs used in this pipeline are from HuggingFace. By default, we use a model
from Mistral, which is gated and requires users to request access. You can
follow this process for doing so:

1. [Create a HuggingFace account](https://huggingface.co/)
2. Request access to [mistralai/Ministral-8B-Instruct-2410](https://huggingface.co/mistralai/Ministral-8B-Instruct-2410)
3. Create a [user access token](https://huggingface.co/settings/tokens)

    You will need to adjust the settings of your user access token so that you
    can download and run the model. To do so, navigate to your HuggingFace
    profile, then click "Edit Profile" > "Access Tokens" and edit the
    permissions for your access token such that all the boxes under "Inference"
    are checked.

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

**Get an interactive session with a GPU on Engaging (replacing the partition and GPU type as necessary):**

```bash
salloc -N 1 -n 8 -p mit_normal_gpu -G l40s:1
```

*Note: For the 8B model, you will need a GPU with at least 40GB of memory. If you don't have a GPU, you can run this on a CPU, but it will be much slower.*

**Create a Python virtual environment:**

For [creating the vector store](create_vectorstore.py) and
[running the RAG model](rag.py):

```bash
module load miniforge
python -m venv venv_rag
source venv_rag/bin/activate
pip install -r requirements_dev.txt
```

## Creating the Vector Store

You can skip this part if you are using the ORCD documentation vector store that
is publicly available on Engaging.

Currently you are able to create a vector store from `.pdf` or `.md` files, or
a mixture of both.

```bash
python create_vectorstore.py --docs_dir <documents directory>
```

For example:

```bash
python create_vectorstore.py --docs_dir orcd_docs
```

This will create a new directory containing your vector store:
`<dir name>_vector_store` (e.g. `orcd_docs_vector_store`)

You can edit the path to your new vector store using the `--vector_store_path`
flag when you run `rag.py`.

## Running the RAG Model

For running with default settings:

```bash
python rag.py
```

The first time you run this, the model will be downloaded from HuggingFace and
cached, so it may take a while to get running. Subsequent times will be much
quicker because the model has already been downloaded.

The 8B model takes about 15GB of space. The default cache location for
HuggingFace models is `$HOME/.cache/huggingface`. If you do not have enough space
in your home directory to store the model, you can set the `HF_HOME` environment
variable to point to another diectory. For example, to save models to your
scratch directory (depending on your storage setup), that would look something
like this:

```bash
export HF_HOME=/home/$USER/orcd/scratch
```

or:

```bash
export HF_HOME=/nobackup1/$USER
```

### Adding Optional Flags

This script takes flags so that you can change the model temperature, vector
store, or LLM being used. Run `python rag.py --help` to see flag information.
