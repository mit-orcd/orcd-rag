#!/bin/bash

#SBATCH -N 1
#SBATCH -n 4
#SBATCH -G l40s:1
#SBATCH -p mit_normal_gpu
#SBATCH -o build_container.out

module load apptainer

apptainer build --nv rag_container.sif rag_container.def
