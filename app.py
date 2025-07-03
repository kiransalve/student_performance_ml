import sys
from src.mlproject_1.exception import CustomException
from src.mlproject_1.logger import logging

if __name__ == "__main__":
    logging.info("The execution is started")

    try:
        a=1/0
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)