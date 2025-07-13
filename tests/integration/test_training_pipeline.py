# tests/integration/test_training_pipeline.py - Updated for S3
import pytest
import os
import importlib

def test_training_pipeline_creates_model():
    """Test complete training pipeline with S3 data"""
    # This should now work with S3 data
    pipeline_module = importlib.import_module("src.pipeline.training_pipeline")
    
    # Verify model file is created
    model_path = "artifacts/model.pkl"
    assert os.path.exists(model_path)
    
    # Verify model file is not empty
    assert os.path.getsize(model_path) > 0

def test_prediction_pipeline():
    """Test prediction pipeline works with trained model"""
    from src.pipeline.prediction_pipeline import PredictPipeline, CustomData
    
    # Create sample data
    sample_data = CustomData(
        carat=1.0,
        depth=61.0,
        table=55.0,
        x=6.0,
        y=6.0,
        z=4.0,
        cut='Premium',
        color='E',
        clarity='VS1'
    )
    
    # Convert to DataFrame
    df = sample_data.get_data_as_dataframe()
    
    # Make prediction
    predict_pipeline = PredictPipeline()
    prediction = predict_pipeline.predict(df)
    
    # Verify prediction
    assert prediction is not None
    assert len(prediction) > 0
    assert prediction[0] > 0  # Price should be positive