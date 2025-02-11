---
tags:
 - Satori
 - MPI
 - RELION
 - Howto Recipes
---

# Installing and Using RELION

RELION (for REgularised LIkelihood OptimisatioN, pronounce rely-on) is a software package that employs an empirical Bayesian approach for electron cryo-microscopy (cryo-EM) structure determination. 

## RELION on Satori 

This recipe is for building and using RELION on x86 nodes on Satori. It is different from working on IBM power9 nodes on Satori.

!!! Note
    The x86 nodes are available to some labs only. 

### Install RELION

Go to your directory and download RELION,
```
cd /nobackup/users/$USER
git clone https://github.com/3dem/relion.git
```

Get an interactive session on x86 nodes of Satori,
```
srun -p sched_mit_mbathe -c 2 -t 60 --pty bash
```

Load modules for the GCC compiler and Openmpi implementation,  
```
module use /software/spack/share/spack/lmod/linux-rocky8-x86_64/Core
module load gcc/12.2.0-x86_64  
module load openmpi/4.1.4-pmi-cuda-ucx-x86_64 
```

> Note: These modules are installed for the x86 nodes only. 

Build RELION with CUDA and FFTW features,
```
cd ~
mkdir relion
cd relion
git checkout master 
cd ..
mkdir 4.0.1
cd 4.0.1
mkdir install
mkdir build
cd build

cmake -DCMAKE_INSTALL_PREFIX=/home/$USER/relion/4.0.1/install -DFORCE_OWN_FFTW=ON -DAMDFFTW=ON -DCUDA_ARCH=80 ../../relion
make
make install
```

It is all set for the installation.

### Use RELION

There is a nice Graphical User Interface (GUI) for RELION. To use the GUI, first log in Satori with x-forwardig support,
```
ssh -Y <user>@satori-login-002.mit.edu
```

Get an interactive session with GPU and x-forwarding support on x86 nodes of Satori,
```
srun --x11 -p sched_mit_mbathe --gres=gpu:1 -c 6 -t 60 --pty bash
```

Set up environment for compilers, mpi implementation, FFTw, and RELION,
```
module use /software/spack/share/spack/lmod/linux-rocky8-x86_64/Core
module load gcc/12.2.0-x86_64  
module load openmpi/4.1.4-pmi-cuda-ucx-x86_64 
module load fftw/3.3.10-x86_64
export LD_LIBRARY_PATH=/nfs/software001/home/software-r8-x86_64/spack-20230328/opt/spack/linux-rocky8-x86_64/gcc-12.2.0/fftw-3.3.10-qiaruimvw6zu2h4f5eolqom7tixem6vk/lib:$LD_LIBRARY_PATH
export RELION_HOME=/home/$USER/relion/4.0.1/install
export PATH=${RELION_HOME}/bin:$PATH
export LD_LIBRARY_PATH=${RELION_HOME}/lib:$LD_LIBRARY_PATH
```

then open the RELION GUI, 
```
relion &
```

Users can use GUI to edit files or submit jobs. Refer to details on [this page](https://hpc.nih.gov/apps/RELION/index.html). 

Alternatively, users can prepare a batch job script to submit jobs. 

Download RELION benchmarks for testing, 
```
cd ~/relion
wget ftp://ftp.mrc-lmb.cam.ac.uk/pub/scheres/relion_benchmark.tar.gz
```
then all benchmark files will be saved in a directory named `relion_benchmark`.

Here is an exmaple job script,
```
#!/bin/bash
#SBATCH --partition=sched_mit_mbathe
#SBATCH --time=12:00:00
#SBATCH --nodes=1
#SBATCH -n 20
#SBATCH --cpus-per-task=2
#SBATCH --mem=10000
#SBATCH --gres=gpu:4
#SBATCH --chdir='.'

module use /software/spack/share/spack/lmod/linux-rocky8-x86_64/Core
module load gcc/12.2.0-x86_64
module load openmpi/4.1.4-pmi-cuda-ucx-x86_64
export LD_LIBRARY_PATH=/nfs/software001/home/software-r8-x86_64/spack-20230328/opt/spack/linux-rocky8-x86_64/gcc-12.2.0/fftw-3.3.10-qiaruimvw6zu2h4f5eolqom7tixem6vk/lib:$LD_LIBRARY_PATH
export RELION_HOME="/home/$USER/relion/4.0.1/install"
export PATH=${RELION_HOME}/bin:$PATH
export LD_LIBRARY_PATH=${RELION_HOME}/lib:$LD_LIBRARY_PATH

cd ~/relion/relion_benchmark
mkdir output

mpirun -np 20 relion_refine_mpi \
  --i Particles/shiny_2sets.star \
  --o output \
  --ref emd_2660.map:mrc \
  --ini_high 60 \
  --pool 100 \
  --pad 2  \
  --ctf \
  --iter 25 \
  --tau2_fudge 4 \
  --particle_diameter 360 \
  --K 4 \
  --flatten_solvent \
  --zero_mask \
  --oversampling 1 \
  --healpix_order 2 \
  --offset_range 5 \
  --offset_step 2 \
  --sym C1 \
  --norm \
  --scale \
  --j 1   \
  --gpu "" \
 --dont_combine_weights_via_disc \
  --scratch_dir /tmp
```

Add the above lines in a file named `job.sh`, then submit the job,
```
sbatch job.sh
```
