from piq import brisque
import cv2

def calculate_brisque(image_path):
    img = cv2.imread(image_path)
    return brisque(img)
