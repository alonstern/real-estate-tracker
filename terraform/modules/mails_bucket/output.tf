output "bucket_name" {
  value = aws_s3_bucket.mails.bucket
}

output "bucket_arn" {
  value = aws_s3_bucket.mails.arn
}
