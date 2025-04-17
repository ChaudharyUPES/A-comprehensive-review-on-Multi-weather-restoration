import cv2
import numpy as np
import math
import glob
import argparse

def make_grid(image_paths, output_path, cols=4, target_size=(256,256)):
    images = [cv2.resize(cv2.imread(p), target_size) for p in image_paths]
    rows = math.ceil(len(images)/cols)
    
    grid = np.vstack([
        np.hstack(images[i*cols : (i+1)*cols]) 
        for i in range(rows)
    ])
    
    cv2.imwrite(output_path, grid)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Glob pattern for images")
    parser.add_argument("--output", required=True)
    parser.add_argument("--cols", type=int, default=4)
    args = parser.parse_args()
    
    image_paths = sorted(glob.glob(args.input))
    make_grid(image_paths, args.output, args.cols)
