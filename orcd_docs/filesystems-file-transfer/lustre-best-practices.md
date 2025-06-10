# Lustre Best Practices

!!! note "Lustre will be Retired"
    We are in the process of migrating all lustre storage to a new flash Scratch filesystem. This page applies if you still have storage on `/nobackup1`. While these are all good general best practices, not everything on this page is relevant to the new Scratch storage.

Lustre is a type of file system technology used on the engaging cluster, known to most users as the `/nobackup1b` or `/nobackup1c` file systems. The Lustre storage system is built to manage extremely high rates of input and output, and can read and write large files faster than traditional storage like NFS, the home directory.

Since it is designed to read and write large files, it has difficulties running jobs that read and write lots of small files. When Lustre is faced with many small file input and output, it can get overloaded and in return responds very slowly across the entire filesystem, effecting more than just the user who is running the job with small file input and output.

Along with avoiding small file input and output, there are a few other things users should know to avoid when using the Lustre file system (`nobackup1b`/`nobackup1c`)

## Avoid using the command `ls -l`

The `ls -l` command displays a lot of information such as ownership, permissions, and the size of files and directories. Some of this information, such as the file size, is only stored in part of the Lustre technology, and so this information must be queried for all files and directories on the file system. This can be very resource consuming and take a long time to complete since many files are stored on `/nobackup1b` and `/nobackup1c` by many users.

Instead of using `ls -l`, you should:

- Use `ls` by itself if you just want to see if a file exists
- Use `ls -l <filename>` if you want the long listing of a specific file

## Avoid having a Large Number of Files in a Single Directory

Opening a file keeps a lock on the parent directory. When many files in the same directory are to be opened, it creates contention. A better practice is to split a large number of files (in the thousands or more) into multiple subdirectories to minimize contention.

## Avoid Storing and Accessing Small Files on Lustre

Accessing small files on the Lustre filesystem is not efficient. There are 2 other locations users can store smaller sized files that are much better suited to handle them. These locations are Pool and the user’s Home Directory. For more information on these storage locations, please see the page on [General Use Filesystems](filesystems.md).

To limit users storing lots of small files on `/nobackup1b` or `/nobackup1c`, there is a inode quota of 50k on these locations. An inode is a file, directory, or symlink, since all *unix systems treat these inodes the same in terms of permissions and storage.

To check how much of your quota you have used, you can use the command:

```bash
lfs quota -h -u <username> /nobackup1
```

## Avoid Accessing and Running Executable Files from Lustre

Executables run slower when they are run from `/nobackup1`, and shouldn’t be run from login or head nodes, regardless if they are ran from `/nobackup1`, Pool, or a user’s Home Directory. To learn how to run on Engaging, see the section on [Running Jobs](../running-jobs/overview.md).

Executable files for jobs are best stored in a user’s home directory. Storing executable files in Pool is also acceptable, but less ideal. Input data, such as datasets or input files, can be stored on `/nobackup1` and your job can generate any large data output to `/nobackup1`. Any files you need to keep long term should also be stored in Home, Pool, or another backed up location. Anything stored in a location that is not backed up, such as `/nobackup1`, has some risk of being lost.

## Avoid Having Multiple Processes Open the Same File(s) at the Same Time

On Lustre filesystems, if multiple processes try to open the same file(s), some processes will not able to find the file(s) and your job will fail.
