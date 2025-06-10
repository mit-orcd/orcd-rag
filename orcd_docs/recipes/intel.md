---
tags:
 - Intel
 - Compiler
 - C
 - Fortran
 - Howto Recipes
---

# Intel compiler

Intel compiler is optimized for intel CPUs. It provides the Math Kernel Library (MKL) in which linear algebra computations are optimized. The performance of C and Fortran codes can be improved on Intel CPUs if compiled with Intel compiler. It provides an MPI implemetation for MPI programs that run on multipe nodes. Users should choose the Intel compiler for intel CPUs when possible. 


## Set up environment 

=== "Rocky 8 nodes" 

    If you use Rocky 8 nodes, log in to an appropriate head node first,
    ```
    ssh <user>@orcd-login003.mit.edu
    ```

    Load an intel module,
    ```
    module load intel/2024.2.1
    ```

    Check commands for intel compiler and MPI and environment variables for MKL are ready for use,
    ```
    $ which icx
    /orcd/software/community/001/rocky8/intel/2024.2.1/compiler/2024.2/bin/icx
    $ which ifort
    /orcd/software/community/001/rocky8/intel/2024.2.1/compiler/2024.2/bin/ifort
    $ which mpiicx
    /orcd/software/community/001/rocky8/intel/2024.2.1/mpi/2021.13/bin/mpiicx
    $ which mpiifort
    /orcd/software/community/001/rocky8/intel/2024.2.1/mpi/2021.13/bin/mpiifort
    $ echo $MKLROOT
    /orcd/software/community/001/rocky8/intel/2024.2.1/mkl/2024.2
    ```


=== "CentOS 7 nodes" 

    If you use CentOS 7 nodes, log in to an appropriate head node first,
    ```
    ssh <user>@orcd-vlogin003.mit.edu
    ```

    Load the modules for intel compiler, intel MPI and MKL,
    ```
    module load intel/2018-01
    module load impi/2018-01
    module load mkl/2018-01 
    ```

    Check commands for intel compiler and MPI and environment variables for MKL are ready for use,
    ```
    $ which icc
    /home/software/intel/2018-01/bin/icc
    $ which ifort
    /home/software/intel/2018-01/bin/ifort
    $ which mpiicc
    /home/software/intel/2018-01/compilers_and_libraries_2018.1.163/linux/mpi/intel64/bin/mpiicc
    $ which mpiifort
    /home/software/intel/2018-01/compilers_and_libraries_2018.1.163/linux/mpi/intel64/bin/mpiifort
    $ echo $MKLROOT
    /home/software/intel/2018-01/compilers_and_libraries_2018.1.163/linux/mkl/
    ```

## Compile and run programs with Intel compiler

=== "Rocky 8 nodes" 
    Once the environment is set up, you can compile your C or Fortran codes like this,
    ```
    icx -O3 name.c -o name
    ifort -O3 name.f90 -o name
    ```
    or MPI codes,
    ```
    mpiicx -O3 name.c -o name
    mpiifort -O3 name.f90 -o name
    ```

    If you use GNU Make to build your program, set up the varialbes in the Makefile, 
    ```
    CC=icx
    FC=ifort
    MPICC=mpiicx
    MPIFC=mpiifort
    ```
    Use the variable `MKLROOT` in the Makefile when needed.

    Finally submit a job script specifying a partition with `-p <partition-name>` and loading the intel module,
    ```
    module load intel/2024.2.1
    ``` 

=== "CentOS 7 nodes" 
    Once the environment is set up, you can compile your C or Fortran codes like this,
    ```
    icc -O3 name.c -o name
    ifort -O3 name.f90 -o name
    ```
    or MPI codes,
    ```
    mpiicc -O3 name.c -o name
    mpiifort -O3 name.f90 -o name
    ```

    If you use GNU Make to build your program, set up the varialbes in the Makefile, 
    ```
    CC=icc
    FC=ifort
    MPICC=mpiicc
    MPIFC=mpiifort
    ```
    Use the variable `MKLROOT` in the Makefile when needed.

    Finally submit a job script specifying a partition with `-p <partition-name>` and loading the intel module,
    ```
    module load intel/2018-01
    module load impi/2018-01
    module load mkl/2018-01 
    ``` 


## References

Refer to the following references for more details on logging in, compiling C/Fortran codes, using GNU make, and using partitions in Slurm job scheduler. 

> [Log in the system](https://orcd-docs.mit.edu/accessing-orcd/ssh-login/) . 

> [Compile C/Fortran Codes and Use GNU Make](https://orcd-docs.mit.edu/software/compile/). 

> [Use Slurm to submit jobs](https://orcd-docs.mit.edu/running-jobs/overview/). 
