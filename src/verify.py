import os
import joblib
from preprocess import preprocess_image
from features import extract_features

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "smartsign_model.pkl")

def verify_signature(img_path):
    model = joblib.load(MODEL_PATH)

    img = preprocess_image(img_path)
    features = extract_features(img)

    result = model.predict([features])[0]

    if result == 1:
        return "Genuine Signature"
    else:
        return "Forged Signature"
