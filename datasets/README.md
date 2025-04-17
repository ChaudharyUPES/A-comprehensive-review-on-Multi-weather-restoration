
# 🌦️ Multi-Weather Datasets

This section includes curated datasets for haze, rain, snow, and multi-weather conditions used in benchmarking image restoration models.

---

## 📥 Download Instructions

Each dataset has a download script that automatically fetches and organizes the files.

### 🔸 Dehazing
```bash
./dehazing/download_reside.sh
```

### 🔸 Deraining
```bash
./deraining/download_rain.sh
```

### 🔸 Desnowing
```bash
./desnowing/download_snow.sh
```

### 🔸 Multi-Weather Combined
```bash
./multi-weather/download_multi.sh
```

---

## ⚙️ Preprocessing Scripts

Some datasets may need preprocessing (e.g., resizing, formatting):

```bash
# Resize RainCityscapes images
python deraining/preprocess.py
```

---

## 📊 Dataset Statistics

| Dataset         | Type         | Samples | Resolution     |
|----------------|--------------|---------|----------------|
| RESIDE          | Hazy         | 13,990  | 620×460        |
| RainCityscapes  | Rainy        | 5,000   | 1920×1080      |
| Snow100K        | Snowy        | 100,000 | 1024×768       |
| All-Weather     | Multi-Cond   | 10,000  | Various        |

---

Place downloaded datasets in the following structure:

```plaintext
datasets/
├── dehazing/
├── deraining/
├── desnowing/
└── multi-weather/
```

> For more details on dataset licensing and citations, refer to each subfolder's `README.md`.
