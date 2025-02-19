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
`rag_container.sif` file. This can take up to one hour to run.

## Run the Container

Get an interactive session with a GPU on Engaging (replacing the partition and
GPU type as necessary):

```bash
salloc -N 1 -n 4 -p mit_normal_gpu --gres=gpu:l40s:1
```

Run the container:

```bash
sh run_container.sh
```

This script runs the container based on the `.sif` file.
