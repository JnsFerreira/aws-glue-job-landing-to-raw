locals {
  iam_policy = file("iac/iam/policies/${var.environment}/policy.json")
}

module "glue_job" {
  source = "git::https://github.com/JnsFerreira/terraform-module-aws-glue-job?ref=v1.0.0"

  name         = var.name
  description  = var.description
  iam_policy   = local.iam_policy
  glue_version = var.glue_version
  command      = var.command
  tags         = var.tags
}
