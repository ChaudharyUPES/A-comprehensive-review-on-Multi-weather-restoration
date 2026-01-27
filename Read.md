# 🚗 Clear Roads, Clear Vision  
## 🌦️ Multi-Weather Image & Video Restoration for Smart Transportation (Survey Companion Repository)

Welcome to the official repository accompanying our survey paper:

**Clear Roads, Clear Vision: Advancements in Multi-Weather Restoration for Smart Transportation**  
Vijay M. Galshetwar, Praful Hambarde, Prashant W. Patil, Santosh Kumar Vipparathi, Akshay Dudhane, Subrahmanyam Murala, and Sachin Chaudhary  
📌 *Manuscript submitted to IEEE Transactions on Intelligent Transportation Systems*

---

## 📘 About This Repository

Adverse weather conditions such as **haze, rain, and snow** significantly degrade image and video quality in Intelligent Transportation Systems (ITS), affecting:

- Autonomous driving  
- Traffic monitoring  
- Surveillance  
- Airport & port operations  

This repository serves as a **living companion resource** to our survey paper and provides:

- A structured taxonomy of restoration methods  
- Curated literature lists  
- Benchmark datasets  
- Evaluation metrics and loss functions  
- Emerging paradigms (Diffusion, Vision-Language Models, Agentic AI)

The repository will be **continuously updated** with newly published papers and open-source implementations.

---

## 🎯 Scope of the Survey (Aligned with the Paper)

We cover:

### Weather-specific restoration
- Dehazing  
- Deraining  
- Desnowing  

### Restoration paradigms
- **Single-task models**  
- **Multi-task / Multi-weather models**  
- **All-in-one restoration frameworks**

### Modalities
- Image restoration  
- Video restoration  

### Conditions
- Daytime  
- Nighttime  
- Mixed / compound degradations  

---

## 🧠 Taxonomy of Methods

Methods are categorized along two dimensions:

### A) By Restoration Scope
1. **Single-task models** (haze / rain / snow separately)  
2. **Multi-weather models** (joint haze–rain–snow learning)  
3. **All-in-one models** (weather + noise, blur, low-light, etc.)

### B) By Model Family
- Prior-based & traditional methods  
- CNN / GAN-based methods  
- Transformer-based methods  
- State Space Models (SSM / Mamba)  
- Diffusion & generative models  
- Vision-Language & prompt-based models  
- Agentic AI & planning-driven frameworks  

---

## 📚 Categorized Restoration Literature

> Representative examples from the survey (full lists will be expanded into structured tables).

### 🌫️ Dehazing (Image & Video)
| Paper Title | Link |
| --- | --- |
| DehazeNet: An End-to-End System for Single Image Haze Removal | https://doi.org/10.1109/TIP.2016.2537790 |
| AOD-Net: All-in-One Dehazing Network | https://doi.org/10.1109/TIP.2017.2735468 |
| Single Image Haze Removal Using Dark Channel Prior | https://doi.org/10.1109/TPAMI.2009.161 |
| Restormer: Efficient Transformer for High-Resolution Image Restoration | https://doi.org/10.1109/ICCV48922.2021.00468 |

---

### 🌧️ Deraining (Image & Video)
| Paper Title | Link |
| --- | --- |
| Deep Joint Rain Detection and Removal from a Single Image | https://doi.org/10.1109/CVPR.2017.561 |
| Density-aware Image Deraining using a Multi-stream Dense Network | https://doi.org/10.1109/CVPR.2018.00611 |
| Spatial Attentive Single-Image Deraining with a High Quality Real Rain Dataset | https://doi.org/10.1109/ICCV.2019.01220 |
| Multi-Scale Progressive Fusion Network for Single Image Deraining | https://openaccess.thecvf.com/content/ICCV2021/html/Hu_Single_Image_Deraining_via_a_Multi-Scale_Progressive_Fusion_Network_ICCV_2021_paper.html |

---

### ❄️ Desnowing (Image & Video)
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

### Prompt / Language-Guided
- PromptIR  
- Language-Driven All-in-One Restoration  
- DPMambaIR  

### Transformer / Diffusion / Others
- TransWeather  
- AutoDIR  
- NAS-AIOIR  
- Weather-Aware Mixture-of-Experts  

---

## 📊 Datasets & Benchmarks (from the Paper)

Benchmark datasets summarized in the survey:
- **Dehazing:** RESIDE, Dense-Haze, NH-HAZE, REVIDE, Night-Haze  
- **Deraining:** Rain100H/L, DID-Data, RainCityscapes, RTTS  
- **Desnowing:** Snow100K, SRRS, SnowCityscapes, SnowKITTI  

Planned repo pages:
- `datasets/dehazing.md`  
- `datasets/deraining.md`  
- `datasets/desnowing.md`  
- `benchmarks/image_results.md`  
- `benchmarks/video_results.md`  

---

## 📏 Metrics & 🧮 Loss Functions

### Metrics
- PSNR, SSIM, LPIPS, FID  
- NIQE, BRISQUE, PIQE, Entropy  
- Temporal Warping Error (TWE)  

### Losses
- L1 / L2 / Charbonnier  
- Edge loss  
- Perceptual loss  
- Adversarial loss  
- Weather classification loss  

---

## 🤖 Emerging Direction: Agentic AI Restoration

Recent work highlights **planning-driven and multi-agent restoration frameworks**:
- LLM-guided restoration  
- Multi-agent scheduling  
- Compound degradation handling  
- Zero-shot generalization  

This represents a key future direction for scalable and robust restoration in real-world ITS environments.

---

## ✍️ Citation

```bibtex
@article{clearroads_multiweather_restoration,
  title   = {Clear Roads, Clear Vision: Advancements in Multi-Weather Restoration for Smart Transportation},
  author  = {Galshetwar, Vijay M. and Hambarde, Praful and Patil, Prashant W. and Vipparathi, Santosh Kumar and Dudhane, Akshay and Murala, Subrahmanyam and Chaudhary, Sachin},
  journal = {IEEE Transactions on Intelligent Transportation Systems},
  year    = {2026},
  note    = {Manuscript submitted}
}
