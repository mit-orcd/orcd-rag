---
tags:
 - Engaging
 - OpenMind
 - Apptainer
 - Singularity
 - Software
---

# Singularity and Apptainer

Containers provide an isolated environment that supports user applications. In many cases, it is helpful to use a container to obtain the right environment for your applications on HPC clusters, so as to avoid installing too many dependencies.

Containers have great portability and mobility, that says, it is convenient to migrate your applications bewtween different platforms, such as laptops/desktops, cloud platforms and HPC clusters. 

The most well known container is Docker, which is designed for laptops/desktops and cloud platforms. On ORCD clusters, we use Apptainer and Singularity instead, which are particularly designed for high-perfromance computing. Apptainer is extended from Singularity. Both are compatible with Docker. 

!!! note 
    In the following, the terminology Singularity will be used in most cases. The statements hold if the terminologies Singularity and Apptainer are switched. 

Users can use Singularity to support many applications, such as Python, R, C/Fortran packages, and many GUI software. In particular, containers are popular in supporting Python pakcages for the artificial intelligence (AI) and data science communities, such as Pytorch, Tensorflow, and many others. The Ubuntu operating system (OS) is widely used in the AI community and it is convinient to install many AI appications in Ubuntu environment. Users can use Singularity to obtain Ubuntu OS other than Rocky 8 OS on the host cluster.

In this document, we will focus on how to use Singularity on ORCD clusters. First, many applications are well-supported in existing Docker images. Search for an image on the internet, in which your target applicaiton has already been installed by some developers, then download the image and use it directly. If there is no suitable image for your target application, you can build an image to support it.

!!! note 
    An image is a file to support container. Users can launch a containter based on an image.


## Run applications with Singularity

Let us start with running an application with Singularity on the cluster first. 

### Preparations

=== "Engaging"

     Log in to a head node,
     ```
     ssh <user>@orcd-login002.mit.edu
     ```
     Check available Apptainer versions in modules,
     ```
     module av apptainer
     ```
     Load an Apptainer module and its dependency, for example, 
     ```
     module load apptainer/1.1.9
     ```

=== "OpenMind"

     Log in to the head node,
     ```
     ssh <user>@openmind7.mit.edu
     ```
     As a certain amount of computing resources are required to run Singularity, always start with getting an  interactive session on a compute node,
     ```
     srun -t 60 --constraint=rocky8 -c 4 --mem=10G --pty bash
     ```
     The `constraint=rocky8` is to request a node with the Rocky 8 OS. 
    
     Check available Apptainer versions in modules,
     ```
     module av openmind8/apptainer
     ```
     Load an Apptainer module, for example, 
     ```
     module load openmind8/apptainer/1.1.7
     ```

!!! note 
    Apptainer modules support both apptainer and singularity commands.

### Download an image

