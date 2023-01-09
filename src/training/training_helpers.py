import os

import joblib


def save_model(model):
    target_directory = "artifacts"
    os.makedirs(target_directory, exist_ok=True)
    joblib.dump(model, f"{target_directory}/pipeline.joblib")


def load_model():
    target_directory = "artifacts"
    model = joblib.load(f"{target_directory}/pipeline.joblib")

    return model
