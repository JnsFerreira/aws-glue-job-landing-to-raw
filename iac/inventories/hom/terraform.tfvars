environment = "hom"
name         = "my-hom-job"
description  = "This is my Glue Job on homolog environment"
glue_version = "4.0"
command = {
  name            = "glueetl"
  script_location = "s3://my-hom-bucket/data_cleaning.py"
  python_version  = 3
}
tags = {
  "env": "homolog"
}