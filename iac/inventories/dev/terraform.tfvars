environment = "dev"

name         = "my-dev-job"
description  = "This is my Glue Job on develop environment"
glue_version = "4.0"
command = {
  name            = "glueetl"
  script_location = "s3://my-dev-bucket/data_cleaning.py"
  python_version  = 3
}
tags = {
  "env": "develop"
}