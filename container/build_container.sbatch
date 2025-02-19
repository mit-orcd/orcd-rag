#!/bin/bash

#SBATCH -N 1
#SBATCH -n 4
#SBATCH -p mit_normal
#SBATCH -o build_container.out

module load apptainer

apptainer build rag_container.sif rag_container.def
