# 🚗 Clear Roads, Clear Vision  
## 🌦️ Multi-Weather Image & Video Restoration for Smart Transportation  
### Survey Companion Repository

![Survey](https://img.shields.io/badge/Type-Survey-blue)
![Status](https://img.shields.io/badge/Status-Under%20Review-orange)
![Domain](https://img.shields.io/badge/Domain-Intelligent%20Transportation-green)

Welcome to the official repository accompanying our survey paper:

**Clear Roads, Clear Vision: Advancements in Multi-Weather Restoration for Smart Transportation**  
Vijay M. Galshetwar, Praful Hambarde, Prashant W. Patil, Santosh Kumar Vipparathi, Akshay Dudhane, Subrahmanyam Murala, and Sachin Chaudhary  
📌 *Manuscript under review at IEEE Transactions on Intelligent Transportation Systems*

---

## 📑 Contents
- [📘 About](#-about-this-repository)
- [🎯 Scope](#-scope-of-the-survey-aligned-with-the-paper)
- [🧠 Taxonomy](#-taxonomy-of-methods)
- [📚 Literature](#-categorized-restoration-literature)
- [📊 Datasets & Benchmarks](#-datasets--benchmarks-from-the-paper)
- [📏 Metrics & Losses](#-metrics--loss-functions)
- [🤖 Agentic AI](#-emerging-direction-agentic-ai-restoration)
- [✍️ Citation](#-citation)
- [🤝 How to Contribute](#-how-to-contribute)
- [⭐ Acknowledgment](#-acknowledgment)

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

| Dimension | Coverage |
|----------|----------|
| **Weather Types** | Dehazing · Deraining · Desnowing |
| **Restoration Paradigms** | Single-task · Multi-weather / Multi-task · All-in-one |
| **Modalities** | Image restoration · Video restoration |
| **Operating Conditions** | Daytime · Nighttime · Mixed / compound degradations |

---

## 🧠 Taxonomy of Methods

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

> 📌 **Note:** The tables below provide representative examples from each category.  
> Full paper lists corresponding to the survey tables will be maintained in dedicated subpages.

<h3>🌫️ Dehazing (Image & Video)</h3>

<table>
<tr><th width="90%">Paper Title</th><th width="10%">Link</th></tr>
<tr><td>DehazeNet: An End-to-End System for Single Image Haze Removal</td><td><a href="https://doi.org/10.1109/TIP.2016.2537790">DOI</a></td></tr>
<tr><td>AOD-Net: All-in-One Dehazing Network</td><td><a href="https://doi.org/10.1109/TIP.2017.2735468">DOI</a></td></tr>
<tr><td>Single Image Haze Removal Using Dark Channel Prior</td><td><a href="https://doi.org/10.1109/TPAMI.2009.161">DOI</a></td></tr>
<tr><td>Restormer: Efficient Transformer for High-Resolution Image Restoration</td><td><a href="https://doi.org/10.1109/ICCV48922.2021.00468">DOI</a></td></tr>
<tr><td>FFA-Net: Feature Fusion Attention Network for Single Image Dehazing</td><td><a href="https://doi.org/10.1007/978-3-030-58545-7_15">DOI</a></td></tr>
</table>

<h3>🌧️ Deraining (Image & Video)</h3>

<table>
<tr><th width="90%">Paper Title</th><th width="10%">Link</th></tr>
<tr><td>Deep Joint Rain Detection and Removal from a Single Image</td><td><a href="https://doi.org/10.1109/CVPR.2017.561">DOI</a></td></tr>
<tr><td>Density-aware Image Deraining using a Multi-stream Dense Network</td><td><a href="https://doi.org/10.1109/CVPR.2018.00611">DOI</a></td></tr>
<tr><td>Spatial Attentive Single-Image Deraining with a High Quality Real Rain Dataset</td><td><a href="https://doi.org/10.1109/ICCV.2019.01220">DOI</a></td></tr>
<tr><td>Multi-Scale Progressive Fusion Network for Single Image Deraining</td><td><a href="https://openaccess.thecvf.com/content/ICCV2021/html/Hu_Single_Image_Deraining_via_a_Multi-Scale_Progressive_Fusion_Network_ICCV_2021_paper.html">CVF</a></td></tr>
</table>

<h3>❄️ Desnowing (Image & Video)</h3>

<table>
<tr><th width="90%">Paper Title</th><th width="10%">Link</th></tr>
<tr><td>DesnowNet: Context-Aware Deep Network for Snow Removal</td><td><a href="https://doi.org/10.1109/TIP.2017.2735474">DOI</a></td></tr>
<tr><td>SnowFormer: A Transformer-Based Framework for Snow Removal</td><td><a href="https://openaccess.thecvf.com/content/CVPR2022/html/Liu_SnowFormer_A_Transformer-Based_Framework_for_Snow_Removal_CVPR_2022_paper.html">CVF</a></td></tr>
<tr><td>MSP-Former: Multi-Stage Progressive Transformer for Single Image Desnowing</td><td><a href="https://openaccess.thecvf.com/content/CVPR2023/html/Liu_MSP-Former_Multi-Stage_Progressive_Transformer_for_Single_Image_Desnowing_CVPR_2023_paper.html">CVF</a></td></tr>
</table>

<h2>☂️ Multi-Weather Restoration (Multi-task)</h2>

<h3>Image</h3>
<table>
<tr><th width="90%">Paper Title</th><th width="10%">Link</th></tr>
<tr><td>MWFormer: Multi-weather Transformer</td><td><a href="https://arxiv.org/abs/2312.12967">arXiv</a></td></tr>
<tr><td>Gated Context Aggregation Network</td><td><a href="https://ieeexplore.ieee.org/document/10157390">IEEE</a></td></tr>
<tr><td>General/Specific Weather Restoration Framework</td><td><a href="https://arxiv.org/abs/2308.12241">arXiv</a></td></tr>
</table>

<h3>Video</h3>
<table>
<tr><th width="90%">Paper Title</th><th width="10%">Link</th></tr>
<tr><td>Video Restoration via Matrix Decomposition</td><td><a href="https://ieeexplore.ieee.org/document/9093415">IEEE</a></td></tr>
<tr><td>Dual Spatio-Temporal Transformer Network</td><td><a href="https://arxiv.org/abs/2404.15338">arXiv</a></td></tr>
<tr><td>Meta-Adaptation Framework</td><td><a href="https://ieeexplore.ieee.org/document/9894307">IEEE</a></td></tr>
</table>

---

## 🧠 All-in-One Restoration (Unified Degradation Handling)

**Prompt / Language-Guided:** PromptIR · Language-Driven All-in-One Restoration · DPMambaIR  

**Transformer / Diffusion / Others:** TransWeather · AutoDIR · NAS-AIOIR · Weather-Aware Mixture-of-Experts  

---

## 📊 Datasets & Benchmarks (from the Paper)

- **Dehazing:** RESIDE, Dense-Haze, NH-HAZE, REVIDE, Night-Haze  
- **Deraining:** Rain100H/L, DID-Data, RainCityscapes, RTTS  
- **Desnowing:** Snow100K, SRRS, SnowCityscapes, SnowKITTI  

Repository pages:
- [datasets/dehazing.md](datasets/dehazing.md)  
- [datasets/deraining.md](datasets/deraining.md)  
- [datasets/desnowing.md](datasets/desnowing.md)  
- [benchmarks/image_results.md](benchmarks/image_results.md)  
- [benchmarks/video_results.md](benchmarks/video_results.md)  

---

## 📏 Metrics, Loss Functions & Implementations

### 📊 Evaluation Metrics

| Category | Metrics |
|----------|---------|
| **Full-reference quality** | PSNR · SSIM · LPIPS · FID |
| **No-reference / perceptual** | NIQE · BRISQUE · PIQE · Entropy |
| **Temporal consistency (video)** | Temporal Warping Error (TWE) |

---

### 🧮 Loss Functions

| Category | Loss Functions |
|----------|----------------|
| **Reconstruction losses** | L1 · L2 · Charbonnier |
| **Perceptual & structural losses** | Perceptual loss · Edge loss |
| **Adversarial & task-aware losses** | Adversarial loss · Weather classification loss |

---

### 💻 Reference Implementations

| Resource | Description |
|----------|-------------|
| [implementations/metrics_and_losses.md](implementations/metrics_and_losses.md) | Mathematical definitions and explanations |
| [implementations/psnr_ssim.py](implementations/psnr_ssim.py) | PSNR and SSIM implementations |
| [implementations/loss_functions.py](implementations/loss_functions.py) | Charbonnier, perceptual, adversarial, and classification losses |

These implementations are provided to support reproducible research, benchmark comparison, and educational use.

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
  journal = {arXiv preprint arXiv:2510.09228},
  year    = {2025},
  url     = {https://arxiv.org/abs/2510.09228}
}

```

## 🤝 How to Contribute

We welcome contributions to keep this repository accurate and up to date.

### ✅ You can contribute by:
- Adding newly published papers (arXiv/DOI/CVF/IEEE links)
- Adding official code repositories and project pages
- Adding datasets (with license/terms + official source links)
- Adding benchmark results (with dataset/metric + exact source citation)
- Fixing broken links, typos, or reclassification issues

### 📌 Paper entry format (recommended)
When adding a paper to any table/page, please include:

- **Task:** haze / rain / snow / multi-weather / all-in-one  
- **Modality:** image / video  
- **Model family:** prior / CNN / GAN / Transformer / SSM / Diffusion / VLM / Agentic  
- **Training setting:** supervised / self-supervised / unsupervised (optional)  
- **Dataset(s):** e.g., RESIDE, Rain100H/L, Snow100K, REVIDE (optional)  
- **Link:** arXiv/DOI/IEEE/CVF (mandatory)  
- **Code link:** GitHub (optional but encouraged)

Example:
- **MWFormer** · multi-weather · image · Transformer · arXiv · (code link if available)

### 🧾 Submission guidelines
- Prefer **official sources** (DOI / CVF / arXiv / IEEE Xplore).
- Use consistent naming and capitalization for method titles.
- If adding benchmark numbers, mention **dataset + metric + table/section** from the original paper.
- Keep the README concise; add full lists to subpages (e.g., `methods/`, `datasets/`, `benchmarks/`).

### 🔁 How to submit
1. Fork the repository  
2. Create a branch: `feature/add-paper-<shortname>`  
3. Commit changes with a clear message  
4. Open a Pull Request (PR) with:
   - what you added/changed
   - sources for papers/datasets/benchmarks
   - any notes on classification

Thank you for helping maintain this living survey companion!

---

## ⭐ Acknowledgment

This repository is developed as a companion resource for the survey paper:

**Clear Roads, Clear Vision: Advancements in Multi-Weather Restoration for Smart Transportation**  
submitted to **IEEE Transactions on Intelligent Transportation Systems**.

We thank the broader research community for open-source code, datasets, and benchmark initiatives that enable progress in multi-weather restoration for intelligent transportation systems.
