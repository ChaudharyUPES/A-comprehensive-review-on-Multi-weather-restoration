#!/bin/bash
echo "Downloading All-Weather dataset..."
gdown https://drive.google.com/uc?id=1SN6cg9L8y6pZ7i9QZSoN0tHvJ-JJYYnU -O datasets/multi-weather/All-Weather.zip
unzip datasets/multi-weather/All-Weather.zip -d datasets/multi-weather/
