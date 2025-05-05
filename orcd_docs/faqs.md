# Frequently Asked Questions

### How do I get GPU access?

Currently we have many public GPUs available to the MIT community on Satori and
we are working on getting more on Engaging. If you have access to a partition
with GPUs (e.g., if your lab has purchased some), you can request GPUs for your
job by following [this documentation](running-jobs/requesting-resources.md#gpus).

If your lab would like to purchase GPUs to be hosted on Engaging, please contact
<orcd-help-engaging@mit.edu>.

### How do I check the status of my job?

Instructions for checking job status can be found
[here](running-jobs/overview.md#checking-job-status).

### How can I submit a module request?

We are open to creating new modules for the Engaging cluster. You can submit all
module requests to <orcd-help-engaging@mit.edu>.

### I am unable to install a package in R. How can I debug the issue?

We recommend using Conda to manage R packages. Please refer to the
[R user guide](software/R.md).

### Can I use export controlled software on the cluster?

Export controlled software has specific requirements around who is allowed to
access the software. Often, our clusters do not meet these requirements, so
we generally do not allow such software to be used on our systems. Please refer
to the terms of use of the software and direct any questions to
<orcd-help@mit.edu>.

### How do I increase the time limit for my job?

Use the `-t` flag in your job script. If you do not specify, Slurm will give
you the maximum time limit for that partition. You can check the maximum time
limit by running `sinfo -p <partition name>`.

For public partitions on Engaging, such as `mit_normal`, we cannot increase the
maximum job time limit, as these resources are shared. For jobs that
need to run longer than the time limit, we encourage
checkpointing, which is a way of periodically saving progress so that subsequent
jobs can pick up where previous jobs left off. The implementation of checkpointing
is domain specific and can vary greatly. You can find more information on
checkpointing [here](https://rc-docs.northeastern.edu/en/latest/best-practices/checkpointing.html).

For increasing the maximum time limit on partitions owned by other groups,
please email <orcd-help-engaging@mit.edu>.

### How do I get an account?

=== "Engaging"
    If you have an MIT Kerberos account, then you can get an account on
    Engaging. To register, navigate to the [Engaging OnDemand Portal](https://engaging-ood.mit.edu/)
    and log in.

=== "Satori"
    If you have an MIT Kerberos account, then you can get an account on Satori.
    To register, navigate to the [Satori Portal](https://satori-portal.mit.edu/)
    and log in.

=== "SuperCloud"
    Access to SuperCloud is more restrictive and the account generation process
    is more involved. For more information, see the
    [SuperCloud documentation](https://mit-supercloud.github.io/supercloud-docs/requesting-account/).

### How do I install a Python package?

See our documentation on [Python](software/python.md).

### Why won't my application run on a different partition?

On Engaging, the older nodes (such as the `sched_mit_hill` and `newnodes`
partitions) run on CentOS 7 while the newer nodes (such as `mit_normal` and
`mit_preemptable`) run on the Rocky 8 operating system (OS). Each set of nodes
has a different set of modules, so if you have set up software to run on one OS,
it will probably not work on the other OS.

### How do I run Jupyter notebooks?

You can run Jupyter a few different ways:

1. Web portal for the cluster you're using
2. [VS Code](recipes/vscode.md)
3. Port forwarding

See our [Jupyter documentation](recipes/jupyter.md).

### Xfce desktop has failed to start. How can I fix this?

This issue is often caused by Conda setup commands existing in your `~/.bashrc`
file. This happens when you run `conda init` when using Miniforge or another
Anaconda install. We recommend **not** running `conda init` as it can lead to
errors such as this one.

To fix this, remove or comment out all conda setup commands from your
`~/.bashrc` file.

### How do I use Git on the cluster?

Git is highly encouraged for use on the cluster. It is useful for backing up
code and version control, especially when collaborating with others.

We recommend setting up an SSH key with GitHub for security and convenience.
This allows you to use the "SSH" link rather than the "HTTPS" link when cloning
repositories. To set up an SSH key, follow these steps:

1. [SSH](accessing-orcd/ssh-login.md) to the cluster you're using

2. Enter the following from the command line:

    ```bash
    ssh-keygen -t ed25519 -C "$USER@mit.edu"
    ```

3. Press "enter" to save your private and public keys to the default `~/.ssh`
location. When prompted, optionally enter a passphrase for higher security. You
will now have two new files in your `~/.ssh` directory: `id_ed25519` and
`id_ed25519.pub`.

4. Print the contents of your **public key** (using `cat id_ed25519.pub`) and
copy the output

5. Navigate to [GitHub.com](https://github.com) > click your profile in the top right
corner > select "Settings" > "SSH and GPG keys" > "New SSH key"

6. Add a title (e.g., "engaging"), paste your **public key**, and click "Add
SSH key"

See [GitHub's documentation on SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux) for more information.

### How do I install PyTorch on Satori?

Satori uses a ppc64le architecture, which is unfortunately not supported by the
newer versions of many Python packages. As a result, the newest version of
PyTorch that is available on Satori is version 2.1.2.

The following channels offer more packages that work on the ppc64le
architecture:

- `https://ftp.osuosl.org/pub/open-ce/current`
- `https://opence.mit.edu`
- `https://public.dhe.ibm.com/ibmdl/export/pub/software/server/ibm-ai/conda/`
- `conda-forge`

You can add these channels with the following command:

```bash
conda config --prepend channels <channel>
```

Some users have had more success installing their own version of Miniconda,
which can be accomplished as such:

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-ppc64le.sh .
chmod +x ./Miniconda3-latest-Linux-ppc64le.sh
./Miniconda3-latest-Linux-ppc64le.sh -b -p ./mc3
source ./mc3/bin/activate
```
