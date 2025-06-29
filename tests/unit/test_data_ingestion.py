import os
from src.components.data_ingestion import DataIngestion

def test_initiate_data_ingestion():
    obj = DataIngestion()
    train_path, test_path = obj.initiate_data_ingestion()
    assert os.path.exists(train_path), "Train data file does not exist"
    assert os.path.exists(test_path), "Test data file does not exist"