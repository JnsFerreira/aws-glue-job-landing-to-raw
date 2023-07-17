environment = "prod"

name         = "landing-to-raw-table-a-prod"
description  = "Glue job to move table A data from landing zone to raw"
glue_version = "4.0"

default_arguments = {
  "--spark-conf" = "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension"
  "--spark-conf" = "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"
}
command = {
  name            = "glueetl"
  script_location = "s3://claropay-prod-pipeline-assets/glue/landing2raw/job.py"
  python_version  = 3
}
tags = {
  "env": "prod"
}
