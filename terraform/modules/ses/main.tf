resource "aws_ses_domain_identity" "realestate-tracker" {
  domain = "realestate-tracker.com"
}

resource "aws_ses_email_identity" "dest-email" {
  email = "alon.stern206@gmail.com"
}

resource "aws_ses_domain_dkim" "realestate-tracker" {
  domain = aws_ses_domain_identity.realestate-tracker.domain
}

resource "aws_ses_receipt_rule_set" "rules" {
  rule_set_name = "rules"
}

resource "aws_ses_active_receipt_rule_set" "rules" {
  rule_set_name = aws_ses_receipt_rule_set.rules.rule_set_name
}

resource "aws_ses_receipt_rule" "forward_lambda" {
  name          = "forward_lambda"
  rule_set_name = aws_ses_receipt_rule_set.rules.rule_set_name
  recipients    = ["scraper@realestate-tracker.com"]
  enabled       = true

  s3_action {
    bucket_name = var.mails_bucket_name
    position    = 1
  }

  lambda_action {
    function_arn = var.lambda_arn
    invocation_type = "Event"
    position = 2
  }
}

data "aws_caller_identity" "current" {}

resource "aws_lambda_permission" "allow_ses" {
  statement_id   = "AllowExecutionFromSES"
  action         = "lambda:InvokeFunction"
  function_name  = var.lambda_function_name
  source_account = data.aws_caller_identity.current.account_id
  principal      = "ses.amazonaws.com"
}