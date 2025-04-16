#!/usr/bin/env python3
"""
Usage:
  For reference metrics: python evaluate.py --ref --gt PATH --restored PATH
  For non-reference: python evaluate.py --no-ref --restored PATH
"""

import argparse
from reference.psnr_ssim import calculate_psnr, calculate_ssim
from non_reference.niqe import calculate_niqe
import pandas as pd
from pathlib import Path

def evaluate(args):
    metrics = []
    for img_path in Path(args.restored).glob("*.*"):
        entry = {"image": img_path.name}
        
        if args.ref:
            gt_path = Path(args.gt)/img_path.name
            gt = cv2.imread(str(gt_path))
            res = cv2.imread(str(img_path))
            
            entry.update({
                "PSNR": calculate_psnr(gt, res),
                "SSIM": calculate_ssim(gt, res)
            })
        
        if args.no_ref:
            entry.update({
                "NIQE": calculate_niqe(str(img_path)),
                "BRISQUE": calculate_brisque(str(img_path))
            })
            
        metrics.append(entry)
    
    pd.DataFrame(metrics).to_csv("results/metrics.csv", index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--ref", action="store_true")
    group.add_argument("--no-ref", action="store_true")
    parser.add_argument("--gt", help="Ground truth path")
    parser.add_argument("--restored", required=True)
    args = parser.parse_args()
    evaluate(args)
