terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region  = "us-east-1"
  profile = "default"
}

terraform {
  backend "s3" {
    bucket = "fipe-project-infrastructure"
    key    = "terraform/terraform.tfstate"
    region = "us-east-1"
    profile = "default"
  }
}