# Building and Running the Container

This directory contains code for building a conatainer based on the Python
environment required to run this RAG program. Using a container is an alternate
route to running the program compared to creating a Python environment. The
container is built via Apptainer, which is optimized for HPC environments.

## Build the Container

```bash
sbatch build_container.sbatch
```

This script builds the container in the background and generates the
`rag_container.sif` file. This can take up to one hour to run. A GPU present
is required to build the container so that the Conda environment can be properly
built.

## Run RAG within the Container

Get an interactive session with a GPU on Engaging (replacing the partition and
GPU type as necessary):

```bash
salloc -N 1 -n 8 --mem-per-cpu=4G -p mit_normal_gpu -G l40s:1
```

Run RAG within the container:

```bash
sh run_rag_with_container.sh
```

This script runs the container based on the `.sif` file.

## Create a New Vector Store Using the Container

If you'd like to create a vector store based on another set of documents, you
can do so using the container. Currently, only `.md` or `.pdf` documents are
supported. For larger PDFs, you may need to split them into multiple smaller
PDFs to avoid hitting memory limits on the GPU when running the RAG pipeline.

```bash
sh create_vector_store_with_container.sh --docs_path <path to documents directory>
```
