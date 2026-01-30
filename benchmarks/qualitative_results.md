# 🖼️ Qualitative Results for Multi-Weather Image & Video Restoration

This page presents **visual (qualitative) comparisons** of representative restoration methods reviewed in the survey:

**Clear Roads, Clear Vision: Advancements in Multi-Weather Restoration for Smart Transportation**  
(arXiv:2510.09228)

Qualitative evaluation highlights:
- Perceptual quality beyond numerical metrics  
- Visual artifacts and failure cases  
- Generalization to real-world and night-time conditions  

These results complement the quantitative benchmarks in:
- [image_results.md](image_results.md)  
- [video_results.md](video_results.md)

---

## 📌 Organization of Qualitative Results

Qualitative results are grouped by:
- **Weather type:** haze, rain, snow, multi-weather  
- **Modality:** image and video  
- **Difficulty:** light, dense, night-time, compound degradations  

Each section typically includes:
- Input degraded image / video frame  
- Output from multiple representative methods  
- Ground truth (if available)  
- Observations on visual quality  

---

## 🌫️ Dehazing (Image)

### Example Scenarios
- Outdoor driving scenes  
- Urban traffic intersections  
- Dense fog and night-time haze  

| Input | Method A | Method B | Method C | Ground Truth |
|-------|----------|----------|----------|--------------|
| ![hazy_input](figures/dehazing/input_1.png) | ![m1](figures/dehazing/method1_1.png) | ![m2](figures/dehazing/method2_1.png) | ![m3](figures/dehazing/method3_1.png) | ![gt](figures/dehazing/gt_1.png) |

**Observations:**
- Transformer-based methods recover sharper edges and colors  
- Prior-based methods may over-enhance contrast  
- Night-time haze remains challenging  

---

## 🌧️ Deraining (Image)

### Example Scenarios
- Heavy rain streaks  
- Urban surveillance scenes  
- Road scenes with occlusions  

| Input | Method A | Method B | Method C | Ground Truth |
|-------|----------|----------|----------|--------------|
| ![rain_input](figures/deraining/input_1.png) | ![m1](figures/deraining/method1_1.png) | ![m2](figures/deraining/method2_1.png) | ![m3](figures/deraining/method3_1.png) | ![gt](figures/deraining/gt_1.png) |

**Observations:**
- Multi-scale models remove rain streaks more effectively  
- Over-smoothing may remove fine scene details  
- Real rain is harder than synthetic rain  

---

## ❄️ Desnowing (Image)

### Example Scenarios
- Snow occlusion  
- Road and vehicle scenes  
- Dense snowfall  

| Input | Method A | Method B | Method C | Ground Truth |
|-------|----------|----------|----------|--------------|
| ![snow_input](figures/desnowing/input_1.png) | ![m1](figures/desnowing/method1_1.png) | ![m2](figures/desnowing/method2_1.png) | ![m3](figures/desnowing/method3_1.png) | ![gt](figures/desnowing/gt_1.png) |

**Observations:**
- Heavy snow causes strong occlusion artifacts  
- Transformer-based methods preserve structure better  
- Motion blur complicates desnowing  

---

## ☂️ Multi-Weather Restoration (Image)

### Example Scenarios
- Haze + rain  
- Snow + low-light  
- Compound weather in traffic scenes  

| Input | Method A | Method B | Method C | Ground Truth |
|-------|----------|----------|----------|--------------|
| ![mw_input](figures/multiweather/input_1.png) | ![m1](figures/multiweather/method1_1.png) | ![m2](figures/multiweather/method2_1.png) | ![m3](figures/multiweather/method3_1.png) | ![gt](figures/multiweather/gt_1.png) |

**Observations:**
- Unified models handle compound degradations better  
- Single-task models often fail on mixed weather  
- Vision-language guided methods improve robustness  

---

## 🎞️ Video Restoration (Qualitative)

### Example Scenarios
- Driving videos under rain and haze  
- Snowfall in surveillance footage  
- Night-time compound weather  

| Frame (Input) | Restored (Method A) | Restored (Method B) | Restored (Method C) |
|---------------|---------------------|---------------------|---------------------|
| ![vin](figures/video/input_1.png) | ![v1](figures/video/method1_1.png) | ![v2](figures/video/method2_1.png) | ![v3](figures/video/method3_1.png) |

**Observations:**
- Temporal consistency is critical  
- Flickering artifacts remain common  
- Multi-frame transformers reduce temporal noise  

---

## ⚠️ Failure Cases

| Scenario | Description |
|----------|-------------|
| Night-time haze | Strong glow and light scattering degrade performance |
| Heavy snow | Occlusion dominates restoration |
| Fast motion | Motion blur + rain confuses models |
| Compound weather | Mixed degradations break single-task models |

These cases motivate:
- Multi-task learning  
- Agentic AI planning  
- Vision-language guidance  

---

## 📊 Key Visual Insights

- Transformer and diffusion models outperform CNNs in perceptual quality  
- Multi-weather models generalize better than single-task models  
- Real-world images remain more challenging than synthetic datasets  
- Qualitative results reveal artifacts not captured by PSNR/SSIM  

---

## 🔗 Related Pages
- [taxonomy.md](../taxonomy.md)  
- [benchmarks/image_results.md](image_results.md)  
- [benchmarks/video_results.md](video_results.md)  
- [datasets/dehazing.md](../datasets/dehazing.md)  
- [datasets/deraining.md](../datasets/deraining.md)  
- [datasets/desnowing.md](../datasets/desnowing.md)  
- [datasets/multiweather.md](../datasets/multiweather.md)  

---

## 📌 Citation

Please cite the survey paper if you use these qualitative summaries:

```bibtex
@article{clearroads_multiweather_restoration,
  title   = {Clear Roads, Clear Vision: Advancements in Multi-Weather Restoration for Smart Transportation},
  author  = {Galshetwar, Vijay M. and Hambarde, Praful and Patil, Prashant W. and Vipparathi, Santosh Kumar and Dudhane, Akshay and Murala, Subrahmanyam and Chaudhary, Sachin},
  journal = {arXiv preprint arXiv:2510.09228},
  year    = {2025},
  url     = {https://arxiv.org/abs/2510.09228}
}

