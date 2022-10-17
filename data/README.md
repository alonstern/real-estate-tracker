# Generating the data

To generate the training data from the DynamoDB table run:

aws dynamodb scan --table-name=realestate-units --output json > training_data.json