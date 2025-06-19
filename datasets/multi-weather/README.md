# ☂️ Multi-Weather Datasets

This section highlights datasets used for combined or mixed weather restoration tasks, including multiple adverse weather types like haze, rain, and snow, as well as general-purpose all-in-one datasets.

---

## 🌦️ DAWN (Diverse Adverse Weather Needs)

A large-scale dataset containing images with mixed weather effects: haze, rain, snow, and combinations thereof. Designed for robust multi-weather visibility restoration.

* \~10,000 labeled samples
* Focused on outdoor road scenes

> 📄 Project: [https://github.com/vis-opt/DAWN](https://github.com/vis-opt/DAWN)

---

## 🌀 Realistic Multi-Weather Dataset (RMWD)

Real-world captured videos and images under naturally occurring multiple weather conditions.

* \~2,500 samples
* Used for evaluating domain generalization and robustness

> 📄 Source: (Link not available)

---

🧊 BID (Blurred Image Dataset)
Originally for blur, this dataset is frequently used in All-in-One restoration settings that jointly consider haze, snow, rain, and blur.

* 586 real-world blurred images with subjective scores

> 📄 Paper: [https://openaccess.thecvf.com/content\_cvpr\_2015/html/Caraffa\_Multi-View\_Structure\_And\_2015\_CVPR\_paper.html](https://openaccess.thecvf.com/content_cvpr_2015/html/Caraffa_Multi-View_Structure_And_2015_CVPR_paper.html)

---

## 📺 NTIRE All-in-One Challenges (2023–2024)

Video restoration benchmarks that include mixed degradation videos such as haze, rain, snow, low light, blur.

* Includes official evaluation scripts and track-wise leaderboard

> 📄 Website: [https://data.vision.ee.ethz.ch/cvl/ntire24/](https://data.vision.ee.ethz.ch/cvl/ntire24/)

---

For preprocessing and usage examples, see `/datasets/multi-weather` folder.

> 📁 For All-in-One datasets, refer to the separate `all-in-one/README.md` for detailed descriptions and scripts.
