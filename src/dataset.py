import os
import cv2
import numpy as np
from preprocess import preprocess_image
from features import extract_features

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(BASE_DIR, "data")

print("BASE_DIR:", BASE_DIR)
print("DATA_DIR:", data_dir)

X = []
y = []

if not os.path.exists(data_dir):
    print("❌ data folder NOT FOUND")
else:
    print("✅ data folder found")

# --- Augmentation function ---
def augment_image(img):
    # Slight rotation
    rows, cols = img.shape
    angle = np.random.uniform(-5, 5)
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    img = cv2.warpAffine(img, M, (cols, rows))

    # Add Gaussian blur occasionally
    if np.random.rand() > 0.5:
        img = cv2.GaussianBlur(img, (3, 3), 0)

    # Slight brightness change
    factor = np.random.uniform(0.9, 1.1)
    img = np.clip(img * factor, 0, 255).astype(np.uint8)

    return img

# --- Load images and extract features ---
for student in os.listdir(data_dir):
    student_path = os.path.join(data_dir, student)
    print("\nFound:", student_path)

    if not os.path.isdir(student_path):
        print("  ⛔ Not a folder, skipping")
        continue

    genuine_path = os.path.join(student_path, "genuine")
    forged_path = os.path.join(student_path, "forged")

    print("  Genuine path:", genuine_path)
    print("  Forged path:", forged_path)

    # Genuine signatures
    if os.path.exists(genuine_path):
        for img_file in os.listdir(genuine_path):
            img_path = os.path.join(genuine_path, img_file)
            img = preprocess_image(img_path)
            features = extract_features(img)
            X.append(features)
            y.append(1)

            # Augmented image
            aug_img = augment_image(img * 255)  # undo normalization
            aug_img = aug_img / 255.0           # normalize again
            aug_features = extract_features(aug_img)
            X.append(aug_features)
            y.append(1)
            print("    Loaded and augmented genuine:", img_file)
    else:
        print("    ❌ genuine folder missing")

    # Forged signatures
    if os.path.exists(forged_path):
        for img_file in os.listdir(forged_path):
            img_path = os.path.join(forged_path, img_file)
            img = preprocess_image(img_path)
            features = extract_features(img)
            X.append(features)
            y.append(0)

            # Augmented image
            aug_img = augment_image(img * 255)
            aug_img = aug_img / 255.0
            aug_features = extract_features(aug_img)
            X.append(aug_features)
            y.append(0)
            print("    Loaded and augmented forged:", img_file)
    else:
        print("    ❌ forged folder missing")

print("\nTOTAL samples loaded (including augmentations):", len(X))
