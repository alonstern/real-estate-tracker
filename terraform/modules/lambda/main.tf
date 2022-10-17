data "aws_iam_policy_document" "assume" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = [
      "sts:AssumeRole"
    ]
  }
}

resource "aws_iam_role" "lambda" {
  name               = "lambdaIam"
  assume_role_policy = data.aws_iam_policy_document.assume.json
}

data "aws_iam_policy_document" "lambda" {
  statement {
    effect = "Allow"

    actions = [
      "logs:CreateLogGroup",
      "logs:CreateLogStream",
      "logs:PutLogEvents"
    ]

    resources = ["*"]
  }

  statement {
    effect = "Allow"

    actions = [
      "ses:SendEmail",
      "ses:SendRawEmail"
    ]

    resources = ["*"]
  }

  statement {
    effect = "Allow"

    actions = [
      "s3:GetObject",
      "s3:DeleteObject"
    ]

    resources = ["${var.mails_bucket_arn}/*"]
  }

  statement {
    effect = "Allow"

    actions = [
      "s3:GetObject",
    ]

    resources = ["${var.model_bucket_arn}/*"]
  }

  statement {
    effect = "Allow"

    actions = [
      "dynamodb:BatchWriteItem",
    ]

    resources = [var.db_arn]
  }
}

resource "aws_iam_policy" "lambda" {
  name        = "lambdaPolicy"
  description = "Allow put logs, use s3 to store email and sent emails with SES"
  policy      = data.aws_iam_policy_document.lambda.json
}

resource "aws_iam_role_policy_attachment" "lambda" {
  role       = aws_iam_role.lambda.name
  policy_arn = aws_iam_policy.lambda.arn
}

locals {
  filename = "${path.module}/../../../_build/package.zip"
}

resource "aws_lambda_function" "lambda" {
  filename      = local.filename
  function_name = "lambda"
  role          = aws_iam_role.lambda.arn
  handler       = "main.main"

  source_code_hash = filebase64sha256(local.filename)

  layers = ["arn:aws:lambda:eu-west-1:399891621064:layer:AWSLambda-Python37-SciPy1x:115", "arn:aws:lambda:eu-west-1:680447875956:layer:Python37-SciKitLearnTest:2"]

  runtime = "python3.7"

  memory_size = 512

  timeout = 60
}