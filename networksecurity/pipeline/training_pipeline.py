import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

from networksecurity.components import DataIngestion
from networksecurity.components import DataValidation
from networksecurity.components import DataTransformation
from networksecurity.components import ModelTrainer
from networksecurity.components import ModelEvaluation
from networksecurity.components import ModelPusher

from networksecurity.entity.config_entity import(
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig,
    ModelPusherConfig
   
)

from networksecurity.entity.artifact_entity import (
    DataIngestionArtifact,
    DataValidationArtifact,
    DataTransformationArtifact,
    ModelTrainerArtifact,
    ModelEvaluationArtifact,
    ModelPusherArtifact
)

from networksecurity.cloud.s3_syncer import S3Sync
from networksecurity.constant.training_pipeline import TRAINING_BUCKET_NAME
from networksecurity.constant.training_pipeline import SAVED_MODEL_DIR

class TrainingPipeline:
    def __init__(self):
        pass

    def run_pipeline(self):
        pass

