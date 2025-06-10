# General Use Filesystems

Large HPC systems often have different filesystems for different purposes. ORCD systems are no different, and each have their own approach. This page documents these.

## Engaging

Users each get a Home Directory that is backed up and meant for important files. An additional larger Pool space is provided for storing larger datasets longer term. Larger Scratch space is not backed up. [Additional storage can be purchased](project-filesystems.md), and PIs can request an additional 5TB of shared Pool storage for their lab. The Scratch spaces are meant for data used in actively running jobs. It will be faster to access Scratch during your job for the majority of workloads, but it is not backed up and should not be used for long term storage. Any files that cannot be easily replaced should be stored in Home or Pool storage, or backed up outside of Engaging.

See the table below for a description of each storage space. If your account was created before January 2025 and has not yet been migrated to the new storage, select the second tab.

=== "Account Created or Migrated After Jan 2025"
    | Storage Type      | <div style="width:18em">Path</div> | Quota | Backed up | Purpose/Notes |
    | ----------- | ----------- |----------- |----------- |----------- |
    | Home Directory <br> Flash  | `/home/<username>` | 200 GB | Backed up with snapshots | Use for important files and software |
    | Pool <br> Hard Disk | `/home/<username>/orcd/pool` | 1 TB | Disaster recovery backup | Storing larger datasets |
    | Scratch <br> Flash | `/home/<username>/orcd/scratch` | 1 TB | **Not backed up** | Scratch space for I/O heavy jobs |

    !!! warning  "Scratch is Not Backed Up"
        Scratch is meant for temporary storage while running compute jobs. It is not meant for long term storage and **is not backed up**. **If you have not logged in for 6 months files in scratch will be deleted**. Any files that you would like to keep long-term should be copied onto another storage location with backup.
=== "Account Created Before Jan 2025 or Not Yet Migrated"
    | Storage Type      | <div style="width:12em">Path</div> | Quota | Backed up | Purpose/Notes |
    | ----------- | ----------- |----------- |----------- |----------- |
    | Home Directory <br> NFS  | `/home/<username>` | 100 GB | Backed up | Use for important files |
    | NFS | `/pool001/<username>` | 1 TB | Not backed up | Scratch space |
    | Lustre | `/nobackup1/<username>` | 1 TB | Not backed up | Scratch space <br> Heavy I/O jobs with few, large files |

    !!! warning  "Lustre /nobackup1 is Not Backed Up"
        /nobackup1 is meant for temporary storage while running compute jobs. It is not meant for long term storage and **is not backed up**. Any files that you would like to keep long-term should be copied onto another storage location with backup.

    !!! note "Lustre /nobackup1 performs best with fewer, larger files"
        Having large numbers of small files will make Lustre slower than NFS and can slow down the filesystem overall, so it is important to follow the [Lustre Best Practices](lustre-best-practices.md).




## Satori

| Storage Type      | Path | Quota | Backed up | Purpose/Notes |
| ----------- | ----------- |----------- |----------- |----------- |
| Home Directory | `/home/<username>` | 25GB | Backed up | Use for important files. Quota increase request to 100GB. |
| GPFS           | `/nobackup/users/<username>` | 500GB | Not backed up | Scratch space. Quota increase request to 2TB. |

## SuperCloud

SuperCloud uses Lustre for all central/shared storage (accessible to all nodes in the system). This storage is not backed up. See the SuperCloud [Best Practices and Performance Tips](https://supercloud.mit.edu/best-practices-and-performance-tips) page for best practices using the Lustre filesystem. Quotas or limits are set on the storage as guardrails. Individual and group storage use and quotas can been viewed on the [User Profile Page](https://txe1-portal.mit.edu/profile/user_profile.php) on the SuperCloud Web Portal (only accessible if you have an account). Additional storage may be granted on a case by case basis. Local disk spaces will be faster than the Lustre shared filesystem, but all are temporary and can only be accessed on the node where they are created.

| Storage Type      | Path | Access | Backed up | Limits |
| ----------- | ----------- |----------- |----------- |----------- |
| Home Directory <br> Lustre  | `/home/gridsan/<username>` | User only | Not backed up | See [User Profile Page](https://txe1-portal.mit.edu/profile/user_profile.php) |
| Group Directories <br> Lustre | `/home/gridsan/groups/<groupname>` | Files shared within a group | Not backed up | See [User Profile Page](https://txe1-portal.mit.edu/profile/user_profile.php) |
| Job-specific Temporary Storage <br> Local Disk | Access using the `$TMPDIR` environment variable | User or Group | Not backed up <br>  Temporary directory created at the start of a job and cleaned up at the end of the job | NA |
| Local Disk Space | Create the directory `/state/partition1/user/$USER` as needed | User or Group | Not backed up <br> Cleaned up monthly during downtimes | NA |

## OpenMind

OpenMind provides a number of different storage options. See the [OpenMind Documentation page on Storage](https://github.mit.edu/MGHPCC/OpenMind/wiki/Which-directory-should-I-use%3F) for more information, best practices, and recommendations.

| Storage Type      | Path | Quota | Backed up | Purpose/Notes |
| ----------- | ----------- |----------- |----------- |----------- |
| Home Directory | `/home/<username>` | 20 GB | Backed up | Use for very important files. Physically located on Flash 2. |
| Flash 1 |  `/om/user/<username>` (individual users) and `/om/group/<groupname>` (groups) | Per group | Backed up | Fast internal storage |
| Flash 1 Scratch | `/om/scratch/<week-day>` | N/A | Not backed up <br> purged 3 weeks after creation | Scratch space |
| Flash 2 | `/om2/user/<username>` (individual users) and `/om2/group/<groupname>` (groups) | Per group | Backed up | Fast internal storage |
| Flash 2 Scratch | `/om2/scratch/<week-day>` | N/A | Not backed up <br> purged 2 weeks after creation | Scratch space |
| NFS | `/om3`, `/om4`, `/om5` | Per group | Backed up | Slow internal long-term storage |
| NESE | `/nese` | Per group | Backed up | Slow internal long-term storage |
