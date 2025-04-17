# Multi-Weather Datasets

## Download Instructions
```bash
# Dehazing
./dehazing/download_reside.sh

# Deraining
./deraining/download_rain.sh

# Desnowing
./desnowing/download_snow.sh

# Multi-weather
./multi-weather/download_multi.sh
### Preprocessing
# Example: Resize RainCityscapes images
python deraining/preprocess.py
Statistics
Dataset	Type	Samples	Resolution
RESIDE	Hazy	13,990	620×460
RainCityscapes	Rainy	5,000	1920×1080
Snow100K	Snowy	100,000	1024×768
All-Weather	Multi-Cond	10,000	Various
