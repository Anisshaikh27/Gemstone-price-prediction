import os
import importlib

def test_training_pipeline_creates_model(tmp_path, monkeypatch):
    # Patch the model save path to a temp directory if possible
    # (Assumes your pipeline allows setting output paths via config/env)
    # Otherwise, clean up after test

    # Import the pipeline module
    pipeline_module = importlib.import_module("src.pipeline.training_pipeline")

    # Path where your model is expected to be saved
    model_path = os.path.join("artifacts", "model.pkl")
    assert os.path.exists(model_path), "Model file was not created by the pipeline"