resource "aws_s3_bucket" "model" {
  bucket = "realestate-tracker-model"
}

resource "aws_s3_bucket_acl" "model" {
  bucket = aws_s3_bucket.model.id
  acl    = "private"
}

resource "aws_s3_object" "model" {
  bucket = aws_s3_bucket.model.id
  key    = "model"
  source = "${path.module}/../../../_build/model"
  source_hash = filemd5("${path.module}/../../../_build/model")
}