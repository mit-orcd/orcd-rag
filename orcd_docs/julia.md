---
tags:
 - Software
 - Julia
 - vscode
 - Engaging
 - SuperCloud
---

# Julia

Julia is a high-level, high-performance programming language designed for
technical and numerical computing, known for its speed and ease of use. Because
of its popularity, we have pre-installed versions of Julia on each of our
clusters. You can begin using Julia right away by running `module load julia`
or by specifying the module specifically:

=== "Engaging"

    On Rocky8 nodes:

    ```bash
    module load julia/1.10.1
    ```

    On Centos7 nodes:

    ```bash
    module load julia/1.8.5
    ```
    
=== "Satori"

    ```bash
    module load julia/1.5.3-rls2opu
    ```

=== "SuperCloud"

    ```bash
    module load julia/1.10.1
    ```

## Installing Packages

Julia organizes packages by the version of Julia you're running. When you
install packages, a `.julia` folder automatically gets created in your home
directory that holds all package installations. Julia will automatically create
an environment for that version, which will be saved in `~/.julia/environments`.

You can change the default package install location by setting the
`$JULIA_DEPOT_PATH` environment variable from the command line before you start
Julia. For example:

```bash
export JULIA_DEPOT_PATH=/home/$USER/orcd/r8/pool
```

## Juliaup

Juliaup provides a convenient way to manage different versions of Julia and
different package installations. It can be installed by running the following
command:

```bash
curl -fsSL https://install.julialang.org | sh
```

You will be asked if you want to proceed with default settings or to customize
your installation. We recommend customizing your installation. The default
settings are as follows:

1. Save the `.juliaup` folder to your home directory. This folder contains all
installations of Julia and their associated packages that are managed by
Juliaup.

    - On Satori, home directories are limited to 20 GB, so you may want to
    change this location to `/nobackup/users/$USER`.

2. Edit your `.bashrc` and `.bash_profile` files to automatically add the
Juliaup-managed version of Julia to your `$PATH` environment variable.

    - We generally discourage editing your `.bashrc` file because it can cause
    issues when trying to use other software. For example, if you want to use a
    pre-installed Julia module, you would have to manually remove Juliaup from
    your `$PATH` any time you connect to the cluster.

    - To add Juliaup to your `$PATH` manually, run:
    ```bash
    export PATH=/path/to/.juliaup/bin${PATH:+:${PATH}}
    ```

