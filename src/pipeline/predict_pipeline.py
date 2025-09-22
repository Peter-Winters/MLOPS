import sys
import pandas as pd
import numpy as np

from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

class PredictPipeline:
    def __init__(self, model_path: str, preprocessor_path: str):
        self.model_path = model_path
        self.preprocessor_path = preprocessor_path

    def predict(self, features: pd.DataFrame) -> np.ndarray:
        '''
        Function to make predictions on input features
        '''
        try:
            logging.info("Loading preprocessor and model")
            preprocessor = load_object(self.preprocessor_path) # load the preprocessor
            model = load_object(self.model_path) # load the model

            logging.info("Transforming features")
            data_scaled = preprocessor.transform(features) # transform the features

            logging.info("Making predictions")
            preds = model.predict(data_scaled) # make predictions

            return preds
         
        except Exception as e:
            logging.error("Error during prediction")
            raise CustomException(e, sys)
        

class CustomData:
    def __init__(self,
                 gender: str,
                 race_ethnicity: str,
                parental_level_of_education: str,
                lunch: str,
                test_preparation_course: str,
                reading_score: int,
                writing_score: int):
        
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score
    
    def get_data_as_dataframe(self) -> pd.DataFrame:
        '''
        Function to convert input data to pandas DataFrame
        '''
        try:
            logging.info("Converting input data to DataFrame")
            data = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "writing_score": [self.writing_score],
                "reading_score": [self.reading_score]
                
            }
            return pd.DataFrame(data)
        
        except Exception as e:
            logging.error("Error in converting data to DataFrame")
            raise CustomException(e, sys)