import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

def calculate_psnr(gt, restored):
    mse = np.mean((gt - restored) ** 2)
    return 10 * np.log10((255**2) / mse)

def calculate_ssim(gt, restored):
    return ssim(gt, restored, multichannel=True, channel_axis=2)
