import os

TRAINING_BUCKET_NAME = "mynetworksecurity"
SAVED_MODEL_DIR =os.path.join("saved_models")
PIPELINE_NAME: str="NetworkSecurity"
ARTIFACT_DIR:str="Artifacts"
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str= "feature_store"
FILE_NAME:str="NetworkData.csv"
DATA_INGESTION_INGESTED_DIR:str="ingested"
TEST_FILE_NAME:str="test.csv"
TRAIN_FILE_NAME:str="train.csv"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION:float=0.2
DATA_INGESTION_COLLECTION_NAME:str="NetworkData"
DATA_INGESTION_DATABASE_NAME:str="KNAcademy"

"""
Data Validation related constant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"   
