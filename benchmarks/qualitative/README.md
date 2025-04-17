
# 🖼️ Qualitative Evaluation Toolkit

This module provides a suite of tools to visually compare the outputs of different restoration algorithms with either ground truth or among models, and to visualize metrics.

---

## 📦 Usage

### 🔍 Single Image Comparison

Compare one restored image with its ground truth:

```bash
python visualize.py     --gt path/to/ground_truth.png     --restored path/to/restored.png     --output comparison.png
```

---

### 📁 Batch Image Comparison

Compare a folder of ground truth and restored images with matching filenames:

```bash
python compare.py     --gt datasets/ground_truth     --restored results/dehazing
```

---

### 🧱 Create Image Grids

Generate a grid layout from multiple image outputs for visual summary:

```bash
python tile_images.py     --input "results/*.png"     --cols 4     --output results_grid.png
```

---

### 📊 Metric Visualization

Plot quantitative metrics (PSNR, SSIM, LPIPS, etc.) from CSV files:

```bash
python metrics_plot.py     --csv quantitative/results/metrics.csv
```

---

## 📁 Toolkit Structure

```plaintext
qualitative/
├── visualize.py       # One-to-one visual comparison
├── compare.py         # Batch comparison for folders
├── tile_images.py     # Generate image collage/grid
├── metrics_plot.py    # Plot metric bar/line charts
└── sample_outputs/    # Example results and figures
```

---

Designed to support visual analysis alongside numerical benchmarking in multi-weather restoration tasks.
