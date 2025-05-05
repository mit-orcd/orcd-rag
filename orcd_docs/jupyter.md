---
tags:
 - Jupyter
 - Best Practices
---

# Jupyter Notebooks

Jupyter notebooks provide a way to run code in an interactive environment. While
most prominently used for [Python](../software/python.md), Jupyter supports a
range of languages, such as [Julia](../software/julia.md) and
[R](../software/R.md).

## Choosing an Approach

There are multiple ways to run Jupyter notebooks on the computing clusters
available through ORCD. The route you choose depends on your needs and level of
familiarity with high performance computing environments.

### Web Portal

The most straightforward way to run a Jupyter notebook on one of our computing
clusters is to use the cluster's web portal. While this route is the easiest
to set up, it can be limiting if you want more control over your environment
or the resources allocated to your notebook.

=== "Engaging"

    - Link to web portal:
    [https://engaging-ood.mit.edu/](https://engaging-ood.mit.edu/)

    - Select "Interactive Apps" --> "Jupyter Notebook"

    - Follow the on-screen instructions to start a session. You are able to use
    a custom Conda environment provided it has `jupyterlab` installed.

    - If you'd like to run [Julia](#julia), enter the name of the Julia module
    you're using (e.g., `julia/1.8.5`). Note that you need to have `IJulia`
    installed in your environment for this version of Julia.

    - If you'd like to run [R](#r), enter the name of your custom Conda
    environment that has `r-irkernel` installed.

    - When the session is ready, click "Connect to Jupyter." From here you can
    create a Jupyter notebook and select the language you would like to use.

    !!! note
        The Engaging web portal is currently running on CentOS 7, which has a
        different set of modules from Rocky 8 nodes. If you would like to run
        a Jupyter notebook on Rocky 8, you will need to follow either the [VS
        Code](#vs-code) or [port forwarding](#port-forwarding) method.

=== "Satori"

    - Link to web portal:
    [https://satori-portal.mit.edu/](https://satori-portal.mit.edu/)

    - Select "Interactive Apps" --> "Jupyter Notebook" or
    "Jupyter Notebook [Experimental]"

    - Follow the on-screen instructions to start a session. You are able to use
    a custom Conda environment in the experimental notebook provided it has
    `jupyterlab` installed.

    - If you'd like to run [R](#r), enter the name of your custom Conda
    environment that has `r-irkernel` installed.

    - When the session is ready, click "Connect to Jupyter." From here you can
    create a Jupyter notebook and select the language you would like to use.

=== "SuperCloud"

    - Link to web portal:
    [https://txe1-portal.mit.edu/](https://txe1-portal.mit.edu/)

    - Select "jupyter" and follow the on-screen instructions to create a Jupyter
    notebook. When you open a notebook, select the kernel for your desired
    language.

    See the [SuperCloud documentation on Jupyter](https://mit-supercloud.github.io/supercloud-docs/jupyter-notebooks/)
    for more information.

### VS Code

First, follow [these instructions](./vscode.md) to set up VS Code to run on a
compute node.

Open a Jupyter notebook and click the top right button to select a kernel. You
can select "Python Environments" for any Conda environments or "Jupyter Kernel"
to find Julia or R environments. If you have installed R with Conda, you can
find your Conda environment under "Jupyter Kernel." `jupyterlab` must be
installed to your Conda environment.

### Port Forwarding

Port forwarding offers the most flexibility in setting up your Jupyter notebook
but the setup is slightly more involved. With port forwarding, the rendering
is handled through your internet browser while computation is done on the
cluster. This method is more lightweight than VS Code and can be more reliable.

Port forwarding consists of running the notebook on a compute node and then
accessing the notebook on your local machine by SSH tunnelling through a login
node.

First, request a compute node with the resources you'll need for your Jupyter
session (here we are requesting 1 node with 4 CPU cores):

=== "Engaging"

    ```bash
    salloc -N 1 -c 4 -p mit_normal
    ```

=== "Satori"

    ```bash
    srun -N 1 -c 4 --pty /bin/bash
    ```

=== "SuperCloud"

    ```bash
    LLsub -i -s 4
    ```

!!! note
    See [Requesting Resources](../running-jobs/requesting-resources.md) for more
    information.

Make a note of the node that your job is running on by running `hostname` from
the command line.

Even if you are using a different language with Jupyter, Jupyter is tightly
linked to Python, so you will need to use a Conda environment with
`jupyterlab` installed:

=== "Engaging"

    ```bash
    module load miniforge
    conda create -n jupyter_env jupyterlab
    conda activate jupyter_env
    ```

=== "Satori"

    ```bash
    module load anaconda3
    conda create -n jupyter_env jupyterlab
    conda activate jupyter_env
    ```

=== "SuperCloud"

    ```bash
    module load anaconda
    conda create -n jupyter_env jupyterlab
    conda activate jupyter_env
    ```

Now, we can run the notebook. To be able to access it on our local machine, we
need to add a few arguments:

```bash
jupyter-lab --ip=0.0.0.0 --port=8888
```

The port can be any number between 1024 and 65535.

!!! note
    You can also set the port to one that you know is open as such:

    ```bash
    port=$(python -c 'import socket; s=socket.socket(); s.bind(("", 0)); print(s.getsockname()[1]); s.close()')
    jupyter-lab --ip=0.0.0.0 --port=$port
    ```

When you run the notebook, the output will contain a link with a token that
allows you to access the notebook:

```
http://127.0.0.1:<remote port>/lab?token=<token>
```

For example:

```
http://127.0.0.1:8888/lab?token=7e97d59f9a17c91c11289bc5bec35ad3921725c6db55fe33
```

We cannot use this link directly yet because that node is not available from our
local machine. Through "tunneling," however, we can access this node through
a login node, which is accessble from our local machine.

In a second terminal window on your local machine, set up an SSH tunnel to your
Jupyter notebook that's running on the compute node, filling in the node name,
port number, and username as necessary:

=== "Engaging"

    ```bash
    ssh -L <local port>:<node>:<remote port> <USER>@orcd-login001.mit.edu
    ```

    In general, it's easier if you keep the local port and the remote port as
    the same number:

    ```bash
    ssh -L 8888:<node>:8888 <USER>@orcd-login001.mit.edu
    ```

=== "Satori"

    ```bash
    ssh -L <local port>:<node>:<remote port> <USER>@satori-login-001.mit.edu
    ```

    In general, it's easier if you keep the local port and the remote port as
    the same number:

    ```bash
    ssh -L 8888:<node>:8888 <USER>@satori-login-001.mit.edu
    ```

=== "SuperCloud"

    ```bash
    ssh -L <local port>:<node>:<remote port> <USER>@txe1-login.mit.edu
    ```

    In general, it's easier if you keep the local port and the remote port as
    the same number:

    ```bash
    ssh -L 8888:<node>:8888 <USER>@txe1-login.mit.edu
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

Now you can open a Jupyter notebook and select your kernel from the top right
corner. The Python environment is the same environment you used to run the
notebook.

## Language-Specific Instructions

### Julia

You will need to add the `IJulia` package to your environment for Jupyter to
recognize the Julia kernel. You can do so from the command line:

```bash title="Bash"
module load julia
julia
```
```julia title="Julia"
using Pkg
Pkg.add("IJulia")
Pkg.build("IJulia")
```

Unlike R, Julia environments are separate from Conda. However, if the `IJulia`
package is installed, then the Julia kernel should be visible regardless of the
Conda environment from which you run your Jupyter notebook.

See our [Julia documentation](../software/julia.md) for more information.

### R

To run R in a Jupyter notebook, you need to create a Conda environment with
both `r-irkernel` and `jupyterlab` installed:

=== "Engaging"

    ```bash
    module load miniforge
    conda create -n r_jupyter_env jupyterlab r-irkernel
    conda activate r_jupyter_env
    ```

=== "Satori"

    ```bash
    module load anaconda3
    conda create -n r_jupyter_env jupyterlab r-irkernel
    conda activate r_jupyter_env
    ```

=== "SuperCloud"

    ```bash
    module load anaconda
    conda create -n r_jupyter_env jupyterlab r-irkernel
    conda activate r_jupyter_env
    ```

Most R packages are available through Conda, so feel free to install other
packages you need to this environment.

See our [R documentation](../software/R.md) for more information.

### Python

To run Python Jupyter notebooks, install `jupyterlab` to whatever Conda
environment that contains the packages you need.

See our [Python documentation](../software/python.md) for more information.

## FAQs

**How do I run a Jupyter notebook with a GPU?**

The cluster web portals offer an option to allocate a GPU to your Jupyter
session. If you would like to use a different partition, however, then follow
the instructions for [VS Code](#vs-code) or [port forwarding](#port-forwarding)
and request a GPU in your Slurm job. See [our documentation on requesting
resources](../running-jobs/requesting-resources.md#gpus) for more information.

**Jupyter does not recognize the kernel for my environment. What do I do?**

First, make sure you have `r-irkernel` installed if you're using R, `IJulia`
installed (and built) if you're using Julia, and `jupyterlab` installed to
your Conda environment.

On VS Code, you may need to specify the path to the `conda` binary of the Conda
installation you're using. This can be done by editing the "Python: Conda Path"
setting. For example, if you're using the `miniforge/24.3.0-0` module on
Engaging, the path would be:

```
/orcd/software/core/001/pkg/miniforge/24.3.0-0/condabin/conda
```

To see all kernels that Jupyter recognizes, activate a Conda environment with
`jupyterlab` installed and run `jupyter kernelspec list`.

**I tried to install `jupyterlab` to my Conda environment, but the installation
failed. How can I run a Jupyter notebook with the dependencies I need?**

It's best to install the packages you need when you create a Conda environment
rather than one-by-one after the environemnt has been created. This will make
Conda more likely to solve your environment succesfully. For example:

```bash
conda create -n jupyter_env jupyterlab pandas pytorch
```

See [Conda Environments](../software/python.md#conda-environments) for
more information.
