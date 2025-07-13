# src/components/data_ingestion.py
import os
import sys
import pandas as pd
import boto3
from io import StringIO
from dataclasses import dataclass
from src.exception.exception import customexception
from src.logger.logging import logging
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def download_data_from_s3(self):
        """
        Download CSV data from S3 using API keys
        """
        try:
            # Get AWS credentials from environment variables
            aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
            aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
            aws_region = os.getenv('AWS_DEFAULT_REGION', 'us-east-1')
            s3_bucket_name = os.getenv('S3_BUCKET_NAME')
            s3_file_key = os.getenv('S3_FILE_KEY', 'gemstone.csv')
            
            if not all([aws_access_key_id, aws_secret_access_key, s3_bucket_name]):
                raise ValueError("Missing required AWS credentials or S3 bucket configuration")
            
            # Create S3 client
            s3_client = boto3.client(
                's3',
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
                region_name=aws_region
            )
            
            # Download file from S3
            logging.info(f"Downloading data from S3 bucket: {s3_bucket_name}/{s3_file_key}")
            obj = s3_client.get_object(Bucket=s3_bucket_name, Key=s3_file_key)
            data = pd.read_csv(obj['Body'])
            
            logging.info("Data successfully downloaded from S3")
            return data
            
        except Exception as e:
            logging.error(f"Error downloading data from S3: {str(e)}")
            raise customexception(e, sys)
    
    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")
        try:
            # Check if running in CI/CD or production environment
            if os.getenv('CI') or os.getenv('GITHUB_ACTIONS') or os.getenv('RENDER'):
                # Download from S3
                data = self.download_data_from_s3()
            else:
                # For local development, try to read from local file
                local_data_path = os.path.join("data", "gemstone.csv")
                if os.path.exists(local_data_path):
                    data = pd.read_csv(local_data_path)
                else:
                    # Fallback to S3 for local development too
                    logging.info("Local data file not found, downloading from S3")
                    data = self.download_data_from_s3()
            
            logging.info("Read dataset as pandas DataFrame")
            
            # Create artifacts directory
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            
            # Save raw data
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Raw data saved")
            
            # Split data
            train_set, test_set = train_test_split(data, test_size=0.30, random_state=42)
            
            # Save train and test sets
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            
            logging.info("Data ingestion completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
        except Exception as e:
            logging.error(f"Error in data ingestion: {str(e)}")
            raise customexception(e, sys)
        

if __name__ == '__main__':
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()