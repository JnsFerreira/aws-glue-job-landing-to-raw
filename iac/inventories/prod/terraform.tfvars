environment = "prod"
name         = "my-prod-job"
description  = "This is my Glue Job on production environment"
glue_version = "4.0"
command = {
  name            = "glueetl"
  script_location = "s3://my-prod-bucket/data_cleaning.py"
  python_version  = 3
}
tags = {
  "env": "production"
}