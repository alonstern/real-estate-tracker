import asyncio
from io import BytesIO

import joblib
import boto3

from parser import parse_mail
from response_email import send_response_email
from train_model import predict_price


def _load_model():
  s3_client = boto3.client('s3')
  with BytesIO() as f:
    s3_client.download_fileobj(Bucket='realestate-tracker-model', Key='model', Fileobj=f)
    f.seek(0)
    return joblib.load(f)


def main(event, context):
  message_id = event['Records'][0]['ses']['mail']['messageId']
  print(message_id)

  s3 = boto3.resource('s3')
  obj = s3.Object('realestate-tracker-mails', message_id)
  content = obj.get()['Body'].read().decode() 

  obj.delete()

  units_data = asyncio.run(parse_mail(content))

  model, vectorizer, scaler = _load_model()

  for unit_data, predicted_price in zip(units_data, predict_price(model, vectorizer, scaler, units_data)):
    round_predicated_price = round(predicted_price)
    unit_data['predicated_price'] = round_predicated_price
    unit_data['predicated_diff'] = unit_data['price'] - round_predicated_price

  dynamodb = boto3.resource('dynamodb')
  table = dynamodb.Table('realestate-units')

  with table.batch_writer() as batch:
    for unit_data in units_data:
        batch.put_item(Item=unit_data)

  send_response_email(units_data)

  print(f'Done - {len(units_data)} units')
