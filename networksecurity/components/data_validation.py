from networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH
from networksecurity.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.exception.exception import NetworkSecurityException 
from networksecurity.logger.logger import logging 
from networksecurity.utils.main_utils.utils import read_yaml_file,write_yaml_file
from scipy.stats import ks_2samp
import pandas as pd
import os,sys

class DataValidation:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    
    def validate_number_of_columns(self,dataframe:pd.DataFrame)->bool:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def is_numerical_column_exist(self,dataframe:pd.DataFrame)->bool:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
        
    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
            
    def detect_dataset_drift(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
                 
    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)