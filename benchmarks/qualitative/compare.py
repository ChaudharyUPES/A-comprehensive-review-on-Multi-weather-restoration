import os
from visualize import generate_comparison
from pathlib import Path

def batch_compare(gt_dir, restored_dir, output_dir="figures/comparisons"):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    for img_path in Path(gt_dir).glob("*.*"):
        gt_path = str(img_path)
        res_path = str(Path(restored_dir)/img_path.name)
        
        if Path(res_path).exists():
            output_path = str(Path(output_dir)/f"comp_{img_path.name}")
            generate_comparison(gt_path, res_path, output_path)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--gt", required=True)
    parser.add_argument("--restored", required=True)
    parser.add_argument("--output", default="figures/comparisons")
    args = parser.parse_args()
    batch_compare(args.gt, args.restored, args.output)
