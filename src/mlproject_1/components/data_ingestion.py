import os
import sys
from src.mlproject_1.exception import CustomException
from src.mlproject_1.logger import logging
import pandas as pd
from dataclasses import dataclass
from src.mlproject_1.utils import read_sql_data
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join("artifacts", "train.csv")
    test_data_path = os.path.join("artifacts", "test.csv")
    raw_data_path = os.path.join("artifacts", "raw.csv")

    
class DataIngestion:
    """
    This class handles the ingestion of data from a SQL database.
    It saves raw, train, and test datasets as CSV files.
    """    
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        try:
            df = read_sql_data()
            logging.info("Reading completed mysql database")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info(f"Raw data saved at {self.ingestion_config.raw_data_path}")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False)
            logging.info(f"Train data saved at {self.ingestion_config.train_data_path}, shape: {train_set.shape}")

            test_set.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info(f"Test data saved at {self.ingestion_config.test_data_path}, shape: {test_set.shape}")

            logging.info("Data Ingestion is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)