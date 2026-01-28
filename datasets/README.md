# 📊 Datasets for Multi-Weather Image & Video Restoration

This directory provides curated benchmark datasets used in the survey:

**Clear Roads, Clear Vision: Advancements in Multi-Weather Restoration for Smart Transportation**  
(arXiv:2510.09228)

The datasets cover adverse weather conditions relevant to Intelligent Transportation Systems (ITS), including:

- 🌫️ Haze  
- 🌧️ Rain  
- ❄️ Snow  
- ☂️ Multi-weather / compound degradations  
- 🎞️ Video restoration  

This folder serves as the **practical companion** to the academic dataset summaries:
- [dehazing.md](dehazing.md)  
- [deraining.md](deraining.md)  
- [desnowing.md](desnowing.md)  
- [multiweather.md](multiweather.md)  

and provides:
- download scripts  
- preprocessing utilities  
- dataset organization guidelines  

---

## 📌 Dataset Categories

| Category | Description |
|----------|-------------|
| **Dehazing** | Image and video datasets with fog and haze degradation |
| **Deraining** | Synthetic and real rainy image datasets |
| **Desnowing** | Snow-covered scenes with paired or unpaired ground truth |
| **Multi-weather** | Compound degradations (haze + rain + snow) |
| **Video restoration** | Sequential benchmarks for temporal consistency |

---

## 📥 Download Instructions

Each dataset category provides helper scripts to download and organize data automatically.

### 🌫️ Dehazing
```bash
bash datasets/dehazing/download_reside.sh

```
### 🌧️ Deraining
```bash
datasets/deraining/download_rain.sh
```

### ❄️ Desnowing
```bash
bash datasets/desnowing/download_snow.sh
```

### ☂️ Multi-Weather
```bash
bash datasets/multiweather/download_multi.sh
```

> 📌 Please ensure sufficient disk space before downloading large-scale datasets (e.g., Snow100K, DAWN).

---

## ⚙️ Preprocessing Scripts

Some datasets require preprocessing (e.g., resizing, patch extraction, or format conversion):

```bash
python datasets/deraining/preprocess.py
```

Typical preprocessing steps include:
- Image resizing  
- Patch extraction  
- Normalization  
- Train/test split generation  

Dataset-specific preprocessing instructions are provided inside each dataset subfolder.

---

## 📊 Dataset Summary

### 🌫️ Haze Datasets

| Dataset | Type | Samples | Resolution | Reference |
|--------|------|---------|------------|-----------|
| RESIDE | Synthetic / Real | ~13,990 | 620×460 | https://sites.google.com/view/reside-dehaze-datasets |
| I-HAZE | Real | 35 | 1280×720 | https://data.vision.ee.ethz.ch/cvl/ntire18/ |
| O-HAZE | Real | 45 | 1280×720 | https://data.vision.ee.ethz.ch/cvl/ntire18/ |
| Dense-Haze | Real | 33 | 2048×1536 | https://data.vision.ee.ethz.ch/cvl/ntire19/dense-haze/ |
| NH-HAZE | Night-time Real | 55 | 2048×1536 | https://data.vision.ee.ethz.ch/cvl/ntire20/nh-haze/ |

---

### 🌧️ Rain Datasets

| Dataset | Type | Samples | Resolution | Reference |
|--------|------|---------|------------|-----------|
| Rain100H | Synthetic Rain (Heavy) | 1,800 | 512×512 | https://xueyangfu.github.io/projects/tip2017.html |
| Rain100L | Synthetic Rain (Light) | 200 | 512×512 | https://xueyangfu.github.io/projects/tip2017.html |
| RainCityscapes | Synthetic Rain | ~5,000 | 1920×1080 | https://xiaoyonghu.com/project/derain.html |
| DID-Data | Density-aware Rain | 12,000 | 512×512 | https://github.com/hezhangsprinter/DID-MDN |

---

### ❄️ Snow Datasets

| Dataset | Type | Samples | Resolution | Reference |
|--------|------|---------|------------|-----------|
| Snow100K | Synthetic Snow | 100,000 | 1024×768 | https://github.com/yxuan0525/Snow100K |
| CSD | Real + Synthetic | 13,000 | 720×480 | https://arxiv.org/abs/2206.10972 |

---

### ☂️ Multi-Weather Datasets

| Dataset | Type | Samples | Resolution | Reference |
|--------|------|---------|------------|-----------|
| DAWN | Multi-weather | 10,000 | Varies | https://github.com/vis-opt/DAWN |
| Realistic MW | Multi-weather | 2,500+ | Varies | — |

---

### 🎞️ Video Datasets

| Dataset | Type | Samples | Resolution | Reference |
|--------|------|---------|------------|-----------|
| REVIDE | Real Video Dehazing | 500+ | 720×480 | https://github.com/liruizhe/REVIDE |
| NTIRE Video Challenges | Multi-type | 1,000+ | Varies | https://data.vision.ee.ethz.ch/cvl/ntire22/ |

---

## 📁 Folder Structure

```text
datasets/
├── dehazing/
│   └── RESIDE/
├── deraining/
│   └── RainCityscapes/
├── desnowing/
│   └── Snow100K/
└── multiweather/
    └── DAWN/
```

Each dataset subfolder should contain:
- Original data  
- Preprocessing scripts  
- A local `README.md` with license and citation  

---

## ⚠️ Licensing & Usage

Each dataset is distributed under its own license defined by the original authors.

Users must:
- Follow dataset-specific license terms  
- Cite the corresponding papers  
- Use the data for research and non-commercial purposes unless explicitly permitted  

Please refer to the `README.md` inside each dataset directory for detailed license information.

---

## 🔗 Related Pages
- [taxonomy.md](../taxonomy.md)  
- [datasets/dehazing.md](dehazing.md)  
- [datasets/deraining.md](deraining.md)  
- [datasets/desnowing.md](desnowing.md)  
- [datasets/multiweather.md](multiweather.md)  
- [benchmarks/image_results.md](../benchmarks/image_results.md)  

---

## 📌 Citation

```bibtex
@article{clearroads_multiweather_restoration,
  title   = {Clear Roads, Clear Vision: Advancements in Multi-Weather Restoration for Smart Transportation},
  author  = {Galshetwar, Vijay M. and Hambarde, Praful and Patil, Prashant W. and Vipparathi, Santosh Kumar and Dudhane, Akshay and Murala, Subrahmanyam and Chaudhary, Sachin},
  journal = {arXiv preprint arXiv:2510.09228},
  year    = {2025},
  url     = {https://arxiv.org/abs/2510.09228}
}
```

---

## ⭐ Acknowledgment

We gratefully acknowledge the authors and dataset contributors whose open benchmarks enable progress in multi-weather image and video restoration research.

