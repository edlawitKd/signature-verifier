import cv2
import os
import numpy as np

def preprocess_image(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Cannot open image: {img_path}")
    img = cv2.resize(img, (200, 100))
    img = img / 255.0
    return img
