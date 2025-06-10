# Engaging Public Partitions

#### mit_normal

| Nodes | Cores | Memory | CPU model                        | Misc. features | Node list                   |
| ----- | ----- | ------ | -------------------------------- | -------------- | --------------------------- |
| 6     | 2x96  | 1510GB | AMD EPYC 9654 96-Core Processor  |                | node1620-1625               |
| 2     | 2x32  | 376GB  | AMD EPYC 9384X 32-Core Processor | high_l3        | node2704-2705               |
| 32    | 2x48  | 376GB  | AMD EPYC 9474F 48-Core Processor |                | node1600-1619;node3103-3114 |
| 12    | 2x48  | 377GB  | AMD EPYC 9474F 48-Core Processor |                | node3303-3314               |

#### mit_preemptable (CPU)

| Nodes | Cores | Memory | CPU model                        | Misc. features | Node list                                                                           |
| ----- | ----- | ------ | -------------------------------- | -------------- | ----------------------------------------------------------------------------------- |
| 2     | 2x48  | 1510GB | AMD EPYC 9474F 48-Core Processor |                | node3612-3613                                                                       |
| 6     | 2x96  | 1510GB | AMD EPYC 9654 96-Core Processor  |                | node1620-1625                                                                       |
| 48    | 2x48  | 376GB  | AMD EPYC 9474F 48-Core Processor |                | node1600-1619;node1626-1631;node2503-2513;node2523-2525;node3602-3607;node3610-3611 |
| 2     | 2x48  | 754GB  | AMD EPYC 9474F 48-Core Processor |                | node3608-3609                                                                       |

#### mit_preemptable (GPU)

| Nodes | Cores | Memory | CPU model                              | GPUs | GPU type              | GPU memory | Misc. features | Node list                                                                                                                         |
| ----- | ----- | ------ | -------------------------------------- | ---- | --------------------- | ---------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 2     | 2x32  | 1006GB | INTELR XEONR PLATINUM 8562Y+           | 4    | NVIDIA L40S           | 44GB       |                | node2643-2644                                                                                                                     |
| 3     | 2x32  | 1006GB | IntelR XeonR Platinum 8462Y+           | 4    | NVIDIA H100 80GB HBM3 | 79GB       |                | node2640-2642                                                                                                                     |
| 1     | 2x32  | 1007GB | INTELR XEONR PLATINUM 8562Y+           | 3    | NVIDIA L40S           | 44GB       |                | node3502                                                                                                                          |
| 48    | 2x32  | 1007GB | INTELR XEONR PLATINUM 8562Y+           | 4    | NVIDIA L40S           | 44GB       |                | node2804;node3002-3008;node3202-3208;node3302;node3402-3408;node3500-3501;node3503-3512;node4102-4103;node4105-4108;node4200-4206 |
| 1     | 2x32  | 1007GB | IntelR XeonR Platinum 8462Y+           | 4    | NVIDIA H100 80GB HBM3 | 79GB       |                | node2906                                                                                                                          |
| 8     | 2x32  | 2014GB | IntelR XeonR Platinum 8462Y+           | 4    | NVIDIA H100 80GB HBM3 | 79GB       |                | node1702-1703;node1802-1803;node2702-2703;node2802-2803                                                                           |
| 10    | 2x60  | 2014GB | INTELR XEONR PLATINUM 8580             | 8    | NVIDIA H200           | 140GB      |                | node2433-2434;node3000;node3100-3101;node3200-3201;node3300-3301;node3400                                                         |
| 4     | 2x20  | 502GB  | IntelR XeonR Silver 4316 CPU @ 2.30GHz | 4    | NVIDIA A100 80GB PCIe | 80GB       |                | node2414-2417                                                                                                                     |
| 14    | 2x64  | 502GB  | AMD EPYC 7763 64-Core Processor        | 4    | NVIDIA A100-SXM4-80GB | 80GB       |                | node1917-1918;node2100-2104;node2119;node2300-2304;node2319                                                                       |

#### mit_quicktest

| Nodes | Cores | Memory | CPU model                        | Misc. features | Node list     |
| ----- | ----- | ------ | -------------------------------- | -------------- | ------------- |
| 6     | 2x96  | 1510GB | AMD EPYC 9654 96-Core Processor  |                | node1620-1625 |
| 20    | 2x48  | 376GB  | AMD EPYC 9474F 48-Core Processor |                | node1600-1619 |

#### mit_normal_gpu

| Nodes | Cores | Memory | CPU model                    | GPUs | GPU type              | GPU memory | Misc. features | Node list                                                                                                                         |
| ----- | ----- | ------ | ---------------------------- | ---- | --------------------- | ---------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 1     | 2x32  | 1007GB | INTELR XEONR PLATINUM 8562Y+ | 3    | NVIDIA L40S           | 44GB       |                | node3502                                                                                                                          |
| 48    | 2x32  | 1007GB | INTELR XEONR PLATINUM 8562Y+ | 4    | NVIDIA L40S           | 44GB       |                | node2804;node3002-3008;node3202-3208;node3302;node3402-3408;node3500-3501;node3503-3512;node4102-4103;node4105-4108;node4200-4206 |
| 1     | 2x32  | 1007GB | IntelR XeonR Platinum 8462Y+ | 4    | NVIDIA H100 80GB HBM3 | 79GB       |                | node2906                                                                                                                          |
| 10    | 2x60  | 2014GB | INTELR XEONR PLATINUM 8580   | 8    | NVIDIA H200           | 140GB      |                | node2433-2434;node3000;node3100-3101;node3200-3201;node3300-3301;node3400                                                         |

