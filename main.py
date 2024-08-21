from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)
from textSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from textSummarizer.pipeline.stage_03_data_transformation import (
    DataTransformationPipeline,
)
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerPipeline


STAGE_NAME = "DATA INGESTION STAGE"

try:
    logger.info(f"{STAGE_NAME} STARTED")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"{STAGE_NAME} ENDED")
except Exception as e:
    raise e


STAGE_NAME = "DATA VALIDATION STAGE"

try:
    logger.info(f"{STAGE_NAME} STARTED")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f"{STAGE_NAME} ENDED")
except Exception as e:
    raise e


STAGE_NAME = "DATA TRANSFORMATION STAGE"

try:
    logger.info(f"{STAGE_NAME} STARTED")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f"{STAGE_NAME} ENDED")
except Exception as e:
    raise e


STAGE_NAME = "MODEL TRAINER STAGE"

try:
    logger.info(f"{STAGE_NAME} STARTED")
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f"{STAGE_NAME} ENDED")
except Exception as e:
    raise e

STAGE_NAME = "MODEL EVALUATION STAGE"

try:
    logger.info(f"{STAGE_NAME} STARTED")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(f"{STAGE_NAME} ENDED")
except Exception as e:
    raise e
