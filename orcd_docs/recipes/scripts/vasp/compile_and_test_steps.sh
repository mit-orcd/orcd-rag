# -8<-- [start:extract]
tar -xzvf vasp.6.4.3.tgz
# -8<-- [end:extract]

# -8<-- [start:cd]
cd vasp.6.4.3
# -8<-- [end:cd]

# -8<-- [start:makefile]
cp arch/makefile.include.gnu_omp makefile.include
# -8<-- [end:makefile]

# -8<-- [start:module]
module load gcc/12.2.0
module load openmpi/4.1.4
module load netlib-lapack/3.10.1
module load netlib-scalapack/2.2.0
module load fftw/3.3.10
module load openblas/0.3.26
# -8<-- [end:module]

# -8<-- [start:env-var]
SCALAPACK_ROOT=`module -t show  netlib-scalapack 2>&1 | grep CMAKE_PREFIX_PATH | awk -F, '{print $2}'  | awk -F\" '{print $2}'`
FFTW_ROOT=`pkgconf --variable=prefix fftw3`
OPENBLAS_ROOT=$(dirname `pkgconf --variable=libdir openblas`)
# -8<-- [end:env-var]

# -8<-- [start:make]
make -j OPENBLAS_ROOT=$OPENBLAS_ROOT FFTW_ROOT=$FFTW_ROOT SCALAPACK_ROOT=$SCALAPACK_ROOT MODS=1 DEPS=1
# -8<-- [end:make]

# -8<-- [start:test]
export LD_LIBRARY_PATH=${OPENBLAS_ROOT}/lib:${FFTW_ROOT}/lib:${SCALAPACK_ROOT}/lib
bin/vasp_std
# -8<-- [end:test]