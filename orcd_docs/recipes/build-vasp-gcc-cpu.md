---
tags:
 - Engaging
 - Howto Recipes
 - MPI
 - VASP
 - Rocky Linux
---

# Example Build of the VASP Software

## About VASP

[VASP](https://www.vasp.at) is a first principles simulation tool for electronic structure and quantum mechanical molecular dynamics computations. The name VASP is an acronym of Vienna Ab-initio Simulation Package. The VASP software is used in quantum chemistry to simulate the properties and structure of atomic scale materials. VASP can compute
detailed atomic structure of molecules, finding terms such as bond lengths and vibration frequencies.

## Building VASP software

VASP is distributed as Fortran source code that must be compiled by end-users to create an executable program. This recipe describes how to compile
VASP using the GNU compiler stack. The recipe shows commands for a Rocky Linux system.

!!! note "Prerequisites"

    * To use VASP a research group must obtain a license from the VASP team as described here [here](https://www.vasp.at/sign_in/registration_form/).
    * This example assumes you are working with a Rocky Linux environment.

### 1. Extract VASP source code files

Once a licensed copy of VASP has been obtained the source code files must be extracted from the tar file that can be
downloaded by license holders from the [VASP portal site](https://www.vasp.at/sign_in/portal/). The command

```bash
--8<-- "docs/recipes/scripts/vasp/compile_and_test_steps.sh:extract"
```

will extract the source files and their directory tree. This command should be executed in a sub-directory where you will store the compiled VASP programs. 

Once the code has been extracted, switch to use the VASP directory for the remaining steps

```bash
--8<-- "docs/recipes/scripts/vasp/compile_and_test_steps.sh:cd"
```

??? tip

     For different versions of VASP, the download file name and directory name will be different. In that case, remember to adjust the example commands above accordingly.

### 2. Configure the compiler options file

The VASP software is distributed with multiple example compiler options files. 
These are in the sub-directory `arch/`. 
For this example we will use the GNU compiler options file `makefile.include.gnu_omp`. 
To activate the chosen options, copy the options file into the top-level VASP directory.

```bash
--8<-- "docs/recipes/scripts/vasp/compile_and_test_steps.sh:makefile"
```

### 3. Activate the relevant modules

To build the VASP program from the licensed source code several tools and libraries are needed. 
The modules below add the needed software. 
The `gcc` and `openmpi` modules provide compilers (gcc) and computational tools (openmpi) 
needed for parallel computing with VASP. 
The `lapack`, `scalapack`, `fftw` and `openblas` toos are numerical libraries that VASP uses.

```bash
--8<-- "docs/recipes/scripts/vasp/compile_and_test_steps.sh:module"
```

### 4. Set environment variables that are needed for compilation

The compilation scripts that come with VASP include variables that must be set to the cluster's local values. Here we set environment variables to hold those settings.

```bash
--8<-- "docs/recipes/scripts/vasp/compile_and_test_steps.sh:env-var"
```

### 5. Compile the VASP code

To compile the VASP code use the `make` program, passing it the environment variable settings as shown. The settings shown will also build the Fortran 90 modules that VASP includes.

```bash
--8<-- "docs/recipes/scripts/vasp/compile_and_test_steps.sh:make"
```

### 6. Check the VASP executables

The above commands should generate VASP executable programs `bin/vasp_std`, `bin/vasp_gam` and `bin/vasp_ncl`. To test that these programs can execute the following commands can be used:

```bash
--8<-- "docs/recipes/scripts/vasp/compile_and_test_steps.sh:test"
```

If the code has compiled successfully the follow output should be generated. This output shows that the 
VASP program can be run. The output shows an error because no input files have been configured.

```
 -----------------------------------------------------------------------------
|                                                                             |
|     EEEEEEE  RRRRRR   RRRRRR   OOOOOOO  RRRRRR      ###     ###     ###     |
|     E        R     R  R     R  O     O  R     R     ###     ###     ###     |
|     E        R     R  R     R  O     O  R     R     ###     ###     ###     |
|     EEEEE    RRRRRR   RRRRRR   O     O  RRRRRR       #       #       #      |
|     E        R   R    R   R    O     O  R   R                               |
|     E        R    R   R    R   O     O  R    R      ###     ###     ###     |
|     EEEEEEE  R     R  R     R  OOOOOOO  R     R     ###     ###     ###     |
|                                                                             |
|     No INCAR found, STOPPING                                                |
|                                                                             |
|       ---->  I REFUSE TO CONTINUE WITH THIS SICK JOB ... BYE!!! <----       |
|                                                                             |
 -----------------------------------------------------------------------------

 -----------------------------------------------------------------------------
|                                                                             |
|     EEEEEEE  RRRRRR   RRRRRR   OOOOOOO  RRRRRR      ###     ###     ###     |
|     E        R     R  R     R  O     O  R     R     ###     ###     ###     |
|     E        R     R  R     R  O     O  R     R     ###     ###     ###     |
|     EEEEE    RRRRRR   RRRRRR   O     O  RRRRRR       #       #       #      |
|     E        R   R    R   R    O     O  R   R                               |
|     E        R    R   R    R   O     O  R    R      ###     ###     ###     |
|     EEEEEEE  R     R  R     R  OOOOOOO  R     R     ###     ###     ###     |
|                                                                             |
|     No INCAR found, STOPPING                                                |
|                                                                             |
|       ---->  I REFUSE TO CONTINUE WITH THIS SICK JOB ... BYE!!! <----       |
|                                                                             |
 -----------------------------------------------------------------------------

STOP 1
```

### 7. Example scripts to compile and test

The commands above can be combined into scripts as shown below. This example
scripts that can either be run from the command line or submitted to Slurm 
as a batch job.

The following script shows compiling VASP and testing that the build completed successfully. Place and run this script from the directory where you put the VASP source .tgz file.

The call to `vasp_std` is expected to produce an error as in [6. Check the VASP executables](#6-check-the-vasp-executables) above. To run a full VASP experiment problem specific inputs and parameters must be added to the script for running (see [Running VASP]() below).

```bash title='compile_and_test.sh'
--8<-- "docs/recipes/scripts/vasp/compile_and_test.sh"
```

## Creating a VASP Module

It can be convenient to create a module for VASP since it does have several dependencies. Below is an example modulefile. This modulefile assumes you have installed VASP 6.4.3, placed it in `$HOME/software/VASP`, and used the same dependency modules to build VASP as described in [Step 3 above](#3-activate-the-relevant-modules). If you have installed a different version of VASP, placed it in a different location, or used different dependency modules you will need to adjust the modulefile accordingly.

```lua title='$HOME/software/modulefiles/vasp/6.4.3.lua'
--8<-- "docs/recipes/scripts/vasp/modulefile.lua"
```

## Running VASP

To run VASP create a job script like the one below in the same directory as your input files. You may need to increase `ntasks` or `cpus-per-task` or allocation additional resources depending on the size of the problem. This script assumes you have [created a module](#creating-a-vasp-module) and placed the modulefile in in `$HOME/software/modulefiles`. Update the location of your VASP module as needed. VASP has a [page of examples](https://www.vasp.at/wiki/index.php/Category:Examples) in their documentation that can be used for testing.

```bash title='run_vasp.sh'
--8<-- "docs/recipes/scripts/vasp/run_vasp.sh"
```

!!! note
    During testing we found that VASP has a tendency to create a very large number of threads that can slow down the calculations and cause them to hang. To prevent that we've set the `$OMP_NUM_THREADS` environment variable to the number of `cpus-per-task` requested (`$SLURM_CPUS_PER_TASK`).