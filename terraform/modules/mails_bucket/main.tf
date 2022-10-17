resource "aws_s3_bucket" "mails" {
  bucket = "realestate-tracker-mails"
}

resource "aws_s3_bucket_acl" "mails" {
  bucket = aws_s3_bucket.mails.id
  acl    = "private"
}

data "aws_caller_identity" "current" {}

data "aws_iam_policy_document" "s3" {
  statement {
    sid = "GiveSESPermissionToWriteEmail"

    effect = "Allow"

    principals {
      identifiers = ["ses.amazonaws.com"]
      type        = "Service"
    }

    actions = ["s3:PutObject"]

    resources = ["${aws_s3_bucket.mails.arn}/*"]

    condition {
      test     = "StringEquals"
      values   = [data.aws_caller_identity.current.account_id]
      variable = "aws:Referer"
    }
  }
}

resource "aws_s3_bucket_policy" "default" {
  bucket = aws_s3_bucket.mails.id
  policy = data.aws_iam_policy_document.s3.json
}
