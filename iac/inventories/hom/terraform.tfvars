environment = "uat"

name         = "landing-to-raw-table-a-uat"
description  = "Glue job to move table A data from landing zone to raw"
glue_version = "4.0"

default_arguments = {
  "--spark-conf"      = "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension"
  "--spark-conf"      = "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"
  "--source_path"     = "s3://claropay-uat-landing-zone/domain/table"
  "--source_format"   = "json"
  "--target_path"     = "s3://claropay-uat-raw-layer/domain/table"
  "--target_format"   = "delta"
  "--target_database" = "claropay-uat-raw"
  "--target_table"    = "table_a"
  "--partition"       = "date"
}
command = {
  name            = "glueetl"
  script_location = "s3://claropay-uat-pipeline-assets/glue/landing2raw/job.py"
  python_version  = 3
}
tags = {
  "env": "uat"
}
