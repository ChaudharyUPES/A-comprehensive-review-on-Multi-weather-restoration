from piq import niqe
import cv2

def calculate_niqe(image_path):
    img = cv2.imread(image_path)
    return niqe(img)
