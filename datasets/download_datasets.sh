#!/bin/bash
# Automated dataset download script

echo "Downloading RESIDE dataset..."
wget https://sites.google.com/view/reside-dehaze-datasets/reside-standard.zip -P datasets/dehazing/RESIDE/
unzip datasets/dehazing/RESIDE/reside-standard.zip -d datasets/dehazing/RESIDE/

echo "Downloading Snow100K..."
gdown https://drive.google.com/uc?id=1-t7Y4VjUq8IBIH1VX3RnXZfimYJLN9nW -O datasets/desnowing/Snow100K.zip
unzip datasets/desnowing/Snow100K.zip -d datasets/desnowing/

echo "Download complete!"
