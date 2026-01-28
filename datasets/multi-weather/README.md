# ☂️ Multi-Weather Datasets

This page summarizes the major benchmark datasets used for **multi-weather and compound degradation restoration** in the survey:

**Clear Roads, Clear Vision: Advancements in Multi-Weather Restoration for Smart Transportation**  
(arXiv:2510.09228)

Multi-weather datasets contain combinations of:
- 🌫️ Haze  
- 🌧️ Rain  
- ❄️ Snow  
- 🌙 Night-time illumination  
- ☀️ Low-light and atmospheric effects  

These datasets support:
- Unified restoration models  
- Compound degradation analysis  
- Real-world evaluation for Intelligent Transportation Systems (ITS)  

---

## 📌 Dataset Categories

| Category | Description |
|----------|-------------|
| **Synthetic multi-weather datasets** | Generated using physical and simulation-based weather models |
| **Real-world multi-weather datasets** | Captured in natural adverse weather conditions |
| **Hybrid datasets** | Combination of synthetic and real-world samples |
| **Video datasets** | Multi-weather video sequences for temporal consistency |

---

## 🖼️ Image Multi-Weather Datasets

| Dataset | Type | Size | Real / Synthetic | Description | Link |
|--------|------|------|------------------|-------------|------|
| **DAWN (Diverse Adverse Weather Needs)** | Image | 10,000 | Mixed | Unified benchmark including haze, rain, and snow | https://github.com/vis-opt/DAWN |
| **Realistic Multi-Weather Dataset (RMWD)** | Image | 2,500+ | Real | Real-world compound weather scenes | — |
| **WeatherBench** | Image | ~5,000 | Synthetic | Multiple degradations with weather labels | https://github.com/WeatherBench/WeatherBench |
| **RTTS (Multi-weather subset)** | Image | 4,000+ | Real | Traffic scenes under rain, haze, and fog | https://sites.google.com/site/boyilics/website-builder/rtts-dataset |
| **SnowCityscapes-MW** | Image | ~2,500 | Synthetic | Snow + rain + haze on Cityscapes scenes | https://github.com/huawei-noah/SmartCar |

---

## 🎞️ Video Multi-Weather Datasets

| Dataset | Type | Size | Real / Synthetic | Description | Link |
|--------|------|------|------------------|-------------|------|
| **REVIDE-MW** | Video | 200+ sequences | Real | Multi-weather video sequences (rain, haze, snow) | https://github.com/liruizhe/REVIDE |
| **NTIRE Multi-Weather Video Dataset** | Video | Challenge dataset | Hybrid | Multi-degradation benchmark from NTIRE challenges | https://data.vision.ee.ethz.ch/cvl/ntire22/ |
| **MW-VideoSet** | Video | 100+ sequences | Synthetic | Synthetic compound weather videos | — |

---

## 🌙 Challenging Conditions

| Dataset | Focus | Description | Link |
|--------|-------|-------------|------|
| **DAWN** | Compound weather | Mixed haze, rain, and snow conditions | https://github.com/vis-opt/DAWN |
| **RTTS** | Traffic scenes | Real-world road scenes under multiple weather types | https://sites.google.com/site/boyilics/website-builder/rtts-dataset |
| **REVIDE-MW** | Video sequences | Real multi-weather driving videos | https://github.com/liruizhe/REVIDE |

---

## 📊 Evaluation Protocols

Common evaluation settings:
- **Train/Test splits:** Single-weather vs compound-weather subsets  
- **Metrics:** PSNR, SSIM, LPIPS, NIQE  
- **Video metrics:** Temporal Warping Error (TWE)  
- **Cross-dataset testing:** Train on synthetic multi-weather, test on real-world data  

---

## ⚠️ Challenges & Limitations

- Limited availability of large-scale real multi-weather paired datasets  
- Compound degradations are difficult to simulate realistically  
- High domain gap between synthetic and real-world weather  
- Lack of standardized evaluation benchmarks  
- Scarcity of multi-weather video datasets  

---

## 🚀 Future Dataset Directions

- Large-scale real-world multi-weather datasets with ground truth  
- Night-time multi-weather benchmarks  
- Multi-modal datasets (RGB + depth + thermal)  
- Task-aware datasets for detection and tracking  
- Unified image + video compound weather benchmarks  

---

## 🔗 Related Pages
- [taxonomy.md](../taxonomy.md)  
- [datasets/dehazing.md](dehazing.md)  
- [datasets/deraining.md](deraining.md)  
- [datasets/desnowing.md](desnowing.md)  
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
