import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def plot_metric_correlation(csv_path, output_dir):
    df = pd.read_csv(csv_path)
    os.makedirs(output_dir, exist_ok=True)
    
    # PSNR vs NIQE
    sns.scatterplot(data=df, x="PSNR", y="NIQE")
    plt.savefig(os.path.join(output_dir, "psnr_vs_niqe.png"))
    plt.clf()
    
    # SSIM vs BRISQUE
    sns.scatterplot(data=df, x="SSIM", y="BRISQUE") 
    plt.savefig(os.path.join(output_dir, "ssim_vs_brisque.png"))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True)
    parser.add_argument("--output", default="figures/metric_charts")
    args = parser.parse_args()
    plot_metric_correlation(args.csv, args.output)
