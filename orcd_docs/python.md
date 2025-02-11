---
tags:
 - Software
 - python
---
# Installing Python Packages 

There are a few different ways to install Python packages. Each ORCD system has its own set of Python modules and naming conventions for those modules, along with a set of recommendations for installing Python packages. This page is meant to give a general overview and link to those pages.

=== "Engaging"

    [Engaging Installing Python Packages Documentation](https://engaging-web.mit.edu/eofe-wiki/software/python_packages/)
    
=== "Satori"

    [Satori Installing Python Packages Documentation](https://mit-satori.github.io/satori-using-anaconda.html)

=== "SuperCloud"

    [SuperCloud Installing Python Packages Documentation](https://mit-supercloud.github.io/supercloud-docs/software-packages/#python-packages)

=== "OpenMind"

    [OpenMind Installing Python Packages Documentation](https://github.mit.edu/MGHPCC/OpenMind/wiki/How-to-make-Python-ready-for-use%3F)

Python packages will need to be installed in your home directory or other directory you have write access to. There are a few different ways to do this, each with its own pros and cons. At a high level, you can:

- [Install packages in your own Python virtual environment (venv)](#python-virtual-environments)
- [Install packages in your own conda/mamba environment](#conda-environments)
- [Install packages to you home directory space using the `pip install --user` command](#home-directory-install)

Which should you use? That can depend on a lot of things. Our recommendation will usually depend on the system, what you are doing, and which packages your are installing. [Python virtual environments](#python-virtual-environments) tend to be a good all-around option as a starting point. With them you can stay organized with environments, but they don't tend to take up as much space or create as many files as conda or mamba environments. Read through the pros and cons for each, they are meant to help you see when one might be better than another.

## Modules for Python

Python is provided on all ORCD systems through either Python, Anaconda or similar [modules](modules.md). See the documentation for the system your are using below for a description of the python modules available. Some systems have some commonly used Python packages installed with their modules, so it is worth checking to see if these packages will satisfy your use case before installing your own.

Refer to the tab below to find out more about the Python modules available on the system you are using.

=== "Engaging"

    Some nodes on Engaging have different operating systems (OS). The newest nodes on Engaging are Rocky 8 and older nodes are Centos 7. Each OS has a different software stack, and so has different sets of Python and Anaconda modules. Both will have both Python and Anaconda modules, but will may have different names and versions. Check `module avail` for this information. Be sure the OS of the login node you are using to launch jobs matches the OS of the compute nodes you are requesting.

    We recommend using the newest miniforge modules for both. For Rocky 8 run:

    ```bash
    module load miniforge/24.3.0-0
    ```

    For Centos 7:

    ```bash
    module load miniforge/24.3.0-0
    ```
    
=== "Satori"

    Satori Python and Anaconda modules are rather old so the advice is to install your own [miniforge](https://conda-forge.org/download/) or [miniconda](https://docs.anaconda.com/free/miniconda/miniconda-install/). Home directories on Satori are quite small, so the recommendation is to install these into `/nobackup/users/$USER` where you have more space.

    Once it is installed you will need to add channels to your conda configuration:

    ```bash
    conda config --prepend channels https://public.dhe.ibm.com/ibmdl/export/pub/software/server/ibm-ai/conda/
    conda config --prepend channels https://opence.mit.edu
    conda config --prepend channels https://ftp.osuosl.org/pub/open-ce/current
    ```

    These channels contain packages compiled for Satori's PowerPC architecture. You only need to run these commands once to add these channels to your configuration file.

=== "SuperCloud"

    SuperCloud releases two anaconda modules per year, named for the year and the release (anaconda/2024a and anaconda/2024b, for example). The most recent modules may continue to be updated until the next "release". There are separate modules for machine learning frameworks (ex: anaconda/Python-ML-2023b). SuperCloud anaconda modules contain a lot of the most commonly used packages and are installed on the local disk of each node, so it is best if you can use packages installed in the modules as much as possible. To enable that, SuperCloud recommends [installing packages to you home directory space using the `pip install --user` command](#home-directory-install), or [creating python virtual environments](#python-virtual-environments) using the `--system-site-packages` flag. SuperCloud has a section on their [Best Practices](https://mit-supercloud.github.io/supercloud-docs/filesystem#installing-python-packages) page about installing Python packages.

=== "OpenMind"

    OpenMind has both Anaconda and miniconda modules available. They have some of the most commonly used packages already installed.

## Python Virtual Environments

Environments allow you to make self-contained “bundles” of packages that can be loaded and unloaded. This helps keep a consistent set of packages and versions for a given project, rather than putting all packages you've ever installed together like they would be when you install with [`pip install --user`](#home-directory-install). Python virtual environments can be placed anywhere you have write access to and have all their packages in that environment’s directory structure.

### Creating Python Virtual Environments

To create a new environment, first load a Python or Anaconda module using the `module load` command. See the page on [Modules](modules.md) for more information on how to load modules. See [Modules for Python](#modules-for-python) above for information about specific modules for the system you are using.

To create a the environment use the `python -m venv` command: 

```bash
python -m venv /path/to/virtual/environment
```

Note that you specify a path, and not only a name for the environment. This means you can place your environment wherever you'd like. Usually it is placed somewhere in the project directory it is used for. For example, if I want to create an environment for a project called `my_project` that lives in my home directory, I would run something like:

```bash
cd ~/my_project
python3 -m venv my_project_env
```

This will create an environment at the path `~/my_project/my_project_env`.

!!!Note
    Virtual Environment documentation and tutorials will often tell you to run the command `python3 -m venv .venv` to create an environment. The `.` at the beginning of `.venv` creates a hidden directory in the current working directory. You won't see this directory if you run the `ls` command by itself, run `ls -a` to see hidden files and directories. If you are new to virtual environments and Linux we recommend using a descriptive name for your environment that is not hidden (doesn't start with `.`).

By default environments will be fully isolated and Python will only see the packages you've installed in the environment. You can signal your virtual environment to "see" system installed packages by using the flag `--system-site-packages` when creating the environment. This is useful when the module you are using has packages already installed. For example:

```bash
python3 -m venv --system-site-packages my_project_env
```

Before installing packages or using an environment we need to activate the environment:

```bash
source /path/to/virtual/environment/bin/activate
```

Using our example above, if we are in the `my_project` directory already, we can run:

```bash
source my_project_env/bin/activate
```

Finally we can now install packages into the environment. Once activating the environment new packages can be installed with the `pip` command:

```bash
pip install pkgname
```

!!!Note
    Do not use `--user` flag to install, this will install into `$HOME/.local` instead of the environment.

When you are done using or installing packages into an environment you can deactivate it with the command:

```bash
deactivate
```

### Using Python Virtual Environments

In order to use an environment you will need to activate it as described above:

```bash
source /path/to/virtual/environment/bin/activate
```

Once it is activated any `python` commands will run in that environment and have access to the packages in the environment. To use an environment in a job activate the environment in your job script. An environment activated on the login node will not necessarily carry over to your job. Using the same example above, let's look at the script `myjob.sh` in the `my_project` directory:

```bash title="myjob.sh"
#!/bin/bash

source my_project_env/bin/activate

python myscript.py
```

When this job runs it will activate the environment in `my_project_env` and then run the python script `myscript.py` using the packages in that environment.

### Requirements.txt and Virtual Environments

Environments can be described by a `requirements.txt` file, which lists packages and optionally their versions. This file can be created from any existing virtual environment and used to re-create that environment. Version numbers are required to recreate the environment exactly.

You can either create a `requirements.txt` file by hand by creating a file with one package name on each line, or you can create one from a currently active environment with the command:

```bash
pip freeze > requirements.txt
```

Given a `requirements.txt` file you can use `pip` to install the packages in that file into your environment. First activate the environment, then install the packages with:

```bash
source /path/to/virtual/environment/bin/activate
pip install -r requirements.txt
```

### Pros and Cons for Virtual Environments

Pros

- Can be set to build “on top of” the central installation packages (not default behavior, use the `--system-site-packages` flag when creating)
- Self-contained environments for each project help stay organized and avoid package dependency conflicts. For software development it allows you to keep better track of your package’s dependencies so others know what they need to install.
- Virtual environments are self-contained, fairly lightweight and can be put anywhere easily without additional configuration files

Cons

- Environments will be the same version of the python that you used to make them
- Only installs packages available through PyPI, cannot install anaconda/conda-forge distributed packages or libraries

## Conda Environments

Environments allow you to make self-contained “bundles” of packages that can be loaded and unloaded. This helps keep a consistent set of packages and versions for a given project, rather than putting them all together like they would be when you install with [`pip install --user`](#home-directory-install). Conda environments are a bit different from Python virtual environments, by default they are stored in the `.conda` directory in your home directory. They also tend to contain a lot more files than Virtual Environments. You can also install some system libraries into conda environments, which can make installing packages with system library dependencies easier.

You'll also see mention of mamba environments. Mamba and conda are nearly the same, however mamba has a different dependency solver. Mamba is often better and faster than conda at solving dependencies and picking packages, so we recommend using mamba whenever possible.

### Creating Conda Environments

First, load a conda or Anaconda module using the `module load` command. See the page on [Modules](modules.md) for more information on how to load modules. See [Modules for Python](#modules-for-python) above for information about specific modules for the system you are using.

!!!Note
    If you are using Satori you will need to add channels to include packages compiled for PowerPC:

    ```bash
    conda config --prepend channels https://public.dhe.ibm.com/ibmdl/export/pub/software/server/ibm-ai/conda/
    conda config --prepend channels https://opence.mit.edu
    conda config --prepend channels https://ftp.osuosl.org/pub/open-ce/current
    ```

    See [Modules for Python](#modules-for-python) above for more information.

If there is no anaconda module on the system you are using, or the modules available aren't sufficient for your work, we recommend installing [miniforge](https://conda-forge.org/download/) or [miniconda](https://docs.anaconda.com/free/miniconda/miniconda-install/) in your home directory. Wwe have had the most  success with miniforge, which is distributed by conda-forge and is packaged with mamba. It is best to avoid installing the full Anaconda as it is very big and can fill up your home directory. One of the most common reasons for slow logins, job startups, and package imports are from a full anaconda installation in the home directory.

!!! Note
    If you are using SuperCloud do not install miniconda or miniforge in your home directory. SuperCloud keeps up to date anaconda modules so installing your own is not necessary and will slow down your applications. See this [Best Practices](https://mit-supercloud.github.io/supercloud-docs/filesystem/#installing-python-packages) page on SuperCloud-Docs for more information.

To create an environment you can use the `mamba create` or `conda create` command after loading your conda module:

```bash
module load conda_module
mamba create -n my_env python=3.10 pkg1 pkg2 pkg3
```

or, using `conda`:

```bash
module load conda_module
conda create -n my_env python=3.10 pkg1 pkg2 pkg3
```

where `conda_module` is the name of the conda or mamba module for the system you are using. In this example I am creating a conda environment named `my_env` with Python 3.10 and installing packages pkg1, pkg2, pkg3. We have found that conda/mamba creates more robust environments when you include all the packages you need when you create the environment.

You can install additional packages by activating the environment and using the `mamba install` or `conda install` command. Again you would first load the appropriate module if it isn't already loaded:

```bash
module load conda_module
source activate my_env
mamba install pkg4
```

where `conda_module` is the name of the conda or mamba module for the system you are using. Here I am showing with `mamba`, replace with `conda` if you have a conda environment. Packages that aren't available through conda channels can be installed with the `pip` command when the environment is activated:

```bash
module load conda_module
source activate my_env
pip install pkg5
```

!!! Note
    To install packages with `pip` to a conda or mamba environment you should *not* include the `--user` flag. Further, if you are using a conda environment and want Python to *only* use packages in your environment, you can run the following two command:
    
    ```bash
    export PYTHONNOUSERSITE=True
    ```
    
    This will make sure your conda environment packages will be chosen before those that may be installed in your home directory.

If you would like to use your conda environment in Jupyter, install the "jupyter" package into your environment. Once you have done that, you should see your conda environment listed in the available kernels.

### Using Conda Environments

Then, whenever you want to activate the environment, first load the anaconda module, then activate with `source activate my_env`. Using `source activate` instead of `conda activate` allows you to use your conda environment at the command line and in submission scripts without additional steps. See [Conda/Mamba Init](#condamamba-init) in the Troubleshooting section below for more information.

```bash
module load conda_module
source activate my_env
```

To use a conda environment in a job you can usually add these lines to you job script:

```bash title="myjob.sh"
#!/bin/bash

module load conda_module

source activate my_env

python myscript.py
```

If this isn't working, see the Troubleshooting section below on [activating an environment in a job script](#environment-is-not-activating-in-a-job-script).

### Pros and Cons for Conda Environments

Pros

- Environments can be created with any supported version of Python.
- Can install packages available through various conda channels as well as PyPI (packages installed with `pip`).
    - Conda channels include many system libraries, making packages with complicated dependencies easier to install.
- Self-contained environments for each project help stay organized and avoid package dependency conflicts. For software development it allows you to keep better track of your package’s dependencies so others know what they need to install.

Cons

- Can not be set to build “on top of” the central installation packages, which means basic package will be re-installed in your home directory.
- Can get very large and take up a lot of space in your home directory.
- It can sometimes be slower than other options.

## Home Directory Install

First, load a Python or Anaconda module using the `module load` command. See the page on [Modules](modules.md) for more information on how to load modules.

Then, install the package with pip using the `--user` flag:

```bash
pip install --user packageName
```

Where `packageName` is the name of the package that you are installing.

With `pip install --user` you are installing a single package and any missing dependencies. Pip will see any packages already installed in the central Python installation and won’t reinstall those as log as they satisfy the dependency requirements. These get installed to:

```
$HOME/.local/lib/pythonV.V/site-packages
```

This location is usually first in Python’s package search path, so Python will pick up any libraries installed here before centrally installed ones. The exceptions are:

- If you have the `PYTHONPATH` environment variable set, that location will be searched first
- You have the `PYTHONNOUSERSITE` environment variable set to True, this tells Python to remove it from the path

### Pros and Cons for .local Install

Pros

- The installs are usually pretty easy
- Only installs what is absolutely needed, allowing Python to use centrally installed packages

Cons

- Keeping and tracking a consistent environment is harder, not great for package development or working on different projects with conflicting requirements
- Everything you’ve installed is always in your environment, which can cause two issues:
    - The space can eventually get “dirty” or “corrupted”, the easiest fix is to delete or rename `$HOME/.local` and start again
    - You can run into package dependency conflict issues, which could be fixed by uninstalling packages no longer needed or by deleting or renaming `$HOME/.local` and starting again


## Troubleshooting Python Package Issues

### Check your Python Executable

When you use the `python` command Linux will pick the first `python` executable it finds in your `$PATH`. If Python is not finding your installed packages it is possible that the `python` running is not what you expect. Run the command:

```bash
which python
```

This will print out the path to the `python` executable that is running. If it doesn't print the right one, check that you've activated your environment or loaded the module you were intending.

### Check Python's Path

Python has its own path that gets set when it looks for packages. This path depends on a few things, such as whether you have an environment loaded and how that environment is configured. When in doubt you can view this path in Python with the following commands:

```python
import sys
sys.path
```

Similar to the `PATH` environment variable, Python checks the locations on the path in the order they are listed and imports the first of the specified package it finds. If Python is loading the wrong version of a package, checking the path will tell you where to check for the wrong-version package. If Python can't find the package, the path will give you more information about where it is looking.

### Conda/Mamba Init

If you use conda or mamba you may at some point be asked to run `conda init` or `mamba init`. These commands will edit your `.bashrc` file which gets run every time you log in. These additional lines will make permanent changes to your environment that could have unintended effects on your use of the system. This can cause issues, including slowing down your logins and affecting any software builds you try to do.

The best thing to do is to never run these commands, or if you have, to remove the lines that they  have added to your `.bashrc` file. Instead of running `conda activate` or `mamba activate`, you can use the `source activate` command.

If this doesn't work for you, as an alternative, you can run the following line:

```bash
source /path/to/conda/install/etc/profile.d/conda.sh
```

whenever you want to use the `conda activate` command. Be sure to replace `/path/to/conda/install` with the path to the conda installation, for example if you installed miniforge in your home directory the full path might be `$HOME/miniforge3/etc/profile.d/conda.sh`.

If you would like to use `mamba activate`, run the following line as well:

```bash
source /path/to/conda/install/etc/profile.d/mamba.sh
```

Both of these lines can be run at the command line, or put in a job script or setup script. Note that environments activated at the command line before launching a job may not carry over to the job itself, so it is always best load these environments in your job script.

```bash title="mycondajob.sh"
#!/bin/bash

source /path/to/conda/install/etc/profile.d/conda.sh
source /path/to/conda/install/etc/profile.d/mamba.sh

mamba activate myenv # or `conda activate myenv` for conda environments

python myscript.sh
```

If you feel strongly that you want to keep the setup that `conda init` gives you in your `.bashrc`, first be aware that it could cause issues and it might be something to look into removing when troubleshooting. Second, one of the things these lines do is activate the base environment associated with the conda installation, which is usually the source of most of the issues you can run into. You can set conda to not activate the base environment at login by running the following line:

```bash
conda config --set auto_activate_base false
```

You only need to run this line once. It will edit a configuration file for conda (.condarc). You will still be able to run `mamba activate` or `conda activate`.

### Environment is not Activating in a Job Script

Getting your python virtual environment or conda/mamba environment to activate in a batch job can sometimes be finicky.

Check your log file to be sure you aren't getting any errors when you try to activate the environment. They may give further instruction on what to do.

Usually the cause is something in your environment that is interfering, these could be:

- The `PYTHONPATH` environment variable is set- this changes where Python looks for packages first. Best practice is to not use `PYTHONPATH` when possible.
- You have another environment activated (see [Conda/Mamba Init](#condamamba-init)).
- Your python script starts with a line like `#!/bin/python` or similar. This tells the system to run the script with a python executable that isn't part of your environment. Removing the line will fix the issue.

Beyond this, there are a few things you can try. These won't necessarily fix your environment issues, but might work around them. First let's talk about virtual environments, then conda environments.

#### Activating a Virtual Environment in a Script

Usually activating the environment in your job script before running your Python script is sufficient. 

If your environment isn't activating, specifying the full path to the python executable in your environment sometimes fixes things. Here is a sample job script:

```bash title="myjob.sh"
#!/bin/bash

source /path/to/virtual/environment/bin/activate

/path/to/virtual/environment/bin/python myscript.py
```

Be sure to replace `/path/to/virtual/environment` with the actual path to your virtual environment.

#### Activating a Conda/Mamba Environment in a Script

Usually loading an anaconda module and then running `source activate myenv` will work to activate a conda or mamba environment in a job script (as shown [above](#conda-environments)).

One thing to try is suggested above in [Conda/Mamba Init](#condamamba-init):

```bash title="mycondajob.sh"
#!/bin/bash

source /path/to/conda/install/etc/profile.d/conda.sh
source /path/to/conda/install/etc/profile.d/mamba.sh #optional

conda activate myenv # or `mamba activate myenv` for mamba environments

python myscript.sh
```

If this doesn't work sometimes adding `eval "$(conda shell.bash hook)"` in the line before activating the environment will make it work:

```bash title="mycondajob.sh"
#!/bin/bash

source /path/to/conda/install/etc/profile.d/conda.sh
source /path/to/conda/install/etc/profile.d/mamba.sh #optional
eval "$(conda shell.bash hook)"

conda activate myenv # or `mamba activate myenv` for mamba environments

python myscript.sh
```
