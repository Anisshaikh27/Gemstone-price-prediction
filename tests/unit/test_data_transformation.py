import numpy as np
from src.components.data_transformation import DataTransformation

def test_initialize_data_transformation():
    transformer = DataTransformation()
    train_arr, test_arr = transformer.initialize_data_transformation("artifacts/train.csv", "artifacts/test.csv")
    assert isinstance(train_arr, np.ndarray), "Train array is not a numpy array"
    assert isinstance(test_arr, np.ndarray), "Test array is not a numpy array"
    assert train_arr.shape[1] == test_arr.shape[1], "Train and test arrays have different number of columns"