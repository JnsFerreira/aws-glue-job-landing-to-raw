terraform {
  cloud {
    organization = "claropay"
    workspaces {
      name = "aws-glue-job-landing-to-raw-table-a"
    }
  }
}