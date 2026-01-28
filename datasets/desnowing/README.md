# ❄️ Desnowing Datasets

This page summarizes the major benchmark datasets used for **single-image and video desnowing** in the survey:

**Clear Roads, Clear Vision: Advancements in Multi-Weather Restoration for Smart Transportation**  
(arXiv:2510.09228)

The datasets are categorized based on:
- Image vs Video modality  
- Synthetic vs Real-world data  
- Snow density and occlusion complexity  

These benchmarks support:
- Training of desnowing models  
- Fair evaluation and comparison  
- Reproducible research in snowy and winter driving conditions  

---

## 📌 Dataset Categories

| Category | Description |
|----------|-------------|
| **Synthetic datasets** | Snow particles simulated on clean images |
| **Real-world datasets** | Captured under natural snowfall |
| **Mixed datasets** | Combination of real and synthetic snow |
| **Video datasets** | Snowy video sequences for temporal evaluation |

---

## 🖼️ Image Desnowing Datasets

| Dataset | Type | Size | Real / Synthetic | Description | Link |
|--------|------|------|------------------|-------------|------|
| **Snow100K** | Image | 100,000 | Synthetic | Large-scale dataset with varying snow density | https://github.com/yxuan0525/Snow100K |
| **SRRS** | Image | 3,000 | Real | Snow removal benchmark with realistic snowfall | https://github.com/hongwang01/SRRS |
| **CSD (Comprehensive Snow Dataset)** | Image | 13,000 | Mixed | Real and synthetic snow images for restoration | https://arxiv.org/abs/2206.10972 |
| **SnowCityscapes** | Image | ~2,500 | Synthetic | Snow simulation on Cityscapes for autonomous driving | https://github.com/huawei-noah/SmartCar |
| **SnowKITTI** | Image | ~1,000 | Synthetic | Snow degradation applied to KITTI dataset | https://github.com/huawei-noah/SmartCar |

---

## 🎞️ Video Desnowing Datasets

| Dataset | Type | Size | Real / Synthetic | Description | Link |
|--------|------|------|------------------|-------------|------|
| **REVIDE-Snow** | Video | 100+ sequences | Real | Real-world snowy video sequences | https://github.com/liruizhe/REVIDE |
| **NTIRE Video Snow Removal** | Video | Challenge dataset | Hybrid | Dataset from NTIRE video restoration challenges | https://data.vision.ee.ethz.ch/cvl/ntire22/ |
| **SnowVideoSet** | Video | 50+ sequences | Synthetic | Synthetic snowy videos with temporal ground truth | — |

---

## 🌙 Challenging Conditions

| Dataset | Focus | Description | Link |
|--------|-------|-------------|------|
| **SRRS** | Dense snow | Heavy snow occlusion in outdoor scenes | https://github.com/hongwang01/SRRS |
| **SnowCityscapes** | Driving scenes | Snow on road and traffic environments | https://github.com/huawei-noah/SmartCar |
| **SnowKITTI** | Autonomous driving | Snow degradation on KITTI driving scenes | https://github.com/huawei-noah/SmartCar |

---

## 📊 Evaluation Protocols

Common evaluation settings:
- **Train/Test splits:** Snow100K subsets (light / medium / heavy snow)  
- **Metrics:** PSNR, SSIM, LPIPS, NIQE  
- **Video metrics:** Temporal Warping Error (TWE)  
- **Cross-dataset testing:** Train on synthetic, test on real snow  

---

## ⚠️ Challenges & Limitations

- Snowflakes cause strong occlusion and transparency artifacts  
- Limited paired real-world snowy images  
- Snow density and shape vary significantly  
- Motion blur and wind effects complicate video desnowing  
- Night-time snow datasets remain scarce  

---

## 🚀 Future Dataset Directions

- Large-scale real-world snowy datasets with paired ground truth  
- Multi-weather datasets (snow + rain + haze)  
- Night-time and low-light snow benchmarks  
- Task-aware datasets for detection and segmentation  
- Unified image + video snow restoration benchmarks  

---

## 🔗 Related Pages
- [taxonomy.md](../taxonomy.md)  
- [datasets/dehazing.md](dehazing.md)  
- [datasets/deraining.md](deraining.md)  
- [datasets/multiweather.md](multiweather.md)  
- [benchmarks/image_results.md](../benchmarks/image_results.md)  

---

## 📌 Citation

Please cite the survey paper if you use this dataset summary:

```bibtex
@article{clearroads_multiweather_restoration,
  title   = {Clear Roads, Clear Vision: Advancements in Multi-Weather Restoration for Smart Transportation},
  author  = {Galshetwar, Vijay M. and Hambarde, Praful and Patil, Prashant W. and Vipparathi, Santosh Kumar and Dudhane, Akshay and Murala, Subrahmanyam and Chaudhary, Sachin},
  journal = {arXiv preprint arXiv:2510.09228},
  year    = {2025},
  url     = {https://arxiv.org/abs/2510.09228}
}
