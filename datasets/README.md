
# 📁 Datasets for Multi-Weather Restoration

This folder contains links and descriptions for datasets referenced in the paper and used in our implementations.

## 🌫️ Hazy Image Datasets
| Name        | Type       | Description                             | Link |
|-------------|------------|-----------------------------------------|------|
| RESIDE      | Synthetic  | Large-scale benchmark for dehazing      | [Download](https://sites.google.com/site/reside-dehazing/) |
| O-HAZE      | Real-world | Outdoor scenes under natural haze       | [Download](https://data.vision.ee.ethz.ch/cvl/ntire19/ohaze/) |
| NH-HAZE     | Real-world | Non-homogeneous haze dataset            | [Download](https://data.vision.ee.ethz.ch/cvl/ntire20/nh-haze/) |

## 🌧️ Rainy Image Datasets
| Name            | Type       | Description                               | Link |
|-----------------|------------|-------------------------------------------|------|
| RainCityscapes  | Synthetic  | Rain overlay on Cityscapes dataset        | [Download](https://www.cs.cmu.edu/~yichengz/raincgan/) |
| Rain100H        | Synthetic  | Heavy synthetic rain streaks              | [Download](https://github.com/hongwang01/ID-CGAN/tree/master/datasets) |
| DID-MDN         | Synthetic  | Diverse rain intensities                  | [Download](https://github.com/hezhangsprinter/DID-MDN) |

## ❄️ Snowy Image Datasets
| Name       | Type       | Description                           | Link |
|------------|------------|---------------------------------------|------|
| Snow100K   | Synthetic  | Snow overlay with varied intensity    | [Download](https://xueyangfu.github.io/projects/Snow100K/) |
| SnowKITTI  | Synthetic  | KITTI with snow degradation           | [Download](https://github.com/SnowVision/SnowKITTI) |

## 🎥 Video Datasets
| Name       | Type       | Description                          | Link |
|------------|------------|--------------------------------------|------|
| REVIDE     | Real-world | Real video dehazing                  | [Download](https://github.com/chaofanwu/REVIDE) |
| DAVIS-2016 | Synthetic  | Segmentation videos adapted for fog  | [Download](https://davischallenge.org/davis2016/) |
| SRRS       | Real-world | Real-world desnowing sequences       | [Download](https://github.com/LabShuHangGu/SRRS) |

> 📦 Place downloaded datasets in the respective subfolders: `datasets/dehazing/`, `datasets/deraining/`, etc.
