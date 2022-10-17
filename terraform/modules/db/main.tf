resource "aws_dynamodb_table" "realestate-units" {
  name           = "realestate-units"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "link"

  attribute {
    name = "link"
    type = "S"
  }
}