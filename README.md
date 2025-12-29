# Signature Verification System

This project is a **signature verification system** built with Python. It allows teachers or users to upload a signature image and automatically determine whether the signature is genuine. The system also includes a GUI for easy interaction.

---

## Features

- Detects if a signature is **genuine or forged**.
- GUI interface using **Tkinter** for selecting images.
- Uses **SVM classifier** trained on extracted signature features.
- Robust to small variations (blur, rotation, brightness) through **data augmentation**.

---

## Project Structure

sign/
│
├─ data/ # Folder for student signature images
│ ├─ student_01/
│ │ ├─ genuine/
│ │ └─ forged/
│ └─ student_02/ ...
│
├─ src/
│ ├─ dataset.py # Loads and augments dataset
│ ├─ train.py # Trains the SVM model
│ ├─ verify.py # Verifies a signature image
│ ├─ preprocess.py # Preprocessing functions
│ ├─ features.py # Feature extraction functions
│ └─ gui_verify.py # Tkinter GUI for verification
│
├─ smartsign_model.pkl # Trained SVM model (optional, not in repo)
Dependencies include: opencv-python, numpy, scikit-learn, Pillow.
