from textSummarizer.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)
from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from textSummarizer.pipeline.stage_03_data_transformation import (
    DataTransformationPipeline,
)


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
