
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str

class DataValidationArtifact:
    validation_status: bool
    valid_train_file_path: str
    valid_test_file_path: str
    invalid_train_file_path: str
    invalid_test_file_path: str
    drift_report_file_path: str

class DataTransformationArtifact:
    def __init__(self):
        pass



class ClassificationMetricArtifact:
    def __init__(self):
        pass

class ModelTrainerArtifact:
    def __init__(self):
        pass

class ModelEvaluationArtifact:
    def __init__(self):
        pass

class ModelPusherArtifact:
    def __init__(self):
        pass