Click [here](https://github.com/JuliaLang/juliaup) for more information on
installing and using Juliaup.

!!!Note
    Currently, Juliaup is not compatible with Satori or SuperCloud.

## Using Different Julia Versions

### Juliaup Versions

If you're using [Juliaup](#juliaup), installing different versions of Julia is
straightforward:

```bash
# Install Julia 1.9.0:
juliaup add 1.9.0
# Use Julia 1.9.0:
julia +1.9.0
```

Note that Juliaup installs versions and packages to your `.julia` folder.

### Manual Installation

If you are unable to use Juliaup and you need a version of Julia that is not
pre-installed on the cluster, you can manually download it.

A complete list of previous Julia versions can be found
[here](https://julialang.org/downloads/oldreleases/). From this site, copy the
link to the `.tar.gz` file that corresponds to the version you need. Be sure to
select the version for a Linux operating system and x86_64 architecture.

Download the `.tar.gz` file:
```bash
wget [link to file]
```

Extract the `.tar.gz` file:
```bash
tar -xvzf [file name]
```

Add the downloaded version to your path:
```bash
export PATH="~/path/to/julia/bin:$PATH"
```

The following example is for Julia 1.9.0:
```bash
wget https://julialang-s3.julialang.org/bin/linux/x64/1.9/julia-1.9.0-linux-x86_64.tar.gz
tar -xvzf julia-1.9.0-linux-x86_64.tar.gz
export PATH="~/julia-1.9.0/bin:$PATH"
```

## Jupyter Notebooks

While Jupyter is heavily integrated with Python, it supports compatibility with
Julia. You can run Jupyter notebooks on the web portals of
[SuperCloud](https://txe1-portal.mit.edu/) and
[Engaging](https://engaging-ood.mit.edu/).

=== "Engaging"

    On the [Engaging OnDemand web portal](https://engaging-ood.mit.edu/), you
    can specify one of the pre-installed Julia modules under the "Additional
    Modules" section. You can see which Julia modules are available by running
    `module avail julia` from the command line.
    
    For Jupyter to recognize Julia, you need to have the `IJulia` package
    installed and built in your Julia environment:

    ```julia
    using Pkg
    Pkg.add("IJulia")
    Pkg.build("IJulia")
    ```

    Note that the Julia environment you are using needs to match the version of
    Julia that you are loading as a module.

=== "SuperCloud"
    
    To use a Jupyter notebook on the SuperCloud web portal, navigate to
    `/jupyter/` and launch a notebook. When the session is running, open the
    notebook and select a Julia kernel.

    For more information on running Jupyter notebooks on SuperCloud, check the
    [SuperCloud documentation](https://mit-supercloud.github.io/supercloud-docs/jupyter-notebooks/).

### Port Forwarding

If you would like to use a different version of Julia that is not offered
as a module, we suggest running a Jupyter notebook manually via port forwarding.
This involves running the notebook on a compute node, and then accessing the
notebook on your local machine by SSH tunnelling through a login node.

To do this, first request a compute node with your desired resources:

```bash
salloc -N 1 -n 4 -p mit_normal
```

Make a note of the node that your job is running on. In this example, we're
running on `node1600`.

Then, start your desired version of Julia add the `IJulia` package to your
environment:

```Julia
using Pkg
Pkg.add("IJulia")
Pkg.build("IJulia")
quit()
```

Because of Jupyter's interaction with Python, you need to create and activate a
Conda environment with `jupyter` installed:

```bash
module load miniforge
conda create -n jupyter_env jupyter
conda activate jupyter_env
```

!!!Note
    For more information on Conda, see our
    [Python documentation](python.md#conda-environments).

Now, we can run the notebook. To be able to access it on our local machine, we
need to add a few arguments:

```bash
jupyter-lab --ip=0.0.0.0 --port=8888
```

The port can be any number between 1024 and 9999. When you run the notebook,
the output will contain a link with a token that allows you to access the
notebook:

```
http://127.0.0.1:<remote port>/lab?token=<token>
```

For example:

```
http://127.0.0.1:8888/lab?token=7e97d59f9a17c91c11289bc5bec35ad3921725c6db55fe33
```

In a second terminal window, set up an SSH tunnel to your Jupyter notebook
that's running on the compute node:

```bash
ssh -L <local port>:<node>:<remote port> <USER>@orcd-login001.mit.edu
```

In general, it's easier if you keep the local port and the remote port as the
same number:

```bash
ssh -L 8888:node1600:8888 <USER>@orcd-login001.mit.edu
```

Now you can access Jupyter in an internet browser:

```
http://127.0.0.1:<local port>/lab?token=<token>
```

If you kept the local and remote ports as the same number, then you can directly
copy the link that was given to you earlier:

```
http://127.0.0.1:8888/lab?token=7e97d59f9a17c91c11289bc5bec35ad3921725c6db55fe33
```

### VS Code

Please refer to the [VS Code page](../recipes/vscode.md) for using VS Code on
the cluster.

VS Code supports compatibility with Jupyter notebooks. If you have installed
and built `IJulia` in your Julia environment, then you should be able to find
the correct Julia kernel by navigating to `Select Kernel` >
`Select Another Kernel` > `Jupyter Kernel`.

## FAQs

**I have loaded/installed a specific version of Julia, but it is not being recognized. What do I do?**

There may be another/no version of Julia in your `PATH` environment variable.
You can check this by running `echo $PATH`.

If you have loaded a Julia module but do not want to use it, you can run `module
purge`. 
