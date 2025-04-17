import cv2
import numpy as np
import os

def generate_comparison(gt_path, restored_path, output_path, text_labels=True):
    gt = cv2.imread(gt_path)
    res = cv2.imread(restored_path)
    comparison = np.hstack([gt, res])
    
    if text_labels:
        cv2.putText(comparison, f"GT: {os.path.basename(gt_path)}", (10,30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
        cv2.putText(comparison, f"Result: {os.path.basename(restored_path)}", 
                   (gt.shape[1]+10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
    
    cv2.imwrite(output_path, comparison)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--gt", required=True)
    parser.add_argument("--restored", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    generate_comparison(args.gt, args.restored, args.output)
