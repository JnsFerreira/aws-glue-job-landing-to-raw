import sys

from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from awsglue.dynamicframe import DynamicFrame


args = getResolvedOptions(sys.argv, ["JOB_NAME", "source_table", "output_path"])

source_table = args["source_table"]
output_path = args["output_path"]

glue_context = GlueContext(SparkContext.getOrCreate())


def read_from_source(database: str, table_name: str) -> DynamicFrame:
    """
    Reads data from source with dynamic frame using Glue Catalog

    Args:
        database (str): Glue database name
        table_name (str): Glue table name

    Returns:
        DynamicFrame: Data retrieved from Glue data catalog
    """
    return glue_context.create_dynamic_frame.from_catalog(
        database=database, table_name=table_name
    )


def apply_transformations(frame: DynamicFrame) -> DynamicFrame:
    """
    Apply needed transformations to dynamic frame

    Args:
        frame (DynamicFrame): Input frame to apply transformations

    Returns:
        DynamicFrame: Output frame with transformations applied
    """
    return frame


def write_to_destination(
    frame: DynamicFrame, output_path: str, connection_type: str, format: str
) -> None:
    """
    Writes a dynamic frame to a destination, like s3

    Args:
        frame (DynamicFrame):
        output_path (str):
        connection_type (str):
        format (str):

    Returns:
        None
    """
    glue_context.write_dynamic_frame.from_options(
        frame=frame,
        connection_type=connection_type,
        connection_options={"path": output_path},
        format=format,
    )


def main() -> None:
    """
    Executes the extract,transform and load steps
    """
    database, table_name = source_table.split(".")

    source_frame = read_from_source(database=database, table_name=table_name)

    transformed_frame = apply_transformations(frame=source_frame)

    write_to_destination(frame=transformed_frame)


if __name__ == "__main__":
    main()
