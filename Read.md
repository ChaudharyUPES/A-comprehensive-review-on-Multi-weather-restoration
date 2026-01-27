# 🚗 Clear Roads, Clear Vision
### 🌦️ Multi-Weather Image & Video Restoration for Smart Transportation (Survey Companion)

Welcome to the official repository accompanying our survey paper:

**“Clear Roads, Clear Vision: Advancements in Multi-Weather Restoration for Smart Transportation”**  
Vijay M. Galshetwar, Praful Hambarde, Prashant W. Patil, Santosh Kumar Vipparathi, Akshay Dudhane, Subrahmanyam Murala, and Sachin Chaudhary  
📌 *Manuscript submitted to IEEE Transactions on Intelligent Transportation Systems*  :contentReference[oaicite:1]{index=1}

---

## 📘 About This Repository

Adverse weather conditions such as **haze, rain, and snow** significantly degrade images/videos used in **Intelligent Transportation Systems (ITS)** (e.g., autonomous driving, traffic monitoring, surveillance). This repository provides a **curated, regularly updated companion** to our survey, including:

- Categorized literature: **prior-based → CNN/GAN → Transformer/SSM → Diffusion → Vision-Language (VLM)**
- Restoration scope taxonomy: **single-task**, **multi-task/multi-weather**, **all-in-one**
- **Day/night** and **image/video** restoration coverage
- Datasets, evaluation metrics, and common loss functions (as summarized in the paper)  :contentReference[oaicite:2]{index=2}

---

## 🎯 Scope (as in the paper)

We cover restoration methods for:
- **Dehazing**, **Deraining**, **Desnowing** (image + video)
- **Multi-weather (multi-task)** restoration (haze/rain/snow jointly)
- **All-in-one** restoration (weather + other degradations like noise/blur/low-light)
- **Daytime & nighttime** restoration challenges
- ITS-facing requirements: **robustness, real-time efficiency, temporal consistency**  :contentReference[oaicite:3]{index=3}

---

## 🧠 Taxonomy Used in This Repo

### A) By Restoration Scope
1. **Single-task models** (specialized: haze OR rain OR snow)
2. **Multi-task / Multi-weather models** (fine-tuned / evaluated across multiple weather types)
3. **All-in-one models** (trained once on mixed degradations; deploy without task-specific tuning)  :contentReference[oaicite:4]{index=4}

### B) By Model Family
- Traditional / Prior-based
- CNN / GAN
- Transformer
- State Space Models (SSM/Mamba)
- Diffusion / Generative
- Vision-Language Models (VLM) & prompt-based
- Agentic / planning-driven restoration (emerging)  :contentReference[oaicite:5]{index=5}

---

## 📚 Categorized Restoration Literature

> **Note:** The lists below are representative (as in your current README).  
> We are aligning the full repo to the paper’s structure and will expand these into dedicated files/tables.

### 🌫️ Dehazing (Image/Video)
| Paper Title | Link |
| --- | --- |
| DehazeNet: An End-to-End System for Single Image Haze Removal | https://doi.org/10.1109/TIP.2016.2537790 |
| AOD-Net: All-in-One Dehazing Network | https://doi.org/10.1109/TIP.2017.2735468 |
| Single Image Haze Removal Using Dark Channel Prior | https://doi.org/10.1109/TPAMI.2009.161 |
| Restormer: Efficient Transformer for High-Resolution Image Restoration | https://doi.org/10.1109/ICCV48922.2021.00468 |
| FFA-Net: Feature Fusion Attention Network for Single Image Dehazing | https://doi.org/10.1007/978-3-030-58545-7_15 |

---

### 🌧️ Deraining (Image/Video)
| Paper Title | Link |
| --- | --- |
| Deep Joint Rain Detection and Removal from a Single Image | https://doi.org/10.1109/CVPR.2017.561 |
| Density-aware Image Deraining using a Multi-stream Dense Network | https://doi.org/10.1109/CVPR.2018.00611 |
| Spatial Attentive Single-Image Deraining with a High Quality Real Rain Dataset | https://doi.org/10.1109/ICCV.2019.01220 |
| Multi-Scale Progressive Fusion Network for Single Image Deraining | https://openaccess.thecvf.com/content/ICCV2021/html/Hu_Single_Image_Deraining_via_a_Multi-Scale_Progressive_Fusion_Network_ICCV_2021_paper.html |

---

