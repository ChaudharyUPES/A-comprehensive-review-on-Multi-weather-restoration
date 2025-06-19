# 🧠 All-in-One Restoration Datasets

This document provides an overview of datasets curated for training and evaluating **All-in-One** weather restoration methods. These datasets include various degradations like haze, rain, snow, blur, and low light in a unified setting.

---

## 🧊 BID (Blurred Image Dataset)

Originally designed for blur evaluation, BID is often used in all-in-one restoration pipelines due to its wide variation in distortion.

* **Samples**: 586 blurred images
* **Labels**: Subjective quality scores

> 📄 Paper: [Multi-View Structure And Motion from Blur and Low Light Images (CVPR 2015)](https://openaccess.thecvf.com/content_cvpr_2015/html/Caraffa_Multi-View_Structure_And_2015_CVPR_paper.html)

---

## 📺 NTIRE All-in-One Challenges (2023–2024)

The NTIRE Video Restoration Challenges include All-in-One tracks that feature degraded videos with a combination of rain, haze, low-light, blur, and noise.

* **Types**: Video sequences with multiple weather conditions
* **Usage**: Benchmarking multi-task video restoration

> 📄 Challenge page: [NTIRE 2024](https://data.vision.ee.ethz.ch/cvl/ntire24/)

---

## 📁 Folder Usage

Place datasets under the following directory structure:

```plaintext
all-in-one/
├── BID/
└── NTIRE2024/
```

> 🛠 Additional preprocessing or splits may be required depending on your training framework.

---

For citation formats and licensing information, refer to each dataset's associated publication or license file.

