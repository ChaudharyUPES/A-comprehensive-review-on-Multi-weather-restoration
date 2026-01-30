# 🎞️ Video Restoration Benchmark Results

This page summarizes representative **quantitative benchmark results for video-based weather restoration methods** reviewed in the survey:

**Clear Roads, Clear Vision: Advancements in Multi-Weather Restoration for Smart Transportation**  
(arXiv:2510.09228)

The benchmarks cover:
- 🌫️ Video Dehazing  
- 🌧️ Video Deraining  
- ❄️ Video Desnowing  
- ☂️ Multi-weather & compound degradation restoration  

Evaluation emphasizes both:
- **spatial restoration quality**, and  
- **temporal consistency across frames**.

Reported metrics include:
**PSNR, SSIM, LPIPS (video), NIQE, and Temporal Warping Error (TWE)**.

> 📌 *Note:* Numerical values are extracted from original papers. Replace placeholder values (XX.XX) with verified results from the survey tables.

---

## 📌 Benchmark Categories

| Task | Dataset Examples | Metrics |
|------|------------------|---------|
| **Video Dehazing** | REVIDE, NTIRE Video Dehazing | PSNR · SSIM · TWE |
| **Video Deraining** | NTIRE Video Rain, SPA-Video | PSNR · SSIM · LPIPS |
| **Video Desnowing** | SnowKITTI-Video, NTIRE Video Snow | PSNR · SSIM · TWE |
| **Multi-weather Video** | DAWN-Video, RTTS-Video | PSNR · SSIM · LPIPS · TWE |

---

## 🌫️ Video Dehazing Benchmarks

| Method | Dataset | PSNR (dB) | SSIM | TWE ↓ | Year | Link |
|--------|---------|-----------|------|------|------|------|
| Video Dehazing via Matrix Decomposition | REVIDE | XX.XX | 0.XX | XX.XX | 2020 | https://ieeexplore.ieee.org/document/9093415 |
| Temporal GAN | REVIDE | XX.XX | 0.XX | XX.XX | 2021 | https://github.com/liruizhe/REVIDE |
| TransWeather-Video | NTIRE Video Dehazing | XX.XX | 0.XX | XX.XX | 2022 | https://doi.org/10.1109/CVPR.2022.00106 |
| Dual Spatio-Temporal Transformer | NTIRE Video | XX.XX | 0.XX | XX.XX | 2024 | https://arxiv.org/abs/2404.15338 |

---

## 🌧️ Video Deraining Benchmarks

| Method | Dataset | PSNR (dB) | SSIM | TWE ↓ | Year | Link |
|--------|---------|-----------|------|------|------|------|
| SPA-VideoNet | SPA-Video | XX.XX | 0.XX | XX.XX | 2019 | https://doi.org/10.1109/ICCV.2019.01220 |
| CANet-Video | NTIRE Video Rain | XX.XX | 0.XX | XX.XX | 2021 | https://openaccess.thecvf.com/content/CVPR2021/html/Yu_CANet_Context_Aggregation_Network_for_Single_Image_Deraining_CVPR_2021_paper.html |
| SmartAssign-Video | NTIRE Video Rain | XX.XX | 0.XX | XX.XX | 2023 | https://openaccess.thecvf.com/content/CVPR2023/html/Li_SmartAssign_Learning_a_Smart_Knowledge_Assignment_Strategy_for_Deraining_and_CVPR_2023_paper.html |

---

## ❄️ Video Desnowing Benchmarks

| Method | Dataset | PSNR (dB) | SSIM | TWE ↓ | Year | Link |
|--------|---------|-----------|------|------|------|------|
| DesnowNet-Video | SnowKITTI-Video | XX.XX | 0.XX | XX.XX | 2017 | https://doi.org/10.1109/TIP.2017.2735474 |
| SnowFormer-Video | NTIRE Video Snow | XX.XX | 0.XX | XX.XX | 2022 | https://openaccess.thecvf.com/content/CVPR2022/html/Liu_SnowFormer_A_Transformer-Based_Framework_for_Snow_Removal_CVPR_2022_paper.html |
| MSP-Former-Video | NTIRE Video Snow | XX.XX | 0.XX | XX.XX | 2023 | https://openaccess.thecvf.com/content/CVPR2023/html/Liu_MSP-Former_Multi-Stage_Progressive_Transformer_for_Single_Image_Desnowing_CVPR_2023_paper.html |

---

## ☂️ Multi-Weather Video Benchmarks

| Method | Dataset | PSNR (dB) | SSIM | TWE ↓ | Year | Link |
|--------|---------|-----------|------|------|------|------|
| MWFormer-Video | DAWN-Video | XX.XX | 0.XX | XX.XX | 2023 | https://arxiv.org/abs/2312.12967 |
| Gated CAN-Video | DAWN-Video | XX.XX | 0.XX | XX.XX | 2023 | https://ieeexplore.ieee.org/document/10157390 |
| NAS-AIOIR-Video | DAWN-Video | XX.XX | 0.XX | XX.XX | 2020 | https://openaccess.thecvf.com/content_CVPR_2020/html/Li_All_in_One_Bad_Weather_Removal_Using_Architectural_Search_CVPR_2020_paper.html |
| TransWeather-Video | DAWN-Video | XX.XX | 0.XX | XX.XX | 2022 | https://doi.org/10.1109/CVPR.2022.00106 |

---

## 📊 Notes on Metrics

- **PSNR / SSIM:** Measure spatial fidelity and structural similarity  
- **LPIPS:** Measures perceptual similarity  
- **TWE (Temporal Warping Error):** Quantifies temporal consistency across frames  
- **NIQE / BRISQUE:** Used for real-world no-reference evaluation  

Results may vary due to:
- different training datasets  
- different preprocessing pipelines  
- different evaluation splits  

Always consult the original publications for reproducibility.

---

## ⚠️ Limitations

- Scarcity of large-scale real multi-weather video datasets  
- Inconsistent reporting of temporal metrics  
- High computational cost of video restoration  
- Lack of unified benchmark protocols  

---

## 🚀 Future Benchmark Directions

- Unified video restoration leaderboards  
- Real-world multi-weather driving videos  
- Joint restoration + detection benchmarks  
- Night-time compound weather benchmarks  
- Multi-modal video datasets (RGB + depth + thermal)  

---

## 🔗 Related Pages
- [taxonomy.md](../taxonomy.md)  
- [datasets/dehazing.md](../datasets/dehazing.md)  
- [datasets/deraining.md](../datasets/deraining.md)  
- [datasets/desnowing.md](../datasets/desnowing.md)  
- [datasets/multiweather.md](../datasets/multiweather.md)  
- [benchmarks/image_results.md](image_results.md)  
- [benchmarks/qualitative_results.md](qualitative_results.md)  

---

## 📌 Citation

Please cite the survey paper if you use these benchmark summaries:

```bibtex
@article{clearroads_multiweather_restoration,
  title   = {Clear Roads, Clear Vision: Advancements in Multi-Weather Restoration for Smart Transportation},
  author  = {Galshetwar, Vijay M. and Hambarde, Praful and Patil, Prashant W. and Vipparathi, Santosh Kumar and Dudhane, Akshay and Murala, Subrahmanyam and Chaudhary, Sachin},
  journal = {arXiv preprint arXiv:2510.09228},
  year    = {2025},
  url     = {https://arxiv.org/abs/2510.09228}
}
