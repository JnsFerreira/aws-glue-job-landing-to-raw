variable "environment" {
  type        = string
  description = "Current execution environment"
  
  validation {
    condition     = contains(["dev", "hom", "prod"], var.environment)
    error_message = "Invalid environment. Must be on of the followin: `dev`, `hom` or `prod`"
  }
}

variable "name" {
  type        = string
  description = "Glue job name"
}

variable "description" {
  type        = string
  description = "Glue job description."
}

variable "glue_version" {
  type        = string
  description = "(Optional) The version of Glue to use."
}

variable "command" {
  type = object({
    name            = optional(string, null)
    script_location = optional(string, null)
    python_version  = number
  })
  description = "The command of the job."
}

variable "default_arguments" {
  type        = map(string)
  description = " (Optional) The map of default arguments for this job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes."
  default     = null
}

variable "tags" {
  type        = map(string)
  description = "Key-value mapping of resource tags"
}
