#!/bin/bash
echo "Downloading RainCityscapes..."
gdown https://drive.google.com/uc?id=1e7R76s6vwUJxILOcAsthgDLPSnOrQ49K -O datasets/deraining/RainCityscapes.zip
unzip datasets/deraining/RainCityscapes.zip -d datasets/deraining/
