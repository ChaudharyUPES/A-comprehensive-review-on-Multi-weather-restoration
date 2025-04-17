#!/bin/bash
echo "Downloading Snow100K..."
gdown https://drive.google.com/uc?id=1-t7Y4VjUq8IBIH1VX3RnXZfimYJLN9nW -O datasets/desnowing/Snow100K.zip
unzip datasets/desnowing/Snow100K.zip -d datasets/desnowing/
