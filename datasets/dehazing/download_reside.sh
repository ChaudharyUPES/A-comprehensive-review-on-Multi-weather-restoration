#!/bin/bash
echo "Downloading RESIDE datasets..."
wget https://sites.google.com/view/reside-dehaze-datasets/reside-standard.zip -P datasets/dehazing/RESIDE/
unzip datasets/dehazing/RESIDE/reside-standard.zip -d datasets/dehazing/RESIDE/
