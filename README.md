# 🚗 Multi-Weather Restoration for Transportation: A Comprehensive Review

This repository accompanies the paper:

**“Clear Roads, Clear Vision: Advancements in Multi-Weather Restoration for Smart Transportation”**  
Submitted to *IEEE Transactions on Intelligent Transportation Systems*, 2025.

---

## 📄 Paper Summary

This work provides a comprehensive survey of restoration methods addressing various weather-induced degradations in images and videos, with a special focus on transportation use cases. We categorize methods based on the degradation type (haze, rain, snow, all-in-one, and multi-weather), discuss their strengths and limitations, present benchmarking datasets, and highlight future directions.

---

## 📂 Categorized Papers

### 🌫 Haze Removal

| Paper            | Link                                                 |
| ---------------- | ---------------------------------------------------- |
| DehazeNet        | [IEEE TIP](https://doi.org/10.1109/TIP.2016.2537790) |
| AOD-Net          | [IEEE TIP](https://doi.org/10.1109/TIP.2017.2735468) |
| Haze-lines       | [CVPR](https://doi.org/10.1109/CVPR.2018.00667)      |
| DCP              | [TPAMI](https://doi.org/10.1109/TPAMI.2009.161)      |
| FFA-Net          | [ECCV](https://doi.org/10.1007/978-3-030-58545-7_15) |
| Tan's Visibility | [IEEE TIP](https://doi.org/10.1109/TIP.2008.926798)  |
| MSRCR Fusion     | [ICIP](#)                                            |
| Restormer        | [ICCV](https://doi.org/10.1109/ICCV48922.2021.00468) |
| FCANet           | [ACM MM](#)                                          |
| FD-GAN           | [AAAI](#)                                            |

### 🌧 Rain Removal

| Paper          | Link |
| -------------- | ---- |
| JORDER         | [CVPR](https://doi.org/10.1109/CVPR.2017.561)       |
| DDN            | [CVPR](https://doi.org/10.1109/CVPR.2017.8375215)   |
| DID-MDN        | [CVPR](https://doi.org/10.1109/CVPR.2018.00611)     |
| RESCAN         | [ECCV](https://doi.org/10.1007/978-3-030-01219-9_1) |
| SPANet         | [ICCV](https://doi.org/10.1109/ICCV.2019.01220)     |
| MSPFN          | [ICCV](#)                                           |
| DerainCycleGAN | [CVPRW](#)                                          |
| SmartAssign    | [CVPR](#)                                           |
| Dual-GCN       | [TPAMI](#)                                          |
| RIDNet         | [CVPRW](#)                                          |

### ❄️ Snow Removal

| Paper                 | Link |
| --------------------- | ---- |
| DesnowNet             | [ICASSP](#)          |
| DesnowGAN             | [ECCV](#)            |
| JSTASR                | [CVPR](#)            |
| DesnowFormer          | [ICCV](#)            |
| MSP-Former            | [CVPR](#)            |
| SnowFormer            | [CVPR](#)            |
| Invertible Separation | [NeurIPS](#)         |
| FPGA Desnowing        | [TCSVT](#)           |
| Marine Snow Removal   | [J. Oceanography](#) |

### 🧠 All-in-One Restoration

#### Prompt-Guided

| Paper                 | Link |
| --------------------- | ---- |
| PromptIR              | [ICCV](#)  |
| Language-Driven AIOIR | [ECCV](#)  |
| DPMambaIR             | [arXiv](#) |

#### Transformer-Based

| Paper                 | Link |
| --------------------- | ---- |
| TransWeather          | [CVPR](https://doi.org/10.1109/CVPR.2022.00106) |
| GridFormer            | [NeurIPS](#)                                    |
| Frequency Transformer | [ECCV](#)                                       |

#### Diffusion-Based

| Paper                       | Link |
| --------------------------- | ---- |
| AutoDIR                     | [CVPR](#)  |
| Visual-Instructed Diffusion | [ECCV](#)  |

#### Others

| Paper     | Link |
| --------- | ---- |
| WM-MoE    | [ICLR](#)  |
| MAC-GAN   | [ICPR](#)  |
| NAS-AIOIR | [AAAI](#)  |

### ☂️ Multi-Weather Restoration

#### Image

| Paper                     | Link |
| ------------------------- | ---- |
| WEAFU                     | [CVPR](#)    |
| MWFormer                  | [NeurIPS](#) |
| Unified Transformer       | [ECCV](#)    |
| Gated Context Aggregation | [TIP](#)     |
| Weather General/Specific  | [CVPR](#)    |

#### Video

| Paper                | Link |
| -------------------- | ---- |
| Matrix Decomposition | [ICCV](#)    |
| CANet                | [CVPR](#)    |
| Dual Spatio-Temporal | [NeurIPS](#) |
| Meta-Adaptation      | [CVPR](#)    |

---

## 🔹 Citation

```bibtex
@article{your2025paper,
  title     = {Clear Roads, Clear Vision: Advancements in Multi-Weather Restoration for Smart Transportation},
  author    = {Your Name and Co-authors},
  journal   = {IEEE Transactions on Intelligent Transportation Systems},
  year      = {2025},
  doi       = {YOUR_DOI_HERE}
}
```

---

## 💾 Dataset and Benchmark Tables

- **Table I**: Haze restoration datasets
- **Table II**: Rain removal datasets
- **Table III**: Snow removal datasets
- **Table IV**: All-in-One restoration benchmarks
- **Table V**: Multi-weather restoration datasets

---

## 📅 Contributing

Pull requests are welcome for:

- Adding newer restoration papers
- Providing paper links (arXiv/DOI)
- Improving benchmarks/tables
- Fixing typos or reclassifications

---

## 🙏 Acknowledgements

This project was initiated at the Centre of Excellence in Computer Vision, [Your Institution], and supported by [Your Funding/Research Program].

---
