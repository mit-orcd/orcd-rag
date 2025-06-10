---
tags:
 - Engaging
 - SuperCloud
 - Howto Recipes
 - MuJoCo
---
# Installing and Using MuJoCo

MuJoCo is a free and open source physics engine that aims to facilitate research and development in robotics, biomechanics, graphics and animation, and other areas where fast and accurate simulation is needed.

You can learn about MuJoCo here: [https://mujoco.org](https://mujoco.org).

Whether you are installing on Engaging or SuperCloud, you’ll first have to install the MuJoCo binaries. This process is the same on all systems.

## Install the MuJoCo Binaries

First, install MuJoCo itself somewhere in your home directory. This is as simple as downloading the MuJoCo binaries, which can be found on their web page. For the release that you want, select the file that ends with “linux-x86_64.tar.gz”, for example for 2.3.0 select [mujoco-2.3.0-linux-x86_64.tar.gz](https://github.com/deepmind/mujoco/releases/download/2.3.0/mujoco-2.3.0-linux-x86_64.tar.gz). Right click, and copy the link address. Then you can download on one of the login nodes with the “wget” command, and untar:

```bash
--8<-- "docs/recipes/scripts/mujoco/mujoco-binaries.sh:login"
```

In order for mujoco-py to find the MuJoCo binaries, set the following paths:

```bash
--8<-- "docs/recipes/scripts/mujoco/mujoco-binaries.sh:path"
```

## Install Mujoco-Py

First, make sure the `MUJOCO_PY_MUJOCO_PATH` and `LD_LIBRARY_PATH` environment variables are set pointing to your mujoco installation. You can use the “echo” command to do this:

```bash
--8<-- "docs/recipes/scripts/mujoco/mujoco-binaries.sh:env-var"
```

If any of these are not set properly you can set them as described above (see [here for MUJOCO_PY_MUJOCO_PATH, LD_LIBRARY_PATH](#install-the-mujoco-binaries).

=== "Engaging"

    Next load either a Python or Anaconda module. In this example I loaded the latest anaconda3 module (run `module avail anaconda` to see the current list of available anaconda modules):

    ```bash
    --8<-- "docs/recipes/scripts/mujoco/mujoco-engaging-setup.sh:module"
    ```

    From here on you can follow the [standard instructions to install mujoco-py](https://github.com/openai/mujoco-py), using the `--user` flag where appropriate to install in your home directory, or install in an anaconda or virtual environment (do not use the `--user` flag if you want to install in a conda or virtual environment). Here I am installing in my home directory with `--user`:

    ```bash
    --8<-- "docs/recipes/scripts/mujoco/mujoco-engaging-setup.sh:install"
    ```

    Start up python and import mujoco_py to complete the build process:

    ```bash
    --8<-- "docs/recipes/scripts/mujoco/mujoco-engaging-setup.sh:python"
    ```

=== "SuperCloud"

    MuJoCo, particularly mujoco-py, can be tricky to install on SuperCloud as it uses file locking during the install and whenever the package is loaded. File locking is disabled on the SuperCloud shared filesystem performance reasons, but is available on the local disk of each node. Therefore, one workaround is to install mujoco-py on the local disk of one of the login nodes and then copy the install to your home directory. To load the package, the install then needs to be copied to the local disk.

    We’ve found the most success by doing this with a python virtual environment. By using a python virtual environment you can install any additional packages you need with mujoco-py, and they can be used along with packages in our anaconda module, unlike conda environments.

    Create the virtual environment on the local disk of the login node and install mujoco-py (install the version you would like to use):

    ``` bash
    --8<-- "docs/recipes/scripts/mujoco/mujoco-supercloud-setup.sh:venv"
    ```

    Now install any other packages you need to run your MuJoCo jobs. With virtual environments you won’t see any of the packages you’ve previously installed with `pip install --user` or what you may have installed in another environment. You should still be able to use any of the packages in the anaconda module you’ve loaded, so no need to install any of those.

    ``` bash
    --8<-- "docs/recipes/scripts/mujoco/mujoco-supercloud-setup.sh:pkgs"
    ```

    Since you are installing into virtual environment, **do not use the `--user` flag**.

    Once you’ve installed the packages you need, start Python and import mujoco_py to finish the build:

    ``` bash
    --8<-- "docs/recipes/scripts/mujoco/mujoco-supercloud-setup.sh:python"
    ```

    Now that your environment is created, copy it to your home directory for permanent storage.

    ``` bash
    --8<-- "docs/recipes/scripts/mujoco/mujoco-supercloud-setup.sh:directory"
    ```


If you’d like you can run the few example lines listed on install section of the mujoco-py github page to verify the install went through properly:

```python
--8<-- "https://github.com/mit-orcd/orcd-examples/raw/main/mujoco/mujoco_test.py"
```

## Using MuJoCo in a Job

To use MuJoCo you’ll need to first load the same Python or Anaconda module you used to install mujoco-py. If you installed it into a conda environment or python virtual environment, load that environment as well. We recommend you do this in your job submission script rather than in your .bashrc or at the command line before you submit the job. This way you know your job is configured properly every time it runs.

You can use the following test scripts to test your MuJoCo setup in a job environment, and as a starting point for your own job:

``` py title="mujoco_test.py"
--8<-- "https://github.com/mit-orcd/orcd-examples/raw/main/mujoco/mujoco_test.py"
```

=== "Engaging"

    ``` bash title="submit_test.sh"
    --8<-- "https://github.com/mit-orcd/orcd-examples/raw/main/mujoco/submit_test_engaging.sh"
    ```
=== "SuperCloud"

    Now whenever you use mujoco-py the installation will need to be on the local disk of the node(s) where you are running. In your job script you can add a few lines of code that will check whether the environment exists on the local disk, and if not copy it. You can run these lines during an interactive job as well.

    ``` bash title="submit_test.sh"
    --8<-- "https://github.com/mit-orcd/orcd-examples/raw/main/mujoco/submit_test_supercloud.sh"
    ```