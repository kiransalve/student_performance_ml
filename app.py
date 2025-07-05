import sys
from src.mlproject_1.exception import CustomException
from src.mlproject_1.logger import logging
from src.mlproject_1.components.data_ingestion import DataIngestion
from src.mlproject_1.components.data_transformation import DataTransformationConfig, DataTransformation

if __name__ == "__main__":
    logging.info("The execution is started")

    try:
        data_ingestion = DataIngestion()
        train_data, test_data  = data_ingestion.initiate_data_ingestion()
        data_transformation = DataTransformation()
        data_transformation.initiate_data_transformation(train_data, test_data)

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)