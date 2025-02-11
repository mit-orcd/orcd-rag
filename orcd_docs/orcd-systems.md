---
tags:
 - Engaging
 - Satori
 - SuperCloud
---

# ORCD Systems

ORCD operates and provides support and training for a number of cluster computer systems available to all researchers. These systems all run with a Slurm scheduler and most have a web portal for interactive computing. These are Engaging, SuperCloud, Satori, and OpenMind.

## Maintenance Schedule

With the exception of SuperCloud, the maintenance schedule for all ORCD systems is:

- Monthly downtimes on the 3rd Tuesday of the month lasting about a day.
- Weekly restarts of login nodes Monday mornings starting at 7am for about 15 minutes. If Monday is a holiday this restart will occur on Tuesday.

SuperCloud has monthly downtimes on the 2nd Tuesday of each month.

## Engaging Cluster

<!--
Does engaging have newer GPUs than Voltas now?
-->

The Engaging cluster is a mixed CPU and GPU computing cluster that is openly available to all 
research projects at MIT. It has around 80,000 x86 CPU cores and 300 
GPU cards ranging from K80 generation to recent Voltas. Hardware access is through the Slurm 
resource scheduler that supports batch and interactive workloads and allows dedicated reservations.
The cluster has a large shared file system for working datasets. Additional compute and storage 
resources can be purchased by PIs. A wide range of standard software is available and the Docker 
compatible Singularity container tool is supported. User-level tools like Anaconda for Python, 
R libraries, and Julia packages are all supported. A range of PI group maintained custom software 
stacks are also available through the widely adopted environment modules toolkit. A standard, 
open-source, web-based portal supporting Jupyter notebooks, R studio, Mathematica, and X graphics 
is available at [https://engaging-ood.mit.edu](https://engaging-ood.mit.edu). Further information and support is available from <orcd-help-engaging@mit.edu>.

### How to Get an Account on Engaging

Accounts on the engaging cluster are connected to your main MIT institutional kerberos id. 
Connecting to the cluster for the first time through its [web portal](https://engaging-ood.mit.edu) automatically activates an account with basic access to resources. See [this page](accessing-orcd/ondemand-login.md) for instructions on how to log in.

### Engaging Quick Links

- Additional Documentation: [https://engaging-web.mit.edu/eofe-wiki/](https://engaging-web.mit.edu/eofe-wiki/)
- OnDemand web portal: [https://engaging-ood.mit.edu](https://engaging-ood.mit.edu)
- Help: Send email to <orcd-help-engaging@mit.edu>

## Satori

Satori is an IBM Power 9 large memory node system. It is open to everyone on campus and has 
optimized software stacks for machine learning and for image stack post-processing for 
MIT.nano Cryo-EM facilities. The system has 256 NVidia Volta GPU cards attached in groups of 
four to 1TB memory nodes and a total of 2560 Power 9 CPU cores. Hardware access is through the 
Slurm resource scheduler that supports batch and interactive workloads and allows dedicated 
reservations. A wide range of standard software is available and the Docker compatible 
Singularity container tool is supported. A standard web based portal 
[https://satori-portal.mit.edu](https://satori-portal.mit.edu) with Jupyter notebook support is available. Additional compute and storage resources can be purchased by PIs and integrated into the system. Further 
information and support is available at <orcd-help-satori@mit.edu>

### How to Get an Account on Satori

You can get an account by logging into [https://satori-portal.mit.edu](https://satori-portal.mit.edu) with your MIT credentials. This automatically activates an account with basic access to resources. See [this page](https://mit-satori.github.io/satori-basics.html#how-can-i-get-an-account) for more information.

### Satori Quick Links

- Documentation: [https://mit-satori.github.io/](https://mit-satori.github.io/)
- OnDemand web portal: [https://satori-portal.mit.edu](https://satori-portal.mit.edu)
- Help: Send email to <orcd-help-satori@mit.edu>

## SuperCloud

The SuperCloud system is a collaboration with MIT Lincoln Laboratory on a shared facility that 
is optimized for streamlining open research collaborations with Lincoln Laboratory. The facility 
is open to everyone on campus. The latest SuperCloud system has more than 16,000 x86 CPU cores 
and more than 850 NVidia Volta GPUs in total. Hardware access is through the Slurm resource 
scheduler that supports batch and interactive workloads and allows dedicated reservations. A wide 
range of standard software is available and the Docker compatible Singularity container tool is 
supported. User-level tools like Anaconda for Python, R libraries, and Julia packages are all supported. A custom, web-based portal supporting Jupyter notebooks is available at
[https://txe1-portal.mit.edu/](https://txe1-portal.mit.edu/). Further information and support is available at <supercloud@mit.edu>.

### How to Get an Account on SuperCloud

To request a SuperCloud account follow the instructions on SuperCloud's [Requesting an Account](https://supercloud.mit.edu/requesting-account) page.

### SuperCloud Quick Links

- Documentation: [https://supercloud.mit.edu/](https://supercloud.mit.edu/)
- Online Course: [https://learn.llx.edly.io/course/practical-hpc/](https://learn.llx.edly.io/course/practical-hpc/)
- Web portal: [https://txe1-portal.mit.edu/](https://txe1-portal.mit.edu/)
- Help: Send email to <supercloud@mit.edu>

## OpenMind

The OpenMind system is a collaboration with Department of Brain and Cognitive Sciences (BCS) and McGovern Institute. OpenMind is mainly a GPU computing cluster optimized for artificial intelligence (AI) research and data science. Totally there are around 70 compute nodes, 3500 CPU cores, 48 TB of RAM, and 340 GPUs, including 142 A100-80GB GPUs. It also provides around 2 PB of flash storage supporting fast read/write data speed. Hardware access is through the Slurm resource scheduler that supports batch and interactive workload and allows dedicated reservations. A wide range of standard software is available and Docker compatible Apptainer/Singularity container tool is supported. User-level tools like Anaconda for Python, R libraries, and Julia packages are all supported. Further information and support is available at <orcd-help-openmind@mit.edu>.

### How to Get an Account on OpenMind
Accounts will be available for MIT users in 2024.

### OpenMind Quick Links

- Documentation: [https://github.mit.edu/MGHPCC/OpenMind/wiki](https://github.mit.edu/MGHPCC/OpenMind/wiki)
- Home Page and Online Course: [https://openmind.mit.edu/](https://openmind.mit.edu/)
- Help: Send email to <orcd-help-openmind@mit.edu>
- Slack: [https://openmind-46.slack.com](https://openmind-46.slack.com)

