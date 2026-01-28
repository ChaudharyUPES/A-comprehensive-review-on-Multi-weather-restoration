
---

## 📄 Benchmark Files

### 🖼️ `image_results.md`
Contains representative **quantitative benchmark results** for image-based restoration methods, organized by task:

- Dehazing  
- Deraining  
- Desnowing  
- Multi-weather restoration  

Each table typically reports:
- Method name  
- Dataset  
- PSNR / SSIM / LPIPS / NIQE (as available)  
- Year  
- Source link (DOI / CVF / arXiv / IEEE)

---

### 🎞️ `video_results.md`
Summarizes **video restoration benchmark results**, focusing on:

- Temporal consistency  
- Compound weather degradations  
- Real and synthetic video datasets  

Reported metrics include:
- PSNR / SSIM  
- Temporal Warping Error (TWE)  
- LPIPS (video)  
- Perceptual quality measures  

---

### 🖼️ `qualitative_results.md`
Provides **visual comparisons** of restoration results, including:

- Side-by-side input vs restored images  
- Comparison across different methods  
- Challenging cases (night-time, dense fog, heavy rain, snow)  

This file highlights:
- Strengths and limitations of methods  
- Failure cases  
- Perceptual quality beyond numerical metrics  

---

## 📏 Evaluation Metrics

The benchmarks use standard evaluation measures adopted in the literature:

- **Full-reference metrics:** PSNR, SSIM, LPIPS, FID  
- **No-reference metrics:** NIQE, BRISQUE, PIQE  
- **Video-specific metrics:** Temporal Warping Error (TWE)

Refer to `implementations/metrics_and_losses.md` for mathematical definitions and code references.

---

## ⚠️ Notes on Comparability

- Results are extracted directly from original papers.  
- Different methods may use:
  - different training data  
  - different preprocessing  
  - different evaluation splits  

Therefore, values across tables should be interpreted as **indicative rather than strictly comparable**.

For full experimental settings, always consult the original publications.

---

## 🚀 Future Benchmark Directions

Planned extensions include:
- Unified benchmark protocols for multi-weather restoration  
- Leaderboards for image and video tasks  
- Downstream task evaluation (detection, tracking, segmentation)  
- Real-world large-scale evaluation  
- Night-time and compound degradation benchmarks  

---

## 🔗 Related Pages
- [taxonomy.md](../taxonomy.md)  
- [datasets/README.md](../datasets/README.md)  
- [benchmarks/image_results.md](image_results.md)  
- [benchmarks/video_results.md](video_results.md)  
- [benchmarks/qualitative_results.md](qualitative_results.md)  

---

## 📌 Citation

If you use these benchmark summaries, please cite the survey paper:

```bibtex
@article{clearroads_multiweather_restoration,
  title   = {Clear Roads, Clear Vision: Advancements in Multi-Weather Restoration for Smart Transportation},
  author  = {Galshetwar, Vijay M. and Hambarde, Praful and Patil, Prashant W. and Vipparathi, Santosh Kumar and Dudhane, Akshay and Murala, Subrahmanyam and Chaudhary, Sachin},
  journal = {arXiv preprint arXiv:2510.09228},
  year    = {2025},
  url     = {https://arxiv.org/abs/2510.09228}
}
