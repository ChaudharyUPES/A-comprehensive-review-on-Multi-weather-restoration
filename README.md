# 🌦️ A Comprehensive Review on Multi-Weather Restoration

This repository presents a detailed review and implementation of state-of-the-art techniques for multi-weather restoration tasks such as **rain**, **snow**, **haze**, and **low-light image enhancement**. The project includes literature surveys, code implementations, and comparative evaluations of various deep learning methods.

---

## 📑 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Datasets](#datasets)
- [Usage](#usage)
- [Results](#results)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## 🧠 Overview

Real-world outdoor images often suffer from various weather-induced degradations that hinder downstream computer vision tasks. This repository presents:
- A survey of recent research in multi-weather restoration.
- Implementation of selected restoration models.
- Sample outputs for visual comparison.
- Performance metrics (PSNR, SSIM).

---

## ✨ Features

- ✅ Review of multiple weather-specific restoration models.
- ✅ Organized repository with individual folders for rain, snow, haze, and low-light enhancement.
- ✅ Sample dataset integration.
- ✅ Model outputs for comparison.
- ✅ Clear structure for future extensions.

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ChaudharyUPES/A-comprehensive-review-on-Multi-weather-restoration.git
   cd A-comprehensive-review-on-Multi-weather-restoration
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

---

## 📂 Datasets

For experimentation, download the datasets corresponding to each weather condition and place them in their respective folders:

- Rain: `./rain/data/`
- Snow: `./snow/data/`
- Haze: `./haze/data/`
- Low-Light: `./low_light/data/`

> 📦 Sample images are provided. Full datasets can be linked in future updates.

---

## 🚀 Usage

Navigate to the relevant directory and run the corresponding script. Example:

```bash
cd rain
python inference.py --input ./data/sample_rainy.jpg --output ./results/
```

Similarly, for haze:
```bash
cd haze
python dehaze.py
```

---

## 📊 Results

| Method           | PSNR (dB) | SSIM  |
|------------------|-----------|--------|
| RainNet          | 29.3      | 0.91   |
| SnowRemovalNet   | 30.1      | 0.92   |
| DehazeNet        | 28.5      | 0.89   |
| EnlightenGAN     | 26.7      | 0.86   |

> Detailed results and comparison charts will be added soon in `/results/`.

---

## 📁 Project Structure

```
A-comprehensive-review-on-Multi-weather-restoration/
│
├── rain/
│   ├── inference.py
│   └── model.py
│
├── haze/
│   ├── dehaze.py
│   └── model.py
│
├── snow/
│   ├── snow_removal.py
│   └── model.py
│
├── low_light/
│   ├── enhance.py
│   └── model.py
│
├── results/
│   └── (output images)
│
├── requirements.txt
└── README.md
```

---

## 🤝 Contributing

We welcome contributions to improve this project!

- 📌 Fork the repository.
- 🔧 Create a new branch: `git checkout -b feature-name`
- 💾 Make your changes and commit: `git commit -m "Add feature"`
- 🚀 Push to your fork and open a Pull Request.

> Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) (coming soon) for detailed guidelines.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

Thanks to all the researchers whose work inspired this project. Model architectures and datasets used in this repository are credited to their respective authors.
