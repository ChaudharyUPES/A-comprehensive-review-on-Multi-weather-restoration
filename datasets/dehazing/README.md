# 🌫️ Dehazing Datasets

This page summarizes the major benchmark datasets used for **single-image and video dehazing** in the survey:

**Clear Roads, Clear Vision: Advancements in Multi-Weather Restoration for Smart Transportation**  
(arXiv:2510.09228)

The datasets are categorized based on:
- Image vs Video modality  
- Synthetic vs Real-world data  
- Daytime vs Night-time conditions  

These benchmarks support:
- Training of dehazing models  
- Fair evaluation and comparison  
- Reproducible research for Intelligent Transportation Systems (ITS)  

---

## 📌 Dataset Categories

| Category | Description |
|----------|-------------|
| **Synthetic datasets** | Generated using atmospheric scattering models |
| **Real-world datasets** | Captured under natural haze and fog conditions |
| **Hybrid datasets** | Combination of synthetic and real data |
| **Video datasets** | Hazy video sequences for temporal evaluation |

---

## 🖼️ Image Dehazing Datasets

| Dataset | Type | Size | Real / Synthetic | Description | Link |
|--------|------|------|------------------|-------------|------|
| **RESIDE** | Image | 20,000+ | Hybrid | Large-scale benchmark with Indoor (ITS) and Outdoor (OTS) subsets | https://sites.google.com/view/reside-dehaze-datasets |
| **SOTS** | Image | 1,000 | Synthetic | Testing subset of RESIDE (indoor & outdoor scenes) | https://sites.google.com/view/reside-dehaze-datasets |
| **I-HAZE** | Image | 35 pairs | Real | Indoor real hazy images with ground truth | https://data.vision.ee.ethz.ch/cvl/ntire18/i-haze/ |
| **O-HAZE** | Image | 45 pairs | Real | Outdoor real hazy images with ground truth | https://data.vision.ee.ethz.ch/cvl/ntire18/o-haze/ |
| **Dense-Haze** | Image | 33 pairs | Real | Dense haze scenes with paired ground truth | https://data.vision.ee.ethz.ch/cvl/ntire19/dense-haze/ |
| **NH-HAZE** | Image | 55 pairs | Real | Night-time hazy scenes with illumination effects | https://data.vision.ee.ethz.ch/cvl/ntire20/nh-haze/ |
| **HazeRD** | Image | 1,000+ | Synthetic | High-resolution outdoor hazy scenes | https://github.com/nathanhubens/hazerd |
| **RTTS (Haze subset)** | Image | 4,000+ | Real | Traffic surveillance images under haze and fog | https://sites.google.com/site/boyilics/website-builder/rtts-dataset |

---

## 🎞️ Video Dehazing Datasets

| Dataset | Type | Size | Real / Synthetic | Description | Link |
|--------|------|------|------------------|-------------|------|
| **REVIDE** | Video | 500+ sequences | Real | Real-world video dehazing benchmark | https://github.com/liruizhe/REVIDE |
| **VideoHaze** | Video | 150 sequences | Synthetic | Synthetic hazy video sequences with temporal ground truth | https://github.com/VideoHaze/VideoHaze |
| **NTIRE Video Dehazing** | Video | Challenge dataset | Hybrid | Dataset from NTIRE video restoration challenges | https://data.vision.ee.ethz.ch/cvl/ntire22/ |

---

## 🌙 Challenging Conditions

| Dataset | Focus | Description | Link |
|--------|-------|-------------|------|
| **NH-HAZE** | Night-time haze | Haze with glow and illumination artifacts | https://data.vision.ee.ethz.ch/cvl/ntire20/nh-haze/ |
| **Dense-Haze** | Dense fog | Strong atmospheric scattering | https://data.vision.ee.ethz.ch/cvl/ntire19/dense-haze/ |
| **RTTS** | Traffic scenes | Real-world road scenes under haze and fog | https://sites.google.com/site/boyilics/website-builder/rtts-dataset |

---

## 📊 Evaluation Protocols

Common evaluation settings:
- **Train/Test splits:** Indoor vs Outdoor (RESIDE)  
- **Metrics:** PSNR, SSIM, LPIPS, NIQE  
- **Video metrics:** Temporal Warping Error (TWE)  
- **Cross-dataset testing:** Train on synthetic, test on real haze  

---

## ⚠️ Challenges & Limitations

- Limited paired real-world hazy–clean image datasets  
- Strong domain gap between synthetic and real haze  
- Night-time haze datasets remain small  
- Illumination and glow artifacts are difficult to model  
- Lack of large-scale multi-weather video benchmarks  

---

## 🚀 Future Dataset Directions

- Large-scale real-world haze datasets with paired ground truth  
- Multi-weather datasets (haze + rain + snow)  
- Night-time and low-light haze benchmarks  
- Task-aware datasets for detection and segmentation  
- Unified image + video dehazing benchmarks  

---

## 🔗 Related Pages
- [taxonomy.md](../taxonomy.md)  
- [datasets/deraining.md](deraining.md)  
- [datasets/desnowing.md](desnowing.md)  
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
