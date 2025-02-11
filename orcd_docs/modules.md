---
tags:
 - Software
 - Modules
---
# Modules

Modules are a handy way to set up your environment for particular work, especially in a shared environment. They provide an easy way to load a particular version of a software, language, or compiler.

To see what modules are available, type the command:

```bash
module avail
```

!!! Note
    (For Engaging only) Engaging's newest hardware is running with the Rocky 8 operating system, whereas older hardware is using CentOS 7. You will see different module lists depending on whether you are on Rocky 8 or CentOS 7 node.

    By default you will only see the modules for [core and community software](overview.md#software-landscape). How to show deprecated modules will differ depending on the operating system for the node you are using.
    
    === "Rocky 8"

        To show deprecated modules load the `deprecated-modules` module:
        ```bash
        module load deprecated-modules
        ```
    === "Centos 7"
        Historically community modules were not separated in the Centos 7 software stack, however some newer community modules are separate. These can be seen by running the following `module use` command:
        ```bash
        module use /orcd/software/community/001/centos7/modulefiles
        ```

To load a module, use the command:

```bash
module load moduleName
```

Where `moduleName` can be any of the modules listed by the `module avail` command.

!!! Note
    We do not recommend including `module load` commands in your `.bashrc`, `.bash_profile`, or any other startup scripts and instead include them in your job scripts. This provides a more predictable and consistent environment for your jobs. It is also very easy to forget that you have modules loaded in your `.bashrc`, and these can have impact on future workloads.

If you want to list the modules you currently have loaded, you can use the `module list` command:

```bash
module list
```

If you want to change to a different version of the module you have loaded, you can switch the module you have loaded. This is important to do when loading a different version of a module you already have loaded, the module command will not allow you to load two different versions of the same software. To switch modules run:

```bash
module switch oldModuleName newModuleName
```

where `oldModuleName` is the name of the module you currently have loaded, and `newModuleName` is the new module that you would like to load.

If you would like to unload the module, or remove the changes the module has made to your environment, use the following command:

```bash
module unload moduleName
```

If you would like to unload all modules in your environment, you can use the command:

```bash
module purge
```

This command is helpful when you want to ensure a clean environment. You can include it at the start of your job scripts to make sure your jobs all have a consistent environment. Loaded modules may carry over into your jobs, and sometimes can interfere with the work you are doing in unexpected ways.


