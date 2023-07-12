import sys
import logging
from typing import Optional
from dataclasses import dataclass

from awsglue.job import Job
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from awsglue.dynamicframe import DynamicFrame


@dataclass
class LandingToRawJob:
    """
    Glue Job to move data from Landing zone to raw layer
    """
    job_name: str
    source_path: str
    source_format: str
    target_path: str
    target_format: str
    target_database: str
    target_table: str
    partition: str
    write_mode: Optional[str] = "append"
    log_level: Optional[int] = logging.INFO

    def __post_init__(self) -> None:
        """
        Post initializes needed parameters
        """
        self._logger = self.setup_logger()
        self._glue_context = GlueContext(SparkContext.getOrCreate())
        self._job = Job(self._glue_context)

    def setup_logger(self):
        """
        Configure a logger to be used
        """
        logging.basicConfig(
            format='%(asctime)s %(levelname)s %(name)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            level=self.log_level,
            force=True
        )
        
        return logging.getLogger()

    def read_from_s3_source(self) -> DynamicFrame:
        """
        Reads data from source with dynamic frame using Glue Catalog
        """
        self._logger.info(f"Reading data from {self.source_path} ...")

        return self._glue_context.create_dynamic_frame.from_options(
            connection_type="s3", 
            connection_options={"path": [self.source_path]}, 
            format=self.source_format,
            transformation_ctx=f"datasource_{self.job_name}"
        )

    def write_to_destination(self, frame: DynamicFrame) -> None:
        """
        Writes a dynamic frame to a destination, like s3

        Args:

        """
        table_reference = f"{self.target_database}.{self.target_table}"

        dataframe = frame.toDF()
        dataframe.write \
            .format(self.target_format) \
            .options(path=self.target_) \
            .mode(self.write_mode) \
            .partitionBy(self.partition) \
            .saveAsTable(table_reference)

    def execute(self) -> None:
        """Executes the entire job"""
        self._logger.info(f"Initialing job {self.job_name} ...")
        self._job.init(self.job_name)

        source_frame = self.read_from_s3_source()
        self.write_to_destination(frame=source_frame)

        self._job.commit()
        self._logger.info("Job completed successfully!")



def main(args) -> None:
    """
    Executes the extract,transform and load steps
    """
    job = LandingToRawJob(
        job_name=args["JOB_NAME"],
        source_path=args["source_path"],
        source_format=args["source_format"],
        target_path=args["target_path"],
        target_format=args["target_format"],
        target_database=args["target_database"],
        target_table=args["target_table"],
        partition=args["partition"],
    )
    
    job.execute()


if __name__ == "__main__":
    required_args = [
        "JOB_NAME",
        "source_path",
        "source_format",
        "target_path",
        "target_format",
        "target_database",
        "target_table",
        "partition",
    ]

    args = getResolvedOptions(sys.argv, required_args)

    main(args)
