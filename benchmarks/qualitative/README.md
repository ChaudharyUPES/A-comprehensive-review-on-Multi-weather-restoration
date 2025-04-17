# Qualitative Evaluation Toolkit

## Usage

### Single Comparison
```bash
python visualize.py \
    --gt path/to/ground_truth.png \
    --restored path/to/restored.png \
    --output comparison.png

Batch Processing
'''bash
python compare.py \
    --gt datasets/ground_truth \
    --restored results/dehazing
    
Create Image Grids
'''bash
python tile_images.py \
    --input "results/*.png" \
    --cols 4 \
    --output results_grid.png
Metric Visualization
'''bash
python metrics_plot.py \
    --csv quantitative/results/metrics.csv
