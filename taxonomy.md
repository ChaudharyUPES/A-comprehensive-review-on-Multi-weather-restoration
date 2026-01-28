# 🧠 Taxonomy of Multi-Weather Image & Video Restoration Methods

This document provides a structured taxonomy of methods reviewed in the survey:

**Clear Roads, Clear Vision: Advancements in Multi-Weather Restoration for Smart Transportation**  
(arXiv:2510.09228)

The taxonomy organizes restoration approaches along three key dimensions:

1. **Restoration Scope** – what degradations are handled  
2. **Model Family** – how restoration is performed  
3. **Application Modality** – image or video  

This taxonomy supports:
- systematic literature comparison  
- benchmarking  
- identification of research gaps  
- reproducible evaluation  

---

## 🎯 I. Taxonomy by Restoration Scope

| Category | Description | Representative Methods |
|----------|-------------|------------------------|
| **Single-task Restoration** | Models designed for one specific degradation type (haze, rain, or snow) | DehazeNet, AOD-Net, DesnowNet, RainNet |
| **Multi-weather Restoration** | Joint learning of haze, rain, and snow removal in a unified framework | MWFormer, Gated Context Aggregation Network |
| **All-in-One Restoration** | Unified handling of weather + blur, noise, low-light, compression | TransWeather, PromptIR, NAS-AIOIR |

---

## 🧠 II. Taxonomy by Model Family

### 1️⃣ Prior-based & Traditional Methods
Use handcrafted priors and physical models.

| Subtype | Examples |
|--------|----------|
| Atmospheric scattering models | Dark Channel Prior, Haze-Lines |
| Filtering & fusion methods | Multi-exposure fusion, guided filtering |
| Low-rank / sparse decomposition | Matrix decomposition methods |

**Strengths:** interpretable, low compute  
**Limitations:** poor generalization to real-world scenes  

---

### 2️⃣ CNN & GAN-based Methods
Learn restoration directly from data.

| Subtype | Examples |
|--------|----------|
| CNN regression models | DehazeNet, DID-MDN, DesnowNet |
| Attention-based CNNs | FFA-Net, RSC-Net |
| GAN-based frameworks | DesnowGAN, MAC-GAN |

**Strengths:** strong performance on synthetic data  
**Limitations:** dataset bias, unstable training (GANs)

---

### 3️⃣ Transformer-based Methods
Leverage long-range dependencies and global context.

| Subtype | Examples |
|--------|----------|
| Vision Transformers | TransWeather, SnowFormer |
| Multi-scale Transformers | MSP-Former, GridFormer |
| Spatio-temporal Transformers | Dual Spatio-Temporal Transformer (video) |

**Strengths:** strong global modeling  
**Limitations:** high computational cost  

---

### 4️⃣ State Space Models (SSM / Mamba)
Model long sequences efficiently with linear complexity.

| Subtype | Examples |
|--------|----------|
| Degradation-aware SSMs | DPMambaIR |
| Cross-modal SSM fusion | Mamba-based fusion networks |

**Strengths:** efficient sequence modeling  
**Limitations:** still emerging, limited benchmarks  

---

### 5️⃣ Diffusion & Generative Models
Learn degradation distributions and perform restoration via sampling.

| Subtype | Examples |
|--------|----------|
| Latent diffusion restoration | AutoDIR |
| Conditioned diffusion models | Visual-Instructed Degradation Diffusion |

**Strengths:** strong realism, generalization  
**Limitations:** slow inference, high compute  

---

### 6️⃣ Vision-Language & Prompt-based Models
Leverage text guidance and language priors.

| Subtype | Examples |
|--------|----------|
| Prompt-driven restoration | PromptIR |
| Language-conditioned frameworks | Language-Driven All-in-One Restoration |

**Strengths:** flexible, zero-shot capable  
**Limitations:** prompt sensitivity  

---

### 7️⃣ Agentic AI & Planning-driven Frameworks
Multi-agent systems for compound degradations.

| Subtype | Examples |
|--------|----------|
| LLM-guided pipelines | Agentic restoration systems |
| Task-planning restoration | Multi-agent scheduling |

**Strengths:** adaptive, interpretable  
**Limitations:** early-stage research  

---

## 🖼️ III. Taxonomy by Modality

| Modality | Focus | Challenges |
|----------|-------|------------|
| **Image Restoration** | Single-frame weather removal | spatial artifacts, color distortion |
| **Video Restoration** | Frame sequence restoration | temporal consistency, motion blur |

---

## 🌙 IV. Taxonomy by Operating Conditions

| Condition | Challenges |
|----------|------------|
| **Daytime** | haze scattering, rain streaks |
| **Nighttime** | glow, low-light, noise |
| **Compound weather** | haze + rain + snow simultaneously |
| **Real-world weather** | unknown degradation distributions |

---

## 📊 V. Taxonomy by Learning Paradigm

| Paradigm | Description |
|----------|-------------|
| Supervised learning | Paired clean–degraded data |
| Self-supervised learning | No clean ground truth |
| Unsupervised learning | Domain adaptation, cycle consistency |
| Zero-shot / prompt-based | No task-specific retraining |

---

## 🧩 VI. Unified View of the Taxonomy

| Dimension | Categories |
|----------|------------|
| Restoration Scope | Single-task · Multi-weather · All-in-one |
| Model Family | Prior · CNN/GAN · Transformer · SSM · Diffusion · VLM · Agentic |
| Modality | Image · Video |
| Condition | Day · Night · Compound |
| Learning Paradigm | Supervised · Self-supervised · Zero-shot |

---

## 🔍 Research Gaps & Open Challenges

- Lack of large-scale real-world multi-weather datasets  
- Poor cross-domain generalization  
- High computational cost of diffusion & transformer models  
- Limited benchmarks for video multi-weather restoration  
- Need for explainable and trustworthy restoration  
- Integration with downstream ITS tasks (detection, tracking)

---

## 🚀 Future Directions

- Agentic AI for compound weather reasoning  
- Vision-language driven restoration  
- Unified diffusion-transformer hybrids  
- Task-aware restoration (joint detection + restoration)  
- Real-time lightweight models for edge deployment  

---

## 🔗 Related Pages
- [datasets/dehazing.md](datasets/dehazing.md)  
- [datasets/deraining.md](datasets/deraining.md)  
- [datasets/desnowing.md](datasets/desnowing.md)  
- [benchmarks/image_results.md](benchmarks/image_results.md)  
- [implementations/metrics_and_losses.md](implementations/metrics_and_losses.md)

---

## 📌 Citation

Please cite the survey paper if you use this taxonomy:

```bibtex
@article{clearroads_multiweather_restoration,
  title   = {Clear Roads, Clear Vision: Advancements in Multi-Weather Restoration for Smart Transportation},
  author  = {Galshetwar, Vijay M. and Hambarde, Praful and Patil, Prashant W. and Vipparathi, Santosh Kumar and Dudhane, Akshay and Murala, Subrahmanyam and Chaudhary, Sachin},
  journal = {arXiv preprint arXiv:2510.09228},
  year    = {2025},
  url     = {https://arxiv.org/abs/2510.09228}
}
```
## ⭐ Acknowledgment
This taxonomy is derived from the comprehensive analysis presented in the survey and is intended as a living resource for the research community.
