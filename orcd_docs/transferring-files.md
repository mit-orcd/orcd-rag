# Transferring Files

There are a few different ways to transfer files depending on your goals, the data you are transferring, and what you are comfortable with. On this page we cover the different methods of transferring files, as well as touch on how to transfer files between systems.

For most of these options you will need to know the hostname of the node where you will be transferring files. This is often a login node, but may also be a dedicated data transfer node. Select the system you are using to see options for the hostname here:

=== "Engaging"

    - `orcd-login001.mit.edu`
    - `orcd-login002.mit.edu`
    - `orcd-login003.mit.edu`
    - `orcd-login004.mit.edu`

=== "Satori"

    - `satori-login-001.mit.edu`
    - `satori-login-002.mit.edu`

=== "OpenMind"

    - `openmind-dtn.mit.edu`

=== "SuperCloud"

    - `txe1-login.mit.edu`

For more information specific to the system you are using, you can consult your system's documentation here:
=== "Engaging"

    Engaging does not have an additional documentation page.

=== "Satori"

    [Satori Transferring Files Documentation Page](https://mit-satori.github.io/satori-getting-started.html#transferring-files)

=== "SuperCloud"

    [SuperCloud Transferring Files Documentation Page](https://supercloud.mit.edu/accessing-and-transferring-data-and-files)

=== "OpenMind"

    [OpenMind Transferring Files Documentation Page](https://github.mit.edu/MGHPCC/OpenMind/wiki/How-to-transfer-files%3F)

## Transferring Files with the Command Line

Two of the most common commands used to transfer files are `scp` and `rsync`. You will need to run both of these commands from your local computer, before logging into any ORCD system. In order to use these two command you will need:

- The hostname of the remote machine you are transferring files or from (usually the login node)
- The path on the remote machine where you are copying the file to or from
- To be able to ssh to the remote machine where you are transferring files to or from

Both `scp` and `rsync` work similar to `cp`, in that you specify a source (where the file is coming from) and destination (where the file is going to).

Unless you have your paths memorized, the easiest way to do this is to have two terminals open. One logged into the ORCD system you are transferring files to or from, one not logged in. In each navigate to the respective directories where the file exists or you want to transfer it to. In the local tab navigate to where you want to put the transferred file or to to the file you want to transfer. In the ORCD system tab use the `pwd` command to print out the path to your current location. You can use this to run the `scp` or `rsync` command.

### scp

First, open a terminal on your computer (not logged into any ORCD system).

To transfer a file from your local computer to an ORCD system you would use the command:

=== "Engaging"

    ``` bash
    scp <file-name> USERNAME@orcd-login001.mit.edu:<path-to-engaging-dir>
    ```

=== "Satori"

    ``` bash
    scp <local-file-name> USERNAME@satori-login-001.mit.edu:<path-to-satori-dir>
    ```
=== "OpenMind"

    ``` bash
    scp <local-file-name> USERNAME@openmind-dtn.mit.edu:<path-to-openmind-dir>
    ```

=== "SuperCloud"

    ``` bash
    scp <local-file-name> USERNAME@txe1-login.mit.edu:<path-to-supercloud-dir>
    ```

For example, let's say you have the local file `myscript.py` and you want to transfer it to the directory `mycode` in your home directory. The command would be:

=== "Engaging"

    ``` bash
    scp myscript.py USERNAME@orcd-login001.mit.edu:/home/USERNAME/mycode/
    ```

=== "Satori"

    ``` bash
    scp  myscript.py USERNAME@satori-login-001.mit.edu:/home/USERNAME/mycode/
    ```
=== "OpenMind"

    ``` bash
    scp  myscript.py USERNAME@openmind-dtn.mit.edu:/home/USERNAME/mycode/
    ```

=== "SuperCloud"

    ``` bash
    scp myscript.py USERNAME@txe1-login.mit.edu:/home/gridsan/USERNAME/mycode/
    ```

To transfer the other direction (from an ORCD system to your local computer) switch the order:

=== "Engaging"

    ``` bash
    scp USERNAME@orcd-login001.mit.edu:<path-to-engaging-file> <path-to-local-dir>
    ```

=== "Satori"

    ``` bash
    scp USERNAME@satori-login-001.mit.edu:<path-to-satori-file> <path-to-local-dir>
    ```
=== "OpenMind"

    ``` bash
    scp USERNAME@openmind-dtn.mit.edu:<path-to-openmind-file> <path-to-local-dir>
    ```

=== "SuperCloud"

    ``` bash
    scp USERNAME@txe1-login.mit.edu:<path-to-supercloud-file> <path-to-local-dir>
    ```

If you were to have the file `results.csv` that you want to copy from the `output` directory in your home directory to the current directory on your computer the command would be:

=== "Engaging"

    ``` bash
    scp USERNAME@orcd-login001.mit.edu:/home/USERNAME/output/results.csv .
    ```

=== "Satori"

    ``` bash
    scp USERNAME@satori-login-001.mit.edu:/home/USERNAME/output/results.csv .
    ```
=== "OpenMind"

    ``` bash
    scp USERNAME@openmind-dtn.mit.edu:/home/USERNAME/output/results.csv .
    ```

=== "SuperCloud"

    ``` bash
    scp USERNAME@txe1-login.mit.edu:/home/gridsan/USERNAME/output/results.csv .
    ```

Note the `.` in the command above means the current directory.

Similar to the `cp` command, if you want to transfer an entire directory and all of its subdirectories, use the `-r` (recursive) flag for either direction:

=== "Engaging"

    ``` bash
    scp -r <file-name> USERNAME@orcd-login001.mit.edu:<path-to-engaging-dir>
    ```

=== "Satori"

    ``` bash
    scp -r <local-file-name> USERNAME@satori-login-001.mit.edu:<path-to-satori-dir>
    ```
=== "OpenMind"

    ``` bash
    scp -r <local-file-name> USERNAME@openmind-dtn.mit.edu:<path-to-openmind-dir>
    ```

=== "SuperCloud"

    ``` bash
    scp -r <local-file-name> USERNAME@txe1-login.mit.edu:<path-to-supercloud-dir>
    ```

!!! note
    To `scp` files to/from the new login nodes on Engaging, you will need to
    authenticate with Duo.

### rsync

The use of `rsync` is very similar to `scp`, but the behavior is different. By default `rsync` will not transfer files that are identical at both the source and destination. There are additional flags you can use to specify what `rsync` should do when files differ. The `rsync` command can be very useful when you want to "sync" updates to a directory or when transferring large directories. If a transfer fails during `rsync` you can re-run the command and it will pick up where it left off, rather than re-transfer everything.

For general use, the example commands above for `scp` apply, use the same command but replace `scp` with `rsync`.

Some useful flags include:

- `-r`, `--recursive` to recursively copy files in all sub-directories
- `-l`, `--links` to copy and retain symbolic links
- `-u`, `--update` skips any files for which the destination file already exists and has a date later than the source file
- `-v`, `--verbose` prints out more information during the file transfer, add more `v`s for more information
- `--partial` keeps partially transferred files, useful when transferring large files so rsync can continue where it left off if the transfer fails
- `--progress` prints information about the progress of the transfer
- `-n`, `--dry-run` does not run the transfer but prints out what actions it would be taken, useful to avoid unintended file overwrites

You can run `rsync --help` to print out a full list of flags that can be used with the `rsync` command.

!!! note
    To `rsync` files to/from the new login nodes on Engaging, you will need to
    authenticate with Duo.

### Moving files between ORCD Systems

If you need to move files between ORCD systems you can do so one of two ways.

1. ssh to one of the ORCD systems and initiate the transfer from that system to the other. Once you are logged into one system the process is the same as if you were to transfer files to or from your own computer.
2. Run the `scp` or `rsync` command on your local system and specify the hostnames and paths for each of the source and destination systems. For example to move a file from Engaging to Satori using `scp` you would run:

```bash title="Transferring files from Engaging to Satori"
scp USERNAME@orcd-login001.mit.edu:<path-to-engaging-file> USERNAME@satori-login-001.mit.edu:<path-to-satori-dir>
```

## Graphical Applications for File Transfer

There are a few applications you can download that will allow you to transfer files with  drag-and-drop, similar to how you would move files around on your own computer.

Some of the most common options are:

- [Cyberduck](https://cyberduck.io/) (Mac and Windows)
- [FileZilla](https://filezilla-project.org/) (Mac, Windows, and Linux)
- [WinSCP](https://winscp.net/eng/index.php) (Windows only)

To use these you will need to know the hostname of the ORCD system you are accessing, either one of the login nodes or a dedicated data transfer node. See the list of hostnames at the top of this page to see which you should use for the system you are transferring files to.

## Transferring Files with a Web Portal

Most ORCD systems have some form of portal that can be accessed through your browser and used to transfer or download files. Engaging and Satori both use OnDemand. SuperCloud has its own custom portal.

- [Engaging OnDemand Portal](https://engaging-ood.mit.edu/)
- [Satori OnDemand Portal](https://satori-portal.mit.edu/)
- [SuperCloud Web Portal](https://txe1-portal.mit.edu) ([Documentation](https://mit-supercloud.github.io/supercloud-docs/transferring-files/#downloading-files-through-the-web-portal))

For documentation on how to download and transfer files on the SuperCloud Web Portal, see the link above.

If you are using Engaging or Satori, you can use the file browser by selecting Files -> Home Directory in the menu bar at the top of the page. You can drag and drop files into and out of this page or use the "Upload" and "Download" buttons. Select multiple files by holding the Control (or Command) key and clicking on the files you'd like to select. Those files can then be downloaded with the "Download" button.

## Globus

Globus is a tool that helps transfer data between designated endpoints. These transfers can be initiated through the Globus webpage, don't require staying logged in through the entire transfer, and will restart automatically if something fails during the transfer. There are endpoints on a few ORCD systems with basic Globus features. Please note that these basic Globus endpoints will transfer data unencrypted. An MIT Globus subscription with more features is coming soon!

To transfer data log into [Globus](https://www.globus.org/) with your MIT credentials. On the "File Manager" tab in one of the two "Collection" boxes search for the endpoint for the system you want to transfer data to or from. The column on the left should list where you want to transfer from, the column on the right should list where you want to transfer to. Endpoints on ORCD systems are listed below.

| System | Globus Endpoint | 
| ----------- | ----------- |
| Engaging | mithpc#engaging | 
| Satori | mithpc#satori | 
| OpenMind | mithpc#openmind | 

To transfer data to or from your own computer you will need to set up a personal endpoint. Follow the instructions on the page for your system listed [here](https://docs.globus.org/globus-connect-personal/).

More documentation on transferring files through Globus can be found on the [Globus Documentation Pages](https://docs.globus.org/guides/tutorials/manage-files/transfer-files/). Globus also has an [FAQ](https://docs.globus.org/faq/globus-connect-endpoints/) that is helpful for answering any questions you might have.

