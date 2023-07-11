terraform {
  cloud {
    organization = "claropay"
    workspaces {
      name = "aws-glue-job-boilerplate"
    }
  }
}