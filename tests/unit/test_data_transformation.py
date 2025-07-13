# tests/unit/test_data_transformation.py - Updated for S3
import pytest
import os
import numpy as np
from src.components.data_transformation import DataTransformation
from src.components.data_ingestion import DataIngestion

def test_initialize_data_transformation():
    """Test data transformation with S3 data"""
    # First, ensure we have data
    ingestion = DataIngestion()
    train_path, test_path = ingestion.initiate_data_ingestion()
    
    # Now test transformation
    transformer = DataTransformation()
    train_arr, test_arr = transformer.initialize_data_transformation(train_path, test_path)
    
    # Verify arrays are created
    assert train_arr is not None
    assert test_arr is not None
    
    # Verify shapes
    assert len(train_arr.shape) == 2
    assert len(test_arr.shape) == 2
    
    # Verify data types
    assert train_arr.dtype in [np.float64, np.float32]
    assert test_arr.dtype in [np.float64, np.float32]
