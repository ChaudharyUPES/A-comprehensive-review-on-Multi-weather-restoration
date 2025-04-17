import cv2
import os

def resize_images(input_dir, output_dir, size=(1024, 768)):
    os.makedirs(output_dir, exist_ok=True)
    for img_name in os.listdir(input_dir):
        img = cv2.imread(os.path.join(input_dir, img_name))
        resized = cv2.resize(img, size)
        cv2.imwrite(os.path.join(output_dir, img_name), resized)

if __name__ == "__main__":
    resize_images("datasets/deraining/RainCityscapes/rain", 
                 "datasets/deraining/RainCityscapes/rain_resized")
