# Signature Verification System

This project is a **signature verification system** built with Python. It allows teachers or users to upload a signature image and automatically determine whether the signature is genuine. The system also includes a GUI for easy interaction.

---

## Features

- Detects if a signature is **genuine or forged**.
- GUI interface using **Tkinter** for selecting images.
- Uses **SVM classifier** trained on extracted signature features.
- Robust to small variations (blur, rotation, brightness) through **data augmentation**.

---

## Install dependencies:

Dependencies include: opencv-python, numpy, scikit-learn, Pillow.
