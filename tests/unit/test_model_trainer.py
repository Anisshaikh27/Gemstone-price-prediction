import numpy as np
import os
from src.components.model_trainer import ModelTrainer

def test_initate_model_training_creates_model_file(tmp_path):
    # Create dummy train and test arrays (10 samples, 5 features + 1 target)
    X_train = np.random.rand(10, 5)
    y_train = np.random.rand(10)
    X_test = np.random.rand(5, 5)
    y_test = np.random.rand(5)
    train_arr = np.column_stack((X_train, y_train))
    test_arr = np.column_stack((X_test, y_test))

    # Patch the model save path to a temp directory
    trainer = ModelTrainer()
    trainer.model_trainer_config.trained_model_file_path = os.path.join("artifacts", "model.pkl")

    trainer.initate_model_training(train_arr, test_arr)

    # Check if the model file was created
    assert os.path.exists(trainer.model_trainer_config.trained_model_file_path)