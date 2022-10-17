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
  region  = "eu-west-1"
  profile = "Alon"
}

module "mails_bucket" {
  source = "./modules/mails_bucket"
}

module "model_bucket" {
  source = "./modules/model_bucket"
}

module "db" {
  source = "./modules/db"
}

module "lambda" {
  source = "./modules/lambda"
  mails_bucket_arn = module.mails_bucket.bucket_arn
  model_bucket_arn = module.model_bucket.bucket_arn
  db_arn = module.db.db_arn
}

module "ses" {
  source = "./modules/ses"
  lambda_arn = module.lambda.lambda_arn
  lambda_function_name = module.lambda.lambda_function_name
  mails_bucket_name = module.mails_bucket.bucket_name
}
