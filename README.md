
# 🌦️ A Comprehensive Review on Multi-Weather Restoration
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/ChaudharyUPES/A-comprehensive-review-on-Multi-weather-restoration/pulls)

> **This repository supports the review paper:  
> _"Clear Roads, Clear Vision: Advancements in Multi-Weather Restoration for Smart Transportation"_  
> Submitted to IEEE Transactions on Intelligent Transportation Systems (T-ITS).**

---

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/ChaudharyUPES/A-comprehensive-review-on-Multi-weather-restoration.git
cd A-comprehensive-review-on-Multi-weather-restoration
pip install -r requirements.txt
```

### Example Usage

```python
from implementations.dehazing.dark_channel import dehaze

# Process a hazy image
dehaze("input/hazy.jpg", "output/clear.jpg")
```

### Benchmark Evaluation

```bash
python benchmarks/quantitative/evaluate.py --gt clean/ --results restored/
```

---

## 🌟 Key Features

- ✅ **140+ Reviewed Papers** organized by task and technique.
- ✅ **Ready-to-Run Implementations:**
  - Classic methods (e.g., Dark Channel Prior)
  - Deep learning (e.g., Transformers, GANs)
- ✅ **Standardized Benchmarks** for PSNR, SSIM, and perceptual metrics.
- ✅ **Dataset summaries and loaders** for quick experimentation.

---

## 🗂️ Dataset Summary

| Dataset         | Type  | Samples  | Resolution | Link     |
|----------------|-------|----------|------------|----------|
| RESIDE         | Haze  | 10,000+  | Up to 4K   | [Download](#) |
| RainCityscapes | Rain  | 5,000    | 1920×1080  | [Download](#) |
| Snow100K       | Snow  | 100,000  | 1024×768   | [Download](#) |

> Refer to `datasets/README.md` for download links and instructions.

---

## 🧪 Implemented Methods

### 🔸 Dehazing
- Dark Channel Prior
- GridDehazeNet

### 🔸 Video Restoration
- Recurrent Video Deraining
- Consolidated Adversarial Network

> Organized by task in `implementations/`

---

## 📜 Citation

If you use this repository, please cite:

```bibtex
@article{multiweather2024,
  title={Comprehensive Survey on Multi-Weather Image Restoration},
  author={Chaudhary, Sachin and Co-authors},
  journal={IEEE Transactions on Intelligent Transportation Systems},
  year={2024}
}
```

---

## 🤝 Contributing

1. Fork the repository  
2. Create a new branch (`git checkout -b feature/new-method`)  
3. Commit changes (`git commit -m "Add new method"`)  
4. Push to branch (`git push origin feature/new-method`)  
5. Open a Pull Request  

> See `CONTRIBUTING.md` for guidelines

---

## 📬 Contact

**Research Lead:**  
**Sachin Chaudhary**  
Computer Vision Group  
University of Petroleum and Energy Studies  
📧 sachin.chaudhary@upes.ac.in
