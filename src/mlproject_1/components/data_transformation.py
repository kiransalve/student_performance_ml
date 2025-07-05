import sys
import os

from dataclasses import dataclass

import numpy as np
import pandas as pd

from sklearn.preprocessing import OneHotEncoder , StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from src.mlproject_1.utils import save_object
from src.mlproject_1.exception import CustomException
from src.mlproject_1.logger import logging

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_object(self):
        """
        this function is responsible for data transformation
        1. Save numerical and categorical feature separately
        2. For Numerical we use StandardScaler
        3. For Categorical we use OneHotEncoder
        4. Pipeline for missing values
        """
        try:
            cat_cols = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']
            num_cols = ['reading_score', 'writing_score']
            
            num_pipline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )
            
            logging.info(f"Categorical columns {cat_cols}")
            logging.info(f"Numerical columns {num_cols}")

            preprocessor = ColumnTransformer([
                ("num_pipeline", num_pipline, num_cols),
                ("cat_pipeline", cat_pipeline, cat_cols),
            ])

            return preprocessor
        
        except Exception as e:
            raise CustomException(sys, e)
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df  = pd.read_csv(train_path) 
            test_df = pd.read_csv(test_path)
            logging.info("Reading the train and test file")

            preprocessing_obj = self.get_data_transformation_object()
            target_column_name = "math_score"
            cat_cols = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']
            num_cols = ['reading_score', 'writing_score']

            # divide the train dataset to independant and dependant features
            input_features_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_features_train_df = train_df[target_column_name]

            # divide the test dataset to independant and dependant features
            input_features_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_features_test_df = test_df[target_column_name]

            logging.info("Applying preprocessing train and test database.")

            input_feature_train_arr = preprocessing_obj.fit_transform(input_features_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_features_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_features_train_df)]    
            test_arr = np.c_[input_feature_test_arr, np.array(target_features_test_df)]    

            logging.info(f"Saved preprocessing object")

            save_object(file_path=self.data_transformation_config.preprocessor_obj_file_path, obj=preprocessing_obj)

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        except Exception as e:
            raise CustomException(sys, e)
        