from textSummarizer.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)
from textSummarizer.logging import logger


STAGE_NAME = "DATA INGESTION STAGE"

try:
    logger.info(f"{STAGE_NAME} STARTED")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"{STAGE_NAME} ENDED")
except Exception as e:
    raise e
