#!/bin/bash
#SBATCH --time=2:00:00
#SBATCH --partition=mit_normal
#SBATCH --ntasks=4 # Number of VASP processes
#SBATCH --cpus-per=task=2 # Number of threads per VASP process

# Limit the number of threads to the number of cpus requested
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

# Load the VASP module
module use $HOME/software/modulefiles
module load vasp/6.4.3

# Run VASP
srun vasp_std