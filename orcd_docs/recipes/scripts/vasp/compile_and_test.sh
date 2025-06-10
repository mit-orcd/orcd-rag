#!/bin/bash
#SBATCH --time=2:00:00
#SBATCH --partition=mit_normal
#SBATCH -c 8

tar -xzvf vasp.6.4.3.tgz
cd vasp.6.4.3
cp arch/makefile.include.gnu_omp makefile.include

module load gcc/12.2.0
module load openmpi/4.1.4
module load netlib-lapack/3.10.1
module load netlib-scalapack/2.2.0
module load fftw/3.3.10
module load openblas/0.3.26

SCALAPACK_ROOT=`module -t show  netlib-scalapack 2>&1 | grep CMAKE_PREFIX_PATH | awk -F, '{print $2}'  | awk -F\" '{print $2}'`
FFTW_ROOT=`pkgconf --variable=prefix fftw3`
OPENBLAS_ROOT=$(dirname `pkgconf --variable=libdir openblas`)

make -j OPENBLAS_ROOT=$OPENBLAS_ROOT FFTW_ROOT=$FFTW_ROOT SCALAPACK_ROOT=$SCALAPACK_ROOT MODS=1 DEPS=1

export LD_LIBRARY_PATH=${OPENBLAS_ROOT}/lib:${FFTW_ROOT}/lib:${SCALAPACK_ROOT}/lib

srun ./bin/vasp_std