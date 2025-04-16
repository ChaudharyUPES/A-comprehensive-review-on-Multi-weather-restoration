# A Comprehensive Review on Multi-Weather Restoration

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

![Multi-Weather Restoration Teaser](https://via.placeholder.com/800x400.png?text=Multi-Weather+Restoration+Examples)

## Table of Contents
- [Repository Structure](#-repository-structure)
- [Quick Start](#-quick-start)  
- [Key Features](#-key-features)
- [Dataset Summary](#-dataset-summary) 
- [Implemented Methods](#-implemented-methods)
- [Citation](#-citation)
- [Contributing](#-contributing)
- [Contact](#-contact)

## 📂 Repository Structure
├── datasets/ # Weather-specific datasets
│ ├── dehazing/ # RESIDE, O-Haze, etc.
│ ├── deraining/ # RainCityscapes, SPA-Data
│ ├── desnowing/ # CSD, Snow100K
│ └── multi-weather/ # Combined condition datasets
├── implementations/ # Algorithm implementations
│ ├── unified_models/ # Multi-weather approaches
│ ├── dehazing/ # Dehazing methods
│ ├── deraining/ # Deraining methods
│ ├── desnowing/ # Desnowing methods
│ └── video_restoration/ # Video processing
├── benchmarks/ # Evaluation tools
│ ├── quantitative/ # PSNR/SSIM metrics
│ └── qualitative/ # Visual comparisons
├── papers/ # PDFs of cited papers
├── LICENSE # MIT License
└── CITATION.md # Citation information


## 🚀 Quick Start

### Installation

git clone https://github.com/ChaudharyUPES/A-comprehensive-review-on-Multi-weather-restoration.git
cd A-comprehensive-review-on-Multi-weather-restoration
pip install -r requirements.txt

from implementations.dehazing.dark_channel_prior import dehaze

dehazed_image = dehaze("input/hazy.jpg")
dehazed_image.save("output/clear.jpg")

🌦️ Key Features
140+ Reviewed Papers covering:

Single-image restoration

Video processing

Unified multi-weather models

Ready-to-Run Implementations of:

Classic algorithms (Dark Channel Prior, etc.)

Deep learning models (Transformers, GANs)

Real-time video pipelines

Standardized Evaluation:
python benchmarks/quantitative/eval.py --gt ground_truth/ --restored results/

📊 Dataset Summary
Dataset	Weather	Samples	Resolution	Download
RESIDE	Haze	10,000+	Up to 4K	Link
RainCityscapes	Rain	5,000	1920×1080	Link
Snow100K	Snow	100,000	1024×768	Link
🛠️ Implemented Methods
Dehazing
Dark Channel Prior [Code]

GridDehazeNet [Code]

Deraining
Attentive GAN [Code]

Recurrent Squeeze-and-Excitation [Code]

Unified Models
TransWeather [Code]

All-in-One Weather Removal [Code]

📝 Citation
bibtex
Copy
@article{multiweather2024,
  title={Comprehensive Survey on Multi-Weather Image Restoration},
  author={Chaudhary, Sachin and Co-authors},
  journal={IEEE Transactions on Intelligent Transportation Systems},
  year={2024}
}
🤝 Contributing
Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some amazing feature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

See CONTRIBUTING.md for detailed guidelines.

📧 Contact
Sachin Chaudhary
Computer Vision Group
University of Petroleum and Energy Studies
Email: sachin.chaudhary@upes.ac.in

This project is maintained by Computer Vision Research Group, UPES


### How to Download:
1. Copy all text above
2. Create a new file named `README.md` in your repository
3. Paste the content
4. Commit and push:

git add README.md
git commit -m "Add comprehensive README"
git push origin main

Customization Tips:
Replace placeholder image URL with actual teaser image

Update contact information

Add specific installation requirements

Include more implementation details as you add code