### ❄️ Desnowing (Image/Video)
| Paper Title | Link |
| --- | --- |
| DesnowNet: Context-Aware Deep Network for Snow Removal | https://doi.org/10.1109/TIP.2017.2735474 |
| SnowFormer: A Transformer-Based Framework for Snow Removal | https://openaccess.thecvf.com/content/CVPR2022/html/Liu_SnowFormer_A_Transformer-Based_Framework_for_Snow_Removal_CVPR_2022_paper.html |
| MSP-Former: Multi-Stage Progressive Transformer for Single Image Desnowing | https://openaccess.thecvf.com/content/CVPR2023/html/Liu_MSP-Former_Multi-Stage_Progressive_Transformer_for_Single_Image_Desnowing_CVPR_2023_paper.html |

---

## ☂️ Multi-Weather Restoration (Multi-task)

### Image
| Paper Title | Link |
| --- | --- |
| MWFormer: Multi-weather Transformer | https://arxiv.org/abs/2312.12967 |
| Gated Context Aggregation Network | https://ieeexplore.ieee.org/document/10157390 |
| General/Specific Weather Restoration Framework | https://arxiv.org/abs/2308.12241 |

### Video
| Paper Title | Link |
| --- | --- |
| Video Restoration via Matrix Decomposition | https://ieeexplore.ieee.org/document/9093415 |
| Dual Spatio-Temporal Transformer Network | https://arxiv.org/abs/2404.15338 |
| Meta-Adaptation Framework | https://ieeexplore.ieee.org/document/9894307 |

---

## 🧠 All-in-One Restoration (Unified Degradation Handling)

### Prompt / Language Guided
| Paper Title | Link |
| --- | --- |
| PromptIR: Prompting for All-in-One Image Restoration | https://proceedings.neurips.cc/paper_files/paper/2023/hash/2e9f1b0b25b8e9c3d2a6a87a8b3d3e0f-Abstract-Conference.html |
| Language-Driven All-in-One Restoration | https://arxiv.org/abs/2402.01149 |
| DPMambaIR: Degradation-Aware Prompt State Space Model | https://arxiv.org/abs/2403.15459 |

### Transformer / Diffusion / Others
| Paper Title | Link |
| --- | --- |
| TransWeather: Transformer-based Restoration of Images Degraded by Adverse Weather | https://doi.org/10.1109/CVPR.2022.00106 |
| AutoDIR: Automatic All-in-One Image Restoration with Latent Diffusion | https://arxiv.org/abs/2311.17028 |
| NAS-AIOIR: All in One Bad Weather Removal Using Architectural Search | https://openaccess.thecvf.com/content_CVPR_2020/html/Li_All_in_One_Bad_Weather_Removal_Using_Architectural_Search_CVPR_2020_paper.html |

---

## 📈 Datasets & Benchmarks (Aligned with the Paper)

We summarize benchmark datasets (synthetic & real) and evaluation protocols as detailed in the survey:
- **Dehazing datasets** (Table I)
- **Deraining datasets** (Table II)
- **Desnowing datasets** (Table III)  :contentReference[oaicite:6]{index=6}

**Planned repo structure (coming as separate pages):**
- `datasets/dehazing.md`
- `datasets/deraining.md`
- `datasets/desnowing.md`
- `benchmarks/image_results.md`
- `benchmarks/video_results.md`

---

## 📏 Metrics & 🧮 Loss Functions

As covered in the paper:
- **Reference metrics:** PSNR, SSIM, LPIPS, FID
- **No-reference metrics:** NIQE, BRISQUE, PIQE, Entropy
- **Video stability / temporal:** temporal warping error (TWE), inter-frame consistency
- **Common losses:** L1/L2/Charbonnier, edge loss, perceptual loss, adversarial loss, weather classification loss  :contentReference[oaicite:7]{index=7}

(Repo page planned: `losses_and_metrics.md`)

---

## 🤖 Emerging Direction: Agentic AI Restoration

The survey highlights a shift toward **planning-driven / agent-based restoration** for compound degradations and better generalization, including multi-agent scheduling and LLM-guided restoration pipelines.  :contentReference[oaicite:8]{index=8}

(Repo page planned: `agentic_ai.md`)

---

## ✍️ Citation

If you use this repository, please cite:

```bibtex
@article{clearroads_clearvision_multiweather_restoration,
  title   = {Clear Roads, Clear Vision: Advancements in Multi-Weather Restoration for Smart Transportation},
  author  = {Galshetwar, Vijay M. and Hambarde, Praful and Patil, Prashant W. and Vipparathi, Santosh Kumar and Dudhane, Akshay and Murala, Subrahmanyam and Chaudhary, Sachin},
  journal = {IEEE Transactions on Intelligent Transportation Systems},
  year    = {2026},
  note    = {Manuscript submitted}
}
