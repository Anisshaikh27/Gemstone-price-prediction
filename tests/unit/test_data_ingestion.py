# tests/unit/test_data_ingestion.py - Updated for S3
import pytest
import os
import sys
import pandas as pd
from src.components.data_ingestion import DataIngestion

def test_initiate_data_ingestion():
    """Test data ingestion from S3 in CI/CD environment"""
    obj = DataIngestion()
    
    # This should now work with S3 data
    train_path, test_path = obj.initiate_data_ingestion()
    
    # Verify paths are returned
    assert train_path is not None
    assert test_path is not None
    
    # Verify files are created
    assert os.path.exists(train_path)
    assert os.path.exists(test_path)
    
    # Verify files have data
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    
    assert len(train_df) > 0
    assert len(test_df) > 0
    
    # Verify train/test split (approximately 70/30)
    total_rows = len(train_df) + len(test_df)
    train_ratio = len(train_df) / total_rows
    assert 0.65 < train_ratio < 0.75  # Allow some tolerance

def test_s3_data_download():
    """Test S3 data download functionality"""
    obj = DataIngestion()
    
    # Only test S3 download if in CI environment
    if os.getenv('CI') or os.getenv('GITHUB_ACTIONS'):
        data = obj.download_data_from_s3()
        assert data is not None
        assert len(data) > 0
        assert 'price' in data.columns  # Assuming price is your target column
