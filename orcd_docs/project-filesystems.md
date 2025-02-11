# Project Specific Filesystems

## Purchasing Storage

Additional project and lab storage can be purchased on ORCD shared clusters by individual
PI groups. This storage is mounted on the cluster and access to the storage is managed 
by the group through [MIT Web Moira](https://groups.mit.edu/webmoira/) (see [below](#managing-access-using-mit-web-moira) for details).

The current options for storage are:

| Storage Type | Description | Encryption at Rest  | Backup  | Namespace |Notes | 
| ----------- | ----------- |----------- |----------- |----------- |----------- |
| Compute | Very frequent data access | Optional | No | Limited | Very fast access, special needs, high IO |
| Data | Frequent data access | Optional | No |  Limited | Day to day research storage, active projects, instrument data buffers, etc. |
| Archival | Infrequent data access | Yes | No | Nearly Unlimited | Infrequently accessed data, unlimited namespace |

Please note that all types of storage **are not backed up by default**.

Storage is charged at the start of each fiscal year. The first year is prorated by the number of months left in the current fiscal year. A purchase must be a minimum of 20 TiB and in increments of 20 TiB.

<!--

TODO: Do we need the Min/increments in the table if we list it here?
-->

If you anticipate needing more than a few 100 TiB let us know when you request your storage. We may suggest purchasing a dedicated server for your lab.

<!--

TODO: List general storage options here? Or leave it out?
archival - is "encrypted at rest", don't need to say it is NESE
No automated backup for all

(remove nese)
Storage options include NESE encrypted at rest disk. The NESE encrypted at rest disk uses a large centrally managed storage cloud at the MGHPCC
facility. Any shared ORCD cluster at the MGHPCC can access this storage. Data on NESE disk
is transparently encrypted at rest.

-->


For more information, including pricing, and to purchase storage please send an email to <orcd-help@mit.edu>. If you are purchasing storage please include the following in your request:

- The storage type (compute, data, or archival)
- Amount in TiB (20 TiB increments)
- Cost object
- The lab PI

## Managing access using MIT Web Moira

Individual group storage is configured so that access is limited to a set
of accounts belonging to a web moira list that is defined for the group
store. The owner and administrators of group storage can manage
access themselves, by modifying the membership of an associated moira list
under **https://groups.mit.edu/webmoira/list/[list_name]**. The name of the
list corresponds to the UNIX group name associated with the ORCD shared 
cluster storage.

### Moira Web Interface Example

The figure below shows a screenshot of the web moira management page at
**https://groups.mit.edu/webmoira/list/cnh_research_computing** for a hypothetical
storage group named ``cnh_research_computing``. The interface provides a 
self-service mechanism for controlling access to any storage belonging to
this group. MIT account IDs can be added and 
removed as needed from this list by the storage access administrators.

![Screen shot of Moira interface](moira-example.jpg)