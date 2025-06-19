# 🌦️ Multi-Weather Datasets

This section includes curated datasets for haze, rain, snow, and multi-weather conditions used in benchmarking image restoration models for transportation and adverse weather scenarios.

---

## 📥 Download Instructions

Each dataset has a helper script to download and organize the files in the correct folder structure.

### 🔸 Dehazing

```bash
bash datasets/dehazing/download_reside.sh
```

### 🔸 Deraining

```bash
bash datasets/deraining/download_rain.sh
```

### 🔸 Desnowing

```bash
bash datasets/desnowing/download_snow.sh
```

### 🔸 Multi-Weather Combined

```bash
bash datasets/multi-weather/download_multi.sh
```

---

## ⚙️ Preprocessing Scripts

For certain datasets (e.g., RainCityscapes), preprocessing may be required such as resizing or patch extraction:

```bash
# Resize images or convert to model-compatible format
python datasets/deraining/preprocess.py
```

---

## 📊 Dataset Summary

### 🌫 Haze Datasets

| Dataset         | Type           | Samples  | Resolution | Citation                                                                 |
| --------------- | -------------- | -------- | ---------- | ------------------------------------------------------------------------ |
| RESIDE          | Synthetic Hazy | \~13,990 | 620×460    | [Li et al., 2018](https://sites.google.com/view/reside-dehaze-datasets/) |
| I-HAZE / O-HAZE | Real Hazy      | 35 / 45  | 1280×720   | [Ancuti et al., 2018](https://data.vision.ee.ethz.ch/cvl/ntire18/)       |
| HazeRD          | Real Hazy      | 2,220    | Varies     | [Zhang et al., 2017](https://github.com/ygjwd12345/HazeRD)               |
| D-HAZY          | Depth-Hazy     | 1,449    | 640×480    | [Ancuti et al., 2016](https://www.ut.ee/~dch/d-hazy/)                    |

### 🌧 Rain Datasets

| Dataset        | Type                   | Samples | Resolution | Citation                                                               |
| -------------- | ---------------------- | ------- | ---------- | ---------------------------------------------------------------------- |
| Rain100H       | Synthetic Rain         | 1,800   | 512×512    | [Yang et al., 2017](https://xueyangfu.github.io/projects/tip2017.html) |
| Rain100L       | Synthetic Rain (Light) | 200     | 512×512    | [Yang et al., 2017](https://xueyangfu.github.io/projects/tip2017.html) |
| Rain800        | Synthetic Rain         | 800     | 500×500    | [Zhang et al., 2019](https://github.com/hezhangsprinter/DID-MDN)       |
| RainCityscapes | Synthetic Rain         | \~5,000 | 1920×1080  | [Hu et al., 2019](https://xiaoyonghu.com/project/derain.html)          |
| DID-Data       | Rainy (Density)        | 12,000  | 512×512    | [Zhang et al., 2018](https://github.com/hezhangsprinter/DID-MDN)       |

### ❄️ Snow Datasets

| Dataset  | Type             | Samples | Resolution | Citation                                                  |
| -------- | ---------------- | ------- | ---------- | --------------------------------------------------------- |
| Snow100K | Synthetic Snow   | 100,000 | 1024×768   | [Liu et al., 2019](https://github.com/yxuan0525/Snow100K) |
| CSD      | Real + Synthetic | 13,000  | 720×480    | [Liu et al., 2022](https://arxiv.org/abs/2206.10972)      |

### 🧠 All-in-One / Blur Datasets

| Dataset | Type                 | Samples | Resolution | Citation                                                                                                                           |
| ------- | -------------------- | ------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| BID     | Blurred (All-in-One) | 586     | 700×700    | [Caraffa et al., 2015](https://openaccess.thecvf.com/content_cvpr_2015/html/Caraffa_Multi-View_Structure_And_2015_CVPR_paper.html) |

### ☂️ Multi-Weather Datasets

| Dataset      | Type          | Samples | Resolution | Citation                                             |
| ------------ | ------------- | ------- | ---------- | ---------------------------------------------------- |
| DAWN         | Multi-Weather | 10,000  | Varies     | [Wang et al., 2022](https://github.com/vis-opt/DAWN) |
| Realistic MW | Multi-Weather | 2,500+  | Varies     | –                                                    |

### 🎞️ Video Datasets

| Dataset   | Type                | Samples | Resolution | Citation                                                        |
| --------- | ------------------- | ------- | ---------- | --------------------------------------------------------------- |
| REVIDE    | Real Video Dehazing | 500+    | 720×480    | [Li et al., 2021](https://github.com/liruizhe/REVIDE)           |
| NTIRE2021 | Video (Multi-Type)  | 1,000+  | Varies     | [Nah et al., 2021](https://data.vision.ee.ethz.ch/cvl/ntire21/) |

> 📝 *More details such as splits, augmentation, and usage guidelines are available in each dataset subfolder.*

---

## 📁 Folder Structure

Place all downloaded datasets in the following directory layout:

```plaintext
datasets/
├── dehazing/
│   └── RESIDE/
├── deraining/
│   └── RainCityscapes/
├── desnowing/
│   └── Snow100K/
└── multi-weather/
    └── DAWN/
```

> 📌 For dataset licenses and citation formats, refer to the `README.md` inside each dataset subfolder.