Search for an image that provides your target application, for exmaple on [Docker Hub](https://hub.docker.com/). Here is an example for downloading a Docker image to support Pytorch,
```
singularity pull my-image.sif docker://bitnami/pytorch:latest
```
The `my-image.sif` is the name of the image. You can name it as you like. 

!!! note 
    In Apptainer, the command `singularity` is a soft link to an executable named `apptainer`, so all `singularity` commands on this page can be replaced by the `apptainer` command. They work the same. 


### Run a program interactively

When the image is ready, launch a container based on the image and then run your application in the container. If you want to work interactively to test and debug codes, it is convineient to log in the containe shell, for exmaple, 
```
$ singularity shell my-image.sif 
Apptainer> python
Python 3.11.9 (main, May 13 2024, 16:49:42) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> # Run your programs here.
```

Alternatively, execute a command in the container to run your programs, 
```
singularity exec my-image.sif python my-code.py
```

Use the full path to the image file if it is not in the current directory. 

The `python` here is installed in the container and has nothing to do with the `python` or `anaconda` modules that have been installed on the host. As the python environment in the container provides all pacakges you need, you don't need to install any python packages and their dependecies. Now you can see the advantage of using a conatainer. 

### Submit a batch job

When the tests are completed, you can submit a batch job to run your program in the background. Here is a typical batch job script (e.g. named `job.sh`).

=== "Engaging"
     
     ```
     #!/bin/bash                      
     #SBATCH -t 01:30:00                  # walltime = 1 hours and 30 minutes
     #SBATCH -N 1                         # one node
     #SBATCH -n 2                         # two CPU cores
     #SBATCH -p mit_normal     # a partition with Rocky 8 nodes
     
     module load apptainer/1.1.9   # load modules
     singularity exec my-image.sif python my-code.py   # Run the program 
     ```

=== "OpenMind"

     ```
     #!/bin/bash                      
     #SBATCH -t 01:30:00                  # walltime = 1 hours and 30 minutes
     #SBATCH -N 1                         # one node
     #SBATCH -n 2                         # two CPU cores
     #SBATCH --constraint=rocky8          # nodes with Rocky 8 OS
     
     module load openmind8/apptainer/1.1.7      # load an apptainer module
     singularity exec my-image.sif python my-code.py   # Run the program 
     ```

The last line is a command to run a Python program uisng Singularity.  

Submit the job script using `sbatch`,
```
sbatch job.sh
```

### More on using Singularity

In many cases, GPUs are needed to accelerate programs. As the GPU driver is installed on the host, use the flag `--nv` to pass necessary GPU driver libraries into the container, so that the program can "see" the GPUs in the container. 

Check if GPUs are available in a container,
```
singularity exec --nv my-image.sif nvidia-smi
```

Here is an exmaple to run Python programs on GPUs.
```
singularity exec --nv my-image.sif python my-code.py  
```

By default, the home directory and the `/tmp` directory are bound to the container. If your programs read/write data files in other directories (e.g. `/path/to/data`), bind them to the container using the flag `-B`,
```
singularity exec -B /path/to/data my-image.sif python my-code.py  
```

In summary, a commonly used syntax to run a program with Singularity is the following,
```
singularity exec [--nv] [-B <path-to-data>] <image-name> <executable-name> [source-code-name]
```
The terms in `<>` are must-needed, while the terms in `[]` are optional, depending on use cases. 

=== "Engaging"

     Here is an example job script to run a python program with a GPU and data files saved in `/nobakcup1` or `/pool001` directories,
     ```
     #!/bin/bash                      
     #SBATCH -t 01:30:00         # walltime = 1 hours and 30 minutes
     #SBATCH -N 1                # one node
     #SBATCH -n 2                # two CPU cores
     #SBATCH --gres=gpu:1        # one GPU
     #SBATCH -p sched_mit_psfc_gpu_r8     # a partition with Rocky 8 nodes

     module load apptainer/1.1.9   # load modules
     singularity exec --nv -B /nobakcup1,/pool001 my-image.sif python my-code.py   # Run the program
     ```

=== "OpenMind"

     Here is an example job script to run a Python program with a GPU and data files saved in `/om` or `/om2` directories,
     ```
     #!/bin/bash                      
     #SBATCH -t 01:30:00             # walltime = 1 hours and 30 minutes
     #SBATCH -N 1                    # one node
     #SBATCH -n 2                    # two CPU cores
     #SBATCH --gres=gpu:1            # one GPU
     #SBATCH --constraint=rocky8     # nodes with Rocky 8 OS

     module load openmind8/apptainer/1.1.7        # load an apptainer module
     singularity exec --nv -B /om,om2 my-image.sif python my-code.py  # Run the program
     ```

## Build Singularity images

In the previous section, it is assumed that all needed packages have been installed in the image. Users need to build a new image if some needed packages do not exist in the image. 

To save work for the building process, search for an image providing the right OS and necessary dependencies to support your target application, then use it as a base image and build your target application on top of it. 

The following is an example of building Python packages such as Pytorch and Pandas in a container image. 

First, download a Docker image that provides the Ubuntu OS and has Python and PyTorch installed already,
```
singularity build --sandbox my-image  docker://bitnami/pytorch:latest
```

The command `build` here does not build anything yet, but just downloads the image and converts it to a new format. The flag `--sandbox` tells `build` to convert the image to the Sandbox format, which is convenient for installing packages interactively. 

Now you can install additional packages in the base image. In many installation processes, it requires virtual root privilege, which is enabled by the `fakeroot` command here. 

=== "Engaging"
     Log in a head node that provides the `fakeroot` command,
     ```
     ssh <user>@orcd-login004.mit.edu
     ```

=== "OpenMind"

     Get an interative session on node115 that provides the `fakeroot` command,
     ```
     srun -t 120 -w node115 --pty bash
     ```

Start a container shell with the flags `--writable --fakeroot `, which enables the write permission and virtual root privileges in the container, and then you can install your packages. Here is an exmaple, 
```
$ singularity shell --writable --fakeroot my-image
Apptainer> apt-get update
Apptainer> pip install pandas
Apptainer> python 
Python 3.8.17 (default, Jun 16 2023, 21:48:21) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> import pandas as pd
```

Here the `apt-get` is to install system software on an Ubuntu machine, which is supported by the `fakeroot` flag. The `pip install` is to build Python packages. Finally, the package Pandas is built in the base image with PyTorch. 

Alternatively, you can build a Docker image on a laptop/desktop such as MAC or PC, transfer it to the cluster, and run it with Singularity. Many packages have been developed and built in the Docker environment, so this approach is more convenient in many cases. 

