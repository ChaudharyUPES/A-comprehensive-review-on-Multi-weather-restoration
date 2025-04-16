
# 🌦️ Multi-Weather Restoration Benchmarks

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Standardized evaluation framework for assessing multi-weather image restoration algorithms, supporting both reference and non-reference metrics.

---

## 📊 Benchmark Structure

```plaintext
benchmarks/
├── quantitative/
│   ├── reference/          # Ground-truth required metrics
│   │   ├── psnr_ssim.py    # Traditional fidelity metrics
│   │   ├── lpips_vgg.py    # Perceptual similarity
│   │   └── fid_score.py    # Feature-level comparison
│   ├── non_reference/      # No-reference quality assessment
│   │   ├── niqe.py         # Natural image quality evaluator
│   │   ├── brisque.py      # Blind/referenceless metric
│   │   └── entropy.py      # Information content analysis
│   ├── evaluate.py         # Unified evaluation script
│   └── results/            # Metric outputs (CSV/JSON)
├── qualitative/            # Visual comparison tools
└── requirements.txt        # Python dependencies
```

---

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/ChaudharyUPES/A-comprehensive-review-on-Multi-weather-restoration.git
cd benchmarks
pip install -r requirements.txt
```

### Basic Usage

```bash
# Reference metrics (requires ground truth)
python quantitative/evaluate.py --ref     --gt path/to/ground_truth     --restored path/to/restored_images

# Non-reference metrics
python quantitative/evaluate.py --no-ref     --restored path/to/restored_images
```

---

## 🔍 Supported Metrics

### Reference Metrics (Require GT)

| Metric | Description                     | Ideal Value | Implementation            |
|--------|---------------------------------|-------------|----------------------------|
| PSNR   | Peak Signal-to-Noise Ratio      | Higher better | reference/psnr_ssim.py   |
| SSIM   | Structural Similarity           | 1.0           | reference/psnr_ssim.py   |
| LPIPS  | Learned Perceptual Similarity   | 0.0           | reference/lpips_vgg.py   |
| FID    | Fréchet Inception Distance      | 0.0           | reference/fid_score.py   |

### Non-Reference Metrics

| Metric   | Description                          | Ideal Value   | Implementation             |
|----------|--------------------------------------|---------------|-----------------------------|
| NIQE     | Natural Image Quality Evaluator      | Lower better  | non_reference/niqe.py      |
| BRISQUE  | Blind/Referenceless Metric           | Lower better  | non_reference/brisque.py   |
| Entropy  | Information Content                  | Scene-dependent | non_reference/entropy.py |

---

## 📈 Sample Results

### Quantitative Output (CSV)
```csv
image,PSNR,SSIM,LPIPS,NIQE,BRISQUE
hazy_001.png,28.45,0.923,0.142,3.56,32.1
rainy_042.jpg,31.02,0.941,0.118,2.89,28.4
```

### Qualitative Comparison
Include side-by-side or overlay visual comparisons using tools in `qualitative/`.

---

## 🛠️ Advanced Usage

### Custom Metric Integration

```python
from quantitative.reference import psnr_ssim

gt = cv2.imread("gt.png")
restored = cv2.imread("restored.png")
print(f"PSNR: {psnr_ssim.calculate_psnr(gt, restored):.2f} dB")
```

### Parallel Evaluation

```bash
# Process 8 images simultaneously
python quantitative/evaluate.py --ref --gt gt/ --restored results/ --workers 8
```

---

## 📝 Citation

If you use this benchmark, please cite:

```bibtex
@article{multiweather2024,
  title={Comprehensive Benchmarking of Multi-Weather Restoration},
  author={Chaudhary, Sachin},
  journal={IEEE Transactions on Image Processing},
  year={2024}
}
```

---

## 🤝 Contributing

New metrics can be added by:

- Implementing in either `reference/` or `non_reference/`
- Updating `evaluate.py` integration
- Submitting a pull request

See `CONTRIBUTING.md` for guidelines.

---

Maintained by **Computer Vision Group, UPES**
