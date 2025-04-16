import cv2
import numpy as np

def dark_channel(img, window_size=15):
    """Compute dark channel prior"""
    min_channel = np.min(img, axis=2)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (window_size, window_size))
    return cv2.erode(min_channel, kernel)

if __name__ == "__main__":
    import sys
    img = cv2.imread(sys.argv[1])
    result = dark_channel(img)
    cv2.imwrite("dark_channel.png", result)
